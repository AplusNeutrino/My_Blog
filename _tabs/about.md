---
# the default layout is 'page'
title: 中间层漫游指南
icon: fas fa-info-circle
order: 5
---

## 关于 Neutriverse

这里是 AplusNeutrino 的个人文字站。它会用来保存学习笔记、技术记录、随想和一些慢慢成形的长期想法。

这个站点基于 GitHub Pages、Jekyll 和 Chirpy。内容以 Markdown 文件保存在仓库里，所以每一次修改都会留下清楚的版本历史。

<p id="middle-layer-countdown">倒计时：剩余--年--月--日--时--分--秒</p>

本站采用 [Jekyll](https://jekyllrb.com/) 主题 [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy)。

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
      target.textContent = `倒计时：剩余${parts.years}年${parts.months}月${parts.days}日${parts.hours}时${parts.minutes}分${parts.seconds}秒`;
    };

    render();
    window.setInterval(render, 1000);
  })();
</script>
