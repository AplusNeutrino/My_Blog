(() => {
  "use strict";

  const root = document.documentElement;
  const app = document.querySelector("[data-gate-app]");

  if (!app) {
    return;
  }

  const qs = (selector) => app.querySelector(selector);
  const qsa = (selector) => [...app.querySelectorAll(selector)];

  const storage = {
    get(key) {
      try {
        return localStorage.getItem(key);
      } catch {
        return null;
      }
    },
    set(key, value) {
      try {
        localStorage.setItem(key, value);
      } catch {
        /* Restricted/private browsing can deny localStorage. */
      }
    },
    remove(key) {
      try {
        localStorage.removeItem(key);
      } catch {
        /* Restricted/private browsing can deny localStorage. */
      }
    },
  };

  function readJson(key, fallback = null) {
    try {
      const value = storage.get(key);
      return value ? JSON.parse(value) : fallback;
    } catch {
      return fallback;
    }
  }

  function writeJson(key, value) {
    storage.set(key, JSON.stringify(value));
  }

  function parseConfig(id, fallback = {}) {
    try {
      return JSON.parse(document.getElementById(id)?.textContent || "{}");
    } catch {
      return fallback;
    }
  }

  // ---------------------------------------------------------------------------
  // Static configuration / DOM references
  // ---------------------------------------------------------------------------

  const engines = parseConfig("gate-search-config", {});
  const vectorDefault = parseConfig("gate-vector-config", {});
  const settingsDefault = parseConfig("gate-settings-config", {});
  const routeGroupsDefault = parseConfig("gate-route-groups-config", []);

  const searchForm = qs("[data-gate-search]");
  const searchInput = qs("[data-gate-search-input]");
  const queryState = qs("[data-gate-query-state]");
  const suggestionsNode = qs("[data-gate-suggestions]");
  const modeToggleButton = qs("[data-gate-mode-toggle]");
  const modeLabelNode = qs("[data-gate-mode-label]");
  const settingsHealthNode = qs("[data-gate-settings-health]");

  const launchGrid = qs("[data-gate-launch-grid]");
  let launchNodes = qsa("[data-gate-launch]");
  const routeNodes = qsa("[data-gate-route]");
  const vectorLinkNodes = qsa("[data-gate-vector-link]");
  let contextRouteNodes = qsa("[data-gate-context-route]");
  let routeGroupTabs = qsa("[data-gate-route-group-tab]");
  let routeGroupPanels = qsa("[data-gate-route-group-panel]");
  const contextTabsNode = qs(".gate-context-tabs");
  const contextPanelsNode = qs(".gate-context-panels");
  const dashboardGrid = qs("[data-gate-dashboard-grid]");
  const dashboardNodes = qsa("[data-gate-layout-id]");

  const launchMap = new Map();

  function rebuildLaunchMap() {
    launchMap.clear();

    launchNodes.forEach((node) => {
      const command = (node.dataset.gateCommand || "").trim().toLowerCase();
      const label = (node.dataset.gateLabel || "").trim().toLowerCase();

      if (command) launchMap.set(command, node.href);
      if (label) launchMap.set(label, node.href);
    });
  }

  rebuildLaunchMap();

  // ---------------------------------------------------------------------------
  // Gate preferences
  // ---------------------------------------------------------------------------

  const settingsKey = "neutriverse-gate-settings-v2";
  const legacySettingsKey = "neutriverse-gate-settings-v1";
  const defaultLaunchOrder = launchNodes
    .map((node) => node.dataset.gateLaunchId || node.dataset.gateCommand)
    .filter(Boolean);

  const defaultDashboardOrder = dashboardNodes
    .map((node) => node.dataset.gateLayoutId)
    .filter(Boolean);

  const defaultRouteGroupIds = Array.isArray(routeGroupsDefault)
    ? routeGroupsDefault.map((group) => group.id).filter(Boolean)
    : [];

  let routeGroupIds = [...defaultRouteGroupIds];

  const customLaunchLimit = Number(settingsDefault.limits?.custom_launches) || 8;
  const customRouteGroupLimit = Number(settingsDefault.limits?.custom_route_groups) || 4;
  const routesPerGroup = Number(settingsDefault.limits?.routes_per_group) || 4;

  function isSafeRouteUrl(value) {
    if (typeof value !== "string") {
      return false;
    }

    const url = value.trim();

    if (!url) {
      return false;
    }

    if (url.startsWith("/")) {
      return !url.startsWith("//");
    }

    try {
      const parsed = new URL(url);
      return parsed.protocol === "https:" || parsed.protocol === "http:";
    } catch {
      return false;
    }
  }

  function cleanText(value, maxLength) {
    return typeof value === "string" ? value.trim().slice(0, maxLength) : "";
  }

  function normalizeCustomLaunches(value) {
    if (!Array.isArray(value)) {
      return [];
    }

    const result = [];
    const ids = new Set();

    value.slice(0, customLaunchLimit).forEach((item) => {
      const id = cleanText(item?.id, 80);
      const label = cleanText(item?.label, 40);
      const role = cleanText(item?.role, 40) || "CUSTOM";
      const url = cleanText(item?.url, 500);

      if (
        !/^custom-launch-[a-z0-9-]+$/i.test(id) ||
        ids.has(id) ||
        !label ||
        !isSafeRouteUrl(url)
      ) {
        return;
      }

      ids.add(id);
      result.push({ id, label, role, url });
    });

    return result;
  }

  function normalizeCustomRouteGroups(value) {
    if (!Array.isArray(value)) {
      return [];
    }

    const result = [];
    const ids = new Set(defaultRouteGroupIds);

    value.slice(0, customRouteGroupLimit).forEach((item) => {
      const id = cleanText(item?.id, 80);
      const label = cleanText(item?.label, 24);
      const detail = cleanText(item?.detail, 40) || "CUSTOM ROUTES";

      if (
        !/^custom-group-[a-z0-9-]+$/i.test(id) ||
        ids.has(id) ||
        !label
      ) {
        return;
      }

      const rawRoutes = Array.isArray(item?.routes) ? item.routes : [];
      const routes = [];

      for (let index = 0; index < routesPerGroup; index += 1) {
        const route = rawRoutes[index] || {};
        const routeLabel = cleanText(route.label, 60);
        const routeDetail = cleanText(route.detail, 60);
        const routeUrl = cleanText(route.url, 500);

        routes.push({
          label: routeLabel,
          detail: routeDetail,
          url: routeUrl && isSafeRouteUrl(routeUrl) ? routeUrl : "",
        });
      }

      ids.add(id);
      result.push({ id, label, detail, routes });
    });

    return result;
  }

  const preferenceDefaults = {
    defaultSearch: settingsDefault.default_search || "google",
    density: settingsDefault.density === "compact" ? "compact" : "standard",
    ambient: settingsDefault.ambient !== false,
    routeShortcuts: settingsDefault.route_shortcuts !== false,
    presentation: settingsDefault.presentation === "focus" ? "focus" : "dashboard",
    modules: {
      launch_routes: settingsDefault.modules?.launch_routes !== false,
      current_vector: settingsDefault.modules?.current_vector !== false,
      local_conditions: settingsDefault.modules?.local_conditions !== false,
      active_systems: settingsDefault.modules?.active_systems !== false,
      field_record: settingsDefault.modules?.field_record !== false,
      recent_transits: settingsDefault.modules?.recent_transits !== false,
      context_routes: settingsDefault.modules?.context_routes !== false,
    },
    launchOrder: [...defaultLaunchOrder],
    hiddenLaunches: [],
    dashboardOrder: Array.isArray(settingsDefault.dashboard_order)
      ? settingsDefault.dashboard_order
      : [...defaultDashboardOrder],
    activeRouteGroup: routeGroupIds.includes(settingsDefault.active_route_group)
      ? settingsDefault.active_route_group
      : (routeGroupIds[0] || "work"),
    dashboardSpans: {
      current_vector: ["standard", "wide"].includes(settingsDefault.dashboard_spans?.current_vector)
        ? settingsDefault.dashboard_spans.current_vector
        : "standard",
      local_conditions: ["standard", "wide"].includes(settingsDefault.dashboard_spans?.local_conditions)
        ? settingsDefault.dashboard_spans.local_conditions
        : "standard",
      active_systems: ["standard", "wide"].includes(settingsDefault.dashboard_spans?.active_systems)
        ? settingsDefault.dashboard_spans.active_systems
        : "standard",
      field_record: "full",
    },
    routeOverrides: {},
    customLaunches: [],
    customRouteGroups: [],
    queryPresets: {},
    routeGroupOrder: Array.isArray(settingsDefault.route_group_order)
      ? settingsDefault.route_group_order
      : [...defaultRouteGroupIds],
    pinnedRouteGroup: settingsDefault.pinned_route_group || "",
    contextLaunchHidden: {},
  };

  function normalizePreferences(raw = {}) {
    const modules = {
      ...preferenceDefaults.modules,
      ...(raw.modules && typeof raw.modules === "object" ? raw.modules : {}),
    };

    const customLaunches = normalizeCustomLaunches(raw.customLaunches);
    const validLaunchIds = [
      ...defaultLaunchOrder,
      ...customLaunches.map((item) => item.id),
    ];

    const requestedOrder = Array.isArray(raw.launchOrder)
      ? raw.launchOrder.filter((id, index, array) =>
          validLaunchIds.includes(id) && array.indexOf(id) === index
        )
      : [];

    const launchOrder = [
      ...requestedOrder,
      ...validLaunchIds.filter((id) => !requestedOrder.includes(id)),
    ];

    const hiddenLaunches = Array.isArray(raw.hiddenLaunches)
      ? raw.hiddenLaunches.filter((id, index, array) =>
          validLaunchIds.includes(id) && array.indexOf(id) === index
        )
      : [];

    const requestedDashboardOrder = Array.isArray(raw.dashboardOrder)
      ? raw.dashboardOrder.filter((id) => defaultDashboardOrder.includes(id))
      : [];

    const dashboardOrder = [
      ...requestedDashboardOrder,
      ...defaultDashboardOrder.filter((id) => !requestedDashboardOrder.includes(id)),
    ];

    const customRouteGroups = normalizeCustomRouteGroups(raw.customRouteGroups);
    const normalizedRouteGroupIds = [
      ...defaultRouteGroupIds,
      ...customRouteGroups.map((group) => group.id),
    ];

    const requestedRouteGroupOrder = Array.isArray(raw.routeGroupOrder)
      ? raw.routeGroupOrder.filter((id, index, array) =>
          normalizedRouteGroupIds.includes(id) && array.indexOf(id) === index
        )
      : [];

    const routeGroupOrder = [
      ...requestedRouteGroupOrder,
      ...normalizedRouteGroupIds.filter((id) => !requestedRouteGroupOrder.includes(id)),
    ];

    const pinnedRouteGroup = normalizedRouteGroupIds.includes(raw.pinnedRouteGroup)
      ? raw.pinnedRouteGroup
      : "";

    const activeRouteGroup = normalizedRouteGroupIds.includes(raw.activeRouteGroup)
      ? raw.activeRouteGroup
      : preferenceDefaults.activeRouteGroup;

    const rawContextLaunchHidden =
      raw.contextLaunchHidden &&
      typeof raw.contextLaunchHidden === "object" &&
      !Array.isArray(raw.contextLaunchHidden)
        ? raw.contextLaunchHidden
        : {};

    const contextLaunchHidden = {};

    normalizedRouteGroupIds.forEach((groupId) => {
      const hidden = Array.isArray(rawContextLaunchHidden[groupId])
        ? rawContextLaunchHidden[groupId].filter((id, index, array) =>
            validLaunchIds.includes(id) && array.indexOf(id) === index
          )
        : [];

      if (hidden.length) {
        contextLaunchHidden[groupId] = hidden;
      }
    });

    const rawQueryPresets =
      raw.queryPresets && typeof raw.queryPresets === "object" && !Array.isArray(raw.queryPresets)
        ? raw.queryPresets
        : {};

    const queryPresets = {};

    normalizedRouteGroupIds.forEach((groupId) => {
      const preset = rawQueryPresets[groupId];

      if (!preset || typeof preset !== "object") {
        return;
      }

      const engine = engines[preset.engine] ? preset.engine : "";
      const placeholder = cleanText(preset.placeholder, 80);

      if (engine || placeholder) {
        queryPresets[groupId] = {
          engine,
          placeholder,
        };
      }
    });

    const presentation = raw.presentation === "focus" ? "focus" : "dashboard";

    const dashboardSpans = {
      current_vector: ["standard", "wide"].includes(raw.dashboardSpans?.current_vector)
        ? raw.dashboardSpans.current_vector
        : preferenceDefaults.dashboardSpans.current_vector,
      local_conditions: ["standard", "wide"].includes(raw.dashboardSpans?.local_conditions)
        ? raw.dashboardSpans.local_conditions
        : preferenceDefaults.dashboardSpans.local_conditions,
      active_systems: ["standard", "wide"].includes(raw.dashboardSpans?.active_systems)
        ? raw.dashboardSpans.active_systems
        : preferenceDefaults.dashboardSpans.active_systems,
      field_record: "full",
    };

    const routeOverrides = {};
    const rawOverrides = raw.routeOverrides && typeof raw.routeOverrides === "object"
      ? raw.routeOverrides
      : {};

    defaultRouteGroupIds.forEach((groupId) => {
      const slots = Array.isArray(rawOverrides[groupId]) ? rawOverrides[groupId] : [];

      routeOverrides[groupId] = slots.slice(0, 4).map((slot) => ({
        label: typeof slot?.label === "string" ? slot.label.slice(0, 60) : "",
        detail: typeof slot?.detail === "string" ? slot.detail.slice(0, 60) : "",
        url: typeof slot?.url === "string" ? slot.url.slice(0, 500) : "",
      }));
    });

    return {
      defaultSearch: engines[raw.defaultSearch]
        ? raw.defaultSearch
        : (engines[preferenceDefaults.defaultSearch] ? preferenceDefaults.defaultSearch : "google"),
      density: raw.density === "compact" ? "compact" : "standard",
      ambient: raw.ambient !== false,
      routeShortcuts: raw.routeShortcuts !== false,
      presentation,
      modules,
      launchOrder,
      hiddenLaunches,
      dashboardOrder,
      activeRouteGroup,
      dashboardSpans,
      routeOverrides,
      customLaunches,
      customRouteGroups,
      queryPresets,
      routeGroupOrder,
      pinnedRouteGroup,
      contextLaunchHidden,
    };
  }

  const storedPreferences = readJson(
    settingsKey,
    readJson(legacySettingsKey, {})
  );

  let preferences = normalizePreferences(storedPreferences);

  function allRouteGroups() {
    const groups = [
      ...(Array.isArray(routeGroupsDefault) ? routeGroupsDefault : []),
      ...preferences.customRouteGroups,
    ];

    const byId = new Map(groups.map((group) => [group.id, group]));
    const orderedIds = [
      ...preferences.routeGroupOrder.filter((id) => byId.has(id)),
      ...groups.map((group) => group.id).filter((id) => !preferences.routeGroupOrder.includes(id)),
    ];

    const effectiveIds =
      preferences.pinnedRouteGroup && orderedIds.includes(preferences.pinnedRouteGroup)
        ? [
            preferences.pinnedRouteGroup,
            ...orderedIds.filter((id) => id !== preferences.pinnedRouteGroup),
          ]
        : orderedIds;

    return effectiveIds.map((id) => byId.get(id)).filter(Boolean);
  }

  function savePreferences(next) {
    preferences = normalizePreferences(next);
    writeJson(settingsKey, preferences);
    applyPreferences();
    syncSettingsControls();
    syncSettingsHealth();
  }

  function moduleEnabled(name) {
    return preferences.modules?.[name] !== false;
  }

  function applyModulePreferences() {
    qsa("[data-gate-module]").forEach((node) => {
      const name = node.dataset.gateModule;
      node.hidden = !moduleEnabled(name);
    });

    syncDashboardIndices();
  }

  function createCustomLaunchNode(item) {
    const node = document.createElement("a");
    node.className = "gate-launch";
    node.href = item.url;
    node.dataset.gateLaunch = "";
    node.dataset.gateLaunchId = item.id;
    node.dataset.gateCustomLaunch = "true";
    node.dataset.gateCommand = "";
    node.dataset.gateLabel = item.label.toLowerCase();

    const code = document.createElement("span");
    code.className = "gate-launch-code";
    code.textContent = "--";

    const arrow = document.createElement("span");
    arrow.className = "gate-launch-arrow";
    arrow.setAttribute("aria-hidden", "true");
    arrow.textContent = "↗";

    const strong = document.createElement("strong");
    strong.textContent = item.label;

    const small = document.createElement("small");
    small.textContent = item.role;

    node.append(code, arrow, strong, small);

    node.addEventListener("click", () => {
      recordTransit({
        label: item.label.toUpperCase(),
        detail: "CUSTOM LAUNCH",
        action: "url",
        value: node.href,
      });
    });

    return node;
  }

  function applyLaunchPreferences() {
    if (!launchGrid) {
      return;
    }

    launchGrid.querySelectorAll('[data-gate-custom-launch="true"]').forEach((node) => {
      node.remove();
    });

    preferences.customLaunches.forEach((item) => {
      launchGrid.appendChild(createCustomLaunchNode(item));
    });

    const currentNodes = qsa("[data-gate-launch]");
    const byId = new Map(
      currentNodes.map((node) => [
        node.dataset.gateLaunchId || node.dataset.gateCommand,
        node,
      ])
    );

    preferences.launchOrder.forEach((id) => {
      const node = byId.get(id);
      if (node) launchGrid.appendChild(node);
    });

    const hidden = new Set([
      ...preferences.hiddenLaunches,
      ...(preferences.contextLaunchHidden?.[preferences.activeRouteGroup] || []),
    ]);

    launchNodes = qsa("[data-gate-launch]");
    let visibleIndex = 1;

    launchNodes.forEach((node) => {
      const id = node.dataset.gateLaunchId || node.dataset.gateCommand;
      const isHidden = hidden.has(id);
      node.hidden = isHidden;

      const code = node.querySelector(".gate-launch-code");
      if (code && !isHidden) {
        code.textContent = String(visibleIndex).padStart(2, "0");
        visibleIndex += 1;
      }
    });

    rebuildLaunchMap();
  }

  function syncDashboardIndices() {
    let nextIndex = 3;

    preferences.dashboardOrder.forEach((id) => {
      const node = dashboardNodes.find((item) => item.dataset.gateLayoutId === id);

      if (!node || node.hidden) {
        return;
      }

      const indexNode = node.querySelector(`[data-gate-layout-index="${id}"]`);

      if (indexNode) {
        indexNode.textContent = String(nextIndex).padStart(2, "0");
      }

      nextIndex += 1;
    });
  }

  function applyDashboardOrder() {
    if (!dashboardGrid) {
      return;
    }

    const byId = new Map(
      dashboardNodes.map((node) => [node.dataset.gateLayoutId, node])
    );

    preferences.dashboardOrder.forEach((id) => {
      const node = byId.get(id);
      if (node) dashboardGrid.appendChild(node);
    });

    syncDashboardIndices();
  }

  function routeGroupDefinition(groupId) {
    return allRouteGroups().find((item) => item.id === groupId) || null;
  }

  function routeGroupDefaults(groupId) {
    const group = routeGroupDefinition(groupId);
    return Array.isArray(group?.routes) ? group.routes : [];
  }

  function isCustomRouteGroup(groupId) {
    return preferences.customRouteGroups.some((group) => group.id === groupId);
  }

  function resolvedRouteSlot(groupId, slotIndex) {
    const defaults = routeGroupDefaults(groupId)[slotIndex] || {};

    if (isCustomRouteGroup(groupId)) {
      return {
        label: defaults.label?.trim() || "UNASSIGNED",
        detail: defaults.detail?.trim() || "CUSTOM ROUTE",
        url: isSafeRouteUrl(defaults.url) ? defaults.url.trim() : "",
      };
    }

    const override = preferences.routeOverrides?.[groupId]?.[slotIndex] || {};

    return {
      label: override.label?.trim() || defaults.label || `Route ${slotIndex + 1}`,
      detail: override.detail?.trim() || defaults.detail || "ROUTE",
      url: isSafeRouteUrl(override.url) ? override.url.trim() : (defaults.url || "/"),
    };
  }

  function bindCustomRouteGroupTab(tab) {
    tab.addEventListener("click", () => {
      const groupId = tab.dataset.gateRouteGroupTab;

      if (!routeGroupIds.includes(groupId)) {
        return;
      }

      savePreferences({
        ...preferences,
        activeRouteGroup: groupId,
      });
    });

    tab.addEventListener("keydown", (event) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) {
        return;
      }

      event.preventDefault();

      const currentIndex = routeGroupTabs.indexOf(tab);
      let nextIndex = currentIndex;

      if (event.key === "ArrowRight") {
        nextIndex = (currentIndex + 1) % routeGroupTabs.length;
      } else if (event.key === "ArrowLeft") {
        nextIndex = (currentIndex - 1 + routeGroupTabs.length) % routeGroupTabs.length;
      } else if (event.key === "Home") {
        nextIndex = 0;
      } else if (event.key === "End") {
        nextIndex = routeGroupTabs.length - 1;
      }

      const nextTab = routeGroupTabs[nextIndex];
      const groupId = nextTab?.dataset.gateRouteGroupTab;

      if (groupId) {
        savePreferences({
          ...preferences,
          activeRouteGroup: groupId,
        });

        qsa("[data-gate-route-group-tab]")
          .find((item) => item.dataset.gateRouteGroupTab === groupId)
          ?.focus();
      }
    });
  }

  function syncCustomRouteMatrix() {
    if (!contextTabsNode || !contextPanelsNode) {
      return;
    }

    contextTabsNode
      .querySelectorAll('[data-gate-custom-route-group="true"]')
      .forEach((node) => node.remove());

    contextPanelsNode
      .querySelectorAll('[data-gate-custom-route-group="true"]')
      .forEach((node) => node.remove());

    preferences.customRouteGroups.forEach((group) => {
      const tab = document.createElement("button");
      tab.type = "button";
      tab.setAttribute("role", "tab");
      tab.dataset.gateRouteGroupTab = group.id;
      tab.dataset.gateCustomRouteGroup = "true";
      tab.setAttribute("aria-controls", `gate-route-group-${group.id}`);
      tab.setAttribute("aria-selected", "false");

      const tabStrong = document.createElement("strong");
      tabStrong.textContent = group.label;
      const tabSmall = document.createElement("small");
      tabSmall.textContent = group.detail;
      tab.append(tabStrong, tabSmall);

      const panel = document.createElement("div");
      panel.id = `gate-route-group-${group.id}`;
      panel.className = "gate-context-panel";
      panel.setAttribute("role", "tabpanel");
      panel.dataset.gateRouteGroupPanel = group.id;
      panel.dataset.gateCustomRouteGroup = "true";
      panel.hidden = true;

      for (let slotIndex = 0; slotIndex < routesPerGroup; slotIndex += 1) {
        const route = resolvedRouteSlot(group.id, slotIndex);
        const anchor = document.createElement("a");
        anchor.dataset.gateContextRoute = "";
        anchor.dataset.gateRouteGroupId = group.id;
        anchor.dataset.gateRouteSlot = String(slotIndex);
        anchor.dataset.gateTransitLabel = route.label;
        anchor.dataset.gateTransitDetail = `${group.label} · ${route.detail}`;

        if (isSafeRouteUrl(route.url)) {
          anchor.href = route.url;
        } else {
          anchor.href = "#";
          anchor.classList.add("gate-context-route-empty");
          anchor.setAttribute("aria-disabled", "true");
        }

        const text = document.createElement("span");
        const strong = document.createElement("strong");
        strong.textContent = route.label;
        const small = document.createElement("small");
        small.textContent = route.detail;
        text.append(strong, small);

        const arrow = document.createElement("span");
        arrow.setAttribute("aria-hidden", "true");
        arrow.textContent = isSafeRouteUrl(route.url) ? "↗" : "—";

        anchor.append(text, arrow);

        anchor.addEventListener("click", (event) => {
          if (anchor.getAttribute("aria-disabled") === "true") {
            event.preventDefault();
            return;
          }

          recordTransit({
            label: anchor.dataset.gateTransitLabel || "CONTEXT ROUTE",
            detail: anchor.dataset.gateTransitDetail || "ROUTE MATRIX",
            action: "url",
            value: anchor.href,
          });
        });

        panel.appendChild(anchor);
      }

      contextTabsNode.appendChild(tab);
      contextPanelsNode.appendChild(panel);
      bindCustomRouteGroupTab(tab);
    });

    const effectiveGroups = allRouteGroups();
    routeGroupIds = effectiveGroups.map((group) => group.id);

    const tabMap = new Map(
      qsa("[data-gate-route-group-tab]").map((tab) => [
        tab.dataset.gateRouteGroupTab,
        tab,
      ])
    );

    const panelMap = new Map(
      qsa("[data-gate-route-group-panel]").map((panel) => [
        panel.dataset.gateRouteGroupPanel,
        panel,
      ])
    );

    routeGroupIds.forEach((groupId) => {
      const tab = tabMap.get(groupId);
      const panel = panelMap.get(groupId);

      if (tab) contextTabsNode.appendChild(tab);
      if (panel) contextPanelsNode.appendChild(panel);
    });

    routeGroupTabs = qsa("[data-gate-route-group-tab]");
    routeGroupPanels = qsa("[data-gate-route-group-panel]");
    contextRouteNodes = qsa("[data-gate-context-route]");

    routeGroupTabs.forEach((tab, index) => {
      const groupId = tab.dataset.gateRouteGroupTab;
      const shortcut = index < 9 ? String(index + 1) : "";

      tab.classList.toggle(
        "gate-route-group-pinned",
        groupId === preferences.pinnedRouteGroup
      );

      if (preferences.routeShortcuts && shortcut) {
        tab.dataset.gateShortcut = `⌘/Ctrl+Alt+${shortcut}`;
        tab.title = `${routeGroupDefinition(groupId)?.label || groupId} · Ctrl/Cmd + Alt + ${shortcut}`;
      } else {
        delete tab.dataset.gateShortcut;
        tab.removeAttribute("title");
      }
    });

    app.style.setProperty("--gate-route-group-count", String(Math.max(1, routeGroupIds.length)));
  }

  function applyRouteOverrides() {
    const defaultNodes = qsa("[data-gate-context-route]")
      .filter((node) => node.dataset.gateCustomRouteGroup !== "true");

    defaultNodes.forEach((node) => {
      const groupId = node.dataset.gateRouteGroupId;
      const slotIndex = Number(node.dataset.gateRouteSlot);

      if (!groupId || !Number.isInteger(slotIndex)) {
        return;
      }

      const route = resolvedRouteSlot(groupId, slotIndex);
      const group = routeGroupDefinition(groupId);

      node.href = route.url;
      node.dataset.gateTransitLabel = route.label;
      node.dataset.gateTransitDetail = `${group?.label || groupId.toUpperCase()} · ${route.detail}`;

      const strong = node.querySelector("strong");
      const small = node.querySelector("small");

      if (strong) strong.textContent = route.label;
      if (small) small.textContent = route.detail;
    });

    syncCustomRouteMatrix();
  }

  function applyDashboardSpans() {
    dashboardNodes.forEach((node) => {
      const id = node.dataset.gateLayoutId;
      const span = id === "field_record"
        ? "full"
        : (preferences.dashboardSpans?.[id] === "wide" ? "wide" : "standard");

      node.dataset.gateSpan = span;
    });
  }

  function applyPresentation() {
    app.dataset.gatePresentation = preferences.presentation;

    if (modeLabelNode) {
      modeLabelNode.textContent = preferences.presentation.toUpperCase();
    }

    if (modeToggleButton) {
      const target = preferences.presentation === "focus" ? "Dashboard" : "Focus";
      modeToggleButton.setAttribute("aria-label", `切换到 ${target} 模式`);
      modeToggleButton.setAttribute("title", `Switch to ${target}`);
    }
  }

  function effectiveLaunchVisibility(groupId = preferences.activeRouteGroup) {
    const globalHidden = new Set(preferences.hiddenLaunches);
    const contextHidden = new Set(preferences.contextLaunchHidden?.[groupId] || []);

    return preferences.launchOrder.filter(
      (id) => !globalHidden.has(id) && !contextHidden.has(id)
    );
  }

  function validRoutesForGroup(groupId) {
    const routes = [];

    for (let index = 0; index < routesPerGroup; index += 1) {
      const route = resolvedRouteSlot(groupId, index);

      if (isSafeRouteUrl(route.url)) {
        routes.push(route);
      }
    }

    return routes;
  }

  function contextProfilePayload(groupId = preferences.activeRouteGroup) {
    const group = routeGroupDefinition(groupId);
    const preset = preferences.queryPresets?.[groupId] || {};
    const engineKey =
      preset.engine && engines[preset.engine]
        ? preset.engine
        : preferences.defaultSearch;
    const engine = engines[engineKey] || defaultEngine();

    const visibleIds = effectiveLaunchVisibility(groupId);
    const launchNodesById = new Map(
      qsa("[data-gate-launch]").map((node) => [
        node.dataset.gateLaunchId || node.dataset.gateCommand,
        node,
      ])
    );

    const launches = visibleIds.map((id) => {
      const node = launchNodesById.get(id);

      return {
        id,
        label: node?.dataset.gateLabel || id,
        detail: node?.querySelector("small")?.textContent || "LAUNCH ROUTE",
        url: node?.href || "",
      };
    });

    const routes = validRoutesForGroup(groupId).map((route) => ({
      label: route.label,
      detail: route.detail,
      url: route.url,
    }));

    const shortcutIndex = routeGroupIds.indexOf(groupId);

    return {
      format: "neutriverse-gate-context-profile",
      version: "1",
      exportedAt: new Date().toISOString(),
      group: {
        id: groupId,
        label: group?.label || groupId,
        detail: group?.detail || "",
        pinned: groupId === preferences.pinnedRouteGroup,
        effectiveOrder: routeGroupIds.indexOf(groupId) + 1,
      },
      search: {
        engine: engineKey,
        label: engine?.label || engineKey,
        inherited: !preset.engine,
        placeholder: preset.placeholder || "",
      },
      launches,
      routes,
      shortcut:
        preferences.routeShortcuts && shortcutIndex >= 0 && shortcutIndex < 9
          ? `Ctrl/Cmd + Alt + ${shortcutIndex + 1}`
          : null,
    };
  }

  function contextProfileText(groupId = preferences.activeRouteGroup) {
    const profile = contextProfilePayload(groupId);

    return [
      `NEUTRIVERSE // CONTEXT PROFILE`,
      `${profile.group.label.toUpperCase()} · ${profile.group.detail || "ROUTES"}`,
      `Search: ${profile.search.label}${profile.search.inherited ? " (global)" : " (context)"}`,
      `Launches: ${profile.launches.length}`,
      `Routes: ${profile.routes.length}`,
      `Pinned: ${profile.group.pinned ? "yes" : "no"}`,
      `Shortcut: ${profile.shortcut || "off"}`,
      "",
      "Launch Routes:",
      ...profile.launches.map((item) => `- ${item.label} · ${item.detail}`),
      "",
      "Transit Routes:",
      ...profile.routes.map((item) => `- ${item.label} · ${item.detail} · ${item.url}`),
    ].join("\n");
  }

  async function copyTextToClipboard(value) {
    try {
      await navigator.clipboard.writeText(value);
      return true;
    } catch {
      const textarea = document.createElement("textarea");
      textarea.value = value;
      textarea.setAttribute("readonly", "");
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.select();

      let copied = false;

      try {
        copied = document.execCommand("copy");
      } catch {
        copied = false;
      }

      textarea.remove();
      return copied;
    }
  }

  async function copyContextProfile() {
    const copied = await copyTextToClipboard(
      contextProfileText(preferences.activeRouteGroup)
    );

    setSettingsStatus(
      copied ? "CONTEXT PROFILE COPIED" : "COPY UNAVAILABLE"
    );
  }

  function exportContextProfile() {
    const profile = contextProfilePayload(preferences.activeRouteGroup);
    const blob = new Blob(
      [JSON.stringify(profile, null, 2)],
      { type: "application/json" }
    );
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    const groupSlug = cleanText(profile.group.label, 24)
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "") || "context";

    anchor.href = url;
    anchor.download = `neutriverse-gate-context-${groupSlug}.json`;
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();

    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
    setSettingsStatus("CONTEXT PROFILE EXPORTED");
  }

  function syncContextProfile(groupId = preferences.activeRouteGroup) {
    if (!routeGroupIds.includes(groupId)) {
      return;
    }

    const group = routeGroupDefinition(groupId);
    const preset = preferences.queryPresets?.[groupId] || {};
    const engineKey =
      preset.engine && engines[preset.engine]
        ? preset.engine
        : preferences.defaultSearch;
    const engine = engines[engineKey] || defaultEngine();

    const visibleLaunches = effectiveLaunchVisibility(groupId);
    const routes = validRoutesForGroup(groupId);
    const shortcutIndex = routeGroupIds.indexOf(groupId);
    const shortcut =
      preferences.routeShortcuts && shortcutIndex >= 0 && shortcutIndex < 9
        ? `CTRL/CMD + ALT + ${shortcutIndex + 1}`
        : "SHORTCUT OFF";

    if (contextProfileGroup) {
      contextProfileGroup.textContent = group?.label || groupId.toUpperCase();
    }

    if (contextProfileSearch) {
      contextProfileSearch.textContent = engine?.label?.toUpperCase() || "GLOBAL";
    }

    if (contextProfileLaunches) {
      contextProfileLaunches.textContent =
        `${visibleLaunches.length} / ${preferences.launchOrder.length}`;
    }

    if (contextProfileRoutes) {
      contextProfileRoutes.textContent = `${routes.length} / ${routesPerGroup}`;
    }

    if (contextProfileShortcut) {
      contextProfileShortcut.textContent = shortcut;
    }

    if (contextProfileNote) {
      const pinNote =
        groupId === preferences.pinnedRouteGroup ? "Pinned first. " : "";

      const searchNote = preset.engine
        ? `${engine?.label || "Context"} overrides global search. `
        : "Global search inherited. ";

      contextProfileNote.textContent =
        `${pinNote}${searchNote}${visibleLaunches.length} Launch routes visible; ${routes.length} transit routes assigned.`;
    }
  }

  function applyRouteGroup(groupId = preferences.activeRouteGroup) {
    const validId = routeGroupIds.includes(groupId)
      ? groupId
      : (routeGroupIds.includes(preferenceDefaults.activeRouteGroup)
          ? preferenceDefaults.activeRouteGroup
          : routeGroupIds[0]);

    routeGroupTabs.forEach((tab) => {
      const selected = tab.dataset.gateRouteGroupTab === validId;
      tab.setAttribute("aria-selected", selected ? "true" : "false");
      tab.tabIndex = selected ? 0 : -1;
    });

    routeGroupPanels.forEach((panel) => {
      panel.hidden = panel.dataset.gateRouteGroupPanel !== validId;
    });

    syncContextProfile(validId);
  }

  function applyPreferences() {
    app.dataset.gateDensity = preferences.density;
    app.dataset.gateAmbient = preferences.ambient ? "on" : "off";
    applyModulePreferences();
    applyLaunchPreferences();
    applyDashboardOrder();
    applyDashboardSpans();
    applyRouteOverrides();
    applyRouteGroup();
    applyPresentation();
    syncQueryContext();
  }

  applyPreferences();

  // ---------------------------------------------------------------------------
  // Theme
  // ---------------------------------------------------------------------------

  const themeKey = "neutriverse-theme-preference";
  const sessionThemeKey = "mode";
  const themeButton = qs("[data-gate-theme]");

  function getTheme() {
    const explicit = root.getAttribute("data-mode");

    if (explicit === "light" || explicit === "dark") {
      return explicit;
    }

    const saved = storage.get(themeKey);

    if (saved === "light" || saved === "dark") {
      return saved;
    }

    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme(mode) {
    const normalized = mode === "light" ? "light" : "dark";

    root.setAttribute("data-mode", normalized);
    root.setAttribute("data-bs-theme", normalized);
    root.style.colorScheme = normalized;
    storage.set(themeKey, normalized);

    try {
      sessionStorage.setItem(sessionThemeKey, normalized);
    } catch {
      /* Ignore restricted storage. */
    }

    document.querySelectorAll('meta[name="theme-color"]').forEach((meta) => {
      meta.setAttribute("content", normalized === "light" ? "#EEE5CE" : "#080B12");
    });

    if (themeButton) {
      const target = normalized === "dark" ? "Prospero Light" : "Night Observatory";
      themeButton.setAttribute("aria-label", `切换到 ${target}`);
      themeButton.setAttribute("title", `切换到 ${target}`);
    }

    window.postMessage({ id: "theme-mode" }, "*");
  }

  applyTheme(getTheme());

  themeButton?.addEventListener("click", () => {
    applyTheme(getTheme() === "dark" ? "light" : "dark");
  });

  modeToggleButton?.addEventListener("click", () => {
    savePreferences({
      ...preferences,
      presentation: preferences.presentation === "focus" ? "dashboard" : "focus",
    });
  });

  // ---------------------------------------------------------------------------
  // Clock / local node
  // ---------------------------------------------------------------------------

  const timeNode = qs("[data-gate-time]");
  const dateNode = qs("[data-gate-date]");
  const timezoneNode = qs("[data-gate-timezone]");
  const zoneNode = qs("[data-gate-zone]");

  const resolvedZone = Intl.DateTimeFormat().resolvedOptions().timeZone || "LOCAL";
  const shortZone = (() => {
    try {
      const parts = new Intl.DateTimeFormat("en-GB", {
        timeZoneName: "short",
      }).formatToParts(new Date());

      return parts.find((part) => part.type === "timeZoneName")?.value || resolvedZone;
    } catch {
      return resolvedZone;
    }
  })();

  function updateClock() {
    const now = new Date();

    if (timeNode) {
      timeNode.textContent = new Intl.DateTimeFormat("en-GB", {
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
      }).format(now);
    }

    if (dateNode) {
      dateNode.textContent = new Intl.DateTimeFormat("en-GB", {
        weekday: "short",
        day: "2-digit",
        month: "short",
        year: "numeric",
      }).format(now).toUpperCase();
    }

    if (timezoneNode) {
      timezoneNode.textContent = `${resolvedZone.toUpperCase()} · ${shortZone.toUpperCase()}`;
    }

    if (zoneNode) {
      zoneNode.textContent = shortZone.toUpperCase();
    }
  }

  updateClock();
  window.setInterval(updateClock, 1000);

  // ---------------------------------------------------------------------------
  // Network indicator
  // ---------------------------------------------------------------------------

  const networkNode = qs("[data-gate-network]");
  const networkDot = qs("[data-gate-network-dot]");

  function syncNetworkState() {
    const online = navigator.onLine;

    if (networkNode) {
      networkNode.textContent = online ? "ONLINE" : "OFFLINE";
    }

    networkDot?.classList.toggle("is-offline", !online);
  }

  syncNetworkState();
  window.addEventListener("online", syncNetworkState);
  window.addEventListener("offline", syncNetworkState);

  // ---------------------------------------------------------------------------
  // Field Record
  // ---------------------------------------------------------------------------

  const noteKey = "neutriverse-gate-field-record";
  const noteTimeKey = "neutriverse-gate-field-record-time";
  const note = qs("[data-gate-note]");
  const noteStatus = qs("[data-gate-note-status]");
  let noteTimer;

  function formatSavedTime(value) {
    if (!value) return "EMPTY";

    const date = new Date(value);

    if (Number.isNaN(date.getTime())) return "SAVED";

    return `SAVED ${new Intl.DateTimeFormat("en-GB", {
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    }).format(date)}`;
  }

  function refreshNoteStatus() {
    if (!noteStatus) return;

    const value = note?.value.trim() || "";
    noteStatus.textContent = value ? formatSavedTime(storage.get(noteTimeKey)) : "EMPTY";
  }

  function clearNote() {
    if (note) note.value = "";
    storage.remove(noteKey);
    storage.remove(noteTimeKey);
    refreshNoteStatus();
  }

  if (note) {
    note.value = storage.get(noteKey) || "";
    refreshNoteStatus();

    note.addEventListener("input", () => {
      window.clearTimeout(noteTimer);

      if (noteStatus) noteStatus.textContent = "WRITING";

      noteTimer = window.setTimeout(() => {
        storage.set(noteKey, note.value);
        storage.set(noteTimeKey, new Date().toISOString());
        refreshNoteStatus();
      }, 280);
    });
  }

  // ---------------------------------------------------------------------------
  // Current Vector
  // ---------------------------------------------------------------------------

  const vectorKey = "neutriverse-gate-current-vector";
  const vectorPanel = qs("[data-gate-vector-panel]");
  const vectorDisplay = qs("[data-gate-vector-display]");
  const vectorEditor = qs("[data-gate-vector-editor]");
  const vectorEditButton = qs("[data-gate-vector-edit]");
  const vectorResetButton = qs("[data-gate-vector-reset]");
  const vectorCancelButton = qs("[data-gate-vector-cancel]");
  const vectorTitleNode = qs("[data-gate-vector-title]");
  const vectorStatusNode = qs("[data-gate-vector-status]");
  const vectorDescriptionNode = qs("[data-gate-vector-description]");
  const vectorUpdatedNode = qs("[data-gate-vector-updated]");
  const vectorTitleInput = qs("[data-gate-vector-title-input]");
  const vectorStatusInput = qs("[data-gate-vector-status-input]");
  const vectorDescriptionInput = qs("[data-gate-vector-description-input]");

  function readVectorOverride() {
    return readJson(vectorKey, null);
  }

  function currentVector() {
    const override = readVectorOverride();

    return {
      title: override?.title || vectorDefault.title || "Current Vector",
      status: override?.status || vectorDefault.status || "ACTIVE",
      description: override?.description || vectorDefault.description || "",
      updatedAt: override?.updatedAt || null,
    };
  }

  function renderVector() {
    if (!vectorPanel) return;

    const vector = currentVector();

    if (vectorTitleNode) vectorTitleNode.textContent = vector.title;
    if (vectorStatusNode) vectorStatusNode.textContent = vector.status;
    if (vectorDescriptionNode) vectorDescriptionNode.textContent = vector.description;

    if (vectorUpdatedNode) {
      if (!vector.updatedAt) {
        vectorUpdatedNode.textContent = "CONFIG DEFAULT";
      } else {
        vectorUpdatedNode.textContent = `UPDATED ${new Intl.DateTimeFormat("en-GB", {
          hour: "2-digit",
          minute: "2-digit",
          hour12: false,
        }).format(new Date(vector.updatedAt))}`;
      }
    }
  }

  function openVectorEditor() {
    if (!vectorEditor || !vectorDisplay) return;

    const vector = currentVector();

    if (vectorTitleInput) vectorTitleInput.value = vector.title;
    if (vectorStatusInput) vectorStatusInput.value = vector.status;
    if (vectorDescriptionInput) vectorDescriptionInput.value = vector.description;

    vectorDisplay.hidden = true;
    vectorEditor.hidden = false;
    vectorEditButton?.setAttribute("aria-expanded", "true");
    vectorTitleInput?.focus();
  }

  function closeVectorEditor() {
    if (!vectorEditor || !vectorDisplay) return;

    vectorEditor.hidden = true;
    vectorDisplay.hidden = false;
    vectorEditButton?.setAttribute("aria-expanded", "false");
  }

  function resetVector() {
    storage.remove(vectorKey);
    renderVector();
    closeVectorEditor();
  }

  vectorEditButton?.setAttribute("aria-expanded", "false");
  vectorEditButton?.addEventListener("click", openVectorEditor);
  vectorCancelButton?.addEventListener("click", closeVectorEditor);
  vectorResetButton?.addEventListener("click", resetVector);

  vectorEditor?.addEventListener("submit", (event) => {
    event.preventDefault();

    const status = ["ACTIVE", "STANDBY", "PAUSED"].includes(vectorStatusInput?.value)
      ? vectorStatusInput.value
      : "ACTIVE";

    writeJson(vectorKey, {
      title: vectorTitleInput?.value.trim() || vectorDefault.title || "Current Vector",
      status,
      description: vectorDescriptionInput?.value.trim() || "",
      updatedAt: new Date().toISOString(),
    });

    renderVector();
    closeVectorEditor();
  });

  renderVector();

  // ---------------------------------------------------------------------------
  // Recent Transits
  // ---------------------------------------------------------------------------

  const recentTransitKey = "neutriverse-gate-recent-transits";
  const recentTransitLimit = 8;

  function readRecentTransits() {
    const value = readJson(recentTransitKey, []);
    return Array.isArray(value) ? value : [];
  }

  function writeRecentTransits(items) {
    writeJson(recentTransitKey, items.slice(0, recentTransitLimit));
  }

  function clearRecentTransits() {
    storage.remove(recentTransitKey);
  }

  function recordTransit(entry) {
    if (!moduleEnabled("recent_transits") || !entry?.label || !entry?.action) {
      return;
    }

    const normalized = {
      label: String(entry.label).slice(0, 80),
      detail: String(entry.detail || "").slice(0, 80),
      action: entry.action,
      value: String(entry.value || "").slice(0, 300),
      timestamp: Date.now(),
    };

    const remaining = readRecentTransits().filter((item) => {
      return !(item.action === normalized.action && item.value === normalized.value);
    });

    writeRecentTransits([normalized, ...remaining]);
  }

  launchNodes.filter((node) => node.dataset.gateCustomLaunch !== "true").forEach((node) => {
    node.addEventListener("click", () => {
      recordTransit({
        label: (node.dataset.gateCommand || node.dataset.gateLabel || "LAUNCH").toUpperCase(),
        detail: "LAUNCH ROUTE",
        action: "url",
        value: node.href,
      });
    });
  });

  routeNodes.forEach((node) => {
    node.addEventListener("click", () => {
      recordTransit({
        label: node.dataset.gateTransitLabel || "INTERNAL ROUTE",
        detail: node.dataset.gateTransitDetail || "NEUTRIVERSE",
        action: "url",
        value: node.href,
      });
    });
  });

  vectorLinkNodes.forEach((node) => {
    node.addEventListener("click", () => {
      recordTransit({
        label: node.dataset.gateTransitLabel || "VECTOR",
        detail: node.dataset.gateTransitDetail || "CURRENT VECTOR",
        action: "url",
        value: node.href,
      });
    });
  });

  contextRouteNodes.filter((node) => node.dataset.gateCustomRouteGroup !== "true").forEach((node) => {
    node.addEventListener("click", () => {
      recordTransit({
        label: node.dataset.gateTransitLabel || "CONTEXT ROUTE",
        detail: node.dataset.gateTransitDetail || "ROUTE MATRIX",
        action: "url",
        value: node.href,
      });
    });
  });

  routeGroupTabs.filter((tab) => tab.dataset.gateCustomRouteGroup !== "true").forEach((tab) => {
    tab.addEventListener("click", () => {
      const groupId = tab.dataset.gateRouteGroupTab;

      if (!routeGroupIds.includes(groupId)) {
        return;
      }

      savePreferences({
        ...preferences,
        activeRouteGroup: groupId,
      });
    });

    tab.addEventListener("keydown", (event) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) {
        return;
      }

      event.preventDefault();

      const currentIndex = routeGroupTabs.indexOf(tab);
      let nextIndex = currentIndex;

      if (event.key === "ArrowRight") {
        nextIndex = (currentIndex + 1) % routeGroupTabs.length;
      } else if (event.key === "ArrowLeft") {
        nextIndex = (currentIndex - 1 + routeGroupTabs.length) % routeGroupTabs.length;
      } else if (event.key === "Home") {
        nextIndex = 0;
      } else if (event.key === "End") {
        nextIndex = routeGroupTabs.length - 1;
      }

      const nextTab = routeGroupTabs[nextIndex];
      const groupId = nextTab?.dataset.gateRouteGroupTab;

      if (groupId) {
        savePreferences({
          ...preferences,
          activeRouteGroup: groupId,
        });
        nextTab.focus();
      }
    });
  });

  // ---------------------------------------------------------------------------
  // Query Array helpers
  // ---------------------------------------------------------------------------

  function engineByPrefix(prefix) {
    return Object.values(engines).find((engine) => {
      return String(engine.prefix || "").toLowerCase() === prefix.toLowerCase();
    });
  }

  function activeQueryPreset() {
    return preferences.queryPresets?.[preferences.activeRouteGroup] || null;
  }

  function defaultEngine() {
    const preset = activeQueryPreset();
    const presetKey = preset?.engine;

    if (presetKey && engines[presetKey]) {
      return engines[presetKey];
    }

    const key = engines[preferences.defaultSearch]
      ? preferences.defaultSearch
      : preferenceDefaults.defaultSearch;

    return engines[key] || Object.values(engines)[0];
  }

  function syncQueryContext() {
    if (!searchInput) {
      return;
    }

    const group = routeGroupDefinition(preferences.activeRouteGroup);
    const preset = activeQueryPreset();
    const engine = defaultEngine();

    searchInput.placeholder =
      preset?.placeholder ||
      `Search ${group?.label || "the web"} via ${engine?.label || "Web"}…`;

    if (queryState && !searchInput.value.trim()) {
      queryState.textContent =
        `${(group?.label || "GLOBAL").toUpperCase()} · ${(engine?.label || "WEB").toUpperCase()} SEARCH`;
    }
  }

  function buildEngineUrl(engine, query) {
    if (!engine?.url) return null;
    return engine.url.replace("{query}", encodeURIComponent(query));
  }

  function looksLikeUrl(value) {
    if (/^[a-z][a-z0-9+.-]*:\/\//i.test(value)) return true;
    return /^[^\s/]+\.[a-z]{2,}(?:[/?#][^\s]*)?$/i.test(value);
  }

  function normalizeUrl(value) {
    if (/^[a-z][a-z0-9+.-]*:\/\//i.test(value)) return value;
    return `https://${value}`;
  }

  function safeOrigin(value) {
    try {
      return new URL(value).origin;
    } catch {
      return value;
    }
  }

  // Settings functions are declarations so Command Mode can call them before
  // their event bindings appear later in this file.
  function openSettings() {
    const drawer = qs("[data-gate-settings-drawer]");
    const backdrop = qs("[data-gate-settings-backdrop]");
    const close = qs("[data-gate-settings-close]");

    if (!drawer || !backdrop) return;

    syncSettingsControls();
    drawer.hidden = false;
    backdrop.hidden = false;
    document.body.classList.add("gate-settings-open");

    window.requestAnimationFrame(() => {
      drawer.classList.add("is-open");
      backdrop.classList.add("is-open");
      close?.focus();
    });
  }

  function runCommand(rawCommand) {
    const command = rawCommand.trim();
    const [verbRaw, ...rest] = command.split(/\s+/);
    const verb = (verbRaw || "").toLowerCase();
    const argument = rest.join(" ").trim();

    if (verb === "theme") {
      if (argument === "light" || argument === "dark") {
        applyTheme(argument);
        return true;
      }

      if (argument === "toggle") {
        applyTheme(getTheme() === "dark" ? "light" : "dark");
        return true;
      }
    }

    if (verb === "note" && note && argument) {
      note.value = note.value.trim()
        ? `${note.value.trimEnd()}\n> ${argument}`
        : `> ${argument}`;
      note.dispatchEvent(new Event("input", { bubbles: true }));
      note.focus();
      return true;
    }

    if (verb === "clear" && argument === "note") {
      clearNote();
      return true;
    }

    if (verb === "clear" && argument === "recent") {
      clearRecentTransits();
      renderSuggestions();
      return true;
    }

    if (verb === "open" && argument) {
      const destination = launchMap.get(argument.toLowerCase());

      if (destination) {
        window.location.assign(destination);
        return true;
      }
    }

    if (verb === "vector" && argument === "edit") {
      openVectorEditor();
      return true;
    }

    if (verb === "settings") {
      openSettings();
      return true;
    }

    if (verb === "focus") {
      savePreferences({
        ...preferences,
        presentation: "focus",
      });
      return true;
    }

    if (verb === "dashboard") {
      savePreferences({
        ...preferences,
        presentation: "dashboard",
      });
      return true;
    }

    if (verb === "export" && argument === "config") {
      exportGateConfig();
      return true;
    }

    if (verb === "snapshot") {
      createConfigSnapshot(argument);
      return true;
    }

    if (verb === "diagnostics") {
      openSettings();

      if (settingsFilterInput) {
        settingsFilterInput.value = "";
        filterSettingsSections("");
      }

      window.setTimeout(() => {
        renderDiagnostics();
        document.querySelector("#gate-settings-diagnostics")?.scrollIntoView({ block: "start" });
      }, 230);
      return true;
    }

    if (verb === "repair" && argument === "config") {
      repairCurrentConfig();
      return true;
    }

    if (verb === "home") {
      recordTransit({
        label: "NEUTRIVERSE",
        detail: "HOME",
        action: "url",
        value: "/",
      });
      window.location.assign("/");
      return true;
    }

    return false;
  }

  function executeQuery(value) {
    const input = value.trim();

    if (!input) return;

    if (input.startsWith(">")) {
      const handled = runCommand(input.slice(1));

      if (!handled && queryState) queryState.textContent = "UNKNOWN COMMAND";
      return;
    }

    if (input.startsWith("/")) {
      recordTransit({
        label: input.toUpperCase(),
        detail: "INTERNAL ROUTE",
        action: "url",
        value: input,
      });
      window.location.assign(input);
      return;
    }

    if (looksLikeUrl(input)) {
      const destination = normalizeUrl(input);
      const origin = safeOrigin(destination);

      recordTransit({
        label: String(origin).replace(/^https?:\/\//, "").toUpperCase(),
        detail: "DIRECT TRANSIT",
        action: "url",
        value: origin,
      });

      window.location.assign(destination);
      return;
    }

    const match = input.match(/^(\S+)\s+(.+)$/);

    if (match) {
      const engine = engineByPrefix(match[1]);

      if (engine) {
        const destination = buildEngineUrl(engine, match[2]);

        if (destination) {
          recordTransit({
            label: `${engine.label} Search`,
            detail: "SEARCH PREFIX",
            action: "fill",
            value: `${engine.prefix} `,
          });
          window.location.assign(destination);
          return;
        }
      }
    }

    const engine = defaultEngine();
    const destination = buildEngineUrl(engine, input);

    if (destination) {
      recordTransit({
        label: `${engine?.label || "Web"} Search`,
        detail: "DEFAULT SEARCH",
        action: "fill",
        value: engine?.prefix ? `${engine.prefix} ` : "",
      });
      window.location.assign(destination);
    }
  }

  // ---------------------------------------------------------------------------
  // Query Suggestions
  // ---------------------------------------------------------------------------

  let suggestionItems = [];
  let activeSuggestionIndex = -1;
  let suggestionHideTimer;

  const commandSuggestions = [
    { label: "> theme dark", detail: "Switch to Night Observatory", action: "fill", value: "> theme dark", code: "CMD" },
    { label: "> theme light", detail: "Switch to Prospero Light", action: "fill", value: "> theme light", code: "CMD" },
    { label: "> theme toggle", detail: "Toggle authored theme state", action: "fill", value: "> theme toggle", code: "CMD" },
    { label: "> note ", detail: "Append to Field Record", action: "fill", value: "> note ", code: "CMD" },
    { label: "> vector edit", detail: "Edit Current Vector", action: "fill", value: "> vector edit", code: "CMD" },
    { label: "> settings", detail: "Open System Configuration", action: "fill", value: "> settings", code: "CMD" },
    { label: "> focus", detail: "Switch to Focus presentation", action: "fill", value: "> focus", code: "CMD" },
    { label: "> dashboard", detail: "Switch to Dashboard presentation", action: "fill", value: "> dashboard", code: "CMD" },
    { label: "> export config", detail: "Download Gate configuration", action: "fill", value: "> export config", code: "CMD" },
    { label: "> snapshot", detail: "Create a local Gate restore point", action: "fill", value: "> snapshot", code: "CMD" },
    { label: "> diagnostics", detail: "Check local Gate configuration", action: "fill", value: "> diagnostics", code: "CMD" },
    { label: "> repair config", detail: "Normalize local Gate configuration", action: "fill", value: "> repair config", code: "CMD" },
    { label: "> clear recent", detail: "Clear Recent Transits", action: "fill", value: "> clear recent", code: "CMD" },
    { label: "> home", detail: "Return to Neutriverse", action: "fill", value: "> home", code: "CMD" },
  ];

  function engineSuggestions() {
    return Object.values(engines).map((engine) => ({
      label: `${engine.prefix} `,
      detail: `${engine.label} search`,
      action: "fill",
      value: `${engine.prefix} `,
      code: String(engine.prefix || "").toUpperCase(),
    }));
  }

  function launchSuggestions() {
    return launchNodes
      .filter((node) => !node.hidden)
      .map((node) => ({
        label: node.dataset.gateCommand
          ? node.dataset.gateCommand.toUpperCase()
          : node.dataset.gateLabel?.toUpperCase() || "LAUNCH",
        detail: "Launch route",
        action: "url",
        value: node.href,
        code: "↗",
      }));
  }

  function routeSuggestions() {
    return routeNodes.map((node) => ({
      label: node.dataset.gateTransitLabel || node.textContent.trim(),
      detail: node.dataset.gateTransitDetail || "Internal route",
      action: "url",
      value: node.href,
      code: "/",
    }));
  }

  function contextRouteSuggestions() {
    return contextRouteNodes.map((node) => ({
      label: node.dataset.gateTransitLabel || node.textContent.trim(),
      detail: node.dataset.gateTransitDetail || "Context route",
      action: "url",
      value: node.href,
      code: "◇",
    }));
  }

  function recentSuggestions() {
    if (!moduleEnabled("recent_transits")) return [];

    return readRecentTransits().slice(0, 5).map((item) => ({
      ...item,
      code: "↺",
    }));
  }

  function matchesSuggestion(item, query) {
    const haystack = `${item.label} ${item.detail} ${item.value}`.toLowerCase();
    return haystack.includes(query.toLowerCase());
  }

  function buildSuggestionGroups(value) {
    const query = value.trim();

    if (!query) {
      const recent = recentSuggestions();
      const groups = [];

      if (recent.length) {
        groups.push({ title: "RECENT TRANSITS", items: recent });
      }

      groups.push({
        title: "QUICK COMMANDS",
        items: [
          ...engineSuggestions().slice(0, 5),
          { label: "> vector edit", detail: "Edit Current Vector", action: "fill", value: "> vector edit", code: "CMD" },
          { label: "> settings", detail: "Open System Configuration", action: "fill", value: "> settings", code: "CMD" },
        ],
      });

      return groups;
    }

    if (query.startsWith(">")) {
      return [{
        title: "COMMAND MODE",
        items: commandSuggestions.filter((item) => matchesSuggestion(item, query)),
      }];
    }

    if (query.startsWith("/")) {
      return [{
        title: "INTERNAL ROUTES",
        items: routeSuggestions().filter((item) => matchesSuggestion(item, query.slice(1))),
      }];
    }

    const prefixMatch = query.split(/\s+/, 1)[0];
    const matchingEngine = engineByPrefix(prefixMatch);

    if (matchingEngine && query.includes(" ")) {
      return [{
        title: `${matchingEngine.label.toUpperCase()} SEARCH`,
        items: [{
          label: query,
          detail: "Execute current search",
          action: "execute",
          value: query,
          code: String(matchingEngine.prefix || "").toUpperCase(),
        }],
      }];
    }

    const pool = [
      ...recentSuggestions(),
      ...launchSuggestions(),
      ...engineSuggestions(),
      ...routeSuggestions(),
      ...contextRouteSuggestions(),
    ];

    const unique = [];
    const seen = new Set();

    pool.forEach((item) => {
      const key = `${item.action}:${item.value}`;

      if (!seen.has(key) && matchesSuggestion(item, query)) {
        seen.add(key);
        unique.push(item);
      }
    });

    return [{ title: "MATCHED VECTORS", items: unique.slice(0, 7) }];
  }

  function renderSuggestions() {
    if (!suggestionsNode || !searchInput) return;

    if (document.activeElement !== searchInput) {
      suggestionsNode.hidden = true;
      return;
    }

    const groups = buildSuggestionGroups(searchInput.value)
      .filter((group) => group.items?.length);

    suggestionItems = groups.flatMap((group) => group.items || []);
    activeSuggestionIndex = -1;

    if (!suggestionItems.length) {
      suggestionsNode.hidden = true;
      return;
    }

    suggestionsNode.replaceChildren();
    let runningIndex = 0;

    groups.forEach((group) => {
      const wrapper = document.createElement("section");
      wrapper.className = "gate-suggestion-group";

      const heading = document.createElement("div");
      heading.className = "gate-suggestion-group-title";

      const headingLabel = document.createElement("span");
      headingLabel.textContent = group.title;

      const headingCount = document.createElement("span");
      headingCount.textContent = String(group.items.length);

      heading.append(headingLabel, headingCount);
      wrapper.appendChild(heading);

      group.items.forEach((item) => {
        const itemIndex = runningIndex;
        const button = document.createElement("button");
        button.type = "button";
        button.className = "gate-suggestion";
        button.setAttribute("role", "option");
        button.setAttribute("aria-selected", "false");
        button.dataset.suggestionIndex = String(itemIndex);

        const code = document.createElement("span");
        code.className = "gate-suggestion-code";
        code.textContent = item.code || "•";

        const main = document.createElement("span");
        main.className = "gate-suggestion-main";

        const strong = document.createElement("strong");
        strong.textContent = item.label;

        const small = document.createElement("small");
        small.textContent = item.detail || "";

        main.append(strong, small);

        const hint = document.createElement("span");
        hint.className = "gate-suggestion-hint";
        hint.textContent =
          item.action === "fill" ? "INSERT" :
          item.action === "execute" ? "EXECUTE" :
          "OPEN";

        button.append(code, main, hint);
        wrapper.appendChild(button);
        runningIndex += 1;
      });

      suggestionsNode.appendChild(wrapper);
    });

    suggestionsNode.hidden = false;
  }

  function syncActiveSuggestion() {
    if (!suggestionsNode) return;

    suggestionsNode.querySelectorAll("[data-suggestion-index]").forEach((node) => {
      const selected = Number(node.dataset.suggestionIndex) === activeSuggestionIndex;
      node.classList.toggle("is-active", selected);
      node.setAttribute("aria-selected", selected ? "true" : "false");

      if (selected) {
        node.scrollIntoView({ block: "nearest" });
      }
    });
  }

  function chooseSuggestion(index = activeSuggestionIndex) {
    const item = suggestionItems[index];

    if (!item || !searchInput) return false;

    if (item.action === "fill") {
      searchInput.value = item.value;
      searchInput.focus();
      searchInput.setSelectionRange(searchInput.value.length, searchInput.value.length);
      renderSuggestions();
      return true;
    }

    if (item.action === "execute") {
      executeQuery(item.value);
      return true;
    }

    if (item.action === "url") {
      recordTransit(item);
      window.location.assign(item.value);
      return true;
    }

    return false;
  }

  suggestionsNode?.addEventListener("pointerdown", (event) => {
    event.preventDefault();
  });

  suggestionsNode?.addEventListener("click", (event) => {
    const button = event.target.closest?.("[data-suggestion-index]");

    if (button) {
      chooseSuggestion(Number(button.dataset.suggestionIndex));
    }
  });

  searchInput?.addEventListener("focus", () => {
    window.clearTimeout(suggestionHideTimer);
    renderSuggestions();
  });

  searchInput?.addEventListener("blur", () => {
    suggestionHideTimer = window.setTimeout(() => {
      if (suggestionsNode) suggestionsNode.hidden = true;
    }, 120);
  });

  searchInput?.addEventListener("input", () => {
    renderSuggestions();

    if (!queryState) return;

    const value = searchInput.value.trim();

    if (!value) {
      syncQueryContext();
      return;
    }

    if (value.startsWith(">")) {
      queryState.textContent = "COMMAND MODE";
      return;
    }

    if (value.startsWith("/")) {
      queryState.textContent = "INTERNAL ROUTE";
      return;
    }

    const prefix = value.split(/\s+/, 1)[0];
    const engine = engineByPrefix(prefix);

    queryState.textContent = engine
      ? `${engine.label.toUpperCase()} SEARCH`
      : `${defaultEngine()?.label?.toUpperCase() || "WEB"} SEARCH`;
  });

  searchForm?.addEventListener("submit", (event) => {
    event.preventDefault();
    executeQuery(searchInput?.value || "");
  });

  // ---------------------------------------------------------------------------
  // Local Conditions
  // ---------------------------------------------------------------------------

  const weatherPanel = qs("[data-gate-weather-panel]");
  const weatherEmpty = qs("[data-gate-weather-empty]");
  const weatherData = qs("[data-gate-weather-data]");
  const weatherTemp = qs("[data-gate-weather-temp]");
  const weatherLabel = qs("[data-gate-weather-label]");
  const weatherFeels = qs("[data-gate-weather-feels]");
  const weatherWind = qs("[data-gate-weather-wind]");
  const weatherLocation = qs("[data-gate-weather-location]");
  const weatherUpdated = qs("[data-gate-weather-updated]");
  const weatherDays = qs("[data-gate-weather-days]");
  const locateButtons = qsa("[data-gate-locate]");

  const weatherLocationKey = "neutriverse-gate-weather-location";
  const weatherCacheKey = "neutriverse-gate-weather-cache";
  const weatherCacheMaxAge = 15 * 60 * 1000;

  const weatherCodes = new Map([
    [0, "CLEAR"],
    [1, "MAINLY CLEAR"],
    [2, "PARTLY CLOUDY"],
    [3, "OVERCAST"],
    [45, "FOG"],
    [48, "RIME FOG"],
    [51, "LIGHT DRIZZLE"],
    [53, "DRIZZLE"],
    [55, "HEAVY DRIZZLE"],
    [56, "FREEZING DRIZZLE"],
    [57, "HEAVY FREEZING DRIZZLE"],
    [61, "LIGHT RAIN"],
    [63, "RAIN"],
    [65, "HEAVY RAIN"],
    [66, "FREEZING RAIN"],
    [67, "HEAVY FREEZING RAIN"],
    [71, "LIGHT SNOW"],
    [73, "SNOW"],
    [75, "HEAVY SNOW"],
    [77, "SNOW GRAINS"],
    [80, "RAIN SHOWERS"],
    [81, "RAIN SHOWERS"],
    [82, "HEAVY SHOWERS"],
    [85, "SNOW SHOWERS"],
    [86, "HEAVY SNOW SHOWERS"],
    [95, "THUNDERSTORM"],
    [96, "THUNDERSTORM / HAIL"],
    [99, "HEAVY THUNDERSTORM / HAIL"],
  ]);

  function weatherCodeLabel(code) {
    return weatherCodes.get(Number(code)) || "VARIABLE";
  }

  function showWeatherEmpty(message = "NO LOCAL FIX") {
    if (!weatherPanel) return;

    weatherEmpty?.removeAttribute("hidden");
    weatherData?.setAttribute("hidden", "");

    const title = weatherEmpty?.querySelector("strong");
    if (title) title.textContent = message;
  }

  function renderWeather(payload, location) {
    if (!payload?.current || !payload?.daily) {
      showWeatherEmpty("WEATHER UNAVAILABLE");
      return;
    }

    weatherEmpty?.setAttribute("hidden", "");
    weatherData?.removeAttribute("hidden");

    const current = payload.current;
    const daily = payload.daily;

    if (weatherTemp) weatherTemp.textContent = `${Math.round(current.temperature_2m)}°`;
    if (weatherLabel) weatherLabel.textContent = weatherCodeLabel(current.weather_code);
    if (weatherFeels) weatherFeels.textContent = `${Math.round(current.apparent_temperature)}°`;
    if (weatherWind) weatherWind.textContent = `${Math.round(current.wind_speed_10m)} KM/H`;

    if (weatherLocation) {
      const zone = payload.timezone_abbreviation || resolvedZone;
      const latitude = Math.abs(location.latitude).toFixed(2);
      const longitude = Math.abs(location.longitude).toFixed(2);
      weatherLocation.textContent =
        `${String(zone).toUpperCase()} · ${latitude}${location.latitude >= 0 ? "N" : "S"} / ${longitude}${location.longitude >= 0 ? "E" : "W"}`;
    }

    if (weatherDays) {
      weatherDays.replaceChildren();

      const count = Math.min(3, daily.time?.length || 0);

      for (let index = 0; index < count; index += 1) {
        const day = document.createElement("div");
        day.className = "gate-weather-day";

        const dayLabel = new Intl.DateTimeFormat("en-GB", {
          weekday: "short",
        }).format(new Date(`${daily.time[index]}T12:00:00`)).toUpperCase();

        const max = Math.round(daily.temperature_2m_max[index]);
        const min = Math.round(daily.temperature_2m_min[index]);
        const rain = daily.precipitation_probability_max?.[index];

        const label = document.createElement("span");
        label.textContent = dayLabel;

        const temperatures = document.createElement("strong");
        temperatures.textContent = `${max}° / ${min}°`;

        const detail = document.createElement("small");
        detail.textContent = Number.isFinite(rain)
          ? `${Math.round(rain)}% PRECIP`
          : weatherCodeLabel(daily.weather_code?.[index]);

        day.append(label, temperatures, detail);
        weatherDays.appendChild(day);
      }
    }

    if (weatherUpdated) {
      weatherUpdated.textContent = `SYNC ${new Intl.DateTimeFormat("en-GB", {
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
      }).format(new Date())}`;
    }
  }

  async function fetchWeather(location, { force = false } = {}) {
    if (!weatherPanel || !moduleEnabled("local_conditions") || !location) return;

    const cached = readJson(weatherCacheKey, null);

    if (!force && cached?.timestamp && cached?.payload) {
      const fresh = Date.now() - cached.timestamp < weatherCacheMaxAge;
      const sameLocation =
        Math.abs((cached.latitude || 0) - location.latitude) < 0.001 &&
        Math.abs((cached.longitude || 0) - location.longitude) < 0.001;

      if (fresh && sameLocation) {
        renderWeather(cached.payload, location);
        return;
      }
    }

    if (weatherUpdated) weatherUpdated.textContent = "SYNCING";

    const params = new URLSearchParams({
      latitude: String(location.latitude),
      longitude: String(location.longitude),
      current: "temperature_2m,apparent_temperature,weather_code,wind_speed_10m",
      daily: "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max",
      forecast_days: "3",
      timezone: "auto",
    });

    try {
      const response = await fetch(`https://api.open-meteo.com/v1/forecast?${params}`, {
        headers: { Accept: "application/json" },
      });

      if (!response.ok) {
        throw new Error(`Weather request failed: ${response.status}`);
      }

      const payload = await response.json();

      writeJson(weatherCacheKey, {
        timestamp: Date.now(),
        latitude: location.latitude,
        longitude: location.longitude,
        payload,
      });

      renderWeather(payload, location);
    } catch {
      if (cached?.payload) {
        renderWeather(cached.payload, location);

        if (weatherUpdated) weatherUpdated.textContent = "CACHED";
        return;
      }

      showWeatherEmpty("WEATHER UNAVAILABLE");
    }
  }

  function resetLocateButtons() {
    locateButtons.forEach((button) => {
      button.disabled = false;
      button.textContent = button.closest("[data-gate-weather-data]") ? "RELOCATE" : "LOCATE";
    });
  }

  function requestLocation() {
    if (!moduleEnabled("local_conditions")) return;

    if (!navigator.geolocation) {
      showWeatherEmpty("LOCATION UNSUPPORTED");
      return;
    }

    locateButtons.forEach((button) => {
      button.disabled = true;
      button.textContent = "LOCATING";
    });

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const location = {
          latitude: Number(position.coords.latitude.toFixed(4)),
          longitude: Number(position.coords.longitude.toFixed(4)),
        };

        writeJson(weatherLocationKey, location);
        resetLocateButtons();
        fetchWeather(location, { force: true });
      },
      () => {
        resetLocateButtons();
        showWeatherEmpty("LOCATION DENIED");
      },
      {
        enableHighAccuracy: false,
        timeout: 9000,
        maximumAge: 24 * 60 * 60 * 1000,
      }
    );
  }

  function clearWeather() {
    storage.remove(weatherLocationKey);
    storage.remove(weatherCacheKey);
    showWeatherEmpty();
  }

  function syncWeatherPreference() {
    if (!weatherPanel || !moduleEnabled("local_conditions")) return;

    const savedLocation = readJson(weatherLocationKey, null);

    if (savedLocation?.latitude && savedLocation?.longitude) {
      fetchWeather(savedLocation);
    } else {
      showWeatherEmpty();
    }
  }

  locateButtons.forEach((button) => {
    button.addEventListener("click", requestLocation);
  });

  syncWeatherPreference();

  // ---------------------------------------------------------------------------
  // Settings Drawer
  // ---------------------------------------------------------------------------

  const settingsOpenButton = qs("[data-gate-settings-open]");
  const settingsDrawer = qs("[data-gate-settings-drawer]");
  const settingsBackdrop = qs("[data-gate-settings-backdrop]");
  const settingsCloseButton = qs("[data-gate-settings-close]");
  const settingSearch = qs("[data-gate-setting-search]");
  const settingDensity = qs("[data-gate-setting-density]");
  const settingAmbient = qs("[data-gate-setting-ambient]");
  const settingRouteShortcuts = qs("[data-gate-setting-route-shortcuts]");
  const settingModuleInputs = qsa("[data-gate-setting-module]");
  const settingRouteGroup = qs("[data-gate-setting-route-group]");
  const settingPresentation = qs("[data-gate-setting-presentation]");
  const dashboardSettingsNode = qs("[data-gate-dashboard-settings]");
  const routeEditGroup = qs("[data-gate-route-edit-group]");
  const routeEditorList = qs("[data-gate-route-editor-list]");
  const routeSaveGroupButton = qs("[data-gate-route-save-group]");
  const routeResetGroupButton = qs("[data-gate-route-reset-group]");

  const customLaunchLabel = qs("[data-gate-custom-launch-label]");
  const customLaunchRole = qs("[data-gate-custom-launch-role]");
  const customLaunchUrl = qs("[data-gate-custom-launch-url]");
  const addCustomLaunchButton = qs("[data-gate-add-custom-launch]");
  const cancelCustomLaunchButton = qs("[data-gate-cancel-custom-launch]");
  const customLaunchCount = qs("[data-gate-custom-launch-count]");

  const customGroupLabel = qs("[data-gate-custom-group-label]");
  const customGroupDetail = qs("[data-gate-custom-group-detail]");
  const addCustomGroupButton = qs("[data-gate-add-custom-group]");
  const cancelCustomGroupButton = qs("[data-gate-cancel-custom-group]");
  const customGroupCount = qs("[data-gate-custom-group-count]");
  const customGroupList = qs("[data-gate-custom-group-list]");

  const queryPresetGroup = qs("[data-gate-query-preset-group]");
  const queryPresetEngine = qs("[data-gate-query-preset-engine]");
  const queryPresetPlaceholder = qs("[data-gate-query-preset-placeholder]");
  const saveQueryPresetButton = qs("[data-gate-save-query-preset]");
  const resetQueryPresetButton = qs("[data-gate-reset-query-preset]");

  const contextLaunchGroup = qs("[data-gate-context-launch-group]");
  const contextLaunchList = qs("[data-gate-context-launch-list]");
  const resetContextLaunchesButton = qs("[data-gate-reset-context-launches]");

  const routeOrderList = qs("[data-gate-route-order-list]");
  const unpinRouteGroupButton = qs("[data-gate-unpin-route-group]");

  const settingsFilterInput = qs("[data-gate-settings-filter]");
  const settingsFilterState = qs("[data-gate-settings-filter-state]");
  const settingsJumpSelect = qs("[data-gate-settings-jump]");
  const settingsSections = qsa(".gate-settings-section");

  const contextProfileGroup = qs("[data-gate-context-profile-group]");
  const contextProfileSearch = qs("[data-gate-context-profile-search]");
  const contextProfileLaunches = qs("[data-gate-context-profile-launches]");
  const contextProfileRoutes = qs("[data-gate-context-profile-routes]");
  const contextProfileShortcut = qs("[data-gate-context-profile-shortcut]");
  const contextProfileNote = qs("[data-gate-context-profile-note]");
  const copyContextProfileButton = qs("[data-gate-copy-context-profile]");
  const exportContextProfileButton = qs("[data-gate-export-context-profile]");

  const snapshotLabel = qs("[data-gate-snapshot-label]");
  const snapshotTag = qs("[data-gate-snapshot-tag]");
  const snapshotReason = qs("[data-gate-snapshot-reason]");
  const createSnapshotButton = qs("[data-gate-create-snapshot]");
  const snapshotList = qs("[data-gate-snapshot-list]");
  const snapshotDiffPanel = qs("[data-gate-snapshot-diff]");
  const snapshotDiffTitle = qs("[data-gate-snapshot-diff-title]");
  const snapshotDiffList = qs("[data-gate-snapshot-diff-list]");
  const snapshotDiffCloseButton = qs("[data-gate-snapshot-diff-close]");
  const snapshotDiffRestoreButton = qs("[data-gate-snapshot-diff-restore]");

  const diagnosticsSummary = qs("[data-gate-diagnostics-summary]");
  const diagnosticsList = qs("[data-gate-diagnostics-list]");
  const runDiagnosticsButton = qs("[data-gate-run-diagnostics]");
  const repairConfigButton = qs("[data-gate-repair-config]");

  const exportConfigButton = qs("[data-gate-export-config]");
  const importConfigButton = qs("[data-gate-import-config]");
  const importConfigFile = qs("[data-gate-import-file]");
  const launchSettingsNode = qs("[data-gate-launch-settings]");
  const settingsStatus = qs("[data-gate-settings-status]");

  const clearRecentButton = qs("[data-gate-clear-recent]");
  const clearWeatherButton = qs("[data-gate-clear-weather]");
  const resetVectorButton = qs("[data-gate-reset-vector]");
  const clearNoteButton = qs("[data-gate-clear-note]");
  const resetSettingsButton = qs("[data-gate-reset-settings]");

  const snapshotKey = "neutriverse-gate-config-snapshots-v1";
  const snapshotLimit = Number(settingsDefault.limits?.config_snapshots) || 5;

  let settingsReturnFocus = null;
  let settingsCloseTimer;

  function setSettingsStatus(message) {
    if (!settingsStatus) return;

    settingsStatus.textContent = message;

    window.setTimeout(() => {
      if (settingsStatus?.textContent === message) {
        settingsStatus.textContent = "LOCAL CONFIGURATION";
      }
    }, 1800);
  }

  function filterSettingsSections(value = settingsFilterInput?.value || "") {
    const query = value.trim().toLowerCase();
    let visibleCount = 0;

    settingsSections.forEach((section) => {
      const haystack = section.textContent.toLowerCase();
      const matches = !query || haystack.includes(query);

      section.classList.toggle("is-filtered-out", !matches);

      if (matches) {
        visibleCount += 1;
      }
    });

    if (settingsFilterState) {
      settingsFilterState.textContent = query
        ? `${visibleCount} / ${settingsSections.length} MATCH`
        : "ALL SECTIONS";
    }
  }

  function renderLaunchSettings() {
    if (!launchSettingsNode) return;

    launchSettingsNode.replaceChildren();

    const hidden = new Set(preferences.hiddenLaunches);
    const allNodes = new Map(
      qsa("[data-gate-launch]").map((node) => [
        node.dataset.gateLaunchId || node.dataset.gateCommand,
        node,
      ])
    );

    preferences.launchOrder.forEach((id, index) => {
      const node = allNodes.get(id);
      if (!node) return;

      const row = document.createElement("div");
      row.className = "gate-launch-setting-row";

      const visible = document.createElement("input");
      visible.type = "checkbox";
      visible.checked = !hidden.has(id);
      visible.setAttribute("aria-label", `显示 ${node.dataset.gateLabel || id}`);
      visible.addEventListener("change", () => {
        const nextHidden = new Set(preferences.hiddenLaunches);

        if (visible.checked) nextHidden.delete(id);
        else nextHidden.add(id);

        savePreferences({
          ...preferences,
          hiddenLaunches: [...nextHidden],
        });

        setSettingsStatus("LAUNCH ROUTES UPDATED");
      });

      const label = document.createElement("span");
      label.className = "gate-launch-setting-label";

      const strong = document.createElement("strong");
      strong.textContent = (node.dataset.gateLabel || id).toUpperCase();

      const small = document.createElement("small");
      small.textContent = node.querySelector("small")?.textContent || "LAUNCH ROUTE";

      label.append(strong, small);

      const controls = document.createElement("span");
      controls.className = "gate-launch-setting-controls";

      const up = document.createElement("button");
      up.type = "button";
      up.textContent = "↑";
      up.disabled = index === 0;
      up.setAttribute("aria-label", `上移 ${strong.textContent}`);

      const down = document.createElement("button");
      down.type = "button";
      down.textContent = "↓";
      down.disabled = index === preferences.launchOrder.length - 1;
      down.setAttribute("aria-label", `下移 ${strong.textContent}`);

      up.addEventListener("click", () => {
        if (index <= 0) return;

        const order = [...preferences.launchOrder];
        [order[index - 1], order[index]] = [order[index], order[index - 1]];
        savePreferences({ ...preferences, launchOrder: order });
        setSettingsStatus("LAUNCH ORDER UPDATED");
      });

      down.addEventListener("click", () => {
        if (index >= preferences.launchOrder.length - 1) return;

        const order = [...preferences.launchOrder];
        [order[index + 1], order[index]] = [order[index], order[index + 1]];
        savePreferences({ ...preferences, launchOrder: order });
        setSettingsStatus("LAUNCH ORDER UPDATED");
      });

      controls.append(up, down);

      if (node.dataset.gateCustomLaunch === "true") {
        const edit = document.createElement("button");
        edit.type = "button";
        edit.className = "gate-launch-edit";
        edit.textContent = "EDIT";
        edit.setAttribute("aria-label", `编辑 ${strong.textContent}`);
        edit.addEventListener("click", () => beginEditCustomLaunch(id));

        const remove = document.createElement("button");
        remove.type = "button";
        remove.className = "gate-launch-delete";
        remove.textContent = "×";
        remove.setAttribute("aria-label", `删除 ${strong.textContent}`);

        remove.addEventListener("click", () => {
          savePreferences({
            ...preferences,
            customLaunches: preferences.customLaunches.filter((item) => item.id !== id),
            launchOrder: preferences.launchOrder.filter((itemId) => itemId !== id),
            hiddenLaunches: preferences.hiddenLaunches.filter((itemId) => itemId !== id),
          });

          if (editingCustomLaunchId === id) {
            resetCustomLaunchEditor();
          }

          setSettingsStatus("CUSTOM LAUNCH REMOVED");
        });

        controls.append(edit, remove);
      }

      row.append(visible, label, controls);
      launchSettingsNode.appendChild(row);
    });
  }

  const dashboardLabels = {
    current_vector: ["CURRENT VECTOR", "Active trajectory"],
    local_conditions: ["LOCAL CONDITIONS", "Weather node"],
    active_systems: ["ACTIVE SYSTEMS", "Internal facility routes"],
    field_record: ["FIELD RECORD", "Local transient memory"],
  };

  function renderDashboardSettings() {
    if (!dashboardSettingsNode) {
      return;
    }

    dashboardSettingsNode.replaceChildren();

    preferences.dashboardOrder.forEach((id, index) => {
      const labels = dashboardLabels[id] || [id.toUpperCase(), "MODULE"];
      const row = document.createElement("div");
      row.className = "gate-dashboard-setting-row";

      const code = document.createElement("span");
      code.className = "gate-dashboard-setting-code";
      code.textContent = String(index + 1).padStart(2, "0");

      const label = document.createElement("span");
      label.className = "gate-dashboard-setting-label";

      const strong = document.createElement("strong");
      strong.textContent = labels[0];

      const small = document.createElement("small");
      small.textContent = labels[1];

      label.append(strong, small);

      const spanSelect = document.createElement("select");
      spanSelect.className = "gate-dashboard-setting-span";
      spanSelect.setAttribute("aria-label", `${labels[0]} 宽度`);

      if (id === "field_record") {
        const full = document.createElement("option");
        full.value = "full";
        full.textContent = "FULL";
        spanSelect.appendChild(full);
        spanSelect.value = "full";
        spanSelect.disabled = true;
      } else {
        ["standard", "wide"].forEach((value) => {
          const option = document.createElement("option");
          option.value = value;
          option.textContent = value.toUpperCase();
          spanSelect.appendChild(option);
        });

        spanSelect.value = preferences.dashboardSpans?.[id] === "wide" ? "wide" : "standard";

        spanSelect.addEventListener("change", () => {
          savePreferences({
            ...preferences,
            dashboardSpans: {
              ...preferences.dashboardSpans,
              [id]: spanSelect.value,
            },
          });

          setSettingsStatus("MODULE WIDTH UPDATED");
        });
      }

      const controls = document.createElement("span");
      controls.className = "gate-dashboard-setting-controls";

      const up = document.createElement("button");
      up.type = "button";
      up.textContent = "↑";
      up.disabled = index === 0;
      up.setAttribute("aria-label", `上移 ${labels[0]}`);

      const down = document.createElement("button");
      down.type = "button";
      down.textContent = "↓";
      down.disabled = index === preferences.dashboardOrder.length - 1;
      down.setAttribute("aria-label", `下移 ${labels[0]}`);

      up.addEventListener("click", () => {
        if (index <= 0) return;

        const order = [...preferences.dashboardOrder];
        [order[index - 1], order[index]] = [order[index], order[index - 1]];

        savePreferences({
          ...preferences,
          dashboardOrder: order,
        });

        setSettingsStatus("DASHBOARD ORDER UPDATED");
      });

      down.addEventListener("click", () => {
        if (index >= preferences.dashboardOrder.length - 1) return;

        const order = [...preferences.dashboardOrder];
        [order[index + 1], order[index]] = [order[index], order[index + 1]];

        savePreferences({
          ...preferences,
          dashboardOrder: order,
        });

        setSettingsStatus("DASHBOARD ORDER UPDATED");
      });

      controls.append(up, down);
      row.append(code, label, spanSelect, controls);
      dashboardSettingsNode.appendChild(row);
    });
  }

  function normalizeSnapshotRecord(item) {
    if (
      !item ||
      typeof item !== "object" ||
      typeof item.id !== "string" ||
      !item.preferences ||
      typeof item.preferences !== "object"
    ) {
      return null;
    }

    return {
      id: item.id.slice(0, 96),
      label: cleanText(item.label, 48) || "Gate Snapshot",
      tag: cleanText(item.tag, 24),
      reason: cleanText(item.reason, 120),
      createdAt: typeof item.createdAt === "string"
        ? item.createdAt
        : new Date().toISOString(),
      lastRestoredAt: typeof item.lastRestoredAt === "string"
        ? item.lastRestoredAt
        : "",
      preferences: item.preferences,
      currentVector: item.currentVector || null,
    };
  }

  function readSnapshots() {
    const value = readJson(snapshotKey, []);

    if (!Array.isArray(value)) {
      return [];
    }

    return value
      .map(normalizeSnapshotRecord)
      .filter(Boolean)
      .slice(0, snapshotLimit);
  }

  function writeSnapshots(items) {
    writeJson(snapshotKey, items.slice(0, snapshotLimit));
  }

  function defaultSnapshotLabel(date = new Date()) {
    return `Snapshot ${new Intl.DateTimeFormat("en-GB", {
      day: "2-digit",
      month: "short",
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    }).format(date)}`;
  }

  function createConfigSnapshot(label = snapshotLabel?.value) {
    const now = new Date();
    const snapshot = {
      id: `snapshot-${now.getTime().toString(36)}-${Math.random().toString(36).slice(2, 6)}`,
      label: cleanText(label, 48) || defaultSnapshotLabel(now),
      tag: cleanText(snapshotTag?.value, 24),
      reason: cleanText(snapshotReason?.value, 120),
      createdAt: now.toISOString(),
      lastRestoredAt: "",
      preferences: normalizePreferences(preferences),
      currentVector: readVectorOverride(),
    };

    writeSnapshots([snapshot, ...readSnapshots()]);

    if (snapshotLabel) snapshotLabel.value = "";
    if (snapshotTag) snapshotTag.value = "";
    if (snapshotReason) snapshotReason.value = "";

    renderSnapshotList();
    setSettingsStatus("CONFIG SNAPSHOT CREATED");
  }

  let snapshotDiffTargetId = null;

  function renameConfigSnapshot(id) {
    const snapshots = readSnapshots();
    const snapshot = snapshots.find((item) => item.id === id);

    if (!snapshot) {
      setSettingsStatus("SNAPSHOT NOT FOUND");
      return;
    }

    const nextLabel = window.prompt("Rename Gate snapshot:", snapshot.label);

    if (nextLabel === null) {
      return;
    }

    const label = cleanText(nextLabel, 48);

    if (!label) {
      setSettingsStatus("SNAPSHOT LABEL REQUIRED");
      return;
    }

    writeSnapshots(
      snapshots.map((item) =>
        item.id === id
          ? { ...item, label }
          : item
      )
    );

    renderSnapshotList();

    if (snapshotDiffTargetId === id) {
      showSnapshotDiff(id);
    }

    setSettingsStatus("SNAPSHOT RENAMED");
  }

  function snapshotComparable(preferenceValue, vectorValue) {
    const normalized = normalizePreferences(preferenceValue || {});

    return {
      search: {
        defaultSearch: normalized.defaultSearch,
        queryPresets: normalized.queryPresets,
      },
      interface: {
        density: normalized.density,
        ambient: normalized.ambient,
        routeShortcuts: normalized.routeShortcuts,
        presentation: normalized.presentation,
        modules: normalized.modules,
      },
      launch: {
        launchOrder: normalized.launchOrder,
        hiddenLaunches: normalized.hiddenLaunches,
        customLaunches: normalized.customLaunches,
        contextLaunchHidden: normalized.contextLaunchHidden,
      },
      context: {
        activeRouteGroup: normalized.activeRouteGroup,
        routeGroupOrder: normalized.routeGroupOrder,
        pinnedRouteGroup: normalized.pinnedRouteGroup,
        customRouteGroups: normalized.customRouteGroups,
        routeOverrides: normalized.routeOverrides,
      },
      dashboard: {
        dashboardOrder: normalized.dashboardOrder,
        dashboardSpans: normalized.dashboardSpans,
      },
      vector: (() => {
        const vector = normalizeImportedVector(vectorValue);

        return vector
          ? {
              title: vector.title,
              status: vector.status,
              description: vector.description,
            }
          : null;
      })(),
    };
  }

  function sameSnapshotValue(left, right) {
    return JSON.stringify(left ?? null) === JSON.stringify(right ?? null);
  }

  function namedItemsById(items = []) {
    return new Map(
      items
        .filter((item) => item && typeof item.id === "string")
        .map((item) => [item.id, item])
    );
  }

  function compactDiffParts(parts, limit = 6) {
    const visible = parts.slice(0, limit);

    if (parts.length > limit) {
      visible.push(`+${parts.length - limit} more`);
    }

    return visible.join("; ");
  }

  function customLaunchDiffDetails(currentLaunch, savedLaunch) {
    const currentMap = namedItemsById(currentLaunch.customLaunches);
    const savedMap = namedItemsById(savedLaunch.customLaunches);
    const details = [];

    savedMap.forEach((item, id) => {
      if (!currentMap.has(id)) {
        details.push(`added ${item.label} (${item.role})`);
      }
    });

    currentMap.forEach((item, id) => {
      if (!savedMap.has(id)) {
        details.push(`removed ${item.label} (${item.role})`);
      }
    });

    currentMap.forEach((currentItem, id) => {
      const savedItem = savedMap.get(id);

      if (!savedItem) {
        return;
      }

      const fieldChanges = [];

      if (currentItem.label !== savedItem.label) {
        fieldChanges.push(`label ${currentItem.label} → ${savedItem.label}`);
      }

      if (currentItem.role !== savedItem.role) {
        fieldChanges.push(`role ${currentItem.role} → ${savedItem.role}`);
      }

      if (currentItem.url !== savedItem.url) {
        fieldChanges.push(`URL ${currentItem.url} → ${savedItem.url}`);
      }

      if (fieldChanges.length) {
        details.push(`${savedItem.label}: ${fieldChanges.join(", ")}`);
      }
    });

    const currentHidden = new Set(currentLaunch.hiddenLaunches || []);
    const savedHidden = new Set(savedLaunch.hiddenLaunches || []);

    const newlyHidden = [...savedHidden].filter((id) => !currentHidden.has(id));
    const newlyVisible = [...currentHidden].filter((id) => !savedHidden.has(id));

    if (newlyHidden.length) {
      details.push(`globally hidden: ${newlyHidden.join(", ")}`);
    }

    if (newlyVisible.length) {
      details.push(`globally visible: ${newlyVisible.join(", ")}`);
    }

    const currentRules = currentLaunch.contextLaunchHidden || {};
    const savedRules = savedLaunch.contextLaunchHidden || {};
    const ruleGroups = new Set([
      ...Object.keys(currentRules),
      ...Object.keys(savedRules),
    ]);

    ruleGroups.forEach((groupId) => {
      if (!sameSnapshotValue(currentRules[groupId] || [], savedRules[groupId] || [])) {
        details.push(
          `${groupId} context-hidden: ` +
          `${(currentRules[groupId] || []).join(", ") || "none"} → ` +
          `${(savedRules[groupId] || []).join(", ") || "none"}`
        );
      }
    });

    return details;
  }

  function queryPresetDiffDetails(currentSearch, savedSearch) {
    const currentPresets = currentSearch.queryPresets || {};
    const savedPresets = savedSearch.queryPresets || {};
    const groupIds = new Set([
      ...Object.keys(currentPresets),
      ...Object.keys(savedPresets),
    ]);
    const details = [];

    groupIds.forEach((groupId) => {
      const currentPreset = currentPresets[groupId] || {};
      const savedPreset = savedPresets[groupId] || {};

      if (sameSnapshotValue(currentPreset, savedPreset)) {
        return;
      }

      const currentEngine = currentPreset.engine || "GLOBAL";
      const savedEngine = savedPreset.engine || "GLOBAL";
      const currentPlaceholder = currentPreset.placeholder || "default hint";
      const savedPlaceholder = savedPreset.placeholder || "default hint";

      details.push(
        `${groupId}: engine ${currentEngine} → ${savedEngine}; ` +
        `hint ${currentPlaceholder} → ${savedPlaceholder}`
      );
    });

    return details;
  }

  function snapshotGroups(context) {
    return [
      ...(Array.isArray(routeGroupsDefault) ? routeGroupsDefault : []),
      ...(context.customRouteGroups || []),
    ];
  }

  function snapshotResolvedRoute(context, groupId, slotIndex) {
    const custom = (context.customRouteGroups || [])
      .find((group) => group.id === groupId);

    if (custom) {
      const route = custom.routes?.[slotIndex] || {};

      return {
        label: route.label || "UNASSIGNED",
        detail: route.detail || "CUSTOM ROUTE",
        url: route.url || "",
      };
    }

    const baseGroup = (Array.isArray(routeGroupsDefault) ? routeGroupsDefault : [])
      .find((group) => group.id === groupId);
    const defaults = baseGroup?.routes?.[slotIndex] || {};
    const override = context.routeOverrides?.[groupId]?.[slotIndex] || {};

    return {
      label: override.label || defaults.label || `Route ${slotIndex + 1}`,
      detail: override.detail || defaults.detail || "ROUTE",
      url: override.url || defaults.url || "",
    };
  }

  function routeContextDiffDetails(currentContext, savedContext) {
    const currentGroups = namedItemsById(snapshotGroups(currentContext));
    const savedGroups = namedItemsById(snapshotGroups(savedContext));
    const details = [];

    savedGroups.forEach((group, id) => {
      if (!currentGroups.has(id)) {
        details.push(`group added ${group.label}`);
      }
    });

    currentGroups.forEach((group, id) => {
      if (!savedGroups.has(id)) {
        details.push(`group removed ${group.label}`);
      }
    });

    currentGroups.forEach((currentGroup, groupId) => {
      const savedGroup = savedGroups.get(groupId);

      if (!savedGroup) {
        return;
      }

      if (
        currentGroup.label !== savedGroup.label ||
        currentGroup.detail !== savedGroup.detail
      ) {
        details.push(
          `group ${currentGroup.label}: ` +
          `${currentGroup.label}/${currentGroup.detail || "—"} → ` +
          `${savedGroup.label}/${savedGroup.detail || "—"}`
        );
      }

      for (let slotIndex = 0; slotIndex < routesPerGroup; slotIndex += 1) {
        const currentRoute = snapshotResolvedRoute(
          currentContext,
          groupId,
          slotIndex
        );
        const savedRoute = snapshotResolvedRoute(
          savedContext,
          groupId,
          slotIndex
        );

        if (!sameSnapshotValue(currentRoute, savedRoute)) {
          details.push(
            `${savedGroup.label} route ${slotIndex + 1}: ` +
            `${currentRoute.label} → ${savedRoute.label}; ` +
            `${currentRoute.url || "unassigned"} → ${savedRoute.url || "unassigned"}`
          );
        }
      }
    });

    return details;
  }

  function dashboardDiffDetails(currentDashboard, savedDashboard) {
    const details = [];

    if (!sameSnapshotValue(currentDashboard.dashboardOrder, savedDashboard.dashboardOrder)) {
      details.push(
        `order ${currentDashboard.dashboardOrder.join(" / ")} → ` +
        `${savedDashboard.dashboardOrder.join(" / ")}`
      );
    }

    Object.keys(currentDashboard.dashboardSpans || {}).forEach((id) => {
      const currentSpan = currentDashboard.dashboardSpans?.[id];
      const savedSpan = savedDashboard.dashboardSpans?.[id];

      if (currentSpan !== savedSpan) {
        details.push(`${id} width ${currentSpan} → ${savedSpan}`);
      }
    });

    return details;
  }

  function snapshotDiffSummary(snapshot) {
    const current = snapshotComparable(preferences, readVectorOverride());
    const saved = snapshotComparable(snapshot.preferences, snapshot.currentVector);
    const changes = [];

    if (!sameSnapshotValue(current.search, saved.search)) {
      const from = engines[current.search.defaultSearch]?.label || current.search.defaultSearch;
      const to = engines[saved.search.defaultSearch]?.label || saved.search.defaultSearch;
      const presetFrom = Object.keys(current.search.queryPresets || {}).length;
      const presetTo = Object.keys(saved.search.queryPresets || {}).length;

      changes.push({
        label: "SEARCH",
        detail:
          `${from} → ${to}; context presets ${presetFrom} → ${presetTo}.`,
      });

      const presetDetails = queryPresetDiffDetails(current.search, saved.search);

      if (presetDetails.length) {
        changes.push({
          label: "SEARCH · DETAIL",
          detail: compactDiffParts(presetDetails),
          isDetail: true,
        });
      }
    }

    if (!sameSnapshotValue(current.interface, saved.interface)) {
      const activeModules = (value) =>
        Object.values(value.modules || {}).filter((enabled) => enabled !== false).length;

      changes.push({
        label: "INTERFACE",
        detail:
          `${current.interface.presentation.toUpperCase()} → ${saved.interface.presentation.toUpperCase()}; ` +
          `${current.interface.density.toUpperCase()} → ${saved.interface.density.toUpperCase()}; ` +
          `modules ${activeModules(current.interface)} → ${activeModules(saved.interface)}; ` +
          `route shortcuts ${current.interface.routeShortcuts ? "on" : "off"} → ` +
          `${saved.interface.routeShortcuts ? "on" : "off"}.`,
      });
    }

    if (!sameSnapshotValue(current.launch, saved.launch)) {
      const visibleCount = (value, groupId) => {
        const globalHidden = new Set(value.hiddenLaunches || []);
        const contextHidden = new Set(value.contextLaunchHidden?.[groupId] || []);

        return (value.launchOrder || []).filter(
          (id) => !globalHidden.has(id) && !contextHidden.has(id)
        ).length;
      };

      changes.push({
        label: "LAUNCH",
        detail:
          `entries ${current.launch.launchOrder.length} → ${saved.launch.launchOrder.length}; ` +
          `active-context visible ${visibleCount(current.launch, current.context.activeRouteGroup)} → ` +
          `${visibleCount(saved.launch, saved.context.activeRouteGroup)}; ` +
          `custom ${current.launch.customLaunches.length} → ${saved.launch.customLaunches.length}.`,
      });

      const launchDetails = customLaunchDiffDetails(current.launch, saved.launch);

      if (launchDetails.length) {
        changes.push({
          label: "LAUNCH · DETAIL",
          detail: compactDiffParts(launchDetails),
          isDetail: true,
        });
      }
    }

    if (!sameSnapshotValue(current.context, saved.context)) {
      const currentGroup =
        routeGroupDefinition(current.context.activeRouteGroup)?.label ||
        current.context.activeRouteGroup ||
        "—";

      const savedGroups = [
        ...(Array.isArray(routeGroupsDefault) ? routeGroupsDefault : []),
        ...(saved.context.customRouteGroups || []),
      ];
      const savedGroup =
        savedGroups.find((group) => group.id === saved.context.activeRouteGroup)?.label ||
        saved.context.activeRouteGroup ||
        "—";

      changes.push({
        label: "CONTEXT",
        detail:
          `${currentGroup} → ${savedGroup}; groups ` +
          `${current.context.routeGroupOrder.length} → ${saved.context.routeGroupOrder.length}; ` +
          `pin ${current.context.pinnedRouteGroup || "none"} → ${saved.context.pinnedRouteGroup || "none"}.`,
      });

      const contextDetails = routeContextDiffDetails(current.context, saved.context);

      if (contextDetails.length) {
        changes.push({
          label: "CONTEXT · DETAIL",
          detail: compactDiffParts(contextDetails, 8),
          isDetail: true,
        });
      }
    }

    if (!sameSnapshotValue(current.dashboard, saved.dashboard)) {
      changes.push({
        label: "DASHBOARD",
        detail:
          `order ${current.dashboard.dashboardOrder.join(" / ")} → ` +
          `${saved.dashboard.dashboardOrder.join(" / ")}.`,
      });

      const dashboardDetails = dashboardDiffDetails(current.dashboard, saved.dashboard);

      if (dashboardDetails.length) {
        changes.push({
          label: "DASHBOARD · DETAIL",
          detail: compactDiffParts(dashboardDetails),
          isDetail: true,
        });
      }
    }

    if (!sameSnapshotValue(current.vector, saved.vector)) {
      changes.push({
        label: "CURRENT VECTOR",
        detail:
          `${current.vector?.title || "default"} → ${saved.vector?.title || "default"}; ` +
          `${current.vector?.status || "default"} → ${saved.vector?.status || "default"}; ` +
          `description ${current.vector?.description || "default"} → ` +
          `${saved.vector?.description || "default"}.`,
      });
    }

    return changes;
  }

  function closeSnapshotDiff() {
    snapshotDiffTargetId = null;

    if (snapshotDiffPanel) {
      snapshotDiffPanel.hidden = true;
    }

    if (snapshotDiffList) {
      snapshotDiffList.replaceChildren();
    }

    if (snapshotDiffRestoreButton) {
      snapshotDiffRestoreButton.disabled = true;
    }
  }

  function showSnapshotDiff(id) {
    const snapshot = readSnapshots().find((item) => item.id === id);

    if (!snapshot || !snapshotDiffPanel || !snapshotDiffList) {
      setSettingsStatus("SNAPSHOT NOT FOUND");
      return;
    }

    snapshotDiffTargetId = id;
    snapshotDiffList.replaceChildren();

    if (snapshotDiffTitle) {
      snapshotDiffTitle.textContent = `DIFF · ${snapshot.label}`;
    }

    const changes = snapshotDiffSummary(snapshot);

    if (snapshot.tag || snapshot.reason || snapshot.lastRestoredAt) {
      const meta = document.createElement("div");
      meta.className = "gate-snapshot-diff-item is-detail";

      const metaLabel = document.createElement("strong");
      metaLabel.textContent = "SNAPSHOT · META";

      const metaDetail = document.createElement("span");
      const restored = snapshot.lastRestoredAt
        ? `; last restored ${snapshot.lastRestoredAt}`
        : "";

      metaDetail.textContent =
        `${snapshot.tag ? `tag ${snapshot.tag}` : "untagged"}` +
        `${snapshot.reason ? `; reason ${snapshot.reason}` : ""}` +
        restored;

      meta.append(metaLabel, metaDetail);
      snapshotDiffList.appendChild(meta);
    }

    if (!changes.length) {
      const empty = document.createElement("div");
      empty.className = "gate-snapshot-diff-empty";
      empty.textContent = "NO CONFIGURATION DIFFERENCE";
      snapshotDiffList.appendChild(empty);
    } else {
      changes.forEach((change) => {
        const row = document.createElement("div");
        row.className = "gate-snapshot-diff-item";
        row.classList.toggle("is-detail", change.isDetail === true);

        const label = document.createElement("strong");
        label.textContent = change.label;

        const detail = document.createElement("span");
        detail.textContent = change.detail;

        row.append(label, detail);
        snapshotDiffList.appendChild(row);
      });
    }

    snapshotDiffPanel.hidden = false;

    if (snapshotDiffRestoreButton) {
      snapshotDiffRestoreButton.disabled = false;
    }

    snapshotDiffPanel.scrollIntoView({
      block: "nearest",
      behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth",
    });
  }

  function restoreConfigSnapshot(id) {
    const snapshot = readSnapshots().find((item) => item.id === id);

    if (!snapshot) {
      setSettingsStatus("SNAPSHOT NOT FOUND");
      return;
    }

    if (!window.confirm(`Restore Gate snapshot "${snapshot.label}"?`)) {
      return;
    }

    const restored = normalizePreferences(snapshot.preferences);
    writeJson(settingsKey, restored);

    const vector = normalizeImportedVector(snapshot.currentVector);

    if (vector) {
      writeJson(vectorKey, vector);
    } else {
      storage.remove(vectorKey);
    }

    const restoredAt = new Date().toISOString();
    writeSnapshots(
      readSnapshots().map((item) =>
        item.id === id
          ? { ...item, lastRestoredAt: restoredAt }
          : item
      )
    );

    window.location.reload();
  }

  function deleteConfigSnapshot(id) {
    writeSnapshots(readSnapshots().filter((item) => item.id !== id));

    if (snapshotDiffTargetId === id) {
      closeSnapshotDiff();
    }

    renderSnapshotList();
    setSettingsStatus("CONFIG SNAPSHOT DELETED");
  }

  function renderSnapshotList() {
    if (!snapshotList) {
      return;
    }

    const snapshots = readSnapshots();
    snapshotList.replaceChildren();

    if (!snapshots.length) {
      const empty = document.createElement("div");
      empty.className = "gate-snapshot-empty";
      empty.textContent = "NO LOCAL SNAPSHOTS";
      snapshotList.appendChild(empty);
      closeSnapshotDiff();
      return;
    }

    snapshots.forEach((snapshot) => {
      const row = document.createElement("div");
      row.className = "gate-snapshot-row";

      const text = document.createElement("span");
      const strong = document.createElement("strong");
      strong.textContent = snapshot.label;

      const small = document.createElement("small");
      const date = new Date(snapshot.createdAt);
      small.textContent = Number.isNaN(date.getTime())
        ? "LOCAL CONFIGURATION"
        : new Intl.DateTimeFormat("en-GB", {
            day: "2-digit",
            month: "short",
            year: "numeric",
            hour: "2-digit",
            minute: "2-digit",
            hour12: false,
          }).format(date).toUpperCase();

      text.append(strong, small);

      const meta = document.createElement("span");
      meta.className = "gate-snapshot-meta";

      if (snapshot.tag) {
        const tag = document.createElement("span");
        tag.className = "gate-snapshot-tag";
        tag.textContent = snapshot.tag.toUpperCase();
        meta.appendChild(tag);
      }

      if (snapshot.reason) {
        const reason = document.createElement("span");
        reason.className = "gate-snapshot-reason";
        reason.textContent = snapshot.reason;
        meta.appendChild(reason);
      }

      if (snapshot.lastRestoredAt) {
        const restoredDate = new Date(snapshot.lastRestoredAt);
        const restored = document.createElement("span");
        restored.className = "gate-snapshot-restored";
        restored.textContent = Number.isNaN(restoredDate.getTime())
          ? "RESTORED"
          : `RESTORED ${new Intl.DateTimeFormat("en-GB", {
              day: "2-digit",
              month: "short",
              hour: "2-digit",
              minute: "2-digit",
              hour12: false,
            }).format(restoredDate).toUpperCase()}`;
        meta.appendChild(restored);
      }

      if (meta.childNodes.length) {
        text.appendChild(meta);
      }

      const controls = document.createElement("span");
      controls.className = "gate-snapshot-controls";

      const rename = document.createElement("button");
      rename.type = "button";
      rename.className = "gate-snapshot-rename";
      rename.textContent = "RENAME";
      rename.addEventListener("click", () => renameConfigSnapshot(snapshot.id));

      const diff = document.createElement("button");
      diff.type = "button";
      diff.className = "gate-snapshot-diff-button";
      diff.textContent = "DIFF";
      diff.addEventListener("click", () => showSnapshotDiff(snapshot.id));

      const restore = document.createElement("button");
      restore.type = "button";
      restore.textContent = "RESTORE";
      restore.addEventListener("click", () => showSnapshotDiff(snapshot.id));

      const remove = document.createElement("button");
      remove.type = "button";
      remove.textContent = "DELETE";
      remove.addEventListener("click", () => deleteConfigSnapshot(snapshot.id));

      controls.append(rename, diff, restore, remove);
      row.append(text, controls);
      snapshotList.appendChild(row);
    });

    if (snapshotDiffTargetId) {
      const exists = snapshots.some((snapshot) => snapshot.id === snapshotDiffTargetId);

      if (exists) {
        showSnapshotDiff(snapshotDiffTargetId);
      } else {
        closeSnapshotDiff();
      }
    }
  }

  function makeLocalId(prefix, label) {
    const slug = cleanText(label, 32)
      .toLowerCase()
      .normalize("NFKD")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, 24) || "node";

    return `${prefix}-${slug}-${Date.now().toString(36)}${Math.random().toString(36).slice(2, 5)}`;
  }

  let editingCustomLaunchId = null;
  let editingCustomGroupId = null;

  function resetCustomLaunchEditor() {
    editingCustomLaunchId = null;

    if (customLaunchLabel) customLaunchLabel.value = "";
    if (customLaunchRole) customLaunchRole.value = "";
    if (customLaunchUrl) customLaunchUrl.value = "";

    if (addCustomLaunchButton) addCustomLaunchButton.textContent = "ADD QUICK LAUNCH";
    if (cancelCustomLaunchButton) cancelCustomLaunchButton.hidden = true;
  }

  function beginEditCustomLaunch(id) {
    const item = preferences.customLaunches.find((entry) => entry.id === id);

    if (!item) {
      return;
    }

    editingCustomLaunchId = id;

    if (customLaunchLabel) customLaunchLabel.value = item.label;
    if (customLaunchRole) customLaunchRole.value = item.role;
    if (customLaunchUrl) customLaunchUrl.value = item.url;

    if (addCustomLaunchButton) addCustomLaunchButton.textContent = "SAVE QUICK LAUNCH";
    if (cancelCustomLaunchButton) cancelCustomLaunchButton.hidden = false;

    customLaunchLabel?.focus();
  }

  function addCustomLaunch() {
    const label = cleanText(customLaunchLabel?.value, 40);
    const role = cleanText(customLaunchRole?.value, 40) || "CUSTOM";
    const url = cleanText(customLaunchUrl?.value, 500);

    if (!label || !isSafeRouteUrl(url)) {
      setSettingsStatus("INVALID CUSTOM LAUNCH");
      return;
    }

    if (editingCustomLaunchId) {
      const exists = preferences.customLaunches.some(
        (item) => item.id === editingCustomLaunchId
      );

      if (!exists) {
        resetCustomLaunchEditor();
        setSettingsStatus("CUSTOM LAUNCH NOT FOUND");
        return;
      }

      savePreferences({
        ...preferences,
        customLaunches: preferences.customLaunches.map((item) =>
          item.id === editingCustomLaunchId
            ? { ...item, label, role, url }
            : item
        ),
      });

      resetCustomLaunchEditor();
      setSettingsStatus("CUSTOM LAUNCH UPDATED");
      return;
    }

    if (preferences.customLaunches.length >= customLaunchLimit) {
      setSettingsStatus("CUSTOM LAUNCH LIMIT REACHED");
      return;
    }

    const item = {
      id: makeLocalId("custom-launch", label),
      label,
      role,
      url,
    };

    savePreferences({
      ...preferences,
      customLaunches: [...preferences.customLaunches, item],
      launchOrder: [...preferences.launchOrder, item.id],
    });

    resetCustomLaunchEditor();
    setSettingsStatus("CUSTOM LAUNCH ADDED");
  }

  function syncRouteGroupSelects(preferredEditId = routeEditGroup?.value) {
    const groups = allRouteGroups();

    [settingRouteGroup, routeEditGroup, queryPresetGroup, contextLaunchGroup].forEach((select) => {
      if (!select) return;

      const desired =
        select === settingRouteGroup
          ? preferences.activeRouteGroup
          : select === queryPresetGroup
            ? (queryPresetGroup?.value || preferences.activeRouteGroup)
            : select === contextLaunchGroup
              ? (contextLaunchGroup?.value || preferences.activeRouteGroup)
              : preferredEditId;

      select.replaceChildren();

      groups.forEach((group) => {
        const option = document.createElement("option");
        option.value = group.id;
        option.textContent = `${group.label} · ${group.detail || "ROUTES"}`;
        select.appendChild(option);
      });

      select.value = groups.some((group) => group.id === desired)
        ? desired
        : (groups[0]?.id || "");
    });
  }

  function renderQueryPresetEditor(groupId = queryPresetGroup?.value || preferences.activeRouteGroup) {
    if (!queryPresetEngine || !queryPresetPlaceholder || !routeGroupIds.includes(groupId)) {
      return;
    }

    const preset = preferences.queryPresets?.[groupId] || {};
    queryPresetEngine.value = engines[preset.engine] ? preset.engine : "";
    queryPresetPlaceholder.value = preset.placeholder || "";
  }

  function saveQueryPreset() {
    const groupId = queryPresetGroup?.value;

    if (!routeGroupIds.includes(groupId)) {
      return;
    }

    const engine = engines[queryPresetEngine?.value]
      ? queryPresetEngine.value
      : "";

    const placeholder = cleanText(queryPresetPlaceholder?.value, 80);

    const nextPresets = {
      ...preferences.queryPresets,
    };

    if (!engine && !placeholder) {
      delete nextPresets[groupId];
    } else {
      nextPresets[groupId] = {
        engine,
        placeholder,
      };
    }

    savePreferences({
      ...preferences,
      queryPresets: nextPresets,
    });

    renderQueryPresetEditor(groupId);
    setSettingsStatus("QUERY PRESET UPDATED");
  }

  function resetQueryPreset() {
    const groupId = queryPresetGroup?.value;

    if (!routeGroupIds.includes(groupId)) {
      return;
    }

    const nextPresets = {
      ...preferences.queryPresets,
    };

    delete nextPresets[groupId];

    savePreferences({
      ...preferences,
      queryPresets: nextPresets,
    });

    renderQueryPresetEditor(groupId);
    setSettingsStatus("QUERY PRESET RESET");
  }

  function renderContextLaunchSettings(
    groupId = contextLaunchGroup?.value || preferences.activeRouteGroup
  ) {
    if (!contextLaunchList || !routeGroupIds.includes(groupId)) {
      return;
    }

    contextLaunchList.replaceChildren();

    const globalHidden = new Set(preferences.hiddenLaunches);
    const contextHidden = new Set(preferences.contextLaunchHidden?.[groupId] || []);

    const nodesById = new Map(
      qsa("[data-gate-launch]").map((node) => [
        node.dataset.gateLaunchId || node.dataset.gateCommand,
        node,
      ])
    );

    preferences.launchOrder.forEach((id) => {
      const node = nodesById.get(id);

      if (!node) {
        return;
      }

      const row = document.createElement("label");
      row.className = "gate-context-launch-row";

      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.checked = !contextHidden.has(id);
      checkbox.disabled = globalHidden.has(id);
      checkbox.setAttribute(
        "aria-label",
        `${groupId} 显示 ${node.dataset.gateLabel || id}`
      );

      checkbox.addEventListener("change", () => {
        const nextHidden = new Set(preferences.contextLaunchHidden?.[groupId] || []);

        if (checkbox.checked) {
          nextHidden.delete(id);
        } else {
          nextHidden.add(id);
        }

        const nextContext = {
          ...preferences.contextLaunchHidden,
        };

        if (nextHidden.size) {
          nextContext[groupId] = [...nextHidden];
        } else {
          delete nextContext[groupId];
        }

        savePreferences({
          ...preferences,
          contextLaunchHidden: nextContext,
        });

        if (contextLaunchGroup) {
          contextLaunchGroup.value = groupId;
        }

        renderContextLaunchSettings(groupId);
        setSettingsStatus("CONTEXT LAUNCHES UPDATED");
      });

      const text = document.createElement("span");
      const strong = document.createElement("strong");
      strong.textContent = (node.dataset.gateLabel || id).toUpperCase();

      const small = document.createElement("small");
      small.textContent = node.querySelector("small")?.textContent || "LAUNCH ROUTE";

      text.append(strong, small);

      const state = document.createElement("span");

      if (globalHidden.has(id)) {
        state.className = "is-global-hidden";
        state.textContent = "GLOBAL HIDDEN";
      } else {
        state.textContent = contextHidden.has(id) ? "CONTEXT HIDDEN" : "VISIBLE";
      }

      row.append(checkbox, text, state);
      contextLaunchList.appendChild(row);
    });
  }

  function resetContextLaunchSettings() {
    const groupId = contextLaunchGroup?.value;

    if (!routeGroupIds.includes(groupId)) {
      return;
    }

    const nextContext = {
      ...preferences.contextLaunchHidden,
    };

    delete nextContext[groupId];

    savePreferences({
      ...preferences,
      contextLaunchHidden: nextContext,
    });

    if (contextLaunchGroup) {
      contextLaunchGroup.value = groupId;
    }

    renderContextLaunchSettings(groupId);
    setSettingsStatus("CONTEXT LAUNCHES RESET");
  }

  function renderRouteGroupOrderSettings() {
    if (!routeOrderList) {
      return;
    }

    routeOrderList.replaceChildren();

    const groupsById = new Map(
      allRouteGroups().map((group) => [group.id, group])
    );

    preferences.routeGroupOrder.forEach((id, index) => {
      const group = groupsById.get(id);

      if (!group) {
        return;
      }

      const row = document.createElement("div");
      row.className = "gate-route-order-row";

      const code = document.createElement("span");
      code.className = "gate-route-order-code";
      code.textContent = String(index + 1).padStart(2, "0");

      const text = document.createElement("span");
      const strong = document.createElement("strong");
      strong.textContent = group.label;

      const small = document.createElement("small");
      small.textContent =
        group.id === preferences.pinnedRouteGroup
          ? `${group.detail || "ROUTES"} · PINNED FIRST`
          : (group.detail || "ROUTES");

      text.append(strong, small);

      const controls = document.createElement("span");
      controls.className = "gate-route-order-controls";

      const up = document.createElement("button");
      up.type = "button";
      up.textContent = "↑";
      up.disabled = index === 0;
      up.setAttribute("aria-label", `上移 ${group.label}`);

      const down = document.createElement("button");
      down.type = "button";
      down.textContent = "↓";
      down.disabled = index === preferences.routeGroupOrder.length - 1;
      down.setAttribute("aria-label", `下移 ${group.label}`);

      const pin = document.createElement("button");
      pin.type = "button";
      pin.textContent = group.id === preferences.pinnedRouteGroup ? "PINNED" : "PIN";
      pin.classList.toggle("is-pinned", group.id === preferences.pinnedRouteGroup);
      pin.setAttribute("aria-label", `置顶 ${group.label}`);

      up.addEventListener("click", () => {
        if (index <= 0) return;

        const order = [...preferences.routeGroupOrder];
        [order[index - 1], order[index]] = [order[index], order[index - 1]];

        savePreferences({
          ...preferences,
          routeGroupOrder: order,
        });

        setSettingsStatus("ROUTE GROUP ORDER UPDATED");
      });

      down.addEventListener("click", () => {
        if (index >= preferences.routeGroupOrder.length - 1) return;

        const order = [...preferences.routeGroupOrder];
        [order[index + 1], order[index]] = [order[index], order[index + 1]];

        savePreferences({
          ...preferences,
          routeGroupOrder: order,
        });

        setSettingsStatus("ROUTE GROUP ORDER UPDATED");
      });

      pin.addEventListener("click", () => {
        savePreferences({
          ...preferences,
          pinnedRouteGroup:
            preferences.pinnedRouteGroup === group.id ? "" : group.id,
        });

        setSettingsStatus(
          preferences.pinnedRouteGroup === group.id
            ? "ROUTE GROUP PINNED"
            : "ROUTE GROUP UNPINNED"
        );
      });

      controls.append(up, down, pin);
      row.append(code, text, controls);
      routeOrderList.appendChild(row);
    });
  }

  function renderCustomGroupList() {
    if (!customGroupList) {
      return;
    }

    customGroupList.replaceChildren();

    preferences.customRouteGroups.forEach((group) => {
      const row = document.createElement("div");
      row.className = "gate-custom-group-row";

      const text = document.createElement("span");
      const strong = document.createElement("strong");
      strong.textContent = group.label;
      const small = document.createElement("small");
      small.textContent = group.detail;
      text.append(strong, small);

      const controls = document.createElement("span");
      controls.className = "gate-custom-group-controls";

      const edit = document.createElement("button");
      edit.type = "button";
      edit.textContent = "EDIT";
      edit.addEventListener("click", () => beginEditCustomRouteGroup(group.id));

      const remove = document.createElement("button");
      remove.type = "button";
      remove.textContent = "DELETE";

      remove.addEventListener("click", () => {
        savePreferences({
          ...preferences,
          customRouteGroups: preferences.customRouteGroups.filter((item) => item.id !== group.id),
          activeRouteGroup: preferences.activeRouteGroup === group.id
            ? preferenceDefaults.activeRouteGroup
            : preferences.activeRouteGroup,
        });

        if (editingCustomGroupId === group.id) {
          resetCustomGroupEditor();
        }

        setSettingsStatus("CUSTOM GROUP REMOVED");
      });

      controls.append(edit, remove);
      row.append(text, controls);
      customGroupList.appendChild(row);
    });
  }

  function resetCustomGroupEditor() {
    editingCustomGroupId = null;

    if (customGroupLabel) customGroupLabel.value = "";
    if (customGroupDetail) customGroupDetail.value = "";

    if (addCustomGroupButton) addCustomGroupButton.textContent = "ADD ROUTE GROUP";
    if (cancelCustomGroupButton) cancelCustomGroupButton.hidden = true;
  }

  function beginEditCustomRouteGroup(id) {
    const group = preferences.customRouteGroups.find((item) => item.id === id);

    if (!group) {
      return;
    }

    editingCustomGroupId = id;

    if (customGroupLabel) customGroupLabel.value = group.label;
    if (customGroupDetail) customGroupDetail.value = group.detail;

    if (addCustomGroupButton) addCustomGroupButton.textContent = "SAVE GROUP NAME";
    if (cancelCustomGroupButton) cancelCustomGroupButton.hidden = false;

    customGroupLabel?.focus();
  }

  function addCustomRouteGroup() {
    const label = cleanText(customGroupLabel?.value, 24);
    const detail = cleanText(customGroupDetail?.value, 40) || "CUSTOM ROUTES";

    if (!label) {
      setSettingsStatus("GROUP LABEL REQUIRED");
      return;
    }

    if (editingCustomGroupId) {
      const exists = preferences.customRouteGroups.some(
        (group) => group.id === editingCustomGroupId
      );

      if (!exists) {
        resetCustomGroupEditor();
        setSettingsStatus("CUSTOM GROUP NOT FOUND");
        return;
      }

      savePreferences({
        ...preferences,
        customRouteGroups: preferences.customRouteGroups.map((group) =>
          group.id === editingCustomGroupId
            ? { ...group, label, detail }
            : group
        ),
      });

      const editedId = editingCustomGroupId;
      resetCustomGroupEditor();
      syncRouteGroupSelects(editedId);

      if (routeEditGroup) routeEditGroup.value = editedId;
      renderRouteEditor(editedId);

      setSettingsStatus("CUSTOM GROUP RENAMED");
      return;
    }

    if (preferences.customRouteGroups.length >= customRouteGroupLimit) {
      setSettingsStatus("CUSTOM GROUP LIMIT REACHED");
      return;
    }

    const group = {
      id: makeLocalId("custom-group", label),
      label,
      detail,
      routes: Array.from({ length: routesPerGroup }, () => ({
        label: "",
        detail: "",
        url: "",
      })),
    };

    savePreferences({
      ...preferences,
      customRouteGroups: [...preferences.customRouteGroups, group],
      activeRouteGroup: group.id,
    });

    resetCustomGroupEditor();
    syncRouteGroupSelects(group.id);

    if (routeEditGroup) routeEditGroup.value = group.id;
    renderRouteEditor(group.id);

    setSettingsStatus("CUSTOM GROUP ADDED");
  }

  function renderRouteEditor(groupId = routeEditGroup?.value || preferences.activeRouteGroup) {
    if (!routeEditorList || !routeGroupIds.includes(groupId)) {
      return;
    }

    routeEditorList.replaceChildren();

    for (let slotIndex = 0; slotIndex < 4; slotIndex += 1) {
      const route = resolvedRouteSlot(groupId, slotIndex);
      const row = document.createElement("div");
      row.className = "gate-route-edit-row";
      row.dataset.routeSlot = String(slotIndex);

      const code = document.createElement("span");
      code.className = "gate-route-edit-code";
      code.textContent = String(slotIndex + 1).padStart(2, "0");

      const fields = document.createElement("div");
      fields.className = "gate-route-edit-fields";

      const makeField = (name, value, maxlength = 80) => {
        const label = document.createElement("label");
        const caption = document.createElement("span");
        caption.textContent = name.toUpperCase();

        const input = document.createElement("input");
        input.type = "text";
        input.maxLength = maxlength;
        input.value = value;
        input.dataset.routeField = name;

        label.append(caption, input);
        return label;
      };

      fields.append(
        makeField("label", route.label, 60),
        makeField("detail", route.detail, 60),
        makeField("url", route.url, 500)
      );

      row.append(code, fields);
      routeEditorList.appendChild(row);
    }
  }

  function collectRouteEditor(groupId) {
    if (!routeEditorList || !routeGroupIds.includes(groupId)) {
      return null;
    }

    const rows = [...routeEditorList.querySelectorAll("[data-route-slot]")];

    return rows.map((row) => {
      const value = (field) =>
        row.querySelector(`[data-route-field="${field}"]`)?.value.trim() || "";

      return {
        label: value("label"),
        detail: value("detail"),
        url: value("url"),
      };
    });
  }

  function saveRouteEditorGroup() {
    const groupId = routeEditGroup?.value;

    if (!routeGroupIds.includes(groupId)) {
      return;
    }

    const routes = collectRouteEditor(groupId);

    if (!routes) {
      return;
    }

    const invalid = routes.find((route) => route.url && !isSafeRouteUrl(route.url));

    if (invalid) {
      setSettingsStatus("INVALID ROUTE URL");
      return;
    }

    if (isCustomRouteGroup(groupId)) {
      savePreferences({
        ...preferences,
        customRouteGroups: preferences.customRouteGroups.map((group) =>
          group.id === groupId ? { ...group, routes } : group
        ),
      });
    } else {
      savePreferences({
        ...preferences,
        routeOverrides: {
          ...preferences.routeOverrides,
          [groupId]: routes,
        },
      });
    }

    syncRouteGroupSelects(groupId);
    if (routeEditGroup) routeEditGroup.value = groupId;
    renderRouteEditor(groupId);
    renderSuggestions();

    setSettingsStatus("ROUTE GROUP SAVED");
  }

  function resetRouteEditorGroup() {
    const groupId = routeEditGroup?.value;

    if (!routeGroupIds.includes(groupId)) {
      return;
    }

    if (isCustomRouteGroup(groupId)) {
      savePreferences({
        ...preferences,
        customRouteGroups: preferences.customRouteGroups.map((group) =>
          group.id === groupId
            ? {
                ...group,
                routes: Array.from({ length: routesPerGroup }, () => ({
                  label: "",
                  detail: "",
                  url: "",
                })),
              }
            : group
        ),
      });
    } else {
      const nextOverrides = { ...preferences.routeOverrides };
      delete nextOverrides[groupId];

      savePreferences({
        ...preferences,
        routeOverrides: nextOverrides,
      });
    }

    syncRouteGroupSelects(groupId);
    if (routeEditGroup) routeEditGroup.value = groupId;
    renderRouteEditor(groupId);
    renderSuggestions();

    setSettingsStatus("ROUTE GROUP RESET");
  }

  function syncSettingsControls() {
    if (settingSearch) {
      settingSearch.value = engines[preferences.defaultSearch]
        ? preferences.defaultSearch
        : preferenceDefaults.defaultSearch;
    }

    if (settingDensity) settingDensity.value = preferences.density;
    if (settingPresentation) settingPresentation.value = preferences.presentation;
    if (settingAmbient) settingAmbient.checked = preferences.ambient;
    if (settingRouteShortcuts) settingRouteShortcuts.checked = preferences.routeShortcuts;

    syncRouteGroupSelects();

    if (customLaunchCount) {
      customLaunchCount.textContent = `${preferences.customLaunches.length} / ${customLaunchLimit}`;
    }

    if (customGroupCount) {
      customGroupCount.textContent = `${preferences.customRouteGroups.length} / ${customRouteGroupLimit}`;
    }

    renderCustomGroupList();
    renderQueryPresetEditor();
    renderContextLaunchSettings();
    renderRouteGroupOrderSettings();

    settingModuleInputs.forEach((input) => {
      input.checked = moduleEnabled(input.dataset.gateSettingModule);
    });

    renderLaunchSettings();
    renderDashboardSettings();
    renderRouteEditor();
    renderSnapshotList();
    filterSettingsSections();
  }

  function closeSettings({ restoreFocus = true } = {}) {
    if (!settingsDrawer || !settingsBackdrop || settingsDrawer.hidden) return;

    window.clearTimeout(settingsCloseTimer);
    settingsDrawer.classList.remove("is-open");
    settingsBackdrop.classList.remove("is-open");
    document.body.classList.remove("gate-settings-open");

    settingsCloseTimer = window.setTimeout(() => {
      settingsDrawer.hidden = true;
      settingsBackdrop.hidden = true;

      if (restoreFocus) settingsReturnFocus?.focus?.();
    }, 205);
  }

  // Replace the earlier declaration body with the fully-featured drawer opener.
  openSettings = function openSettingsDrawer() {
    if (!settingsDrawer || !settingsBackdrop) return;

    window.clearTimeout(settingsCloseTimer);
    settingsReturnFocus = document.activeElement;
    syncSettingsControls();
    renderDiagnostics();

    settingsDrawer.hidden = false;
    settingsBackdrop.hidden = false;
    document.body.classList.add("gate-settings-open");

    window.requestAnimationFrame(() => {
      settingsDrawer.classList.add("is-open");
      settingsBackdrop.classList.add("is-open");
      settingsCloseButton?.focus();
    });
  };

  settingsOpenButton?.addEventListener("click", openSettings);
  settingsCloseButton?.addEventListener("click", () => closeSettings());
  settingsBackdrop?.addEventListener("click", () => closeSettings());

  settingsFilterInput?.addEventListener("input", () => {
    filterSettingsSections(settingsFilterInput.value);
  });

  settingsJumpSelect?.addEventListener("change", () => {
    const targetId = settingsJumpSelect.value;

    if (!targetId) {
      return;
    }

    if (settingsFilterInput) {
      settingsFilterInput.value = "";
      filterSettingsSections("");
    }

    const heading = document.getElementById(targetId);
    const section = heading?.closest(".gate-settings-section");

    section?.scrollIntoView({
      block: "start",
      behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches
        ? "auto"
        : "smooth",
    });

    window.setTimeout(() => {
      settingsJumpSelect.value = "";
    }, 180);
  });

  createSnapshotButton?.addEventListener("click", () => {
    createConfigSnapshot();
  });

  copyContextProfileButton?.addEventListener("click", copyContextProfile);
  exportContextProfileButton?.addEventListener("click", exportContextProfile);

  snapshotDiffCloseButton?.addEventListener("click", closeSnapshotDiff);

  snapshotDiffRestoreButton?.addEventListener("click", () => {
    if (snapshotDiffTargetId) {
      restoreConfigSnapshot(snapshotDiffTargetId);
    }
  });

  settingSearch?.addEventListener("change", () => {
    savePreferences({
      ...preferences,
      defaultSearch: settingSearch.value,
    });
    setSettingsStatus("DEFAULT SEARCH UPDATED");
  });

  settingDensity?.addEventListener("change", () => {
    savePreferences({
      ...preferences,
      density: settingDensity.value,
    });
    setSettingsStatus("DENSITY UPDATED");
  });

  settingPresentation?.addEventListener("change", () => {
    savePreferences({
      ...preferences,
      presentation: settingPresentation.value,
    });
    setSettingsStatus("PRESENTATION UPDATED");
  });

  settingAmbient?.addEventListener("change", () => {
    savePreferences({
      ...preferences,
      ambient: settingAmbient.checked,
    });
    setSettingsStatus("AMBIENT GRAPHICS UPDATED");
  });

  settingRouteShortcuts?.addEventListener("change", () => {
    savePreferences({
      ...preferences,
      routeShortcuts: settingRouteShortcuts.checked,
    });
    setSettingsStatus("ROUTE SHORTCUTS UPDATED");
  });

  settingRouteGroup?.addEventListener("change", () => {
    savePreferences({
      ...preferences,
      activeRouteGroup: settingRouteGroup.value,
    });

    setSettingsStatus("DEFAULT ROUTE GROUP UPDATED");
  });

  routeEditGroup?.addEventListener("change", () => {
    renderRouteEditor(routeEditGroup.value);
  });

  routeSaveGroupButton?.addEventListener("click", saveRouteEditorGroup);
  routeResetGroupButton?.addEventListener("click", resetRouteEditorGroup);

  addCustomLaunchButton?.addEventListener("click", addCustomLaunch);
  addCustomGroupButton?.addEventListener("click", addCustomRouteGroup);

  cancelCustomLaunchButton?.addEventListener("click", resetCustomLaunchEditor);
  cancelCustomGroupButton?.addEventListener("click", resetCustomGroupEditor);

  queryPresetGroup?.addEventListener("change", () => {
    renderQueryPresetEditor(queryPresetGroup.value);
  });

  saveQueryPresetButton?.addEventListener("click", saveQueryPreset);
  resetQueryPresetButton?.addEventListener("click", resetQueryPreset);

  contextLaunchGroup?.addEventListener("change", () => {
    renderContextLaunchSettings(contextLaunchGroup.value);
  });

  resetContextLaunchesButton?.addEventListener("click", resetContextLaunchSettings);

  unpinRouteGroupButton?.addEventListener("click", () => {
    if (!preferences.pinnedRouteGroup) {
      setSettingsStatus("NO PINNED ROUTE GROUP");
      return;
    }

    savePreferences({
      ...preferences,
      pinnedRouteGroup: "",
    });

    setSettingsStatus("ROUTE GROUP UNPINNED");
  });

  settingModuleInputs.forEach((input) => {
    input.addEventListener("change", () => {
      const name = input.dataset.gateSettingModule;

      savePreferences({
        ...preferences,
        modules: {
          ...preferences.modules,
          [name]: input.checked,
        },
      });

      if (name === "local_conditions" && input.checked) {
        syncWeatherPreference();
      }

      renderSuggestions();
      setSettingsStatus("MODULE STATE UPDATED");
    });
  });

  clearRecentButton?.addEventListener("click", () => {
    clearRecentTransits();
    renderSuggestions();
    setSettingsStatus("RECENT TRANSITS CLEARED");
  });

  clearWeatherButton?.addEventListener("click", () => {
    clearWeather();
    setSettingsStatus("WEATHER DATA CLEARED");
  });

  resetVectorButton?.addEventListener("click", () => {
    resetVector();
    setSettingsStatus("VECTOR RESET");
  });

  clearNoteButton?.addEventListener("click", () => {
    if (window.confirm("Clear the local Field Record in this browser?")) {
      clearNote();
      setSettingsStatus("FIELD RECORD CLEARED");
    }
  });

  function diagnosePreferences(raw) {
    const issues = [];

    if (!raw || typeof raw !== "object" || Array.isArray(raw)) {
      return {
        issues: ["Settings payload is not an object."],
        repaired: normalizePreferences({}),
      };
    }

    if (
      Object.prototype.hasOwnProperty.call(raw, "routeShortcuts") &&
      typeof raw.routeShortcuts !== "boolean"
    ) {
      issues.push("Route shortcut preference is malformed.");
    }

    const rawCustomLaunches = Array.isArray(raw.customLaunches) ? raw.customLaunches : [];

    if (rawCustomLaunches.length > customLaunchLimit) {
      issues.push(`Custom Quick Launch count exceeds ${customLaunchLimit}.`);
    }

    const launchIds = new Set();

    rawCustomLaunches.forEach((item, index) => {
      if (!/^custom-launch-[a-z0-9-]+$/i.test(item?.id || "")) {
        issues.push(`Custom Quick Launch ${index + 1} has an invalid ID.`);
      }

      if (launchIds.has(item?.id)) {
        issues.push(`Duplicate Custom Quick Launch ID: ${item.id}.`);
      }

      launchIds.add(item?.id);

      if (!cleanText(item?.label, 40)) {
        issues.push(`Custom Quick Launch ${index + 1} has no label.`);
      }

      if (!isSafeRouteUrl(item?.url || "")) {
        issues.push(`Custom Quick Launch ${index + 1} has an invalid URL.`);
      }
    });

    const rawGroups = Array.isArray(raw.customRouteGroups) ? raw.customRouteGroups : [];

    if (rawGroups.length > customRouteGroupLimit) {
      issues.push(`Custom Route Group count exceeds ${customRouteGroupLimit}.`);
    }

    const groupIds = new Set(defaultRouteGroupIds);

    rawGroups.forEach((group, groupIndex) => {
      if (!/^custom-group-[a-z0-9-]+$/i.test(group?.id || "")) {
        issues.push(`Custom Route Group ${groupIndex + 1} has an invalid ID.`);
      }

      if (groupIds.has(group?.id)) {
        issues.push(`Duplicate Route Group ID: ${group.id}.`);
      }

      groupIds.add(group?.id);

      if (!cleanText(group?.label, 24)) {
        issues.push(`Custom Route Group ${groupIndex + 1} has no label.`);
      }

      const routes = Array.isArray(group?.routes) ? group.routes : [];

      routes.slice(0, routesPerGroup).forEach((route, routeIndex) => {
        if (route?.url && !isSafeRouteUrl(route.url)) {
          issues.push(
            `${cleanText(group?.label, 24) || `Group ${groupIndex + 1}`} route ${routeIndex + 1} has an invalid URL.`
          );
        }
      });
    });

    const validLaunchIds = [
      ...defaultLaunchOrder,
      ...normalizeCustomLaunches(rawCustomLaunches).map((item) => item.id),
    ];

    const rawLaunchOrder = Array.isArray(raw.launchOrder) ? raw.launchOrder : [];

    if (new Set(rawLaunchOrder).size !== rawLaunchOrder.length) {
      issues.push("Launch order contains duplicate IDs.");
    }

    rawLaunchOrder.forEach((id) => {
      if (!validLaunchIds.includes(id)) {
        issues.push(`Launch order contains unknown ID: ${id}.`);
      }
    });

    const validGroupIds = [
      ...defaultRouteGroupIds,
      ...normalizeCustomRouteGroups(rawGroups).map((group) => group.id),
    ];

    if (raw.activeRouteGroup && !validGroupIds.includes(raw.activeRouteGroup)) {
      issues.push(`Active Route Group is unavailable: ${raw.activeRouteGroup}.`);
    }

    const rawRouteGroupOrder = Array.isArray(raw.routeGroupOrder)
      ? raw.routeGroupOrder
      : [];

    if (new Set(rawRouteGroupOrder).size !== rawRouteGroupOrder.length) {
      issues.push("Route Group order contains duplicate IDs.");
    }

    rawRouteGroupOrder.forEach((id) => {
      if (!validGroupIds.includes(id)) {
        issues.push(`Route Group order contains unknown ID: ${id}.`);
      }
    });

    if (raw.pinnedRouteGroup && !validGroupIds.includes(raw.pinnedRouteGroup)) {
      issues.push(`Pinned Route Group is unavailable: ${raw.pinnedRouteGroup}.`);
    }

    const rawContextLaunchHidden =
      raw.contextLaunchHidden &&
      typeof raw.contextLaunchHidden === "object" &&
      !Array.isArray(raw.contextLaunchHidden)
        ? raw.contextLaunchHidden
        : {};

    Object.entries(rawContextLaunchHidden).forEach(([groupId, hiddenIds]) => {
      if (!validGroupIds.includes(groupId)) {
        issues.push(`Context Launch rules reference unknown Route Group: ${groupId}.`);
        return;
      }

      if (!Array.isArray(hiddenIds)) {
        issues.push(`Context Launch rules for ${groupId} are malformed.`);
        return;
      }

      if (new Set(hiddenIds).size !== hiddenIds.length) {
        issues.push(`Context Launch rules for ${groupId} contain duplicate Launch IDs.`);
      }

      hiddenIds.forEach((id) => {
        if (!validLaunchIds.includes(id)) {
          issues.push(`Context Launch rules for ${groupId} contain unknown Launch ID: ${id}.`);
        }
      });
    });

    const rawDashboardOrder = Array.isArray(raw.dashboardOrder) ? raw.dashboardOrder : [];

    if (new Set(rawDashboardOrder).size !== rawDashboardOrder.length) {
      issues.push("Dashboard order contains duplicate IDs.");
    }

    rawDashboardOrder.forEach((id) => {
      if (!defaultDashboardOrder.includes(id)) {
        issues.push(`Dashboard order contains unknown ID: ${id}.`);
      }
    });

    const rawQueryPresets =
      raw.queryPresets && typeof raw.queryPresets === "object" && !Array.isArray(raw.queryPresets)
        ? raw.queryPresets
        : {};

    Object.entries(rawQueryPresets).forEach(([groupId, preset]) => {
      if (!validGroupIds.includes(groupId)) {
        issues.push(`Query preset references unknown Route Group: ${groupId}.`);
        return;
      }

      if (!preset || typeof preset !== "object" || Array.isArray(preset)) {
        issues.push(`Query preset for ${groupId} is malformed.`);
        return;
      }

      if (preset.engine && !engines[preset.engine]) {
        issues.push(`Query preset for ${groupId} uses unknown engine: ${preset.engine}.`);
      }

      if (
        typeof preset.placeholder === "string" &&
        preset.placeholder.length > 80
      ) {
        issues.push(`Query preset placeholder for ${groupId} exceeds 80 characters.`);
      }
    });

    return {
      issues: [...new Set(issues)],
      repaired: normalizePreferences(raw),
    };
  }

  function currentRawPreferences() {
    const value = storage.get(settingsKey);

    if (!value) {
      return { raw: preferences, parseIssue: null };
    }

    try {
      return { raw: JSON.parse(value), parseIssue: null };
    } catch {
      return { raw: {}, parseIssue: "Settings JSON cannot be parsed." };
    }
  }

  function settingsHealthReport() {
    const rawState = currentRawPreferences();
    const report = diagnosePreferences(rawState.raw);

    return {
      issues: [
        ...(rawState.parseIssue ? [rawState.parseIssue] : []),
        ...report.issues,
      ],
      repaired: report.repaired,
    };
  }

  function syncSettingsHealth() {
    if (!settingsHealthNode) {
      return;
    }

    const report = settingsHealthReport();
    const warning = report.issues.length > 0;

    settingsHealthNode.dataset.health = warning ? "warning" : "nominal";

    const settingsButton = settingsHealthNode.closest("[data-gate-settings-open]");

    if (settingsButton) {
      settingsButton.title = warning
        ? `Gate Settings · ${report.issues.length} configuration issue${report.issues.length === 1 ? "" : "s"}`
        : "Gate Settings · Configuration nominal";
    }
  }

  function renderDiagnostics(report = null) {
    if (!diagnosticsSummary || !diagnosticsList) {
      return;
    }

    const rawState = currentRawPreferences();
    const result = report || diagnosePreferences(rawState.raw);
    const issues = [
      ...(rawState.parseIssue ? [rawState.parseIssue] : []),
      ...result.issues,
    ];

    diagnosticsList.replaceChildren();

    const summaryBox = diagnosticsSummary.closest(".gate-diagnostics-summary");

    if (!issues.length) {
      diagnosticsSummary.textContent = "CONFIGURATION NOMINAL";
      summaryBox?.classList.remove("is-warning");
      syncSettingsHealth();
      return;
    }

    diagnosticsSummary.textContent = `${issues.length} ISSUE${issues.length === 1 ? "" : "S"} DETECTED`;
    summaryBox?.classList.add("is-warning");

    issues.forEach((issue) => {
      const item = document.createElement("div");
      item.className = "gate-diagnostic-item";
      item.textContent = issue;
      diagnosticsList.appendChild(item);
    });

    syncSettingsHealth();
  }

  function repairCurrentConfig() {
    const rawState = currentRawPreferences();
    const report = diagnosePreferences(rawState.raw);

    preferences = report.repaired;
    writeJson(settingsKey, preferences);
    applyPreferences();
    syncSettingsControls();
    renderDiagnostics();
    renderSuggestions();

    setSettingsStatus(
      rawState.parseIssue || report.issues.length
        ? "CONFIG REPAIRED"
        : "NO REPAIR REQUIRED"
    );
  }

  runDiagnosticsButton?.addEventListener("click", () => {
    renderDiagnostics();
    setSettingsStatus("DIAGNOSTICS COMPLETE");
  });

  repairConfigButton?.addEventListener("click", repairCurrentConfig);

  function gateConfigPayload() {
    return {
      format: "neutriverse-gate-config",
      version: "3.6",
      exportedAt: new Date().toISOString(),
      preferences: normalizePreferences(preferences),
      currentVector: readVectorOverride(),
    };
  }

  function exportGateConfig() {
    const payload = JSON.stringify(gateConfigPayload(), null, 2);
    const blob = new Blob([payload], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");

    const stamp = new Date().toISOString().slice(0, 10);
    anchor.href = url;
    anchor.download = `neutriverse-gate-config-${stamp}.json`;
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();

    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
    setSettingsStatus("CONFIG EXPORTED");
  }

  function normalizeImportedVector(value) {
    if (!value || typeof value !== "object") {
      return null;
    }

    const status = ["ACTIVE", "STANDBY", "PAUSED"].includes(value.status)
      ? value.status
      : "ACTIVE";

    return {
      title: typeof value.title === "string" ? value.title.slice(0, 72) : "",
      status,
      description: typeof value.description === "string" ? value.description.slice(0, 140) : "",
      updatedAt: new Date().toISOString(),
    };
  }

  async function importGateConfigFile(file) {
    if (!file || file.size > 256 * 1024) {
      setSettingsStatus("INVALID CONFIG FILE");
      return;
    }

    try {
      const text = await file.text();
      const payload = JSON.parse(text);

      if (
        payload?.format !== "neutriverse-gate-config" ||
        !payload.preferences ||
        typeof payload.preferences !== "object"
      ) {
        throw new Error("Unsupported Gate configuration");
      }

      const importReport = diagnosePreferences(payload.preferences);
      const importedPreferences = importReport.repaired;
      writeJson(settingsKey, importedPreferences);

      try {
        sessionStorage.setItem(
          "neutriverse-gate-last-import-report",
          JSON.stringify({
            issueCount: importReport.issues.length,
            importedAt: new Date().toISOString(),
          })
        );
      } catch {
        /* Ignore restricted storage. */
      }

      const vector = normalizeImportedVector(payload.currentVector);

      if (vector) {
        writeJson(vectorKey, vector);
      } else {
        storage.remove(vectorKey);
      }

      window.location.reload();
    } catch {
      setSettingsStatus("IMPORT FAILED");
    } finally {
      if (importConfigFile) {
        importConfigFile.value = "";
      }
    }
  }

  exportConfigButton?.addEventListener("click", exportGateConfig);

  importConfigButton?.addEventListener("click", () => {
    importConfigFile?.click();
  });

  importConfigFile?.addEventListener("change", () => {
    importGateConfigFile(importConfigFile.files?.[0]);
  });

  resetSettingsButton?.addEventListener("click", () => {
    if (!window.confirm("Reset Gate preferences and local Gate data in this browser?")) {
      return;
    }

    storage.remove(settingsKey);
    storage.remove(legacySettingsKey);
    storage.remove(recentTransitKey);
    storage.remove(weatherLocationKey);
    storage.remove(weatherCacheKey);
    storage.remove(vectorKey);
    storage.remove(noteKey);
    storage.remove(noteTimeKey);
    storage.remove(snapshotKey);

    window.location.reload();
  });

  // Drawer focus loop.
  settingsDrawer?.addEventListener("keydown", (event) => {
    if (event.key !== "Tab") return;

    const focusable = [...settingsDrawer.querySelectorAll(
      'button:not([disabled]), select:not([disabled]), input:not([disabled]), [href], [tabindex]:not([tabindex="-1"])'
    )].filter(
      (node) =>
        !node.hidden &&
        !node.closest("[hidden]") &&
        !node.closest(".is-filtered-out")
    );

    if (!focusable.length) return;

    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  syncSettingsControls();
  syncSettingsHealth();

  try {
    const importReport = JSON.parse(
      sessionStorage.getItem("neutriverse-gate-last-import-report") || "null"
    );

    if (importReport) {
      sessionStorage.removeItem("neutriverse-gate-last-import-report");

      if (importReport.issueCount > 0) {
        setSettingsStatus(
          `IMPORT REPAIRED ${importReport.issueCount} ISSUE${importReport.issueCount === 1 ? "" : "S"}`
        );
      }
    }
  } catch {
    /* Ignore malformed session report. */
  }

  // ---------------------------------------------------------------------------
  // Global keyboard shortcuts
  // ---------------------------------------------------------------------------

  document.addEventListener("keydown", (event) => {
    const commandKey = event.metaKey || event.ctrlKey;
    const target = event.target;
    const editableTarget =
      target instanceof HTMLElement &&
      (
        target.matches("input, textarea, select") ||
        target.isContentEditable
      );

    if (
      preferences.routeShortcuts &&
      commandKey &&
      event.altKey &&
      /^[1-9]$/.test(event.key) &&
      !editableTarget
    ) {
      const index = Number(event.key) - 1;
      const groupId = routeGroupIds[index];

      if (groupId) {
        event.preventDefault();

        savePreferences({
          ...preferences,
          activeRouteGroup: groupId,
        });

        return;
      }
    }

    if (commandKey && event.key.toLowerCase() === "k") {
      event.preventDefault();
      closeSettings({ restoreFocus: false });
      searchInput?.focus();
      searchInput?.select();
      renderSuggestions();
      return;
    }

    if (commandKey && event.key === ",") {
      event.preventDefault();
      openSettings();
      return;
    }

    if (commandKey && event.shiftKey && event.key.toLowerCase() === "f") {
      event.preventDefault();
      savePreferences({
        ...preferences,
        presentation: preferences.presentation === "focus" ? "dashboard" : "focus",
      });
      return;
    }

    if (event.key === "Escape" && settingsDrawer && !settingsDrawer.hidden) {
      event.preventDefault();
      closeSettings();
      return;
    }

    if (document.activeElement === searchInput && !suggestionsNode?.hidden) {
      if (event.key === "ArrowDown") {
        event.preventDefault();
        activeSuggestionIndex = suggestionItems.length
          ? (activeSuggestionIndex < 0 ? 0 : (activeSuggestionIndex + 1) % suggestionItems.length)
          : -1;
        syncActiveSuggestion();
        return;
      }

      if (event.key === "ArrowUp") {
        event.preventDefault();
        activeSuggestionIndex = suggestionItems.length
          ? (activeSuggestionIndex < 0
              ? suggestionItems.length - 1
              : (activeSuggestionIndex - 1 + suggestionItems.length) % suggestionItems.length)
          : -1;
        syncActiveSuggestion();
        return;
      }

      if (event.key === "Enter" && activeSuggestionIndex >= 0 && suggestionItems.length) {
        event.preventDefault();
        chooseSuggestion(activeSuggestionIndex);
        return;
      }
    }

    if (event.key === "Escape" && document.activeElement === searchInput) {
      searchInput.value = "";
      searchInput.blur();

      if (suggestionsNode) suggestionsNode.hidden = true;
      syncQueryContext();
    }
  });
})();
