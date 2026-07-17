#!/usr/bin/env python3
"""Fetch, validate, and atomically stage the Ravenis public data release."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import tarfile
from pathlib import Path
from typing import Any

try:
    import boto3
    from botocore.config import Config as BotoConfig
except ImportError:  # pragma: no cover - installed by the deployment workflow
    boto3 = None
    BotoConfig = None


POINTER_FIELDS = {
    "schema_version", "run_id", "generated_at", "object_key", "sha256",
    "size", "retention_days", "files",
}
PUBLIC_RECORD_FIELDS = {
    "id", "short_id", "date", "type", "title", "source", "source_count",
    "url", "category", "tags", "score", "first_seen", "last_seen",
    "occurrence_count", "summary",
}
FORBIDDEN_KEYS = {
    "full_text", "raw_payload", "raw_response", "prompt", "messages", "content",
    "playbook", "significance", "observation", "source_urls", "private_config",
    "sqlite", "database",
}
RELEASE_KEY_RE = re.compile(r"^history/releases/[A-Za-z0-9._-]+\.tar\.gz$")
DAY_PATH_RE = re.compile(r"^days/\d{4}-\d{2}-\d{2}\.json$")
MAX_RELEASE_BYTES = 64 * 1024 * 1024
MAX_MEMBER_BYTES = 16 * 1024 * 1024


def json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def validate_pointer(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != POINTER_FIELDS:
        raise ValueError("Ravenis current pointer has an unexpected shape")
    if value.get("schema_version") != 1:
        raise ValueError("unsupported Ravenis pointer schema")
    if not RELEASE_KEY_RE.fullmatch(str(value.get("object_key") or "")):
        raise ValueError("Ravenis release object key is outside the immutable prefix")
    digest = str(value.get("sha256") or "").lower()
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise ValueError("Ravenis release SHA-256 is invalid")
    files = value.get("files")
    if not isinstance(files, list) or not files or len(files) != len(set(files)):
        raise ValueError("Ravenis pointer file list is invalid")
    required = {"manifest.json", "search-index.json", "weekly/latest.json"}
    if not required.issubset(files) or not all(name in required or DAY_PATH_RE.fullmatch(name) for name in files):
        raise ValueError("Ravenis pointer contains an unexpected path")
    if int(value.get("size") or 0) <= 0 or int(value["size"]) > MAX_RELEASE_BYTES:
        raise ValueError("Ravenis release size is invalid")
    if not 1 <= int(value.get("retention_days") or 0) <= 31:
        raise ValueError("Ravenis retention window is invalid")
    return value


def reject_forbidden_keys(value: Any, trail: str = "root") -> None:
    if isinstance(value, dict):
        forbidden = set(value) & FORBIDDEN_KEYS
        if forbidden:
            raise ValueError(f"forbidden public field at {trail}: {sorted(forbidden)}")
        for key, child in value.items():
            reject_forbidden_keys(child, f"{trail}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_forbidden_keys(child, f"{trail}[{index}]")


def validate_records(items: Any, *, search: bool = False) -> None:
    if not isinstance(items, list):
        raise ValueError("Ravenis public records are not a list")
    allowed = PUBLIC_RECORD_FIELDS | ({"slots"} if search else set())
    for item in items:
        if not isinstance(item, dict) or set(item) - allowed:
            raise ValueError("Ravenis public record contains unknown fields")
        if not str(item.get("id") or "").strip() or not str(item.get("title") or "").strip():
            raise ValueError("Ravenis public record lacks id/title")
        url = str(item.get("url") or "").strip()
        if url and not re.match(r"^https?://", url, re.IGNORECASE):
            raise ValueError("Ravenis public record contains an unsafe URL")


def validate_release(pointer_value: Any, payload: bytes) -> tuple[dict[str, Any], dict[str, bytes]]:
    pointer = validate_pointer(pointer_value)
    if len(payload) != int(pointer["size"]):
        raise ValueError("Ravenis release size does not match its pointer")
    if hashlib.sha256(payload).hexdigest() != pointer["sha256"]:
        raise ValueError("Ravenis release SHA-256 does not match its pointer")

    files: dict[str, bytes] = {}
    total = 0
    try:
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:gz") as archive:
            for member in archive.getmembers():
                name = member.name.replace("\\", "/")
                if not member.isfile() or name.startswith(("/", "../")) or "/../" in name:
                    raise ValueError("Ravenis archive contains an unsafe member")
                if name not in pointer["files"] or member.size > MAX_MEMBER_BYTES:
                    raise ValueError("Ravenis archive member is unexpected or too large")
                total += member.size
                if total > MAX_RELEASE_BYTES:
                    raise ValueError("Ravenis archive expands beyond its safety limit")
                stream = archive.extractfile(member)
                if stream is None:
                    raise ValueError("Ravenis archive member cannot be read")
                files[name] = stream.read()
    except tarfile.TarError as exc:
        raise ValueError(f"Ravenis release is not a valid tar.gz: {exc}") from exc
    if set(files) != set(pointer["files"]):
        raise ValueError("Ravenis archive and pointer file lists differ")

    decoded: dict[str, Any] = {}
    for name, body in files.items():
        try:
            decoded[name] = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError(f"Ravenis release JSON is invalid: {name}") from exc
        reject_forbidden_keys(decoded[name], name)

    manifest = decoded["manifest.json"]
    search = decoded["search-index.json"]
    if not isinstance(manifest, dict) or not isinstance(manifest.get("days"), list) or not manifest["days"]:
        raise ValueError("Ravenis manifest is empty or invalid")
    if manifest.get("search", {}).get("path") != "search-index.json":
        raise ValueError("Ravenis manifest search path is invalid")
    expected_search_hash = str(manifest.get("search", {}).get("sha256") or "")
    if expected_search_hash != hashlib.sha256(files["search-index.json"]).hexdigest():
        raise ValueError("Ravenis search index hash is invalid")
    expected_days = {entry.get("path") for entry in manifest["days"] if isinstance(entry, dict)}
    if expected_days != {name for name in files if DAY_PATH_RE.fullmatch(name)}:
        raise ValueError("Ravenis manifest day list does not match the archive")
    validate_records(search.get("items") if isinstance(search, dict) else None, search=True)
    for name in expected_days:
        day = decoded[name]
        if not isinstance(day, dict) or not isinstance(day.get("runs"), list):
            raise ValueError(f"Ravenis day shard is invalid: {name}")
        validate_records(day.get("items"))
    return pointer, files


def make_s3_client():
    required = (
        "RAVENIS_R2_BUCKET", "RAVENIS_R2_ACCESS_KEY_ID",
        "RAVENIS_R2_SECRET_ACCESS_KEY", "RAVENIS_R2_ENDPOINT",
    )
    missing = [name for name in required if not os.environ.get(name, "").strip()]
    if missing:
        raise RuntimeError("missing Ravenis read-only R2 settings: " + ", ".join(missing))
    if boto3 is None or BotoConfig is None:
        raise RuntimeError("boto3 is required to read Ravenis releases")
    client = boto3.client(
        "s3",
        endpoint_url=os.environ["RAVENIS_R2_ENDPOINT"],
        aws_access_key_id=os.environ["RAVENIS_R2_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["RAVENIS_R2_SECRET_ACCESS_KEY"],
        region_name=os.environ.get("RAVENIS_R2_REGION") or "auto",
        config=BotoConfig(signature_version="s3v4", s3={"addressing_style": "virtual"}),
    )
    return client, os.environ["RAVENIS_R2_BUCKET"]


def read_remote(pointer_key: str) -> tuple[dict[str, Any], bytes]:
    client, bucket = make_s3_client()
    pointer_body = client.get_object(Bucket=bucket, Key=pointer_key)["Body"].read()
    pointer = validate_pointer(json.loads(pointer_body.decode("utf-8")))
    payload = client.get_object(Bucket=bucket, Key=pointer["object_key"])["Body"].read()
    return pointer, payload


def atomic_replace_directory(target: Path, files: dict[str, bytes]) -> None:
    target = target.resolve()
    staging = target.parent / f".{target.name}-staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    try:
        for name, body in files.items():
            path = staging.joinpath(*name.split("/"))
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
        if target.exists():
            shutil.rmtree(target)
        os.replace(staging, target)
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def save_lkg(lkg: Path, pointer: dict[str, Any], payload: bytes) -> None:
    atomic_replace_directory(lkg, {
        "current.json": json_bytes(pointer),
        "release.tar.gz": payload,
    })


def load_lkg(lkg: Path) -> tuple[dict[str, Any], bytes]:
    pointer_path = lkg / "current.json"
    release_path = lkg / "release.tar.gz"
    if not pointer_path.is_file() or not release_path.is_file():
        raise RuntimeError("no cached Ravenis last-known-good release is available")
    return json.loads(pointer_path.read_text(encoding="utf-8")), release_path.read_bytes()


def write_action_outputs(source: str, digest: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return
    with Path(output_path).open("a", encoding="utf-8") as stream:
        stream.write(f"source={source}\nrelease_sha={digest}\n")


def deploy_release(target: Path, lkg: Path, pointer_key: str, allow_lkg: bool) -> str:
    source = "remote"
    try:
        pointer_value, payload = read_remote(pointer_key)
        pointer, files = validate_release(pointer_value, payload)
        save_lkg(lkg, pointer, payload)
    except Exception as remote_error:
        if not allow_lkg:
            raise RuntimeError(f"Ravenis remote release rejected: {remote_error}") from remote_error
        print(f"[ravenis] remote release unavailable; validating LKG: {remote_error}")
        pointer_value, payload = load_lkg(lkg)
        pointer, files = validate_release(pointer_value, payload)
        source = "lkg"
    atomic_replace_directory(target, files)
    write_action_outputs(source, pointer["sha256"])
    print(
        f"[ravenis] source={source} run_id={pointer['run_id']} files={len(files)} "
        f"sha256={pointer['sha256']}"
    )
    return source


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch the verified Ravenis public release")
    parser.add_argument("--target", required=True)
    parser.add_argument("--lkg", default="_ravenis_lkg")
    parser.add_argument("--pointer-key", default="history/current.json")
    parser.add_argument("--allow-lkg", action="store_true")
    args = parser.parse_args()
    try:
        deploy_release(Path(args.target), Path(args.lkg), args.pointer_key, args.allow_lkg)
        return 0
    except Exception as exc:
        print(f"[ravenis] deployment data step failed: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
