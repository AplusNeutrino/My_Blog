# Neutriverse Shared Design Contract

> Status: authoritative visual and interaction contract for T07–T38
> Route and visibility authority: `docs/neutriverse-route-visibility-map.md`
> Product and execution authority: `NEUTRIVERSE_CONTENT_RESTRUCTURE_PLAN.md`
> Implementation baseline: Night in `assets/css/NormaiNight.css`, Prospero Light in `assets/css/ProsperoLight.css`

This document defines one product with two visual states. It is not a request to replace Jekyll/Chirpy, rewrite content, or make every special application visually identical. When an older sentence, screenshot, CSS selector, or roadmap conflicts with the master plan or route/visibility map, those two documents win.

## 1. Product shell and information architecture

Neutriverse keeps the proven Chirpy shell mechanics—content widths, panel behavior, search, pagination, article rendering and the existing theme controller—but replaces the old first-level tab model with four primary entrances:

| Entrance | Chinese explanation | Route | Visual role |
|---|---|---|---|
| THINK | 我如何思考与表达 | `/think/` | writing, inquiry, signals and records |
| BUILD | 我正在制作什么 | `/build/` | projects, releases and working systems |
| OBSERVE | 我持续观察什么 | `/observe/` | observation interfaces and watched fields |
| ABOUT | 我是谁以及这个站如何生长 | `/about/` | identity, site history and personal connections |

The English name and Chinese explanation are both present in the accessible navigation label or adjacent visible copy. Lore may add a tertiary subtitle, but it never replaces these plain-language labels.

Search, Tags, Archive, RSS, social links and theme switching are secondary utilities. `/categories/`, `/tags/`, `/archives/`, `/thoughts/`, `/library/`, `/links/` and all existing application routes remain reachable according to the route contract; removing them from the first navigation level does not authorize deleting or redirecting them.

## 2. Two states of one facility

Night and Prospero Light express the same hierarchy, semantics, actions and content.

| Role | Night | Prospero Light |
|---|---|---|
| Atmosphere | deep-space observation console | modern arcane archive |
| Canvas | near-black void | sandstone page |
| Primary surface | dark instrument panel | ivory paper |
| Structural accent | signal blue | lapis / turquoise |
| Rare emphasis | restrained signal yellow / violet | old gold / rare violet |
| Depth | borders, low-contrast gradients, sparse stars | layered paper, rules, restrained shadow |
| Tone | operational, quiet, observant | scholarly, archival, operational |

Neither theme may change route availability, sort order, field names, counts, hidden filtering, focus order, accessible names or error meaning. Theme-specific decorative copy may coexist in the HTML through `.theme-copy-night` and `.theme-copy-day`; essential meaning must remain available in both states and may not depend on JavaScript completing.

The existing theme controller remains canonical:

- `data-mode` is the saved user-facing state and `data-bs-theme` mirrors it for Bootstrap/Chirpy compatibility.
- Keep the single `neutriverse-theme-preference` storage key and the existing system-preference fallback.
- New components consume semantic tokens; they do not create a second toggle, storage key or theme-detection script.
- A theme change must not reset filters, scroll position, form values, application state or the current route.
- Initial paint must remain legible if scripts, web fonts or storage access fail.

## 3. Semantic token contract

Shared components should consume the following roles. Existing theme variables may map into them incrementally; this contract does not require a one-shot CSS rename.

| Shared role | Intended use | Night source | Prospero source |
|---|---|---|---|
| `--nv-canvas` | page background | `--night-void` | `--prospero-page` |
| `--nv-surface-1` | primary card/panel | `--night-surface-1` | `--prospero-surface-1` |
| `--nv-surface-2` | raised/secondary controls | `--night-surface-2` | `--prospero-surface-2` |
| `--nv-border` | ordinary divisions | `--night-border` | `--prospero-border` |
| `--nv-border-strong` | selected/structural divisions | `--night-border-strong` | `--prospero-border-strong` |
| `--nv-text` | body text | `--night-text-secondary` | `--prospero-text-secondary` |
| `--nv-text-strong` | headings/primary values | `--night-text-primary` | `--prospero-text-primary` |
| `--nv-text-muted` | secondary metadata | `--night-text-muted` | `--prospero-text-muted` |
| `--nv-accent` | links, focus, active control | `--night-blue` | `--prospero-teal` |
| `--nv-signal` | rare status emphasis | `--night-signal` | `--prospero-gold-ink` |
| `--nv-anomaly` | exceptional state only | `--night-violet` | `--prospero-violet` |
| `--nv-focus` | keyboard focus ring | `--night-blue` | `--prospero-teal` |

Rules:

- Color names stay inside theme palettes; component CSS uses semantic roles.
- Text and interactive state must not rely on color alone. Add label, icon, border, weight or position.
- Gold/yellow and violet are accents, not body text or large background fields.
- New essential text must meet WCAG AA contrast: 4.5:1 for normal text and 3:1 for large text; non-text control boundaries and focus indicators target 3:1 against adjacent colors.
- Gradients, textures and stars are decorative layers with `pointer-events: none`; content stays usable without them.

