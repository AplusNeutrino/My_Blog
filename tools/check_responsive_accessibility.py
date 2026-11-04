#!/usr/bin/env python3
"""Validate the built Neutriverse UI across breakpoints, themes and input modes."""

import json
import os
import shutil
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from check_mobile_sidebar import require, serve


VIEWPORTS = (
    (390, 844),
    (768, 900),
    (1024, 900),
    (1366, 900),
)
THEMES = ("dark", "light")
PAGE_CONTRACTS = {
    "/": "[data-home-section='identity']",
    "/think/": "[data-section-identity='think']",
    "/build/": "[data-section-identity='build']",
    "/observe/": "[data-section-identity='observe']",
    "/about/": "[data-section-identity='about']",
}


def set_theme(driver, theme):
    driver.execute_script(
        """
        document.documentElement.setAttribute('data-mode', arguments[0]);
        document.documentElement.setAttribute('data-bs-theme', arguments[0]);
        """,
        theme,
    )


def read_layout(driver, root_selector):
    return driver.execute_script(
        r"""
        const root = document.querySelector(arguments[0]);
        const main = document.querySelector('main');
        const visible = (node) => {
          if (!node) return false;
          const style = getComputedStyle(node);
          const rect = node.getBoundingClientRect();
          return style.display !== 'none' && style.visibility !== 'hidden'
            && rect.width > 0 && rect.height > 0;
        };
        return {
          rootVisible: visible(root),
          mainVisible: visible(main),
          viewportWidth: window.innerWidth,
          bodyClientWidth: document.body.clientWidth,
          bodyScrollWidth: document.body.scrollWidth,
          documentClientWidth: document.documentElement.clientWidth,
          documentScrollWidth: document.documentElement.scrollWidth
        };
        """,
        root_selector,
    )


def read_contrast(driver, selector):
    return driver.execute_script(
        r"""
        const node = document.querySelector(arguments[0]);
        if (!node) return null;
        const parse = (value) => {
          const hex = value.trim().match(/^#([0-9a-f]{6})$/i);
          if (hex) {
            return [
              Number.parseInt(hex[1].slice(0, 2), 16),
              Number.parseInt(hex[1].slice(2, 4), 16),
              Number.parseInt(hex[1].slice(4, 6), 16),
              1
            ];
          }
          const match = value.match(/[\d.]+/g);
          if (!match || match.length < 3) return null;
          const values = match.slice(0, 4).map(Number);
          if (value.startsWith('color(')) {
            values[0] *= 255;
            values[1] *= 255;
            values[2] *= 255;
          }
          return values;
        };
        const opaqueBackground = (start) => {
          let current = start;
          while (current) {
            const style = getComputedStyle(current);
            if (style.backgroundImage !== 'none') {
              const surface = parse(
                getComputedStyle(document.documentElement)
                  .getPropertyValue('--nv-surface-1')
              );
              if (surface) return surface;
            }
            const parsed = parse(style.backgroundColor);
            if (parsed && (parsed.length < 4 || parsed[3] > 0.99)) return parsed;
            current = current.parentElement;
          }
          return parse(getComputedStyle(document.documentElement).backgroundColor)
            || [255, 255, 255, 1];
        };
        const luminance = (rgb) => {
          const channel = (value) => {
            const normalized = value / 255;
            return normalized <= 0.04045
              ? normalized / 12.92
              : Math.pow((normalized + 0.055) / 1.055, 2.4);
          };
          return 0.2126 * channel(rgb[0])
            + 0.7152 * channel(rgb[1])
            + 0.0722 * channel(rgb[2]);
        };
        const foreground = parse(getComputedStyle(node).color);
        const background = opaqueBackground(node);
        const high = Math.max(luminance(foreground), luminance(background));
        const low = Math.min(luminance(foreground), luminance(background));
        return {
          ratio: (high + 0.05) / (low + 0.05),
          foreground: getComputedStyle(node).color,
          background: `rgb(${background.slice(0, 3).join(', ')})`,
          text: node.textContent.trim().replace(/\s+/g, ' ').slice(0, 80)
        };
        """,
        selector,
    )


def require_contrast(driver, selector, label):
    result = read_contrast(driver, selector)
    require(result is not None, f"missing contrast target {label}: {selector}")
    require(
        result["ratio"] >= 4.5,
        f"WCAG AA contrast failed for {label}: {result}",
    )


