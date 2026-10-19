#!/usr/bin/env python3
"""Real Chrome controls/screenshots; only the like service is an explicit fixture.

The fixture lives in this disposable browser profile, never posts production likes,
and is NOT evidence that the remote service is healthy. All page JS/CSS is real.
"""
import json
import os
import shutil
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from check_mobile_sidebar import serve
from check_think_build_visual import VIEWPORTS, settle


FIXTURE = r'''
(() => {
  const realFetch = window.fetch.bind(window);
  window.fetch = (input, options = {}) => {
    const url = new URL(typeof input === 'string' ? input : input.url, location.href);
    if (url.origin !== 'https://neutriverse-stats.feiyuzou-me.workers.dev'
        || !['/likes','/like'].includes(url.pathname)) return realFetch(input, options);
    const counts = JSON.parse(sessionStorage.getItem('uia11-counts') || '{}');
    const calls = JSON.parse(sessionStorage.getItem('uia11-calls') || '[]');
    const method = options.method || 'GET';
    const key = method === 'POST' ? JSON.parse(options.body).path : url.searchParams.get('path');
    calls.push({method, key});
    if (method === 'POST') counts[key] = (counts[key] || 0) + 1;
    sessionStorage.setItem('uia11-counts', JSON.stringify(counts));
    sessionStorage.setItem('uia11-calls', JSON.stringify(calls));
    return Promise.resolve(new Response(JSON.stringify({likes:counts[key] || 0}),
      {status:200,headers:{'Content-Type':'application/json'}}));
  };
})();
'''


def state(driver):
    return driver.execute_script('''return [...document.querySelectorAll('[data-post-like]')].map(r => ({
      key:r.dataset.likeKey, count:r.querySelector('[data-like-count]').textContent,
      pressed:r.querySelector('button').getAttribute('aria-pressed'),
      disabled:r.querySelector('button').disabled,
      focused:r.querySelector('button') === document.activeElement
    }));''')


def capture(driver, output, name, states):
    driver.save_screenshot(str(output / (name + '.png')))
    states[name] = state(driver)
    metrics = driver.execute_cdp_cmd('Page.getLayoutMetrics', {})['cssContentSize']
    shot = driver.execute_cdp_cmd('Page.captureScreenshot', {'format':'png',
        'captureBeyondViewport':True, 'clip':{'x':0,'y':0,'width':metrics['width'],
        'height':metrics['height'],'scale':1}})
    import base64
    (output / (name + '-full.png')).write_bytes(base64.b64decode(shot['data']))


def main():
    output = Path(os.environ.get('UI_LIKES_DIR', '/tmp/neutriverse-thought-likes'))
    output.mkdir(parents=True, exist_ok=True)
    live = os.environ.get('UI_LIVE_BASE', '').rstrip('/')
    if live not in ('', 'https://neutriverse.uk'):
        raise AssertionError('Only the requested public live origin is allowed')
    options = webdriver.ChromeOptions()
    options.binary_location = next((shutil.which(n) for n in
        ('google-chrome','google-chrome-stable','chromium') if shutil.which(n)), None)
    for option in ('--headless=new','--no-sandbox','--disable-dev-shm-usage'):
        options.add_argument(option)
    results = []
    try:
        with serve(Path(sys.argv[1]).resolve()) as port, webdriver.Chrome(options=options) as driver:
            driver.set_script_timeout(30)
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source':FIXTURE})
            wait = WebDriverWait(driver, 20)
            url = (live or f'http://127.0.0.1:{port}') + '/thoughts/'
            for width, height in VIEWPORTS:
                driver.set_window_size(width, height)
                driver.execute_cdp_cmd('Emulation.setTouchEmulationEnabled', {'enabled':width <= 768})
                for theme in ('dark','light'):
                    name = f'thought-likes-{width}-{theme}'
                    driver.get(url)
                    # This profile is created solely for this audit, not a user session.
                    driver.execute_script('localStorage.clear(); sessionStorage.clear();')
                    driver.refresh()
                    settle(driver, wait, theme)
                    settings = driver.execute_script('''return [...document.querySelectorAll('[data-post-like]')]
                      .map(r => [r.dataset.likeEndpoint, r.dataset.likeCountPath, r.dataset.likeHitPath]);''')
                    assert settings == [['https://neutriverse-stats.feiyuzou-me.workers.dev',
                        '/likes', '/like']] * 5, 'Fixture scope changed; refuse any real like POST'
                    states = {}
                    results.append({'name':name,'fixture':'likes-only; remote health NOT verified',
                                    'states':states,'passed':False})
                    wait.until(lambda d: len(state(d)) == 5 and all(r['count'] == '0' for r in state(d)))
                    assert all(r['pressed'] == 'false' for r in state(driver))
                    capture(driver, output, name+'-initial', states)
                    buttons = driver.find_elements(By.CSS_SELECTOR, '[data-post-like] button')
                    buttons[0].click()
                    wait.until(lambda d: state(d)[0]['pressed'] == 'true')
                    assert [r['count'] for r in state(driver)] == ['1','0','0','0','0']
                    # Native Tab from the clicked first button must reach the next like.
                    buttons[0].send_keys(Keys.TAB)
                    assert state(driver)[1]['focused'], 'Native Tab did not reach second like'
                    capture(driver, output, name+'-keyboard-focus', states)
                    buttons[1].send_keys(Keys.SPACE)
                    wait.until(lambda d: state(d)[1]['pressed'] == 'true')
                    buttons[0].click()
                    ActionChains(driver).move_to_element(buttons[2]).perform()
                    capture(driver, output, name+'-liked-hover', states)
                    assert [r['count'] for r in state(driver)] == ['1','1','0','0','0']
                    driver.refresh()
                    settle(driver, wait, theme)
                    wait.until(lambda d: [r['count'] for r in state(d)] == ['1','1','0','0','0'])
                    assert [r['pressed'] for r in state(driver)] == ['true','true','false','false','false']
                    assert all(not r['disabled'] for r in state(driver))
                    capture(driver, output, name+'-refresh', states)
                    calls = driver.execute_script("return JSON.parse(sessionStorage.getItem('uia11-calls'))")
                    assert len([c for c in calls if c['method'] == 'POST']) == 2
                    assert len({r['key'] for r in state(driver)}) == 5
                    results[-1].update(passed=True, calls=calls,
                        viewport=driver.execute_script('return {width:innerWidth,height:innerHeight}'))
    finally:
        (output / 'audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Thoughts likes: 8 fixture flows, actual click/Tab/Space/hover/refresh; screenshots require human review.')


if __name__ == '__main__':
    main()
