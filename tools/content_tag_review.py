#!/usr/bin/env python3
"""Render the T04 tag second-pass audit from current writing metadata.

The tool is read-only unless ``--output`` is supplied. It deliberately treats
frequency as evidence, not as an automatic deletion rule.
"""

import argparse
from collections import Counter, defaultdict
from pathlib import Path

from content_restructure_baseline import build


SOURCE_SHA = "b2a2a15321efb0c443b57f001368227105b1cdce"

# The second pass is intentionally small. Every unspecified current tag is kept.
DECISIONS = {
    "Bus": (
        "MERGE",
        "System Bus",
        "与现有 `System Bus` 指向同一硬件互连概念；统一命名可形成跨文章检索。",
    ),
    "Changelog": (
        "RETIRE",
        "—",
        "编辑形式而非主题；同篇仍有 `Neutriverse` 与 `Jekyll`，检索信息不会丢失。",
    ),
}

NAMED_WORKS_OR_ENTITIES = {
    "Akasha Notes",
    "Ernest Becker",
    "Final Fantasy",
    "Final Fantasy II",
    "Final Fantasy XIV",
    "Garlean Empire",
    "Nhalmasque",
    "Neutriverse",
    "Toyosatomimi's Headphone",
    "Z.A.T.O.",
}


def item_key(item):
    if item.get("path"):
        path = Path(item["path"])
        label = path.stem
        return f"H:{label}" if item.get("hidden") else label
    return f"F:{item['date']}"


def keep_reason(tag, count, public_count, fragment_tags):
    if public_count == 0:
        return "具体概念仅用于 hidden 内容；不以可见性替代语义判断，公开索引过滤交由 T05/T17。"
    if tag in fragment_tags:
        return "保留 Fragment 原有检索词与语言；未发现同义冲突，不为统一英文而改写。"
    if tag in NAMED_WORKS_OR_ENTITIES:
        return "命名作品、人物或实体，具有直接检索价值；即使单次出现也保留。"
    if count > 1:
        return f"已在 {count} 个内容项复用，且未与 Type、Topic 或 Series 重复。"
    return "具体技术概念或分析主题；未发现同义/结构重复，单次出现不是删除理由。"


def collect():
    inventory = build()
    items = inventory["posts"] + inventory["fragments"]
    uses = defaultdict(list)
    fragment_tags = set()
    for item in items:
        for tag in item["tags"]:
            uses[tag].append(item)
            if not item.get("path"):
                fragment_tags.add(tag)

    rows = []
    for tag in sorted(uses, key=str.casefold):
        tagged = uses[tag]
        public_count = sum(not item.get("hidden") for item in tagged)
        hidden_count = len(tagged) - public_count
        action, target, reason = DECISIONS.get(
            tag,
            ("KEEP", "—", keep_reason(tag, len(tagged), public_count, fragment_tags)),
        )
        rows.append(
            {
                "tag": tag,
                "count": len(tagged),
                "public": public_count,
                "hidden": hidden_count,
                "action": action,
                "target": target,
                "reason": reason,
                "items": ", ".join(item_key(item) for item in tagged),
            }
        )
    return inventory, rows


def render():
    inventory, rows = collect()
    frequency = Counter(row["count"] for row in rows)
    assignments = sum(row["count"] for row in rows)
    hidden_only = sum(row["public"] == 0 for row in rows)
    mixed = sum(row["public"] > 0 and row["hidden"] > 0 for row in rows)
    projected_unique = len(rows) - 2  # Bus merges into an existing tag; Changelog retires.
    projected_assignments = assignments - 1  # merge preserves one use; retirement removes one.

    lines = [
        "# Neutriverse Tag Second-Pass Review",
        "",
        f"> T04 artifact, 2026-10-04. Source head: `{SOURCE_SHA}`. ",
        "> Scope: 44 posts and 5 Fragments. This is a decision audit; T04 does not edit content metadata.",
        "",
        "## Method and guardrails",
        "",
        "- Read the current `tags` arrays from all 49 writing items; visibility is recorded separately from semantic value.",
        "- Compare exact names and meanings against Type, Topic, Series and the first-pass canonical map.",
        "- A one-off tag is kept when it names a work/entity, technical concept or concrete analytical theme.",
        "- T04 proposes only finite changes. T05 applies accepted metadata edits and compatibility routes; T17 completes public-index filtering.",
        "- Item references use `H:` for hidden posts and `F:` for Fragments.",
        "",
        "## Inventory summary",
        "",
        "| Measure | Current | After proposed T05 changes |",
        "|---|---:|---:|",
        f"| Writing items | {len(inventory['posts']) + len(inventory['fragments'])} | 49 |",
        f"| Unique tags | {len(rows)} | {projected_unique} |",
        f"| Tag assignments | {assignments} | {projected_assignments} |",
        f"| Used once | {frequency[1]} | n/a until T05 |",
        f"| Used twice | {frequency[2]} | n/a until T05 |",
        f"| Used three times | {frequency[3]} | n/a until T05 |",
        f"| Hidden-only tags | {hidden_only} | semantic tags retained; public listing filtered separately |",
        f"| Mixed public/hidden tags | {mixed} | unchanged |",
        "",
        "The frequency distribution is sparse, but that reflects a small and varied archive. It is not evidence that named works or precise concepts should be deleted.",
        "",
        "## Finite change set for T05",
        "",
        "| Current tag | Decision | Canonical target | Metadata effect | Legacy tag URL strategy |",
        "|---|---|---|---|---|",
        "| `Bus` | MERGE | `System Bus` | Replace one assignment; target then has two uses. | Preserve `/tags/bus/` as a noindex redirect stub to `/tags/system-bus/`. |",
        "| `Changelog` | RETIRE | — | Remove one editorial-form assignment; keep `Neutriverse` and `Jekyll`. | Preserve `/tags/changelog/` as a noindex redirect stub to `/tags/neutriverse/`. |",
        "",
        "No other tag change is proposed. In particular, hidden-only tags remain semantically intact: deleting metadata is not a substitute for fixing public tag indexes. Fragment tags remain in their existing language, and one-off works/entities remain available for future retrieval.",
        "",
        "## Complete decision inventory",
        "",
        "| Tag | Uses | Public | Hidden | Decision | Target | Reason | Item references |",
        "|---|---:|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        tag = row["tag"].replace("|", "\\|")
        reason = row["reason"].replace("|", "\\|")
        items = row["items"].replace("|", "\\|")
        lines.append(
            f"| `{tag}` | {row['count']} | {row['public']} | {row['hidden']} | "
            f"{row['action']} | `{row['target']}` | {reason} | {items} |"
        )
    lines += [
        "",
        "## T05 handoff",
        "",
        "1. Change only the two assignments listed above and update the authoritative migration audit/final counts.",
        "2. Add the two explicit legacy tag route stubs before generated archive pages disappear.",
        "3. Make public tag aggregation count/list only non-hidden posts; do not expose hidden-only names through the public index or trending tags.",
        "4. Re-run the content-protection baseline so article/Fragment bodies and protected URL metadata remain unchanged.",
        "5. Verify the exact implementation SHA with regression tests, Jekyll build and Pages deployment.",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    content = render()
    if args.check:
        if args.check.read_text(encoding="utf-8") != content:
            raise SystemExit(f"tag review differs from {args.check}")
        print(f"tag review matches {args.check}")
        return
    if args.output:
        args.output.write_text(content, encoding="utf-8")
        print(args.output)
        return
    print(content, end="")


if __name__ == "__main__":
    main()
