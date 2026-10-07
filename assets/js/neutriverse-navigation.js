(() => {
  document.addEventListener('DOMContentLoaded', () => {
    const searchTriggers = document.querySelectorAll('[data-nv-search-trigger]');

    searchTriggers.forEach((searchTrigger) => {
      searchTrigger.addEventListener('click', () => {
        const nativeTrigger = document.getElementById('search-trigger');
        const searchInput = document.getElementById('search-input');

        if (nativeTrigger) {
          nativeTrigger.click();
          window.requestAnimationFrame(() => searchInput?.focus());
        } else {
          searchInput?.focus();
        }
      });
    });

    const sidebar = document.getElementById('sidebar');
    const mobileTrigger = document.getElementById('sidebar-trigger');
    const mobileQuery = window.matchMedia('(max-width: 849px)');

    if (!sidebar || !mobileTrigger) {
      return;
    }

    let mobileOpen = false;

    const mobileFocusable = () =>
      Array.from(
        sidebar.querySelectorAll(
          'a[href], button:not([disabled]), input:not([disabled]), [tabindex]:not([tabindex="-1"])'
        )
      ).filter(
        (element) => !element.hidden && element.getAttribute('aria-hidden') !== 'true'
      );

    const syncMobileSidebar = () => {
      const isOpen =
        mobileQuery.matches && document.body.hasAttribute('sidebar-display');

      mobileTrigger.setAttribute('aria-controls', 'sidebar');
      mobileTrigger.setAttribute('aria-expanded', String(isOpen));
      mobileTrigger.setAttribute(
        'aria-label',
        isOpen ? '关闭左侧栏' : '打开左侧栏'
      );

      if (isOpen && !mobileOpen) {
        window.requestAnimationFrame(() => mobileFocusable()[0]?.focus());
      } else if (!isOpen && mobileOpen && mobileQuery.matches) {
        mobileTrigger.focus();
      }

      mobileOpen = isOpen;
    };

    const sidebarStateObserver = new MutationObserver(syncMobileSidebar);
    sidebarStateObserver.observe(document.body, {
      attributes: true,
      attributeFilter: ['sidebar-display']
    });

    sidebar.addEventListener('keydown', (event) => {
      if (!mobileOpen) {
        return;
      }

      if (event.key === 'Escape') {
        event.preventDefault();
        mobileTrigger.click();
        return;
      }

      if (event.key !== 'Tab') {
        return;
      }

      const focusable = mobileFocusable();
      const first = focusable[0];
      const last = focusable[focusable.length - 1];

      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last?.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first?.focus();
      }
    });

    const handleMobileBreakpoint = () => {
      if (
        !mobileQuery.matches &&
        document.body.hasAttribute('sidebar-display')
      ) {
        mobileOpen = false;
        mobileTrigger.click();
      }

      syncMobileSidebar();
    };

    mobileQuery.addEventListener('change', handleMobileBreakpoint);
    syncMobileSidebar();
  });
})();
