/* Isole al Vento - campagna: progressi, mappa dei mondi, scheda livello, Arsenale, Imprese, Sfida del giorno, aiuti, risultati e pubblicità.
   Il motore di gioco resta in index.html: qui si parla con lui solo tramite window.IAV. I livelli arrivano da campagna-livelli.js (mappe logiche). */
(()=>{
'use strict';
const IAV=window.IAV,LV=window.CAMP_LEVELS||[],WORLDS=window.CAMP_WORLDS||[],DF=window.CAMP_DIFF;
if(!IAV||!LV.length||!WORLDS.length||!DF)return;
const $=id=>document.getElementById(id);
const el=(t,c,h)=>{const e=document.createElement(t);if(c)e.className=c;if(h!==undefined)e.innerHTML=h;return e};
const UT=IAV.UT,UN={G:'guerriero',A:'arciere',E:'esploratore',K:'cavaliere',W:'sciamano',L:'lanciere',H:'guaritore',B:'balestriere',R:'alfiere'};
const byId={};for(const l of LV)byId[l.id]=l;
const wLv=w=>LV.filter(l=>l.world===w);
const KEY='isole-camp';

/* ------------------------------------------------ progressi (salvati sul telefono) */
const STAT0={wins:0,plays:0,kills:0,lost:0,perfect:0,boss:0,erupt:0,fast:0,aids:0,daily:0,upg:0,wx:{}};
function defState(){return {v:1,lv:{},perle:0,boost:{sereno:2,cura:2,rinforzo:1},up:{},ach:{},diff:1,stats:Object.assign({},STAT0,{wx:{}}),daily:{last:'',streak:0,done:''},wd:{},ads:0}}
function load(){
  let o=null;try{o=JSON.parse(localStorage.getItem(KEY)||'null')}catch(e){}
  const d=defState();if(!o||typeof o!=='object')return d;
  const s=Object.assign(d,o);s.stats=Object.assign({},STAT0,o.stats||{});s.stats.wx=Object.assign({},(o.stats||{}).wx||{});
  s.boost=Object.assign({sereno:0,cura:0,rinforzo:0},o.boost||{});if(![0,1,2].includes(s.diff))s.diff=1;s.daily=Object.assign({last:'',streak:0,done:''},o.daily||{});
  return s;
}
let S=load();
function save(){try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}}
const done=id=>!!(S.lv[id]&&S.lv[id].done);
const starsOf=id=>(S.lv[id]&&S.lv[id].s)||0;
const starsTotal=()=>LV.reduce((a,l)=>a+starsOf(l.id),0);
const worldStars=w=>wLv(w).reduce((a,l)=>a+starsOf(l.id),0);
const doneCount=()=>LV.filter(l=>done(l.id)).length;
const worldDone=w=>wLv(w).every(l=>done(l.id));
function worldOpen(w){const W=WORLDS.find(x=>x.id===w);if(!W)return false;return w===1||(worldDone(w-1)&&starsTotal()>=W.need)}
function unlocked(l){if(!worldOpen(l.world))return false;const ws=wLv(l.world),i=ws.findIndex(x=>x.id===l.id);return i===0||done(ws[i-1].id)}
const currentLevel=()=>LV.find(l=>unlocked(l)&&!done(l.id))||null;
const topIn=(n,root)=>{let y=0;while(n&&n!==root){y+=n.offsetTop;n=n.offsetParent}return y};
const nextOf=l=>{const i=LV.indexOf(l);return LV[i+1]||null};
const firstLevelOf=t=>LV.find(l=>(l.allow||[]).includes(t));
const unitOpen=t=>'GAE'.includes(t)||(firstLevelOf(t)&&done(firstLevelOf(t).id));
const upgCount=()=>Object.values(S.up).reduce((a,b)=>a+b,0);
// Potenziamenti dell'Arsenale: 3 livelli per unità, cumulativi (vita e attacco in più). Valgono solo nella campagna.
const UPB=[{hp:0,atk:0},{hp:1,atk:0},{hp:1,atk:1},{hp:3,atk:1}],UPC=[40,100,200];
function upgMap(d){const m={},pb=DF.pbonus[d===undefined?1:d]||{hp:0,atk:0};for(const t of Object.keys(UN)){const k=S.up[t]||0,b=UPB[k],hp=b.hp+pb.hp,atk=b.atk+pb.atk;if(hp||atk)m[t]={hp,atk}}return m}
const DN=DF.names,dOf=rec=>rec&&rec.done?(rec.d===undefined?1:rec.d):-1;

/* messaggio breve sopra a tutte le schermate della campagna (il «toast» del gioco sta sotto e qui non si vedrebbe) */
let noteT=0;
function note(msg,ms){
  let n=$('cmNote');if(!n){n=el('div');n.id='cmNote';n.setAttribute('role','status');document.body.appendChild(n)}
  n.textContent=msg;n.classList.add('on');clearTimeout(noteT);noteT=setTimeout(()=>n.classList.remove('on'),ms||1800);
}
/* ------------------------------------------------ icone */
const star=on=>`<svg viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z" fill="${on?'#ffd24a':'#35596b'}" stroke="${on?'#a8741f':'#9fb6c0'}" stroke-width="1.5" stroke-linejoin="round"/></svg>`;
const pearl='<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="#d9eeff" stroke="#5a8bb0" stroke-width="1.6"/><ellipse cx="9" cy="8.5" rx="3.2" ry="2" fill="#fff" opacity=".9"/><circle cx="14.5" cy="14.5" r="3" fill="#b9d8f2" opacity=".8"/></svg>';
const lockI='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="9.5" rx="2.4" fill="currentColor" fill-opacity=".25"/><path d="M8 11V8.2a4 4 0 0 1 8 0V11"/></svg>';
const crown='<svg class="crown" viewBox="0 0 34 24"><path d="M3 21L1.5 6l8 7L17 2l7.5 11 8-7L31 21z" fill="#ffd24a" stroke="#a8741f" stroke-width="2" stroke-linejoin="round"/><circle cx="17" cy="2.8" r="2" fill="#ef6a5a"/></svg>';
const tick='<svg viewBox="0 0 24 24" fill="none" stroke="#8fe39a" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 12.5l5 5 10-11"/></svg>';
const cross='<svg viewBox="0 0 24 24" fill="none" stroke="#c9d8de" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>';
const IC={
  flag:'<path d="M6 21V3M6 4h11l-2.5 4L17 12H6"/>',sword:'<path d="M5 19l10-10M14 5h5v5L9 20M4 20l2-2"/>',shield:'<path d="M12 3l7.5 3v5.5c0 4.6-3.2 7.9-7.5 9.5-4.3-1.6-7.5-4.9-7.5-9.5V6z"/>',
  crown:'<path d="M3 18L2 7l5.5 4.5L12 4l4.5 7.5L22 7l-1 11z"/>',cloud:'<path d="M7 18a4 4 0 0 1 .3-8 5 5 0 0 1 9.4 1.2A3.4 3.4 0 0 1 17 18z"/>',flame:'<path d="M12 3c1 4 5 5.5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 .2 1.2.8 2 1.6 2.3C10 8 11 5 12 3z"/>',
  hammer:'<path d="M14 4l6 6-3 3-6-6zM12.5 11L4 19.5 6.5 22l8.5-8.5"/>',cal:'<rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',bolt:'<path d="M13 2L5 13.5h6L10 22l8-11.5h-6z"/>',star:'<path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/>',
  trophy:'<path d="M7 4h10v5a5 5 0 0 1-10 0zM7 6H4v2a3 3 0 0 0 3 3M17 6h3v2a3 3 0 0 1-3 3M12 14v4M8.5 20h7"/>',pearl:'<circle cx="12" cy="12" r="8"/><path d="M8.5 9.5a4 4 0 0 1 3-2"/>'
};
const ico=k=>`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">${IC[k]||IC.star}</svg>`;

/* ------------------------------------------------ testi dei livelli */
function goalText(l){
  const r=goalText0(l),v=(l.p||[]).find(u=>u[3]&&u[3].vip);
  if(v&&l.goal.t!=='reach')r[1]+=' '+(v[3].name||'Il protetto')+' non deve cadere: se cade, perdi.';
  return r;
}
function goalText0(l){
  const G=l.goal||{t:'stations'};
  if(G.t==='elim')return ['Elimina tutti i nemici','Non servono le stazioni: basta eliminare ogni unità nemica.'];
  if(G.t==='survive')return ['Resisti fino alla fine del round '+l.rounds,'Il nemico arriva a ondate. Se resta un nemico sulla tua base a fine round, perdi.'];
  if(G.t==='reach'){const v=(l.p||[]).find(u=>u[3]&&u[3].vip);return G.vip&&v?['Porta '+(v[3].name||'il messaggero')+' alla meta','La meta è la casella con la bandiera dorata. Se cade, perdi.']:['Raggiungi la meta con una tua unità','La meta è la casella con la bandiera dorata. Hai '+l.rounds+' round.']}
  if(G.t==='boss'){const b=(l.e||[]).find(u=>u[3]&&u[3].boss);return ['Sconfiggi '+(b&&b[3].name||'il boss'),'Il boss ha il segno rosso accanto alla vita. Le guardie lo proteggono.']}
  return ['Tieni le stazioni meteo per '+(G.hold||3)+' round di fila','Devi occupare tutte le stazioni (bandierine) alla fine di ogni round.'];
}
const wxIcon=t=>`<img src="assets/interfaccia/icona_meteo_${t}.png" alt="${t}">`;
const WXN={sereno:'Sereno',vento:'Vento',pioggia:'Pioggia',nebbia:'Nebbia',gelo:'Gelo'};
function levelReward(l){const b=(l.reward&&l.reward.bonus)||0;return 20+30+b}

/* ------------------------------------------------ pubblicità: spenta di base. «Prova» mostra una striscia e un finto video, per vedere dove andranno.
   Quando si collegherà un servizio vero (es. AdMob) basta cambiare qui dentro banner() e rewarded(): il resto del gioco non cambia. */
const ADS={
  mode:(()=>{try{return localStorage.getItem('isole-ads')==='prova'?'prova':'off'}catch(e){return 'off'}})(),
  on(){return this.mode!=='off'},
  set(m){this.mode=m;try{localStorage.setItem('isole-ads',m)}catch(e){}this.refresh()},
  refresh(){document.body.classList.toggle('adson',this.on());document.querySelectorAll('.adBan').forEach(b=>{b.hidden=!this.on()});renderAll()},
  rewarded(why,cb){ // chiede un video e chiama cb(true) solo se è stato visto fino in fondo
    if(!this.on()){cb(false);return}
    const ov=$('ovAd'),num=ov.querySelector('.adVid'),msg=ov.querySelector('p'),bt=$('adClose');
    ov.hidden=false;bt.hidden=true;let n=4;num.textContent=n;msg.textContent='Annuncio di prova ('+why+'). Il video vero arriverà più avanti.';
    const iv=setInterval(()=>{n--;if(n>0){num.textContent=n;return}clearInterval(iv);num.textContent='✓';msg.textContent='Ricompensa pronta!';bt.hidden=false;bt.onclick=()=>{ov.hidden=true;ADS.n=(ADS.n||0)+1;cb(true)}},1000);
  }
};

/* ------------------------------------------------ struttura delle schermate */
const root=el('div');root.id='ovCamp';root.hidden=true;
root.innerHTML=`<div class="cmTop"><button type="button" class="cmBack" id="cmBack" aria-label="Indietro"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button><div class="cmTt" id="cmTt">Campagna</div><div class="cmChip" id="cmStars"></div><div class="cmChip" id="cmPearls"></div></div>
<div class="cmBody" id="cmBody"></div>
<div class="cmTabs" role="tablist">
<button type="button" class="cmTab" role="tab" data-t="map">${ico('flag')}Campagna</button>
<button type="button" class="cmTab" role="tab" data-t="daily">${ico('cal')}Sfida<i hidden id="dyBadge">1</i></button>
<button type="button" class="cmTab" role="tab" data-t="arsenal">${ico('shield')}Arsenale</button>
<button type="button" class="cmTab" role="tab" data-t="goals">${ico('trophy')}Imprese<i hidden id="acBadge">1</i></button></div>
<div class="adBan" hidden>Spazio pubblicitario (prova)</div>`;
document.body.appendChild(root);
const sheet=el('div','ov');sheet.id='ovCmSheet';sheet.hidden=true;document.body.appendChild(sheet);
const aid=el('div','ov');aid.id='ovAid';aid.hidden=true;document.body.appendChild(aid);
IAV.onUsed=k=>{S.boost[k]--;S.stats.aids++;save();renderAll()};
const adOv=el('div','ov');adOv.id='ovAd';adOv.hidden=true;adOv.innerHTML='<div class="adBox"><div class="adVid">4</div><p></p><button type="button" class="cmBtn" id="adClose" hidden>Prendi la ricompensa</button></div>';document.body.appendChild(adOv);
{const b=el('div','adBan','Spazio pubblicitario (prova)');b.hidden=true;$('ovStart').appendChild(b)}
let tab='map',focusId=null;

function setTop(){
  $('cmStars').innerHTML=star(true)+starsTotal();$('cmPearls').innerHTML=pearl+S.perle;
  const n=achReady();const ab=$('acBadge');ab.textContent=n;ab.hidden=!n;
  const db=$('dyBadge');db.hidden=S.daily.done===todayStr();
  root.querySelectorAll('.cmTab').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.t===tab)));
  $('cmTt').textContent={map:'Campagna',daily:'Sfida del giorno',arsenal:'Arsenale',goals:'Imprese'}[tab];
}
function renderAll(){
  refreshHome();
  if(root.hidden)return;
  setTop();const b=$('cmBody'),keep=tab==='map'?b.scrollTop:0;
  b.innerHTML='';b.onscroll=null;
  ({map:renderMap,daily:renderDaily,arsenal:renderArsenal,goals:renderGoals})[tab](b);
  if(tab==='map'){if(focusId){const n=b.querySelector('[data-id="'+focusId+'"]');if(n){b.scrollTop=Math.max(0,topIn(n,b)-b.clientHeight/2+30)}focusId=null}else b.scrollTop=keep;if(b.onscroll)b.onscroll()}
}
function openCamp(t,fid){
  tab=t||'map';focusId=fid||null;
  if(tab==='map'&&!fid){const c=currentLevel()||[...LV].reverse().find(l=>done(l.id));focusId=c?c.id:null}
  $('ovStart').hidden=true;$('ovEnd').hidden=true;sheet.hidden=true;root.hidden=false;renderAll();
}
function closeCamp(){root.hidden=true;sheet.hidden=true;IAV.showStart();refreshHome()}
$('cmBack').onclick=closeCamp;
root.querySelectorAll('.cmTab').forEach(b=>{b.onclick=()=>{tab=b.dataset.t;renderAll();$('cmBody').scrollTop=0}});
root.addEventListener('click',e=>{if(e.target.closest('button'))IAV.sfx('tap')},true);
sheet.addEventListener('click',e=>{if(e.target.closest('button'))IAV.sfx('tap')},true);

