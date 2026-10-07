(() => {
  const PARAM_KEYS = ['type', 'topic', 'series', 'sort', 'page'];
  const ALLOWED_TYPES = new Set(['all', 'note', 'essay', 'fragment']);
  const ALLOWED_TOPICS = new Set(['all', 'computation', 'humanity', 'otaku', 'arts']);
  const ALLOWED_SORTS = new Set(['newest', 'oldest']);

  const init = () => {
    const ledger = document.querySelector('[data-writing-ledger]');
    const controls = ledger?.querySelector('[data-writing-controls]');
    const list = ledger?.querySelector('#nv-writing-list');

    if (!ledger || !controls || !list) {
      return;
    }

    const items = Array.from(list.querySelectorAll('[data-writing-item]')).map(
      (element, index) => {
        const record = element.querySelector('[data-writing-record]');
        return {
          element,
          index,
          date: record?.dataset.writingDate || '',
          type: record?.dataset.writingType || '',
          topic: record?.dataset.writingTopic || '',
          series: record?.dataset.writingSeries || ''
        };
      }
    );
    const pageSize = Number.parseInt(ledger.dataset.writingPageSize || '12', 10);
    const typeSelect = controls.elements.type;
    const topicSelect = controls.elements.topic;
    const seriesSelect = controls.elements.series;
    const sortSelect = controls.elements.sort;
    const allowedSeries = new Set(
      Array.from(seriesSelect.options, (option) => option.value)
    );
    const matchCount = ledger.querySelector('[data-writing-match-count]');
    const countLabel = ledger.querySelector('[data-writing-count-label]');
    const status = ledger.querySelector('[data-writing-status]');
    const empty = ledger.querySelector('[data-writing-filter-empty]');
    const pagination = ledger.querySelector('[data-writing-pagination]');
    const pages = ledger.querySelector('[data-writing-pages]');
    const previous = ledger.querySelector('[data-writing-page="previous"]');
    const next = ledger.querySelector('[data-writing-page="next"]');
    const topicBrowser = ledger.querySelector('[data-writing-topic-browser]');
    const topicLinks = Array.from(ledger.querySelectorAll('[data-writing-topic-link]'));
    const seriesBrowser = ledger.querySelector('[data-writing-series-browser]');
    const seriesLinks = Array.from(ledger.querySelectorAll('[data-writing-series-link]'));

    let state = {
      type: 'all',
      topic: 'all',
      series: 'all',
      sort: 'newest',
      page: 1
    };

    const parseState = () => {
      const params = new URLSearchParams(window.location.search);
      const type = params.get('type');
      const topic = params.get('topic');
      const series = params.get('series');
      const sort = params.get('sort');
      const rawPage = Number.parseInt(params.get('page') || '1', 10);

      return {
        type: ALLOWED_TYPES.has(type) ? type : 'all',
        topic: ALLOWED_TOPICS.has(topic) ? topic : 'all',
        series: allowedSeries.has(series) ? series : 'all',
        sort: ALLOWED_SORTS.has(sort) ? sort : 'newest',
        page: Number.isInteger(rawPage) && rawPage > 0 ? rawPage : 1
      };
    };

    const stateUrl = (candidate) => {
      const url = new URL(window.location.href);
      PARAM_KEYS.forEach((key) => url.searchParams.delete(key));

      if (candidate.type !== 'all') {
        url.searchParams.set('type', candidate.type);
      }
      if (candidate.topic !== 'all') {
        url.searchParams.set('topic', candidate.topic);
      }
      if (candidate.series !== 'all') {
        url.searchParams.set('series', candidate.series);
      }
      if (candidate.sort !== 'newest') {
        url.searchParams.set('sort', candidate.sort);
      }
      if (candidate.page > 1) {
        url.searchParams.set('page', String(candidate.page));
      }

      return url.pathname + (url.searchParams.toString() ? '?' + url.searchParams.toString() : '') + url.hash;
    };

    const matchingItems = () =>
      items
        .filter(
          (item) =>
            (state.type === 'all' || item.type === state.type) &&
            (state.topic === 'all' || item.topic === state.topic) &&
            (state.series === 'all' || item.series === state.series)
        )
        .sort((left, right) => {
          const direction = state.sort === 'oldest' ? 1 : -1;
          const dateOrder = left.date.localeCompare(right.date) * direction;
          return dateOrder || left.index - right.index;
        });

    const syncControls = () => {
      typeSelect.value = state.type;
      topicSelect.value = state.topic;
      seriesSelect.value = state.series;
      sortSelect.value = state.sort;
      topicLinks.forEach((link) => {
        const isCurrent = link.dataset.writingTopicLink === state.topic;
        link.classList.toggle('is-current', isCurrent);
        if (isCurrent) {
          link.setAttribute('aria-current', 'true');
        } else {
          link.removeAttribute('aria-current');
        }
      });
      seriesLinks.forEach((link) => {
        const isCurrent = link.dataset.writingSeriesLink === state.series;
        link.classList.toggle('is-current', isCurrent);
        if (isCurrent) {
          link.setAttribute('aria-current', 'true');
        } else {
          link.removeAttribute('aria-current');
        }
      });
    };

    const pageLink = (page, label, current = false) => {
      if (current) {
        const marker = document.createElement('span');
        marker.className = 'is-current';
        marker.setAttribute('aria-current', 'page');
        marker.textContent = label;
        return marker;
      }

      const link = document.createElement('a');
      link.href = stateUrl({ ...state, page });
      link.dataset.writingPageNumber = String(page);
      link.textContent = label;
      link.setAttribute('aria-label', '第 ' + label + ' 页');
      return link;
    };

    const renderPagination = (totalPages) => {
      pages.replaceChildren();
      pagination.hidden = totalPages <= 1;

      if (totalPages <= 1) {
        return;
      }

      previous.hidden = state.page === 1;
      previous.href = stateUrl({ ...state, page: Math.max(1, state.page - 1) });
      previous.dataset.writingPageNumber = String(Math.max(1, state.page - 1));

      next.hidden = state.page === totalPages;
      next.href = stateUrl({ ...state, page: Math.min(totalPages, state.page + 1) });
      next.dataset.writingPageNumber = String(Math.min(totalPages, state.page + 1));

      for (let page = 1; page <= totalPages; page += 1) {
        pages.append(pageLink(page, String(page), page === state.page));
      }
    };

    const render = ({ historyMode = 'replace' } = {}) => {
      const matched = matchingItems();
      const totalPages = Math.max(1, Math.ceil(matched.length / pageSize));
      state.page = Math.min(state.page, totalPages);
      const start = (state.page - 1) * pageSize;
      const visible = matched.slice(start, start + pageSize);

      items.forEach(({ element }) => {
        element.hidden = true;
      });
      matched.forEach(({ element }) => list.append(element));
      visible.forEach(({ element }) => {
        element.hidden = false;
      });

      syncControls();
      matchCount.textContent = String(matched.length);
      countLabel.textContent = matched.length === items.length ? '项公开记录' : '项匹配记录';
      empty.hidden = matched.length !== 0;
      list.hidden = matched.length === 0;

      if (matched.length === 0) {
        status.textContent = '当前条件没有匹配记录';
      } else {
        status.textContent =
          '显示第 ' + (start + 1) + '–' + (start + visible.length) + ' 项，共 ' + matched.length + ' 项';
      }

      ledger.dataset.writingPageCurrent = String(state.page);
      ledger.dataset.writingPageTotal = String(totalPages);
      renderPagination(totalPages);

      const nextUrl = stateUrl(state);
      const currentUrl = window.location.pathname + window.location.search + window.location.hash;
      if (nextUrl !== currentUrl) {
        window.history[historyMode + 'State']({ writing: state }, '', nextUrl);
      }
    };

    const updateFromControls = () => {
      state = {
        type: ALLOWED_TYPES.has(typeSelect.value) ? typeSelect.value : 'all',
        topic: ALLOWED_TOPICS.has(topicSelect.value) ? topicSelect.value : 'all',
        series: allowedSeries.has(seriesSelect.value) ? seriesSelect.value : 'all',
        sort: ALLOWED_SORTS.has(sortSelect.value) ? sortSelect.value : 'newest',
        page: 1
      };
      render({ historyMode: 'push' });
    };

    topicBrowser?.addEventListener('click', (event) => {
      const link = event.target.closest('a[data-writing-topic-link]');
      if (!link || !ALLOWED_TOPICS.has(link.dataset.writingTopicLink)) {
        return;
      }
      event.preventDefault();
      state = {
        type: 'all',
        topic: link.dataset.writingTopicLink,
        series: 'all',
        sort: 'newest',
        page: 1
      };
      render({ historyMode: 'push' });
    });

    seriesBrowser?.addEventListener('click', (event) => {
      const link = event.target.closest('a[data-writing-series-link]');
      if (!link || !allowedSeries.has(link.dataset.writingSeriesLink)) {
        return;
      }
      event.preventDefault();
      state = {
        type: 'all',
        topic: 'all',
        series: link.dataset.writingSeriesLink,
        sort: 'newest',
        page: 1
      };
      render({ historyMode: 'push' });
    });

    controls.addEventListener('change', updateFromControls);
    controls.addEventListener('reset', (event) => {
      event.preventDefault();
      state = { type: 'all', topic: 'all', series: 'all', sort: 'newest', page: 1 };
      render({ historyMode: 'push' });
    });

    pagination.addEventListener('click', (event) => {
      const link = event.target.closest('a[data-writing-page-number]');
      if (!link) {
        return;
      }
      event.preventDefault();
      state.page = Number.parseInt(link.dataset.writingPageNumber || '1', 10);
      render({ historyMode: 'push' });
      ledger.scrollIntoView({ block: 'start', behavior: 'auto' });
    });

    window.addEventListener('popstate', () => {
      state = parseState();
      render({ historyMode: 'replace' });
    });

    controls.hidden = false;
    state = parseState();
    render({ historyMode: 'replace' });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
