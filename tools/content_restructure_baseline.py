#!/usr/bin/env python3
"""Read-only source inventory; URLs are candidates, not a Jekyll runtime claim.

Requires Python 3 and PyYAML. Run from the repository root, specifying an output
outside public assets. Never overwrite the original baseline during validation.
"""
import argparse
import collections
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess

import yaml


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def read_source(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
    if not match:
        return {}, text, raw
    return yaml.safe_load(match[1]) or {}, text[match.end():], raw


def normalize(value):
    return json.loads(json.dumps(value, default=str, ensure_ascii=False))


def source_url(path, fm):
    if fm.get("permalink"):
        return str(fm["permalink"])
    if path.parts[0] == "_posts":
        name = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
        return "/posts/" + str(fm.get("slug", name)).lower() + "/"
    if path.parts[0] == "_tabs":
        return "/" + path.stem + "/"
    if path.name in ("index.html", "index.md"):
        parent = path.parent.as_posix()
        return "/" if parent == "." else "/" + parent + "/"
    return None


def build():
    posts = []
    for path in sorted(Path("_posts").glob("*.md")):
        fm, body, raw = read_source(path)
        posts.append({
            "path": path.as_posix(), "title": fm.get("title"),
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
            "body_sha256_lf": digest(body), "body_bytes_utf8_lf": len(body.encode("utf-8")),
            "protected_url_metadata": {key: normalize(fm.get(key)) for key in ("date", "slug", "permalink")},
            "source_url_candidate": source_url(path, fm), "runtime_url_verified": False,
            "type": fm.get("type"), "topic": fm.get("topic"), "series": fm.get("series"),
            "tags": fm.get("tags", []), "categories": fm.get("categories", []),
            "hidden": fm.get("hidden") is True, "published": fm.get("published", True),
            "sitemap": fm.get("sitemap"), "robots": fm.get("robots"),
        })
    fm, _, _ = read_source(Path("_tabs/thoughts.md"))
    fragments = [{
        "source": "_tabs/thoughts.md", "source_index": i,
        "date": normalize(f.get("date")), "text_sha256": digest(f["text"]),
        "type": f.get("type"), "topic": f.get("topic"), "tags": f.get("tags", []),
        "hidden": f.get("hidden") is True,
    } for i, f in enumerate(fm.get("fragments", []))]
    pages = []
    paths = list(Path("_tabs").glob("*.md")) + list(Path("_hidden_pages").glob("*.md"))
    paths += [Path(x) for x in ("index.html", "gate/index.md", "ravenis/index.html", "projfitzgerald/index.html", "occult-atlas-app/index.html")]
    for path in sorted(paths):
        fm, _, raw = read_source(path)
        pages.append({"path": str(path), "source_url_candidate": source_url(path, fm),
                      "front_matter_visibility": {k: fm.get(k) for k in ("hidden", "sitemap", "robots")},
                      "layout": fm.get("layout"), "raw_sha256": hashlib.sha256(raw).hexdigest(),
                      "hidden_collection": path.parts[0] == "_hidden_pages",
                      "runtime_url_verified": False})
    counts = lambda items, key: dict(sorted(collections.Counter(x.get(key) for x in items).items()))
    all_items = posts + fragments
    tracked = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
    contract_paths = [p for p in tracked if p.startswith(("_layouts/", "_includes/", "_plugins/", ".github/workflows/"))]
    contract_paths += [p for p in tracked if p.startswith(("assets/js/", "assets/css/", "assets/pgl/", "_data/", "projfitzgerald/", "occult-atlas-app/", "ravenis/")) and not p.endswith((".json", ".png", ".jpg"))]
    contract_paths += [p for p in tracked if p in ("_config.yml", "CNAME", "Gemfile", "DESIGN.md")]
    return {
        "schema_version": 1,
        "captured_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_head_sha": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "source_url_rules": "Explicit permalink first; otherwise configured /posts/:title/ with filename slug, tab /:title/, directory index. Unicode paths unescaped. All candidates require Jekyll output validation; slugify/archive-generated routes are not asserted here.",
        "hash_rules": "UTF-8; strip initial BOM; normalize CRLF/CR to LF; body is exact suffix after front matter closing line; preserve other whitespace including terminal newline. Fragment hash covers parsed text only, date separately protected.",
        "counts": {"posts": len(posts), "fragments": len(fragments), "hidden_posts": sum(x["hidden"] for x in posts),
                   "types": counts(all_items, "type"), "topics": counts(all_items, "topic"),
                   "unique_post_tags": len({t for x in posts for t in x["tags"]}),
                   "unique_writing_tags": len({t for x in all_items for t in x["tags"]})},
        "posts": posts, "fragments": fragments, "pages": pages,
        "contracts": [{"path": p, "sha256": hashlib.sha256(Path(p).read_bytes()).hexdigest()} for p in sorted(set(contract_paths))],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check-against", type=Path)
    parser.add_argument("--source-ref", help="Record an existing source snapshot after verifying inventoried sources match it")
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Output already exists; choose a new path to protect the original baseline.")
    current = build()
    if args.source_ref:
        sources = [x["path"] for x in current["posts"] + current["pages"] + current["contracts"]]
        subprocess.run(["git", "diff", "--quiet", args.source_ref, "--", *sources], check=True)
        current["source_head_sha"] = subprocess.check_output(["git", "rev-parse", args.source_ref], text=True).strip()
    if args.check_against:
        original = json.loads(args.check_against.read_text())
        previous = {x["path"]: x for x in original["posts"]}
        errors = []
        now = {x["path"]: x for x in current["posts"]}
        for path, old in previous.items():
            if path not in now:
                errors.append(path + ": removed or renamed")
                continue
            for key in ("body_sha256_lf", "protected_url_metadata", "source_url_candidate", "hidden", "published"):
                if old[key] != now[path][key]:
                    errors.append(path + ": " + key + " changed")
        old_fragments = collections.Counter((x["date"], x["text_sha256"]) for x in original["fragments"])
        new_fragments = collections.Counter((x["date"], x["text_sha256"]) for x in current["fragments"])
        if old_fragments - new_fragments:
            errors.append("Original Fragment text/date missing or changed")
        current["protection_check"] = {"baseline": str(args.check_against), "passed": not errors, "errors": errors}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(current, ensure_ascii=False, indent=2, default=str) + "\n")
    print(json.dumps(current["counts"], ensure_ascii=False))
    if args.check_against:
        print(json.dumps(current["protection_check"], ensure_ascii=False))
        raise SystemExit(0 if current["protection_check"]["passed"] else 1)


if __name__ == "__main__":
    main()
