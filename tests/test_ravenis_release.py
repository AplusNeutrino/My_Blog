from __future__ import annotations

import gzip
import hashlib
import importlib.util
import io
import json
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "tools" / "fetch_ravenis_release.py"
SPEC = importlib.util.spec_from_file_location("fetch_ravenis_release", SCRIPT)
release = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = release
SPEC.loader.exec_module(release)


def public_record(**overrides):
    record = {
        "id": "r_1", "short_id": "A001", "date": "2026-07-16", "type": "news",
        "title": "DeepSeek 发布新模型", "source": "示例来源", "source_count": 2,
        "url": "https://example.com/news", "category": "AI / 模型", "tags": ["DeepSeek"],
        "score": 86, "first_seen": "2026-07-16T08:00:00+08:00",
        "last_seen": "2026-07-16T12:00:00+08:00", "occurrence_count": 2,
        "summary": "公开短摘要。",
    }
    record.update(overrides)
    return record


def make_release(record=None):
    record = record or public_record()
    day = {
        "date": "2026-07-16", "total": 1,
        "runs": [{"date": "2026-07-16", "slot": "B", "source": "ravenis",
                  "generated_at": "2026-07-16T12:00:00+08:00", "record_ids": [record["id"]],
                  "summary": {"status": "rules", "overview": "午间更新。", "top_items": [], "watchlist": []}}],
        "items": [record],
    }
    search_record = dict(record, slots=["B"])
    search = {"schema_version": 1, "generated_at": "2026-07-16T12:00:00Z", "total": 1, "items": [search_record]}
    search_body = release.json_bytes(search)
    manifest = {
        "schema_version": 2, "generated_at": "2026-07-16T12:00:00Z", "retention_days": 30,
        "total": 1, "run_count": 1,
        "days": [{"date": "2026-07-16", "count": 1, "path": "days/2026-07-16.json"}],
        "types": ["news"], "slots": ["B"],
        "weekly": {"path": "weekly/latest.json", "start_date": "2026-07-10", "end_date": "2026-07-16", "record_count": 1, "theme_count": 1},
        "search": {"path": "search-index.json", "count": 1, "sha256": hashlib.sha256(search_body).hexdigest()},
    }
    weekly = {"schema_version": 1, "start_date": "2026-07-10", "end_date": "2026-07-16", "record_count": 1, "theme_count": 1, "top_themes": [], "sections": {}, "watchlist": []}
    files = {
        "manifest.json": release.json_bytes(manifest),
        "search-index.json": search_body,
        "weekly/latest.json": release.json_bytes(weekly),
        "days/2026-07-16.json": release.json_bytes(day),
    }
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb", mtime=0) as zipped:
        with tarfile.open(fileobj=zipped, mode="w") as archive:
            for name, body in files.items():
                info = tarfile.TarInfo(name)
                info.size = len(body)
                archive.addfile(info, io.BytesIO(body))
    payload = buffer.getvalue()
    pointer = {
        "schema_version": 1, "run_id": "fixture", "generated_at": "2026-07-16T12:00:00Z",
        "object_key": "history/releases/fixture.tar.gz", "sha256": hashlib.sha256(payload).hexdigest(),
        "size": len(payload), "retention_days": 30, "files": list(files),
    }
    return pointer, payload


class RavenisReleaseTests(unittest.TestCase):
    def test_valid_release_is_accepted(self):
        pointer, payload = make_release()
        validated, files = release.validate_release(pointer, payload)
        self.assertEqual(validated["sha256"], hashlib.sha256(payload).hexdigest())
        self.assertEqual(set(files), set(pointer["files"]))

    def test_forbidden_field_is_rejected(self):
        pointer, payload = make_release(public_record(full_text="private body"))
        with self.assertRaisesRegex(ValueError, "forbidden public field"):
            release.validate_release(pointer, payload)

    def test_hash_mismatch_is_rejected(self):
        pointer, payload = make_release()
        pointer["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            release.validate_release(pointer, payload)

    def test_normal_build_can_fall_back_to_valid_lkg(self):
        pointer, payload = make_release()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            lkg = root / "lkg"
            target = root / "site" / "ravenis" / "data"
            release.save_lkg(lkg, pointer, payload)
            with patch.object(release, "read_remote", side_effect=RuntimeError("R2 unavailable")):
                source = release.deploy_release(target, lkg, "history/current.json", allow_lkg=True)
            self.assertEqual(source, "lkg")
            self.assertTrue((target / "manifest.json").is_file())

    def test_dispatch_build_does_not_fall_back(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with patch.object(release, "read_remote", side_effect=RuntimeError("R2 unavailable")):
                with self.assertRaisesRegex(RuntimeError, "remote release rejected"):
                    release.deploy_release(root / "target", root / "lkg", "history/current.json", allow_lkg=False)


if __name__ == "__main__":
    unittest.main()
