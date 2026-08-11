# Neutriverse Gate Roadmap

This document is the durable design memory for `https://neutriverse.uk/gate/`.

## Product identity

Gate is not a generic start-page dashboard. It is a personal navigation terminal
inside the Neutriverse facility language.

- Night: deep-space observation / transit console.
- Prospero Light: sandstone paper, lapis structure, old-gold rules, turquoise interaction.
- Visual tone: scholarly, operational, restrained.
- World-building terminology must never reduce usability.

## Core principles

1. First viewport answers: what time is it, what do I want to find, where do I want to go.
2. Search / command execution is the primary interaction.
3. Night and Prospero are two authored states, never an automatic color inversion.
4. Gate reuses existing Neutriverse design tokens; avoid a parallel palette.
5. No wallpaper feed, news feed, stock ticker, quote-of-the-day, or icon wall by default.
6. Keyboard access is first-class.
7. Private information stays local unless a deliberate backend integration is added.
8. Gate should remain useful when optional APIs fail.
9. Desktop Facility Rail is viewport-fixed; mobile uses a bottom facility rail.
10. Motion is functional and reduced-motion safe.

## Architecture

- `/gate/` — public URL but `noindex,nofollow`.
- `_layouts/gate.html` — standalone shell.
- `_data/gate.yml` — static link/provider configuration.
- `assets/css/gate.css` — Gate-only styling using Neutriverse tokens.
- `assets/js/gate.js` — browser-local interactions and optional API modules.

## Development stages

### V1 · Start / Transit
- Clock and local timezone.
- Query Array.
- URL and internal route execution.
- Search prefixes.
- Eight Quick Launch routes.
- Night / Prospero theme.
- Responsive Facility Rail.
- Field Record in localStorage.
- Online/offline status.

### V2 · Productivity
- Command mode (`> ...`).
- Local Conditions weather module with explicit opt-in location.
- Current Vector with browser-local editable override.
- Query Array suggestions with keyboard navigation.
- Recent Transits inside Query Array without storing full search text.
- Settings Drawer:
  - default search engine;
  - standard / compact density;
  - ambient graphics toggle;
  - module visibility;
  - Quick Launch visibility and ordering;
  - browser-local data cleanup.
- `Cmd/Ctrl + ,` opens System Configuration.
- Today / Calendar is intentionally not part of Gate.

### V3 · Composable Gate

#### V3.0 — implemented
- Context Route Matrix with four modes:
  - WORK;
  - KNOWLEDGE;
  - MEDIA;
  - SYSTEM.
- Route Matrix is a compact strip, not another large dashboard card.
- Selected Route Matrix group is browser-local and keyboard accessible.
- Dashboard module order is configurable in Settings.
- Current Vector / Local Conditions / Active Systems / Field Record participate in ordering.
- Visible dashboard section numbers update after reordering/hiding.
- V2.2 preferences migrate forward to the V3 settings schema.

#### V3.1 — implemented
- Focus / Dashboard presentation modes.
  - Focus keeps Clock / Query / Launch / Route Matrix.
  - Focus hides secondary dashboard modules.
  - Toggle from Facility Rail, Settings, `> focus`, `> dashboard`, or `Cmd/Ctrl + Shift + F`.
- Route Group local overrides.
  - Edit the four routes inside WORK / KNOWLEDGE / MEDIA / SYSTEM.
  - Custom label, detail, and URL.
  - URL validation allows only root-relative, HTTP, and HTTPS routes.
- Dashboard width presets.
  - STANDARD;
  - WIDE;
  - FIELD RECORD remains FULL.
- Configuration export/import.
  - JSON file for cross-browser migration.
  - Includes Gate preferences, layout, route overrides, and Current Vector.
  - Explicitly excludes weather coordinates, Recent Transits, and Field Record.

#### V3.2 — implemented
- Custom Quick Launch entries.
  - Add browser-local label / role / URL.
  - Hide, reorder, or delete alongside the repository defaults.
  - Maximum 8 custom entries.
- Custom Route Groups.
  - Add up to 4 browser-local groups beyond WORK / KNOWLEDGE / MEDIA / SYSTEM.
  - Four route slots per group.
  - Custom groups participate in Route Matrix, keyboard navigation, Query Suggestions, Recent Transits, and config export/import.
