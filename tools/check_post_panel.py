#!/usr/bin/env python3
"""UI-026 desktop reading-panel clearance. Real input; screenshots need review."""
import json
import os
import shutil
import sys
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from check_mobile_sidebar import serve
from check_think_build_visual import settle


def metrics(driver):
    return driver.execute_script(r'''
      const stack=document.querySelector('#post-panel-stack'),button=document.querySelector('#back-to-top');
      const rect=n=>n.getBoundingClientRect().toJSON(),br=rect(button),sr=rect(stack);
      const visible=n=>{const c=getComputedStyle(n),r=rect(n);return c.display!=='none'&&
        c.visibility!=='hidden'&&Number(c.opacity)>0&&r.width>0&&r.height>0};
      const clips=(node,r)=>{let left=Math.max(0,r.left),right=Math.min(innerWidth,r.right),
        top=Math.max(0,r.top),bottom=Math.min(innerHeight,r.bottom);
        for(let p=node.parentElement;p;p=p.parentElement){const c=getComputedStyle(p),a=rect(p);
          if(/auto|scroll|hidden|clip/.test(c.overflowY)){top=Math.max(top,a.top);bottom=Math.min(bottom,a.bottom)}
          if(/auto|scroll|hidden|clip/.test(c.overflowX)){left=Math.max(left,a.left);right=Math.min(right,a.right)}}
        return {left,right,top,bottom};};
      const covered=[],seen=[];
      const links=[...stack.querySelectorAll('.post-series-item a,.post-series-neighbors a')];
      links.forEach((link,index)=>{
        const lr=rect(link),lc=clips(link,lr);
        if(lr.top>=lc.top&&lr.bottom<=lc.bottom&&lr.left>=lc.left&&lr.right<=lc.right)seen.push(index);
        const walker=document.createTreeWalker(link,NodeFilter.SHOW_TEXT);let node;
        while(node=walker.nextNode())for(let i=0;i<node.length;i++){
          const char=node.textContent[i];if(!char.trim())continue;
          const range=document.createRange();range.setStart(node,i);range.setEnd(node,i+1);
          for(const r of range.getClientRects()){
            const c=clips(node.parentElement,r),x=r.x+r.width/2,y=r.y+r.height/2;
            if(x<c.left||x>=c.right||y<c.top||y>=c.bottom)continue;
            const hit=document.elementFromPoint(x,y);
            if(visible(button)&&hit&&(hit===button||button.contains(hit)))covered.push({index,char,rect:r.toJSON()});
          }
        }
      });
      return {width:innerWidth,height:innerHeight,theme:document.documentElement.dataset.mode,
        docWidth:document.documentElement.scrollWidth,y:scrollY,stack:sr,button:br,
        buttonVisible:visible(button),clearance:sr.bottom<=br.top-1,
        scrollTop:stack.scrollTop,scrollMax:stack.scrollHeight-stack.clientHeight,
        linkCount:links.length,seen,covered,hrefs:links.map(n=>n.getAttribute('href')),
        heading:rect(document.getElementById('8-速记'))};
    ''')


def assert_clear(data):
    assert data['linkCount'] == 10, data
    assert data['docWidth'] <= data['width'] + 1, data
    assert data['buttonVisible'] and data['clearance'], data
    assert not data['covered'], data


def settled_scroll(driver):
    driver.execute_async_script('''
      const done=arguments[arguments.length-1],s=document.querySelector('#post-panel-stack');
      let y=scrollY,sy=s.scrollTop,stable=0;
      const tick=()=>{stable=Math.abs(scrollY-y)<.1&&Math.abs(s.scrollTop-sy)<.1?stable+1:0;
        y=scrollY;sy=s.scrollTop;
        if(stable>=3)done(true);else requestAnimationFrame(tick)};requestAnimationFrame(tick);
    ''')


def capture(driver, output, name, row):
    data=metrics(driver)
    driver.save_screenshot(str(output/(name+'.png')))
    row['frames'].append({'name':name,**data})
    assert_clear(data)
    return data


