---
# the default layout is 'page'
title: 中间层漫游指南
icon: fas fa-info-circle
order: 5
excerpt_separator: <!-- about-excerpt-end -->
---

<div class="nv-about-entry" data-neutriverse-section="about">
  {% include neutriverse-section-identity.html current='about' %}
  {% include neutriverse-primary-nav.html current='about' %}
  {% include neutriverse-section-links.html current='about' %}
</div>

{% include neutriverse-about-profile.html %}

  {% comment %}
  GEO MEMORY PANEL SWITCH
  Set travel_globe_enabled to false to hide the entire globe panel while keeping the code/data in place.
  {% endcomment %}
  {% assign travel_globe_enabled = false %}

  {% if travel_globe_enabled %}
  {% assign travel_regions = site.data.travel_regions %}
  {% assign travel_boundary_sources = site.data.travel_boundary_sources %}
  <section class="about-travel-panel" aria-labelledby="travel-globe-title" data-travel-globe-root>
    <script type="application/json" data-travel-region-data>{{ travel_regions | jsonify }}</script>
    <script type="application/json" data-travel-boundary-sources>{{ travel_boundary_sources | jsonify }}</script>

    <div class="about-travel-header">
      <div>
        <span class="about-stack-kicker">GEO MEMORY REGISTER</span>
        <h3 id="travel-globe-title">中间出游记录</h3>
        <p class="about-travel-note" id="travel-globe-note">记录出游历史</p>
      </div>
    </div>

    <div class="travel-globe-shell">
      <div class="travel-globe-placeholder" aria-hidden="true"><span></span></div>
      <canvas
        class="travel-globe-canvas"
        data-travel-globe-canvas
        aria-label="旋转地理记忆球"
        aria-describedby="travel-globe-note"
        tabindex="0"
      ></canvas>
      <div class="travel-globe-reticle" aria-hidden="true">
        <span class="travel-globe-corner is-north-west"></span>
        <span class="travel-globe-corner is-north-east"></span>
        <span class="travel-globe-corner is-south-east"></span>
        <span class="travel-globe-corner is-south-west"></span>
        <span class="travel-globe-reticle-center"></span>
      </div>
      <div class="travel-boundary-status" data-travel-boundary-status aria-live="polite">
        <span data-travel-boundary-message>边界层载入中</span>
        <button type="button" data-travel-boundary-retry hidden>重新载入</button>
      </div>
    </div>

    <div
      class="travel-globe-dossier is-empty"
      data-travel-globe-dossier
      role="status"
      aria-live="polite"
      aria-atomic="true"
    >
      <div class="travel-dossier-primary">
        <span class="travel-dossier-kicker" data-travel-tooltip-mode>GEO MEMORY RECORD</span>
        <strong data-travel-tooltip-name>未选择记录</strong>
        <div class="travel-dossier-meta">
          <span data-travel-tooltip-region hidden></span>
          <em data-travel-tooltip-status hidden></em>
        </div>
      </div>
      <dl class="travel-dossier-fields" data-travel-dossier-fields hidden>
        <div data-travel-tooltip-dates-row hidden>
          <dt>VISITED</dt>
          <dd data-travel-tooltip-dates></dd>
        </div>
        <div data-travel-tooltip-places-row hidden>
          <dt>PLACES</dt>
          <dd data-travel-tooltip-places></dd>
        </div>
      </dl>
      <p class="travel-dossier-note" data-travel-tooltip-note hidden></p>
    </div>

    <div class="travel-source-note" aria-label="边界数据来源">
      <span>边界数据来源</span>
      <div class="travel-source-links">
        {% for source in travel_boundary_sources %}
          {% if source.enabled and source.reference_hidden != true %}
            <a href="{{ source.source_url }}" target="_blank" rel="noopener noreferrer">{{ source.reference_name | default: source.name }}：{{ source.source_name }}</a>
          {% endif %}
        {% endfor %}
      </div>
    </div>
  </section>
  {% endif %}

{% if travel_globe_enabled %}
<script type="module" src="{{ '/assets/js/travel-globe.js' | relative_url }}?v={{ site.github.build_revision | default: 'local' }}-{{ site.time | date: '%Y%m%d%H%M%S' }}"></script>
{% endif %}

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<p id="middle-layer-countdown" class="about-countdown">剩余--年--月--日--时--分--秒</p>

<script>
  (() => {
    const target = document.getElementById('middle-layer-countdown');

    if (!target) {
      return;
    }

    const targetDate = new Date('2039-09-15T20:00:00+08:00');

    const addYears = (date, years) => {
      const next = new Date(date);
      next.setFullYear(next.getFullYear() + years);
      return next;
    };

    const addMonths = (date, months) => {
      const next = new Date(date);
      next.setMonth(next.getMonth() + months);
      return next;
    };

    const diffParts = (from, to) => {
      if (from >= to) {
        return { years: 0, months: 0, days: 0, hours: 0, minutes: 0, seconds: 0 };
      }

      let cursor = new Date(from);
      let years = 0;
      let months = 0;

      while (addYears(cursor, 1) <= to) {
        cursor = addYears(cursor, 1);
        years += 1;
      }

      while (addMonths(cursor, 1) <= to) {
        cursor = addMonths(cursor, 1);
        months += 1;
      }

      let remainingMs = to - cursor;
      const dayMs = 24 * 60 * 60 * 1000;
      const hourMs = 60 * 60 * 1000;
      const minuteMs = 60 * 1000;

      const days = Math.floor(remainingMs / dayMs);
      remainingMs -= days * dayMs;
      const hours = Math.floor(remainingMs / hourMs);
      remainingMs -= hours * hourMs;
      const minutes = Math.floor(remainingMs / minuteMs);
      remainingMs -= minutes * minuteMs;
      const seconds = Math.floor(remainingMs / 1000);

      return { years, months, days, hours, minutes, seconds };
    };

    const render = () => {
      const parts = diffParts(new Date(), targetDate);
      target.textContent = `剩余${parts.years}年${parts.months}月${parts.days}日${parts.hours}时${parts.minutes}分${parts.seconds}秒`;
    };

    render();
    window.setInterval(render, 1000);
  })();
</script>
