# Neutriverse Gate V1

Copy the contents of this folder into the repository root of `AplusNeutrino/My_Blog`.

Target URL after deployment:

`https://neutriverse.uk/gate/`

Files:
- `_layouts/gate.html`
- `_data/gate.yml`
- `gate/index.md`
- `assets/css/gate.css`
- `assets/js/gate.js`

No existing production file needs to be edited.

Main functions:
- Night / Prospero theme support
- Local clock / timezone
- Query array with prefixes: `g`, `ddg`, `gh`, `yt`, `wiki`, `map`, `ai`
- URL and internal `/route` navigation
- Commands: `> theme light`, `> theme dark`, `> theme toggle`, `> note ...`, `> clear note`, `> open github`, `> home`
- Eight configurable quick launch routes
- Browser-local Field Record
- Online/offline indicator
- Responsive mobile facility rail
- `noindex,nofollow`

PowerShell:

```powershell
git checkout -b agent/neutriverse-gate-prototype
git add _layouts/gate.html _data/gate.yml gate/index.md assets/css/gate.css assets/js/gate.js
git commit -m "add neutriverse gate prototype"
git push -u origin agent/neutriverse-gate-prototype
```

To publish to the current GitHub Pages workflow, merge the branch into `main`.
