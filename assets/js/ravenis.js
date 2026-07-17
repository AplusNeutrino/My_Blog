(() => {
  'use strict';

  const PAGE_SIZE = 20;
  const MAX_MATCHES = 200;
  const TYPE_LABELS = {
    news: '新闻',
    event_cluster: '事件簇',
    ai_digest: 'AI Digest',
    rss: 'RSS',
    hotlist: '热榜'
  };
  const SLOT_LABELS = { A: '早间', B: '午间', C: '晚间', DIGEST: 'AI Digest' };
  const STATUS_LABELS = {
    new: '本周新增',
    reinforced: '持续增强',
    stable: '保持稳定',
    cooled: '明显降温'
  };

  function resolveSignalTitle(item, records) {
    const evidenceIds = new Set([
      item?.id,
      ...(Array.isArray(item?.evidence_ids) ? item.evidence_ids : [])
    ].filter(Boolean));
    const evidence = (Array.isArray(records) ? records : [])
      .find((record) => evidenceIds.has(record.id) && record.title);
    return evidence?.title || item?.headline || '未命名信号';
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { resolveSignalTitle };
  }

  const app = typeof document === 'undefined' ? null : document.getElementById('ravenis-app');
  if (!app) return;

  const $ = (id) => document.getElementById(id);
  const ui = {
    form: $('ravenis-search'),
    q: $('ravenis-q'),
    date: $('ravenis-target-date'),
    from: $('ravenis-from'),
    to: $('ravenis-to'),
    slot: $('ravenis-slot'),
    category: $('ravenis-category'),
    source: $('ravenis-source'),
    type: $('ravenis-type'),
    sort: $('ravenis-sort'),
    reset: $('ravenis-reset'),
    retry: $('ravenis-retry'),
    loading: $('ravenis-loading'),
    content: $('ravenis-content'),
    error: $('ravenis-error'),
    errorMessage: $('ravenis-error-message'),
    overview: $('ravenis-overview'),
    dateLabel: $('ravenis-date'),
    freshness: $('ravenis-freshness'),
    topSection: $('ravenis-top-section'),
    topHeading: $('ravenis-top-heading'),
    topItems: $('ravenis-top-items'),
    watchSection: $('ravenis-watch-section'),
    watchHeading: $('ravenis-watch-heading'),
    watchlist: $('ravenis-watchlist'),
    categorySection: $('ravenis-category-section'),
    categoryHeading: $('ravenis-category-heading'),
    categories: $('ravenis-categories'),
    recordHeading: $('ravenis-record-heading'),
    records: $('ravenis-records'),
    count: $('ravenis-result-count'),
    pagination: $('ravenis-pagination'),
    filterCount: $('ravenis-filter-count'),
    dailyLink: $('ravenis-daily-link'),
    weeklyLink: $('ravenis-weekly-link')
  };

  const params = new URLSearchParams(window.location.search);
  const state = {
    view: params.get('view') === 'weekly' ? 'weekly' : 'daily',
    q: params.get('q') || '',
    date: params.get('date') || '',
    from: params.get('from') || '',
    to: params.get('to') || '',
    slot: (params.get('slot') || '').toUpperCase(),
    category: params.get('category') || '',
    source: params.get('source') || '',
    type: params.get('type') || '',
    sort: params.get('sort') === 'first' ? 'first' : 'latest',
    page: Math.max(1, Number.parseInt(params.get('page') || '1', 10) || 1)
  };
  const cache = { manifest: null, day: null, dayDate: '', index: null };
  const baseUrl = new URL(app.dataset.baseUrl || '/ravenis/data/', window.location.origin);

  function escapeHTML(value) {
    return String(value ?? '').replace(/[&<>'"]/g, (char) => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
    }[char]));
  }

  function normalize(value) {
    const text = String(value ?? '');
    try {
      return text.normalize('NFKC').toLocaleLowerCase('zh-CN').replace(/\s+/g, ' ').trim();
    } catch {
      return text.toLowerCase().replace(/\s+/g, ' ').trim();
    }
  }

  function safeHttpUrl(value) {
    try {
      const url = new URL(String(value || ''));
      return ['http:', 'https:'].includes(url.protocol) ? url.href : '';
    } catch {
      return '';
    }
  }

  function dataUrl(path) {
    if (!/^(?:manifest|search-index)\.json$|^days\/\d{4}-\d{2}-\d{2}\.json$|^weekly\/latest\.json$/.test(path)) {
      throw new Error('数据路径未通过安全校验。');
    }
    return new URL(path, baseUrl).href;
  }

  async function fetchJSON(path) {
    const response = await fetch(dataUrl(path), { credentials: 'same-origin' });
    if (!response.ok) throw new Error(`公开数据读取失败（HTTP ${response.status}）。`);
    return response.json();
  }

  async function fetchSearchIndex() {
    if (cache.index) return cache.index;
    const meta = cache.manifest?.search;
    if (!meta?.path) throw new Error('当前发布包没有历史搜索索引。');
    const response = await fetch(dataUrl(meta.path), { credentials: 'same-origin' });
    if (!response.ok) throw new Error(`历史索引读取失败（HTTP ${response.status}）。`);
    const buffer = await response.arrayBuffer();
    if (meta.sha256 && window.crypto?.subtle) {
      const hash = await window.crypto.subtle.digest('SHA-256', buffer);
      const actual = [...new Uint8Array(hash)].map((byte) => byte.toString(16).padStart(2, '0')).join('');
      if (actual !== meta.sha256) throw new Error('历史索引哈希不匹配，已拒绝显示。');
    }
    const payload = JSON.parse(new TextDecoder().decode(buffer));
    if (!Array.isArray(payload.items)) throw new Error('历史索引结构无效。');
    cache.index = payload;
    return payload;
  }

  function formatDate(value) {
    if (!/^\d{4}-\d{2}-\d{2}/.test(value || '')) return value || '—';
    const [year, month, day] = value.slice(0, 10).split('-');
    return `${year}年${Number(month)}月${Number(day)}日`;
  }

  function formatMoment(value) {
    if (!value) return '—';
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return escapeHTML(value);
    return new Intl.DateTimeFormat('zh-CN', {
      month: 'numeric', day: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false
    }).format(date);
  }

  function freshnessLabel(value) {
    const then = new Date(value).getTime();
    if (!Number.isFinite(then)) return '已验证发布';
    const hours = Math.max(0, Math.floor((Date.now() - then) / 36e5));
    if (hours < 1) return '刚刚验证';
    if (hours < 24) return `${hours} 小时前验证`;
    return `${Math.floor(hours / 24)} 天前验证`;
  }

  function setOptions(select, values, selected, allLabel) {
    const options = [`<option value="">${escapeHTML(allLabel)}</option>`];
    [...new Set(values.filter(Boolean))].sort((a, b) => a.localeCompare(b, 'zh-CN')).forEach((value) => {
      options.push(`<option value="${escapeHTML(value)}">${escapeHTML(value)}</option>`);
    });
    select.innerHTML = options.join('');
    select.value = selected;
  }

  function populateFacets(items) {
    setOptions(ui.category, items.map((item) => item.category), state.category, '全部分类');
    setOptions(ui.source, items.map((item) => item.source), state.source, '全部来源');
  }

  function activeSearch() {
    return Boolean(state.q || state.from || state.to || state.category || state.source || state.type);
  }

  function activeFilterCount() {
    return [state.q, state.from, state.to, state.slot, state.category, state.source, state.type]
      .filter(Boolean).length;
  }

  function readControls() {
    state.q = ui.q.value.trim();
    state.date = ui.date.value;
    state.from = ui.from.value;
    state.to = ui.to.value;
    state.slot = ui.slot.value;
    state.category = ui.category.value;
    state.source = ui.source.value;
    state.type = ui.type.value;
    state.sort = ui.sort.value;
    state.page = 1;
  }

  function writeControls() {
    ui.q.value = state.q;
    ui.date.value = state.date;
    ui.from.value = state.from;
    ui.to.value = state.to;
    ui.slot.value = state.slot;
    ui.category.value = state.category;
    ui.source.value = state.source;
    ui.type.value = state.type;
    ui.sort.value = state.sort;
    const count = activeFilterCount();
    ui.filterCount.textContent = count ? `${count} 项` : '';
  }

  function syncUrl({ replace = false } = {}) {
    const next = new URLSearchParams();
    if (state.view === 'weekly') {
      next.set('view', 'weekly');
    } else if (activeSearch()) {
      for (const key of ['q', 'from', 'to', 'slot', 'category', 'source', 'type']) {
        if (state[key]) next.set(key, state[key]);
      }
      if (state.sort !== 'latest') next.set('sort', state.sort);
      if (state.page > 1) next.set('page', String(state.page));
    } else {
      if (state.date) next.set('date', state.date);
      if (state.slot) next.set('slot', state.slot);
      if (state.page > 1) next.set('page', String(state.page));
    }
    const url = `${window.location.pathname}${next.size ? `?${next}` : ''}`;
    window.history[replace ? 'replaceState' : 'pushState']({}, '', url);
  }

  function selectRun(day) {
    const runs = Array.isArray(day.runs) ? day.runs : [];
    const matches = state.slot ? runs.filter((run) => run.slot === state.slot) : runs;
    return [...matches].sort((a, b) => String(b.generated_at).localeCompare(String(a.generated_at)))[0] || null;
  }

  function recordsForRun(day, run) {
    const items = Array.isArray(day.items) ? day.items : [];
    if (!run) return state.slot ? [] : items;
    const ids = new Set(run.record_ids || []);
    return items.filter((item) => ids.has(item.id));
  }

  function sourceEvidence(ids, records) {
    const wanted = new Set(ids || []);
    const sources = records.filter((record) => wanted.has(record.id)).map((record) => record.source).filter(Boolean);
    return [...new Set(sources)].slice(0, 3);
  }

  function signalMarkup(item, index, records) {
    const sources = sourceEvidence(item.evidence_ids, records);
    const title = resolveSignalTitle(item, records);
    const chips = [
      ...sources,
      item.evidence_ids?.length ? `${item.evidence_ids.length} 条证据` : ''
    ].filter(Boolean).map((value) => `<span class="ravenis-chip">${escapeHTML(value)}</span>`).join('');
    return `
      <article class="ravenis-signal">
        <div class="ravenis-signal-number">${String(index + 1).padStart(2, '0')}</div>
        <div>
          <h4>${escapeHTML(title)}</h4>
          <dl>
            <dt>发生</dt><dd>${escapeHTML(item.event || '公开记录出现新的变化。')}</dd>
            <dt>影响</dt><dd>${escapeHTML(item.impact || '影响范围仍需由后续公开证据确认。')}</dd>
            <dt>观察</dt><dd>${escapeHTML(item.watch || '等待新的独立来源或正式数据。')}</dd>
          </dl>
          ${chips ? `<div class="ravenis-evidence">${chips}</div>` : ''}
        </div>
      </article>`;
  }

  function renderTop(summary, records) {
    const items = (summary?.top_items || []).slice(0, 3);
    ui.topSection.hidden = false;
    ui.topItems.innerHTML = items.length
      ? items.map((item, index) => signalMarkup(item, index, records)).join('')
      : '<p class="ravenis-empty-signal">本时段无新增强信号。</p>';
  }

  function renderWatch(summary) {
    const items = (summary?.watchlist || []).slice(0, 3);
    ui.watchSection.hidden = items.length === 0;
    ui.watchlist.innerHTML = items.map((item) => `<li>${escapeHTML(item.text)}</li>`).join('');
  }

  function renderCategories(records) {
    const counts = new Map();
    records.forEach((record) => {
      const key = record.category || '其他';
      counts.set(key, (counts.get(key) || 0) + 1);
    });
    const entries = [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], 'zh-CN'));
    ui.categorySection.hidden = entries.length === 0;
    ui.categories.innerHTML = entries.map(([name, count]) => `
      <div class="ravenis-category"><strong>${escapeHTML(name)}</strong><span>${count.toString().padStart(2, '0')}</span></div>
    `).join('');
  }

  function recordMarkup(record) {
    const url = safeHttpUrl(record.url);
    const type = TYPE_LABELS[record.type] || record.type || '新闻';
    const sourceCount = Math.max(1, Number(record.source_count) || 1);
    const tags = (record.tags || []).slice(0, 4).map((tag) => `<span class="ravenis-chip">${escapeHTML(tag)}</span>`).join('');
    const details = !url && record.summary ? `
      <details><summary>展开公开摘要</summary><p class="ravenis-record-summary">${escapeHTML(record.summary)}</p></details>` : '';
    const action = url ? `<div class="ravenis-record-actions"><a href="${escapeHTML(url)}" target="_blank" rel="noopener noreferrer">访问原文 ↗</a></div>` : '';
    return `
      <article class="ravenis-record">
        <div class="ravenis-record-header">
          <h4>${escapeHTML(record.title || '未命名记录')}</h4>
          <span class="ravenis-record-score" title="综合分数">${Number(record.score) || 0}</span>
        </div>
        <div class="ravenis-record-meta">
          <span>${escapeHTML(record.source || '未知来源')}</span>
          <span>${escapeHTML(type)}</span>
          <span>${sourceCount} 个来源</span>
          <span>首次 ${formatMoment(record.first_seen || record.date)}</span>
          <span>最新 ${formatMoment(record.last_seen || record.date)}</span>
          <span>出现 ${Math.max(1, Number(record.occurrence_count) || 1)} 次</span>
        </div>
        ${url && record.summary ? `<p class="ravenis-record-summary">${escapeHTML(record.summary)}</p>` : ''}
        ${tags ? `<div class="ravenis-evidence">${tags}</div>` : ''}
        ${action}${details}
      </article>`;
  }

  function renderPagination(total) {
    const pages = Math.max(1, Math.ceil(total / PAGE_SIZE));
    state.page = Math.min(state.page, pages);
    if (pages <= 1) {
      ui.pagination.innerHTML = '';
      return;
    }
    const numbers = new Set([1, pages, state.page - 1, state.page, state.page + 1]);
    const buttons = [`<button type="button" data-page="${state.page - 1}" ${state.page === 1 ? 'disabled' : ''} aria-label="上一页">‹</button>`];
    let previous = 0;
    [...numbers].filter((page) => page >= 1 && page <= pages).sort((a, b) => a - b).forEach((page) => {
      if (previous && page > previous + 1) buttons.push('<span aria-hidden="true">…</span>');
      buttons.push(`<button type="button" data-page="${page}" ${page === state.page ? 'aria-current="page"' : ''}>${page}</button>`);
      previous = page;
    });
    buttons.push(`<button type="button" data-page="${state.page + 1}" ${state.page === pages ? 'disabled' : ''} aria-label="下一页">›</button>`);
    ui.pagination.innerHTML = buttons.join('');
  }

  function renderRecords(records, label = '') {
    const total = records.length;
    const start = (state.page - 1) * PAGE_SIZE;
    const visible = records.slice(start, start + PAGE_SIZE);
    ui.records.innerHTML = visible.length
      ? visible.map(recordMarkup).join('')
      : '<p class="ravenis-empty-signal">没有符合当前条件的公开记录。</p>';
    ui.count.textContent = `${label || '共'} ${total} 条${total >= MAX_MATCHES ? ' · 已截取前 200 条' : ''}`;
    renderPagination(total);
  }

  function scoreRecord(record, tokens) {
    if (!tokens.length) return 0;
    const fields = {
      title: normalize(record.title),
      category: normalize(record.category),
      tags: normalize((record.tags || []).join(' ')),
      source: normalize(record.source),
      summary: normalize(record.summary)
    };
    let score = 0;
    for (const token of tokens) {
      const matched = Object.values(fields).some((field) => field.includes(token));
      if (!matched) return -1;
      if (fields.title.includes(token)) score += 8;
      if (fields.category.includes(token)) score += 5;
      if (fields.tags.includes(token)) score += 5;
      if (fields.source.includes(token)) score += 3;
      if (fields.summary.includes(token)) score += 1;
    }
    return score;
  }

  function filterIndex(items) {
    const tokens = normalize(state.q).split(' ').filter(Boolean);
    return items.map((record) => ({ record, relevance: scoreRecord(record, tokens) }))
      .filter(({ record, relevance }) => {
        if (relevance < 0) return false;
        if (state.from && record.date < state.from) return false;
        if (state.to && record.date > state.to) return false;
        if (state.slot && !(record.slots || []).includes(state.slot)) return false;
        if (state.category && record.category !== state.category) return false;
        if (state.source && record.source !== state.source) return false;
        return !(state.type && record.type !== state.type);
      })
      .sort((left, right) => {
        if (tokens.length && right.relevance !== left.relevance) return right.relevance - left.relevance;
        const leftDate = state.sort === 'first' ? (left.record.first_seen || left.record.date) : (left.record.last_seen || left.record.date);
        const rightDate = state.sort === 'first' ? (right.record.first_seen || right.record.date) : (right.record.last_seen || right.record.date);
        return String(rightDate).localeCompare(String(leftDate)) || (Number(right.record.score) - Number(left.record.score));
      })
      .slice(0, MAX_MATCHES)
      .map(({ record }) => record);
  }

  async function renderSearch() {
    setBusy(true);
    try {
      const index = await fetchSearchIndex();
      populateFacets(index.items);
      writeControls();
      const results = filterIndex(index.items);
      ui.overview.textContent = state.q
        ? `“${state.q}” 的公开记录检索结果；标题匹配权重最高。`
        : '最近 30 天公开记录的组合筛选结果。';
      ui.dateLabel.textContent = `${cache.manifest.retention_days || 30} DAY INDEX`;
      ui.topSection.hidden = true;
      ui.watchSection.hidden = true;
      renderCategories(results);
      ui.recordHeading.textContent = '历史检索结果';
      renderRecords(results, '匹配');
      showContent();
    } catch (error) {
      showError(error);
    }
  }

  async function loadDay(date) {
    if (cache.day && cache.dayDate === date) return cache.day;
    const entry = cache.manifest.days.find((day) => day.date === date);
    if (!entry) throw new Error('所选日期没有公开简报。');
    cache.day = await fetchJSON(entry.path);
    cache.dayDate = date;
    return cache.day;
  }

  async function renderDaily() {
    setBusy(true);
    try {
      const day = await loadDay(state.date);
      const run = selectRun(day);
      const records = recordsForRun(day, run);
      const summary = run?.summary || {};
      populateFacets(day.items || []);
      writeControls();
      ui.overview.textContent = summary.overview || `${records.length} 条公开记录；未公开正文和原始 AI 响应。`;
      ui.dateLabel.textContent = `${formatDate(day.date)}${run?.slot ? ` · ${SLOT_LABELS[run.slot] || run.slot}` : ''}`;
      ui.topHeading.textContent = '当日重点';
      ui.watchHeading.textContent = '继续观察';
      ui.categoryHeading.textContent = '分类速览';
      ui.recordHeading.textContent = '完整公开记录';
      renderTop(summary, records);
      renderWatch(summary);
      renderCategories(records);
      const ordered = [...records].sort((a, b) => String(b.last_seen || b.date).localeCompare(String(a.last_seen || a.date)) || Number(b.score) - Number(a.score));
      renderRecords(ordered);
      showContent();
    } catch (error) {
      showError(error);
    }
  }

  function weeklyRecord(theme) {
    return {
      title: theme.headline || theme.name,
      type: 'event_cluster',
      source: `${Number(theme.source_count) || 0} 个公开来源`,
      source_count: Number(theme.source_count) || 1,
      category: theme.category,
      tags: [STATUS_LABELS[theme.status] || theme.status],
      score: theme.max_score,
      first_seen: theme.first_seen,
      last_seen: theme.last_seen,
      occurrence_count: theme.record_count,
      summary: `${theme.impact || ''} ${theme.watch || ''}`.trim(),
      url: ''
    };
  }

  async function renderWeekly() {
    setBusy(true);
    try {
      const digest = await fetchJSON(cache.manifest.weekly?.path || 'weekly/latest.json');
      const themes = Object.values(digest.sections || {}).flat();
      ui.overview.textContent = `${digest.record_count || 0} 条公开记录归纳为 ${digest.theme_count || 0} 条主题；周报不是七份日报的拼接。`;
      ui.dateLabel.textContent = `${formatDate(digest.start_date)} — ${formatDate(digest.end_date)}`;
      ui.topHeading.textContent = '本周主线';
      ui.topSection.hidden = false;
      ui.topItems.innerHTML = (digest.top_themes || []).slice(0, 3).map((theme, index) => signalMarkup({
        headline: theme.headline || theme.name,
        event: `${STATUS_LABELS[theme.status] || theme.status} · ${theme.record_count || 0} 条记录`,
        impact: theme.impact,
        watch: theme.watch,
        evidence_ids: theme.evidence_ids
      }, index, [])).join('') || '<p class="ravenis-empty-signal">本周暂无足够主题信号。</p>';
      ui.watchHeading.textContent = '下周验证信号';
      const watch = (digest.watchlist || []).slice(0, 3);
      ui.watchSection.hidden = watch.length === 0;
      ui.watchlist.innerHTML = watch.map((item) => `<li>${escapeHTML(item)}</li>`).join('');
      ui.categoryHeading.textContent = '主题走势';
      const statusCounts = Object.entries(digest.sections || {}).map(([status, values]) => [STATUS_LABELS[status] || status, values.length]).filter(([, count]) => count);
      ui.categorySection.hidden = statusCounts.length === 0;
      ui.categories.innerHTML = statusCounts.map(([name, count]) => `<div class="ravenis-category"><strong>${escapeHTML(name)}</strong><span>${count.toString().padStart(2, '0')}</span></div>`).join('');
      ui.recordHeading.textContent = '完整主题证据';
      renderRecords(themes.map(weeklyRecord));
      showContent();
    } catch (error) {
      showError(error);
    }
  }

  function setBusy(busy) {
    app.setAttribute('aria-busy', String(busy));
    ui.loading.hidden = !busy;
    if (busy) {
      ui.content.hidden = true;
      ui.error.hidden = true;
    }
  }

  function showContent() {
    setBusy(false);
    ui.error.hidden = true;
    ui.content.hidden = false;
  }

  function showError(error) {
    setBusy(false);
    ui.content.hidden = true;
    ui.error.hidden = false;
    ui.errorMessage.textContent = error?.message || '线上上一版不会被空数据覆盖，请稍后再试。';
  }

  async function renderCurrent() {
    ui.dailyLink.setAttribute('aria-current', state.view === 'daily' ? 'page' : 'false');
    ui.weeklyLink.setAttribute('aria-current', state.view === 'weekly' ? 'page' : 'false');
    if (state.view === 'weekly') return renderWeekly();
    return activeSearch() ? renderSearch() : renderDaily();
  }

  async function initialize() {
    setBusy(true);
    try {
      cache.manifest = await fetchJSON('manifest.json');
      if (!Array.isArray(cache.manifest.days) || !cache.manifest.days.length) {
        throw new Error('已拒绝空的 Ravenis 发布包。');
      }
      const dates = cache.manifest.days.map((day) => day.date).sort();
      const latest = dates[dates.length - 1];
      if (!dates.includes(state.date)) state.date = latest;
      for (const input of [ui.date, ui.from, ui.to]) {
        input.min = dates[0];
        input.max = latest;
      }
      ui.freshness.textContent = freshnessLabel(cache.manifest.generated_at);
      writeControls();
      syncUrl({ replace: true });
      await renderCurrent();
    } catch (error) {
      showError(error);
    }
  }

  ui.form.addEventListener('submit', async (event) => {
    event.preventDefault();
    readControls();
    syncUrl();
    await renderCurrent();
  });

  ui.date.addEventListener('change', async () => {
    state.date = ui.date.value;
    state.page = 1;
    if (!activeSearch() && state.view === 'daily') {
      syncUrl();
      await renderDaily();
    }
  });

  ui.slot.addEventListener('change', async () => {
    state.slot = ui.slot.value;
    state.page = 1;
    if (!activeSearch() && state.view === 'daily') {
      syncUrl();
      await renderDaily();
    }
  });

  ui.reset.addEventListener('click', async () => {
    Object.assign(state, { q: '', from: '', to: '', slot: '', category: '', source: '', type: '', sort: 'latest', page: 1 });
    writeControls();
    syncUrl();
    await renderDaily();
  });

  ui.retry.addEventListener('click', initialize);

  ui.pagination.addEventListener('click', async (event) => {
    const button = event.target.closest('button[data-page]');
    if (!button || button.disabled) return;
    state.page = Math.max(1, Number(button.dataset.page) || 1);
    syncUrl();
    await renderCurrent();
    ui.recordHeading.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  });

  window.addEventListener('popstate', () => window.location.reload());
  initialize();
})();