def require_focus(driver, selector, label, minimum_height=44):
    result = driver.execute_script(
        r"""
        const node = document.querySelector(arguments[0]);
        if (!node) return null;
        node.focus();
        const style = getComputedStyle(node);
        const rect = node.getBoundingClientRect();
        return {
          active: document.activeElement === node,
          outlineStyle: style.outlineStyle,
          outlineWidth: Number.parseFloat(style.outlineWidth),
          width: rect.width,
          height: rect.height,
          name: (node.getAttribute('aria-label') || node.textContent)
            .trim().replace(/\s+/g, ' ').slice(0, 80)
        };
        """,
        selector,
    )
    require(result is not None, f"missing focus target {label}: {selector}")
    require(
        result["active"]
        and result["outlineStyle"] not in ("none", "hidden")
        and result["outlineWidth"] >= 2,
        f"focus indicator failed for {label}: {result}",
    )
    require(
        result["height"] >= minimum_height,
        f"touch target below {minimum_height}px for {label}: {result}",
    )


def require_reduced_motion(driver):
    driver.execute_cdp_cmd(
        "Emulation.setEmulatedMedia",
        {
            "features": [
                {"name": "prefers-reduced-motion", "value": "reduce"},
            ]
        },
    )
    result = driver.execute_script(
        r"""
        const node = document.querySelector('.nv-filter-select summary');
        const style = getComputedStyle(node);
        return {
          matches: matchMedia('(prefers-reduced-motion: reduce)').matches,
          transitionDuration: style.transitionDuration,
          animationName: style.animationName,
          scrollBehavior: getComputedStyle(
            document.querySelector('[data-neutriverse-section]') ||
            document.querySelector('[data-home-section]')
          ).scrollBehavior
        };
        """
    )
    require(
        result["matches"]
        and result["transitionDuration"] == "0s"
        and result["animationName"] == "none"
        and result["scrollBehavior"] == "auto",
        f"reduced-motion contract failed: {result}",
    )
    driver.execute_cdp_cmd("Emulation.setEmulatedMedia", {"features": []})


def require_article_reading(driver, site_url, wait, theme):
    driver.get(site_url + "/think/")
    wait.until(lambda current: current.find_element(By.CSS_SELECTOR, "[data-writing-ledger]").is_displayed())
    post_path = driver.execute_script(
        """
        const link = document.querySelector('#nv-writing-list h3 a');
        return link ? new URL(link.href).pathname : null;
        """
    )
    require(post_path, "THINK did not expose a public article for reading checks")
    driver.get(site_url + post_path)
    wait.until(lambda current: current.find_element(By.CSS_SELECTOR, "article.nv-post .content").is_displayed())
    set_theme(driver, theme)
    result = driver.execute_script(
        r"""
        const content = document.querySelector('article.nv-post .content');
        const rect = content.getBoundingClientRect();
        const overflow = [...content.querySelectorAll(
          'pre, .highlight, .table-wrapper, img, video, iframe'
        )].filter((node) => node.getBoundingClientRect().width > rect.width + 1)
          .map((node) => node.tagName);
        return {
          width: rect.width,
          fontSize: Number.parseFloat(getComputedStyle(content).fontSize),
          lineHeight: Number.parseFloat(getComputedStyle(content).lineHeight),
          overflow,
          bodyClientWidth: document.body.clientWidth,
          bodyScrollWidth: document.body.scrollWidth
        };
        """
    )
    require(
        0 < result["width"] <= 740
        and result["fontSize"] >= 16
        and result["lineHeight"] / result["fontSize"] >= 1.7
        and result["overflow"] == []
        and result["bodyScrollWidth"] <= result["bodyClientWidth"] + 1,
        f"article reading contract failed: {result}",
    )
    require_contrast(driver, "article.nv-post .content", "article body")
    driver.execute_script(
        "document.querySelector('.post-tail-wrapper').scrollIntoView({behavior:'instant',block:'end'});"
    )
    panel = driver.execute_script(
        """
        const stack = document.querySelector('#post-panel-stack');
        const memory = document.querySelector('#panel-wrapper .access');
        return {
          position: getComputedStyle(stack).position,
          overflowY: getComputedStyle(stack).overflowY,
          stackBottom: stack.getBoundingClientRect().bottom,
          memoryTop: memory.getBoundingClientRect().top
        };
        """
    )
    require(
        panel["position"] == "static"
        and panel["overflowY"] == "visible"
        and panel["stackBottom"] <= panel["memoryTop"] + 1,
        f"article panel overlaps the memory note after a long scroll: {panel}",
    )