/* ------------------------------------------------ mappa dei mondi */
const PX=[34,66,38,70,32,64,40,58];
const DEC={1:['pino_a','boschetto_a','pino_b','montagna_b','pino_c','boschetto_b','pino_a','pino_b'],2:['montagna_a','pino_b','montagna_b','pino_c','montagna_a','pino_a','montagna_b','pino_b'],3:['terreno_vulcano_arde','montagna_a','montagna_b','terreno_vulcano_calmo','montagna_a','pino_c','montagna_b','terreno_vulcano_arde'],
4:['boschetto_a','pino_a','montagna_b','boschetto_b','pino_c','montagna_a','pino_b','boschetto_a'],
5:['pino_a','pino_b','boschetto_a','pino_c','boschetto_b','pino_a','pino_b','boschetto_a'],
6:['montagna_a','pino_c','montagna_b','montagna_a','pino_b','montagna_b','pino_c','montagna_a','montagna_b'],
7:['pino_b','montagna_a','boschetto_b','pino_a','montagna_b','pino_c','boschetto_a','montagna_a'],
8:['boschetto_a','pino_a','boschetto_b','pino_b','boschetto_a','pino_c','boschetto_b','pino_a','boschetto_a'],
9:['terreno_vulcano_arde','montagna_a','terreno_vulcano_eruttato','montagna_b','terreno_vulcano_calmo','montagna_a','terreno_vulcano_arde','montagna_b'],
10:['montagna_b','pino_b','terreno_vulcano_calmo','montagna_a','pino_c','boschetto_a','montagna_b','terreno_vulcano_arde','pino_a','montagna_a']};
const S1_NAME='Stagione 1';
function renderMap(b){
  const sv=IAV.saveInfo();
  if(sv&&byId[sv.id]){
    const c=el('div','cmP cmCont');c.innerHTML=`<div style="flex:1;min-width:0"><h3>Partita in corso</h3><p>${byId[sv.id].id} · ${byId[sv.id].name} · round ${sv.round}</p></div>`;
    const bt=el('button','cmBtn','Riprendi');bt.type='button';bt.onclick=()=>{root.hidden=true;IAV.resume()};c.appendChild(bt);b.appendChild(c);
  }
  const dn=doneCount(),all=dn===LV.length;
  const se=el('div','cmP cmSeason');se.innerHTML=`<h3>${S1_NAME}${all?' · completata!':''}</h3><p>${WORLDS.length} mondi · ${LV.length} livelli · ${dn} completati · ⭐ ${starsTotal()}/${LV.length*3}</p><div class="acBar"><i style="width:${Math.round(dn/LV.length*100)}%"></i></div>`;b.appendChild(se);
  const jump=el('div','cmJump');jump.setAttribute('role','navigation');jump.setAttribute('aria-label','Vai al mondo');
  const secs={};
  for(const W of WORLDS){const j=el('button','cmJ'+(worldOpen(W.id)?'':' lock'),worldOpen(W.id)?String(W.id):W.id+lockI);j.type='button';j.dataset.w=W.id;j.setAttribute('aria-label','Mondo '+W.id+': '+W.name);
    j.onclick=()=>{const t=secs[W.id];if(t)b.scrollTo({top:Math.max(0,topIn(t,b)-jump.offsetHeight-8),behavior:'auto'})};jump.appendChild(j)}
  b.appendChild(jump);
  for(const W of WORLDS){
    const ws=wLv(W.id),open=worldOpen(W.id),H=ws.length*104+64;
    const sec=el('section','cmW w'+W.id);sec.dataset.w=W.id;if(W.wf)sec.style.setProperty('--wf',W.wf);if(W.wg)sec.style.setProperty('--wg',W.wg);
    const hd=el('div','cmP cmWH',`<h3>Mondo ${W.id} · ${W.name}</h3><p>${W.sub}</p><div class="cmWS">${star(true)}${worldStars(W.id)}/${ws.length*3}</div>`);
    sec.appendChild(hd);
    const path=el('div','cmPath');path.style.height=H+'px';
    const pts=ws.map((l,i)=>({x:i===ws.length-1?50:PX[i%PX.length],y:48+i*104}));
    let d='M'+pts[0].x+' '+pts[0].y;for(let i=1;i<pts.length;i++){const a=pts[i-1],c=pts[i],my=(a.y+c.y)/2;d+=' C'+a.x+' '+my+' '+c.x+' '+my+' '+c.x+' '+c.y}
    path.innerHTML=`<svg class="cmLine" viewBox="0 0 100 ${H}" preserveAspectRatio="none"><path d="${d}" fill="none" stroke="rgba(255,255,255,.75)" stroke-width="5" stroke-dasharray="1 11" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>`;
    (DEC[W.id]||DEC[1]).forEach((n,i)=>{if(i>=ws.length)return;const left=i%2===0,im=el('img','cmDec');im.src='assets/oggetti/'+n+'.png';im.alt='';const sz=n.startsWith('terreno')?96:n.startsWith('montagna')?84:60;im.style.width=sz+'px';im.style[left?'left':'right']='0px';im.style.top=(40+i*104-sz/3)+'px';im.style.opacity=.95;path.appendChild(im)});
    ws.forEach((l,i)=>{
      const un=open&&unlocked(l),dn=done(l.id),cur=un&&!dn,boss=l.goal.t==='boss';
      const n=el('button','cmNode'+(dn?' done':'')+(un?'':' lock')+(cur?' cur':'')+(boss?' boss':''));n.type='button';n.dataset.id=l.id;
      n.style.left=pts[i].x+'%';n.style.top=pts[i].y+'px';
      n.innerHTML=(boss?crown:'')+`<div class="md">${un?l.n:lockI}</div>`+(un?`<div class="st">${[1,2,3].map(k=>star(k<=starsOf(l.id))).join('')}</div>`:'')+(un||boss?`<div class="nm">${l.name}</div>`:'');
      n.onclick=()=>{if(!open){note(gateText(W),2200);return}if(!un){note('Completa prima il livello '+(i?ws[i-1].id:'precedente'),1800);return}openSheet(l)};
      path.appendChild(n);
    });
    sec.appendChild(path);
    if(!open){const g=el('div','cmGate');g.innerHTML=`<div class="cmP"><h3>${lockI.replace('<svg','<svg style="width:28px;height:28px;vertical-align:-6px;margin-right:4px"')}Mondo bloccato</h3><p>${gateText(W)}</p></div>`;sec.appendChild(g)}
    b.appendChild(sec);secs[W.id]=sec;
  }
  // in fondo alla mappa: la prossima stagione, ancora chiusa
  const s2=el('section','cmW s2');s2.style.setProperty('--wf','grayscale(.75) brightness(.5)');s2.style.setProperty('--wg','linear-gradient(rgba(10,16,34,.5),rgba(10,16,34,.35))');
  const pp=el('div','cmPath');pp.style.height='170px';
  [[28,40],[52,92],[74,50]].forEach(q=>{const n=el('div','cmNode lock');n.style.left=q[0]+'%';n.style.top=q[1]+'px';n.innerHTML='<div class="md">?</div>';pp.appendChild(n)});
  s2.appendChild(pp);
  const c2=el('div','cmP cmS2');c2.innerHTML=`${lockI.replace('<svg','<svg class="lk"')}<h3>Stagione 2</h3><p>Nuovi mondi, nuovi nemici e nuove sfide.</p><span class="soon">Arriverà prossimamente</span>`;s2.appendChild(c2);
  b.appendChild(s2);
  const sy=()=>{const y=b.scrollTop+jump.offsetHeight+30;let cur=WORLDS[0].id;for(const W of WORLDS){if(topIn(secs[W.id],b)<=y)cur=W.id}
    jump.querySelectorAll('.cmJ').forEach(j=>{const on=+j.dataset.w===cur;j.classList.toggle('on',on);if(on&&!j._seen){}});
    const a=jump.querySelector('.cmJ.on');if(a){const l=a.offsetLeft-jump.clientWidth/2+a.offsetWidth/2;if(Math.abs(jump.scrollLeft-l)>6)jump.scrollLeft=l}};
  b.onscroll=sy;
}
function gateText(W){
  const p=WORLDS.find(x=>x.id===W.id-1);
  if(!worldDone(W.id-1))return 'Completa il boss del mondo «'+p.name+'».';
  return 'Servono '+W.need+' stelle in tutto: ne hai '+starsTotal()+'.';
}

