#!/usr/bin/env python3
"""Capture and check THINK states and the public BUILD facts, not private apps."""
import base64
import json
import os
import shutil
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait

from check_mobile_sidebar import require, serve

VIEWPORTS = ((390, 844), (768, 900), (1024, 900), (1366, 900))
PROJECTS = ('fitzsight', 'akasha-notes', 'toyosatomimis-headphone',
            'ravenis', 'occult-atlas', 'gate', 'officespire')
SCENARIOS = [
    ('think-all', '/think/', 12),
    ('think-fragments', '/think/?type=fragment', 5),
    ('think-empty', '/think/?type=essay&topic=arts', 0),
    ('think-last-page', '/think/?page=4', 8),
    ('build-all', '/build/', 7),
    ('build-known', '/build/?status=implemented_unverified', 1),
    ('build-unspecified', '/build/?status=unspecified', 6),
    *((f'project-{project}', f'/build/{project}/', None) for project in PROJECTS),
]


def visible_count(driver, kind):
    selector = '[data-writing-item]' if kind == 'think' else '[data-project-card]'
    return driver.execute_script(
        "return [...document.querySelectorAll(arguments[0])].filter(n => !n.hidden).length;",
        selector,
    )


def settle(driver, wait, theme):
    wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
    if driver.execute_script('return document.documentElement.dataset.mode') != theme:
        driver.find_element(By.ID, 'mode-toggle').click()
    wait.until(lambda d: d.execute_script('return document.documentElement.dataset.mode') == theme)
    driver.execute_async_script(
        'const done = arguments[arguments.length - 1]; document.fonts.ready.then(() => done(true));'
    )
    # Let finite CSS transitions finish; infinite decorative animation is not a blocker.
    wait.until(lambda d: d.execute_script(
        "return document.getAnimations().every(a => a.playState !== 'running'"
        " || a.effect.getTiming().iterations === Infinity);"
    ))


def geometry(driver):
    return driver.execute_script("""
      const visible = n => n.getBoundingClientRect().width > 0
        && n.getBoundingClientRect().height > 0;
      const detail = document.querySelector('[data-project-detail]');
      const surfaces = [...document.querySelectorAll(
        '.nv-project-card, .nv-project-hero, .nv-project-detail-grid > section'
      )].filter(visible).map(n => ({radius: getComputedStyle(n).borderTopLeftRadius}));
      const mono = detail?.querySelector('.nv-project-breadcrumb');
      return {
        width: innerWidth, body: document.body.scrollWidth,
        document: document.documentElement.scrollWidth,
        headings: [...document.querySelectorAll('main h1, main h2, main h3')]
          .filter(visible).filter(n => n.scrollWidth > n.clientWidth + 1)
          .map(n => n.textContent),
        surfaces, font: mono ? getComputedStyle(mono).fontFamily : null,
        noindex: document.querySelector('meta[name="robots"]')?.content || ''
      };
    """)


def exercise_controls(driver, wait, kind):
    if kind == 'think':
        Select(driver.find_element(By.ID, 'nv-writing-type')).select_by_value('fragment')
        wait.until(lambda d: visible_count(d, kind) == 5)
        require('type=fragment' in driver.current_url, 'THINK state is not shareable')
    else:
        driver.find_element(By.CSS_SELECTOR, '[data-project-filter="implemented_unverified"]').send_keys(Keys.ENTER)
        wait.until(lambda d: visible_count(d, kind) == 1)
        require('status=implemented_unverified' in driver.current_url, 'BUILD state is not shareable')
    driver.refresh()
    wait.until(lambda d: visible_count(d, kind) == (5 if kind == 'think' else 1))
    driver.back()
    wait.until(lambda d: visible_count(d, kind) == (12 if kind == 'think' else 7))
    if kind == 'build':
        driver.find_element(By.CSS_SELECTOR, '[data-project-filter="unspecified"]').click()
        wait.until(lambda d: visible_count(d, kind) == 6)
        driver.find_element(By.CSS_SELECTOR, '[data-project-filter="all"]').click()
        wait.until(lambda d: visible_count(d, kind) == 7)
    return {'filter': True, 'refresh': True, 'back': True}


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
    output = Path(os.environ.get('UI_AUDIT_DIR', '/tmp/neutriverse-think-build-audit'))
    output.mkdir(parents=True, exist_ok=True)
    chrome = next((p for n in ('google-chrome', 'google-chrome-stable', 'chromium')
                   if (p := shutil.which(n))), None)
    require(chrome, 'Chrome executable missing')
    options = webdriver.ChromeOptions()
    options.binary_location = chrome
    for arg in ('--headless=new', '--no-sandbox', '--disable-dev-shm-usage'):
        options.add_argument(arg)
    results = []
    try:
        with serve(site) as port, webdriver.Chrome(options=options) as driver:
            driver.set_script_timeout(30)
            wait = WebDriverWait(driver, 20)
            base = f'http://127.0.0.1:{port}'
            for width, height in VIEWPORTS:
                driver.set_window_size(width, height)
                for theme in ('dark', 'light'):
                    for name, path, count in SCENARIOS:
                        driver.get(base + path)
                        settle(driver, wait, theme)
                        kind = 'think' if name.startswith('think') else 'build'
                        if count is not None:
                            wait.until(lambda d: visible_count(d, kind) == count)
                        g = geometry(driver)
                        result = {'name': name, 'path': path, 'window': [width, height],
                                  'theme': theme, 'geometry': g, 'count': count}
                        results.append(result)
                        png = driver.execute_cdp_cmd('Page.captureScreenshot', {
                            'format': 'png', 'captureBeyondViewport': True,
                            'clip': {'x': 0, 'y': 0, 'width': g['width'],
                                     'height': driver.execute_script('return document.documentElement.scrollHeight'),
                                     'scale': 1},
                        })['data']
                        (output / f'{width}-{theme}-{name}.png').write_bytes(base64.b64decode(png))
                        require(g['body'] <= g['width'] + 1 and g['document'] <= g['width'] + 1,
                                f'page overflow: {result}')
                        require(not g['headings'], f'heading clipping: {result}')
                        require(all(float(x['radius'].removesuffix('px')) > 0 for x in g['surfaces']),
                                f'project radius token is ineffective: {result}')
                        if name.startswith('project'):
                            require(g['font'] and 'mono' in g['font'].lower(), f'project data font missing: {result}')
                            if name in ('project-gate', 'project-ravenis', 'project-occult-atlas'):
                                require('noindex' in g['noindex'], f'noindex changed: {result}')
                        if name in ('think-all', 'build-all'):
                            result['interactions'] = exercise_controls(driver, wait, kind)
    finally:
        (output / 'audit.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'screenshots': len(results), 'viewports': VIEWPORTS, 'themes': 2}))


if __name__ == '__main__':
    main()
