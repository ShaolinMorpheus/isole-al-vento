/* Bozza C: suoni piu' ricchi (file sintetizzati). Se un file manca, resta il suono di prima. */
(function(){
  var names=['tap','sel','turn','move','hit','kill','recruit','erupt','win','lose','draw','w_pioggia','w_vento','w_gelo','w_nebbia','w_sereno'];
  var B={},loading=false,VOL={tap:.9,sel:.8,turn:.7,move:.8,hit:1,kill:1,recruit:.8,erupt:1,win:.9,lose:.9,draw:.9,w_pioggia:.8,w_vento:.9,w_gelo:.8,w_nebbia:.9,w_sereno:.8};
  function load(){
    if(loading)return;var a=acx();if(!a)return;loading=true;
    names.forEach(function(n){fetch('assets/audio/'+n+'.mp3').then(function(r){return r.arrayBuffer()}).then(function(b){return new Promise(function(ok,ko){a.decodeAudioData(b,ok,ko)})}).then(function(d){B[n]=d}).catch(function(){})});
  }
  document.addEventListener('pointerdown',load,{passive:true});
  function play(n){var a=acx();if(!a||!B[n])return false;var s=a.createBufferSource(),g=a.createGain();s.buffer=B[n];g.gain.value=VOL[n]||1;s.connect(g);g.connect(a.destination);s.start();return true}
  var _sfx=sfx,_wx=weatherSfx;
  var T0=0;
  document.addEventListener('pointerdown',function(e){if(e.target.closest&&e.target.closest('#ovStart button'))T0=Date.now()},true);
  function quiet(){return Date.now()-T0<6000}
  sfx=function(k){
    if(k==='turn')return;
    if(quiet()&&k!=='sel')return;
    if(SND&&B[k]){var s=SND;SND=false;try{_sfx(k)}finally{SND=s}play(k);return}
    _sfx(k);
  };
  weatherSfx=function(w){
    if(quiet())return;
    if(!SND||!w)return _wx(w);
    var n='w_'+(['pioggia','vento','gelo','nebbia'].indexOf(w.t)>=0?w.t:'sereno');
    if(!B[n])return _wx(w);
    duck(5);play(n);
  };
})();

/* Bozza C: Arsenale con icone Blender (vita/attacco/passi/gittata) e foto ingrandibile al tocco. */
(function(){
  var IC={Vita:'vita',Attacco:'attacco',Passi:'passi',Gittata:'gittata'};
  function fix(){
    var l=document.querySelectorAll('.arRow .tx > span:not([data-ic])');
    for(var i=0;i<l.length;i++){
      var s=l[i],m=s.textContent.match(/^Vita (\d+) · Attacco (\d+) · Passi (\d+) · Gittata (\d+)/);
      s.setAttribute('data-ic','1');if(!m)continue;
      var h='',k=['Vita','Attacco','Passi','Gittata'];
      for(var j=0;j<4;j++)h+='<span class="stc" title="'+k[j]+'"><img src="assets/icone/'+IC[k[j]]+'.webp" alt="'+k[j]+'"><b>'+m[j+1]+'</b><small>'+k[j]+'</small></span>';
      s.innerHTML=h;s.className='stRow';
    }
  }
  new MutationObserver(fix).observe(document.documentElement,{childList:true,subtree:true});
  document.addEventListener('click',function(e){
    var im=e.target.closest&&e.target.closest('.arRow img.sp');
    if(!im)return;
    var nm=im.parentNode.querySelector('.tx b');
    var o=document.createElement('div');o.className='spZoom';
    o.innerHTML='<img src="'+im.src+'" alt=""><div>'+(nm?nm.textContent:'')+'</div>';
    o.onclick=function(){o.remove()};document.body.appendChild(o);
  });
})();

/* Bozza C: barra vita con cornice Blender; avversario nascosto finche' non si muove (poi su tutte); sempre dentro il campo. */
(function(){
  var _hp=hpBar,lastG=null,seen=false,FR=new Image();FR.src='assets/hp/ui_hp_barra.webp';
  hpBar=function(u,x,hy,hw){
    if(g!==lastG){lastG=g;seen=false}
    if(!seen&&(g.round>1||g.units.some(function(v){return v.o===1&&(v.moved||v.done)})))seen=true;
    if(u.o===1&&!seen)return;
    hy=Math.max(hy,5);
    if(!FR.complete||!FR.naturalWidth)return _hp(u,x,hy,hw);
    var cs=lay.cs,bh=Math.max(9,Math.round(cs*.22)),hx=x-hw/2,hv=Math.max(0,u.hv===undefined?u.hp:u.hv),f=hv/mhp(u);
    ctx.fillStyle='rgba(8,24,32,.92)';rr(hx,hy,hw,bh,bh/2);ctx.fill();
    ctx.save();rr(hx,hy,hw,bh,bh/2);ctx.clip();
    var gr=ctx.createLinearGradient(0,hy,0,hy+bh),c1=f>.55?'#7fe6cf':f>.28?'#ffd36b':'#ff8a7a',c2=f>.55?'#2fa58f':f>.28?'#d69220':'#c53a2c';
    gr.addColorStop(0,c1);gr.addColorStop(1,c2);ctx.fillStyle=gr;ctx.fillRect(hx,hy,Math.max(0,hw*f),bh);
    ctx.fillStyle='rgba(255,255,255,.28)';ctx.fillRect(hx,hy+1,Math.max(0,hw*f),bh*.32);ctx.restore();
    var fw=hw/.69,fh=bh/.76;ctx.drawImage(FR,x-fw/2,hy+bh/2-fh/2,fw,fh);
    ctx.font='800 '+Math.round(bh*.92)+'px Nunito, system-ui, sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';
    ctx.lineWidth=2.2;ctx.strokeStyle='rgba(8,18,26,.9)';ctx.lineJoin='round';var tx=String(Math.ceil(hv-.001));ctx.strokeText(tx,x,hy+bh/2+.5);ctx.fillStyle='#fff';ctx.fillText(tx,x,hy+bh/2+.5);
    ctx.textBaseline='alphabetic';
    if(u.boss||u.vip){
      var R=bh*.82,bx=hx-R*.95-bh*.3,by=hy+bh/2;
      ctx.save();ctx.translate(bx,by);ctx.lineJoin='round';ctx.lineWidth=2;ctx.strokeStyle='rgba(8,18,26,.95)';
      ctx.fillStyle=u.boss?'#ef6a5a':'#6fd0ff';ctx.beginPath();
      if(u.boss){ctx.moveTo(-R,R*.7);ctx.lineTo(-R,-R*.4);ctx.lineTo(-R*.5,R*.1);ctx.lineTo(0,-R*.8);ctx.lineTo(R*.5,R*.1);ctx.lineTo(R,-R*.4);ctx.lineTo(R,R*.7);ctx.closePath()}
      else{for(var i=0;i<10;i++){var a=-Math.PI/2+i*Math.PI/5,r0=i%2?R*.45:R;ctx.lineTo(Math.cos(a)*r0,Math.sin(a)*r0)}ctx.closePath()}
      ctx.stroke();ctx.fill();ctx.restore();
    }
  };
})();
