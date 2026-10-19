#!/usr/bin/env python3
"""UI-A12: real controls/viewport PNGs; no service fixture or backend health claim."""
import json
import os
import shutil
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait

from check_mobile_sidebar import serve
from check_think_build_visual import VIEWPORTS, settle


def dialog_metrics(driver):
    return driver.execute_script('''
      const panel=document.querySelector('#chartControlPanel');
      const command=document.querySelector('.sky-command');
      const nav=document.querySelector('[data-observe-app-nav]');
      const heading=panel.querySelector('h2');
      const rect=n=>n.getBoundingClientRect().toJSON();
      return {hidden:panel.hidden, panel:rect(panel), heading:rect(heading),
        commandZ:Number(getComputedStyle(command).zIndex),
        navZ:Number(getComputedStyle(nav).zIndex),
        scrimZ:Number(getComputedStyle(document.body,'::after').zIndex),
        width:innerWidth,height:innerHeight,
        docWidth:document.documentElement.scrollWidth,
        panelWidth:panel.clientWidth, contentWidth:panel.scrollWidth,
        focusedInside:panel.contains(document.activeElement),
        noindex:document.querySelector('meta[name="robots"]').content};
    ''')


def assert_open(metrics):
    assert not metrics['hidden']
    assert metrics['commandZ'] > max(metrics['navZ'], metrics['scrimZ']), metrics
    assert metrics['panel']['left'] >= 0 and metrics['panel']['right'] <= metrics['width'] + 1
    assert metrics['panel']['top'] >= 0 and metrics['panel']['bottom'] <= metrics['height'] + 1
    assert metrics['heading']['top'] >= metrics['panel']['top']
    assert metrics['heading']['bottom'] <= metrics['height']
    assert metrics['contentWidth'] <= metrics['panelWidth'] + 1
    assert metrics['docWidth'] <= metrics['width'] + 1
    assert 'noindex' in metrics['noindex']


def click(driver, selector):
    target = driver.find_element(By.CSS_SELECTOR, selector)
    driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", target)
    # aria-expanded updates before the desktop sidebar transition finishes.
    # Wait for the real native click point, never bypass interception with JS.
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('''
      const n=arguments[0],r=n.getBoundingClientRect();
      const hit=document.elementFromPoint(r.x+r.width/2,r.y+r.height/2);
      return r.width>0 && r.height>0 && hit && (hit===n || n.contains(hit));
    ''', target))
    target.click()


def loading_focus_metrics(driver):
    """Capture only public control state; never alter fixture timing or requests."""
    return driver.execute_script('''
      const p=document.querySelector('#chartControlPanel');
      const a=Array.from(p.querySelectorAll("button:not(:disabled), input:not(:disabled), [href], [tabindex]:not([tabindex='-1'])"))
        .filter(n=>!n.hidden && n.offsetParent!==null);
      const describe=n=>n?{tag:n.tagName,id:n.id,disabled:!!n.disabled,
        filterBody:n.dataset.filterBody||null,filterAspect:n.dataset.filterAspect||null,
        filterBodyVisibility:n.dataset.filterBodyVisibility||null}:null;
      return {at:performance.now(),active:describe(document.activeElement),
        inside:p.contains(document.activeElement),hidden:p.hidden,
        first:describe(a[0]),last:describe(a[a.length-1]),
        focusIsLast:document.activeElement===a[a.length-1],
        controls:a.map(describe),planetNodes:document.querySelectorAll('.planet-node').length,
        requestButtons:['refreshAstroButton','exportChartButton'].map(id=>describe(document.getElementById(id)))};
    ''')


