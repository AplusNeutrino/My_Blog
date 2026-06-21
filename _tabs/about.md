---
# the default layout is 'page'
title: 中间层漫游指南
icon: fas fa-info-circle
order: 5
excerpt_separator: <!-- about-excerpt-end -->
---

{% comment %}
============================================================
ABOUT PAGE TEXT CONFIG
以后更新 About / Now 页面，只需要改这里的文字。

status_items、roadmap_items 和 signal_items 的格式：
标签|内容||标签|内容
每一组用两个竖线 || 分隔，标签和内容之间用一个竖线 | 分隔。
============================================================
{% endcomment %}
{% assign about_info_kicker = 'NEUTRIVERSE INFO' %}
{% capture about_info_text %}本站是 Neutrino 的个人文字站。
主要用于存储笔记、读后感和记忆碎片。
<span class="nv-blue"><strong>欢迎所有的你。</strong></span>{% endcapture %}

{% assign about_now_kicker = 'PERSONAL ORBIT' %}
{% assign about_now_title = 'Neutrino状态监控' %}
{% capture about_now_summary %}最近在迁移整理近五年散落在各个软件中的笔记资料。
本人正在绝赞求职中。{% endcapture %}
{% assign about_now_updated = '更新于 2026-05-05' %}
{% assign signal_items = 'focus|中间层维护||load|63%||mode|quiet build||sync|2026-05-05' | split: '||' %}
{% assign status_items = '学|CS技能复健||写|修订整理笔记||做|前往面试！||态|我将结束这一切' | split: '||' %}
{% assign roadmap_items = '现在|面经持续背诵中||接下来|CS专业知识复健||稍后|读书《洛丽塔》' | split: '||' %}
{% assign reading_stack_items = '《迷雾之子》|2026/05/02||《大师与玛格丽特》|2025/12/25||《阿特拉斯耸耸肩》|2025/11/21||《无限近似于青色的蓝》|2025/04/03||《诺瓦利斯作品选集》|2026/02/06||《洛丽塔》|1970/01/02||待记录|----/--/--||待记录|----/--/--' | split: '||' %}
{% assign visual_stack_items = '《纽约提喻法》|2025/03/05||《Amadeus》|2025/04/04||《挽救计划》|2026/03/23||《全金属外壳》|2026/01/26||《斯巴达克斯》|2026/01/26||待记录|----/--/--||待记录|----/--/--||待记录|----/--/--' | split: '||' %}

