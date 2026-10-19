#!/usr/bin/env python3
"""UI-A12c natural service flows. No response/chart/disabled-state fixture.

Datetime filling is explicit form setup, not native date-picker acceptance.
All activation uses native pointer or CDP touch, and screenshots need human review.
"""
import json
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlsplit

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from check_mobile_sidebar import serve
from check_observe_dialog import assert_open, click, dialog_metrics
from check_think_build_visual import VIEWPORTS, settle


def service_route(url):
    """Only the configured public now endpoint; exclude query/fragment/userinfo."""
    try:
        parsed = urlsplit(url)
        if (parsed.scheme == 'https' and parsed.netloc == 'occult-atlas.onrender.com'
                and parsed.path == '/api/astrology/now'):
            return 'https://occult-atlas.onrender.com/api/astrology/now'
    except (TypeError, ValueError):
        pass
    return None


def summarize_service_events(entries, console):
    """Reduce already observed events; no requests, headers, body or full logs."""
    events = []
    malformed = 0
    for entry in entries:
        try:
            event = json.loads(entry['message'])['message']
            if not isinstance(event, dict) or not isinstance(event.get('params', {}), dict):
                malformed += 1
                continue
            events.append(event)
        except (ValueError, KeyError, TypeError):
            malformed += 1
    by_id = {}
    for event in events:
        params = event.get('params', {})
        if event.get('method') == 'Network.requestWillBeSent':
            request = params.get('request', {})
            route = service_route(request.get('url', ''))
            if route:
                by_id[params['requestId']] = {'route':route,
                    'method':request.get('method'), 'events':[]}
    for event in events:
        params = event.get('params', {})
        row = by_id.get(params.get('requestId'))
        if row is None:
            continue
        method = event.get('method')
        if method == 'Network.responseReceived':
            row['events'].append({'kind':'response','status':params.get('response', {}).get('status')})
        elif method == 'Network.responseReceivedExtraInfo':
            row['events'].append({'kind':'response-extra','status':params.get('statusCode')})
        elif method == 'Network.loadingFailed':
            row['events'].append({'kind':'failed',
                'networkCodes':re.findall(r'net::ERR_[A-Z_0-9]+', params.get('errorText', '')),
                'blockedReason':params.get('blockedReason'),
                'corsError':params.get('corsErrorStatus', {}).get('corsError')})
        elif method == 'Network.loadingFinished':
            row['events'].append({'kind':'finished'})
    console_flags = []
    for entry in console:
        text = entry.get('message', '')
        if 'https://occult-atlas.onrender.com/api/astrology/now' in text:
            console_flags.append({'level':entry.get('level'), 'corsMentioned':'CORS' in text,
                'networkCodes':re.findall(r'net::ERR_[A-Z_0-9]+', text)})
    return {'requests':list(by_id.values()),'consoleFlags':console_flags,
            'malformedEvents':malformed, 'missingRequests':not bool(by_id)}


def service_failure(driver):
    """Diagnostic errors must never replace the original failed gate."""
    result = {'diagnosticErrors':[]}
    logs = {}
    for kind in ('performance', 'browser'):
        try:
            logs[kind] = driver.get_log(kind)
        except Exception as error:
            result['diagnosticErrors'].append({'source':kind,'type':type(error).__name__})
            logs[kind] = []
    try:
        result.update(summarize_service_events(logs['performance'], logs['browser']))
    except Exception as error:
        result['diagnosticErrors'].append({'source':'reducer','type':type(error).__name__})
        result['missingRequests'] = True
    return result


def snapshot(driver):
    return driver.execute_script('''
      const q=s=>document.querySelector(s),r=n=>n.getBoundingClientRect().toJSON();
      return {theme:document.documentElement.dataset.mode,width:innerWidth,height:innerHeight,
        docWidth:document.documentElement.scrollWidth,title:q('#chartTitle').textContent,
        status:q('#astroStatus').textContent,state:q('#chartState').dataset.state||null,
        stateHidden:q('#chartState').hidden,nodes:document.querySelectorAll('.planet-node').length,
        planetRows:q('#astroPlanetTable').querySelectorAll('button').length,
        aspectRows:q('#astroAspectList').querySelectorAll('button').length,
        details:[...document.querySelectorAll('details.sky-data-panel')].map(n=>({
          open:n.open,summary:n.querySelector('summary').textContent.trim(),rect:r(n)})),
        date:q('#chartDateTime').value,label:q('#chartLocationLabel').value,
        history:[...q('#chartHistoryList').querySelectorAll('.history-row')].map(n=>n.textContent.trim()),
        disabled:['refreshAstroButton','exportChartButton','chartQueryButton','resetToNowButton']
          .map(id=>document.getElementById(id).disabled),
        noindex:q('meta[name="robots"]').content};
    ''')


