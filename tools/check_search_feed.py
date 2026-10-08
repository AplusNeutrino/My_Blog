#!/usr/bin/env python3
"""Validate built public Search and Atom outputs against protected writing sources."""

import json
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
ATOM = {"atom": "http://www.w3.org/2005/Atom"}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    require(text.startswith("---\n"), f"missing front matter: {path}")
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def normalized_path(url):
    parsed = urlparse(url)
    return parsed.path + (f"#{parsed.fragment}" if parsed.fragment else "")


def date_key(item):
    return datetime.fromisoformat(item["date"][:10])


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    search_path = site / "assets" / "js" / "data" / "search.json"
    feed_path = site / "feed.xml"
    require(search_path.is_file(), f"missing built Search index: {search_path}")
    require(feed_path.is_file(), f"missing built Atom feed: {feed_path}")

    baseline = json.loads(
        (ROOT / "docs" / "neutriverse-restructure-baseline.json").read_text(encoding="utf-8")
    )
    public_posts = [
        post for post in baseline["posts"] if not post["hidden"] and post["published"]
    ]
    hidden_titles = {post["title"] for post in baseline["posts"] if post["hidden"]}
    fragment_source = front_matter(ROOT / "_tabs" / "thoughts.md")
    fragments = fragment_source.get("fragments", [])
    require(all(fragment.get("id") and fragment.get("text") for fragment in fragments), "Fragment id/text contract failed")

    search = json.loads(search_path.read_text(encoding="utf-8"))
    expected_count = len(public_posts) + len(fragments)
    require(len(search) == expected_count, f"Search count {len(search)} != {expected_count}")
    search_urls = [item["url"] for item in search]
    require(len(search_urls) == len(set(search_urls)), "Search contains duplicate URLs")
    require(not hidden_titles.intersection(item["title"] for item in search), "hidden post leaked into Search")

    fragment_search = [item for item in search if item.get("type") == "fragment"]
    require(len(fragment_search) == len(fragments), "Search Fragment count mismatch")
    expected_fragments = {
        f"/thoughts/#{fragment['id']}": fragment["text"] for fragment in fragments
    }
    actual_fragments = {item["url"]: item["content"] for item in fragment_search}
    require(actual_fragments == expected_fragments, "Search Fragment links or protected text changed")

    root = ET.parse(feed_path).getroot()
    require(root.tag == "{http://www.w3.org/2005/Atom}feed", "feed is not Atom")
    self_links = [
        node.get("href")
        for node in root.findall("atom:link", ATOM)
        if node.get("rel") == "self"
    ]
    require(len(self_links) == 1 and normalized_path(self_links[0]) == "/feed.xml", "invalid feed self link")

    feed_entries = root.findall("atom:entry", ATOM)
    config = yaml.safe_load((ROOT / "_data" / "neutriverse_discovery.yml").read_text(encoding="utf-8"))
    limit = config["feed"]["limit"]
    require(len(feed_entries) == min(limit, expected_count), "feed entry limit/count mismatch")
    feed_titles = [entry.findtext("atom:title", namespaces=ATOM) for entry in feed_entries]
    require(not hidden_titles.intersection(feed_titles), "hidden post leaked into feed")

    feed_urls = [
        normalized_path(entry.find("atom:link", ATOM).get("href")) for entry in feed_entries
    ]
    require(len(feed_urls) == len(set(feed_urls)), "feed contains duplicate entry URLs")
    expected_feed_urls = [
        item["url"] for item in sorted(search, key=date_key, reverse=True)[:limit]
    ]
    require(feed_urls == expected_feed_urls, "feed order or public writing membership mismatch")
    require(any(url.startswith("/thoughts/#fragment-") for url in feed_urls), "feed omitted recent Fragments")

    print(
        json.dumps(
            {
                "search_items": len(search),
                "search_fragments": len(fragment_search),
                "feed_entries": len(feed_entries),
                "feed_fragments": sum(url.startswith("/thoughts/#fragment-") for url in feed_urls),
                "hidden_excluded": len(hidden_titles),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
