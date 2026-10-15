"""Execute the real renderCards function with a minimal DOM sink, not a rewrite."""
import json
from pathlib import Path
import shutil
import subprocess
import unittest


class LibraryPaginationTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which('node'), 'Node required for real JS regression')
    def test_initial_empty_render_keeps_page_then_loaded_catalog_clamps(self):
        source=Path('assets/pgl/pgl.js').read_text()
        function=source.split('  function renderCards(allSelected) {',1)[1].split('\n  function ',1)[0]
        script='''
          const state={page:2,view:'category'}, PAGE_SIZE=24;
          let libraryDataLoaded=false, rendered=[];
          const grid={replaceChildren:f=>{rendered=f.nodes}}, root={dataset:{}},resultCount={};
          const document={createDocumentFragment:()=>({nodes:[],append(n){this.nodes.push(n)}})};
          const make=(tag,cls,text)=>({tag,cls,text}), buildCard=x=>x;
          const renderPagination=()=>{};
          function renderCards(allSelected) {FUNCTION
          const require=(v,m)=>{if(!v)throw Error(m)};
          renderCards([]);require(state.page===2,'empty pending data destroyed requested page');
          libraryDataLoaded=true;
          const items=Array.from({length:60},(_,id)=>({id,status:'completed'}));
          renderCards(items);require(state.page===2,'loaded valid page lost');
          require(rendered.length===24 && rendered[0].id===24,'wrong second page slice');
          state.page=99;renderCards(items);require(state.page===3,'loaded overflow not clamped');
          renderCards([]);require(state.page===1,'loaded empty catalog not clamped');
        '''.replace('FUNCTION',function)
        result=subprocess.run(['node','-e',script],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)

    def test_loaded_flag_precedes_successful_render_not_failure(self):
        source=Path('assets/pgl/pgl.js').read_text()
        self.assertIn('let libraryDataLoaded = false;',source)
        loaded=source.index('libraryDataLoaded = true;')
        self.assertLess(source.index('items = Array.isArray(library.items)'),loaded)
        self.assertLess(loaded,source.index('render();',loaded))
        self.assertNotIn('libraryDataLoaded = true;',source.split('.catch((error) => {',1)[1])

    def test_browser_audit_requires_reload_content_not_just_url(self):
        source=Path('tools/check_think_build_visual.py').read_text()
        self.assertIn('Library reload lost page 2 despite page URL',source)
        self.assertIn('ids() == second_page',source)
        self.assertIn('Library filter reload changed URL',source)
