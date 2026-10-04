(() => {
  document.addEventListener('DOMContentLoaded', () => {
    const utilityTrigger = document.querySelector('[data-nv-search-trigger]');

    utilityTrigger?.addEventListener('click', () => {
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
})();