## 4. Typography and reading measure

Typography has four semantic roles:

| Role | Preferred stack | Use |
|---|---|---|
| Reading | `Noto Serif SC`, `Source Han Serif SC`, `Songti SC`, serif | article prose and essay-led headings in Prospero Light; Night may retain its current readable body face |
| Interface | `Noto Sans SC`, `Source Han Sans SC`, `Microsoft YaHei`, sans-serif | navigation, filters, buttons, forms and compact explanations |
| Inscription | `Cinzel`, `Times New Roman`, serif | short English entrance names, section kickers and lore labels only |
| Data | `IBM Plex Mono`, `Sarasa Mono SC`, UI monospace | dates, versions, counters, status and code |

The hierarchy is semantic before decorative:

- Long-form body text: approximately 17px, line-height 1.75–1.9, reading measure 700–740px.
- General interface/body copy: at least 16px where sustained reading is expected.
- Essential labels and controls: normally at least 12px; smaller telemetry is decorative and must not carry unique meaning.
- English inscriptions use uppercase sparingly with 0.10em–0.14em tracking; Chinese explanations are not letter-spaced to imitate them.
- Headings use real `h1`–`h4` order. Visual size may vary by Type, but heading rank may not be skipped for styling.
- Font loading failure must fall back to a system stack without hiding content or materially changing control dimensions.

Fragment, Note and Essay retain distinct visual rhythm:

- Fragment feels like a timestamped signal.
- Note feels like a compact record.
- Essay feels like a composed work with a stronger opening and quieter long-form body.

Their text, metadata semantics and URLs remain identical across themes.

## 5. Spacing, width and depth

Use an 8px primary rhythm with a 4px micro-step. Preferred values are 4, 8, 12, 16, 24, 32, 48 and 64px. One-off values require a real alignment or target-size reason.

- Control radius: 4–6px; panel/card radius: 6–8px. Pill radius is reserved for tags, statuses and compact filters.
- Normal divisions use 1px borders. Selection may use a stronger border, marker or inset rule without shifting layout.
- Shadows indicate elevation, not ornament. Night prefers borders/tonal layering; Prospero Light may use low-opacity blue-gray/gold shadows.
- Article measure stays near 700–740px. Directory and application surfaces may use the available content shell but must not force article prose to full width.
- Page-level horizontal scrolling is prohibited at supported widths. Code blocks, tables and deliberately horizontal rails scroll inside their own labelled container.

## 6. Shared component contract

New shared components use the `nv-` class prefix and keep one semantic DOM structure across themes. Theme selectors provide tokens and decoration, not duplicate markup.

| Component | Required structure and states | Accessibility contract |
|---|---|---|
| Primary entrance | English name, Chinese explanation, short true summary, canonical link | whole-card link only when nested actions are absent; visible focus; `aria-current="page"` in navigation |
| Section header | plain-language `h1`/`h2`, optional lore kicker, optional count/source note | one heading owner; lore never becomes the only label |
| Record card | heading link, date/status metadata, optional description/tags | DOM reading order matches visual order; no hover-only information |
| Project card | name, sourced status if known, summary, detail link, optional application/repository actions | “了解项目” and “打开工具” remain distinct; absent facts stay absent |
| Filter group | visible label, native links/buttons, selected state, result count or empty state | keyboard reachable; selected state uses text/`aria-pressed`/`aria-current`, not color alone |
| Status / tag | concise label plus optional icon/dot | status meaning remains textual; not the only carrier of errors |
| Empty / loading / error | heading or strong label, explanation, safe next action | loading uses `aria-live` only when useful; retry is a real button; no indefinite decorative spinner as sole feedback |
| Pagination | previous/next plus current page context | disabled controls are not fake links; labels remain understandable out of context |
| Utility link | Search, Tags, Archive, RSS, social or theme action | stays visually secondary but retains 44px mobile target where practical |

Links navigate; buttons change state or perform an action. A clickable `div` is not an acceptable substitute. Disabled and unavailable are separate: unavailable future functions are not rendered as active controls.

## 7. Focus, keyboard and interaction

- Every interactive element has a visible `:focus-visible` indicator: 2px solid `--nv-focus` (or mapped theme accent) with 3px offset unless clipping requires an equivalent inset treatment.
- Focus rings are never removed without a replacement of equal or better visibility.
- Interactive targets are at least 44×44px on mobile where practical. Dense data rows may use a smaller visual control only when surrounding padding preserves the target.
- Menus and disclosures expose correct expanded/current state and retain a predictable tab order.
- Escape closes modal-like overlays and returns focus to the opener. Opening an overlay moves focus only when the overlay is modal or requires immediate input.
- Hover may enhance, never reveal the only route or explanation. All hover behavior has keyboard equivalence.
- Form errors are attached to fields in text; successful operations do not depend only on color or transient toast timing.

## 8. Responsive contract

Required verification viewports are 390, 768, 1024 and 1366px wide.