def require_navigation_alignment(driver, context):
    """Every editorial page exposes real, visible content rather than duplicate navigation."""
    cards = driver.execute_script(
        """
        return [...document.querySelectorAll(
          '.nv-home-featured-card, .nv-writing-record, .nv-project-card, .nv-observe-card, .about-info'
        )].filter(node => !node.hidden && node.getClientRects().length > 0).map((node, index) => {
          const rect = node.getBoundingClientRect();
          return {index, width: rect.width, height: rect.height, text: node.innerText.slice(0, 80)};
        });
        """
    )
    require(cards, f"missing editorial content {context}")
    for card in cards:
        require(card['width'] > 0 and card['height'] > 0 and card['text'].strip(),
                f"invisible or empty editorial component {context}: {card}")

    audit = driver.execute_script(
        """
        const section = document.querySelector('[data-neutriverse-section]')?.dataset.neutriverseSection;
        const definition = {
          build: {section, selector: '.nv-project-card', count: 7, borderless: true},
          observe: {section, selector: '.nv-observe-card', count: 2, borderless: true},
          about: {
            section,
            selector: '.about-current, .about-context-panel, .about-current-meta, .about-current-meta > div, .about-stack-panel, .about-stack-item',
            count: 17,
            borderless: false
          }
        }[section];
        const surfaces = definition ? [...document.querySelectorAll(definition.selector)].map(node => {
          const style = getComputedStyle(node);
          return {
            className: node.className,
            borderTopWidth: style.borderTopWidth,
            borderRadius: style.borderTopLeftRadius,
            backgroundColor: style.backgroundColor,
            boxShadow: style.boxShadow
          };
        }) : [];
        const stackTitles = definition?.section === 'about'
          ? [...document.querySelectorAll('.about-stack-item')].map(item => {
              const title = item.querySelector('strong');
              return {
                text: title.textContent.trim(),
                width: title.getBoundingClientRect().width,
                whiteSpace: getComputedStyle(title).whiteSpace,
                opacity: getComputedStyle(title).opacity,
                indexPosition: getComputedStyle(item.querySelector('.about-stack-index')).position,
                datePosition: getComputedStyle(item.querySelector('time')).position
              };
            })
          : [];
        return {definition, surfaces, stackTitles};
        """
    )
    definition = audit["definition"]
    if definition:
        surfaces = audit["surfaces"]
        require(len(surfaces) == definition["count"], f"editorial surface count changed {context}: {surfaces}")
        require(
            all(
                surface["borderRadius"] == "0px"
                and surface["backgroundColor"] == "rgba(0, 0, 0, 0)"
                and surface["boxShadow"] == "none"
                and (not definition["borderless"] or surface["borderTopWidth"] == "0px")
                for surface in surfaces
            ),
            f"legacy card surface remains {context}: {surfaces}",
        )
    if audit["stackTitles"]:
        require(
            len(audit["stackTitles"]) == 10
            and all(
                title["text"]
                and title["width"] > 40
                and title["whiteSpace"] == "normal"
                and title["opacity"] == "1"
                and title["indexPosition"] == "static"
                and title["datePosition"] == "static"
                for title in audit["stackTitles"]
            ),
            f"about stack titles are clipped or misplaced {context}: {audit['stackTitles']}",
        )
    return cards


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    for relative_path in ("index.html", "think/index.html", "build/index.html", "observe/index.html", "about/index.html"):
        require((site / relative_path).exists(), f"missing built page: {relative_path}")

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
    for argument in ("--headless=new", "--no-sandbox", "--disable-dev-shm-usage"):
        options.add_argument(argument)

    results = []
    screenshot_dir = os.environ.get('UI_SCREENSHOT_DIR')
    if screenshot_dir:
        Path(screenshot_dir).mkdir(parents=True, exist_ok=True)
    with serve(site) as port, webdriver.Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 12)
        site_url = f"http://127.0.0.1:{port}"
        for width, height in VIEWPORTS:
            driver.set_window_size(width, height)
            if os.name == 'nt':
                driver.execute_cdp_cmd(
                    'Emulation.setDeviceMetricsOverride',
                    {'width': width, 'height': height, 'deviceScaleFactor': 1, 'mobile': width < 850},
                )
            for theme in THEMES:
                for path, root_selector in PAGE_CONTRACTS.items():
                    driver.get(site_url + path)
                    wait.until(lambda current: current.execute_script("return document.readyState") == "complete")
                    set_theme(driver, theme)
                    driver.execute_async_script(
                        "const done = arguments[arguments.length - 1]; document.fonts.ready.then(() => done(true));"
                    )
                    wait.until(lambda current: current.execute_script(
                        "return document.getAnimations().every(a => a.playState !== 'running'"
                        " || a.effect.getTiming().iterations === Infinity);"
                    ))
                    layout = read_layout(driver, root_selector)
                    require(
                        layout["rootVisible"]
                        and layout["mainVisible"]
                        and layout["bodyScrollWidth"] <= layout["bodyClientWidth"] + 1
                        and layout["documentScrollWidth"] <= layout["documentClientWidth"] + 1,
                        f"responsive layout failed at {width}px {theme} {path}: {layout}",
                    )
                    if width >= 850:
                        sidebar = driver.execute_script(
                            """
                            const node = document.querySelector('#sidebar');
                            return {
                              overflowY: getComputedStyle(node).overflowY,
                              clientHeight: node.clientHeight,
                              scrollHeight: node.scrollHeight
                            };
                            """
                        )
                        require(
                            sidebar["overflowY"] == "hidden"
                            and sidebar["scrollHeight"] <= sidebar["clientHeight"] + 1,
                            f"desktop sidebar scrolls at {width}px {theme} {path}: {sidebar}",
                        )
                        require_contrast(driver, "#sidebar .site-title", f"sidebar title {theme} {path}")
                        require_contrast(
                            driver,
                            "#sidebar .nv-sidebar-primary .nav-link[aria-current='page'] small",
                            f"sidebar current item {theme} {path}",
                        )
                    if path == "/":
                        require_contrast(driver, ".nv-home-identity", f"home identity {theme}")
                        require_focus(driver, ".nv-home-more", "home writing entrance")
                        card_shells = driver.execute_script(
                            """
                            return [...document.querySelectorAll(
                              '.nv-home-transmission, .nv-home-featured-card, .nv-home-signal-card, .nv-home-status-grid > div'
                            )].map(node => {
                              const style = getComputedStyle(node);
                              return {
                                className: node.className,
                                borderTopWidth: style.borderTopWidth,
                                borderRadius: style.borderTopLeftRadius,
                                backgroundColor: style.backgroundColor,
                                boxShadow: style.boxShadow
                              };
                            });
                            """
                        )
                        require(
                            len(card_shells) == 13
                            and all(
                                card["borderTopWidth"] == "0px"
                                and card["borderRadius"] == "0px"
                                and card["backgroundColor"] == "rgba(0, 0, 0, 0)"
                                and card["boxShadow"] == "none"
                                for card in card_shells
                            ),
                            f"legacy homepage card styling remains at {width}px {theme}: {card_shells}",
                        )
                    else:
                        require_contrast(driver, ".nv-section-identity h1", f"section title {theme} {path}")
                        require_contrast(driver, ".nv-section-summary", f"section summary {theme} {path}")
                        focus_selector = {
                            "/think/": ".nv-writing-reset",
                            "/build/": ".nv-project-card-action a",
                            "/observe/": ".nv-observe-card-actions a",
                            "/about/": ".about-relation-action[href]",
                        }[path]
                        require_focus(driver, focus_selector, f"section action {path}")
                    cards = require_navigation_alignment(driver, f"{width}px {theme} {path}")
                    visible_h1_count = driver.execute_script(
                        "return [...document.querySelectorAll('main h1')]"
                        ".filter(node => node.getClientRects().length > 0).length;"
                    )
                    require(
                        visible_h1_count == 1,
                        f"duplicate or missing page title at {width}px {theme} {path}: {visible_h1_count}",
                    )
                    if screenshot_dir:
                        name = path.strip('/').replace('/', '-') or 'home'
                        header = driver.find_element(By.CSS_SELECTOR, '.nv-section-identity, .nv-home-identity')
                        driver.execute_script(
                            "arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});",
                            header,
                        )
                        require(driver.save_screenshot(
                            str(Path(screenshot_dir) / f'{width}-{theme}-{name}-editorial.png')
                        ), f"could not save editorial screenshot: {width} {theme} {path}")
                    results.append({"width": width, "theme": theme, "path": path, "cards": cards})

                require_article_reading(driver, site_url, wait, theme)

            driver.get(site_url + "/think/")
            wait.until(lambda current: current.find_element(By.CSS_SELECTOR, "[data-section-identity='think']").is_displayed())
            require_reduced_motion(driver)

    if screenshot_dir:
        (Path(screenshot_dir) / 'navigation-metrics.json').write_text(
            json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8'
        )
    print(json.dumps({"checks": len(results), "viewports": VIEWPORTS, "themes": THEMES}, sort_keys=True))


if __name__ == "__main__":
    main()
