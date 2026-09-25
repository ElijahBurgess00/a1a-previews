(function(){
  var doc=document.documentElement;doc.classList.remove('no-js');
  var body=document.body;

  // Header: transparent over the home hero, solid once scrolled or on subpages
  var header=document.querySelector('.site-header');
  var overHero=body.hasAttribute('data-hero');
  function onScroll(){
    var solid=!overHero||window.scrollY>24;
    header.classList.toggle('solid',solid);
    header.classList.toggle('over',!solid);
  }
  onScroll();window.addEventListener('scroll',onScroll,{passive:true});

  // Mobile drawer: overlay, ESC, focus trap, scroll lock
  var burger=document.querySelector('.burger'),drawer=document.getElementById('mobile-drawer'),overlay=document.querySelector('.drawer-overlay');
  function focusables(){return drawer.querySelectorAll('a,button')}
  function openDrawer(){body.classList.add('drawer-open');burger.setAttribute('aria-expanded','true');drawer.removeAttribute('inert');var f=focusables();if(f[0])f[0].focus()}
  function closeDrawer(){body.classList.remove('drawer-open');burger.setAttribute('aria-expanded','false');drawer.setAttribute('inert','');burger.focus({preventScroll:true})}
  burger.addEventListener('click',openDrawer);
  overlay.addEventListener('click',closeDrawer);
  drawer.querySelector('.drawer-close').addEventListener('click',closeDrawer);
  drawer.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){body.classList.remove('drawer-open');burger.setAttribute('aria-expanded','false');drawer.setAttribute('inert','')})});
  document.addEventListener('keydown',function(e){
    if(!body.classList.contains('drawer-open'))return;
    if(e.key==='Escape'){closeDrawer();return}
    if(e.key==='Tab'){var f=focusables(),first=f[0],last=f[f.length-1];
      if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus()}
      else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus()}}
  });

  // Reveal on scroll
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-visible');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(el){io.observe(el)});
  }else{els.forEach(function(el){el.classList.add('is-visible')})}

  // Before / after sliders
  document.querySelectorAll('.ba').forEach(function(ba){
    var r=ba.querySelector('input');if(!r)return;
    var set=function(){ba.style.setProperty('--pos',r.value+'%')};r.addEventListener('input',set);set();
  });

  // Estimate form -> pre-filled email (no backend on the preview)
  var f=document.getElementById('estimate-form');
  if(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var E=f.elements,bad=null;
      ['name','phone'].forEach(function(n){if(!E[n].value.trim()){E[n].classList.add('err');bad=bad||E[n]}});
      var em=E['email'].value.trim();
      if(em&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em)){E['email'].classList.add('err');bad=bad||E['email']}
      if(bad){bad.focus();return}
      var body='Name: '+E['name'].value.trim()+'\nPhone: '+E['phone'].value.trim()+'\nEmail: '+em+'\nProperty address: '+E['address'].value.trim()+'\nService: '+(E['service'].value||'Not specified')+'\n\nNotes: '+E['message'].value.trim();
      window.location.href='mailto:Magictouchpw7@gmail.com?subject='+encodeURIComponent('Free Estimate Request - '+E['name'].value.trim())+'&body='+encodeURIComponent(body);
      document.getElementById('form-done').classList.add('show');
    });
    f.querySelectorAll('input').forEach(function(i){i.addEventListener('input',function(){i.classList.remove('err')})});
    // Pre-select service from ?service=
    var m=location.search.match(/[?&]service=([^&]+)/);
    if(m){var v=decodeURIComponent(m[1].replace(/\+/g,' '));var s=f.elements['service'];for(var k=0;k<s.options.length;k++){if(s.options[k].value===v){s.selectedIndex=k}}}
  }

  var y=document.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
})();
