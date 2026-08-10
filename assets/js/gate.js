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
  // Quick note
  // ---------------------------------------------------------------------------

  const noteKey = "neutriverse-gate-field-record";
  const noteTimeKey = "neutriverse-gate-field-record-time";
  const note = qs("[data-gate-note]");
  const noteStatus = qs("[data-gate-note-status]");
  let noteTimer;

  function formatSavedTime(value) {
    if (!value) {
      return "EMPTY";
    }

    const date = new Date(value);

    if (Number.isNaN(date.getTime())) {
      return "SAVED";
    }

    return `SAVED ${new Intl.DateTimeFormat("en-GB", {
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    }).format(date)}`;
  }

  function refreshNoteStatus() {
    if (!noteStatus) {
      return;
    }

    const value = note?.value.trim() || "";
    noteStatus.textContent = value ? formatSavedTime(storage.get(noteTimeKey)) : "EMPTY";
  }

  if (note) {
    note.value = storage.get(noteKey) || "";
    refreshNoteStatus();

    note.addEventListener("input", () => {
      window.clearTimeout(noteTimer);

      if (noteStatus) {
        noteStatus.textContent = "WRITING";
      }

      noteTimer = window.setTimeout(() => {
        const value = note.value;
        const savedAt = new Date().toISOString();

        storage.set(noteKey, value);
        storage.set(noteTimeKey, savedAt);
        refreshNoteStatus();
      }, 280);
    });
  }

  // ---------------------------------------------------------------------------
  // Current Vector
  // ---------------------------------------------------------------------------

  const vectorConfigNode = document.getElementById("gate-vector-config");
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

  let vectorDefault = {};

  try {
    vectorDefault = JSON.parse(vectorConfigNode?.textContent || "{}");
  } catch {
    vectorDefault = {};
  }

  function readVectorOverride() {
    try {
      return JSON.parse(storage.get(vectorKey) || "null");
    } catch {
      return null;
    }
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
    if (!vectorPanel) {
      return;
    }

    const vector = currentVector();

    if (vectorTitleNode) vectorTitleNode.textContent = vector.title;
    if (vectorStatusNode) vectorStatusNode.textContent = vector.status;
    if (vectorDescriptionNode) vectorDescriptionNode.textContent = vector.description;

    if (vectorUpdatedNode) {
      if (!vector.updatedAt) {
        vectorUpdatedNode.textContent = "CONFIG DEFAULT";
      } else {
        const date = new Date(vector.updatedAt);
        vectorUpdatedNode.textContent = `UPDATED ${new Intl.DateTimeFormat("en-GB", {
          hour: "2-digit",
          minute: "2-digit",
          hour12: false,
        }).format(date)}`;
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

  vectorEditButton?.setAttribute("aria-expanded", "false");
  vectorEditButton?.addEventListener("click", openVectorEditor);
  vectorCancelButton?.addEventListener("click", closeVectorEditor);

  vectorResetButton?.addEventListener("click", () => {
    storage.remove(vectorKey);
    renderVector();
    closeVectorEditor();
  });

  vectorEditor?.addEventListener("submit", (event) => {
    event.preventDefault();

    const status = ["ACTIVE", "STANDBY", "PAUSED"].includes(vectorStatusInput?.value)
      ? vectorStatusInput.value
      : "ACTIVE";

    storage.set(vectorKey, JSON.stringify({
      title: vectorTitleInput?.value.trim() || vectorDefault.title || "Current Vector",
      status,
      description: vectorDescriptionInput?.value.trim() || "",
      updatedAt: new Date().toISOString(),
    }));

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
    try {
      const parsed = JSON.parse(storage.get(recentTransitKey) || "[]");
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }

  function writeRecentTransits(items) {
    storage.set(recentTransitKey, JSON.stringify(items.slice(0, recentTransitLimit)));
  }

  function recordTransit(entry) {
    if (!entry?.label || !entry?.action) return;

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

  function safeOrigin(value) {
    try {
      return new URL(value).origin;
    } catch {
      return value;
    }
  }

  launchNodes.forEach((node) => {
    node.addEventListener("click", () => {
      recordTransit({
        label: node.dataset.gateCommand
          ? node.dataset.gateCommand.toUpperCase()
          : node.textContent.trim(),
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

  // ---------------------------------------------------------------------------
  // Query array
  // ---------------------------------------------------------------------------

  const searchForm = qs("[data-gate-search]");
  const searchInput = qs("[data-gate-search-input]");
  const queryState = qs("[data-gate-query-state]");
  const configNode = document.getElementById("gate-search-config");

  let engines = {};

  try {
    engines = JSON.parse(configNode?.textContent || "{}");
  } catch {
    engines = {};
  }

  const defaultEngine = "google";
  const launchNodes = qsa("[data-gate-launch]");
  const routeNodes = qsa("[data-gate-route]");
  const vectorLinkNodes = qsa("[data-gate-vector-link]");

  const launchMap = new Map();
  launchNodes.forEach((node) => {
    const command = (node.dataset.gateCommand || "").trim().toLowerCase();
    const label = (node.dataset.gateLabel || "").trim().toLowerCase();

    if (command) {
      launchMap.set(command, node.href);
    }

    if (label) {
      launchMap.set(label, node.href);
    }
  });

  function engineByPrefix(prefix) {
    return Object.values(engines).find((engine) => {
      return String(engine.prefix || "").toLowerCase() === prefix.toLowerCase();
    });
  }

  function buildEngineUrl(engine, query) {
    if (!engine?.url) {
      return null;
    }

    return engine.url.replace("{query}", encodeURIComponent(query));
  }

  function looksLikeUrl(value) {
    if (/^[a-z][a-z0-9+.-]*:\/\//i.test(value)) {
      return true;
    }

    return /^[^\s/]+\.[a-z]{2,}(?:[/?#][^\s]*)?$/i.test(value);
  }

  function normalizeUrl(value) {
    if (/^[a-z][a-z0-9+.-]*:\/\//i.test(value)) {
      return value;
    }

    return `https://${value}`;
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

    if (verb === "note") {
      if (note && argument) {
        note.value = note.value.trim()
          ? `${note.value.trimEnd()}\n> ${argument}`
          : `> ${argument}`;
        note.dispatchEvent(new Event("input", { bubbles: true }));
        note.focus();
        return true;
      }
    }

    if (verb === "clear" && argument === "note") {
      if (note) {
        note.value = "";
        storage.set(noteKey, "");
        storage.set(noteTimeKey, "");
        refreshNoteStatus();
        return true;
      }
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

    if (verb === "clear" && argument === "recent") {
      storage.remove(recentTransitKey);
      renderSuggestions();
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
      recordTransit({
        label: safeOrigin(destination).replace(/^https?:\/\//, "").toUpperCase(),
        detail: "DIRECT TRANSIT",
        action: "url",
        value: safeOrigin(destination),
      });
      window.location.assign(destination);
      return;
    }

    const match = input.match(/^(\S+)\s+(.+)$/);

    if (match) {
      const prefix = match[1];
      const query = match[2];
      const engine = engineByPrefix(prefix);

      if (engine) {
        const destination = buildEngineUrl(engine, query);

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

    const engine = engines[defaultEngine] || Object.values(engines)[0];
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

  const suggestionsNode = qs("[data-gate-suggestions]");
  let suggestionItems = [];
  let activeSuggestionIndex = -1;
  let suggestionHideTimer;

  const commandSuggestions = [
    { label: "> theme dark", detail: "Switch to Night Observatory", action: "fill", value: "> theme dark", code: "CMD" },
    { label: "> theme light", detail: "Switch to Prospero Light", action: "fill", value: "> theme light", code: "CMD" },
    { label: "> theme toggle", detail: "Toggle authored theme state", action: "fill", value: "> theme toggle", code: "CMD" },
    { label: "> note ", detail: "Append to Field Record", action: "fill", value: "> note ", code: "CMD" },
    { label: "> vector edit", detail: "Edit Current Vector", action: "fill", value: "> vector edit", code: "CMD" },
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
    return launchNodes.map((node) => ({
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

  function recentSuggestions() {
    return readRecentTransits().slice(0, 5).map((item) => ({ ...item, code: "↺" }));
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

      if (recent.length) groups.push({ title: "RECENT TRANSITS", items: recent });

      groups.push({
        title: "QUICK COMMANDS",
        items: [
          ...engineSuggestions().slice(0, 5),
          { label: "> vector edit", detail: "Edit Current Vector", action: "fill", value: "> vector edit", code: "CMD" },
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
        const button = document.createElement("button");
        const itemIndex = runningIndex;
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
          item.action === "execute" ? "EXECUTE" : "OPEN";

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
      if (selected) node.scrollIntoView({ block: "nearest" });
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

  suggestionsNode?.addEventListener("pointerdown", (event) => event.preventDefault());

  suggestionsNode?.addEventListener("click", (event) => {
    const button = event.target.closest?.("[data-suggestion-index]");
    if (button) chooseSuggestion(Number(button.dataset.suggestionIndex));
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

  searchForm?.addEventListener("submit", (event) => {
    event.preventDefault();
    executeQuery(searchInput?.value || "");
  });

  searchInput?.addEventListener("input", () => {
    renderSuggestions();

    if (!queryState) {
      return;
    }

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

    queryState.textContent = engine ? `${engine.label.toUpperCase()} SEARCH` : "GOOGLE SEARCH";
  });

  document.addEventListener("keydown", (event) => {
    const commandKey = event.metaKey || event.ctrlKey;

    if (commandKey && event.key.toLowerCase() === "k") {
      event.preventDefault();
      searchInput?.focus();
      searchInput?.select();
      renderSuggestions();
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
        const value = searchInput.value.trim();

        if (!value || value.startsWith(">") || value.startsWith("/") || !value.includes(" ")) {
          event.preventDefault();
          chooseSuggestion(activeSuggestionIndex);
          return;
        }
      }
    }

    if (event.key === "Escape" && document.activeElement === searchInput) {
      searchInput.value = "";
      searchInput.blur();

      if (suggestionsNode) suggestionsNode.hidden = true;

      if (queryState) {
        queryState.textContent = "g / gh / yt / wiki / map / ai";
      }
    }
  });

  // ---------------------------------------------------------------------------
  // V2 · Local Conditions
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

  function readJsonStorage(key) {
    try {
      return JSON.parse(storage.get(key) || "null");
    } catch {
      return null;
    }
  }

  function writeJsonStorage(key, value) {
    storage.set(key, JSON.stringify(value));
  }

  function weatherCodeLabel(code) {
    return weatherCodes.get(Number(code)) || "VARIABLE";
  }

  function showWeatherEmpty(message = "NO LOCAL FIX") {
    if (!weatherPanel) {
      return;
    }

    weatherEmpty?.removeAttribute("hidden");
    weatherData?.setAttribute("hidden", "");

    const title = weatherEmpty?.querySelector("strong");
    if (title) {
      title.textContent = message;
    }
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

    if (weatherTemp) {
      weatherTemp.textContent = `${Math.round(current.temperature_2m)}°`;
    }

    if (weatherLabel) {
      weatherLabel.textContent = weatherCodeLabel(current.weather_code);
    }

    if (weatherFeels) {
      weatherFeels.textContent = `${Math.round(current.apparent_temperature)}°`;
    }

    if (weatherWind) {
      weatherWind.textContent = `${Math.round(current.wind_speed_10m)} KM/H`;
    }

    if (weatherLocation) {
      const zone = payload.timezone_abbreviation || resolvedZone;
      weatherLocation.textContent = `${zone.toUpperCase()} · ${Math.abs(location.latitude).toFixed(2)}${location.latitude >= 0 ? "N" : "S"} / ${Math.abs(location.longitude).toFixed(2)}${location.longitude >= 0 ? "E" : "W"}`;
    }

    if (weatherDays) {
      weatherDays.replaceChildren();

      const count = Math.min(3, daily.time?.length || 0);

      for (let index = 0; index < count; index += 1) {
        const day = document.createElement("div");
        day.className = "gate-weather-day";

        const label = new Intl.DateTimeFormat("en-GB", {
          weekday: "short",
        }).format(new Date(`${daily.time[index]}T12:00:00`)).toUpperCase();

        const max = Math.round(daily.temperature_2m_max[index]);
        const min = Math.round(daily.temperature_2m_min[index]);
        const rain = daily.precipitation_probability_max?.[index];

        day.innerHTML = `
          <span>${label}</span>
          <strong>${max}° / ${min}°</strong>
          <small>${Number.isFinite(rain) ? `${Math.round(rain)}% PRECIP` : weatherCodeLabel(daily.weather_code?.[index])}</small>
        `;

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
    if (!weatherPanel || !location) {
      return;
    }

    const cached = readJsonStorage(weatherCacheKey);

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

    if (weatherUpdated) {
      weatherUpdated.textContent = "SYNCING";
    }

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

      writeJsonStorage(weatherCacheKey, {
        timestamp: Date.now(),
        latitude: location.latitude,
        longitude: location.longitude,
        payload,
      });

      renderWeather(payload, location);
    } catch {
      if (cached?.payload) {
        renderWeather(cached.payload, location);

        if (weatherUpdated) {
          weatherUpdated.textContent = "CACHED";
        }

        return;
      }

      showWeatherEmpty("WEATHER UNAVAILABLE");
    }
  }

  function requestLocation() {
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

        writeJsonStorage(weatherLocationKey, location);

        locateButtons.forEach((button) => {
          button.disabled = false;
          button.textContent = button.closest("[data-gate-weather-data]") ? "RELOCATE" : "LOCATE";
        });

        fetchWeather(location, { force: true });
      },
      () => {
        locateButtons.forEach((button) => {
          button.disabled = false;
          button.textContent = button.closest("[data-gate-weather-data]") ? "RELOCATE" : "LOCATE";
        });

        showWeatherEmpty("LOCATION DENIED");
      },
      {
        enableHighAccuracy: false,
        timeout: 9000,
        maximumAge: 24 * 60 * 60 * 1000,
      }
    );
  }

  locateButtons.forEach((button) => {
    button.addEventListener("click", requestLocation);
  });

  const savedWeatherLocation = readJsonStorage(weatherLocationKey);

  if (savedWeatherLocation?.latitude && savedWeatherLocation?.longitude) {
    fetchWeather(savedWeatherLocation);
  } else if (weatherPanel) {
    showWeatherEmpty();
  }


})();
