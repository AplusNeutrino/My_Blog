#!/usr/bin/env python3
"""Exercise the built mobile sidebar in a real 390px Chrome viewport."""

import json
import shutil
import sys
import threading
from contextlib import contextmanager
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, _format, *_args):
        pass


@contextmanager
def serve(directory):
    handler = lambda *args, **kwargs: QuietHandler(
        *args, directory=str(directory), **kwargs
    )
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_port
    finally:
        server.shutdown()
        thread.join()


def read_state(driver):
    return driver.execute_script(
        r"""
        const trigger = document.getElementById('sidebar-trigger');
        const sidebar = document.getElementById('sidebar');
        const primary = [...document.querySelectorAll(
          '#sidebar .nv-sidebar-primary .nav-link'
        )];
        const utilities = [...document.querySelectorAll(
          '#sidebar .nv-sidebar-utilities .nav-link'
        )];
        const rect = trigger.getBoundingClientRect();
        const ledger = document.querySelector('[data-writing-ledger]');
        const controls = ledger?.querySelector('[data-writing-controls]');
        const writingRecords = [...document.querySelectorAll('[data-writing-record]')];
        const visibleWritingRecords = writingRecords.filter(
          (item) => !item.closest('[data-writing-item]')?.hidden
        );
        const writingCounts = (field) => writingRecords.reduce((counts, item) => {
          const value = item.dataset[field];
          counts[value] = (counts[value] || 0) + 1;
          return counts;
        }, {});
        return {
          innerWidth: window.innerWidth,
          innerHeight: window.innerHeight,
          bodyClientWidth: document.body.clientWidth,
          bodyScrollWidth: document.body.scrollWidth,
          bodyOverflowX: getComputedStyle(document.body).overflowX,
          rootOverflowX: getComputedStyle(document.documentElement).overflowX,
          triggerWidth: rect.width,
          triggerHeight: rect.height,
          triggerVisible: getComputedStyle(trigger).display !== 'none',
          expanded: trigger.getAttribute('aria-expanded'),
          controls: trigger.getAttribute('aria-controls'),
          open: document.body.hasAttribute('sidebar-display'),
          focusInSidebar: sidebar.contains(document.activeElement),
          focusIsTrigger: document.activeElement === trigger,
          primaryVisible: primary.filter(
            (item) => item.getBoundingClientRect().height > 0
          ).length,
          primaryLabels: primary.map(
            (item) => (
              item.querySelector('.nv-sidebar-copy strong')?.textContent ||
              item.textContent
            ).trim().split(/\s+/)[0]
          ),
          utilitiesVisible: utilities.filter(
            (item) => item.getBoundingClientRect().height > 0
          ).length,
          mode: document.documentElement.getAttribute('data-mode'),
          background: getComputedStyle(document.body).backgroundColor,
          writingCount: writingRecords.length,
          writingTypes: writingCounts('writingType'),
          writingTopics: writingCounts('writingTopic'),
          topicEntries: [...document.querySelectorAll('[data-writing-topic-link]')].map(
            (link) => ({
              topic: link.dataset.writingTopicLink,
              count: Number.parseInt(
                link.querySelector('[data-writing-topic-count]')?.textContent || '0',
                10
              ),
              current: link.getAttribute('aria-current'),
              href: link.getAttribute('href')
            })
          ),
          seriesEntries: [...document.querySelectorAll('[data-writing-series-link]')].map(
            (link) => ({
              series: link.dataset.writingSeriesLink,
              count: Number.parseInt(
                link.querySelector('[data-writing-series-count]')?.textContent || '0',
                10
              ),
              current: link.getAttribute('aria-current'),
              href: link.getAttribute('href')
            })
          ),
          firstWritingDate: writingRecords[0]?.dataset.writingDate || null,
          visibleWritingCount: visibleWritingRecords.length,
          visibleFirstWritingDate: visibleWritingRecords[0]?.dataset.writingDate || null,
          controlsVisible: controls ? !controls.hidden : false,
          filterType: controls?.elements.type?.value || null,
          filterTopic: controls?.elements.topic?.value || null,
          filterSeries: controls?.elements.series?.value || null,
          filterSort: controls?.elements.sort?.value || null,
          filterEmptyVisible: ledger?.querySelector('[data-writing-filter-empty]')?.hidden === false,
          pageCurrent: Number.parseInt(ledger?.dataset.writingPageCurrent || '0', 10),
          pageTotal: Number.parseInt(ledger?.dataset.writingPageTotal || '0', 10),
          urlSearch: window.location.search,
          hiddenWritingTitles: [
            'Zodiac',
            '最后的纳尔马斯克人',
            'NoSQL 项目面经',
            'ROSSMANN项目面经',
            '中间层网站更新记录'
          ].filter(
            (title) => document.getElementById('nv-writing-list')?.textContent.includes(title)
          )
        };
        """
    )



