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

  const launchGrid = qs("[data-gate-launch-grid]");
  let launchNodes = qsa("[data-gate-launch]");
  const routeNodes = qsa("[data-gate-route]");
  const vectorLinkNodes = qsa("[data-gate-vector-link]");
  const contextRouteNodes = qsa("[data-gate-context-route]");
  const routeGroupTabs = qsa("[data-gate-route-group-tab]");
  const routeGroupPanels = qsa("[data-gate-route-group-panel]");
  const dashboardGrid = qs("[data-gate-dashboard-grid]");
  const dashboardNodes = qsa("[data-gate-layout-id]");

  const launchMap = new Map();
  launchNodes.forEach((node) => {
    const command = (node.dataset.gateCommand || "").trim().toLowerCase();
    const label = (node.dataset.gateLabel || "").trim().toLowerCase();

    if (command) launchMap.set(command, node.href);
    if (label) launchMap.set(label, node.href);
  });

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

  const routeGroupIds = Array.isArray(routeGroupsDefault)
    ? routeGroupsDefault.map((group) => group.id).filter(Boolean)
    : [];

  const preferenceDefaults = {
    defaultSearch: settingsDefault.default_search || "google",
    density: settingsDefault.density === "compact" ? "compact" : "standard",
    ambient: settingsDefault.ambient !== false,
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
  };

  function normalizePreferences(raw = {}) {
    const modules = {
      ...preferenceDefaults.modules,
      ...(raw.modules && typeof raw.modules === "object" ? raw.modules : {}),
    };

    const requestedOrder = Array.isArray(raw.launchOrder)
      ? raw.launchOrder.filter((id) => defaultLaunchOrder.includes(id))
      : [];

    const launchOrder = [
      ...requestedOrder,
      ...defaultLaunchOrder.filter((id) => !requestedOrder.includes(id)),
    ];

    const hiddenLaunches = Array.isArray(raw.hiddenLaunches)
      ? raw.hiddenLaunches.filter((id) => defaultLaunchOrder.includes(id))
      : [];

    const requestedDashboardOrder = Array.isArray(raw.dashboardOrder)
      ? raw.dashboardOrder.filter((id) => defaultDashboardOrder.includes(id))
      : [];

    const dashboardOrder = [
      ...requestedDashboardOrder,
      ...defaultDashboardOrder.filter((id) => !requestedDashboardOrder.includes(id)),
    ];

    const activeRouteGroup = routeGroupIds.includes(raw.activeRouteGroup)
      ? raw.activeRouteGroup
      : preferenceDefaults.activeRouteGroup;

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

    routeGroupIds.forEach((groupId) => {
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
      presentation,
      modules,
      launchOrder,
      hiddenLaunches,
      dashboardOrder,
      activeRouteGroup,
      dashboardSpans,
      routeOverrides,
    };
  }

  const storedPreferences = readJson(
    settingsKey,
    readJson(legacySettingsKey, {})
  );

  let preferences = normalizePreferences(storedPreferences);

  function savePreferences(next) {
    preferences = normalizePreferences(next);
    writeJson(settingsKey, preferences);
    applyPreferences();
    syncSettingsControls();
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

  function applyLaunchPreferences() {
    if (!launchGrid) {
      return;
    }

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

    const hidden = new Set(preferences.hiddenLaunches);

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

  function routeGroupDefaults(groupId) {
    const group = Array.isArray(routeGroupsDefault)
      ? routeGroupsDefault.find((item) => item.id === groupId)
      : null;

    return Array.isArray(group?.routes) ? group.routes : [];
  }

  function resolvedRouteSlot(groupId, slotIndex) {
    const defaults = routeGroupDefaults(groupId)[slotIndex] || {};
    const override = preferences.routeOverrides?.[groupId]?.[slotIndex] || {};

    return {
      label: override.label?.trim() || defaults.label || `Route ${slotIndex + 1}`,
      detail: override.detail?.trim() || defaults.detail || "ROUTE",
      url: isSafeRouteUrl(override.url) ? override.url.trim() : (defaults.url || "/"),
    };
  }

  function applyRouteOverrides() {
    contextRouteNodes.forEach((node) => {
      const groupId = node.dataset.gateRouteGroupId;
      const slotIndex = Number(node.dataset.gateRouteSlot);

      if (!groupId || !Number.isInteger(slotIndex)) {
        return;
      }

      const route = resolvedRouteSlot(groupId, slotIndex);
      const group = routeGroupsDefault.find?.((item) => item.id === groupId);

      node.href = route.url;
      node.dataset.gateTransitLabel = route.label;
      node.dataset.gateTransitDetail = `${group?.label || groupId.toUpperCase()} · ${route.detail}`;

      const strong = node.querySelector("strong");
      const small = node.querySelector("small");

      if (strong) strong.textContent = route.label;
      if (small) small.textContent = route.detail;
    });
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

  function applyRouteGroup(groupId = preferences.activeRouteGroup) {
    const validId = routeGroupIds.includes(groupId)
      ? groupId
      : preferenceDefaults.activeRouteGroup;

    routeGroupTabs.forEach((tab) => {
      const selected = tab.dataset.gateRouteGroupTab === validId;
      tab.setAttribute("aria-selected", selected ? "true" : "false");
      tab.tabIndex = selected ? 0 : -1;
    });

    routeGroupPanels.forEach((panel) => {
      panel.hidden = panel.dataset.gateRouteGroupPanel !== validId;
    });
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

  launchNodes.forEach((node) => {
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

  contextRouteNodes.forEach((node) => {
    node.addEventListener("click", () => {
      recordTransit({
        label: node.dataset.gateTransitLabel || "CONTEXT ROUTE",
        detail: node.dataset.gateTransitDetail || "ROUTE MATRIX",
        action: "url",
        value: node.href,
      });
    });
  });

  routeGroupTabs.forEach((tab) => {
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

  function defaultEngine() {
    const key = engines[preferences.defaultSearch]
      ? preferences.defaultSearch
      : preferenceDefaults.defaultSearch;

    return engines[key] || Object.values(engines)[0];
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
      queryState.textContent = "g / gh / yt / wiki / map / ai";
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
  const settingModuleInputs = qsa("[data-gate-setting-module]");
  const settingRouteGroup = qs("[data-gate-setting-route-group]");
  const settingPresentation = qs("[data-gate-setting-presentation]");
  const dashboardSettingsNode = qs("[data-gate-dashboard-settings]");
  const routeEditGroup = qs("[data-gate-route-edit-group]");
  const routeEditorList = qs("[data-gate-route-editor-list]");
  const routeSaveGroupButton = qs("[data-gate-route-save-group]");
  const routeResetGroupButton = qs("[data-gate-route-reset-group]");
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

    savePreferences({
      ...preferences,
      routeOverrides: {
        ...preferences.routeOverrides,
        [groupId]: routes,
      },
    });

    renderRouteEditor(groupId);
    renderSuggestions();
    setSettingsStatus("ROUTE GROUP SAVED");
  }

  function resetRouteEditorGroup() {
    const groupId = routeEditGroup?.value;

    if (!routeGroupIds.includes(groupId)) {
      return;
    }

    const nextOverrides = {
      ...preferences.routeOverrides,
    };

    delete nextOverrides[groupId];

    savePreferences({
      ...preferences,
      routeOverrides: nextOverrides,
    });

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
    if (settingRouteGroup) settingRouteGroup.value = preferences.activeRouteGroup;
    if (routeEditGroup && !routeGroupIds.includes(routeEditGroup.value)) {
      routeEditGroup.value = preferences.activeRouteGroup;
    }

    settingModuleInputs.forEach((input) => {
      input.checked = moduleEnabled(input.dataset.gateSettingModule);
    });

    renderLaunchSettings();
    renderDashboardSettings();
    renderRouteEditor();
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

  function gateConfigPayload() {
    return {
      format: "neutriverse-gate-config",
      version: "3.1",
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

      const importedPreferences = normalizePreferences(payload.preferences);
      writeJson(settingsKey, importedPreferences);

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

    window.location.reload();
  });

  // Drawer focus loop.
  settingsDrawer?.addEventListener("keydown", (event) => {
    if (event.key !== "Tab") return;

    const focusable = [...settingsDrawer.querySelectorAll(
      'button:not([disabled]), select:not([disabled]), input:not([disabled]), [href], [tabindex]:not([tabindex="-1"])'
    )].filter((node) => !node.hidden);

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

  // ---------------------------------------------------------------------------
  // Global keyboard shortcuts
  // ---------------------------------------------------------------------------

  document.addEventListener("keydown", (event) => {
    const commandKey = event.metaKey || event.ctrlKey;

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
      if (queryState) queryState.textContent = "g / gh / yt / wiki / map / ai";
    }
  });
})();