| Width | Contract |
|---|---|
| 390px | one-column primary flow; no body-level horizontal overflow; navigation, filters and utilities remain operable; primary targets meet mobile sizing |
| 768px | compact/tablet layout may use two columns when each retains readable labels and focus order |
| 1024px | desktop navigation and secondary panel may appear without shrinking article measure below readability |
| 1366px | full shell may show panel/depth details; extra width becomes whitespace or supporting context, not stretched prose |

Additional rules:

- Primary navigation may collapse, but all four entrances and their Chinese explanations remain reachable without hover.
- Controls wrap before labels truncate. If horizontal scrolling is truly intrinsic, the container signals that behavior and keeps focus visible.
- Tables use an internal `.table-wrapper`-style overflow region. Images and canvases use responsive bounds and meaningful fallbacks.
- Fixed controls respect safe areas and the visual viewport. They must not cover focused content or essential actions.
- The Probe Tracking Module, travel globe, Ravenis rails and application workspaces must degrade to readable lists/status when their enhanced layout cannot fit or initialize.

## 9. Motion and reduced motion

Functional transitions use 160–250ms and only the properties needed (`color`, `background-color`, `border-color`, `box-shadow`, `opacity`, `transform`). `transition: all` is prohibited.

- Hover movement is at most 1px and only on fine pointers.
- Decorative rotation, parallax, star movement and nonessential pulsing stop under `prefers-reduced-motion: reduce`.
- Reduced motion does not remove feedback: state changes remain visible immediately through color, border, label or icon.
- No animation delays navigation, blocks reading or creates a persistent full-page effect.
- Auto-advancing media/feeds require pause control or are not used.

## 10. Special surfaces

Special surfaces may have stronger local character while retaining shared behavior.

### Ravenis

Ravenis is a publicly discoverable OBSERVE interface reached from `/observe/`; the application page remains `noindex,nofollow` and outside the sitemap. It is also associated with a BUILD entity. Public discovery does not authorize exposing unpublished data or changing its release pipeline.

- It inherits the saved Night/Prospero Light preference and keeps a clear route back to OBSERVE/Neutriverse.
- The first viewport answers what changed, what matters and what to verify next.
- Search keyword is primary; secondary filters wrap and never overflow the viewport.
- Date/slot navigation exposes real availability. Missing runs are absent or disabled; legacy/fallback ranking is labelled honestly.
- Search reports the true match count before any display cap.
- Controls keep visible labels, focus indicators, keyboard operation, mobile targets and reduced-motion behavior.
- Data loading remains incremental: current manifest/day first, historical search data only when requested.

### Occult Atlas

Occult Atlas is publicly discoverable from `/observe/`; `/occult-atlas/` remains `noindex`, and `/occult-atlas-app/` remains only a compatibility entrance.

- Reuse the canonical theme controller; do not introduce a second preference store.
- Preserve chart state, API behavior and old-entry compatibility across theme/navigation changes.
- Canvas/color information has a textual or labelled equivalent for controls and errors.
- Provide a clear return to OBSERVE/Neutriverse without creating a redirect loop.

### Gate and NAVI

Gate and NAVI retain their existing URLs and hidden-discovery level. A public BUILD description of Gate may exist, but the tool entrance is not promoted into the global primary navigation.

- Standalone styling may remain denser than the main shell, but essential labels, focus, keyboard operation, reduced motion and 390px containment still apply.
- Tiny telemetry is decorative; any unique instruction or state is repeated at a readable size.
- Private navigation data remains free of credentials, account-only URLs or unpublished personal information.

### Library, friends and travel globe

These are ABOUT relationships, not new top-level entrances. `/library/` and `/links/` remain independent pages; the travel globe stays embedded in ABOUT. Entry reorganization must not duplicate or rewrite their data sources, privacy filters, associations or travel records.

## 11. Implementation boundaries

T07 defines the contract; later tasks implement it incrementally.

- T08 creates truthful four-entrance data/page skeletons and reusable navigation markup.
- T09/T10 implement desktop/mobile navigation, active state, keyboard and collapse behavior.
- T11–T17 apply record/filter/empty-state rules to THINK.
- T21–T29 apply project/observation/about component rules without copying protected data sources.
- T30/T31 perform the full shared visual, responsive and accessibility pass.

Do not perform broad CSS rewrites merely to rename tokens. Map existing stable variables, add shared roles when a component needs them, and keep diffs attributable to the task being implemented.

## 12. Verification checklist

Every new or materially changed shared component must verify:

1. Night and Prospero Light show the same content, actions and state.
2. Default, hover, focus-visible, active/current, disabled, loading, empty and error states relevant to that component are defined.
3. Keyboard order follows the semantic DOM; focus remains visible and recoverable.
4. 390 / 768 / 1024 / 1366px checks show no body-level horizontal overflow.
5. Normal text/control contrast meets the targets in Section 3.
6. `prefers-reduced-motion: reduce` keeps feedback while removing decorative motion.
7. No hidden/noindex/private boundary is widened by styling or navigation changes.
8. Old routes and application return paths remain reachable.
9. Article/Fragment text and protected metadata are unchanged.
10. Automated tests and the exact implementation SHA's Pages workflow pass before the task is marked done.