<section class="about-profile" aria-labelledby="about-info-title">
  <div class="about-info">
    <span class="about-section-kicker">{{ about_info_kicker }}</span>
    <p id="about-info-title" class="about-info-text">{{ about_info_text | newline_to_br }}</p>
  </div>

  <div class="about-now" aria-labelledby="about-now-title">
    <div class="about-now-main">
      <span class="about-section-kicker">{{ about_now_kicker }}</span>
      <h2 id="about-now-title">{{ about_now_title }}</h2>
      <p class="about-now-summary">{{ about_now_summary | newline_to_br }}</p>
    </div>

    <div class="about-instruments" aria-label="当前信号">
      <div class="about-gauge-row" aria-hidden="true">
        <div class="about-scan">
          <span></span>
        </div>

        <div class="about-bars">
          <span></span>
          <span></span>
          <span></span>
        </div>

        <div class="about-monitor">
          <span></span>
          <i></i>
          <b></b>
        </div>
      </div>

      <div class="about-signal">
        <span class="about-signal-title">SIGNAL</span>
        {% for item in signal_items %}
          {% assign signal = item | split: '|' %}
          <div class="about-signal-row">
            <span>{{ signal[0] }}</span>
            <strong>{{ signal[1] }}</strong>
          </div>
        {% endfor %}
      </div>
    </div>

    <div class="about-now-grid" aria-label="最近状态">
      {% for item in status_items %}
        {% assign status = item | split: '|' %}
        <div class="about-now-item">
          <span>{{ status[0] }}</span>
          <strong>{{ status[1] }}</strong>
        </div>
      {% endfor %}
    </div>

    <span class="about-now-updated">{{ about_now_updated }}</span>
  </div>

  <div class="about-now-roadmap" aria-label="个人路线图">
    {% for item in roadmap_items %}
      {% assign step = item | split: '|' %}
      <div class="about-now-step{% if forloop.first %} is-active{% endif %}">
        <span>{{ step[0] }}</span>
        <strong>{{ step[1] }}</strong>
      </div>
    {% endfor %}
  </div>

  <div class="about-stacks" aria-label="阅读与影像监控栈">
    <section class="about-stack-panel" aria-labelledby="reading-stack-title">
      <div class="about-stack-header">
        <span class="about-stack-kicker">FUTURE READING STACK</span>
        <h3 id="reading-stack-title">待阅读栈</h3>
      </div>

      <ol class="about-stack-list">
        {% assign reading_stack_sorted = '' | split: '' %}
        {% for item in reading_stack_items %}
          {% assign stack_item = item | split: '|' %}
          {% assign stack_title = stack_item[0] | strip %}
          {% assign stack_date = stack_item[1] | strip %}
          {% unless stack_title == '' or stack_title == '待记录' or stack_date == '' or stack_date contains '----' %}
            {% capture sortable_item %}{{ stack_date }}|{{ stack_title }}{% endcapture %}
            {% assign reading_stack_sorted = reading_stack_sorted | push: sortable_item %}
          {% endunless %}
        {% endfor %}

        {% assign reading_stack_sorted = reading_stack_sorted | sort %}
        {% for item in reading_stack_sorted limit: 8 %}
          {% assign stack_item = item | split: '|' %}
          <li class="about-stack-item">
            <span class="about-stack-index">{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span>
            <strong>{{ stack_item[1] }}</strong>
            <time>{{ stack_item[0] }}</time>
          </li>
        {% endfor %}
      </ol>
    </section>

    <section class="about-stack-panel" aria-labelledby="visual-stack-title">
      <div class="about-stack-header">
        <span class="about-stack-kicker">FUTURE MEDIA STACK</span>
        <h3 id="visual-stack-title">待观看栈</h3>
      </div>

      <ol class="about-stack-list">
        {% assign visual_stack_sorted = '' | split: '' %}
        {% for item in visual_stack_items %}
          {% assign stack_item = item | split: '|' %}
          {% assign stack_title = stack_item[0] | strip %}
          {% assign stack_date = stack_item[1] | strip %}
          {% unless stack_title == '' or stack_title == '待记录' or stack_date == '' or stack_date contains '----' %}
            {% capture sortable_item %}{{ stack_date }}|{{ stack_title }}{% endcapture %}
            {% assign visual_stack_sorted = visual_stack_sorted | push: sortable_item %}
          {% endunless %}
        {% endfor %}

        {% assign visual_stack_sorted = visual_stack_sorted | sort %}
        {% for item in visual_stack_sorted limit: 8 %}
          {% assign stack_item = item | split: '|' %}
          <li class="about-stack-item">
            <span class="about-stack-index">{{ forloop.index | prepend: '0' | slice: -2, 2 }}</span>
            <strong>{{ stack_item[1] }}</strong>
            <time>{{ stack_item[0] }}</time>
          </li>
        {% endfor %}
      </ol>
    </section>
  </div>

  {% assign travel_places = site.data.travel_places %}
  {% assign travel_boundary_sources = site.data.travel_boundary_sources %}
  {% assign travel_visited_places = travel_places | where: 'visited', true %}
  {% assign travel_unvisited_places = travel_places | where: 'visited', false %}
  <section class="about-travel-panel" aria-labelledby="travel-globe-title" data-travel-globe-root>
    <script type="application/json" data-travel-globe-data>{{ travel_places | jsonify }}</script>
    <script type="application/json" data-travel-boundary-sources>{{ travel_boundary_sources | jsonify }}</script>

    <div class="about-travel-header">
      <div>
        <span class="about-stack-kicker">GEO MEMORY REGISTER</span>
        <h3 id="travel-globe-title">地理记忆球</h3>
        <p class="about-travel-note">边界层只接入可核验官方来源；中国边界等待自然资源部认可数据后启用。</p>
      </div>

      <div class="about-travel-stats" aria-label="漫游统计">
        <span><strong>{{ travel_visited_places.size }}</strong> 已标注</span>
        <span><strong>{{ travel_unvisited_places.size }}</strong> 未标注</span>
      </div>
    </div>

    <div class="about-travel-grid">
      <div class="travel-globe-shell">
        <canvas class="travel-globe-canvas" data-travel-globe-canvas aria-label="旋转地理记忆球"></canvas>
        <div class="travel-globe-reticle" aria-hidden="true"></div>
        <div class="travel-boundary-status" data-travel-boundary-status>边界层初始化中</div>
        <div class="travel-globe-tooltip" data-travel-globe-tooltip hidden>
          <strong data-travel-tooltip-name></strong>
          <span data-travel-tooltip-region></span>
          <em data-travel-tooltip-status></em>
          <code data-travel-tooltip-coords></code>
        </div>
      </div>

      <div class="travel-ledger" aria-label="地理记忆索引">
        <div class="travel-ledger-section">
          <span class="travel-ledger-label">visited nodes</span>
          <div class="travel-place-cloud">
            {% for place in travel_places %}
              {% if place.visited %}
                <span class="travel-place-chip is-visited" data-travel-place-name="{{ place.name }}">{{ place.name }}</span>
              {% endif %}
            {% endfor %}
          </div>
        </div>

        <div class="travel-ledger-section">
          <span class="travel-ledger-label">outside current route</span>
          <div class="travel-place-cloud">
            {% for place in travel_places %}
              {% unless place.visited %}
                <span class="travel-place-chip" data-travel-place-name="{{ place.name }}">{{ place.name }}</span>
              {% endunless %}
            {% endfor %}
          </div>
        </div>
      </div>
    </div>
  </section>

</section>

<script src="{{ '/assets/js/travel-globe.js' | relative_url }}?v={{ site.github.build_revision | default: site.time | date: '%Y%m%d%H%M%S' }}" defer></script>

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