/* ------------------------------------------------ scheda livello */
function drawMini(cv,l){
  const rows=l.map,w=rows[0].length,h=rows.length,cs=Math.max(7,Math.floor(Math.min(124/w,164/h)));
  cv.width=w*cs;cv.height=h*cs;cv.style.width=w*cs+'px';cv.style.height=h*cs+'px';
  const c=cv.getContext('2d');
  for(let y=0;y<h;y++)for(let x=0;x<w;x++){
    const ch=rows[y][x],X=x*cs,Y=y*cs;
    c.fillStyle=(x+y)%2?'#9bd06a':'#a6d874';
    if(ch==='L')c.fillStyle='#55b3d8';else if(ch==='M')c.fillStyle='#8f9099';else if(ch==='V')c.fillStyle='#4a3b38';
    c.fillRect(X,Y,cs,cs);
    if(ch==='F'){c.fillStyle='#3f8f4d';c.beginPath();c.arc(X+cs/2,Y+cs/2,cs*.36,0,7);c.fill()}
    if(ch==='M'){c.fillStyle='#cfd1d8';c.beginPath();c.moveTo(X+cs*.15,Y+cs*.85);c.lineTo(X+cs*.5,Y+cs*.15);c.lineTo(X+cs*.85,Y+cs*.85);c.fill()}
    if(ch==='V'){c.fillStyle='#ff7a3d';c.beginPath();c.arc(X+cs/2,Y+cs/2,cs*.3,0,7);c.fill()}
    if(ch==='S'){c.fillStyle='#ffd24a';c.fillRect(X+cs*.3,Y+cs*.15,cs*.12,cs*.7);c.fillRect(X+cs*.3,Y+cs*.15,cs*.45,cs*.3)}
    if(ch==='T'){c.strokeStyle='#ffe9a6';c.lineWidth=Math.max(2,cs*.14);c.strokeRect(X+cs*.15,Y+cs*.15,cs*.7,cs*.7)}
    if(ch==='1'||ch==='2'){c.fillStyle=ch==='1'?'#f2b84b':'#6f9fe0';c.fillRect(X+cs*.18,Y+cs*.18,cs*.64,cs*.64)}
  }
  for(const [side,col] of [['p','#f2b84b'],['e','#6f9fe0']])for(const u of l[side]||[]){
    const boss=u[3]&&u[3].boss,vip=u[3]&&u[3].vip;
    c.fillStyle=boss?'#ef4a3a':vip?'#6fd0ff':col;c.strokeStyle='#1a1424';c.lineWidth=1.4;c.beginPath();c.arc(u[1]*cs+cs/2,u[2]*cs+cs/2,cs*(boss?.42:.3),0,7);c.fill();c.stroke();
  }
}
function openSheet(l){
  const W=WORLDS.find(x=>x.id===l.world),rec=S.lv[l.id]||{s:0},g=goalText(l),boss=l.goal.t==='boss';
  const sv=IAV.saveInfo(),same=sv&&sv.id===l.id;
  const wx=[...new Set((l.weather&&l.weather.pool)||['sereno','vento','pioggia','nebbia','gelo'])];
  const en=(l.e||[]).length,wv=(l.waves||[]).reduce((a,w)=>a+w.u.length,0);
  const d=S.diff,best=dOf(rec),mult=DF.mult[d];
  const card=el('div','card menu shCard');
  const starRows=[['Vinci il livello']].concat((l.stars||[]).map(x=>[x.txt])).map((x,i)=>`<div class="shStar${i<rec.s?'':' off'}">${star(i<rec.s)}<span>${x[0]}</span></div>`).join('');
  card.innerHTML=`<div class="shHead"><div class="shNum${boss?' boss':''}">${l.id}</div><div class="shTt"><h2>${l.name}</h2><small>Mondo ${W.id} · ${W.name}</small></div><button type="button" class="shClose" id="shX" aria-label="Chiudi">×</button></div>
  <div class="sc shBody">
  <p class="shDesc">${l.desc}</p>
  <div class="shDiff" role="group" aria-label="Difficoltà">${[0,1,2].map(i=>`<button type="button" class="shD" data-d="${i}" aria-pressed="${i===d}">${DN[i]}</button>`).join('')}<button type="button" class="shD lock" id="shIns" aria-disabled="true" aria-label="Insane, bloccata">${lockI}${DN[3]}</button></div>
  <div class="shMid"><canvas class="shMap" id="shMap"></canvas><div class="shSide"><div class="shGoalT">${ico('flag').replace('<svg','<svg style="width:18px;height:18px;flex:none"')}<b>${g[0]}</b></div><div class="shStars">${starRows}</div></div></div>
  <div class="shNote">${g[1]} Limite: ${l.rounds} round · campo ${l.map[0].length}×${l.map.length}.</div>
  <div class="shChips"><span class="shChip">${en?en+' nemici':'Solo ondate'}${en&&wv?' + '+wv+' a ondate':wv?' · '+wv+' unità':''}</span>${best>=0?`<span class="shChip ok">✓ Vinto in ${DN[best]}</span>`:''}${wx.map(t=>`<span class="shChip" title="${WXN[t]}">${wxIcon(t)}${WXN[t]}</span>`).join('')}</div>
  <div class="shUnR"><span class="shSave">Unità:</span><div class="shUn">${(l.allow||[]).map(t=>`<img src="${IAV.unitImg(t)}" alt="${UT[t].n}" title="${UT[t].n}">`).join('')}</div></div>
  <div class="shSave">Primo successo: fino a ${Math.max(1,Math.round(levelReward(l)*mult))} perle${l.reward&&l.reward.bonus?' (compreso il bonus boss)':''}${mult!==1?' · ricompensa ×'+mult:''}.</div>
  ${(sv&&!same)?`<div class="shSave shWarn">Hai una partita in corso (${sv.id}): iniziare questo livello la cancella.</div>`:''}
  </div>
  <div class="cmRow shFoot">${same?'<button type="button" class="cmBtn" id="shRes">Riprendi</button><button type="button" class="cmBtn alt" id="shGo">Ricomincia</button>':'<button type="button" class="cmBtn" id="shGo">Inizia</button>'}</div>`;
  sheet.innerHTML='';sheet.appendChild(card);sheet.hidden=false;
  drawMini(card.querySelector('#shMap'),l);
  card.querySelector('#shX').onclick=()=>{sheet.hidden=true};
  card.querySelector('#shGo').onclick=()=>{sheet.hidden=true;startLevel(l)};
  card.querySelectorAll('.shD[data-d]').forEach(b=>{b.onclick=()=>{S.diff=+b.dataset.d;save();openSheet(l)}});
  card.querySelector('#shIns').onclick=()=>note('Insane è bloccata: arriverà più avanti.',1900);
  const r=card.querySelector('#shRes');if(r)r.onclick=()=>{sheet.hidden=true;root.hidden=true;IAV.resume()};
}
function startLevel(l,d){
  d=d===undefined?S.diff:d;root.hidden=true;sheet.hidden=true;
  IAV.startLevel(DF.apply(l,d),{upg:upgMap(d),allow:l.allow||null});
}

