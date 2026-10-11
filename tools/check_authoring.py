#!/usr/bin/env python3
"""Validate Neutriverse authoring sources with the Python standard library."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
POST_TYPES = {"note", "essay"}
TOPICS = {"computation", "humanity", "otaku", "arts"}
PROJECT_CONTEXTS = {"build", "observe"}
PROJECT_VISIBILITIES = {"listed", "listed_noindex", "unlisted_noindex"}
PROJECT_LINKS = {"application", "repository", "documentation"}
FRAGMENT_ID = re.compile(r"fragment-(\d{4}-\d{2}-\d{2})(?:-[a-z0-9]+(?:-[a-z0-9]+)*)?")
KEBAB_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
IMPLICIT_NON_STRING = re.compile(
    r"(?:[-+]?(?:\d[\d_]*)(?:\.\d[\d_]*)?|"
    r"true|false|yes|no|on|off|null|~|"
    r"\d{4}-\d{2}-\d{2})",
    re.IGNORECASE,
)


def front_matter(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)(.*)\Z", text, re.S)
    if not match:
        raise ValueError("missing YAML front matter")
    return match.group(1), match.group(2)


def scalar(block: str, name: str) -> str | None:
    match = re.search(rf"^{re.escape(name)}:[ \t]*(.*?)[ \t]*$", block, re.M)
    if not match:
        return None
    value = match.group(1).strip()
    if value in {"", "null", "~"}:
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
        return parsed if isinstance(parsed, str) else str(parsed)
    return value


def split_inline_list(value: str) -> list[str]:
    if not (value.startswith("[") and value.endswith("]")):
        raise ValueError("must use an inline [..] list or an indented YAML list")
    body = value[1:-1]
    if not body.strip():
        return []
    result: list[str] = []
    start = 0
    quote = None
    escaped = False
    for index, char in enumerate(body):
        if escaped:
            escaped = False
            continue
        if char == "\\" and quote == '"':
            escaped = True
            continue
        if char in "\"'":
            if quote is None and not body[start:index].strip():
                quote = char
            elif quote == char:
                quote = None
        elif char == "," and quote is None:
            result.append(body[start:index].strip())
            start = index + 1
    if quote is not None:
        raise ValueError("contains an unclosed quote")
    result.append(body[start:].strip())
    return result


def raw_list(block: str, name: str) -> list[str] | None:
    match = re.search(rf"^{re.escape(name)}:[ \t]*(.*)$", block, re.M)
    if not match:
        return None
    inline = match.group(1).strip()
    if inline:
        return split_inline_list(inline)
    result = []
    for line in block[match.end():].splitlines():
        if not line.strip():
            continue
        item = re.match(r"^\s+-\s+(.*?)\s*$", line)
        if not item:
            break
        result.append(item.group(1))
    return result


def string_item(raw: str) -> tuple[str, str | None]:
    value = raw.strip()
    if not value:
        return "", "contains an empty item"
    quoted = len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'"
    if quoted:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return "", f"has invalid quoting: {value}"
        if not isinstance(parsed, str):
            return "", f"must be a string: {value}"
        return parsed, None
    if IMPLICIT_NON_STRING.fullmatch(value):
        return value, f"must be quoted to remain a YAML string: {value}"
    return value, None


def validate_string_list(block: str, name: str, required: bool = False) -> tuple[list[str], list[str]]:
    try:
        items = raw_list(block, name)
    except ValueError as error:
        return [], [f"{name} {error}"]
    if items is None:
        return [], [f"missing {name}"] if required else []
    values, errors = [], []
    for raw in items:
        value, error = string_item(raw)
        if error:
            errors.append(f"{name} {error}")
        else:
            values.append(value)
    return values, errors


def taxonomy_series(root: Path) -> set[str]:
    text = (root / "_data" / "content_taxonomy.yml").read_text(encoding="utf-8")
    section = re.search(r"^series:\s*\n(.*?)^types:", text, re.M | re.S)
    if not section:
        raise ValueError("content taxonomy has no series section")
    return set(re.findall(r"^\s+label:\s*(.*?)\s*$", section.group(1), re.M))


def validate_post(path: Path, series_labels: set[str]) -> list[str]:
    errors = []
    try:
        block, body = front_matter(path)
    except ValueError as error:
        return [str(error)]

    filename = re.fullmatch(r"(\d{4}-\d{2}-\d{2})-(.+)\.md", path.name)
    if not filename:
        errors.append("filename must be YYYY-MM-DD-slug.md")
    date = scalar(block, "date")
    if not date or not ISO_DATE.fullmatch(date):
        errors.append("date must be YYYY-MM-DD")
    elif filename and filename.group(1) != date:
        errors.append("front matter date must match filename date")
    if not scalar(block, "title"):
        errors.append("title is required")
    kind = scalar(block, "type")
    if kind not in POST_TYPES:
        errors.append("type must be note or essay; fragment belongs in _tabs/thoughts.md")
    topic = scalar(block, "topic")
    if topic not in TOPICS:
        errors.append("topic must be computation, humanity, otaku, or arts")
    series = scalar(block, "series")
    if series and series not in series_labels:
        errors.append(f"series is not defined in _data/content_taxonomy.yml: {series}")
    _, tag_errors = validate_string_list(block, "tags", required=True)
    errors.extend(tag_errors)
    _, category_errors = validate_string_list(block, "categories", required=False)
    errors.extend(category_errors)
    hidden = scalar(block, "hidden")
    if hidden and hidden.lower() not in {"true", "false"}:
        errors.append("hidden must be true or false when present")
    if not body.strip():
        errors.append("post body must not be empty")
    return errors


def fragment_objects(path: Path) -> list[dict[str, object]]:
    block, _ = front_matter(path)
    fragments = re.search(r"^fragments:\s*\n(.*)\Z", block, re.M | re.S)
    if not fragments:
        raise ValueError("missing fragments list")
    objects = []
    current = None
    for line in fragments.group(1).splitlines():
        start = re.match(r"^\s{2}-\s+text:\s*(.*?)\s*$", line)
        if start:
            if current:
                objects.append(current)
            text, error = string_item(start.group(1))
            current = {"text": text, "_text_error": error}
            continue
        field = re.match(r"^\s{4}(id|date|type|topic|tags):\s*(.*?)\s*$", line)
        if current is not None and field:
            key, value = field.groups()
            current[key] = value
    if current:
        objects.append(current)
    return objects


def validate_fragments(path: Path) -> tuple[int, list[str]]:
    errors = []
    try:
        fragments = fragment_objects(path)
    except ValueError as error:
        return 0, [str(error)]
    seen = set()
    for index, item in enumerate(fragments, 1):
        prefix = f"fragment #{index}"
        if item.get("_text_error") or not item.get("text"):
            errors.append(f"{prefix}: text must be a non-empty string")
        fragment_id = str(item.get("id", "")).strip("\"'")
        date = str(item.get("date", "")).strip("\"'")
        match = FRAGMENT_ID.fullmatch(fragment_id)
        if not match:
            errors.append(f"{prefix}: id must be fragment-YYYY-MM-DD with an optional kebab suffix")
        elif match.group(1) != date:
            errors.append(f"{prefix}: id date must match date")
        if fragment_id in seen:
            errors.append(f"{prefix}: duplicate id {fragment_id}")
        seen.add(fragment_id)
        if not ISO_DATE.fullmatch(date):
            errors.append(f"{prefix}: date must be YYYY-MM-DD")
        if str(item.get("type", "")).strip("\"'") != "fragment":
            errors.append(f"{prefix}: type must be fragment")
        if str(item.get("topic", "")).strip("\"'") not in TOPICS:
            errors.append(f"{prefix}: invalid topic")
        tags_raw = str(item.get("tags", ""))
        try:
            tags = split_inline_list(tags_raw)
        except ValueError as error:
            errors.append(f"{prefix}: tags {error}")
        else:
            for raw in tags:
                _, error = string_item(raw)
                if error:
                    errors.append(f"{prefix}: tags {error}")
    return len(fragments), errors


def valid_link(value: object) -> bool:
    return isinstance(value, str) and (value.startswith("/") or value.startswith("https://"))


def validate_projects(root: Path) -> tuple[int, list[str]]:
    errors = []
    path = root / "_data" / "neutriverse_projects.yml"
    try:
        catalog = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return 0, [f"project catalog is not valid JSON-compatible YAML: {error}"]
    projects = catalog.get("projects")
    if catalog.get("schema_version") != 1 or not isinstance(projects, list):
        return 0, ["project catalog requires schema_version 1 and a projects list"]
    seen = set()
    for index, project in enumerate(projects, 1):
        project_id = project.get("id") if isinstance(project, dict) else None
        prefix = f"project #{index} ({project_id or 'missing-id'})"
        if not isinstance(project, dict):
            errors.append(f"{prefix}: entry must be an object")
            continue
        if not isinstance(project_id, str) or not KEBAB_ID.fullmatch(project_id):
            errors.append(f"{prefix}: id must be lowercase kebab-case")
        elif project_id in seen:
            errors.append(f"{prefix}: duplicate id")
        seen.add(project_id)
        for field in ("name", "summary"):
            if not isinstance(project.get(field), str) or not project[field].strip():
                errors.append(f"{prefix}: {field} is required")
        contexts = project.get("contexts")
        if not isinstance(contexts, list) or not contexts or "build" not in contexts:
            errors.append(f"{prefix}: contexts must be a non-empty list containing build")
        elif any(not isinstance(item, str) or item not in PROJECT_CONTEXTS for item in contexts):
            errors.append(f"{prefix}: contexts may only contain build and observe")
        if project.get("visibility") not in PROJECT_VISIBILITIES:
            errors.append(f"{prefix}: invalid visibility")
        if "status" in project and (not isinstance(project["status"], str) or not project["status"].strip()):
            errors.append(f"{prefix}: status must be omitted when unknown")
        links = project.get("links")
        if links is not None:
            if not isinstance(links, dict) or not links:
                errors.append(f"{prefix}: links must be omitted when empty")
            else:
                for key, value in links.items():
                    if key not in PROJECT_LINKS or not valid_link(value):
                        errors.append(f"{prefix}: invalid {key} link")
        sources = project.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{prefix}: at least one source is required")
        else:
            for source in sources:
                if not isinstance(source, dict):
                    errors.append(f"{prefix}: source must be an object")
                elif source.get("kind") == "site":
                    source_path = source.get("path")
                    if not isinstance(source_path, str) or not (root / source_path).is_file():
                        errors.append(f"{prefix}: site source does not exist: {source_path}")
                elif source.get("kind") == "external":
                    if not isinstance(source.get("url"), str) or not source["url"].startswith("https://"):
                        errors.append(f"{prefix}: external source must use https")
                else:
                    errors.append(f"{prefix}: source kind must be site or external")
        related_posts = project.get("related_posts")
        if related_posts is not None:
            if not isinstance(related_posts, list) or not related_posts:
                errors.append(f"{prefix}: related_posts must be omitted when empty and otherwise be a list")
            else:
                for post in related_posts:
                    if not isinstance(post, dict):
                        errors.append(f"{prefix}: related post must be an object")
                    elif not (root / str(post.get("source_path", ""))).is_file():
                        errors.append(f"{prefix}: related post source does not exist")
                    elif not str(post.get("url", "")).startswith("/posts/"):
                        errors.append(f"{prefix}: related post URL must use /posts/")
        releases = project.get("releases")
        if releases is not None:
            if not isinstance(releases, list) or not releases:
                errors.append(f"{prefix}: releases must be omitted when none are verified")
            else:
                for release in releases:
                    if not isinstance(release, dict) or not (release.get("name") or release.get("version")):
                        errors.append(f"{prefix}: each release needs a verified name or version")
                    elif "url" in release and not valid_link(release["url"]):
                        errors.append(f"{prefix}: release URL is invalid")
        expected_detail = f"/build/{project_id}/"
        if project.get("detail_url") != expected_detail:
            errors.append(f"{prefix}: detail_url must be {expected_detail}")
        detail_path = root / "build" / str(project_id) / "index.md"
        if not detail_path.is_file():
            errors.append(f"{prefix}: detail page is missing")
        else:
            try:
                detail, _ = front_matter(detail_path)
            except ValueError as error:
                errors.append(f"{prefix}: detail page {error}")
            else:
                if scalar(detail, "project_id") != project_id:
                    errors.append(f"{prefix}: detail page project_id mismatch")
                if scalar(detail, "permalink") != expected_detail:
                    errors.append(f"{prefix}: detail page permalink mismatch")
    return len(projects), errors


def validate(root: Path = ROOT) -> tuple[dict[str, int], list[str]]:
    errors = []
    try:
        series_labels = taxonomy_series(root)
    except ValueError as error:
        series_labels = set()
        errors.append(str(error))
    posts = [path for path in sorted((root / "_posts").glob("*.md")) if path.name != ".placeholder"]
    for path in posts:
        errors.extend(f"{path.relative_to(root)}: {message}" for message in validate_post(path, series_labels))
    fragment_count, fragment_errors = validate_fragments(root / "_tabs" / "thoughts.md")
    errors.extend(f"_tabs/thoughts.md: {message}" for message in fragment_errors)
    project_count, project_errors = validate_projects(root)
    errors.extend(f"_data/neutriverse_projects.yml: {message}" for message in project_errors)
    return {"posts": len(posts), "fragments": fragment_count, "projects": project_count}, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (defaults to this checkout)")
    args = parser.parse_args()
    summary, errors = validate(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(json.dumps({**summary, "passed": False, "errors": len(errors)}, ensure_ascii=False))
        return 1
    print(json.dumps({**summary, "passed": True, "errors": 0}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
