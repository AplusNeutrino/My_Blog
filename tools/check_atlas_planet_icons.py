#!/usr/bin/env python3
"""UI-025: isolated real CSS/PNG rendering, not backend or full-app verification."""
import json
import os
from pathlib import Path
import shutil
import sys

from selenium import webdriver

from check_mobile_sidebar import serve
from check_think_build_visual import VIEWPORTS


def main():
    root = Path(sys.argv[1]).resolve()
    output = Path(os.environ.get('UI_ATLAS_ICONS_DIR', '/tmp/atlas-planet-icons'))
    output.mkdir(parents=True, exist_ok=True)
    css = (root / 'occult-atlas-app/styles.css').read_text()
    options = webdriver.ChromeOptions()
    options.binary_location = next((shutil.which(n) for n in
        ('google-chrome', 'google-chrome-stable', 'chromium') if shutil.which(n)), None)
    for flag in ('--headless=new', '--no-sandbox', '--disable-dev-shm-usage'):
        options.add_argument(flag)
    rows = []
    with serve(root) as port, webdriver.Chrome(options=options) as driver:
        base = f'http://127.0.0.1:{port}'
        for width, height in VIEWPORTS:
            driver.set_window_size(width, height)
            for theme in ('dark', 'light'):
                # Same-origin real built PNGs, real unmodified stylesheet, no remote service.
                driver.get(base + '/occult-atlas/')
                cards = ''.join(f'''<section><h2>{body}</h2>
                  <div class="sample"><span>normal</span><svg viewBox="0 0 72 72">
                  <g class="planet-node"><circle cx="36" cy="36" r="25"/>
                  <image href="{base}/occult-atlas-app/assets/astro-icons/planet-{body}.png"
                    x="12" y="12" width="48" height="48"/></g></svg></div>
                  <div class="sample"><span>selected</span><svg viewBox="0 0 72 72">
                  <g class="planet-node active"><circle cx="36" cy="36" r="25"/>
                  <image href="{base}/occult-atlas-app/assets/astro-icons/planet-{body}.png"
                    x="12" y="12" width="48" height="48"/></g></svg></div></section>'''
                  for body in ('sun', 'moon', 'saturn'))
                html = f'''<!doctype html><html data-mode="{theme}"><head><meta charset="utf-8">
                  <style>{css}</style><style>
                  body{{padding:20px;background:var(--atlas-main)}}
                  h1{{font:20px sans-serif}}h2{{font:18px sans-serif;width:70px}}
                  section{{display:flex;align-items:center;gap:12px;margin:18px 0}}
                  .sample{{width:90px;text-align:center;font:14px sans-serif}}
                  svg{{display:block;width:80px;height:80px}}</style></head><body>
                  <h1>UI-025 / {theme} / isolated CSS + PNG fixture</h1>{cards}</body></html>'''
                driver.execute_script('document.open();document.write(arguments[0]);document.close()', html)
                metrics = driver.execute_async_script('''
                  const done=arguments[arguments.length-1];
                  Promise.all([...document.querySelectorAll('image')].map(n=>new Promise((resolve,reject)=>{
                    const im=new Image();im.onload=()=>resolve(im.naturalWidth>0);im.onerror=reject;
                    im.src=n.getAttribute('href');
                  }))).then(images=>done({images,
                    fills:[...document.querySelectorAll('.planet-node circle')].map(n=>getComputedStyle(n).fill),
                    width:innerWidth,docWidth:document.documentElement.scrollWidth}));
                ''')
                assert len(metrics['images']) == 6 and all(metrics['images']), metrics
                assert metrics['docWidth'] <= metrics['width'] + 1, metrics
                expected = 'rgb(255, 248, 231)' if theme == 'light' else 'rgb(231, 236, 243)'
                assert metrics['fills'][::2] == [expected] * 3, metrics
                name = f'planet-icons-{width}-{theme}'
                driver.save_screenshot(str(output / (name + '.png')))
                # Inject precisely the old coupling in this disposable fixture; it must fail.
                driver.execute_script("document.querySelectorAll('.planet-node:not(.active) circle').forEach(n=>n.style.fill='var(--atlas-heading)')")
                old = driver.execute_script("return getComputedStyle(document.querySelector('.planet-node circle')).fill")
                if theme == 'light':
                    assert old != expected, old
                rows.append({'name': name, 'fixture': 'isolated built CSS and PNG only',
                             'metrics': metrics, 'oldLightFillRejected': theme == 'light' and old != expected})
        (output / 'audit.json').write_text(json.dumps(rows, indent=2) + '\n')


if __name__ == '__main__':
    main()