/* ------------------------------------------------ Arsenale: unità, potenziamenti e scorte di aiuti */
const BOOST={
  sereno:{n:'Cielo sereno',d:'Azzera il meteo di questo round: niente vento, pioggia, nebbia o gelo.',img:'assets/interfaccia/icona_meteo_sereno.png'},
  cura:{n:'Cura',d:'Le tue unità ferite recuperano fino a 3 vita ciascuna.',img:'assets/interfaccia/icona_cuore.png'},
  rinforzo:{n:'Rinforzo',d:'Un Guerriero in più compare subito sulla tua base.',img:null}
};
const boostTotal=()=>S.boost.sereno+S.boost.cura+S.boost.rinforzo;
IAV.boostCount=boostTotal;
function renderArsenal(b){
  const bx=el('div','cmP');bx.innerHTML='<h3>Scorte di aiuti</h3><p>Li usi durante un livello con il tasto a sinistra, sotto il menu. Ognuno una volta per livello.</p>';
  for(const k of Object.keys(BOOST)){
    const r=el('div','arBoost');r.style.marginTop='9px';
    r.innerHTML=(BOOST[k].img?`<img src="${BOOST[k].img}" alt="">`:`<img src="${IAV.unitImg('G')}" alt="">`)+`<div class="tx"><b>${BOOST[k].n}</b><span>${BOOST[k].d}</span></div><div class="n">×${S.boost[k]}</div>`;
    bx.appendChild(r);
  }
  if(ADS.on()){const v=el('button','cmBtn alt','▶ Guarda un video: +1 aiuto');v.type='button';v.style.marginTop='9px';v.style.width='100%';v.onclick=()=>ADS.rewarded('aiuto in regalo',ok=>{if(!ok)return;const k=['sereno','cura','rinforzo'][Math.floor(Math.random()*3)];S.boost[k]++;save();note('Hai ricevuto: '+BOOST[k].n,1800);renderAll()});bx.appendChild(v)}
  b.appendChild(bx);
  const hd=el('div','cmP','<h3>Potenziamenti</h3><p>Spendi le perle per rendere le unità più forti. Valgono solo in campagna.</p>');b.appendChild(hd);
  for(const t of Object.keys(UN)){
    const open=unitOpen(t),k=S.up[t]||0,T=UT[t],bn=UPB[k],nx=UPB[k+1];
    const row=el('div','cmP arRow'+(open?'':' arLock'));
    const first=firstLevelOf(t);
    row.innerHTML=`<img class="sp" src="${IAV.unitImg(t)}" alt=""><div class="tx"><b>${T.n}</b><span>Vita ${T.hp+bn.hp} · Attacco ${T.atk+bn.atk} · Passi ${T.mv} · Gittata ${T.rg}</span><div class="arPips">${[1,2,3].map(i=>`<i class="${i<=k?'on':''}"></i>`).join('')}</div><span>${open?(nx?'Prossimo: '+(nx.hp-bn.hp?'+'+(nx.hp-bn.hp)+' vita ':'')+(nx.atk-bn.atk?'+'+(nx.atk-bn.atk)+' attacco':''):'Potenziata al massimo'):'Si sblocca completando il livello '+first.id}</span></div>`;
    if(open&&nx){const bt=el('button','cmBtn',`${pearl.replace('<svg','<svg style="width:18px;height:18px"')}${UPC[k]}`);bt.type='button';bt.disabled=S.perle<UPC[k];
      bt.onclick=()=>{if(S.perle<UPC[k])return;S.perle-=UPC[k];S.up[t]=k+1;S.stats.upg=upgCount();save();IAV.sfx('recruit');note(T.n+' potenziato',1400);renderAll()};row.appendChild(bt)}
    b.appendChild(row);
  }
}

