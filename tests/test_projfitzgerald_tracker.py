import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "PROJFITZGERALD_PROGRESS.md"


def tracker_data():
    text = SOURCE.read_text(encoding="utf-8")
    match = re.search(
        r"<!-- TRACKER_DATA_START -->\s*```json\s*([\s\S]*?)\s*```\s*<!-- TRACKER_DATA_END -->",
        text,
    )
    assert match, "tracker JSON block is missing"
    return json.loads(match.group(1))


def test_tracker_has_unique_ids_and_valid_states():
    data = tracker_data()
    items = [item for milestone in data["milestones"] for item in milestone["items"]]
    ids = [item["id"] for item in items]
    assert len(ids) == len(set(ids))
    assert {item["status"] for item in items} <= {"done", "in_progress", "todo", "blocked"}


def test_summary_matches_tracker_items():
    data = tracker_data()
    items = [item for milestone in data["milestones"] for item in milestone["items"]]
    actual = {status: sum(item["status"] == status for item in items) for status in ("done", "in_progress", "todo", "blocked")}
    expected = data["summary"]
    assert actual["done"] == expected["verifiedDone"]
    assert actual["in_progress"] == expected["inProgress"]
    assert actual["todo"] == expected["todo"]
    assert actual["blocked"] == expected["blocked"]


def test_page_loads_the_progress_source():
    page = (ROOT / "projfitzgerald" / "index.html").read_text(encoding="utf-8")
    script = (ROOT / "projfitzgerald" / "app.js").read_text(encoding="utf-8")
    assert "/projfitzgerald/" in page
    assert "PROJFITZGERALD_PROGRESS.md" in script