def exercise(driver, wait, base, output, width, height, theme):
    name=f'post-panel-{width}-{height}-{theme}'
    row={'name':name,'frames':[],'input':'native pointer + W3C wheel',
         'scope':'desktop right reading panel only; not mobile TOC dialog'}
    try:
        driver.set_window_size(width,height)
        driver.get(base+'/posts/%E8%AE%A1%E7%BB%84-07/')
        settle(driver,wait,theme)
        driver.save_screenshot(str(output/(name+'-top.png')))
        wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'#toc-wrapper a'))==8)
        driver.find_elements(By.CSS_SELECTOR,'#toc-wrapper a')[-1].click()
        settled_scroll(driver)
        data=capture(driver,output,name+'-last',row)
        assert 0<=data['heading']['top']<data['height']/2, data
        # Finite old-CSS fixture: detection must reject full-height stack. Never network mocking.
        driver.execute_script('''const s=document.createElement('style');s.id='ui026-old-height';
          s.textContent='@media(min-width:1200px){#post-panel-stack{max-height:100vh!important}}';
          document.head.append(s);''')
        try:
            old=metrics(driver)
            driver.save_screenshot(str(output/(name+'-old-height-fixture.png')))
            row['oldHeightFixture']=old
            try:
                assert_clear(old)
            except AssertionError:
                row['oldHeightRejected']=True
            else:
                raise AssertionError('UI-026 old full-height stack was accepted')
        finally:
            driver.execute_script("document.getElementById('ui026-old-height').remove()")
        seen=set()
        for step in range(30):
            data=capture(driver,output,f'{name}-sweep-{step:02d}',row)
            seen.update(data['seen'])
            if data['scrollTop']>=data['scrollMax']-1:
                break
            r=data['stack']
            origin=ScrollOrigin.from_viewport(int(r['right']-3),int((r['top']+r['bottom'])/2))
            ActionChains(driver).scroll_from_origin(origin,0,200).perform()
            wait.until(lambda d:metrics(d)['scrollTop']>data['scrollTop']+.5)
            settled_scroll(driver)
        assert data['scrollTop']>=data['scrollMax']-1, data
        assert seen==set(range(10)), {'seen':sorted(seen),'data':data}
        row['seenLinks']=sorted(seen)
        driver.find_element(By.ID,'back-to-top').click()
        wait.until(lambda d:d.execute_script('return scrollY<=1'))
        driver.save_screenshot(str(output/(name+'-returned-top.png')))
        row['returnedTop']=True
        row['status']='passed'
        return row
    except Exception as error:
        row['status']='failed';row['error']=type(error).__name__+': '+str(error)
        driver.save_screenshot(str(output/(name+'-failure.png')))
        row['failure']=metrics(driver)
        (output/'failure.json').write_text(json.dumps(row,ensure_ascii=False,indent=2))
        raise


def main():
    output=Path(os.environ.get('UI_POST_PANEL_DIR','/tmp/neutriverse-post-panel'))
    output.mkdir(parents=True,exist_ok=True)
    options=webdriver.ChromeOptions()
    options.binary_location=shutil.which('google-chrome') or shutil.which('chromium')
    for arg in ('--headless=new','--no-sandbox','--disable-dev-shm-usage'):
        options.add_argument(arg)
    rows=[]
    with serve(Path(sys.argv[1]).resolve()) as port, webdriver.Chrome(options=options) as driver:
        driver.set_script_timeout(30)
        base=os.environ.get('UI_LIVE_BASE',f'http://127.0.0.1:{port}').rstrip('/')
        for width in (1366,1920):
            for height in (900,640):
                for theme in ('dark','light'):
                    rows.append(exercise(driver,WebDriverWait(driver,15),base,output,width,height,theme))
                    (output/'audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    print(f'Post panel: {len(rows)} desktop flows; screenshots require human review')


if __name__=='__main__':
    main()
