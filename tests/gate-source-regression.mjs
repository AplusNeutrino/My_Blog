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
check("Settings filter present", gatePage.includes("data-gate-settings-filter"));
check("Context Launch editor present", gatePage.includes("data-gate-context-launch-list"));
check("Route Group order editor present", gatePage.includes("data-gate-route-order-list"));
check("Config snapshot UI present", gatePage.includes("data-gate-create-snapshot"));

check("Quick Launch editor retained", gatePage.includes("data-gate-cancel-custom-launch"));
check("Route Group rename retained", gatePage.includes("data-gate-cancel-custom-group"));
check("Query preset editor retained", gatePage.includes("data-gate-query-preset-engine"));

check("Context Launch visibility normalized", gateJs.includes("contextLaunchHidden"));
check("Route Group order normalized", gateJs.includes("routeGroupOrder"));
check("Pinned Route Group normalized", gateJs.includes("pinnedRouteGroup"));
check("Snapshot storage isolated", gateJs.includes("neutriverse-gate-config-snapshots-v1"));
check("Settings filter logic present", gateJs.includes("function filterSettingsSections("));
check("Snapshot renderer present", gateJs.includes("function renderSnapshotList()"));
check("Config diagnostics retained", gateJs.includes("function diagnosePreferences("));
check("Rail health sync retained", gateJs.includes("function syncSettingsHealth()"));

check("Custom launch limit retained", gateData.includes("custom_launches: 8"));
check("Custom group limit retained", gateData.includes("custom_route_groups: 4"));
check("Snapshot limit configured", gateData.includes("config_snapshots: 5"));

check("Roadmap packaged", roadmap.includes("Package convention"));
check("V3.4 roadmap recorded", roadmap.includes("V3.4"));

const failed = checks.filter((item) => !item.condition);

checks.forEach((item) => {
  console.log(`${item.condition ? "PASS" : "FAIL"} · ${item.name}`);
});

if (failed.length) {
  console.error(`\n${failed.length} Gate source regression check(s) failed.`);
  process.exit(1);
}

console.log(`\nGate source regression: ${checks.length}/${checks.length} PASS`);
