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

#### V3.2 — next
- Route Group creation beyond the four default groups.
- Optional custom Quick Launch entries rather than only hide/reorder.
- Configuration diagnostics / conflict repair after import.
- Small-screen layout polish after wider real-device testing.

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