/* ------------------------------------------------ Imprese (obiettivi con ricompensa) */
const ACH=[
  ['first','Prima vittoria','Vinci un livello della campagna',()=>S.stats.wins,1,10,'sword'],
  ['lv5','Cadetto','Completa 5 livelli',doneCount,5,20,'flag'],
  ['lv12','Veterano','Completa 12 livelli',doneCount,12,40,'flag'],
  ['lv24','Maresciallo','Completa 24 livelli',doneCount,24,60,'flag'],
  ['lv40','Condottiero','Completa 40 livelli',doneCount,40,70,'flag'],
  ['lv60','Stratega','Completa 60 livelli',doneCount,60,100,'flag'],
  ['lvAll','Leggenda','Completa tutti i livelli della Stagione 1',doneCount,LV.length,250,'crown'],
  ['st10','Cacciatore di stelle','Raccogli 10 stelle',starsTotal,10,20,'star'],
  ['st30','Costellazione','Raccogli 30 stelle',starsTotal,30,50,'star'],
  ['st60','Cielo stellato','Raccogli 60 stelle',starsTotal,60,100,'star'],
  ['st120','Via Lattea','Raccogli 120 stelle',starsTotal,120,150,'star'],
  ['st180','Notte di stelle','Raccogli 180 stelle',starsTotal,180,200,'star'],
  ['stAll','Tre stelle ovunque','Raccogli tutte le stelle',starsTotal,LV.length*3,400,'star'],
  ['k25','Spada e scudo','Sconfiggi 25 nemici',()=>S.stats.kills,25,15,'sword'],
  ['k100','Mietitore','Sconfiggi 100 nemici',()=>S.stats.kills,100,30,'sword'],
  ['k300','Flagello dei mari','Sconfiggi 300 nemici',()=>S.stats.kills,300,80,'sword'],
  ['k600','Tempesta di spade','Sconfiggi 600 nemici',()=>S.stats.kills,600,120,'sword'],
  ['k1000','Leggenda del vento','Sconfiggi 1000 nemici',()=>S.stats.kills,1000,200,'sword'],
  ['perf1','Senza un graffio','Vinci un livello senza perdere unità',()=>S.stats.perfect,1,15,'shield'],
  ['perf8','Imbattibile','Vinci 8 livelli senza perdere unità',()=>S.stats.perfect,8,60,'shield'],
  ['perf25','Intoccabile','Vinci 25 livelli senza perdere unità',()=>S.stats.perfect,25,150,'shield'],
  ['boss1','Cacciatore di boss','Sconfiggi un boss',()=>S.stats.boss,1,30,'crown'],
  ['boss5','Domatore di boss','Sconfiggi 5 boss',()=>S.stats.boss,5,60,'crown'],
  ['boss3','Sovrano dei boss','Sconfiggi tutti i boss',()=>S.stats.boss,WORLDS.length,200,'crown'],
  ['rain','Sotto la pioggia','Vinci un livello mentre piove',()=>S.stats.wx.pioggia||0,1,15,'cloud'],
  ['fog','Nella nebbia','Vinci un livello con la nebbia',()=>S.stats.wx.nebbia||0,1,15,'cloud'],
  ['ice','Sul ghiaccio','Vinci un livello durante il gelo',()=>S.stats.wx.gelo||0,1,15,'cloud'],
  ['wind','Contro vento','Vinci un livello con il vento',()=>S.stats.wx.vento||0,1,15,'cloud'],
  ['er10','Amico del vulcano','Assisti a 10 eruzioni',()=>S.stats.erupt,10,25,'flame'],
  ['er30','Signore del fuoco','Assisti a 30 eruzioni',()=>S.stats.erupt,30,50,'flame'],
  ['fast','Lampo','Vinci un livello in 6 round o meno',()=>S.stats.fast,1,20,'bolt'],
  ['alta1','Sfida accettata','Vinci un livello in difficoltà Alta',()=>LV.filter(l=>dOf(S.lv[l.id])===2).length,1,20,'bolt'],
  ['alta20','Sfidante','Vinci 20 livelli in difficoltà Alta',()=>LV.filter(l=>dOf(S.lv[l.id])===2).length,20,80,'bolt'],
  ['alta24','Maestro del vento','Vinci tutti i livelli in difficoltà Alta',()=>LV.filter(l=>dOf(S.lv[l.id])===2).length,LV.length,400,'crown'],
  ['aid5','Un aiutino','Usa 5 aiuti',()=>S.stats.aids,5,10,'pearl'],
  ['up3','Fabbro','Compra 3 potenziamenti',upgCount,3,15,'hammer'],
  ['up10','Armaiolo','Compra 10 potenziamenti',upgCount,10,40,'hammer'],
  ['up27','Arsenale completo','Compra tutti i potenziamenti',upgCount,27,150,'hammer'],
  ['d3','Costanza','Completa 3 sfide del giorno',()=>S.stats.daily,3,20,'cal'],
  ['d10','Abitudinario','Completa 10 sfide del giorno',()=>S.stats.daily,10,60,'cal'],
  ['w1','Alba conquistata','Completa il Mondo 1',()=>worldDone(1)?1:0,1,50,'flag'],
  ['w2','Oltre la nebbia','Completa il Mondo 2',()=>worldDone(2)?1:0,1,50,'flag'],
  ['w3','Fuoco domato','Completa il Mondo 3',()=>worldDone(3)?1:0,1,80,'flag'],
  ['w4','Dopo la tempesta','Completa il Mondo 4',()=>worldDone(4)?1:0,1,90,'flag'],
  ['w5','Voce del bosco','Completa il Mondo 5',()=>worldDone(5)?1:0,1,100,'flag'],
  ['w6','Cuore di ghiaccio','Completa il Mondo 6',()=>worldDone(6)?1:0,1,110,'flag'],
  ['w7','Domatore di fulmini','Completa il Mondo 7',()=>worldDone(7)?1:0,1,120,'flag'],
  ['w8','Signore dell’arcipelago','Completa il Mondo 8',()=>worldDone(8)?1:0,1,130,'flag'],
  ['w9','Cratere domato','Completa il Mondo 9',()=>worldDone(9)?1:0,1,150,'flag'],
  ['w10','Occhio del ciclone','Completa il Mondo 10',()=>worldDone(10)?1:0,1,250,'crown']
].map(a=>({id:a[0],n:a[1],d:a[2],val:a[3],goal:a[4],rew:a[5],ic:a[6]}));
const achReady=()=>ACH.filter(a=>!S.ach[a.id]&&a.val()>=a.goal).length;
function renderGoals(b){
  const head=el('div','cmP','<h3>Imprese</h3><p>Completale per ricevere perle. Sono sempre a portata di mano: gioca come ti piace.</p>');b.appendChild(head);
  const list=ACH.slice().sort((a,c)=>{const ra=!S.ach[a.id]&&a.val()>=a.goal,rc=!S.ach[c.id]&&c.val()>=c.goal;if(ra!==rc)return ra?-1:1;if(!!S.ach[a.id]!==!!S.ach[c.id])return S.ach[a.id]?1:-1;return 0});
  for(const a of list){
    const v=Math.min(a.val(),a.goal),got=!!S.ach[a.id],rdy=!got&&v>=a.goal;
    const row=el('div','cmP acRow'+(got?' done':''));
    row.innerHTML=`<div class="ic">${ico(got?'trophy':a.ic)}</div><div class="tx"><b>${a.n}</b><span>${a.d}</span><div class="acBar"><i style="width:${Math.round(v/a.goal*100)}%"></i></div><span>${v}/${a.goal}</span></div>`;
    if(rdy){const bt=el('button','cmBtn',`${pearl.replace('<svg','<svg style="width:18px;height:18px"')}+${a.rew}`);bt.type='button';bt.onclick=()=>{S.ach[a.id]=1;S.perle+=a.rew;save();IAV.sfx('recruit');note('Impresa completata: +'+a.rew+' perle',1600);renderAll()};row.appendChild(bt)}
    else row.appendChild(el('div','acRew',got?'✓':pearl+a.rew));
    b.appendChild(row);
  }
}

