#!/usr/bin/env python3
"""Validate the built Neutriverse UI across breakpoints, themes and input modes."""

import json
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
        const node = document.querySelector('.nv-primary-nav-link');
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
    with serve(site) as port, webdriver.Chrome(options=options) as driver:
        wait = WebDriverWait(driver, 12)
        site_url = f"http://127.0.0.1:{port}"
        for width, height in VIEWPORTS:
            driver.set_window_size(width, height)
            for theme in THEMES:
                for path, root_selector in PAGE_CONTRACTS.items():
                    driver.get(site_url + path)
                    wait.until(lambda current: current.execute_script("return document.readyState") == "complete")
                    set_theme(driver, theme)
                    layout = read_layout(driver, root_selector)
                    require(
                        layout["rootVisible"]
                        and layout["mainVisible"]
                        and layout["bodyScrollWidth"] <= layout["bodyClientWidth"] + 1
                        and layout["documentScrollWidth"] <= layout["documentClientWidth"] + 1,
                        f"responsive layout failed at {width}px {theme} {path}: {layout}",
                    )
                    if path == "/":
                        require_contrast(driver, ".nv-home-identity", f"home identity {theme}")
                        require_focus(driver, ".nv-home-explore .nv-primary-nav-link", "home entrance")
                    else:
                        require_contrast(driver, ".nv-section-label", f"section label {theme} {path}")
                        require_contrast(driver, ".nv-section-summary", f"section summary {theme} {path}")
                        require_contrast(driver, ".nv-primary-nav-name", f"section navigation {theme} {path}")
                        require_focus(driver, ".nv-primary-nav-link", f"section navigation {path}")
                    if path == "/build/":
                        require_focus(driver, ".nv-project-filters button", "BUILD filter")
                    if path == "/observe/":
                        require_focus(driver, ".nv-observe-card-actions a", "OBSERVE action")
                    results.append({"width": width, "theme": theme, "path": path})

                require_article_reading(driver, site_url, wait, theme)

            driver.get(site_url + "/think/")
            wait.until(lambda current: current.find_element(By.CSS_SELECTOR, "[data-section-identity='think']").is_displayed())
            require_reduced_motion(driver)

    print(json.dumps({"checks": len(results), "viewports": VIEWPORTS, "themes": THEMES}, sort_keys=True))


if __name__ == "__main__":
    main()
