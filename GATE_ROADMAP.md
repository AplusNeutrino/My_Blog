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
- Local Conditions weather module.
- Weather location requested only on explicit user action.
- Weather cache and graceful offline fallback.
- Next: proper command-palette suggestions/history.
- Next: Today/Calendar integration only after choosing a privacy-safe calendar strategy.

### V3 · Dashboard
- Focus / Dashboard modes.
- Bento-style secondary modules.
- Bookmark groups by context (WORK / KNOWLEDGE / MEDIA / SYSTEM), not app categories.
- Projects.
- Widget show/hide/reorder; resize only where it adds value.
- Settings drawer.

### V4 · Personal OS
- Optional authenticated sync.
- NAS / home-server status.
- Tasks.
- RSS only as an opt-in secondary module.
- PWA/offline caching after the current site's PWA policy is revisited.
- API secrets must never ship to the browser.

## Calendar decision

Do not expose a private Google Calendar token or private ICS URL in static frontend code.

Preferred future options:
1. backend/BFF with OAuth and scoped calendar read access;
2. deliberately public calendar feed for non-sensitive events;
3. local-only manual agenda.

Until one is intentionally selected, Gate should not fake a calendar integration.

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
