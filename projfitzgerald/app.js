const SOURCE = '../docs/PROJFITZGERALD_PROGRESS.md';
const labels = {done:'DONE',in_progress:'ACTIVE',todo:'TODO',blocked:'BLOCKED'};
let tracker;

function allItems(data){return data.milestones.flatMap(m=>m.items)}
function setText(id,value){document.getElementById(id).textContent=value}
function counts(data){
  return allItems(data).reduce((a,x)=>{a[x.status]=(a[x.status]||0)+1;return a},{done:0,in_progress:0,todo:0,blocked:0});
}
function renderSummary(data){
  const c=counts(data), total=Object.values(c).reduce((a,b)=>a+b,0), pct=total?Math.round(c.done/total*100):0;
  setText('subtitle',data.project.subtitle);setText('north-star',data.project.northStar);
  setText('phase',data.project.phase);setText('priority',`${data.project.priority} · 当前优先级`);setText('updated',`更新 · ${data.project.lastUpdated}`);
  setText('percent',pct);document.getElementById('bar').style.width=`${pct}%`;setText('summary-note',data.summary.note);
  setText('done-count',c.done);setText('doing-count',c.in_progress);setText('todo-count',c.todo);setText('blocked-count',c.blocked);
}
function renderMilestones(data,filter='all'){
  const root=document.getElementById('milestones');root.innerHTML='';
  data.milestones.forEach(m=>{
    const items=m.items.filter(x=>filter==='all'||x.status===filter||x.priority===filter);
    if(!items.length)return;
    const el=document.createElement('article');el.className='milestone';
    el.innerHTML=`<div class="milestone-head"><span class="milestone-index">${m.id}</span><div><h2>${m.title}</h2><p class="milestone-goal">${m.goal}</p></div><span class="milestone-date">${m.date}</span></div><div class="task-list">${items.map(x=>`<div class="task"><span class="task-id">${x.id}</span><div><div class="task-title">${x.title}</div>${x.evidence?`<div class="task-evidence">证据 · ${x.evidence}</div>`:''}</div><span class="status ${x.status}">${labels[x.status]}</span></div>`).join('')}</div>`;
    root.appendChild(el);
  });
}
function renderIntel(data){
  document.getElementById('risks').innerHTML=data.risks.map(x=>`<div class="risk"><span class="level ${x.level}">${x.level.toUpperCase()}</span><strong>${x.id} · ${x.title}</strong><p>${x.mitigation}</p></div>`).join('');
  document.getElementById('unknowns').innerHTML=data.unknowns.map(x=>`<li>${x}</li>`).join('');
  document.getElementById('decisions').innerHTML=data.decisions.map(x=>`<li>${x}</li>`).join('');
}
async function init(){
  try{
    const text=await fetch(SOURCE,{cache:'no-store'}).then(r=>{if(!r.ok)throw new Error(r.status);return r.text()});
    const match=text.match(/<!-- TRACKER_DATA_START -->\s*```json\s*([\s\S]*?)\s*```\s*<!-- TRACKER_DATA_END -->/);
    if(!match)throw new Error('tracker data missing');
    tracker=JSON.parse(match[1]);renderSummary(tracker);renderMilestones(tracker);renderIntel(tracker);
  }catch(error){document.getElementById('milestones').innerHTML='<div class="error">进度真源读取失败，请检查 PROJFITZGERALD_PROGRESS.md 的 JSON 格式。</div>'}
}
document.querySelector('.filters').addEventListener('click',event=>{
  const button=event.target.closest('button');if(!button||!tracker)return;
  document.querySelectorAll('.filters button').forEach(x=>x.classList.toggle('active',x===button));renderMilestones(tracker,button.dataset.filter);
});
init();