def assert_ready(data, historical=False):
    assert data['stateHidden'] and data['state'] is None, data
    assert not any(data['disabled']), data
    assert data['nodes'] == 10 and data['planetRows'] > 0, data
    assert ('历史星盘' in data['title']) == historical, data
    if historical:
        assert '2020/01/01 12:00' in data['status'], data
        assert data['date'] == '2020-01-01T12:00', data
    else:
        assert '实时星盘' in data['title'], data
        assert data['label'] == '', data


def wait_ready(driver, historical=False):
    # Product owns its unchanged 45-second timeout. No blind retry/keep-alive.
    def ready(d):
        data = snapshot(d)
        assert data['state'] != 'error', data
        if not data['stateHidden'] or any(data['disabled']):
            return False
        assert_ready(data, historical)
        return data
    return WebDriverWait(driver, 55).until(ready)


def activate(driver, selector, touch):
    if not touch:
        click(driver, selector)
        return
    element = driver.find_element(By.CSS_SELECTOR, selector)
    driver.execute_script("arguments[0].scrollIntoView({behavior:'instant',block:'center'});", element)
    def point(d):
        return d.execute_script('''
          const n=arguments[0],r=n.getBoundingClientRect(),x=r.x+r.width/2,y=r.y+r.height/2;
          const hit=document.elementFromPoint(x,y);
          return x>=0 && y>=0 && x<innerWidth && y<innerHeight && hit &&
            (hit===n || n.contains(hit)) ? {x,y}:null;
        ''', element)
    xy = WebDriverWait(driver, 10).until(point)
    driver.execute_cdp_cmd('Input.dispatchTouchEvent', {'type':'touchStart',
        'touchPoints':[dict(xy, radiusX=1, radiusY=1, force=1, id=0)]})
    driver.execute_cdp_cmd('Input.dispatchTouchEvent', {'type':'touchEnd','touchPoints':[]})


def capture(driver, output, name, row):
    data = snapshot(driver)
    row['states'][name] = data
    # Save actual viewport before asserting so failures still have visual evidence.
    driver.save_screenshot(str(output / (name + '.png')))
    assert data['docWidth'] <= data['width'] + 1, data
    assert 'noindex' in data['noindex'], data
    return data


def close_panel(driver, touch):
    # A request disables its pressed button and may leave body focused.
    # Restore a real in-panel keyboard target before using the native Escape path.
    driver.find_element(By.ID, 'chartDateTime').send_keys(Keys.ESCAPE)
    WebDriverWait(driver, 10).until(lambda d:
        d.find_element(By.ID, 'chartControlPanel').get_attribute('hidden'))
    assert driver.execute_script('return document.activeElement.id') == 'chartControlToggle'


