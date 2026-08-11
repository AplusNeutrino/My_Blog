---
layout: gate
title: "Gate"
permalink: /gate/
description: "Neutriverse personal transit gate."
---

{% assign gate = site.data.gate %}

<div class="gate-app" data-gate-app>
  <aside class="gate-rail" aria-label="Gate navigation">
    <a class="gate-rail-logo" href="{{ '/' | relative_url }}" aria-label="返回 Neutriverse">
      <img src="{{ '/assets/img/logo.png' | relative_url }}" alt="">
    </a>

    <nav class="gate-rail-nav" aria-label="Facility routes">
      <a href="{{ '/' | relative_url }}" data-gate-tooltip="Neutriverse">
        <span aria-hidden="true">N</span>
      </a>
      <a href="{{ '/ravenis/' | relative_url }}" data-gate-tooltip="Ravenis">
        <span aria-hidden="true">R</span>
      </a>
      <a href="{{ '/occult-atlas/' | relative_url }}" data-gate-tooltip="Atlas">
        <span aria-hidden="true">A</span>
      </a>
    </nav>

    <div class="gate-rail-controls">
      <button
        class="gate-rail-control gate-presentation-toggle"
        type="button"
        data-gate-mode-toggle
        aria-label="切换 Gate 展示模式"
        title="Toggle Focus / Dashboard"
      >
        <svg viewBox="0 0 24 24" aria-hidden="true">
          <rect x="4" y="4" width="6" height="6" rx="1"></rect>
          <rect x="14" y="4" width="6" height="6" rx="1"></rect>
          <rect x="4" y="14" width="6" height="6" rx="1"></rect>
          <rect x="14" y="14" width="6" height="6" rx="1"></rect>
        </svg>
      </button>

      <button
        class="gate-rail-control gate-settings-toggle"
        type="button"
        data-gate-settings-open
        aria-label="打开 Gate 设置"
        title="Gate Settings"
      >
        <svg viewBox="0 0 24 24" aria-hidden="true">
          <circle cx="12" cy="12" r="3"></circle>
          <path d="M19.4 15a1.7 1.7 0 0 0 .34 1.88l.06.06-2.83 2.83-.06-.06A1.7 1.7 0 0 0 15 19.4a1.7 1.7 0 0 0-1 .6 1.7 1.7 0 0 0-.4 1.1V21h-4v-.1a1.7 1.7 0 0 0-1.4-1.66 1.7 1.7 0 0 0-1.5.47l-.06.06-2.83-2.83.06-.06A1.7 1.7 0 0 0 4.6 15a1.7 1.7 0 0 0-.6-1 1.7 1.7 0 0 0-1.1-.4H3v-4h.1A1.7 1.7 0 0 0 4.76 8.2a1.7 1.7 0 0 0-.47-1.5l-.06-.06 2.83-2.83.06.06A1.7 1.7 0 0 0 9 4.6a1.7 1.7 0 0 0 1-.6 1.7 1.7 0 0 0 .4-1.1V3h4v.1A1.7 1.7 0 0 0 15.8 4.76a1.7 1.7 0 0 0 1.5-.47l.06-.06 2.83 2.83-.06.06A1.7 1.7 0 0 0 19.4 9c.1.38.32.72.6 1 .3.28.68.42 1.1.4h.1v4h-.1A1.7 1.7 0 0 0 19.4 15Z"></path>
        </svg>
      </button>

      <button
        class="gate-rail-control gate-theme-toggle"
        type="button"
        data-gate-theme
        aria-label="切换主题"
      >
        <svg viewBox="0 0 24 24" aria-hidden="true">
          <circle cx="12" cy="12" r="4"></circle>
          <path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.66 6.34l1.41-1.41"></path>
        </svg>
      </button>
    </div>
  </aside>

  <main class="gate-main">
    <header class="gate-topline">
      <div>
        <p class="gate-eyebrow">
          <span class="theme-copy-night">NEUTRIVERSE // TRANSIT MODULE</span>
          <span class="theme-copy-day">NEUTRIVERSE // INDEXING DESK</span>
        </p>
        <p class="gate-node">
          <span class="theme-copy-night">PERSONAL NAVIGATION ARRAY</span>
          <span class="theme-copy-day">PERSONAL REFERENCE HALL</span>
        </p>
      </div>

      <div class="gate-top-status" aria-label="Local status">
        <span data-gate-mode-label>DASHBOARD</span>
        <span aria-hidden="true">/</span>
        <span data-gate-network-dot class="gate-status-dot"></span>
        <span data-gate-network>ONLINE</span>
        <span aria-hidden="true">/</span>
        <span data-gate-zone>LOCAL NODE</span>
      </div>
    </header>

    <section class="gate-hero" aria-labelledby="gate-time">
      <div class="gate-orbit gate-orbit-a" aria-hidden="true"></div>
      <div class="gate-orbit gate-orbit-b" aria-hidden="true"></div>

      <p class="gate-hero-label">
        <span class="theme-copy-night">LOCAL TEMPORAL REFERENCE</span>
        <span class="theme-copy-day">CURRENT ARCHIVE HOUR</span>
      </p>

      <h1 id="gate-time" class="gate-time" data-gate-time>--:--</h1>
      <p class="gate-date" data-gate-date>---</p>
      <p class="gate-timezone" data-gate-timezone>LOCAL NODE</p>
    </section>

    <section class="gate-query-section" aria-labelledby="gate-query-label">
      <div class="gate-section-heading gate-query-heading">
        <div>
          <span class="gate-section-index">00</span>
          <div>
            <p id="gate-query-label">
              <span class="theme-copy-night">QUERY ARRAY</span>
              <span class="theme-copy-day">REFERENCE INDEX</span>
            </p>
            <span>
              <span class="theme-copy-night">Awaiting signal input.</span>
              <span class="theme-copy-day">请输入检索内容或指令。</span>
            </span>
          </div>
        </div>
        <kbd>⌘ K</kbd>
      </div>

      <form class="gate-query" data-gate-search>
        <label class="sr-only" for="gate-search-input">Search or command</label>
        <span class="gate-prompt" aria-hidden="true">&gt;</span>
        <input
          id="gate-search-input"
          data-gate-search-input
          type="text"
          inputmode="search"
          autocomplete="off"
          spellcheck="false"
          placeholder="Search the web, paste a URL, or type a command…"
        >
        <button type="submit">EXECUTE</button>
      </form>

      <div
        class="gate-query-suggestions"
        data-gate-suggestions
        role="listbox"
        aria-label="Query suggestions"
        hidden
      ></div>

      <div class="gate-query-hints" aria-live="polite">
        <span data-gate-query-state>g / gh / yt / wiki / map / ai</span>
        <span>URL · /route · &gt; command</span>
      </div>
    </section>

    <section class="gate-launch-section" aria-labelledby="gate-launch-title" data-gate-module="launch_routes">
      <div class="gate-section-heading">
        <div>
          <span class="gate-section-index">01</span>
          <div>
            <p id="gate-launch-title">
              <span class="theme-copy-night">LAUNCH ROUTES</span>
              <span class="theme-copy-day">PRIMARY REFERENCES</span>
            </p>
            <span>
              <span class="theme-copy-night">Frequent external vectors.</span>
              <span class="theme-copy-day">常用站点与检索入口。</span>
            </span>
          </div>
        </div>
      </div>

      <div class="gate-launch-grid" data-gate-launch-grid>
        {% for item in gate.launches %}
          <a
            class="gate-launch"
            href="{{ item.url }}"
            data-gate-launch
            data-gate-launch-id="{{ item.command | downcase }}"
            data-gate-command="{{ item.command | downcase }}"
            data-gate-label="{{ item.name | downcase }}"
          >
            <span class="gate-launch-code">{{ item.code }}</span>
            <span class="gate-launch-arrow" aria-hidden="true">↗</span>
            <strong>{{ item.name }}</strong>
            <small>{{ item.role }}</small>
          </a>
        {% endfor %}
      </div>
    </section>

    <section
      class="gate-context-section"
      aria-labelledby="gate-context-title"
      data-gate-module="context_routes"
      data-gate-context-routes
    >
      <div class="gate-section-heading gate-context-heading">
        <div>
          <span class="gate-section-index">02</span>
          <div>
            <p id="gate-context-title">
              <span class="theme-copy-night">ROUTE MATRIX</span>
              <span class="theme-copy-day">REFERENCE ROUTES</span>
            </p>
            <span>
              <span class="theme-copy-night">Context-bound transit vectors.</span>
              <span class="theme-copy-day">按使用情境组织的入口。</span>
            </span>
          </div>
        </div>
      </div>

      <div class="gate-context-shell">
        <div class="gate-context-tabs" role="tablist" aria-label="Route groups">
          {% for group in gate.route_groups %}
            <button
              type="button"
              role="tab"
              data-gate-route-group-tab="{{ group.id }}"
              aria-controls="gate-route-group-{{ group.id }}"
              aria-selected="{% if forloop.first %}true{% else %}false{% endif %}"
            >
              <strong>{{ group.label }}</strong>
              <small>{{ group.detail }}</small>
            </button>
          {% endfor %}
        </div>

        <div class="gate-context-panels">
          {% for group in gate.route_groups %}
            <div
              id="gate-route-group-{{ group.id }}"
              class="gate-context-panel"
              role="tabpanel"
              data-gate-route-group-panel="{{ group.id }}"
              {% unless forloop.first %}hidden{% endunless %}
            >
              {% for route in group.routes %}
                {% assign external = false %}
                {% if route.url contains '://' %}
                  {% assign external = true %}
                {% endif %}
                <a
                  href="{% if external %}{{ route.url }}{% else %}{{ route.url | relative_url }}{% endif %}"
                  data-gate-context-route
                  data-gate-route-group-id="{{ group.id }}"
                  data-gate-route-slot="{{ forloop.index0 }}"
                  data-gate-default-label="{{ route.label | escape }}"
                  data-gate-default-detail="{{ route.detail | escape }}"
                  data-gate-default-url="{{ route.url | escape }}"
                  data-gate-transit-label="{{ route.label }}"
                  data-gate-transit-detail="{{ group.label }} · {{ route.detail }}"
                >
                  <span>
                    <strong>{{ route.label }}</strong>
                    <small>{{ route.detail }}</small>
                  </span>
                  <span aria-hidden="true">↗</span>
                </a>
              {% endfor %}
            </div>
          {% endfor %}
        </div>
      </div>
    </section>

    <div class="gate-dashboard-grid" data-gate-dashboard-grid>
      {% if gate.current_vector.enabled %}
      <section class="gate-panel gate-vector-panel" aria-labelledby="gate-vector-title" data-gate-vector-panel data-gate-module="current_vector" data-gate-layout-id="current_vector">
        <div class="gate-section-heading">
          <div>
            <span class="gate-section-index" data-gate-layout-index="current_vector">02</span>
            <div>
              <p id="gate-vector-title">CURRENT VECTOR</p>
              <span>
                <span class="theme-copy-night">Resume the active trajectory.</span>
                <span class="theme-copy-day">继续当前工作路径。</span>
              </span>
            </div>
          </div>
          <button class="gate-panel-action" type="button" data-gate-vector-edit>EDIT</button>
        </div>

        <div class="gate-vector-display" data-gate-vector-display>
          <div class="gate-vector-header">
            <div>
              <span class="gate-vector-status">
                <span class="gate-status-dot"></span>
                <span data-gate-vector-status>{{ gate.current_vector.status }}</span>
              </span>
              <h2 data-gate-vector-title>{{ gate.current_vector.title }}</h2>
              <p data-gate-vector-description>{{ gate.current_vector.description }}</p>
            </div>
            <span class="gate-vector-mark" aria-hidden="true">↗</span>
          </div>

          <div class="gate-vector-links">
            {% for link in gate.current_vector.links %}
              {% assign external = false %}
              {% if link.url contains '://' %}
                {% assign external = true %}
              {% endif %}
              <a
                href="{% if external %}{{ link.url }}{% else %}{{ link.url | relative_url }}{% endif %}"
                data-gate-vector-link
                data-gate-transit-label="{{ link.label }}"
                data-gate-transit-detail="{{ link.detail }}"
              >
                <span>{{ link.label }}</span>
                <small>{{ link.detail }}</small>
              </a>
            {% endfor %}
          </div>

          <div class="gate-vector-meta">
            <span>LOCAL OVERRIDE</span>
            <span data-gate-vector-updated>CONFIG DEFAULT</span>
          </div>
        </div>

        <form class="gate-vector-editor" data-gate-vector-editor hidden>
          <label>
            <span>TITLE</span>
            <input type="text" maxlength="72" data-gate-vector-title-input>
          </label>

          <label>
            <span>STATUS</span>
            <select data-gate-vector-status-input>
              <option value="ACTIVE">ACTIVE</option>
              <option value="STANDBY">STANDBY</option>
              <option value="PAUSED">PAUSED</option>
            </select>
          </label>

          <label class="gate-vector-editor-wide">
            <span>DESCRIPTION</span>
            <input type="text" maxlength="140" data-gate-vector-description-input>
          </label>

          <div class="gate-vector-editor-actions">
            <button type="submit">SAVE</button>
            <button type="button" data-gate-vector-reset>RESET</button>
            <button type="button" data-gate-vector-cancel>CANCEL</button>
          </div>
        </form>
      </section>
      {% endif %}

      {% if gate.weather.enabled %}
      <section class="gate-panel gate-weather-panel" aria-labelledby="gate-weather-title" data-gate-weather-panel data-gate-module="local_conditions" data-gate-layout-id="local_conditions">
        <div class="gate-section-heading">
          <div>
            <span class="gate-section-index" data-gate-layout-index="local_conditions">03</span>
            <div>
              <p id="gate-weather-title">LOCAL CONDITIONS</p>
              <span data-gate-weather-subtitle>
                <span class="theme-copy-night">Location remains local to this browser.</span>
                <span class="theme-copy-day">位置仅保存在当前浏览器。</span>
              </span>
            </div>
          </div>
        </div>

        <div class="gate-weather-empty" data-gate-weather-empty>
          <span class="gate-weather-sigil" aria-hidden="true">◎</span>
          <strong>NO LOCAL FIX</strong>
          <p>Grant location once to establish this node.</p>
          <button type="button" data-gate-locate>LOCATE</button>
        </div>

        <div class="gate-weather-data" data-gate-weather-data hidden>
          <div class="gate-weather-current">
            <div>
              <span class="gate-weather-location" data-gate-weather-location>LOCAL NODE</span>
              <strong data-gate-weather-temp>--°</strong>
              <span data-gate-weather-label>---</span>
            </div>
            <div class="gate-weather-meta">
              <span>FEELS <b data-gate-weather-feels>--°</b></span>
              <span>WIND <b data-gate-weather-wind>--</b></span>
            </div>
          </div>

          <div class="gate-weather-days" data-gate-weather-days></div>

          <div class="gate-weather-footer">
            <span data-gate-weather-updated>NOT SYNCED</span>
            <button type="button" data-gate-locate>RELOCATE</button>
          </div>
        </div>
      </section>
      {% endif %}

      <section class="gate-panel gate-routes-panel" aria-labelledby="gate-routes-title" data-gate-module="active_systems" data-gate-layout-id="active_systems">
        <div class="gate-section-heading">
          <div>
            <span class="gate-section-index" data-gate-layout-index="active_systems">04</span>
            <div>
              <p id="gate-routes-title">
                <span class="theme-copy-night">ACTIVE SYSTEMS</span>
                <span class="theme-copy-day">REFERENCE ROOMS</span>
              </p>
              <span>
                <span class="theme-copy-night">Internal facility vectors.</span>
                <span class="theme-copy-day">Neutriverse 内部入口。</span>
              </span>
            </div>
          </div>
        </div>

        <div class="gate-route-list">
          {% for route in gate.routes %}
            {% assign external = false %}
            {% if route.url contains '://' %}
              {% assign external = true %}
            {% endif %}
            <a
              class="gate-route"
              href="{% if external %}{{ route.url }}{% else %}{{ route.url | relative_url }}{% endif %}"
              data-gate-route
              data-gate-transit-label="{{ route.label }}"
              data-gate-transit-detail="{{ route.detail }}"
            >
              <span class="gate-status-dot"></span>
              <span>
                <strong>{{ route.label }}</strong>
                <small>{{ route.detail }}</small>
              </span>
              <span class="gate-route-state">NOMINAL</span>
            </a>
          {% endfor %}
        </div>
      </section>
    <section class="gate-panel gate-note-panel gate-note-wide" aria-labelledby="gate-note-title" data-gate-module="field_record" data-gate-layout-id="field_record">
      <div class="gate-section-heading">
        <div>
          <span class="gate-section-index" data-gate-layout-index="field_record">05</span>
          <div>
            <p id="gate-note-title">
              <span class="theme-copy-night">FIELD RECORD</span>
              <span class="theme-copy-day">MARGIN NOTES</span>
            </p>
            <span>
              <span class="theme-copy-night">Local transient memory.</span>
              <span class="theme-copy-day">仅保存在当前浏览器。</span>
            </span>
          </div>
        </div>
      </div>

      <textarea
        data-gate-note
        aria-label="Quick note"
        placeholder="> Record something before transit…"
      ></textarea>

      <div class="gate-note-meta">
        <span>LOCAL STORAGE</span>
        <span data-gate-note-status>EMPTY</span>
      </div>
    </section>

    </div>

    <footer class="gate-footer">
      <span>NEUTRIVERSE // GATE NODE 01</span>
      <span>
        <span class="gate-status-dot"></span>
        SYSTEM NOMINAL
      </span>
    </footer>
  </main>

  <div class="gate-settings-backdrop" data-gate-settings-backdrop hidden></div>

  <aside
    class="gate-settings-drawer"
    data-gate-settings-drawer
    role="dialog"
    aria-modal="true"
    aria-labelledby="gate-settings-title"
    hidden
  >
    <header class="gate-settings-header">
      <div>
        <p>NEUTRIVERSE // GATE</p>
        <h2 id="gate-settings-title">SYSTEM CONFIGURATION</h2>
      </div>

      <button
        class="gate-settings-close"
        type="button"
        data-gate-settings-close
        aria-label="关闭 Gate 设置"
      >
        <span aria-hidden="true">×</span>
      </button>
    </header>

    <div class="gate-settings-scroll">
      <section class="gate-settings-section" aria-labelledby="gate-settings-query">
        <div class="gate-settings-section-title">
          <span>01</span>
          <div>
            <h3 id="gate-settings-query">QUERY ARRAY</h3>
            <p>检索入口与默认行为。</p>
          </div>
        </div>

        <label class="gate-setting-field">
          <span>DEFAULT SEARCH</span>
          <select data-gate-setting-search>
            {% for engine in gate.search_engines %}
              <option value="{{ engine[0] }}">{{ engine[1].label }}</option>
            {% endfor %}
          </select>
        </label>
      </section>

      <section class="gate-settings-section" aria-labelledby="gate-settings-interface">
        <div class="gate-settings-section-title">
          <span>02</span>
          <div>
            <h3 id="gate-settings-interface">INTERFACE</h3>
            <p>调整信息密度与环境图形。</p>
          </div>
        </div>

        <label class="gate-setting-field">
          <span>DENSITY</span>
          <select data-gate-setting-density>
            <option value="standard">STANDARD</option>
            <option value="compact">COMPACT</option>
          </select>
        </label>

        <label class="gate-setting-field gate-setting-field-spaced">
          <span>PRESENTATION</span>
          <select data-gate-setting-presentation>
            <option value="dashboard">DASHBOARD</option>
            <option value="focus">FOCUS</option>
          </select>
        </label>

        <label class="gate-setting-switch">
          <span>
            <strong>AMBIENT GRAPHICS</strong>
            <small>轨道、星点与档案网格背景。</small>
          </span>
          <input type="checkbox" data-gate-setting-ambient>
          <i aria-hidden="true"></i>
        </label>
      </section>

      <section class="gate-settings-section" aria-labelledby="gate-settings-modules">
        <div class="gate-settings-section-title">
          <span>03</span>
          <div>
            <h3 id="gate-settings-modules">MODULES</h3>
            <p>核心 Clock 与 Query Array 始终保留。</p>
          </div>
        </div>

        <div class="gate-settings-switch-list">
          <label class="gate-setting-switch">
            <span><strong>LAUNCH ROUTES</strong><small>常用站点快速入口。</small></span>
            <input type="checkbox" data-gate-setting-module="launch_routes">
            <i aria-hidden="true"></i>
          </label>

          <label class="gate-setting-switch">
            <span><strong>CONTEXT ROUTES</strong><small>WORK / KNOWLEDGE / MEDIA / SYSTEM。</small></span>
            <input type="checkbox" data-gate-setting-module="context_routes">
            <i aria-hidden="true"></i>
          </label>

          <label class="gate-setting-switch">
            <span><strong>CURRENT VECTOR</strong><small>当前工作路径。</small></span>
            <input type="checkbox" data-gate-setting-module="current_vector">
            <i aria-hidden="true"></i>
          </label>

          <label class="gate-setting-switch">
            <span><strong>LOCAL CONDITIONS</strong><small>浏览器本地天气。</small></span>
            <input type="checkbox" data-gate-setting-module="local_conditions">
            <i aria-hidden="true"></i>
          </label>

          <label class="gate-setting-switch">
            <span><strong>ACTIVE SYSTEMS</strong><small>Neutriverse 内部入口。</small></span>
            <input type="checkbox" data-gate-setting-module="active_systems">
            <i aria-hidden="true"></i>
          </label>

          <label class="gate-setting-switch">
            <span><strong>FIELD RECORD</strong><small>浏览器本地临时记录。</small></span>
            <input type="checkbox" data-gate-setting-module="field_record">
            <i aria-hidden="true"></i>
          </label>

          <label class="gate-setting-switch">
            <span><strong>RECENT TRANSITS</strong><small>在 Query Array 中显示最近入口。</small></span>
            <input type="checkbox" data-gate-setting-module="recent_transits">
            <i aria-hidden="true"></i>
          </label>
        </div>
      </section>

      <section class="gate-settings-section" aria-labelledby="gate-settings-launch">
        <div class="gate-settings-section-title">
          <span>04</span>
          <div>
            <h3 id="gate-settings-launch">LAUNCH ROUTES</h3>
            <p>管理默认入口与浏览器本地的自定义入口。</p>
          </div>
        </div>

        <div class="gate-launch-settings" data-gate-launch-settings></div>

        <div class="gate-custom-create">
          <div class="gate-custom-create-head">
            <span>CUSTOM QUICK LAUNCH</span>
            <small data-gate-custom-launch-count>0 / 8</small>
          </div>

          <div class="gate-custom-create-fields">
            <label>
              <span>LABEL</span>
              <input type="text" maxlength="40" placeholder="Vercel" data-gate-custom-launch-label>
            </label>
            <label>
              <span>ROLE</span>
              <input type="text" maxlength="40" placeholder="DEPLOY" data-gate-custom-launch-role>
            </label>
            <label class="gate-custom-create-wide">
              <span>URL</span>
              <input type="url" maxlength="500" placeholder="https://vercel.com/" data-gate-custom-launch-url>
            </label>
          </div>

          <button class="gate-settings-primary" type="button" data-gate-add-custom-launch>
            ADD QUICK LAUNCH
          </button>
        </div>
      </section>

      <section class="gate-settings-section" aria-labelledby="gate-settings-context">
        <div class="gate-settings-section-title">
          <span>05</span>
          <div>
            <h3 id="gate-settings-context">CONTEXT ROUTES</h3>
            <p>选择 Gate 打开时默认显示的 Route Matrix。</p>
          </div>
        </div>

        <label class="gate-setting-field">
          <span>DEFAULT GROUP</span>
          <select data-gate-setting-route-group>
            {% for group in gate.route_groups %}
              <option value="{{ group.id }}">{{ group.label }} · {{ group.detail }}</option>
            {% endfor %}
          </select>
        </label>

        <div class="gate-custom-create gate-custom-group-create">
          <div class="gate-custom-create-head">
            <span>CUSTOM ROUTE GROUP</span>
            <small data-gate-custom-group-count>0 / 4</small>
          </div>

          <div class="gate-custom-create-fields">
            <label>
              <span>LABEL</span>
              <input type="text" maxlength="24" placeholder="RESEARCH" data-gate-custom-group-label>
            </label>
            <label>
              <span>DETAIL</span>
              <input type="text" maxlength="40" placeholder="DATA / PAPERS" data-gate-custom-group-detail>
            </label>
          </div>

          <button class="gate-settings-primary" type="button" data-gate-add-custom-group>
            ADD ROUTE GROUP
          </button>

          <div class="gate-custom-group-list" data-gate-custom-group-list></div>
        </div>

        <div class="gate-route-editor">
          <div class="gate-route-editor-head">
            <span>LOCAL ROUTE OVERRIDES</span>
            <button type="button" data-gate-route-reset-group>RESET GROUP</button>
          </div>

          <label class="gate-setting-field">
            <span>EDIT GROUP</span>
            <select data-gate-route-edit-group>
              {% for group in gate.route_groups %}
                <option value="{{ group.id }}">{{ group.label }}</option>
              {% endfor %}
            </select>
          </label>

          <div class="gate-route-editor-list" data-gate-route-editor-list></div>

          <button class="gate-settings-primary" type="button" data-gate-route-save-group>
            SAVE GROUP
          </button>
        </div>
      </section>

      <section class="gate-settings-section" aria-labelledby="gate-settings-layout">
        <div class="gate-settings-section-title">
          <span>06</span>
          <div>
            <h3 id="gate-settings-layout">DASHBOARD ORDER</h3>
            <p>调整下方状态模块的排列顺序。</p>
          </div>
        </div>

        <div class="gate-dashboard-settings" data-gate-dashboard-settings></div>
        <p class="gate-settings-footnote">
          STANDARD 保持单列；WIDE 跨两列；FIELD RECORD 固定为 FULL。
        </p>
      </section>

      <section class="gate-settings-section" aria-labelledby="gate-settings-transfer">
        <div class="gate-settings-section-title">
          <span>07</span>
          <div>
            <h3 id="gate-settings-transfer">CONFIGURATION TRANSFER</h3>
            <p>在不同浏览器间迁移 Gate 配置，不包含天气坐标、浏览记录或 Field Record。</p>
          </div>
        </div>

        <div class="gate-config-transfer">
          <button type="button" data-gate-export-config>EXPORT CONFIG</button>
          <button type="button" data-gate-import-config>IMPORT CONFIG</button>
          <input
            type="file"
            accept="application/json,.json"
            data-gate-import-file
            hidden
          >
        </div>
      </section>

      <section class="gate-settings-section" aria-labelledby="gate-settings-diagnostics">
        <div class="gate-settings-section-title">
          <span>08</span>
          <div>
            <h3 id="gate-settings-diagnostics">CONFIG DIAGNOSTICS</h3>
            <p>检查本地配置冲突、无效 URL、重复 ID 与旧数据残留。</p>
          </div>
        </div>

        <div class="gate-diagnostics" data-gate-diagnostics>
          <div class="gate-diagnostics-summary">
            <span class="gate-status-dot" data-gate-diagnostics-dot></span>
            <strong data-gate-diagnostics-summary>NOT CHECKED</strong>
          </div>
          <div class="gate-diagnostics-list" data-gate-diagnostics-list></div>
          <div class="gate-diagnostics-actions">
            <button type="button" data-gate-run-diagnostics>RUN DIAGNOSTICS</button>
            <button type="button" data-gate-repair-config>REPAIR CONFIG</button>
          </div>
        </div>
      </section>

      <section class="gate-settings-section" aria-labelledby="gate-settings-storage">
        <div class="gate-settings-section-title">
          <span>09</span>
          <div>
            <h3 id="gate-settings-storage">LOCAL STORAGE</h3>
            <p>这些操作只影响当前浏览器。</p>
          </div>
        </div>

        <div class="gate-storage-actions">
          <button type="button" data-gate-clear-recent>CLEAR RECENT</button>
          <button type="button" data-gate-clear-weather>CLEAR WEATHER</button>
          <button type="button" data-gate-reset-vector>RESET VECTOR</button>
          <button type="button" data-gate-clear-note>CLEAR FIELD RECORD</button>
        </div>
      </section>
    </div>

    <footer class="gate-settings-footer">
      <span data-gate-settings-status>LOCAL CONFIGURATION</span>
      <button type="button" data-gate-reset-settings>RESET GATE</button>
    </footer>
  </aside>

  <script type="application/json" id="gate-search-config">
    {{ gate.search_engines | jsonify }}
  </script>

  <script type="application/json" id="gate-vector-config">
    {{ gate.current_vector | jsonify }}
  </script>

  <script type="application/json" id="gate-settings-config">
    {{ gate.settings_defaults | jsonify }}
  </script>

  <script type="application/json" id="gate-route-groups-config">
    {{ gate.route_groups | jsonify }}
  </script>
</div>