def pin_loading_controls(driver):
    """Isolate the two explicitly disabled fixture controls from async callbacks."""
    driver.execute_script('''
      for(const id of ['refreshAstroButton','exportChartButton']) {
        const n=document.getElementById(id);
        if(n.__uiDisabledFixture)throw new Error('fixture already installed');
        const saved={own:Object.getOwnPropertyDescriptor(n,'disabled'),latest:n.disabled};
        n.disabled=true;
        n.__uiDisabledFixture=saved;
        Object.defineProperty(n,'disabled',{configurable:true,get(){return true;},
          set(value){saved.latest=Boolean(value);}});
      }
    ''')


def restore_loading_controls(driver):
    driver.execute_script('''
      for(const id of ['refreshAstroButton','exportChartButton']) {
        const n=document.getElementById(id),saved=n.__uiDisabledFixture;
        if(!saved)continue;
        delete n.disabled;
        if(saved.own)Object.defineProperty(n,'disabled',saved.own);
        n.disabled=saved.latest;
        delete n.__uiDisabledFixture;
      }
    ''')


def main():
    output = Path(os.environ.get('UI_OBSERVE_DIR', '/tmp/neutriverse-observe-dialog'))
    output.mkdir(parents=True, exist_ok=True)
    live = os.environ.get('UI_LIVE_BASE', '').rstrip('/')
    assert live in ('', 'https://neutriverse.uk')
    options = webdriver.ChromeOptions()
    options.binary_location = next((shutil.which(n) for n in
        ('google-chrome', 'google-chrome-stable', 'chromium') if shutil.which(n)), None)
    for flag in ('--headless=new', '--no-sandbox', '--disable-dev-shm-usage'):
        options.add_argument(flag)
    results = []
    try:
        with serve(Path(sys.argv[1]).resolve()) as port, webdriver.Chrome(options=options) as driver:
            base = live or f'http://127.0.0.1:{port}'
            wait = WebDriverWait(driver, 25)
            for width, height in VIEWPORTS:
                driver.set_window_size(width, height)
                driver.execute_cdp_cmd('Emulation.setTouchEmulationEnabled', {'enabled':width <= 768})
                for theme in ('dark', 'light'):
                    name = f'observe-dialog-{width}-{theme}'
                    row = {'name':name, 'passed':False, 'service':'unmocked; health NOT certified'}
                    results.append(row)
                    driver.get(base + '/ravenis/')
                    settle(driver, wait, theme)
                    driver.save_screenshot(str(output / (name + '-ravenis.png')))
                    click(driver, '[data-observe-app-link="occult-atlas"]')
                    wait.until(lambda d: d.find_element(By.ID, 'chartControlToggle').is_displayed())
                    wait.until(lambda d: d.execute_script('return document.documentElement.dataset.mode') == theme)
                    driver.execute_async_script('const done=arguments[arguments.length-1];document.fonts.ready.then(done);')
                    driver.save_screenshot(str(output / (name + '-atlas.png')))
                    click(driver, '#chartControlToggle')
                    wait.until(lambda d: not d.find_element(By.ID, 'chartControlPanel').get_attribute('hidden'))
                    metrics = dialog_metrics(driver)
                    row['open'] = metrics
                    driver.save_screenshot(str(output / (name + '-open.png')))
                    assert_open(metrics)
                    wait.until(lambda d: dialog_metrics(d)['focusedInside'])
                    row['initialFocus'] = driver.execute_script('return document.activeElement.id')
                    # Reproduce the old ancestor level in this disposable CI page.
                    # The same gate MUST reject it; restore the exact inline style.
                    old = driver.execute_script("const n=document.querySelector('.sky-command');const old=n.getAttribute('style');n.style.zIndex='50';return old;")
                    rejected = False
                    try:
                        assert_open(dialog_metrics(driver))
                    except AssertionError:
                        rejected = True
                    finally:
                        driver.execute_script("const n=document.querySelector('.sky-command');arguments[0]===null?n.removeAttribute('style'):n.setAttribute('style',arguments[0]);", old)
                    assert rejected, 'Gate failed to catch the UI-023 stacking fault'
                    row['oldStackRejected'] = True
                    ActionChains(driver).send_keys(Keys.TAB).perform()
                    assert dialog_metrics(driver)['focusedInside'], 'Tab must enter/stay in dialog'
                    driver.save_screenshot(str(output / (name + '-focus.png')))
                    panel = driver.find_element(By.ID, 'chartControlPanel')
                    before_scroll = driver.execute_script('return arguments[0].scrollTop;', panel)
                    ActionChains(driver).scroll_from_origin(ScrollOrigin.from_element(panel), 0, 1800).perform()
                    if driver.execute_script('return arguments[0].scrollHeight>arguments[0].clientHeight;', panel):
                        wait.until(lambda d: d.execute_script('return arguments[0].scrollTop;', panel) > before_scroll)
                    row['dialogScrollTop'] = driver.execute_script('return arguments[0].scrollTop;', panel)
                    driver.save_screenshot(str(output / (name + '-scrolled.png')))
                    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    wait.until(lambda d: d.find_element(By.ID, 'chartControlPanel').get_attribute('hidden'))
                    assert driver.execute_script('return document.activeElement.id') == 'chartControlToggle'
                    click(driver, '#chartControlToggle')
                    reopened = dialog_metrics(driver)
                    assert not reopened['hidden']
                    assert reopened['commandZ'] > max(reopened['navZ'], reopened['scrimZ'])
                    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    if width > 1100:
                        click(driver, '#sidebarToggle')
                        wait.until(lambda d: d.find_element(By.ID, 'sidebarToggle').get_attribute('aria-expanded') == 'false')
                        driver.save_screenshot(str(output / (name + '-sidebar-closed.png')))
                        click(driver, '#sidebarToggle')
                        wait.until(lambda d: d.find_element(By.ID, 'sidebarToggle').get_attribute('aria-expanded') == 'true')
                    # UI-024 deterministic loading-controls fixture only: no network
                    # interception or backend-health claim. Async callbacks may request
                    # new values; restore those latest values after this isolated fixture.
                    pin_loading_controls(driver)
                    try:
                        click(driver, '#chartControlToggle')
                        wait.until(lambda d: d.execute_script('return document.activeElement.id') == 'chartDateTime')
                        row['loadingInitialFocus'] = driver.execute_script('return document.activeElement.id')
                        driver.save_screenshot(str(output / (name + '-loading-focus.png')))
                        row['loadingBeforeReverseTab'] = loading_focus_metrics(driver)
                        assert row['loadingBeforeReverseTab']['first']['id'] == 'chartDateTime'
                        assert all(n['disabled'] for n in row['loadingBeforeReverseTab']['requestButtons'])
                        ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
                        row['loadingAfterReverseTab'] = loading_focus_metrics(driver)
                        driver.save_screenshot(str(output / (name + '-loading-wrap.png')))
                        assert row['loadingAfterReverseTab']['focusIsLast'], (
                            'Reverse Tab must wrap within loading dialog', row['loadingAfterReverseTab'])
                        row['loadingReverseTabWrapped'] = True
                        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                        wait.until(lambda d: d.find_element(By.ID, 'chartControlPanel').get_attribute('hidden'))
                        assert driver.execute_script('return document.activeElement.id') == 'chartControlToggle'
                    finally:
                        restore_loading_controls(driver)
                    click(driver, '[data-observe-app-nav] a[href="/observe/"]')
                    wait.until(lambda d: '/observe/' in d.current_url)
                    driver.back()
                    wait.until(lambda d: d.find_element(By.ID, 'chartControlToggle').is_displayed())
                    click(driver, '[data-observe-app-link="ravenis"]')
                    wait.until(lambda d: d.find_element(By.ID, 'ravenis-app').is_displayed())
                    assert driver.execute_script('return document.documentElement.dataset.mode') == theme
                    row['passed'] = True
    finally:
        (output / 'audit.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print('UI-A12: 8 dialog flows, old-stack fault rejected; real viewport PNGs need human review.')


if __name__ == '__main__':
    main()
