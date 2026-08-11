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
check("Settings jump navigation present", gatePage.includes("data-gate-settings-jump"));
check("Context Profile present", gatePage.includes("data-gate-context-profile-group"));
check("Snapshot diff panel present", gatePage.includes("data-gate-snapshot-diff-list"));

check("Context Launch editor retained", gatePage.includes("data-gate-context-launch-list"));
check("Route Group order editor retained", gatePage.includes("data-gate-route-order-list"));
check("Config snapshot UI retained", gatePage.includes("data-gate-create-snapshot"));
check("Quick Launch editor retained", gatePage.includes("data-gate-cancel-custom-launch"));
check("Route Group rename retained", gatePage.includes("data-gate-cancel-custom-group"));
check("Query preset editor retained", gatePage.includes("data-gate-query-preset-engine"));

check("Context profile logic present", gateJs.includes("function syncContextProfile("));
check("Route shortcut labels present", gateJs.includes("data.gateShortcut") || gateJs.includes("dataset.gateShortcut"));
check(
  "Route keyboard shortcut present",
  gateJs.includes("event.altKey") &&
    gateJs.includes("/^[1-9]$/.test(event.key)")
);
check("Settings jump logic present", gateJs.includes("settingsJumpSelect?.addEventListener"));
check("Snapshot rename present", gateJs.includes("function renameConfigSnapshot("));
check("Snapshot diff summary present", gateJs.includes("function snapshotDiffSummary("));
check("Snapshot restore preview present", gateJs.includes("showSnapshotDiff(snapshot.id)"));
check("Snapshot timestamp noise excluded", gateJs.includes("description: vector.description"));

check("Context Launch visibility retained", gateJs.includes("contextLaunchHidden"));
check("Route Group order retained", gateJs.includes("routeGroupOrder"));
check("Pinned Route Group retained", gateJs.includes("pinnedRouteGroup"));
check("Snapshot storage isolated", gateJs.includes("neutriverse-gate-config-snapshots-v1"));
check("Config diagnostics retained", gateJs.includes("function diagnosePreferences("));
check("Rail health sync retained", gateJs.includes("function syncSettingsHealth()"));

check("Custom launch limit retained", gateData.includes("custom_launches: 8"));
check("Custom group limit retained", gateData.includes("custom_route_groups: 4"));
check("Snapshot limit retained", gateData.includes("config_snapshots: 5"));
check("Route shortcuts enabled", gateData.includes("route_shortcuts: true"));

check("Roadmap packaged", roadmap.includes("Package convention"));
check("V3.5 roadmap recorded", roadmap.includes("V3.5"));

const failed = checks.filter((item) => !item.condition);

checks.forEach((item) => {
  console.log(`${item.condition ? "PASS" : "FAIL"} · ${item.name}`);
});

if (failed.length) {
  console.error(`\n${failed.length} Gate source regression check(s) failed.`);
  process.exit(1);
}

console.log(`\nGate source regression: ${checks.length}/${checks.length} PASS`);
