(() => {
  const catalog = document.querySelector('[data-project-catalog]');
  if (!catalog) return;

  const cards = [...catalog.querySelectorAll('[data-project-card]')];
  const filters = [...catalog.querySelectorAll('[data-project-filter]')];
  const count = catalog.querySelector('[data-project-visible-count]');
  const empty = catalog.querySelector('[data-project-filter-empty]');
  const valid = new Set(filters.map((button) => button.dataset.projectFilter));

  const normalize = (value) => valid.has(value) ? value : 'all';

  const apply = (requested, historyMode = null) => {
    const status = normalize(requested);
    let visible = 0;

    cards.forEach((card) => {
      const matches = status === 'all' || card.dataset.projectStatus === status;
      card.hidden = !matches;
      if (matches) visible += 1;
    });

    filters.forEach((button) => {
      button.setAttribute(
        'aria-pressed',
        String(button.dataset.projectFilter === status)
      );
    });

    if (count) count.textContent = String(visible);
    if (empty) empty.hidden = visible !== 0;
    catalog.dataset.projectFilterCurrent = status;

    if (historyMode) {
      const url = new URL(window.location.href);
      if (status === 'all') url.searchParams.delete('status');
      else url.searchParams.set('status', status);
      window.history[historyMode]({ status }, '', url);
    }
  };

  filters.forEach((button) => {
    button.addEventListener('click', () => {
      apply(button.dataset.projectFilter, 'pushState');
    });
  });

  window.addEventListener('popstate', () => {
    const value = new URL(window.location.href).searchParams.get('status') || 'all';
    apply(value);
  });

  const initialUrl = new URL(window.location.href);
  const requested = initialUrl.searchParams.get('status') || 'all';
  const initial = normalize(requested);
  apply(initial);

  if (initial !== requested) {
    initialUrl.searchParams.delete('status');
    window.history.replaceState({ status: 'all' }, '', initialUrl);
  } else {
    window.history.replaceState({ status: initial }, '', initialUrl);
  }

  catalog.dataset.projectFilterReady = 'true';
})();