/* ------------------------------------------------ Sfida del giorno: stesso giorno = stesso campo per tutti. Premio una volta al giorno. */
const pad=n=>String(n).padStart(2,'0');
const dstr=d=>d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate());
const todayStr=()=>dstr(new Date());
const yesterStr=()=>{const d=new Date();d.setDate(d.getDate()-1);return dstr(d)};
const DAYK=[
  {n:'Domenica di vento',d:'Il vento soffia quasi sempre: sfrutta i boschi che riparano.',wx:['vento','vento','vento','sereno'],goal:{t:'stations',hold:3}},
  {n:'Lunedì di pioggia',d:'Passi ridotti e archi più deboli. Tieni le stazioni.',wx:['pioggia','pioggia','pioggia','sereno'],goal:{t:'stations',hold:3}},
  {n:'Martedì di nebbia',d:'Vedi poco e non sai cosa arriva. Attenzione alle stazioni.',wx:['nebbia','nebbia','nebbia','sereno'],goal:{t:'stations',hold:3}},
  {n:'Mercoledì di gelo',d:'I laghi si aprono e si richiudono. Non farti sorprendere sul ghiaccio.',wx:['gelo','gelo','sereno','vento'],goal:{t:'stations',hold:3}},
  {n:'Giovedì di fuoco',d:'Il vulcano erutta ogni 2 round! Tieni le stazioni lontano dal cratere.',wx:['sereno','vento','pioggia'],goal:{t:'stations',hold:3},erupt:2},
  {n:'Venerdì di duello',d:'Cinque contro cinque, nessun rinforzo. Elimina tutti i nemici.',wx:['sereno','vento','pioggia','nebbia'],goal:{t:'elim'},duel:true},
  {n:'Sabato d’assedio',d:'Il nemico arriva a ondate. Resisti fino al round 9.',wx:['sereno','vento','pioggia'],goal:{t:'survive'},siege:true}
];
function hashStr(s){let h=2166136261;for(const c of s){h^=c.charCodeAt(0);h=Math.imul(h,16777619)}return (h>>>0)%900000000+1000}
function dailyDef(ds){
  const dt=new Date(ds+'T12:00:00'),K=DAYK[dt.getDay()],seed=hashStr(ds);
  const rows=IAV.boardRows(seed),h=rows.length,w=rows[0].length;
  const def={id:'daily',world:0,n:0,name:K.n,desc:K.d,tip:'',map:rows,seed,p:[['G',4,11],['A',3,12],['E',5,12]],e:[],coins:[3,0],rounds:K.siege?9:24,maxu:8,erupt:K.erupt||4,
    goal:K.goal,rules:{},ai:{mode:'stations'},lvl:K.siege?'difficile':'normale',weather:{pool:K.wx},allow:['G','A','E','L','W','K','H','B','R'],stars:[],reward:{}};
  // le unità partono accanto alle basi, trovate sul campo vero
  const b0=rows.map((r,y)=>[r.indexOf('1'),y]).find(p=>p[0]>=0),b1=rows.map((r,y)=>[r.indexOf('2'),y]).find(p=>p[0]>=0);
  const near=(b,k)=>{const out=[];for(let r=1;r<5&&out.length<k;r++)for(let dy=-r;dy<=r;dy++)for(let dx=-r;dx<=r;dx++){if(Math.abs(dx)+Math.abs(dy)!==r)continue;const x=b[0]+dx,y=b[1]+dy;if(x<0||y<0||x>=w||y>=h)continue;if('.F'.includes(rows[y][x])&&!out.some(p=>p[0]===x&&p[1]===y)&&out.length<k)out.push([x,y])}return out};
  const mk=(types,b)=>{const c=near(b,types.length);return types.map((t,i)=>[t,c[i][0],c[i][1]])};
  def.p=mk(['G','A','E'],b0);
  if(K.siege){def.e=[];def.coins=[7,0];def.rules={eNoRec:true,eNoRf:true,baseFall:true};def.ai={mode:'hunt'};
    def.waves=[{r:2,u:[['G',{}],['E',{}]],at:[[b1[0],Math.min(h-1,b1[1]+3)]]},{r:4,u:[['G',{}],['A',{}],['L',{}]],at:[[Math.max(0,b1[0]-3),b1[1]+3],[Math.min(w-1,b1[0]+3),b1[1]+3]]},{r:6,u:[['K',{}],['G',{}],['A',{}],['W',{}]],at:[[b1[0],b1[1]+3]]},{r:8,u:[['L',{}],['G',{}],['K',{}]],at:[[b1[0],b1[1]+3]]}]}
  else if(K.duel){def.e=mk(['G','G','A','A','E'],b1);def.p=mk(['G','G','A','A','E'],b0);def.rules={eNoRec:true,eNoRf:true,norec:true,norf:true};def.coins=[0,0];def.ai={mode:'hunt'}}
  else def.e=mk(['G','A','E'],b1);
  return def;
}
function renderDaily(b){
  const ds=todayStr(),K=DAYK[new Date().getDay()],dn=S.daily.done===ds;
  const streak=S.daily.last===ds||S.daily.last===yesterStr()?S.daily.streak:0;
  const nextDay=dn?streak:streak+1,rew=dailyReward(nextDay);
  const c=el('div','cmP');
  c.innerHTML=`<h3>${K.n}</h3><p>${K.d}</p><p style="margin-top:6px">Un campo nuovo ogni giorno, uguale per tutti. Vinci per ricevere <b>${rew.perle} perle</b>${rew.boost?' e un aiuto di ogni tipo':''}.</p>
  <div class="dyDays">${[1,2,3,4,5,6,7].map(i=>`<div class="dyD${i<=streak?' on':''}${i===nextDay&&!dn?' cur':''}">Giorno<b>${i}</b></div>`).join('')}</div>`;
  const bt=el('button','cmBtn',dn?'Completata · torna domani':'Gioca la sfida');bt.type='button';bt.disabled=dn;bt.style.width='100%';bt.onclick=()=>startDaily();c.appendChild(bt);
  if(dn){const p=el('p','','Puoi comunque rigiocarla per allenarti: non dà altre ricompense.');p.style.marginTop='8px';c.appendChild(p);const r=el('button','cmBtn alt','Rigioca per allenarti');r.type='button';r.style.cssText='width:100%;margin-top:8px';r.onclick=()=>startDaily();c.appendChild(r)}
  b.appendChild(c);
  const info=el('div','cmP','<h3>Serie di giorni</h3><p>Se giochi ogni giorno la serie sale e il premio cresce. Il settimo giorno ricevi anche un aiuto di ogni tipo. Se salti un giorno, si riparte dal primo.</p>');b.appendChild(info);
}
function dailyReward(n){const i=((n-1)%7)+1;return {perle:[15,20,25,30,35,40,60][i-1],boost:i===7}}
function startDaily(){root.hidden=true;IAV.startLevel(dailyDef(todayStr()),{upg:upgMap(1),allow:null})}

