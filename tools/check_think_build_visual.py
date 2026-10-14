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
    ('tags', '/tags/', None),
    ('archives', '/archives/', None),
    ('thoughts', '/thoughts/', None),
    ('series-directory', '/think/#nv-series-browser-title', None),
    ('article-tables', '/posts/%E8%AE%A1%E7%BB%84-04/', None),
    ('article-code', '/posts/%E8%AE%A1%E7%BB%84-07/', None),
    ('article-images', '/posts/FF1%E8%AE%B0%E5%BD%95/', None),
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
    # Visiting an article through Archive deliberately stores a collapsed
    # desktop sidebar. Reopen it through its public control before auditing.
    if not driver.find_element(By.ID, 'sidebar-trigger').is_displayed():
        recalls = driver.find_elements(By.CSS_SELECTOR, '.site-sidebar-recall')
        if recalls and recalls[0].is_displayed():
            recalls[0].click()
            wait.until(lambda d: not d.execute_script("return document.querySelector('#sidebar').inert"))
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
                wait.until(lambda d: d.execute_script("return document.body.hasAttribute('sidebar-display') && document.querySelector('#sidebar').contains(document.activeElement)"))
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
                    # Begin on a stable closed shell. Its menu trigger moves during
                    # Chirpy's closing transition; clicking it mid-move can miss.
                    wait.until(lambda d: d.execute_script("return document.getAnimations().every(a => a.playState !== 'running' || a.effect.getTiming().iterations === Infinity)"))
                    trigger = driver.find_element(By.ID, 'sidebar-trigger')
                    ActionChains(driver, duration=0).click(trigger).perform()
                    # Click mask at a known point outside the 260px drawer.
                    action = ActionBuilder(driver)
                    action.pointer_action.move_to_location(width-20, 100)
                    action.pointer_action.click()
                    action.perform()
                    try:
                        wait.until(lambda d: d.execute_script("return !document.body.hasAttribute('sidebar-display') && document.activeElement.id==='sidebar-trigger'"))
                    except Exception:
                        row['failureState'] = driver.execute_script("""
                          const r = document.querySelector('#sidebar-trigger').getBoundingClientRect();
                          return {open:document.body.hasAttribute('sidebar-display'),
                            focus:document.activeElement.id, trigger:[r.left,r.top,r.right,r.bottom],
                            hit:document.elementFromPoint(innerWidth-20,100)?.id};
                        """)
                        (output / 'sidebar-failure.json').write_text(json.dumps(row, ensure_ascii=False, indent=2), encoding='utf-8')
                        driver.save_screenshot(str(output / 'sidebar-failure.png'))
                        raise
                    driver.execute_async_script('const done=arguments[arguments.length-1]; requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
                    require(driver.execute_script("return document.activeElement.id==='sidebar-trigger'"), 'late focus returned to closed drawer')
                row['rapidMaskClose'] = 3
            else:
                driver.find_element(By.CSS_SELECTOR, '[data-nv-search-trigger]').click()
                wait.until(lambda d: d.find_element(By.ID, 'search-input').is_displayed())
                driver.find_element(By.ID, 'search-cancel').click()
            row['themeAndSearchOrMask'] = True
    return results


def retrieval_controls(driver, wait, name):
    original = driver.current_url
    if name == 'tags':
        links = driver.find_elements(By.CSS_SELECTOR, '.tag-ledger-entry')
        link = max(links, key=lambda e: len(e.text))
    elif name == 'archives':
        link = driver.find_element(By.CSS_SELECTOR, '.archive-entry-title')
    elif name == 'series-directory':
        link = driver.find_element(By.CSS_SELECTOR, '[data-writing-series-link]')
        expected = int(link.find_element(By.CSS_SELECTOR, 'strong').text)
    else:
        fragments = driver.find_elements(By.CSS_SELECTOR, '.thought-fragment-card[id]')
        require(len(fragments) == 5, 'original Thoughts records missing')
        target = fragments[-1]
        driver.get(original.split('#')[0] + '#' + target.get_attribute('id'))
        wait.until(lambda d: d.execute_script('return location.hash') != '')
        driver.back()
        wait.until(lambda d: d.current_url == original)
        return {'stableAnchor': True, 'back': True}
    destination = link.get_attribute('href')
    driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", link)
    link.send_keys(Keys.ENTER)
    # The existing in-page Series filter preserves the directory's hash.
    wait.until(lambda d: d.current_url.split('#')[0] == destination.split('#')[0])
    if name == 'series-directory':
        wait.until(lambda d: visible_count(d, 'think') == expected)
    else:
        wait.until(lambda d: bool(d.find_elements(By.CSS_SELECTOR, 'main h1')))
    driver.back()
    wait.until(lambda d: d.current_url == original)
    return {'open': True, 'back': True, 'destination': destination}


def load_reading_images(driver, wait):
    images = driver.find_elements(By.CSS_SELECTOR, 'article img')
    require(len(images) == 3, 'representative image inventory changed')
    for img in images:
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", img)
        wait.until(lambda d: d.execute_script('return arguments[0].complete && arguments[0].naturalWidth > 0', img))
    return images


def reading_controls(driver, wait, name, output, width, theme):
    original = driver.current_url
    result = {}
    if name == 'article-code':
        code = driver.find_element(By.CSS_SELECTOR, 'article .content pre code')
        require('LOAD 005' in code.text and 'HALT' in code.text, 'code text missing')
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", code)
        driver.save_screenshot(str(output / f'viewport-{width}-{theme}-{name}.png'))
        result['codeVisible'] = True
    else:
        images = load_reading_images(driver, wait)
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", images[1])
        driver.save_screenshot(str(output / f'viewport-{width}-{theme}-{name}.png'))
        images[1].find_element(By.XPATH, '..').click()
        current = lambda d: d.find_element(By.CSS_SELECTOR, '#glightbox-body .gslide.current img')
        wait.until(lambda d: current(d).get_attribute('src').endswith('FF1-02.jpg'))
        wait.until(lambda d: d.execute_script('return arguments[0].complete && arguments[0].naturalWidth > 0', current(d)))
        wait.until(lambda d: d.execute_script("return document.getAnimations().every(a=>a.playState !== 'running' || a.effect.getTiming().iterations === Infinity)"))
        driver.save_screenshot(str(output / f'gallery-{width}-{theme}.png'))
        def gallery_step(direction):
            button = driver.find_element(By.CSS_SELECTOR, '#glightbox-body ' + ('.gnext' if direction == 'next' else '.gprev'))
            if button.is_displayed():
                button.click()
                return 'pointer-button'
            # GLightbox hides arrows on narrow touch layouts; use its actual
            # touch navigation rather than clicking a hidden control.
            from selenium.webdriver.common.actions.pointer_input import PointerInput
            box = current(driver).rect
            start = box['x'] + box['width'] * (0.8 if direction == 'next' else 0.2)
            end = box['x'] + box['width'] * (0.2 if direction == 'next' else 0.8)
            y = box['y'] + box['height'] * 0.5
            action = ActionBuilder(driver, mouse=PointerInput('touch', 'reading-swipe'))
            action.pointer_action.move_to_location(int(start), int(y))
            action.pointer_action.pointer_down()
            action.pointer_action.move_to_location(int(end), int(y))
            action.pointer_action.pointer_up()
            action.perform()
            return 'touch-swipe'
        next_method = gallery_step('next')
        wait.until(lambda d: current(d).get_attribute('src').endswith('FF1-03.jpg'))
        wait.until(lambda d: d.execute_script('return arguments[0].complete && arguments[0].naturalWidth > 0', current(d)))
        wait.until(lambda d: d.execute_script("return document.getAnimations().every(a=>a.playState !== 'running' || a.effect.getTiming().iterations === Infinity)"))
        previous_method = gallery_step('previous')
        wait.until(lambda d: current(d).get_attribute('src').endswith('FF1-02.jpg'))
        wait.until(lambda d: d.execute_script("return document.getAnimations().every(a=>a.playState !== 'running' || a.effect.getTiming().iterations === Infinity)"))
        driver.find_element(By.CSS_SELECTOR, '#glightbox-body .gclose').click()
        wait.until(lambda d: not d.find_elements(By.ID, 'glightbox-body'))
        require(driver.current_url == original, 'gallery changed article URL')
        result.update({'imagesLoaded': 3, 'galleryNextPreviousClose': True,
                       'nextInput': next_method, 'previousInput': previous_method})
    copy = driver.find_element(By.ID, 'copy-link')
    driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", copy)
    copy.click()
    expected = copy.get_attribute('data-title-succeed')
    wait.until(lambda d: any(t.text == expected for t in d.find_elements(By.CSS_SELECTOR, '.tooltip-inner')))
    result.update({'copyLinkFeedback': True, 'clipboardBytes': 'not-verified'})
    driver.save_screenshot(str(output / f'copy-feedback-{width}-{theme}-{name}.png'))
    return result


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
                        print(json.dumps({'scene':name,'window':[width,height],'theme':theme}), flush=True)
                        try:
                            settle(driver, wait, theme)
                        except Exception:
                            driver.save_screenshot(str(output / 'scene-failure.png'))
                            failure = driver.execute_script("""
                              const e=document.querySelector('#mode-toggle'),r=e?.getBoundingClientRect();
                              return {url:location.href,mode:document.documentElement.dataset.mode,
                                open:document.body.hasAttribute('sidebar-display'),focus:document.activeElement.id,
                                toggle:r?{x:r.x,y:r.y,w:r.width,h:r.height,display:getComputedStyle(e).display}:null};
                            """)
                            (output / 'scene-failure.json').write_text(json.dumps(failure,ensure_ascii=False,indent=2),encoding='utf-8')
                            raise
                        kind = 'think' if name.startswith('think') else 'build'
                        if count is not None:
                            wait.until(lambda d: visible_count(d, kind) == count)
                        if name == 'article-images':
                            load_reading_images(driver, wait)
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
                        if name == 'series-directory':
                            driver.execute_script("document.querySelector('[data-writing-series-browser]').scrollIntoView({behavior:'instant',block:'center'});")
                        if name == 'article-tables':
                            tables = driver.find_elements(By.CSS_SELECTOR, 'article .content table')
                            require(len(tables) == 2, 'legacy Markdown tables rendered as pipe prose')
                            driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", tables[0])
                            driver.save_screenshot(str(output / f'viewport-{width}-{theme}-{name}.png'))
                            wrappers = driver.find_elements(By.CSS_SELECTOR, 'article .content .table-wrapper')
                            require(len(wrappers) == 2, 'reading tables lost horizontal containment')
                            result['tables'] = driver.execute_script("""
                              return [...document.querySelectorAll('article .content .table-wrapper')].map(n=>({
                                width:n.clientWidth, scrollWidth:n.scrollWidth, overflow:getComputedStyle(n).overflowX}));
                            """)
                            require(all(x['overflow'] in ('auto', 'scroll') for x in result['tables']), 'tables not scrollable')
                            # Real pointer-wheel horizontal scrolling, not a JS click/scroll substitute.
                            scrollable = next((w for w in wrappers if driver.execute_script('return arguments[0].scrollWidth > arguments[0].clientWidth', w)), None)
                            if scrollable:
                                from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
                                driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", scrollable)
                                ActionChains(driver).scroll_from_origin(ScrollOrigin.from_element(scrollable), 400, 0).perform()
                                wait.until(lambda d: d.execute_script('return arguments[0].scrollLeft', scrollable) > 0)
                            result['interactions'] = {'tableScroll': bool(scrollable), 'tables': 2}
                        if name in ('think-all', 'build-all', 'observe', 'project-toyosatomimis-headphone', 'tags', 'archives', 'thoughts', 'series-directory'):
                            driver.save_screenshot(str(output / f'viewport-{width}-{theme}-{name}.png'))
                        if g['titleVisible'] and not name.startswith('article-'):
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
                        if name in ('tags', 'archives', 'thoughts', 'series-directory'):
                            result['interactions'] = retrieval_controls(driver, wait, name)
                        if name in ('article-code', 'article-images'):
                            try:
                                result['interactions'] = reading_controls(driver, wait, name, output, width, theme)
                            except Exception:
                                driver.save_screenshot(str(output / 'reading-failure.png'))
                                (output / 'reading-failure.json').write_text(json.dumps({
                                    'scene': name, 'window': [width,height], 'theme': theme,
                                    'url': driver.current_url, 'dialog': bool(driver.find_elements(By.ID, 'glightbox-body')),
                                }, ensure_ascii=False, indent=2), encoding='utf-8')
                                raise
            sidebar_results = sidebar_checks(driver, wait, base, output)
    finally:
        (output / 'audit.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
        (output / 'sidebar-audit.json').write_text(json.dumps(sidebar_results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'screenshots': len(results), 'viewports': VIEWPORTS, 'themes': 2}))


if __name__ == '__main__':
    main()
