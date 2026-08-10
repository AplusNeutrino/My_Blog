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

    if (verb === "home") {
      window.location.assign("/");
      return true;
    }

    return false;
  }

  function executeQuery(value) {
    const input = value.trim();

    if (!input) {
      return;
    }

    if (input.startsWith(">")) {
      const handled = runCommand(input.slice(1));

      if (!handled && queryState) {
        queryState.textContent = "UNKNOWN COMMAND";
      }

      return;
    }

    if (input.startsWith("/")) {
      window.location.assign(input);
      return;
    }

    if (looksLikeUrl(input)) {
      window.location.assign(normalizeUrl(input));
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
          window.location.assign(destination);
          return;
        }
      }
    }

    const engine = engines[defaultEngine] || Object.values(engines)[0];
    const destination = buildEngineUrl(engine, input);

    if (destination) {
      window.location.assign(destination);
    }
  }

  searchForm?.addEventListener("submit", (event) => {
    event.preventDefault();
    executeQuery(searchInput?.value || "");
  });

  searchInput?.addEventListener("input", () => {
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
      return;
    }

    if (event.key === "Escape" && document.activeElement === searchInput) {
      searchInput.value = "";
      searchInput.blur();

      if (queryState) {
        queryState.textContent = "g / gh / yt / wiki / map / ai";
      }
    }
  });
})();