/* ------------------------------------------------ aiuti durante il livello */
IAV.onAid=()=>{
  const g=IAV.g;if(!g||!g.camp)return;
  const used=g.bu||{};
  const card=el('div','card menu');card.innerHTML='<h2>Aiuti</h2><div class="sc"><p>Ognuno si può usare una volta per livello. Con le stelle conta come «aiuto usato».</p></div>';const sc=card.querySelector('.sc');
  const list=el('div');list.style.cssText='display:flex;flex-direction:column;gap:8px';
  for(const k of Object.keys(BOOST)){
    const r=el('div','cmP arBoost');r.style.margin='0';
    r.innerHTML=(BOOST[k].img?`<img src="${BOOST[k].img}" alt="">`:`<img src="${IAV.unitImg('G')}" alt="">`)+`<div class="tx"><b>${BOOST[k].n}</b><span>${BOOST[k].d}</span></div>`;
    const bt=el('button','cmBtn',used[k]?'Usato':'Usa ×'+S.boost[k]);bt.type='button';bt.style.cssText='flex:none;min-width:84px';bt.disabled=!!used[k]||S.boost[k]<1;
    bt.onclick=()=>{const res=IAV.useBoost(k);if(res.ok&&res.pending){aid.hidden=true}else if(res.ok){S.boost[k]--;S.stats.aids++;save();aid.hidden=true;renderAll()}else note(res.msg,1700)};
    r.appendChild(bt);list.appendChild(r);
  }
  sc.appendChild(list);
  if(ADS.on()){const v=el('button','cmBtn alt','▶ Guarda un video: +1 aiuto');v.type='button';v.onclick=()=>ADS.rewarded('aiuto in regalo',ok=>{if(!ok)return;const k=['sereno','cura','rinforzo'][Math.floor(Math.random()*3)];S.boost[k]++;save();note('Hai ricevuto: '+BOOST[k].n,1600);aid.hidden=true;IAV.onAid()});sc.appendChild(v)}
  const x=el('button','cmBtn alt','Chiudi');x.type='button';x.onclick=()=>{aid.hidden=true};sc.appendChild(x);
  aid.innerHTML='';aid.appendChild(card);aid.hidden=false;
};