- Configuration diagnostics and repair.
  - Detect malformed settings, duplicate/unknown IDs, excessive custom objects, unavailable Route Groups, and invalid custom URLs.
  - Repair normalizes the Gate settings schema without touching weather/history/Field Record.
  - Imports are normalized before activation and can report repaired issues.
- Small-screen polish.
  - Route Group tabs scroll horizontally instead of compressing indefinitely.
  - Settings drawer uses dynamic viewport height and safe-area padding.
  - Query Suggestions gain a bounded mobile scroll region.
  - Very narrow screens collapse Quick Launch to one column.

#### V3.3 — implemented
- Custom Quick Launch in-place editing.
  - Edit label / role / URL without deleting and recreating the entry.
  - Existing stable local ID and Launch order are preserved.
- Custom Route Group rename/edit.
  - Edit group label and detail while preserving group ID, routes, active state, and Query presets.
- Context-specific Query presets.
  - Each Route Group can optionally override the global default search engine.
  - Each Route Group can provide its own Query Array placeholder.
  - Explicit search prefixes still override the context preset.
- Facility Rail configuration health.
  - Settings control shows nominal/warning state without opening the drawer.
  - Health state derives from the same diagnostics engine used by CONFIG DIAGNOSTICS.
- Repository source regression test.
  - `node tests/gate-source-regression.mjs`
  - Guards critical Gate structure, Prospero/fixed-Rail regressions, V3.3 controls, and roadmap packaging.
  - This is source-level regression coverage; browser E2E remains separate.

#### V3.4 — implemented
- Context-specific Quick Launch visibility.
  - Each Route Group can add an extra local hidden set on top of global Launch visibility.
  - Global hidden state always wins.
  - Custom Launch additions/deletions are normalized automatically against Context rules.
- Route Group ordering and pinning.
  - Reorder all default and custom Route Groups.
  - Pin one Route Group to the first Matrix position without destroying its underlying order.
  - Pin state is browser-local and exported with normal Gate preferences.
- Settings search/filter.
  - Filter the growing Settings drawer by section text without adding another navigation layer.
  - Filtering is local UI state and is not persisted.
- Configuration snapshots / restore points.
  - Up to 5 browser-local snapshots.
  - Snapshot contains Gate preferences and Current Vector.
  - Snapshots explicitly exclude weather location/cache, Recent Transits, Field Record, and shared theme preference.
  - Snapshots are stored outside the main Gate preferences object and are not recursively exported.
- Diagnostics extended for:
  - Route Group order;
  - pinned Route Group;
  - Context Launch visibility rules.
- Source regression suite expanded to cover V3.4 controls and schema.

#### V3.5 — next
- Snapshot rename and optional diff preview before restore.
- Context profile summary showing Search + Launch + Route behavior in one place.
- Optional Route Group keyboard shortcuts.
- Settings section anchors / quick navigation if filtering alone becomes insufficient.
- Real-browser E2E regression suite when a reliable browser runtime is available.

### V4 · Personal OS
- Optional authenticated sync.
- NAS / home-server status.
- Tasks.
- RSS only as an opt-in secondary module.
- PWA/offline caching after the current site's PWA policy is revisited.
- API secrets must never ship to the browser.

## Calendar / Today decision

Gate intentionally does not include a Today or Calendar module.

Reason:
- Gate is a browser transit terminal, not a productivity dashboard.
- Calendar OAuth would introduce private-account complexity into a static start page.
- Current Vector provides a better "continue what I am doing" primitive.
- If calendar information is ever added, it should be an optional secondary module rather than a core dependency.

## Interaction vocabulary

Night examples:
- TRANSIT MODULE
- QUERY ARRAY
- LAUNCH ROUTES
- FIELD RECORD
- ACTIVE SYSTEMS
- LOCAL CONDITIONS

Prospero may use archive/reference language, but labels for real services remain literal.

## Performance targets

Core UI (clock, query, launch routes) must not wait for any network API.
Weather, calendar, server status, and future integrations load asynchronously.


## Package convention

Every future Gate release ZIP must include the current `docs/GATE_ROADMAP.md`.
The roadmap is part of the deliverable, not an optional side file.
