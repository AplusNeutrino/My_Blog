#!/usr/bin/env python3
"""Validate resource scoping and graceful integration contracts in a built site."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import sys


PRIMARY_ROUTES = ("/", "/think/", "/build/", "/observe/", "/about/")
SCOPED_TOKENS = (
    "/assets/pgl/",
    "/assets/js/ravenis.js",
    "/occult-atlas-app/app.js",
    "/assets/js/travel-globe.js",
    "/assets/js/travel-globe-worker.js",
)


class Resources(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.scripts: list[dict[str, str | None]] = []
        self.links: list[dict[str, str | None]] = []
        self.attrs: list[dict[str, str | None]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        self.attrs.append(values)
        if tag == "script":
            self.scripts.append(values)
        elif tag == "link":
            self.links.append(values)


def route_file(site: Path, route: str) -> Path:
    return site / ("index.html" if route == "/" else route.strip("/") + "/index.html")


def read_route(site: Path, route: str, errors: list[str]) -> tuple[str, Resources]:
    path = route_file(site, route)
    if not path.is_file():
        errors.append(f"missing built route: {route} ({path})")
        return "", Resources()
    text = path.read_text(encoding="utf-8")
    parser = Resources()
    parser.feed(text)
    return text, parser


def urls(parser: Resources) -> list[str]:
    return [str(item.get("src") or item.get("href") or "") for item in parser.scripts + parser.links]


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate(site: Path, source_root: Path) -> list[str]:
    errors: list[str] = []

    for route in PRIMARY_ROUTES:
        text, parser = read_route(site, route, errors)
        resources = urls(parser)
        for token in SCOPED_TOKENS:
            require(not any(token in value for value in resources), f"{route} loads scoped resource {token}", errors)
        require(any("NormaiNight.css" in value for value in resources), f"{route} lost Night theme CSS", errors)
        require(any("ProsperoLight.css" in value for value in resources), f"{route} lost Prospero Light CSS", errors)
        require(
            any(item.get("rel") == "alternate" and item.get("type") == "application/atom+xml" and "/feed.xml" in str(item.get("href")) for item in parser.links),
            f"{route} lost Atom discovery",
            errors,
        )
        require("data-post-like" not in text or "data-like-endpoint" in text, f"{route} has incomplete like markup", errors)

    library_text, library = read_route(site, "/library/", errors)
    pgl_scripts = [item for item in library.scripts if "/assets/pgl/pgl.js" in str(item.get("src"))]
    require(len(pgl_scripts) == 1, "/library/ must load exactly one PGL controller", errors)
    require(bool(pgl_scripts and "defer" in pgl_scripts[0]), "/library/ PGL controller must remain deferred", errors)
    require("data-library-url=" in library_text and "data-stats-url=" in library_text, "/library/ lost data endpoints", errors)
    require(not any("library.json" in str(item.get("src")) or "stats.json" in str(item.get("src")) for item in library.scripts), "/library/ directly scripts data JSON", errors)

    _, ravenis = read_route(site, "/ravenis/", errors)
    ravenis_urls = urls(ravenis)
    require(any("/assets/js/ravenis.js" in value for value in ravenis_urls), "/ravenis/ lost its controller", errors)
    for token in ("/assets/pgl/", "/occult-atlas-app/app.js", "/assets/js/travel-globe.js"):
        require(not any(token in value for value in ravenis_urls), f"/ravenis/ loads unrelated resource {token}", errors)

    _, occult = read_route(site, "/occult-atlas/", errors)
    occult_urls = urls(occult)
    require(any("/occult-atlas-app/app.js" in value for value in occult_urls), "/occult-atlas/ lost its controller", errors)
    for token in ("/assets/pgl/", "/assets/js/ravenis.js", "/assets/js/travel-globe.js"):
        require(not any(token in value for value in occult_urls), f"/occult-atlas/ loads unrelated resource {token}", errors)

    # Select a real built post by its integration markers rather than guessing
    # Jekyll's case-sensitive slug normalization from a source filename.
    post_text = ""
    post = Resources()
    for path in site.rglob("*.html"):
        candidate = path.read_text(encoding="utf-8", errors="replace")
        if "data-post-like" not in candidate or 'id="twikoo-comments"' not in candidate:
            continue
        post_text = candidate
        post.feed(candidate)
        break
    require(bool(post_text), "no built public post exposes both comments and likes", errors)
    if post_text:
        require(not any("twikoo" in str(item.get("src")).lower() for item in post.scripts), "post parser-loads Twikoo", errors)
        require("data-twikoo-status" in post_text and "评论服务暂时不可用" in post_text, "post lost visible Twikoo fallback", errors)
        require("data-like-endpoint" in post_text, "post lost like integration markers", errors)

    pgl_source = (source_root / "assets/pgl/pgl.js").read_text(encoding="utf-8")
    require("function loadLibraryData()" in pgl_source and "requestIdleCallback" in pgl_source, "PGL lazy/idle loader contract missing", errors)
    require("if (state.view !== 'index')" in pgl_source and "pointerdown" in pgl_source and "focusin" in pgl_source, "PGL direct-view or interaction loading contract missing", errors)

    twikoo_source = (source_root / "_includes/comments/twikoo.html").read_text(encoding="utf-8")
    require("script.async = true" in twikoo_source and "IntersectionObserver" in twikoo_source, "Twikoo async/near-viewport contract missing", errors)
    require("envId:" in twikoo_source and "path:" in twikoo_source and "lang:" in twikoo_source, "Twikoo provider context changed", errors)

    ravenis_source = (source_root / "assets/js/ravenis.js").read_text(encoding="utf-8")
    require(ravenis_source.count("fetchSearchIndex()") == 2, "Ravenis search index is no longer search-on-demand", errors)
    require("fetchJSON('manifest.json')" in ravenis_source, "Ravenis manifest bootstrap changed", errors)

    likes_source = (source_root / "_includes/post-like.html").read_text(encoding="utf-8")
    require("localStorage.getItem" in likes_source and "localStorage.setItem" in likes_source, "like local fallback changed", errors)
    require("data-like-endpoint" in likes_source and "fetch(`${endpoint}${hitPath}`" in likes_source, "like endpoint contract changed", errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path)
    parser.add_argument("--source-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.site.resolve(), args.source_root.resolve())
    if errors:
        print("Resource and integration validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Resource and integration validation passed for primary routes, scoped applications, comments, likes, and data loaders.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