/* ------------------------------------------------ fine livello: stelle, ricompense, prossimi passi */
function evalStars(l,g,win){
  if(!win)return {s:0,ok:[]};
  const st=g.st||{lost:0,kills:0,erupt:0,burn:0},ok=[];
  for(const c of l.stars||[]){
    let r=false;
    if(c.t==='rounds')r=g.round<=c.v;else if(c.t==='lost')r=st.lost<=c.v;else if(c.t==='kills')r=st.kills>=c.v;
    else if(c.t==='noaid')r=!g.boostN;else if(c.t==='vipsafe')r=!st.vipHit;else if(c.t==='units')r=g.units.filter(u=>u.o===0).length>=c.v;
    ok.push(r);
  }
  return {s:1+ok.filter(Boolean).length,ok};
}
IAV.onFinish=(g,o)=>{
  const box=$('campEnd'),win=o===0,id=g.camp.id;
  if(id==='daily')return finishDaily(g,win,box);
  const l=byId[id];if(!l)return;
  const dd=g.camp.diff===undefined?1:g.camp.diff;
  const st=g.st||{lost:0,kills:0,erupt:0,burn:0},ev=evalStars(l,g,win),prev=S.lv[id]||{s:0,done:0};
  S.stats.plays++;S.stats.kills+=st.kills||0;S.stats.lost+=st.lost||0;S.stats.erupt+=st.erupt||0;
  let perle=0,first=false,unlockedU=[],note=[],drop=null;
  if(win){
    first=!prev.done;const newS=Math.max(0,ev.s-prev.s);
    perle=newS*10+(first?20+((l.reward&&l.reward.bonus)||0):0)+((!first&&!newS)?3:0);
    perle=Math.max(1,Math.round(perle*DF.mult[dd]));
    S.lv[id]={s:Math.max(prev.s,ev.s),done:1,d:Math.max(prev.done?(prev.d===undefined?1:prev.d):0,dd),bestR:Math.min(prev.bestR||99,g.round),plays:(prev.plays||0)+1};
    S.stats.wins++;if(!(st.lost>0))S.stats.perfect++;if(l.goal.t==='boss'&&first)S.stats.boss++;if(g.round<=6)S.stats.fast++;
    const wt=(g.wx[Math.min(g.round,g.wx.length)-1]||{}).t;if(wt)S.stats.wx[wt]=(S.stats.wx[wt]||0)+1;
    if(first)for(const t of Object.keys(UN))if(!'GAE'.includes(t)&&firstLevelOf(t)&&firstLevelOf(t).id===id)unlockedU.push(t);
    if(ev.s===3&&prev.s<3){const k=['sereno','cura','rinforzo'][Math.floor(Math.random()*3)];S.boost[k]++;drop=k}
    if(worldDone(l.world)&&!S.wd[l.world]){S.wd[l.world]=1;perle+=100;for(const k of Object.keys(S.boost))S.boost[k]++;note.push('Mondo completato! +100 perle e un aiuto di ogni tipo.')}
    S.perle+=perle;
  }else{S.lv[id]=Object.assign({s:0,done:0},prev,{plays:(prev.plays||0)});}
  save();
  const nx=nextOf(l),canNext=win&&nx&&unlocked(nx);
  let h='';
  if(win)h+=`<div class="ceStars">${[1,2,3].map(k=>star(k<=ev.s).replace('<svg','<svg class="'+(k<=ev.s?'pop':'')+'" style="animation-delay:'+(1.4+k*.35)+'s"')).join('')}</div>`;
  h+=`<div class="ceRows">`;
  if(win){h+=`<div class="ceRow">${tick}<span>Livello completato</span></div>`;(l.stars||[]).forEach((c,i)=>{h+=`<div class="ceRow${ev.ok[i]?'':' no'}">${ev.ok[i]?tick:cross}<span>${c.txt}</span></div>`})}
  else h+=`<div class="ceRow no">${cross}<span>Riprova: puoi cambiare strategia. Ogni livello ha un modo per vincere.</span></div>`;
  h+=`</div>`;
  if(win)h+=`<div class="ceRew">${pearl}+${perle}</div>`+(dd!==1?`<div class="ceNote">Difficoltà ${DN[dd]}: perle ×${DF.mult[dd]}</div>`:'');
  for(const t of unlockedU)h+=`<div class="ceNote"><img src="${IAV.unitImg(t)}" alt="">Nuova unità: <b>${UT[t].n}</b> (ora anche nell’Arsenale)</div>`;
  if(drop)h+=`<div class="ceNote">Tre stelle! Ricevi un aiuto: <b>${BOOST[drop].n}</b></div>`;
  for(const n of note)h+=`<div class="ceNote">${n}</div>`;
  h+=`<div class="ceBtns"></div>`;box.innerHTML=h;
  const bs=box.querySelector('.ceBtns'),add=(t,alt,fn)=>{const b=el('button','cmBtn'+(alt?' alt':''),t);b.type='button';b.onclick=fn;bs.appendChild(b);return b};
  if(win&&ADS.on()&&perle>0){let dbl=add('▶ Raddoppia le perle (video)',true,()=>ADS.rewarded('perle doppie',ok=>{if(!ok)return;S.perle+=perle;save();dbl.disabled=true;dbl.textContent='Perle raddoppiate!';box.querySelector('.ceRew').innerHTML=pearl+'+'+perle*2;setTop()}))}
  if(canNext)add('Prossimo livello',false,()=>{$('ovEnd').hidden=true;startLevel(nx)});
  add(win?'Rigioca il livello':'Riprova',!!canNext,()=>{$('ovEnd').hidden=true;startLevel(l)});
  add('Torna alla mappa',true,()=>{$('ovEnd').hidden=true;openCamp('map',win&&nx&&unlocked(nx)?nx.id:l.id)});
  renderAll();
};
function finishDaily(g,win,box){
  const ds=todayStr();let h='',perle=0,boost=false;
  S.stats.plays++;const st=g.st||{};S.stats.kills+=st.kills||0;S.stats.lost+=st.lost||0;S.stats.erupt+=st.erupt||0;
  if(win&&S.daily.done!==ds){
    const streak=S.daily.last===yesterStr()?S.daily.streak+1:(S.daily.last===ds?S.daily.streak:1);
    const r=dailyReward(streak);perle=r.perle;boost=r.boost;S.daily={last:ds,streak,done:ds};S.stats.daily++;S.perle+=perle;if(boost)for(const k of Object.keys(S.boost))S.boost[k]++;
  }
  save();
  if(win){h+=`<div class="ceStars">${star(true).replace('<svg','<svg class="pop"')}</div>`;h+=perle?`<div class="ceRew">${pearl}+${perle}</div><div class="ceNote">Serie: ${S.daily.streak} ${S.daily.streak===1?'giorno':'giorni'}${boost?' · ricevi un aiuto di ogni tipo':''}</div>`:'<div class="ceNote">Già completata oggi: nessuna altra ricompensa, ma ottimo allenamento.</div>'}
  else h+=`<div class="ceNote">Non è andata: puoi riprovare quante volte vuoi.</div>`;
  h+='<div class="ceBtns"></div>';box.innerHTML=h;
  const bs=box.querySelector('.ceBtns'),add=(t,alt,fn)=>{const b=el('button','cmBtn'+(alt?' alt':''),t);b.type='button';b.onclick=fn;bs.appendChild(b)};
  if(!win||perle===0)add('Riprova',false,()=>{$('ovEnd').hidden=true;startDaily()});
  add('Torna alla campagna',win&&perle>0?false:true,()=>{$('ovEnd').hidden=true;openCamp('daily')});
  renderAll();
}

/* ------------------------------------------------ menu principale: pulsante Campagna e impostazioni pubblicità */
function refreshHome(){
  const s=$('campSub');if(!s)return;
  const c=currentLevel(),n=doneCount();
  const gw=WORLDS.find(W=>!worldOpen(W.id));
  s.textContent=c?('Livello '+c.id+' · ⭐ '+starsTotal()+'/'+LV.length*3):(n===LV.length?('Stagione 1 completata! ⭐ '+starsTotal()+'/'+LV.length*3):(gw?('Mondo '+gw.id+': servono ⭐ '+gw.need+' · hai '+starsTotal()):'⭐ '+starsTotal()+'/'+LV.length*3));
  const bd=$('campBadge');if(bd){const k=achReady()+(S.daily.done!==todayStr()?1:0);bd.textContent=k;bd.hidden=!k}
  const ba=$('bAds');if(ba)ba.textContent='Pubblicità (prova): '+(ADS.on()?'accesa':'spenta');
}
if($('bCamp'))$('bCamp').onclick=()=>openCamp('map');
if($('bAds'))$('bAds').onclick=()=>ADS.set(ADS.on()?'off':'prova');
IAV.openCamp=()=>openCamp('map');
IAV.onMenu=()=>{root.hidden=true;refreshHome()};
IAV.ADS=ADS;
window.IAVCamp={S:()=>S,reset:()=>{S=defState();save();renderAll()},open:openCamp,levels:LV,worlds:WORLDS,startLevel,dailyDef,evalStars,unlocked,done,give:o=>{Object.assign(S,o);save();renderAll()},finish:IAV.onFinish};
ADS.refresh();refreshHome();
})();
