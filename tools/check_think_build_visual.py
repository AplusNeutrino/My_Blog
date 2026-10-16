#!/usr/bin/env python3
"""Capture and check THINK states and the public BUILD facts, not private apps."""
import base64
import json
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

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
    ('library', '/library/', None),
    ('links', '/links/', None),
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


def library_visible_covers(driver, wait, output, width, theme):
    """Observe native lazy loading in the current viewport without changing it."""
    script = """
      return [...document.querySelectorAll('#pgl-grid img.pgl-cover')].filter(e=>{
        const r=e.getBoundingClientRect();return r.width>0 && r.height>0 &&
          r.bottom>0 && r.top<innerHeight && r.right>0 && r.left<innerWidth;
      }).map(e=>({src:e.currentSrc || e.src,complete:e.complete,
        naturalWidth:e.naturalWidth,naturalHeight:e.naturalHeight}));
    """
    initial = driver.execute_script(script)
    require(initial, 'no visible Library cover images to audit')
    try:
        wait.until(lambda d: all(r['complete'] for r in d.execute_script(script)))
        # complete/naturalWidth can precede decoding and the next paint when
        # the existing image uses decoding=async. Await native decoding only
        # after load; do not change src/loading or replace the browser loader.
        decoded = driver.execute_async_script("""
          const done=arguments[arguments.length-1];
          const images=[...document.querySelectorAll('#pgl-grid img.pgl-cover')].filter(e=>{
            const r=e.getBoundingClientRect();return r.width>0 && r.height>0 &&
              r.bottom>0 && r.top<innerHeight && r.right>0 && r.left<innerWidth;
          });
          Promise.all(images.map(e=>e.decode())).then(()=>{
            requestAnimationFrame(()=>requestAnimationFrame(()=>done({ok:true})));
          }).catch(error=>done({ok:false,error:String(error)}));
        """)
        require(decoded.get('ok'), f'Library cover decoding failed: {decoded}')
    finally:
        rows = driver.execute_script(script)
        (output / f'covers-{width}-{theme}-library.json').write_text(
            json.dumps({'windowWidth':width,'theme':theme,'images':rows},ensure_ascii=False,indent=2),encoding='utf-8')
        driver.save_screenshot(str(output / f'covers-{width}-{theme}-library.png'))
    require(len(rows) == len(initial) and all(r['complete'] and r['naturalWidth'] > 0
            and r['naturalHeight'] > 0 for r in rows), f'Library cover failed to load: {rows}')
    return {'visibleImages':len(rows),'loaded':True}


