from __future__ import annotations

import gzip
import hashlib
import importlib.util
import io
import json
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "tools" / "fetch_ravenis_release.py"
RAVENIS_JS = Path(__file__).parents[1] / "assets" / "js" / "ravenis.js"
RAVENIS_PAGE = Path(__file__).parents[1] / "ravenis" / "index.html"
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
        "runs": [{"date": "2026-07-16", "slot": "B", "perspective": "B", "source": "ravenis",
                  "generated_at": "2026-07-16T12:00:00+08:00", "record_ids": [record["id"]],
                  "ranking": [{"id": record["id"], "score": 88,
                               "reasons": ["B 核心主题：宏观 / 财经", "高可信专业来源"]}],
                  "summary": {"status": "rules", "overview": "午间更新。", "top_items": [], "watchlist": []}}],
        "items": [record],
    }
    search_record = dict(record, slots=["B"], perspectives={
        "B": {"score": 88, "reasons": ["B 核心主题：宏观 / 财经", "高可信专业来源"]}
    })
    search = {"schema_version": 2, "generated_at": "2026-07-16T12:00:00Z", "total": 1, "items": [search_record]}
    search_body = release.json_bytes(search)
    manifest = {
        "schema_version": 3, "generated_at": "2026-07-16T12:00:00Z", "retention_days": 30,
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
    @staticmethod
    def run_renderer(script, fixture):
        result = subprocess.run(
            [shutil.which("node"), "-e", script, str(RAVENIS_JS)],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            input=json.dumps(fixture, ensure_ascii=False),
        )
        return json.loads(result.stdout)

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the Ravenis renderer test")
    def test_priority_signal_uses_complete_evidence_title(self):
        fixture = {
            "item": {
                "id": "r_1",
                "headline": "半导体抛售潮拖累美股…",
                "evidence_ids": ["r_1"],
            },
            "records": [{
                "id": "r_1",
                "title": "半导体抛售潮拖累美股，纳指100一度跌2%，中概股逆市上涨，黄金大跌破4000",
            }],
        }
        script = """
const { resolveSignalTitle } = require(process.argv[1]);
const fixture = JSON.parse(process.argv[2]);
process.stdout.write(resolveSignalTitle(fixture.item, fixture.records));
"""
        result = subprocess.run(
            [shutil.which("node"), "-e", script, str(RAVENIS_JS), json.dumps(fixture, ensure_ascii=False)],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(result.stdout, fixture["records"][0]["title"])
        self.assertNotIn("…", result.stdout)

    def test_page_has_persistent_day_navigation_and_explicit_search_scopes(self):
        page = RAVENIS_PAGE.read_text(encoding="utf-8")
        self.assertIn('id="ravenis-day-select"', page)
        self.assertIn('id="ravenis-slot-nav"', page)
        for scope in ("articles", "ai", "clusters", "all"):
            self.assertIn(f'value="{scope}"', page)
        self.assertNotIn('id="ravenis-target-date"', page)
        self.assertNotIn('id="ravenis-type"', page)
        self.assertIn('id="ravenis-perspective"', page)
        self.assertIn('按分类筛选记录', page)

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the Ravenis renderer test")
    def test_v3_run_order_and_category_order_are_preserved(self):
        fixture = {
            "date": "2026-07-18",
            "items": [
                {"id": "r1", "title": "AI 新闻", "category": "AI / 模型", "score": 60},
                {"id": "r2", "title": "财经新闻", "category": "宏观 / 财经 / 地缘", "score": 70},
                {"id": "r3", "title": "另一条 AI 新闻", "category": "AI / 模型", "score": 65},
            ],
            "run": {
                "slot": "B", "perspective": "B", "record_ids": ["r2", "r3", "r1"],
                "ranking": [
                    {"id": "r2", "score": 91, "reasons": ["B 核心主题：宏观 / 财经"]},
                    {"id": "r3", "score": 82, "reasons": ["高可信专业来源"]},
                    {"id": "r1", "score": 77, "reasons": ["24 小时内更新"]},
                ],
            },
        }
        script = """
const { recordsForRun, dailyCategoryEntries } = require(process.argv[1]);
const fixture = JSON.parse(require('fs').readFileSync(0, 'utf8'));
const records = recordsForRun(fixture, fixture.run);
process.stdout.write(JSON.stringify({ records, categories: dailyCategoryEntries(records) }));
"""
        result = self.run_renderer(script, fixture)
        self.assertEqual([item["id"] for item in result["records"]], ["r2", "r3", "r1"])
        self.assertEqual(result["records"][0]["rankScore"], 91)
        self.assertEqual(result["records"][0]["rankPerspective"], "B")
        self.assertEqual([item["name"] for item in result["categories"]], ["宏观 / 财经 / 地缘", "AI / 模型"])

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the Ravenis renderer test")
    def test_v2_run_fallback_does_not_mislabel_global_score_as_a_perspective(self):
        fixture = {
            "items": [{"id": "r1", "title": "旧版记录", "score": 73}],
            "run": {"slot": "B", "record_ids": ["r1"]},
        }
        script = """
const { recordsForRun } = require(process.argv[1]);
const fixture = JSON.parse(require('fs').readFileSync(0, 'utf8'));
process.stdout.write(JSON.stringify(recordsForRun(fixture, fixture.run)));
"""
        result = self.run_renderer(script, fixture)
        self.assertEqual(result[0]["rankScore"], 73)
        self.assertEqual(result[0]["rankPerspective"], "")
        self.assertTrue(result[0]["rankLegacy"])

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the Ravenis renderer test")
    def test_search_relevance_tie_uses_selected_perspective(self):
        fixture = [
            {"id": "tech", "type": "news", "title": "共同关键词 技术进展", "date": "2026-07-18",
             "last_seen": "2026-07-18T10:00:00", "perspectives": {
                 "A": {"score": 92, "reasons": ["A 核心主题：AI / 模型"]},
                 "B": {"score": 61, "reasons": ["来源身份已规范化"]}}},
            {"id": "public", "type": "news", "title": "共同关键词 公共事件", "date": "2026-07-18",
             "last_seen": "2026-07-18T10:00:00", "perspectives": {
                 "A": {"score": 58, "reasons": ["来源身份已规范化"]},
                 "B": {"score": 95, "reasons": ["B 核心主题：国内政策"]}}},
        ]
        script = """
const { filterSearchItems } = require(process.argv[1]);
const items = JSON.parse(require('fs').readFileSync(0, 'utf8'));
const a = filterSearchItems(items, { q: '共同关键词', scope: 'articles', perspective: 'A' });
const b = filterSearchItems(items, { q: '共同关键词', scope: 'articles', perspective: 'B' });
process.stdout.write(JSON.stringify({ a, b }));
"""
        result = self.run_renderer(script, fixture)
        self.assertEqual(result["a"]["items"][0]["id"], "tech")
        self.assertEqual(result["b"]["items"][0]["id"], "public")
        self.assertEqual(result["b"]["items"][0]["rankScore"], 95)

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the Ravenis renderer test")
    def test_search_defaults_to_articles_and_rejects_invalid_clusters(self):
        fixture = [
            {"id": "n1", "type": "news", "title": "芯片行业出现新的价格信号", "source": "财联社",
             "source_count": 1, "occurrence_count": 1, "date": "2026-07-18", "last_seen": "2026-07-18T09:00:00", "score": 82},
            {"id": "c0", "type": "event_cluster", "title": "芯片相关信号", "source": "0 个独立来源",
             "source_count": 1, "occurrence_count": 1, "date": "2026-07-18", "last_seen": "2026-07-18T10:00:00", "score": 99},
            {"id": "c1", "type": "event_cluster", "title": "芯片供应链价格变化", "source": "2 个独立来源",
             "source_count": 2, "occurrence_count": 2, "date": "2026-07-18", "last_seen": "2026-07-18T08:00:00", "score": 85},
            {"id": "d1", "type": "ai_digest", "title": "芯片晨间摘要", "source": "AI Digest",
             "source_count": 1, "occurrence_count": 1, "date": "2026-07-18", "last_seen": "2026-07-18T10:00:00", "score": 70},
        ]
        script = """
const { filterSearchItems } = require(process.argv[1]);
const items = JSON.parse(require('fs').readFileSync(0, 'utf8'));
const articles = filterSearchItems(items, { q: '芯片', scope: 'articles', sort: 'latest' });
const clusters = filterSearchItems(items, { q: '芯片', scope: 'clusters', sort: 'latest' });
process.stdout.write(JSON.stringify({ articles, clusters }));
"""
        result = self.run_renderer(script, fixture)
        self.assertEqual(result["articles"]["total"], 1)
        self.assertEqual(result["articles"]["items"][0]["title"], fixture[0]["title"])
        self.assertEqual([item["id"] for item in result["clusters"]["items"]], ["c1"])

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the Ravenis renderer test")
    def test_search_reports_true_total_before_200_item_cap(self):
        fixture = [
            {"id": f"n{index}", "type": "news", "title": f"芯片新闻 {index}", "source": "示例",
             "source_count": 1, "occurrence_count": 1, "date": "2026-07-18", "score": index}
            for index in range(205)
        ]
        script = """
const { filterSearchItems } = require(process.argv[1]);
const items = JSON.parse(require('fs').readFileSync(0, 'utf8'));
process.stdout.write(JSON.stringify(filterSearchItems(items, { q: '芯片', scope: 'articles' })));
"""
        result = self.run_renderer(script, fixture)
        self.assertEqual(result["total"], 205)
        self.assertEqual(len(result["items"]), 200)

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the Ravenis renderer test")
    def test_slot_navigation_uses_schedule_order_and_legacy_label(self):
        fixture = {
            "scheduled": {"runs": [
                {"slot": "C", "record_ids": ["c1"]},
                {"slot": "A", "record_ids": ["a1", "a2"]},
                {"slot": "DIGEST", "record_ids": ["d1"]},
                {"slot": "B", "record_ids": ["b1"]},
            ]},
            "legacy": {"total": 9, "runs": [{"slot": "MIGRATION", "record_ids": ["m1"]}], "items": []},
            "partial": {"runs": [
                {"slot": "A", "record_ids": ["a1"]},
                {"slot": "B", "record_ids": ["b1"]},
            ]},
        }
        script = """
const { availableSlotsForDay, chooseDailySlot } = require(process.argv[1]);
const fixture = JSON.parse(require('fs').readFileSync(0, 'utf8'));
process.stdout.write(JSON.stringify({
  slots: availableSlotsForDay(fixture.scheduled),
  fallback: chooseDailySlot(fixture.scheduled, 'MISSING'),
  retained: chooseDailySlot(fixture.scheduled, 'DIGEST'),
  legacy: availableSlotsForDay(fixture.legacy),
  partial: availableSlotsForDay(fixture.partial),
  partialFallback: chooseDailySlot(fixture.partial, 'C')
}));
"""
        result = self.run_renderer(script, fixture)
        self.assertEqual([item["slot"] for item in result["slots"]], ["A", "DIGEST", "B", "C"])
        self.assertEqual(result["fallback"], "C")
        self.assertEqual(result["retained"], "DIGEST")
        self.assertEqual(result["legacy"][0]["label"], "全天归档")
        self.assertFalse(result["partial"][3]["available"])
        self.assertEqual(result["partialFallback"], "B")

    def test_valid_release_is_accepted(self):
        pointer, payload = make_release()
        validated, files = release.validate_release(pointer, payload)
        self.assertEqual(validated["sha256"], hashlib.sha256(payload).hexdigest())
        self.assertEqual(set(files), set(pointer["files"]))

    def test_v3_run_ranking_must_match_record_order(self):
        pointer, payload = make_release()
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:gz") as archive:
            files = {member.name: archive.extractfile(member).read() for member in archive.getmembers()}
        day = json.loads(files["days/2026-07-16.json"])
        day["runs"][0]["record_ids"] = ["missing"]
        files["days/2026-07-16.json"] = release.json_bytes(day)
        buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode="wb", mtime=0) as zipped:
            with tarfile.open(fileobj=zipped, mode="w") as archive:
                for name, body in files.items():
                    info = tarfile.TarInfo(name)
                    info.size = len(body)
                    archive.addfile(info, io.BytesIO(body))
        broken = buffer.getvalue()
        pointer["size"] = len(broken)
        pointer["sha256"] = hashlib.sha256(broken).hexdigest()
        with self.assertRaisesRegex(ValueError, "record_ids"):
            release.validate_release(pointer, broken)

    def test_v2_empty_ranking_remains_compatible(self):
        release.validate_runs(
            [{"slot": "B", "record_ids": ["r_1"], "ranking": []}],
            {"r_1"},
        )

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