def read_series_navigation(driver):
    return driver.execute_script(
        r"""
        const panel = document.getElementById('post-series');
        const path = (selector) => {
          const link = panel?.querySelector(selector);
          if (!link) {
            return null;
          }
          const url = new URL(link.href);
          return url.pathname + url.search;
        };
        return {
          id: panel?.dataset.seriesId || null,
          position: panel?.querySelector('.post-series-count')?.textContent.trim() || null,
          itemCount: panel?.querySelectorAll('.post-series-item').length || 0,
          root: path('.post-series-root a'),
          previous: path('[data-series-previous]'),
          next: path('[data-series-next]')
        };
        """
    )

def read_post_presentation(driver):
    return driver.execute_script(
        r"""
        const article = document.querySelector('article.nv-post');
        const content = article?.querySelector('.content');
        const rect = content?.getBoundingClientRect();
        const constrained = [...(content?.querySelectorAll(
          'pre, .highlight, .table-wrapper, img, video, iframe'
        ) || [])].filter((item) => {
          const itemRect = item.getBoundingClientRect();
          return itemRect.width > (rect?.width || 0) + 1;
        });
        return {
          type: article?.dataset.writingType || null,
          classes: article ? [...article.classList] : [],
          marker: article?.querySelector('.nv-post-type')?.textContent
            .trim().replace(/\s+/g, ' ') || null,
          contentWidth: rect?.width || 0,
          bodyClientWidth: document.body.clientWidth,
          bodyScrollWidth: document.body.scrollWidth,
          constrainedOverflow: constrained.map((item) => item.tagName)
        };
        """
    )


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    require((site / "think" / "index.html").exists(), f"missing built THINK page: {site}")

    chrome = next(
        (
            path
            for name in ("google-chrome", "google-chrome-stable", "chromium")
            if (path := shutil.which(name))
        ),
        None,
    )
    require(chrome, "Chrome/Chromium executable not found")

    options = webdriver.ChromeOptions()
    options.binary_location = chrome
    for argument in (
        "--headless=new",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--force-device-scale-factor=1",
        "--window-size=390,844",
    ):
        options.add_argument(argument)

    with serve(site) as port, webdriver.Chrome(options=options) as driver:
        driver.set_window_size(390, 844)
        driver.get(f"http://127.0.0.1:{port}/think/")
        wait = WebDriverWait(driver, 10)
        wait.until(lambda current: current.execute_script("return document.readyState") == "complete")

        initial = read_state(driver)
        require(380 <= initial["innerWidth"] <= 400, f"unexpected viewport: {initial}")
        require(initial["bodyScrollWidth"] <= initial["bodyClientWidth"], f"horizontal overflow: {initial}")
        require(initial["triggerVisible"], f"mobile trigger hidden: {initial}")
        require(initial["triggerWidth"] >= 44 and initial["triggerHeight"] >= 44, f"undersized trigger: {initial}")
        require(initial["primaryVisible"] == 5, f"HOME + four primary links unavailable: {initial}")
        require(
            initial["primaryLabels"] == ["HOME", "THINK", "BUILD", "OBSERVE", "ABOUT"],
            f"primary link order changed: {initial}",
        )
        require(initial["utilitiesVisible"] == 3, f"utility links unavailable: {initial}")
        require(initial["controls"] == "sidebar" and initial["expanded"] == "false", f"trigger semantics wrong: {initial}")
        require(initial["writingCount"] == 44, f"writing count changed: {initial}")
        require(
            initial["writingTypes"] == {"note": 35, "essay": 4, "fragment": 5},
            f"public Type counts changed: {initial}",
        )
        require(
            initial["writingTopics"] == {
                "computation": 34,
                "humanity": 6,
                "otaku": 3,
                "arts": 1,
            },
            f"public Topic counts changed: {initial}",
        )
        require(
            initial["topicEntries"] == [
                {"topic": "computation", "count": 34, "current": None, "href": "/think/?topic=computation"},
                {"topic": "humanity", "count": 6, "current": None, "href": "/think/?topic=humanity"},
                {"topic": "otaku", "count": 3, "current": None, "href": "/think/?topic=otaku"},
                {"topic": "arts", "count": 1, "current": None, "href": "/think/?topic=arts"},
            ],
            f"Topic directory changed: {initial}",
        )
        require(
            initial["seriesEntries"] == [
                {"series": "database-systems", "count": 10, "current": None, "href": "/think/?series=database-systems"},
                {"series": "computer-architecture", "count": 8, "current": None, "href": "/think/?series=computer-architecture"},
                {"series": "computer-networks", "count": 10, "current": None, "href": "/think/?series=computer-networks"},
            ],
            f"Series directory changed: {initial}",
        )
        require(initial["firstWritingDate"] == "2026-08-17", f"writing order changed: {initial}")
        require(
            initial["hiddenWritingTitles"] == [],
            f"hidden title leaked: {initial['hiddenWritingTitles']}",
        )
        wait.until(lambda current: read_state(current)["controlsVisible"])
        initial = read_state(driver)
        require(
            initial["visibleWritingCount"] == 12
            and initial["pageCurrent"] == 1
            and initial["pageTotal"] == 4,
            f"default pagination contract failed: {initial}",
        )

        topic_link = driver.find_element(
            By.CSS_SELECTOR, '[data-writing-topic-link="humanity"]'
        )
        driver.execute_script("arguments[0].click();", topic_link)
        wait.until(
            lambda current: (
                (state := read_state(current))["filterTopic"] == "humanity"
                and state["visibleWritingCount"] == 6
                and "topic=humanity" in state["urlSearch"]
                and next(
                    entry for entry in state["topicEntries"] if entry["topic"] == "humanity"
                )["current"] == "true"
            )
        )
        driver.refresh()
        wait.until(
            lambda current: (
                (state := read_state(current))["controlsVisible"]
                and state["filterTopic"] == "humanity"
                and state["visibleWritingCount"] == 6
            )
        )
        driver.back()
        wait.until(lambda current: read_state(current)["filterTopic"] == "all")

        series_link = driver.find_element(
            By.CSS_SELECTOR, '[data-writing-series-link="database-systems"]'
        )
        driver.execute_script("arguments[0].click();", series_link)
        wait.until(
            lambda current: (
                (state := read_state(current))["filterSeries"] == "database-systems"
                and state["visibleWritingCount"] == 10
                and "series=database-systems" in state["urlSearch"]
                and next(
                    entry for entry in state["seriesEntries"]
                    if entry["series"] == "database-systems"
                )["current"] == "true"
            )
        )
        driver.refresh()
        wait.until(
            lambda current: (
                (state := read_state(current))["controlsVisible"]
                and state["filterSeries"] == "database-systems"
                and state["visibleWritingCount"] == 10
            )
        )
        driver.back()
        wait.until(lambda current: read_state(current)["filterSeries"] == "all")

        Select(driver.find_element(By.ID, "nv-writing-type")).select_by_value("fragment")
        wait.until(lambda current: read_state(current)["visibleWritingCount"] == 5)
        Select(driver.find_element(By.ID, "nv-writing-topic")).select_by_value("humanity")
        wait.until(lambda current: read_state(current)["visibleWritingCount"] == 4)
        Select(driver.find_element(By.ID, "nv-writing-sort")).select_by_value("oldest")
        wait.until(
            lambda current: (
                (state := read_state(current))["visibleFirstWritingDate"] == "2024-09-12"
                and "type=fragment" in state["urlSearch"]
                and "topic=humanity" in state["urlSearch"]
                and "sort=oldest" in state["urlSearch"]
            )
        )

        driver.refresh()
        wait.until(lambda current: read_state(current)["controlsVisible"])
        refreshed = read_state(driver)
        require(
            refreshed["filterType"] == "fragment"
            and refreshed["filterTopic"] == "humanity"
            and refreshed["filterSort"] == "oldest"
            and refreshed["visibleWritingCount"] == 4,
            f"refresh lost filter state: {refreshed}",
        )

        Select(driver.find_element(By.ID, "nv-writing-type")).select_by_value("essay")
        wait.until(lambda current: read_state(current)["visibleWritingCount"] == 1)
        driver.back()
        wait.until(
            lambda current: (
                (state := read_state(current))["filterType"] == "fragment"
                and state["filterTopic"] == "humanity"
                and state["filterSort"] == "oldest"
                and state["visibleWritingCount"] == 4
            )
        )

        think_url = f"http://127.0.0.1:{port}/think/"
        driver.get(think_url + "?type=essay&topic=arts")
        wait.until(lambda current: read_state(current)["controlsVisible"])
        no_results = read_state(driver)
        require(
            no_results["visibleWritingCount"] == 0
            and no_results["filterEmptyVisible"],
            f"filter empty state failed: {no_results}",
        )

        driver.get(think_url + "?sort=oldest")
        wait.until(lambda current: read_state(current)["controlsVisible"])
        oldest = read_state(driver)
        require(
            oldest["visibleWritingCount"] == 12
            and oldest["visibleFirstWritingDate"] == "2024-09-12",
            f"oldest sort failed: {oldest}",
        )

        driver.get(think_url + "?page=2")
        wait.until(
            lambda current: (
                (state := read_state(current))["controlsVisible"]
                and state["pageCurrent"] == 2
            )
        )
        driver.refresh()
        wait.until(lambda current: read_state(current)["pageCurrent"] == 2)
        paged = read_state(driver)
        require(
            paged["visibleWritingCount"] == 12 and paged["pageTotal"] == 4,
            f"pagination refresh failed: {paged}",
        )

        driver.get(
            think_url
            + "?type=invalid&topic=invalid&series=invalid&sort=invalid&page=-2"
        )
        wait.until(
            lambda current: (
                (state := read_state(current))["controlsVisible"]
                and state["urlSearch"] == ""
            )
        )
        initial = read_state(driver)
        require(
            initial["filterType"] == "all"
            and initial["filterTopic"] == "all"
            and initial["filterSeries"] == "all"
            and initial["filterSort"] == "newest"
            and initial["pageCurrent"] == 1,
            f"invalid parameters did not fall back: {initial}",
        )

        driver.get(think_url + "?series=database-systems&sort=oldest")
        wait.until(
            lambda current: (
                (state := read_state(current))["controlsVisible"]
                and state["filterSeries"] == "database-systems"
                and state["visibleWritingCount"] == 10
            )
        )
        database_paths = driver.execute_script(
            r"""
            return [...document.querySelectorAll(
              '#nv-writing-list [data-writing-item]:not([hidden]) h3 a'
            )].map((link) => new URL(link.href).pathname);
            """
        )
        require(
            len(database_paths) == 10,
            f"Database Systems built links changed: {database_paths}",
        )

        site_url = f"http://127.0.0.1:{port}"
        expected_series_pages = [
            (
                database_paths[0],
                {
                    "id": "database-systems",
                    "position": "1/10",
                    "itemCount": 10,
                    "root": "/think/?series=database-systems",
                    "previous": None,
                    "next": database_paths[1],
                },
            ),
            (
                database_paths[4],
                {
                    "id": "database-systems",
                    "position": "5/10",
                    "itemCount": 10,
                    "root": "/think/?series=database-systems",
                    "previous": database_paths[3],
                    "next": database_paths[5],
                },
            ),
            (
                database_paths[9],
                {
                    "id": "database-systems",
                    "position": "10/10",
                    "itemCount": 10,
                    "root": "/think/?series=database-systems",
                    "previous": database_paths[8],
                    "next": None,
                },
            ),
        ]
        for path, expected in expected_series_pages:
            driver.get(site_url + path)
            wait.until(
                lambda current: current.execute_script(
                    "return document.readyState"
                ) == "complete"
            )
            actual = read_series_navigation(driver)
            require(actual == expected, f"Series neighbor contract failed at {path}: {actual}")

        type_expectations = [
            ("note", "Note / 笔记"),
            ("essay", "Essay / 长文"),
        ]
        for writing_type, marker in type_expectations:
            driver.get(think_url + f"?type={writing_type}")
            wait.until(
                lambda current: (
                    (state := read_state(current))["controlsVisible"]
                    and state["filterType"] == writing_type
                    and state["visibleWritingCount"] > 0
                )
            )
            post_path = driver.execute_script(
                r"""
                const link = document.querySelector(
                  '#nv-writing-list [data-writing-item]:not([hidden]) h3 a'
                );
                return link ? new URL(link.href).pathname : null;
                """
            )
            require(post_path, f"missing built {writing_type} link")
            driver.get(site_url + post_path)
            wait.until(
                lambda current: current.execute_script(
                    "return document.readyState"
                ) == "complete"
            )
            presentation = read_post_presentation(driver)
            require(
                presentation["type"] == writing_type
                and f"nv-post--{writing_type}" in presentation["classes"]
                and presentation["marker"] == marker,
                f"{writing_type} presentation contract failed: {presentation}",
            )
            require(
                0 < presentation["contentWidth"] <= 740
                and presentation["bodyScrollWidth"]
                <= presentation["bodyClientWidth"],
                f"{writing_type} reading measure overflow: {presentation}",
            )
            require(
                presentation["constrainedOverflow"] == [],
                f"{writing_type} rich content escaped its container: {presentation}",
            )

        driver.get(think_url + "?type=fragment")
        wait.until(
            lambda current: (
                (state := read_state(current))["controlsVisible"]
                and state["visibleWritingCount"] == 5
            )
        )
        fragment_source = driver.find_element(
            By.CSS_SELECTOR,
            '#nv-writing-list [data-writing-item]:not([hidden]) .nv-writing-source',
        )
        require(
            fragment_source.get_attribute("href").endswith(
                "/thoughts/#fragment-2026-05-02"
            ),
            f"Fragment source link changed: {fragment_source.get_attribute('href')}",
        )
        driver.execute_script("arguments[0].click();", fragment_source)
        wait.until(
            lambda current: current.current_url.endswith(
                "/thoughts/#fragment-2026-05-02"
            )
        )
        target = driver.find_element(By.ID, "fragment-2026-05-02")
        require(target.is_displayed(), "Fragment stable anchor target is not visible")

        driver.get(think_url)
        wait.until(lambda current: read_state(current)["controlsVisible"])

        trigger = driver.find_element(By.ID, "sidebar-trigger")
        trigger.click()
        wait.until(
            lambda current: (
                (state := read_state(current))["open"] and state["focusInSidebar"]
            )
        )
        opened = read_state(driver)
        require(opened["expanded"] == "true" and opened["focusInSidebar"], f"open focus contract failed: {opened}")
        require(
            opened["bodyOverflowX"] == "hidden" or opened["rootOverflowX"] == "hidden",
            f"open drawer allows horizontal scrolling: {opened}",
        )

        driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        wait.until(lambda current: not read_state(current)["open"])
        escaped = read_state(driver)
        require(escaped["expanded"] == "false" and escaped["focusIsTrigger"], f"Escape close contract failed: {escaped}")

        trigger.click()
        wait.until(lambda current: read_state(current)["open"])
        mask = driver.find_element(By.ID, "mask")
        driver.execute_script("arguments[0].click();", mask)
        wait.until(lambda current: not read_state(current)["open"])
        masked = read_state(driver)
        require(masked["focusIsTrigger"], f"mask did not restore trigger focus: {masked}")

        trigger.click()
        wait.until(lambda current: read_state(current)["open"])
        before_theme = read_state(driver)
        mode_toggle = driver.find_element(By.ID, "mode-toggle")
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", mode_toggle
        )
        wait.until(lambda _current: mode_toggle.is_displayed() and mode_toggle.is_enabled())
        mode_toggle.click()
        wait.until(lambda current: read_state(current)["background"] != before_theme["background"])
        themed = read_state(driver)
        require(
            themed["bodyOverflowX"] == "hidden" or themed["rootOverflowX"] == "hidden",
            f"theme allows horizontal scrolling: {themed}",
        )
        require(themed["primaryVisible"] == 5 and themed["utilitiesVisible"] == 3, f"theme hid navigation: {themed}")

        first_navigation = driver.find_element(
            By.CSS_SELECTOR, "#sidebar .nv-sidebar-primary .nav-link"
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", first_navigation
        )
        first_navigation.click()
        wait.until(lambda current: not read_state(current)["open"])
        navigated = read_state(driver)
        require(navigated["expanded"] == "false", f"navigation did not close menu: {navigated}")

        print(json.dumps({
            "initial": initial,
            "opened": opened,
            "escaped": escaped,
            "masked": masked,
            "themed": themed,
            "navigated": navigated,
        }, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