def library_search_controls(driver, wait, output, width, theme, query, expected_id):
    """Real input, reload, empty-state and clear; no scripted UI state writes."""
    def q_value():
        return parse_qs(urlsplit(driver.current_url).query).get('q', [''])[0]
    def input_box():
        field = driver.find_element(By.ID, 'pgl-search')
        if not field.is_displayed():
            driver.find_element(By.ID, 'pgl-search-toggle').click()
            wait.until(lambda d: d.find_element(By.ID, 'pgl-search').is_displayed())
        return driver.find_element(By.ID, 'pgl-search')
    def type_query(value):
        field = input_box()
        field.send_keys(Keys.CONTROL, 'a')
        field.send_keys(Keys.BACKSPACE)
        if value:
            field.send_keys(value)
        wait.until(lambda d: q_value() == value)
    def capture(state):
        header = driver.find_element(By.CSS_SELECTOR, '.pgl-header')
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", header)
        driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
        require(driver.execute_script('return document.documentElement.scrollWidth <= innerWidth+1'),
                f'Library {state} page overflow')
        search_geometry = driver.execute_script('''
          const rect=s=>{const r=document.querySelector(s).getBoundingClientRect();
            return {left:r.left,right:r.right,top:r.top,bottom:r.bottom};};
          return {heading:rect('.pgl-heading-block'),search:rect('#pgl-search-box'),
            header:rect('.pgl-header')};
        ''')
        driver.save_screenshot(str(output / f'search-{state}-{width}-{theme}-library.png'))
        (output / f'search-{state}-{width}-{theme}-library.json').write_text(
            json.dumps(search_geometry, indent=2))
        heading, search, bounds = (search_geometry[k] for k in ('heading','search','header'))
        overlap = (min(heading['right'],search['right']) > max(heading['left'],search['left'])+1
                   and min(heading['bottom'],search['bottom']) > max(heading['top'],search['top'])+1)
        require(not overlap, f'Library {state} search overlaps heading/subtitle')
        require(search['bottom'] <= bounds['bottom']+1,
                f'Library {state} search escapes header into following content')
    type_query(query)
    wait.until(lambda d: expected_id in [e.get_attribute('data-pgl-id') for e in d.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card')])
    search_url = driver.current_url
    driver.refresh()
    wait.until(lambda d: d.find_element(By.ID, 'pgl-search').get_attribute('value') == query)
    wait.until(lambda d: expected_id in [e.get_attribute('data-pgl-id') for e in d.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card')])
    require(driver.current_url == search_url, 'Library search reload changed URL')
    capture('results')
    sentinel = 'neutriverse-ui-audit-no-match-008c'
    type_query(sentinel)
    wait.until(lambda d: bool(d.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-empty')))
    require(not driver.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card'), 'Library empty query retained cards')
    require(driver.find_element(By.CSS_SELECTOR, '#pgl-grid .pgl-empty').text.strip(), 'Library empty message missing')
    capture('empty')
    type_query('')
    wait.until(lambda d: d.find_element(By.ID, 'pgl-root-view').is_displayed())
    require(not urlsplit(driver.current_url).query, 'Library clear did not restore root URL')
    capture('cleared')
    return {'query':query,'expectedId':expected_id,'reloadPreserved':True,
            'emptyMessage':True,'clearRestoredRoot':True}


def library_filter_pagination_controls(driver, wait, output, width, theme):
    """UI-007: preserve the actual second-page IDs across a full reload."""
    def ids():
        return [e.get_attribute('data-pgl-id') for e in driver.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card')]
    def params():
        return parse_qs(urlsplit(driver.current_url).query)
    def ready():
        wait.until(lambda d: not d.find_element(By.ID, 'prospero-great-library').get_attribute('aria-busy'))
    def position(element):
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", element)
        driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
    def click(selector):
        element = driver.find_element(By.CSS_SELECTOR, selector)
        position(element)
        wait.until(lambda d: d.execute_script('const e=arguments[0],r=e.getBoundingClientRect();return e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));', element))
        element.click()
    def capture(state, selector):
        position(driver.find_element(By.CSS_SELECTOR, selector))
        geometry = driver.execute_script('''
          const panel=document.querySelector('.pgl-advanced-panel'),r=panel.getBoundingClientRect();
          return {scrollX,viewport:innerWidth,open:document.querySelector('.pgl-advanced').open,
            panel:{left:r.left,right:r.right,top:r.top,bottom:r.bottom},
            years:[...document.querySelectorAll('#pgl-grid .pgl-meta')].map(e=>({visible:e.innerText,text:e.textContent}))};
        ''')
        driver.save_screenshot(str(output / f'filters-{state}-{width}-{theme}-library.png'))
        (output / f'filters-{state}-{width}-{theme}-library.json').write_text(json.dumps(geometry, indent=2))
        if geometry['open']:
            require(geometry['panel']['left'] >= -1 and geometry['panel']['right'] <= geometry['viewport']+1,
                    f'Library {state} advanced panel outside viewport: {geometry}')
        require(abs(geometry['scrollX']) <= 1, f'Library {state} horizontal scroll offset: {geometry}')
        require(driver.execute_script('return document.documentElement.scrollWidth <= innerWidth+1'),
                f'Library {state} page overflow')
    def open_filters():
        if not driver.find_element(By.CSS_SELECTOR, '.pgl-advanced').get_attribute('open'):
            click('.pgl-advanced summary')
        wait.until(lambda d: d.find_element(By.ID, 'pgl-source').is_displayed())

    ready()
    first_page = ids()
    require(first_page, 'Library first page empty')
    next_selector = '#pgl-pagination .pgl-page-nav:last-child'
    require(driver.find_element(By.CSS_SELECTOR, next_selector).is_enabled(), 'Library needs a real second page')
    click(next_selector)
    wait.until(lambda d: params().get('page') == ['2'] and ids() and ids() != first_page)
    second_page, second_url = ids(), driver.current_url
    require(not set(first_page).intersection(second_page), 'Library pages repeat IDs')
    driver.refresh()
    ready()
    wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '#pgl-pagination [aria-current="page"]'))
    require(driver.find_element(By.CSS_SELECTOR, '#pgl-pagination [aria-current="page"]').text == '2',
            'Library reload lost page 2 despite page URL')
    require(driver.current_url == second_url and ids() == second_page, 'Library reload changed second-page IDs or URL')
    capture('page2', '#pgl-pagination')
    click('#pgl-pagination .pgl-page-nav:first-child')
    wait.until(lambda d: ids() == first_page and 'page' not in params())
    open_filters()
    capture('open', '.pgl-advanced-panel')
    Select(driver.find_element(By.ID, 'pgl-source')).select_by_value('bangumi')
    wait.until(lambda d: params().get('source') == ['bangumi'] and ids())
    ready()
    years = driver.execute_script("return [...document.querySelectorAll('#pgl-grid .pgl-meta span')].map(e=>e.textContent.trim()).filter(t=>/^\\d{4}$/.test(t));")
    require(years, 'Library public source has no year fixture')
    selected_year = years[0]
    Select(driver.find_element(By.ID, 'pgl-year')).select_by_value(selected_year)
    wait.until(lambda d: params().get('year') == [selected_year] and ids())
    ready()
    filtered_ids, filtered_url = ids(), driver.current_url
    year_texts = [e.get_attribute('textContent') for e in driver.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-meta')]
    require(year_texts and all(selected_year in text for text in year_texts),
            f'Library year filter contains mismatched card year: {selected_year}, {year_texts}')
    driver.refresh()
    ready()
    wait.until(lambda d: ids() == filtered_ids)
    require(driver.current_url == filtered_url, 'Library filter reload changed URL')
    require(Select(driver.find_element(By.ID, 'pgl-source')).first_selected_option.get_attribute('value') == 'bangumi', 'Library source selection lost')
    require(Select(driver.find_element(By.ID, 'pgl-year')).first_selected_option.get_attribute('value') == selected_year, 'Library year selection lost')
    open_filters()
    capture('combined', '.pgl-advanced-panel')
    click('#pgl-clear-filters')
    wait.until(lambda d: ids() == first_page and 'source' not in params() and 'year' not in params())
    click('.pgl-advanced summary')
    capture('cleared', '.pgl-view-toolbar')
    return {'page2ReloadIds':True,'previousPageRestored':True,'source':'bangumi',
            'year':selected_year,'filterReloadIds':True,'clearRestored':True}


def library_sort_layout_controls(driver, wait, output, width, theme):
    """Real sort/layout controls; keep the locked in-progress-first grouping."""
    def ids():
        return [e.get_attribute('data-pgl-id') for e in driver.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card')]
    def ready():
        wait.until(lambda d: not d.find_element(By.ID, 'prospero-great-library').get_attribute('aria-busy') and ids())
    def position(element):
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", element)
        driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
    def sort(key):
        element = driver.find_element(By.ID, 'pgl-sort')
        position(element)
        Select(element).select_by_value(key)
        wait.until(lambda d: parse_qs(urlsplit(d.current_url).query).get('sort', ['updated']) == [key])
        ready()
        require('page' not in parse_qs(urlsplit(driver.current_url).query), 'Library sort retained page')
    def capture(state):
        position(driver.find_element(By.CSS_SELECTOR, '.pgl-view-toolbar'))
        geometry = driver.execute_script('''
          return {scrollX,viewport:innerWidth,page:document.documentElement.scrollWidth,
            list:document.querySelector('#pgl-grid').classList.contains('is-list'),
            gridPressed:document.querySelector('#pgl-layout-grid').getAttribute('aria-pressed'),
            listPressed:document.querySelector('#pgl-layout-list').getAttribute('aria-pressed'),
            cards:[...document.querySelectorAll('#pgl-grid .pgl-card')].map(e=>{
              const r=e.getBoundingClientRect();return {id:e.dataset.pglId,status:e.dataset.status,
                left:r.left,right:r.right,client:e.clientWidth,scroll:e.scrollWidth,
                title:e.querySelector('.pgl-card-title').textContent,
                meta:[...e.querySelectorAll('.pgl-meta span')].map(s=>s.textContent.trim())};})};
        ''')
        driver.save_screenshot(str(output / f'sort-layout-{state}-{width}-{theme}-library.png'))
        (output / f'sort-layout-{state}-{width}-{theme}-library.json').write_text(json.dumps(geometry, indent=2))
        require(abs(geometry['scrollX']) <= 1 and geometry['page'] <= geometry['viewport']+1, 'Library sort/layout page overflow')
        require(all(c['left'] >= -1 and c['right'] <= geometry['viewport']+1 and c['scroll'] <= c['client']+1
                    for c in geometry['cards']), f'Library {state} card overflow: {geometry}')
        require(geometry['listPressed'] == str(geometry['list']).lower() and
                geometry['gridPressed'] == str(not geometry['list']).lower(), 'Library layout pressed state mismatch')
        return geometry
    def numeric_order(geometry, key):
        groups = {}
        ranks = []
        for card in geometry['cards']:
            rank = 0 if card['status'] == 'in_progress' else 1
            ranks.append(rank)
            values = card['meta']
            if key == 'rating':
                value = next((float(t.replace('★', '').strip()) for t in values if t.startswith('★')), -1)
            else:
                value = next((int(t) for t in values if len(t) == 4 and t.isdigit()), 0)
            groups.setdefault(rank, []).append(value)
        require(ranks == sorted(ranks), 'Library lost in-progress priority')
        require(all(values == sorted(values, reverse=True) for values in groups.values()), f'Library {key} order incorrect: {groups}')

    ready()
    initial_ids = ids()
    sort('rating')
    numeric_order(capture('rating'), 'rating')
    sort('year')
    numeric_order(capture('year'), 'year')
    sort('title')
    title_ids, title_url = ids(), driver.current_url
    button = driver.find_element(By.ID, 'pgl-layout-list')
    position(button)
    button.click()
    require(ids() == title_ids, 'Library list toggle changed IDs')
    require(capture('list')['list'], 'Library list toggle failed')
    driver.refresh()
    ready()
    require(driver.current_url == title_url and ids() == title_ids, 'Library title sort reload lost URL/IDs')
    require(Select(driver.find_element(By.ID, 'pgl-sort')).first_selected_option.get_attribute('value') == 'title', 'Library reload lost selected sort')
    require(capture('reloaded')['list'], 'Library reload lost list preference')
    button = driver.find_element(By.ID, 'pgl-layout-grid')
    position(button)
    button.send_keys(Keys.ENTER)
    require(not driver.find_element(By.ID, 'pgl-grid').get_attribute('class').split().count('is-list'), 'Library keyboard grid restore failed')
    require(ids() == title_ids, 'Library grid restore changed IDs')
    sort('updated')
    require(ids() == initial_ids, 'Library default sort did not restore initial IDs')
    return {'ratingOrder':True,'yearOrder':True,'titleReloadIds':True,'listKeepsIds':True,
            'listReloadPreference':True,'keyboardGridRestored':True,'defaultRestored':True}


def library_other_status_controls(driver, wait, output, width, theme):
    """Read-only public status navigation; clear filters intentionally keeps status."""
    def params():
        return parse_qs(urlsplit(driver.current_url).query)
    def ids():
        return [e.get_attribute('data-pgl-id') for e in driver.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card')]
    def ready():
        wait.until(lambda d: not d.find_element(By.ID, 'prospero-great-library').get_attribute('aria-busy'))
    def position(element):
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", element)
        driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
    def click(selector):
        element = driver.find_element(By.CSS_SELECTOR, selector)
        position(element)
        wait.until(lambda d: d.execute_script('const e=arguments[0],r=e.getBoundingClientRect();return e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));', element))
        element.click()
    def open_filters():
        if not driver.find_element(By.CSS_SELECTOR, '.pgl-advanced').get_attribute('open'):
            click('.pgl-advanced summary')
        wait.until(lambda d: d.find_element(By.CSS_SELECTOR, '[data-pgl-status="on_hold"]').is_displayed())
    def close_filters():
        if driver.find_element(By.CSS_SELECTOR, '.pgl-advanced').get_attribute('open'):
            click('.pgl-advanced summary')
    def verify(category, status):
        wait.until(lambda d: params().get('category') == [category] and params().get('status') == [status])
        ready()
        cards = driver.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card')
        require(all(c.get_attribute('data-category') == category and c.get_attribute('data-status') == status
                    for c in cards), 'Library status/category leaked records')
        if not cards:
            empty = driver.find_element(By.CSS_SELECTOR, '#pgl-grid .pgl-empty')
            require(empty.is_displayed() and empty.text.strip(), 'Library empty status has no visible message')
        else:
            require(all(c.find_element(By.CSS_SELECTOR, '.pgl-status').text.strip() for c in cards), 'Library status label missing')
        require(driver.find_element(By.ID, 'pgl-browser-title').text.strip(), 'Library status heading missing')
    def reload_same(category, status):
        expected, url = ids(), driver.current_url
        driver.refresh()
        verify(category, status)
        require(driver.current_url == url and ids() == expected, 'Library status reload lost URL/IDs')
    def capture(state):
        position(driver.find_element(By.CSS_SELECTOR, '.pgl-view-toolbar'))
        geometry = driver.execute_script('''
          const panel=document.querySelector('.pgl-advanced-panel'),p=panel.getBoundingClientRect();
          return {scrollX,viewport:innerWidth,page:document.documentElement.scrollWidth,
            open:document.querySelector('.pgl-advanced').open,panel:{left:p.left,right:p.right},
            heading:document.querySelector('#pgl-browser-title').textContent,
            empty:document.querySelector('#pgl-grid .pgl-empty')?.textContent||'',
            cards:[...document.querySelectorAll('#pgl-grid .pgl-card')].map(e=>{
              const r=e.getBoundingClientRect();return {id:e.dataset.pglId,category:e.dataset.category,status:e.dataset.status,
                left:r.left,right:r.right,client:e.clientWidth,scroll:e.scrollWidth};})};
        ''')
        driver.save_screenshot(str(output / f'other-status-{state}-{width}-{theme}-library.png'))
        (output / f'other-status-{state}-{width}-{theme}-library.json').write_text(json.dumps(geometry, indent=2))
        require(abs(geometry['scrollX']) <= 1 and geometry['page'] <= geometry['viewport']+1, 'Library status page overflow')
        require(all(c['left'] >= -1 and c['right'] <= geometry['viewport']+1 and c['scroll'] <= c['client']+1
                    for c in geometry['cards']), 'Library status card overflow')
        if geometry['open']:
            require(geometry['panel']['left'] >= -1 and geometry['panel']['right'] <= geometry['viewport']+1,
                    'Library status panel outside viewport')

    ready()
    book_ids = ids()
    require(book_ids, 'Library book fixture empty before status audit')
    open_filters()
    click('[data-pgl-status="on_hold"]')
    verify('book', 'on_hold')
    book_empty = not ids()
    reload_same('book', 'on_hold')
    capture('book-hold')
    click('#pgl-back')
    wait.until(lambda d: d.find_element(By.ID, 'pgl-root-view').is_displayed())
    click('[data-pgl-category="game"]')
    wait.until(lambda d: params().get('category') == ['game'] and ids())
    open_filters()
    click('[data-pgl-status="on_hold"]')
    verify('game', 'on_hold')
    require(ids(), 'Library game hold fixture empty')
    reload_same('game', 'on_hold')
    capture('game-hold')
    open_filters()
    click('[data-pgl-status="dropped"]')
    verify('game', 'dropped')
    require(ids(), 'Library game dropped fixture empty')
    reload_same('game', 'dropped')
    dropped_ids = ids()
    capture('game-dropped')
    element = driver.find_element(By.ID, 'pgl-sort')
    position(element)
    Select(element).select_by_value('rating')
    wait.until(lambda d: params().get('sort') == ['rating'])
    ready()
    open_filters()
    click('#pgl-clear-filters')
    verify('game', 'dropped')
    require(ids() == dropped_ids and all(k not in params() for k in ('source', 'year', 'sort', 'page')),
            'Library clear filters did not keep status and restore its default sort')
    close_filters()
    capture('cleared')
    click('#pgl-back')
    wait.until(lambda d: d.find_element(By.ID, 'pgl-root-view').is_displayed())
    require('status' not in params() and 'category' not in params(), 'Library back retained status/category')
    click('[data-pgl-category="book"]')
    ready()
    wait.until(lambda d: ids() == book_ids)
    return {'bookHoldEmpty':book_empty,'bookHoldReloadIds':True,'gameHoldReloadIds':True,
            'gameDroppedReloadIds':True,'statusCategoryIsolation':True,'clearKeepsStatus':True,
            'clearDefaultIds':True,'backRestoresBook':True}


def library_wishlist_controls(driver, wait, output, width, theme):
    """Navigate the real public ledger; counts/fixtures come from current data."""
    def params():
        return parse_qs(urlsplit(driver.current_url).query)
    def ids():
        return [e.get_attribute('data-pgl-id') for e in driver.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card')]
    def ready():
        wait.until(lambda d: not d.find_element(By.ID, 'prospero-great-library').get_attribute('aria-busy'))
    def position(element):
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", element)
        driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
    def click(selector):
        element = driver.find_element(By.CSS_SELECTOR, selector)
        position(element)
        wait.until(lambda d: d.execute_script('const e=arguments[0],r=e.getBoundingClientRect();return e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));', element))
        element.click()
    def index():
        wait.until(lambda d: params().get('view') == ['wishlist'] and 'category' not in params())
        ready()
        require(driver.find_element(By.ID, 'pgl-wishlist-ledger').is_displayed(), 'Wishlist ledger missing')
        require(not driver.find_element(By.ID, 'pgl-card-view').is_displayed(), 'Wishlist index leaked stale cards')
        links = driver.find_elements(By.CSS_SELECTOR, '[data-pgl-wishlist-category]')
        counts = {e.get_attribute('data-pgl-wishlist-category'): int(e.find_element(By.CSS_SELECTOR, '.pgl-ledger-count').text.split()[0]) for e in links}
        require(set(counts) == {'book','comic','movie','drama','anime','game','music'}, 'Wishlist category ledger incomplete')
        require(sum(counts.values()) == int(driver.find_element(By.ID, 'pgl-result-count').text.split()[0]), 'Wishlist ledger total differs from categories')
        return counts
    def category_view(category, count):
        wait.until(lambda d: params().get('view') == ['wishlist'] and params().get('category') == [category])
        ready()
        require(driver.find_element(By.ID, 'pgl-card-view').is_displayed(), 'Wishlist cards hidden')
        require(not driver.find_element(By.ID, 'pgl-wishlist-ledger').is_displayed(), 'Wishlist category leaked ledger')
        cards = driver.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card')
        page_size = int(driver.find_element(By.ID, 'prospero-great-library').get_attribute('data-page-size') or 24)
        require(len(cards) == min(count, page_size), 'Wishlist category count/page differs from ledger')
        require(int(driver.find_element(By.ID, 'pgl-result-count').text.split()[0]) == count, 'Wishlist result total differs from ledger')
        require(all(c.get_attribute('data-category') == category and c.get_attribute('data-status') == 'wishlist' for c in cards), 'Wishlist status/category isolation failed')
        if not cards:
            empty = driver.find_element(By.CSS_SELECTOR, '#pgl-grid .pgl-empty')
            require(empty.is_displayed() and empty.text.strip(), 'Wishlist empty category has no message')
        return ids()
    def capture(state):
        position(driver.find_element(By.ID, 'pgl-browser-title'))
        wait.until(lambda d: d.execute_script('''return [...document.querySelectorAll('#pgl-grid img')].every(e=>{
          const r=e.getBoundingClientRect();return r.bottom<=0||r.top>=innerHeight||e.complete&&e.naturalWidth>0;});''') if d.find_element(By.ID, 'pgl-card-view').is_displayed() else True)
        geometry = driver.execute_script('''
          const selector=document.querySelector('#pgl-wishlist-ledger').hidden?'#pgl-grid .pgl-card':'[data-pgl-wishlist-category]';
          return {scrollX,viewport:innerWidth,page:document.documentElement.scrollWidth,
            heading:document.querySelector('#pgl-browser-title').textContent,
            empty:document.querySelector('#pgl-grid .pgl-empty')?.textContent||'',
            elements:[...document.querySelectorAll(selector)].map(e=>{const r=e.getBoundingClientRect();
              return {id:e.dataset.pglId||e.dataset.pglWishlistCategory,category:e.dataset.category,status:e.dataset.status,
                left:r.left,right:r.right,client:e.clientWidth,scroll:e.scrollWidth};})};
        ''')
        driver.save_screenshot(str(output / f'wishlist-{state}-{width}-{theme}-library.png'))
        (output / f'wishlist-{state}-{width}-{theme}-library.json').write_text(json.dumps(geometry, indent=2))
        require(abs(geometry['scrollX']) <= 1 and geometry['page'] <= geometry['viewport']+1, 'Wishlist page overflow')
        require(all(e['left'] >= -1 and e['right'] <= geometry['viewport']+1 and e['scroll'] <= e['client']+1
                    for e in geometry['elements']), 'Wishlist element overflow')

    ready()
    book_ids = ids()
    require(book_ids, 'Wishlist audit starts without book records')
    click('#pgl-back')
    wait.until(lambda d: d.find_element(By.ID, 'pgl-root-view').is_displayed())
    click('[data-pgl-wishlist]')
    counts = index()
    capture('index')
    nonempty = min((c for c in counts if counts[c] > 0), key=lambda c: counts[c])
    click(f'[data-pgl-wishlist-category="{nonempty}"]')
    expected = category_view(nonempty, counts[nonempty])
    require(expected, 'Wishlist nonempty fixture missing')
    capture('category')
    url = driver.current_url
    driver.refresh()
    category_view(nonempty, counts[nonempty])
    require(driver.current_url == url and ids() == expected, 'Wishlist reload lost URL/IDs')
    capture('reloaded')
    click('#pgl-back')
    require(index() == counts, 'Wishlist back changed ledger counts')
    empty_categories = [c for c in counts if counts[c] == 0]
    empty_category = empty_categories[0] if empty_categories else None
    if empty_category:
        click(f'[data-pgl-wishlist-category="{empty_category}"]')
        category_view(empty_category, 0)
        capture('empty')
        driver.refresh()
        category_view(empty_category, 0)
        click('#pgl-back')
        require(index() == counts, 'Wishlist empty back lost ledger')
    click('#pgl-back')
    wait.until(lambda d: d.find_element(By.ID, 'pgl-root-view').is_displayed())
    require(not params(), 'Wishlist two-level back retained URL state')
    click('[data-pgl-category="book"]')
    ready()
    wait.until(lambda d: ids() == book_ids)
    return {'ledgerCounts':counts,'nonemptyCategory':nonempty,'emptyCategory':empty_category,
            'categoryStatusIsolation':True,'reloadIds':True,'twoLevelBack':True,'restoredBookIds':True}


def library_rating_controls(driver, wait, output, width, theme):
    """Exercise public rating scopes and real keyboard tooltips, not synthetic focus."""
    distribution = json.loads(Path('_data/prospero_great_library/stats.json').read_text())['rating_curve_distribution']
    bins, scopes = distribution['bins'], distribution['scopes']
    def position(element):
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", element)
        driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
    def ready():
        wait.until(lambda d: not d.find_element(By.ID, 'prospero-great-library').get_attribute('aria-busy'))
    def verify(scope):
        counts = scopes[scope]
        expected = [f'{b}: {n}' for b, n in zip(bins, counts)]
        def matching_snapshot(d):
            # Both existing renderers replace SVG children after a refresh.
            # Read one DOM task, not WebElements that may detach between calls.
            snapshot = rating_chart_snapshot(d)
            return snapshot if (snapshot['hits'] == expected and snapshot['area']
                                and snapshot['active'] == [scope]
                                and snapshot['summary'].strip()) else False
        snapshot = wait.until(matching_snapshot)
        require(snapshot['active'] == [scope], 'Multiple rating scopes active')
        require(snapshot['labels'] == [str(b) for b in bins], 'Rating axis bins differ from data')
        summary = snapshot['summary']
        numbers = [float(v) for v in re.findall(r'\d+(?:\.\d+)?', summary)]
        total = sum(counts)
        require(numbers and numbers[0] == total, 'Rating summary total differs from data')
        if total:
            mean = sum(float(b)*n for b,n in zip(bins,counts))/total
            peak = bins[counts.index(max(counts))]
            require(len(numbers) == 3 and abs(numbers[1]-mean) <= .051 and numbers[2] == peak, 'Rating mean/peak differs from distribution')
        else:
            require(len(numbers) == 1, 'Empty rating summary retained mean/peak')
        return {'counts':counts,'summary':summary}
    def choose(scope):
        element = driver.find_element(By.CSS_SELECTOR, f'[data-rating-scope="{scope}"]')
        position(element)
        wait.until(lambda d: d.execute_script('const e=arguments[0],r=e.getBoundingClientRect();return e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));',element))
        element.click()
        ready()
        return verify(scope)
    def tooltip(index):
        wait.until(lambda d: d.execute_script('return document.activeElement === document.querySelectorAll("#pgl-rating-chart .pgl-chart-hit")[arguments[0]]', index))
        wait.until(lambda d: d.find_element(By.ID, 'pgl-rating-tooltip').is_displayed())
        text = driver.find_element(By.ID, 'pgl-rating-tooltip').text
        require(text.startswith(f'{bins[index]} · {scopes["all"][index]} '), 'Keyboard rating tooltip differs from focused bin')
    def capture(state):
        position(driver.find_element(By.CSS_SELECTOR, '.pgl-rating-section'))
        geometry = driver.execute_script('''
          const rect=e=>{const r=e.getBoundingClientRect();return {left:r.left,right:r.right,top:r.top,bottom:r.bottom,client:e.clientWidth,scroll:e.scrollWidth};};
          const tip=document.querySelector('#pgl-rating-tooltip');
          return {scrollX,viewport:innerWidth,clientViewport:document.documentElement.clientWidth,page:document.documentElement.scrollWidth,
            shell:rect(document.querySelector('.pgl-rating-chart-shell')),
            chart:rect(document.querySelector('#pgl-rating-chart')),scopes:rect(document.querySelector('#pgl-rating-scopes')),
            summary:document.querySelector('#pgl-rating-summary').textContent,
            tooltip:{...rect(tip),visible:!tip.hidden,text:tip.textContent},
            focused:document.activeElement.getAttribute('aria-label')};
        ''')
        driver.save_screenshot(str(output / f'rating-{state}-{width}-{theme}-library.png'))
        (output / f'rating-{state}-{width}-{theme}-library.json').write_text(json.dumps(geometry, indent=2))
        require(abs(geometry['scrollX']) <= 1 and geometry['page'] <= geometry['viewport']+1, 'Rating chart page overflow')
        for key in ('chart','scopes'):
            r = geometry[key]
            require(r['left'] >= -1 and r['right'] <= geometry['viewport']+1 and r['scroll'] <= r['client']+1, 'Rating chart/scope overflow')
        if geometry['tooltip']['visible']:
            r = geometry['tooltip']
            require(r['left'] >= -1 and r['right'] <= geometry['viewport']+1, 'Rating tooltip outside viewport')
            require(r['left'] >= -1 and r['right'] <= geometry['clientViewport']+1,
                    'Rating tooltip clipped by usable viewport/scrollbar')
            require(r['left'] >= geometry['shell']['left']-1 and r['right'] <= geometry['shell']['right']+1,
                    'Rating tooltip outside chart shell')

    results = {}
    for scope in ('all','book','comic','movie','drama','anime','game','music'):
        results[scope] = choose(scope)
        if scope in ('book','music'):
            capture(scope)
    choose('all')
    all_button = driver.find_element(By.CSS_SELECTOR, '[data-rating-scope="all"]')
    position(all_button)
    all_button.send_keys(Keys.SHIFT, Keys.TAB)
    tooltip(len(bins)-1)
    capture('tooltip-last')
    for _ in range(len(bins)-1):
        ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
    tooltip(0)
    capture('tooltip-first')
    for _ in bins:
        ActionChains(driver).send_keys(Keys.TAB).perform()
    wait.until(lambda d: not d.find_element(By.ID, 'pgl-rating-tooltip').is_displayed())
    require(driver.execute_script('return document.activeElement === arguments[0]', driver.find_element(By.CSS_SELECTOR, '[data-rating-scope="all"]')), 'Rating keyboard exit did not reach scope button')
    choose('book')
    driver.refresh()
    ready()
    verify('all')
    return {'scopes':results,'keyboardEndpoints':True,'tooltipBlurHidden':True,'reloadDefaultAll':True}


def rating_chart_snapshot(driver):
    """Atomic read-only DOM sample: never return replaceable SVG WebElements."""
    return driver.execute_script('''
      const chart=document.querySelector('#pgl-rating-chart');
      return {hits:[...chart.querySelectorAll('.pgl-chart-hit')].map(e=>e.getAttribute('aria-label').split(' ').slice(1).join(' ')),
        labels:[...chart.querySelectorAll('.pgl-chart-label')].map(e=>e.textContent),
        area:Boolean(chart.querySelector('.pgl-chart-area')),
        active:[...document.querySelectorAll('[data-rating-scope].is-active')].map(e=>e.dataset.ratingScope),
        summary:document.querySelector('#pgl-rating-summary').textContent};
    ''')


def library_timeline_controls(driver, wait, output, width, theme):
    """Load public history through real controls, including reload and keyboard."""
    def rows():
        return [e.get_attribute('textContent') for e in
                driver.find_elements(By.CSS_SELECTOR, '#pgl-timeline li')]

    def settle(element):
        driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", element)
        driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
        wait.until(lambda d: d.execute_script('const e=arguments[0],r=e.getBoundingClientRect();return r.top>=0 && r.bottom<=innerHeight && e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));', element))

    def capture(state, anchor):
        settle(anchor)
        geometry = driver.execute_script("""
          const root=document.querySelector('#pgl-timeline');
          const button=document.querySelector('#back-to-top');
          const b=button?.getBoundingClientRect();
          const style=button && getComputedStyle(button);
          const buttonVisible=!!b && b.width>0 && b.height>0 &&
            style.display!=='none' && style.visibility!=='hidden' && Number(style.opacity)>0;
          const textRects=[];
          const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
          while(walker.nextNode()){
            const node=walker.currentNode;
            if(!node.textContent.trim())continue;
            const range=document.createRange();range.selectNodeContents(node);
            for(const r of range.getClientRects()){
              if(r.width>0 && r.height>0 && r.bottom>0 && r.top<innerHeight)
                textRects.push({left:r.left,right:r.right,top:r.top,bottom:r.bottom,text:node.textContent});
            }
          }
          const overlaps=buttonVisible ? textRects.filter(r=>
            r.left<b.right && r.right>b.left && r.top<b.bottom && r.bottom>b.top) : [];
          return {width:innerWidth,scrollX,body:document.body.scrollWidth,
            document:document.documentElement.scrollWidth,
            backToTop:buttonVisible ? {left:b.left,right:b.right,top:b.top,bottom:b.bottom}:null,
            textRects,overlaps,
            rows:[...root.querySelectorAll('li')].map(e=>{
              const r=e.getBoundingClientRect();return {left:r.left,right:r.right,
                client:e.clientWidth,scroll:e.scrollWidth,text:e.textContent};
            })};
        """)
        (output / f'timeline-{state}-{width}-{theme}-library.json').write_text(
            json.dumps(geometry,ensure_ascii=False,indent=2),encoding='utf-8')
        driver.save_screenshot(str(output / f'timeline-{state}-{width}-{theme}-library.png'))
        require(geometry['backToTop'], 'Library timeline fixed-button scenario not active')
        require(not geometry['overlaps'],
                f'Library timeline text covered by back-to-top: {geometry["overlaps"]}')
        require(abs(geometry['scrollX']) <= 1, 'Library timeline shifted horizontally')
        require(max(geometry['body'],geometry['document']) <= geometry['width']+1,
                'Library timeline page overflow')
        require(all(r['left'] >= -1 and r['right'] <= geometry['width']+1 and
                    r['scroll'] <= r['client']+1 for r in geometry['rows']),
                'Library timeline row overflow')

    require(not rows(), 'Library timeline unexpectedly loaded before activation')
    button = driver.find_element(By.ID, 'pgl-load-timeline')
    settle(button)
    button.click()
    wait.until(lambda d: rows())
    expected = rows()
    require(0 < len(expected) <= 100 and all(re.match(r'^\d{4}-\d{2}-\d{2} · .+ · .+', t) for t in expected),
            'Library timeline dates or event labels missing')
    capture('start', driver.find_element(By.CSS_SELECTOR, '#pgl-timeline li:first-child'))
    capture('tail', driver.find_element(By.CSS_SELECTOR, '#pgl-timeline li:last-child'))
    # The shipped UI is a one-shot lazy loader: replaceChildren(list) removes
    # its button. Do not click that detached element or invent a reload control.
    require(not driver.find_elements(By.ID, 'pgl-load-timeline'),
            'Library timeline loader remained after successful replacement')
    require(len(driver.find_elements(By.CSS_SELECTOR, '#pgl-timeline ul')) == 1,
            'Library timeline rendered duplicate lists')
    require(rows() == expected, 'Library timeline scrolling changed rows')
    driver.refresh()
    wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '#pgl-current-list [data-open-pgl]'))
    require(not rows(), 'Library reload did not reset lazy timeline')
    button = driver.find_element(By.ID, 'pgl-load-timeline')
    settle(button)
    button.send_keys(Keys.ENTER)
    wait.until(lambda d: rows())
    require(rows() == expected, 'Library keyboard reload changed timeline rows')
    capture('reloaded', driver.find_element(By.CSS_SELECTOR, '#pgl-timeline li:first-child'))
    return {'rows':len(expected),'oneShotLoaderReplaced':True,'singleList':True,
            'scrollSameRows':True,'reloadLazy':True,'keyboardSameRows':True}


def relationship_controls(driver, wait, name, output, width, theme):
    """Limited public Library browsing and friend-card inspection, no external writes."""
    if name == 'links':
        cards = driver.find_elements(By.CSS_SELECTOR, '.about-friend-node')
        require(cards, 'friend cards missing')
        require(all(c.get_attribute('href').startswith(('https://', 'http://')) for c in cards),
                'friend URL missing')
        # Element.send_keys re-focuses its target before each call: sending
        # Shift+Tab to the card itself moves away from it, not back to it.
        # Traverse the actual page tab order without JS focus or navigation.
        for _ in range(80):
            if driver.execute_script('return document.activeElement === arguments[0]', cards[0]):
                break
            ActionChains(driver).send_keys(Keys.TAB).perform()
        require(driver.execute_script('return document.activeElement === arguments[0]', cards[0]),
                'friend card keyboard focus unavailable')
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        require(driver.execute_script('return document.activeElement === arguments[0]', cards[0]),
                'friend card reverse tab return unavailable')
        driver.save_screenshot(str(output / f'focus-{width}-{theme}-links.png'))
        return {'friendCards': len(cards), 'hrefsPresent': True, 'keyboardFocus': True,
                'externalDestinations': 'not-verified'}
    current = driver.find_elements(By.CSS_SELECTOR, '#pgl-current-list [data-open-pgl]')
    require(current, 'Library current entries missing')
    current[0].click()
    dialog = driver.find_element(By.ID, 'pgl-drawer')
    wait.until(lambda d: dialog.get_attribute('open') is not None)
    wait.until(lambda d: d.execute_script("return document.getAnimations().every(a=>a.playState !== 'running' || a.effect.getTiming().iterations === Infinity)"))
    require(driver.find_element(By.CSS_SELECTOR, '#pgl-drawer-content h2').text,
            'Library drawer title missing')
    box = driver.execute_script('const r=arguments[0].getBoundingClientRect();return {x:r.x,y:r.y,right:r.right,bottom:r.bottom,w:innerWidth,h:innerHeight}', dialog)
    require(box['x'] >= -1 and box['y'] >= -1 and box['right'] <= box['w']+1 and box['bottom'] <= box['h']+1,
            f'Library drawer outside viewport: {box}')
    driver.save_screenshot(str(output / f'drawer-{width}-{theme}-library.png'))
    dialog.find_element(By.CSS_SELECTOR, '.pgl-close').click()
    wait.until(lambda d: dialog.get_attribute('open') is None)
    # The dialog close event asynchronously restores opener focus, which can
    # scroll the document back after WebDriver has begun its next click.
    wait.until(lambda d: d.execute_script('return document.activeElement === arguments[0]', current[0]))
    driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
    category = driver.find_element(By.CSS_SELECTOR, '[data-pgl-category="book"]')
    driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", category)
    wait.until(lambda d: d.execute_script("const e=arguments[0],r=e.getBoundingClientRect();return r.y>=0 && r.bottom<=innerHeight && e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));", category))
    category.click()
    wait.until(lambda d: d.find_element(By.ID, 'pgl-browser-view').is_displayed())
    wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '#pgl-grid .pgl-card'))
    require('category=book' in driver.current_url, 'Library category URL not stored')
    back = driver.find_element(By.ID, 'pgl-back')
    # Category navigation starts a smooth scroll. Cancel/settle that scroll
    # before screenshot and the real pointer click, not by bypassing hit tests.
    driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", back)
    driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
    wait.until(lambda d: d.execute_script("const e=arguments[0],r=e.getBoundingClientRect();return r.y>=0 && r.bottom<=innerHeight && e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));", back))
    covers = library_visible_covers(driver, wait, output, width, theme)
    driver.save_screenshot(str(output / f'category-{width}-{theme}-library.png'))
    first = driver.find_element(By.CSS_SELECTOR, '#pgl-grid .pgl-card')
    query = first.find_element(By.CSS_SELECTOR, '.pgl-card-title').text
    expected_id = first.get_attribute('data-pgl-id')
    filters_pagination = library_filter_pagination_controls(driver, wait, output, width, theme)
    sort_layout = library_sort_layout_controls(driver, wait, output, width, theme)
    other_status = library_other_status_controls(driver, wait, output, width, theme)
    wishlist = library_wishlist_controls(driver, wait, output, width, theme)
    back = driver.find_element(By.ID, 'pgl-back')
    driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", back)
    driver.execute_async_script('const done=arguments[arguments.length-1];requestAnimationFrame(()=>requestAnimationFrame(()=>done(true)));')
    back.click()
    wait.until(lambda d: d.find_element(By.ID, 'pgl-root-view').is_displayed())
    require('category=' not in driver.current_url, 'Library back retained category')
    search_result = library_search_controls(driver, wait, output, width, theme, query, expected_id)
    rating_result = library_rating_controls(driver, wait, output, width, theme)
    timeline_result = library_timeline_controls(driver, wait, output, width, theme)
    return {'drawerOpenClose': True, 'categoryOpenBack': True, 'covers':covers, 'search':search_result,
            'filtersPagination':filters_pagination,'sortLayout':sort_layout,'otherStatus':other_status,'wishlist':wishlist,'rating':rating_result,'timeline':timeline_result}


def clipboard_text(driver, value=None):
    """Read/write only the isolated audit browser's real clipboard, no API mock."""
    result = driver.execute_async_script("""
      const value = arguments[0], done = arguments[arguments.length - 1];
      const operation = value === null ? navigator.clipboard.readText()
        : navigator.clipboard.writeText(value).then(() => value);
      operation.then(text => done({ok:true,text}))
        .catch(error => done({ok:false,error:String(error)}));
    """, value)
    require(result.get('ok'), f'clipboard operation failed: {result}')
    return result['text']


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
            # W3C move_to_location takes viewport coordinates; WebElement.rect
            # uses document coordinates after scrolling far down an article.
            box = driver.execute_script('const r=arguments[0].getBoundingClientRect(); return {x:r.x,y:r.y,width:r.width,height:r.height}', current(driver))
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
    # Prevent a previous scene's clipboard contents from producing a false pass.
    sentinel = f'neutriverse-audit-before-copy:{width}:{theme}:{name}'
    clipboard_text(driver, sentinel)
    require(clipboard_text(driver) == sentinel, 'clipboard sentinel not stored')
    copy.click()
    expected = copy.get_attribute('data-title-succeed')
    wait.until(lambda d: any(t.text == expected for t in d.find_elements(By.CSS_SELECTOR, '.tooltip-inner')))
    actual = wait.until(lambda d: (text if (text := clipboard_text(d)) != sentinel else False))
    require(actual == driver.current_url, f'copied URL mismatch: {actual!r}')
    result.update({'copyLinkFeedback': True, 'clipboardBytes': 'verified',
                   'copiedUrl': actual, 'clipboardSentinelReplaced': True})
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
            # This permission applies only to the disposable audit origin/browser.
            driver.execute_cdp_cmd('Browser.grantPermissions', {
                'origin': base,
                'permissions': ['clipboardReadWrite', 'clipboardSanitizedWrite'],
            })
            for width, height in VIEWPORTS:
                driver.set_window_size(width, height)
                driver.execute_cdp_cmd('Emulation.setTouchEmulationEnabled', {
                    'enabled': width <= 768, 'maxTouchPoints': 1,
                })
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
                        if name == 'library':
                            wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '#pgl-current-list [data-open-pgl]'))
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
                        if name in ('think-all', 'build-all', 'observe', 'project-toyosatomimis-headphone', 'tags', 'archives', 'thoughts', 'series-directory', 'library', 'links'):
                            driver.save_screenshot(str(output / f'viewport-{width}-{theme}-{name}.png'))
                        if g['titleVisible'] and not name.startswith('article-') and name not in ('library', 'links'):
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
                        if name in ('library', 'links'):
                            try:
                                result['interactions'] = relationship_controls(driver, wait, name, output, width, theme)
                            except Exception:
                                driver.save_screenshot(str(output / 'relationship-failure.png'))
                                failure = driver.execute_script("""
                                  const e=document.querySelector('[data-pgl-category="book"]'),r=e?.getBoundingClientRect();
                                  const a=document.activeElement;
                                  return {url:location.href,focus:a.id,focusTag:a.tagName,focusClass:a.className,focusHref:a.getAttribute('href'),
                                    drawerOpen:document.querySelector('#pgl-drawer')?.open,
                                    scrollY,viewport:[innerWidth,innerHeight],
                                    category:r?{x:r.x,y:r.y,w:r.width,h:r.height}:null};
                                """)
                                (output / 'relationship-failure.json').write_text(json.dumps(failure,ensure_ascii=False,indent=2),encoding='utf-8')
                                raise
                        if name in ('article-code', 'article-images'):
                            try:
                                result['interactions'] = reading_controls(driver, wait, name, output, width, theme)
                            except Exception:
                                driver.save_screenshot(str(output / 'reading-failure.png'))
                                (output / 'reading-failure.json').write_text(json.dumps({
                                    'scene': name, 'window': [width,height], 'theme': theme,
                                    'url': driver.current_url, 'dialog': bool(driver.find_elements(By.ID, 'glightbox-body')),
                                    'touch': driver.execute_script('return {points:navigator.maxTouchPoints,events:"ontouchstart" in window}'),
                                }, ensure_ascii=False, indent=2), encoding='utf-8')
                                raise
            sidebar_results = sidebar_checks(driver, wait, base, output)
    finally:
        (output / 'audit.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
        (output / 'sidebar-audit.json').write_text(json.dumps(sidebar_results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'screenshots': len(results), 'viewports': VIEWPORTS, 'themes': 2}))


if __name__ == '__main__':
    main()
