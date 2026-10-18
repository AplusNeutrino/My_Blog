"""Wiring checks only; actual screenshots and pointer flows run in Chrome CI."""
import ast
import json
from pathlib import Path
import shutil
import subprocess
import unittest


class ThinkPaginationAuditTests(unittest.TestCase):
    def test_series_description_lane_is_limited_to_confirmed_surface(self):
        css = Path('assets/css/neutriverse-sections.css').read_text()
        start = css.index('/* UI-021:')
        block = css[start:css.index('.nv-topic-browser-count {', start)]
        for token in ('@media (max-width: 1199.98px)',
                      "[data-neutriverse-section='think'] [data-writing-series-browser] .nv-topic-browser-description",
                      'padding-right: 2.75rem;'):
            self.assertIn(token, block)
        self.assertEqual(block.count('padding-right:'), 1)
        for token in ('#back-to-top', 'font-size:', 'display:', 'position:',
                      'grid-template', '[data-writing-topic-browser]', '.nv-section-links'):
            self.assertNotIn(token, block)

    def test_directory_text_scope_requires_real_ranges_and_preserves_existing_guards(self):
        source=Path('tools/check_think_build_visual.py').read_text()
        start=source.index('# UI-A10b:');block=source[start:source.index('require(start <= (covered',start)]
        for token in ('[data-writing-topic-browser] .nv-topic-browser-description',
                      '[data-writing-series-browser] .nv-topic-browser-description',
                      '.nv-section-links .nv-section-link > span:last-child', 'counts = [4, 3, 5]',
                      'document.createTreeWalker', 'document.createRange()', 'range.getClientRects()',
                      'g[\'rootCount\'] == count and not g[\'emptyRoots\']',
                      "all(not g['overlaps'] for g in directories)",
                      'r.left<br.right&&r.right>br.left&&r.top<br.bottom&&r.bottom>br.top',
                      'think-pagination-directory-overlap-'):
            self.assertIn(token,block)
        self.assertLess(block.index('driver.save_screenshot'),block.index('require('))
        self.assertIn("require(not controls['misses']",source[:start])
        self.assertIn('THINK text covered by back-to-top',source[:start])
        self.assertNotIn('.style',block)

    def test_actual_pointer_script_rejects_each_interior_or_edge_obstruction(self):
        """Execute the production JS, not a Python copy; not a visual/browser pass."""
        node=shutil.which('node')
        self.assertIsNotNone(node, 'Node is required for pointer audit regression')
        tree=ast.parse(Path('tools/check_think_build_visual.py').read_text())
        assignment=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign)
                        and any(isinstance(t,ast.Subscript) and isinstance(t.slice,ast.Constant)
                                and t.slice.value=='writingControlButton' for t in n.targets))
        script=ast.literal_eval(assignment.value.args[0])
        harness=r'''
          const audit=new Function(SCRIPT),rect={left:100,right:206,top:100,bottom:144,width:106,height:44};
          const parent={tagName:'DIV',id:'',className:'nv-writing-control',getBoundingClientRect:()=>rect};
          const e={tagName:'SELECT',id:'series',className:'',textContent:'All',
            getBoundingClientRect:()=>rect,contains:n=>n===e};
          const outside={left:500,right:544,top:500,bottom:544,width:44,height:44};
          let buttonRect=outside,blocked=null,rounded=true;
          const button={getBoundingClientRect:()=>buttonRect};
          global.innerHeight=757;global.devicePixelRatio=1;
          global.getComputedStyle=()=>({display:'block',visibility:'visible',opacity:'1',
            appearance:'auto',pointerEvents:'auto',transform:'none',borderWidth:'1px',borderRadius:'5.6px',
            borderTopLeftRadius:'5.6px',borderTopRightRadius:'5.6px',
            borderBottomLeftRadius:'5.6px',borderBottomRightRadius:'5.6px'});
          global.document={documentElement:{clientWidth:1009},
            querySelector:q=>q==='#back-to-top'?button:{getBoundingClientRect:()=>({bottom:0})},
            querySelectorAll:q=>q==='.nv-writing-controls select'?[e,e,e,e]:
              q==='.nv-writing-reset'?[e]:Array(10).fill(e),
            elementFromPoint:(x,y)=>{
              if(blocked&&Math.abs(x-blocked.x)<0.01&&Math.abs(y-blocked.y)<0.01)return parent;
              if(rounded&&x===204&&y===142)return parent;
              return e;
            }};
          const valid=r=>r.selectCount===4&&r.resetCount===1&&r.totalControls>=9&&
            !r.overlaps.length&&!r.misses.length;
          const base=audit();
          if(!valid(base)||base.visible[0].probes.length!==9||
            base.visible[0].cornerDiagnostics.filter(p=>!p.hit).length!==1)throw Error('rounded fixture');
          let rejected=0;
          for(const p of base.visible[0].probes){blocked=p;if(valid(audit()))throw Error('miss accepted');rejected++;}
          blocked=null;
          // Same legacy corner is covered by a tiny fixed button without covering any new probe.
          buttonRect={left:203.5,right:204.5,top:141.5,bottom:142.5,width:1,height:1};
          const overlap=audit();
          if(valid(overlap)||!overlap.overlaps.length||overlap.misses.length)throw Error('corner overlap accepted');
          console.log(JSON.stringify({rejected,cornerOverlapRejected:true,legacyCornerRecorded:true}));
        '''.replace('SCRIPT',json.dumps(script))
        result=subprocess.run([node,'-e',harness],capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(result.stdout),
                         {'rejected':9,'cornerOverlapRejected':True,'legacyCornerRecorded':True})

    def test_failed_pointer_probes_keep_assertions_and_capture_actual_target(self):
        source=Path('tools/check_think_build_visual.py').read_text()
        start=source.index('# UI-020:');block=source[start:source.index('require(start <= (covered',start)]
        for token in ('target:describe(target)', 'neighbors:hit?[]:',
                      '[[-1,0],[1,0],[0,-1],[0,1]]', 'target:describe(n)',
                      'appearance:cs.appearance', 'pointerEvents:cs.pointerEvents',
                      'borderRadius:cs.borderRadius', 'devicePixelRatio',
                      '[r.left+2,r.top+2],[r.right-2,r.top+2],[r.left+2,r.bottom-2],[r.right-2,r.bottom-2]',
                      "misses:visible.filter(e=>e.probes.some(p=>!p.hit))",
                      "require(not controls['overlaps']", "require(not controls['misses']"):
            self.assertIn(token,block)

    def test_think_control_lane_preserves_existing_layout_and_behavior(self):
        css=Path('assets/css/neutriverse-sections.css').read_text()
        start=css.index('/* UI-020:');block=css[start:css.index('.post-series-root a,',start)]
        for token in ('@media (max-width: 1199.98px)',
                      "[data-neutriverse-section='think'] .nv-writing-controls",
                      "[data-neutriverse-section='think'] .nv-writing-pagination",
                      'padding-right: calc(1rem + 2.75rem);','padding-right: 2.75rem;'):
            self.assertIn(token,block)
        for token in ('#back-to-top','display:','font-size:','grid-template','position:'):
            self.assertNotIn(token,block)

    def test_control_edges_require_clearance_and_real_pointer_hit_targets(self):
        source=Path('tools/check_think_build_visual.py').read_text()
        start=source.index('# UI-020:');block=source[start:source.index('require(start <= (covered',start)]
        for token in ('.nv-writing-controls select, .nv-writing-reset, .nv-writing-pagination a[href]',
                      'r.right-2,r.bottom-2','document.elementFromPoint(x,y)',
                      'document.documentElement.clientWidth','topbar.bottom',
                      "controls['selectCount'] == 4", "controls['resetCount'] == 1",
                      "require(not controls['overlaps']", "require(not controls['misses']",
                      'think-pagination-control-overlap-', 'write_text(json.dumps(observed'):
            self.assertIn(token,block)
        self.assertLess(block.index('driver.save_screenshot'),block.index('require('))
        for token in ('.style','dispatchEvent','captureBeyondViewport'):
            self.assertNotIn(token,block)

    def test_think_text_lane_is_scoped_without_changing_button_or_typography(self):
        css = Path('assets/css/neutriverse-sections.css').read_text()
        block = css[css.index('/* UI-019:'):css.index('.nv-writing-taxonomy {')]
        for token in ('@media (max-width: 1199.98px)',
                      "[data-neutriverse-section='think'] .nv-section-intro",
                      "[data-neutriverse-section='think'] .nv-writing-record-body",
                      'padding-right: 2.75rem;'):
            self.assertIn(token, block)
        for token in ('#back-to-top', 'font-size:', 'display:', 'position:', 'grid-template'):
            self.assertNotIn(token, block)

    def test_visible_record_ranges_reject_overlap_and_save_failure_before_raise(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        block = source[source.index("elif name.startswith('think-page-'):"):
                       source.index("require(start <= (covered")]
        for token in ('[data-neutriverse-section="think"] .nv-section-intro',
                      '[data-writing-item]:not([hidden]) .nv-writing-record-body',
                      'document.createTreeWalker', 'document.createRange()', 'range.getClientRects()',
                      'Number(s.opacity)>0', "[1, 8 if name == 'think-page-4' else 12]",
                      "g['rootCount'] == count and not g['emptyRoots']",
                      "all(not g['overlaps'] for g in groups)",
                      'r.left<br.right&&r.right>br.left&&r.top<br.bottom&&r.bottom>br.top',
                      'think-pagination-overlap-', 'THINK text covered by back-to-top'):
            self.assertIn(token, block)
        self.assertLess(block.index('driver.save_screenshot'), block.index('require('))
        self.assertNotIn('.style', block)

    def test_lossless_scoped_artifacts_keep_complete_archives(self):
        import yaml
        workflow = yaml.safe_load(Path('.github/workflows/pages-deploy.yml').read_text())
        for job, full, scoped in (
            ('build', 'neutriverse-think-build-', 'neutriverse-think-pagination-'),
            ('verify-live-ui', 'neutriverse-live-ui-', 'neutriverse-live-think-pagination-'),
        ):
            steps = workflow['jobs'][job]['steps']
            uploads = [s for s in steps if s.get('uses') == 'actions/upload-artifact@v4']
            self.assertTrue(any(s['with']['name'].startswith(full) for s in uploads))
            scope = next(s for s in uploads if s['with']['name'].startswith(scoped))
            self.assertEqual(scope['if'], 'always()')
            self.assertEqual(scope['with']['retention-days'], 14)
            for pattern in ('public-sweep-think-page-*.png', 'public-sweep-think-page-*.json',
                            'public-top-think-page-*.png', 'think-pagination-*.json',
                            'think-pagination-*.png', 'audit.json'):
                self.assertIn(pattern, scope['with']['path'])

    def helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'think_pagination_controls')
        return source, ast.get_source_segment(source, node)

    def test_all_pages_exact_public_inventory_and_native_sweeps(self):
        source, helper = self.helper()
        for token in ('range(1, 5)', 'len(expected) == 44', 'len(set(seen)) == 44',
                      'expected[(number-1)*12:number*12]', 'public_page_sweep(',
                      'data-writing-page-current', 'data-writing-page-total', 'aria-current'):
            self.assertIn(token, helper)
        self.assertIn("result['paginationInventory'] = think_pagination_controls(", source)
        self.assertNotIn('captureBeyondViewport', helper)

    def test_refresh_previous_real_click_and_failure_evidence(self):
        _, helper = self.helper()
        for token in ('driver.refresh()', 'driver.current_url == original', 'expected[36:44]',
                      'expected[24:36]', 'e.click()', 'elementFromPoint', 'think-pagination-failure-',
                      'finally:', 'visibleHrefs', 'raise', 'settle(driver, wait, theme)'):
            self.assertIn(token, helper)
        self.assertNotIn('dispatchEvent', helper)
