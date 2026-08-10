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

    <button class="gate-theme-toggle" type="button" data-gate-theme aria-label="切换主题">
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="4"></circle>
        <path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.66 6.34l1.41-1.41"></path>
      </svg>
    </button>
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

    <section class="gate-launch-section" aria-labelledby="gate-launch-title">
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

    <div class="gate-dashboard-grid">
      {% if gate.current_vector.enabled %}
      <section class="gate-panel gate-vector-panel" aria-labelledby="gate-vector-title" data-gate-vector-panel>
        <div class="gate-section-heading">
          <div>
            <span class="gate-section-index">02</span>
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
      <section class="gate-panel gate-weather-panel" aria-labelledby="gate-weather-title" data-gate-weather-panel>
        <div class="gate-section-heading">
          <div>
            <span class="gate-section-index">03</span>
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

      <section class="gate-panel gate-routes-panel" aria-labelledby="gate-routes-title">
        <div class="gate-section-heading">
          <div>
            <span class="gate-section-index">04</span>
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
    </div>

    <section class="gate-panel gate-note-panel gate-note-wide" aria-labelledby="gate-note-title">
      <div class="gate-section-heading">
        <div>
          <span class="gate-section-index">05</span>
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

    <footer class="gate-footer">
      <span>NEUTRIVERSE // GATE NODE 01</span>
      <span>
        <span class="gate-status-dot"></span>
        SYSTEM NOMINAL
      </span>
    </footer>
  </main>

  <script type="application/json" id="gate-search-config">
    {{ gate.search_engines | jsonify }}
  </script>

  <script type="application/json" id="gate-vector-config">
    {{ gate.current_vector | jsonify }}
  </script>
</div>
