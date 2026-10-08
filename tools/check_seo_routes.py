#!/usr/bin/env python3
"""Validate built Neutriverse SEO and route contracts without third-party packages."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree

ORIGIN = "https://neutriverse.uk"
PUBLIC_ROUTES = ("/", "/think/", "/build/", "/observe/", "/about/")
NOINDEX_ROUTES = (
    "/gate/",
    "/navi/",
    "/ravenis/",
    "/occult-atlas/",
    "/occult-atlas-app/",
    "/build/ravenis/",
    "/build/occult-atlas/",
    "/build/gate/",
    "/tags/bus/",
    "/tags/changelog/",
)
REDIRECTS = {
    "/occult-atlas-app/": "/occult-atlas/",
    "/tags/bus/": "/tags/system-bus/",
    "/tags/changelog/": "/tags/neutriverse/",
}


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonicals: list[str] = []
        self.robots: list[str] = []
        self.descriptions: list[str] = []
        self.refreshes: list[str] = []
        self.links: list[str] = []
        self.title_parts: list[str] = []
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        if tag.lower() == "link" and "canonical" in values.get("rel", "").lower().split():
            self.canonicals.append(values.get("href", ""))
        elif tag.lower() == "meta":
            name = values.get("name", "").lower()
            equiv = values.get("http-equiv", "").lower()
            if name == "robots":
                self.robots.append(values.get("content", ""))
            elif name == "description":
                self.descriptions.append(values.get("content", ""))
            elif equiv == "refresh":
                self.refreshes.append(values.get("content", ""))
        elif tag.lower() == "a" and values.get("href"):
            self.links.append(values["href"])
        elif tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        return "".join(self.title_parts).strip()


def route_file(site: Path, route: str) -> Path:
    path = unquote(urlsplit(route).path)
    if path == "/":
        return site / "index.html"
    relative = path.lstrip("/")
    if path.endswith("/"):
        return site / relative / "index.html"
    candidate = site / relative
    return candidate if candidate.suffix else candidate / "index.html"


def file_route(site: Path, path: Path) -> str:
    relative = path.relative_to(site).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    return "/" + relative


def parse_documents(site: Path) -> dict[str, DocumentParser]:
    documents: dict[str, DocumentParser] = {}
    for path in site.rglob("*.html"):
        parser = DocumentParser()
        parser.feed(path.read_text(encoding="utf-8", errors="replace"))
        documents[file_route(site, path)] = parser
    return documents


def canonical_path(value: str) -> str | None:
    parsed = urlsplit(value)
    if parsed.netloc and parsed.netloc != "neutriverse.uk":
        return None
    return unquote(parsed.path or "/")


def refresh_target(route: str, values: list[str]) -> str | None:
    for value in values:
        fields = value.split(";", 1)
        if len(fields) != 2 or "url=" not in fields[1].lower():
            continue
        target = fields[1].split("=", 1)[1].strip(" \"'")
        return unquote(urlsplit(urljoin(ORIGIN + route, target)).path)
    return None


def sitemap_locations(site: Path) -> set[str]:
    root = ElementTree.parse(site / "sitemap.xml").getroot()
    return {
        unquote(urlsplit(node.text or "").path)
        for node in root.iter()
        if node.tag.rsplit("}", 1)[-1] == "loc"
    }


def baseline_routes(repo: Path) -> set[str]:
    data = json.loads((repo / "docs/neutriverse-restructure-baseline.json").read_text(encoding="utf-8"))
    routes = {entry["source_url_candidate"] for entry in data["pages"]}
    for post in data["posts"]:
        metadata = post["protected_url_metadata"]
        if metadata["permalink"]:
            route = metadata["permalink"]
        else:
            slug = metadata["slug"] or Path(post["path"]).stem[11:]
            route = f"/posts/{slug}/"
        routes.add(route)
    return routes


def check(site: Path, repo: Path) -> list[str]:
    errors: list[str] = []
    documents = parse_documents(site)

    required = baseline_routes(repo) | set(PUBLIC_ROUTES) | set(NOINDEX_ROUTES) | set(REDIRECTS.values())
    for route in sorted(required):
        if not route_file(site, route).is_file():
            errors.append(f"protected route did not build: {route}")

    for route, document in sorted(documents.items()):
        if len(document.canonicals) > 1:
            errors.append(f"duplicate canonical on {route}: {document.canonicals}")
        for value in document.canonicals:
            target = canonical_path(value)
            if target is not None and not route_file(site, target).is_file():
                errors.append(f"canonical target does not exist: {route} -> {target}")

    for route in sorted(required):
        document = documents.get(route)
        if not document:
            continue
        expected = REDIRECTS.get(route, route)
        canonical_ok = len(document.canonicals) == 1
        if canonical_ok:
            value = urlsplit(document.canonicals[0])
            canonical_ok = (
                value.scheme == "https"
                and value.netloc == "neutriverse.uk"
                and unquote(value.path) == expected
                and not value.query
                and not value.fragment
            )
        if not canonical_ok:
            errors.append(f"canonical mismatch on {route}: expected {ORIGIN + expected}, got {document.canonicals}")

    for route in PUBLIC_ROUTES:
        document = documents.get(route)
        if document and (not document.title or not any(value.strip() for value in document.descriptions)):
            errors.append(f"public entrance lacks title or description: {route}")

    for route in NOINDEX_ROUTES:
        document = documents.get(route)
        if document and (
            len(document.robots) != 1
            or "noindex" not in {item.strip().lower() for item in document.robots[0].split(",")}
        ):
            errors.append(f"noindex contract mismatch on {route}: {document.robots}")

    locations = sitemap_locations(site)
    for route in PUBLIC_ROUTES:
        if route not in locations:
            errors.append(f"public entrance missing from sitemap: {route}")
    for route in NOINDEX_ROUTES:
        if route in locations:
            errors.append(f"noindex route leaked into sitemap: {route}")

    robots = (site / "robots.txt").read_text(encoding="utf-8")
    if "Disallow: /ravenis/" in robots:
        errors.append("robots.txt blocks Ravenis and prevents page-level noindex discovery")
    if f"Sitemap: {ORIGIN}/sitemap.xml" not in robots:
        errors.append("robots.txt lacks the absolute canonical sitemap URL")

    actual_redirects: dict[str, str] = {}
    for route, expected in REDIRECTS.items():
        document = documents.get(route)
        if not document:
            continue
        actual = refresh_target(route, document.refreshes)
        if actual != expected:
            errors.append(f"redirect mismatch on {route}: expected {expected}, got {actual}")
        elif actual:
            actual_redirects[route] = actual
    for origin in actual_redirects:
        seen: set[str] = set()
        cursor = origin
        while cursor in actual_redirects:
            if cursor in seen:
                errors.append(f"redirect loop detected from {origin}")
                break
            seen.add(cursor)
            cursor = actual_redirects[cursor]

    broken: set[tuple[str, str]] = set()
    for route, document in documents.items():
        for href in document.links:
            parsed = urlsplit(href)
            if parsed.scheme in {"mailto", "tel", "javascript", "data"}:
                continue
            if parsed.netloc and parsed.netloc != "neutriverse.uk":
                continue
            target = unquote(urlsplit(urljoin(ORIGIN + route, href)).path)
            suffix = Path(target).suffix.lower()
            if suffix and suffix not in {".html", ".htm", ".md"}:
                continue
            if not route_file(site, target).is_file():
                broken.add((route, target))
    for origin, target in sorted(broken):
        errors.append(f"broken internal page link: {origin} -> {target}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_seo_routes.py SITE_DIR", file=sys.stderr)
        return 2
    site = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]
    errors = check(site, repo)
    if errors:
        print("SEO and route validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "SEO and route validation passed: protected routes, canonical targets, noindex/sitemap, "
        "redirects, robots, and internal page links are consistent."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
