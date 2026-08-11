import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const root = process.cwd();

const read = (relative) =>
  fs.readFileSync(path.join(root, relative), "utf8");

const gateJs = read("assets/js/gate.js");
const gateCss = read("assets/css/gate.css");
const gatePage = read("gate/index.md");
const gateData = read("_data/gate.yml");
const roadmap = read("docs/GATE_ROADMAP.md");

const checks = [];

function check(name, condition) {
  checks.push({ name, condition: Boolean(condition) });
}

check("Gate permalink retained", gatePage.includes("permalink: /gate/"));
check("Facility Rail fixed viewport retained", gateCss.includes("height: 100dvh;"));
check(
  "Prospero Light owns Gate accent",
  gateCss.includes("--gate-accent: var(--prospero-teal")
);

check("Settings health indicator retained", gatePage.includes("data-gate-settings-health"));
check("Settings filter retained", gatePage.includes("data-gate-settings-filter"));
check("Settings jump navigation retained", gatePage.includes("data-gate-settings-jump"));

check("Context Profile retained", gatePage.includes("data-gate-context-profile-group"));
check("Context Profile copy action present", gatePage.includes("data-gate-copy-context-profile"));
check("Context Profile export action present", gatePage.includes("data-gate-export-context-profile"));

check("Route shortcut preference UI present", gatePage.includes("data-gate-setting-route-shortcuts"));
check("Route shortcut preference normalized", gateJs.includes("routeShortcuts: raw.routeShortcuts !== false"));
check("Route keyboard shortcut uses preference", gateJs.includes("preferences.routeShortcuts"));
check("Route shortcut diagnostics present", gateJs.includes("Route shortcut preference is malformed"));

check("Snapshot diff panel retained", gatePage.includes("data-gate-snapshot-diff-list"));
check("Snapshot tag input present", gatePage.includes("data-gate-snapshot-tag"));
check("Snapshot reason input present", gatePage.includes("data-gate-snapshot-reason"));
check("Snapshot record normalization present", gateJs.includes("function normalizeSnapshotRecord("));
check("Snapshot last-restored metadata present", gateJs.includes("lastRestoredAt"));
check("Snapshot detailed Launch diff present", gateJs.includes("function customLaunchDiffDetails("));
check("Snapshot detailed Context diff present", gateJs.includes("function routeContextDiffDetails("));
check("Snapshot Query preset diff present", gateJs.includes("function queryPresetDiffDetails("));
check("Snapshot Dashboard diff present", gateJs.includes("function dashboardDiffDetails("));
check("Snapshot timestamp noise excluded", gateJs.includes("description: vector.description"));

check("Context profile payload present", gateJs.includes("function contextProfilePayload("));
check("Context profile clipboard export present", gateJs.includes("function copyContextProfile("));
check("Context profile JSON export present", gateJs.includes("function exportContextProfile("));

check("Context Launch visibility retained", gateJs.includes("contextLaunchHidden"));
check("Route Group order retained", gateJs.includes("routeGroupOrder"));
check("Pinned Route Group retained", gateJs.includes("pinnedRouteGroup"));
check("Config snapshot storage isolated", gateJs.includes("neutriverse-gate-config-snapshots-v1"));
check("Config diagnostics retained", gateJs.includes("function diagnosePreferences("));
check("Rail health sync retained", gateJs.includes("function syncSettingsHealth()"));

check("Custom launch limit retained", gateData.includes("custom_launches: 8"));
check("Custom group limit retained", gateData.includes("custom_route_groups: 4"));
check("Snapshot limit retained", gateData.includes("config_snapshots: 5"));
check("Route shortcuts default enabled", gateData.includes("route_shortcuts: true"));

check("Export format updated to 3.6", gateJs.includes('version: "3.6"'));
check("Roadmap packaged", roadmap.includes("Package convention"));
check("V3.6 roadmap recorded", roadmap.includes("V3.6"));

const failed = checks.filter((item) => !item.condition);

checks.forEach((item) => {
  console.log(`${item.condition ? "PASS" : "FAIL"} · ${item.name}`);
});

if (failed.length) {
  console.error(`\n${failed.length} Gate source regression check(s) failed.`);
  process.exit(1);
}

console.log(`\nGate source regression: ${checks.length}/${checks.length} PASS`);
