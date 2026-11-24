/* Isole al Vento - difficoltà della campagna: Facile, Medio, Alta (e Insane, per ora bloccata).
   Parte dalla difficoltà «disegnata» del livello e la sposta: niente stravolge la mappa, cambia solo l'avversario e un po' di aiuti. */
(()=>{
'use strict';
const ORD=['facile','normale','difficile'];

const NAMES=['Facile','Medio','Alta','Insane'];
const MULT=[0.6,1,1.5];            // moltiplicatore delle perle di ricompensa
const PBONUS=[{hp:1,atk:0},{hp:0,atk:0},{hp:0,atk:0}]; // bonus a tutte le tue unità
const clone=o=>JSON.parse(JSON.stringify(o));
function apply(def,d){
  const o=clone(def);d=(d===0||d===1||d===2)?d:1;o.diff=d;
  const base=Math.max(0,ORD.indexOf(def.lvl||'normale'));
  // Facile: avversario «facile» (piu' lento e distratto, non recluta), +3 monete, 2 round in piu', nemici un po' piu' fragili, tue unita' +1 vita.
  // Medio: avversario tra «facile» e «normale», +2 monete. Alta: avversario «normale» come disegnato (mai il «difficile»).
  // Un livello nato «facile» (i primi) resta facile in Medio e diventa «normale» in Alta.
  if(d===0)o.lvl='facile';
  else if(d===1){if(base===0)o.lvl='facile';else{o.lvl='normale';o.aiOv=Object.assign({},o.aiOv,{noise:2.2,skip:0.33})}}
  else o.lvl='normale';
  if(d===1&&o.coins)o.coins[0]+=2;
  if(d===0){
    if(o.coins)o.coins[0]+=3;
    if(o.goal&&o.goal.t!=='survive'&&o.rounds)o.rounds+=2;
    for(const u of o.e||[]){const ex=u[3]=u[3]||{};if(ex.boss)ex.bh=Math.round((ex.bh||0)*0.75);else ex.bh=(ex.bh||0)-1}
    for(const w of o.waves||[])for(const u of w.u){const ex=u[1]=u[1]||{};ex.bh=(ex.bh||0)-1}
  }
  return o;
}
window.CAMP_DIFF={names:NAMES,mult:MULT,pbonus:PBONUS,apply};
})();
