(() => {
  const root = document.documentElement;
  const params = new URLSearchParams(window.location.search);
  const initial = params.get('theme') === 'light' ? 'light' : 'dark';

  const applyTheme = (mode) => {
    root.dataset.mode = mode;
    document.querySelectorAll('[data-theme-choice]').forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.themeChoice === mode));
    });
    const url = new URL(window.location.href);
    url.searchParams.set('theme', mode);
    window.history.replaceState({}, '', url);
  };

  document.querySelectorAll('[data-theme-choice]').forEach((button) => {
    button.addEventListener('click', () => applyTheme(button.dataset.themeChoice));
  });

  applyTheme(initial);

  const dropdowns = Array.from(document.querySelectorAll('.filter-select'));

  const closeDropdown = (details, restoreFocus = false) => {
    details.open = false;
    if (restoreFocus) {
      details.querySelector('summary').focus();
    }
  };

  dropdowns.forEach((details) => {
    const summary = details.querySelector('summary');
    const options = Array.from(details.querySelectorAll('[role="option"]'));
    const input = details.querySelector('input[type="hidden"]');

    summary.addEventListener('keydown', (event) => {
      if (event.key !== 'ArrowDown' && event.key !== 'ArrowUp') {
        return;
      }
      event.preventDefault();
      details.open = true;
      const selected = options.find((option) => option.getAttribute('aria-selected') === 'true') || options[0];
      const target = event.key === 'ArrowUp' ? options[options.length - 1] : selected;
      target?.focus();
    });

    options.forEach((option, index) => {
      option.addEventListener('click', () => {
        options.forEach((item) => item.setAttribute('aria-selected', 'false'));
        option.setAttribute('aria-selected', 'true');
        summary.querySelector('[data-filter-value]').textContent = option.textContent;
        summary.setAttribute('aria-label', `${details.dataset.filterName}：${option.textContent}`);
        input.value = option.dataset.value;
        closeDropdown(details, true);
      });

      option.addEventListener('keydown', (event) => {
        let target;
        if (event.key === 'ArrowDown') target = options[(index + 1) % options.length];
        if (event.key === 'ArrowUp') target = options[(index - 1 + options.length) % options.length];
        if (event.key === 'Home') target = options[0];
        if (event.key === 'End') target = options[options.length - 1];
        if (target) {
          event.preventDefault();
          target.focus();
        }
        if (event.key === 'Escape') {
          event.preventDefault();
          closeDropdown(details, true);
        }
        if (event.key === 'Tab') {
          closeDropdown(details);
        }
      });
    });

    details.addEventListener('toggle', () => {
      summary.setAttribute('aria-expanded', String(details.open));
      if (details.open) {
        dropdowns.filter((other) => other !== details).forEach((other) => closeDropdown(other));
      }
    });
  });

  document.addEventListener('click', (event) => {
    dropdowns.forEach((details) => {
      if (!details.contains(event.target)) {
        closeDropdown(details);
      }
    });
  });

  document.querySelector('.filter-reset')?.addEventListener('click', () => {
    dropdowns.forEach((details) => {
      details.querySelector('[role="option"]')?.click();
    });
  });
})();
