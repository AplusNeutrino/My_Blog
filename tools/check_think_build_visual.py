#!/usr/bin/env python3
"""Capture and check THINK states and the public BUILD facts, not private apps."""
import base64
import json
import os
import shutil
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
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
    ('observe', '/observe/', None),
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
        toggle = driver.find_element(By.ID, 'mode-toggle')
        mobile_menu = driver.find_element(By.ID, 'sidebar-trigger').is_displayed()
        if mobile_menu:
            driver.find_element(By.ID, 'sidebar-trigger').click()
            wait.until(lambda d: d.execute_script("return document.body.hasAttribute('sidebar-display')"))
        wait.until(lambda d: d.execute_script("return document.getAnimations().every(a => a.playState !== 'running' || a.effect.getTiming().iterations === Infinity)"))
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", toggle)
        driver.find_element(By.ID, 'mode-toggle').click()
        if mobile_menu:
            driver.find_element(By.ID, 'mode-toggle').send_keys(Keys.ESCAPE)
            wait.until(lambda d: d.find_element(By.ID, 'sidebar-trigger').get_attribute('aria-expanded') == 'false')
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
      const title = document.getElementById('topbar-title');
      const sidebar = document.getElementById('sidebar').getBoundingClientRect();
      const titleRect = title.getBoundingClientRect();
      const menu = document.getElementById('sidebar-trigger').getBoundingClientRect();
      const search = document.getElementById('search-trigger').getBoundingClientRect();
      return {
        title: title.textContent.trim(), titleTooltip: title.title,
        pageTitle: document.querySelector('main h1')?.textContent.trim(),
        titleVisible: visible(title), titleLeft: titleRect.left, titleRight: titleRect.right,
        menuRight: menu.right, searchLeft: search.left,
        sidebar: {left: sidebar.left, right: sidebar.right, width: sidebar.width},
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
        button = driver.find_element(By.CSS_SELECTOR, '[data-project-filter="unspecified"]')
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", button)
        button.click()
        wait.until(lambda d: visible_count(d, kind) == 6)
        button = driver.find_element(By.CSS_SELECTOR, '[data-project-filter="all"]')
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", button)
        button.click()
        wait.until(lambda d: visible_count(d, kind) == 7)
    return {'filter': True, 'refresh': True, 'back': True}


def sidebar_checks(driver, wait, base, output):
    """UI-004 short-window flow and UI-003a rapid real-pointer mask close."""
    results = []
    for width, height in ((390, 700), (768, 700), (1024, 700), (1366, 700),
                          (1024, 900), (1366, 900), (1366, 1100)):
        driver.set_window_size(width, height)
        for theme in ('dark', 'light'):
            driver.get(base + '/build/')
            settle(driver, wait, theme)
            mobile = width < 850
            if mobile:
                driver.find_element(By.ID, 'sidebar-trigger').click()
                wait.until(lambda d: d.execute_script("return document.body.hasAttribute('sidebar-display')"))
            sidebar = driver.find_element(By.ID, 'sidebar')
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', sidebar)
            wait.until(lambda d: d.execute_script("return document.getAnimations().every(a => a.playState !== 'running' || a.effect.getTiming().iterations === Infinity)"))
            g = driver.execute_script("""
              const box = s => {const r=document.querySelector(s).getBoundingClientRect();
                return {top:r.top,bottom:r.bottom};};
              const controls=[...document.querySelectorAll('.nv-sidebar-utilities .nav-link, .sidebar-bottom button, .sidebar-bottom > a')]
                .filter(e=>e.getBoundingClientRect().width>0);
              return {viewport:[innerWidth,innerHeight], primary:box('.nv-sidebar-primary'),
                utilities:box('.nv-sidebar-utility-group'), bottom:box('.sidebar-bottom'),
                scroll:document.querySelector('#sidebar').scrollTop,
                accessible:controls.map(e=>{const r=e.getBoundingClientRect(),
                  hit=document.elementFromPoint(r.left+r.width/2,r.top+r.height/2);
                  return {name:e.getAttribute('aria-label')||e.textContent.trim(),
                    hit:!!hit&&(hit===e||e.contains(hit)),top:r.top,bottom:r.bottom};})};
            """)
            row = {'window':[width,height], 'theme':theme, 'geometry':g}
            results.append(row)
            driver.save_screenshot(str(output / f'sidebar-{width}-{height}-{theme}.png'))
            require(g['primary']['bottom'] <= g['utilities']['top'] + 1, f'primary overlaps utilities: {row}')
            require(g['utilities']['bottom'] <= g['bottom']['top'] + 1, f'utility/social overlap: {row}')
            require(all(c['hit'] and c['top'] >= 0 and c['bottom'] <= g['viewport'][1]+1 for c in g['accessible']),
                    f'sidebar controls obscured: {row}')
            driver.find_element(By.ID, 'mode-toggle').click()
            other = 'light' if theme == 'dark' else 'dark'
            wait.until(lambda d: d.execute_script('return document.documentElement.dataset.mode') == other)
            if mobile:
                driver.find_element(By.ID, 'mode-toggle').send_keys(Keys.ESCAPE)
                wait.until(lambda d: d.execute_script("return !document.body.hasAttribute('sidebar-display') && document.activeElement.id==='sidebar-trigger'"))
                # No wait between pointer actions: cover the delayed-open-focus race.
                for _ in range(3):
                    trigger = driver.find_element(By.ID, 'sidebar-trigger')
                    ActionChains(driver, duration=0).click(trigger).perform()
                    # Click mask at a known point outside the 260px drawer.
                    action = ActionBuilder(driver)
                    action.pointer_action.move_to_location(width-20, 100)
                    action.pointer_action.click()
                    action.perform()
                    wait.until(lambda d: d.execute_script("return !document.body.hasAttribute('sidebar-display') && document.activeElement.id==='sidebar-trigger'"))
                    driver.execute_async_script('const done=arguments[arguments.length-1]; requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
                    require(driver.execute_script("return document.activeElement.id==='sidebar-trigger'"), 'late focus returned to closed drawer')
                row['rapidMaskClose'] = 3
            else:
                driver.find_element(By.CSS_SELECTOR, '[data-nv-search-trigger]').click()
                wait.until(lambda d: d.find_element(By.ID, 'search-input').is_displayed())
                driver.find_element(By.ID, 'search-cancel').click()
            row['themeAndSearchOrMask'] = True
    return results


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
    sidebar_results = []
    try:
        with serve(site) as port, webdriver.Chrome(options=options) as driver:
            driver.set_script_timeout(30)
            wait = WebDriverWait(driver, 20)
            live = os.environ.get('UI_LIVE_BASE', '')
            require(not live or live == 'https://neutriverse.uk', 'unexpected live audit target')
            base = live or f'http://127.0.0.1:{port}'
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
                        if name in ('think-all', 'build-all', 'observe', 'project-toyosatomimis-headphone'):
                            driver.save_screenshot(str(output / f'viewport-{width}-{theme}-{name}.png'))
                        if g['titleVisible']:
                            require(g['title'] == g['pageTitle'], f'internal layout name in topbar: {result}')
                            require(g['titleTooltip'] == g['pageTitle'], f'full title is unavailable: {result}')
                            require(g['titleLeft'] >= g['menuRight'] - 1 and
                                    g['titleRight'] <= g['searchLeft'] + 1,
                                    f'topbar controls overlap title: {result}')
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
            sidebar_results = sidebar_checks(driver, wait, base, output)
    finally:
        (output / 'audit.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
        (output / 'sidebar-audit.json').write_text(json.dumps(sidebar_results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'screenshots': len(results), 'viewports': VIEWPORTS, 'themes': 2}))


if __name__ == '__main__':
    main()