def main():
    output = Path(os.environ.get('UI_OBSERVE_HISTORY_DIR', '/tmp/neutriverse-observe-history'))
    output.mkdir(parents=True, exist_ok=True)
    live = os.environ.get('UI_LIVE_BASE', '').rstrip('/')
    assert live in ('', 'https://neutriverse.uk')
    options = webdriver.ChromeOptions()
    options.set_capability('goog:loggingPrefs', {'performance':'ALL', 'browser':'ALL'})
    options.binary_location = next((shutil.which(n) for n in
        ('google-chrome', 'google-chrome-stable', 'chromium') if shutil.which(n)), None)
    for flag in ('--headless=new', '--no-sandbox', '--disable-dev-shm-usage', '--lang=en-US'):
        options.add_argument(flag)
    results = []
    try:
        with serve(Path(sys.argv[1]).resolve()) as port, webdriver.Chrome(options=options) as driver:
            driver.set_script_timeout(30)
            driver.execute_cdp_cmd('Network.enable', {})
            driver.execute_cdp_cmd('Emulation.setTimezoneOverride', {'timezoneId':'UTC'})
            base = live or f'http://127.0.0.1:{port}'
            wait = WebDriverWait(driver, 25)
            for width, height in VIEWPORTS:
                driver.set_window_size(width, height)
                driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride',
                    {'width':width,'height':height,'deviceScaleFactor':1,'mobile':False})
                touch = width <= 768
                driver.execute_cdp_cmd('Emulation.setTouchEmulationEnabled', {'enabled':touch})
                for theme in ('dark', 'light'):
                    name = f'observe-history-{width}-{theme}'
                    row = {'name':name,'passed':False,'states':{},
                        'input':'CDP touch' if touch else 'native pointer',
                        'service':'unmocked; no astronomy or general health certification',
                        'formSetup':'datetime value + input/change events; date-picker typing NOT verified'}
                    results.append(row)
                    try:
                        driver.get(base + '/ravenis/')
                        settle(driver, wait, theme)
                        activate(driver, '[data-observe-app-link="occult-atlas"]', touch)
                        wait.until(lambda d: d.find_element(By.ID, 'chartControlToggle').is_displayed())
                        wait.until(lambda d: d.execute_script('return document.documentElement.dataset.mode') == theme)
                        driver.execute_async_script('const done=arguments[arguments.length-1];document.fonts.ready.then(done);')
                        wait_ready(driver)
                        assert snapshot(driver)['history'] == [], 'Disposable profile must start without history'
                        for index in (1, 2):
                            summary = f'details.sky-data-panel:nth-child({index}) > summary'
                            details = f'details.sky-data-panel:nth-child({index})'
                            # Mobile may initially collapse details: normalize via native control.
                            if driver.find_element(By.CSS_SELECTOR, details).get_attribute('open'):
                                activate(driver, summary, touch)
                            wait.until(lambda d: not d.find_element(By.CSS_SELECTOR, details).get_attribute('open'))
                            data = capture(driver, output, name + f'-collapsed-{index}', row)
                            assert data['nodes'] == 10
                            activate(driver, summary, touch)
                            wait.until(lambda d: d.find_element(By.CSS_SELECTOR, details).get_attribute('open'))
                        capture(driver, output, name + '-expanded', row)
                        activate(driver, '#chartControlToggle', touch)
                        wait.until(lambda d: not d.find_element(By.ID, 'chartControlPanel').get_attribute('hidden'))
                        assert_open(dialog_metrics(driver))
                        # Explicit form fill only; never writes chart, response, loading or disabled state.
                        driver.execute_script('''
                          const input=document.querySelector('#chartDateTime');
                          input.value='2020-01-01T12:00';
                          input.dispatchEvent(new Event('input',{bubbles:true}));
                          input.dispatchEvent(new Event('change',{bubbles:true}));
                        ''')
                        label = driver.find_element(By.ID, 'chartLocationLabel')
                        label.clear()
                        label.send_keys('UI-A12c CHECK')
                        activate(driver, '#chartQueryButton', touch)
                        wait_ready(driver, historical=True)
                        data = capture(driver, output, name + '-history-panel', row)
                        assert len(data['history']) == 1 and 'UI-A12c CHECK' in data['history'][0]
                        close_panel(driver, touch)
                        capture(driver, output, name + '-history-result', row)
                        activate(driver, '#chartControlToggle', touch)
                        activate(driver, '#resetToNowButton', touch)
                        wait_ready(driver)
                        close_panel(driver, touch)
                        capture(driver, output, name + '-now-result', row)
                        activate(driver, '#chartControlToggle', touch)
                        activate(driver, '#chartHistoryList [data-history-load]', touch)
                        wait_ready(driver, historical=True)
                        capture(driver, output, name + '-history-reloaded', row)
                        activate(driver, '#resetToNowButton', touch)
                        wait_ready(driver)
                        activate(driver, '#chartHistoryList [data-history-delete]', touch)
                        wait.until(lambda d: snapshot(d)['history'] == [])
                        close_panel(driver, touch)
                        final = capture(driver, output, name + '-restored', row)
                        assert all(item['open'] for item in final['details']), final
                        assert_ready(final)
                        row['passed'] = True
                    except Exception as error:
                        row['error'] = f'{type(error).__name__}: {error}'
                        row['serviceFailure'] = service_failure(driver)
                        driver.save_screenshot(str(output / (name + '-failure.png')))
                        row['failure'] = snapshot(driver)
                        raise
    finally:
        (output / 'audit.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print('UI-A12c: 8 natural history flows; viewport PNGs require human review, not date-picker acceptance.')


if __name__ == '__main__':
    main()
