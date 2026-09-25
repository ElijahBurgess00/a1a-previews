/* ==========================================================================
   COASTAL VALLEY CHARTERS: main.js
   Vanilla, dependency-free. Hero film loader, mobile drawer, dropdown a11y,
   accordion, reveals, sticky book bar, desktop nudge, CTA tracking, gallery
   filters, booking form (live price + AJAX). Chassis from Brightwild Adventures.
   ========================================================================== */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var RATES = { 4: 650, 6: 800, extra: 100, base: 2, cruise: 600, boat: 650, cruiseMax: 3 };

  document.addEventListener("DOMContentLoaded", function () {
    initHeroVideo();
    initMobileDrawer();
    initDesktopDropdowns();
    initAccordion();
    initReveals();
    initBookBar();
    initNudge();
    initTracking();
    initGalleryFilters();
    initBookForm();
  });

  /* Hero film. The markup ships with no src, so nothing downloads for no-JS or
     reduced-motion visitors and the poster stays. The swap is gated on the
     `playing` signal (never a timer), and play() is retried on the first gesture
     and on pageshow because iOS low-power mode and bfcache both block autoplay. */
  function initHeroVideo() {
    var v = document.querySelector(".hero video[data-src]");
    if (!v || reduceMotion) return;
    var hero = v.closest(".hero");
    var conn = navigator.connection || {};
    if (conn.saveData || /(^|-)2g$/.test(conn.effectiveType || "")) return;
    v.addEventListener("playing", function () { hero.classList.add("video-ready"); });
    v.addEventListener("error", function () { hero.classList.remove("video-ready"); });
    // Phones and slow connections get the 540px encode (about half the bytes).
    var sm = v.getAttribute("data-src-sm");
    var small = window.matchMedia("(max-width: 700px)").matches || /3g/.test(conn.effectiveType || "");
    v.src = (sm && small) ? sm : v.getAttribute("data-src");
    v.load();
    function tryPlay() { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
    tryPlay();
    // Stop decoding once the hero is scrolled away: saves battery on phones.
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (en) { if (en[0].isIntersecting) { if (v.paused) tryPlay(); } else if (!v.paused) v.pause(); }, { threshold: 0.05 }).observe(hero);
    }
    ["touchstart", "click", "scroll"].forEach(function (ev) { window.addEventListener(ev, function once() { if (v.paused) tryPlay(); window.removeEventListener(ev, once); }, { passive: true }); });
    window.addEventListener("pageshow", function () { if (v.paused) tryPlay(); });
  }

  function initMobileDrawer() {
    var burger = document.querySelector(".hamburger");
    var drawer = document.querySelector(".mobile-drawer");
    if (!burger || !drawer) return;
    function open() { document.body.classList.add("drawer-open"); burger.setAttribute("aria-expanded", "true"); burger.setAttribute("aria-label", "Close menu"); drawer.setAttribute("aria-hidden", "false"); }
    function close() { document.body.classList.remove("drawer-open"); burger.setAttribute("aria-expanded", "false"); burger.setAttribute("aria-label", "Open menu"); drawer.setAttribute("aria-hidden", "true"); }
    burger.addEventListener("click", function () { document.body.classList.contains("drawer-open") ? close() : open(); });
    drawer.querySelectorAll(".drawer-group > .drawer-link").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var expanded = btn.closest(".drawer-group").classList.toggle("open");
        btn.setAttribute("aria-expanded", expanded ? "true" : "false");
      });
    });
    drawer.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", close); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
    window.addEventListener("resize", function () { if (window.innerWidth > 1120) close(); });
  }

  function initDesktopDropdowns() {
    var items = document.querySelectorAll(".nav-item.has-dropdown");
    function closeAll() { items.forEach(function (i) { i.classList.remove("open"); var t = i.querySelector(".nav-link"); if (t) t.setAttribute("aria-expanded", "false"); }); }
    items.forEach(function (item) {
      var trigger = item.querySelector(".nav-link");
      var menu = item.querySelector(".dropdown");
      if (!trigger || !menu) return;
      trigger.setAttribute("aria-haspopup", "true");
      trigger.setAttribute("aria-expanded", "false");
      trigger.addEventListener("click", function (e) { e.preventDefault(); var was = item.classList.contains("open"); closeAll(); if (!was) { item.classList.add("open"); trigger.setAttribute("aria-expanded", "true"); } });
      trigger.addEventListener("keydown", function (e) { if (e.key === "ArrowDown") { e.preventDefault(); item.classList.add("open"); trigger.setAttribute("aria-expanded", "true"); var f = menu.querySelector("a"); if (f) f.focus(); } });
      item.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeAll(); trigger.focus(); } });
      item.addEventListener("focusout", function (e) { if (!item.contains(e.relatedTarget)) closeAll(); });
    });
    document.addEventListener("click", function (e) { if (!e.target.closest(".nav-item.has-dropdown")) closeAll(); });
  }

  function initAccordion() {
    document.querySelectorAll(".acc-trigger").forEach(function (trigger) {
      var panel = document.getElementById(trigger.getAttribute("aria-controls"));
      if (!panel) return;
      trigger.addEventListener("click", function () {
        var expanded = trigger.getAttribute("aria-expanded") === "true";
        var acc = trigger.closest(".accordion");
        if (acc && !expanded) acc.querySelectorAll(".acc-trigger[aria-expanded='true']").forEach(function (o) { o.setAttribute("aria-expanded", "false"); var op = document.getElementById(o.getAttribute("aria-controls")); if (op) op.style.maxHeight = null; });
        trigger.setAttribute("aria-expanded", expanded ? "false" : "true");
        panel.style.maxHeight = expanded ? null : panel.scrollHeight + "px";
      });
    });
    window.addEventListener("resize", function () { document.querySelectorAll(".acc-trigger[aria-expanded='true']").forEach(function (t) { var p = document.getElementById(t.getAttribute("aria-controls")); if (p) p.style.maxHeight = p.scrollHeight + "px"; }); });
  }

  /* Reveals only arm once the observer exists; elements already in view are
     marked visible in the same frame, so nothing above the fold ever flashes. */
  function initReveals() {
    var els = document.querySelectorAll(".reveal");
    if (!els.length || reduceMotion || !("IntersectionObserver" in window)) return;
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-visible"); obs.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
    els.forEach(function (el) { if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("is-visible"); obs.observe(el); });
    root.classList.add("reveal-armed");
    // A hidden tab never fires the observer: reveal everything when it matters.
    document.addEventListener("visibilitychange", function () { if (document.visibilityState === "visible") return; els.forEach(function (el) { el.classList.add("is-visible"); }); });
    window.addEventListener("beforeprint", function () { els.forEach(function (el) { el.classList.add("is-visible"); }); });
  }

  function initBookBar() {
    var bar = document.querySelector(".mobile-book-bar");
    if (!bar) return;
    function update() { bar.classList.toggle("visible", window.scrollY > 380); }
    update();
    window.addEventListener("scroll", update, { passive: true });
  }

  function initNudge() {
    var nudge = document.querySelector(".book-nudge");
    if (!nudge || !window.matchMedia("(min-width: 901px)").matches) return;
    try { if (sessionStorage.getItem("mt_nudge_closed") === "1") return; } catch (e) {}
    nudge.querySelector(".book-nudge__close").addEventListener("click", function () { nudge.classList.remove("visible"); try { sessionStorage.setItem("mt_nudge_closed", "1"); } catch (e) {} });
    var onScroll = function () {
      var frac = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight;
      if (frac >= 0.45) { nudge.classList.add("visible"); window.removeEventListener("scroll", onScroll); }
    };
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function track(name, data) {
    window.dataLayer = window.dataLayer || [];
    var payload = { event: name };
    for (var k in (data || {})) payload[k] = data[k];
    window.dataLayer.push(payload);
    if (typeof window.gtag === "function") { try { window.gtag("event", name, data || {}); } catch (e) {} }
  }

  function initTracking() {
    document.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest("a[data-cta]") : null;
      if (!a) return;
      var href = a.getAttribute("href") || "";
      var name = href.indexOf("tel:") === 0 ? "call_click" : (href.indexOf("estimate/") !== -1 ? "book_click" : (href.indexOf("captainexperiences") !== -1 ? "marketplace_click" : "cta_click"));
      track(name, { placement: a.getAttribute("data-cta"), page_path: location.pathname });
    }, true);
  }

  function initGalleryFilters() {
    var filters = document.querySelectorAll(".gallery-filter");
    if (!filters.length) return;
    var items = document.querySelectorAll("[data-gallery-item]");
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var cat = btn.getAttribute("data-filter");
        filters.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
        btn.setAttribute("aria-pressed", "true");
        items.forEach(function (item) {
          var cats = (item.getAttribute("data-cats") || "").split(" ");
          var show = cat === "all" ? true : cats.indexOf(cat) !== -1;
          item.hidden = !show;
          item.style.display = show ? "" : "none";
        });
      });
    });
  }

  /* Booking form: trip prefill from ?trip=, live total, AJAX submit. Fishing
     charters price from trip length and anglers; sandbar and sunset trips are a
     flat rate; sheepshead and corporate are quoted by the captain. When the
     endpoint is not configured it answers non-2xx and the visitor is told
     plainly, with working alternatives. Never a fake success. */
  function initBookForm() {
    var form = document.getElementById("book-form");
    if (!form) return;
    var status = document.getElementById("form-status");
    var total = document.getElementById("book-total");
    var note = document.getElementById("book-total-note");
    var anglersBox = document.getElementById("bf-anglers");
    var hoursBox = document.getElementById("bf-hours");
    var sizeEl = document.getElementById("bf-size");
    var groupBox = document.getElementById("bf-group");
    var companyWrap = document.getElementById("bf-company-wrap");
    var sizeLabel = form.querySelector('label[for="bf-size"]');
    var CE = form.getAttribute("data-ce");

    var want = (new URLSearchParams(location.search)).get("trip");
    if (want) { var pre = form.querySelector('input[name="trip"][data-key="' + want.replace(/[^a-z0-9]/gi, "") + '"]'); if (pre) pre.checked = true; }

    var dateEl = form.querySelector("#bf-date"), date2El = form.querySelector("#bf-date2");
    var today = new Date(); today.setMinutes(today.getMinutes() - today.getTimezoneOffset());
    var min = today.toISOString().slice(0, 10);
    if (dateEl) dateEl.min = min;
    if (date2El) date2El.min = min;

    function recalc() {
      var t = form.querySelector('input[name="trip"]:checked');
      var kind = t.getAttribute("data-kind");
      var fishing = kind === "fish" || kind === "sheeps";
      anglersBox.hidden = !fishing;
      hoursBox.hidden = kind !== "sheeps";
      groupBox.hidden = fishing;
      companyWrap.hidden = kind !== "corp";
      if (sizeLabel) sizeLabel.textContent = kind === "corp" ? "Number of people" : "Number of guests (up to 3)";
      if (sizeEl) { if (kind === "cruise") sizeEl.max = RATES.cruiseMax; else sizeEl.removeAttribute("max"); }
      if (fishing) {
        // Sheepshead trips are 4 or 6 hours at the same rates as every fishing charter.
        var h = kind === "sheeps" ? +form.querySelector('input[name="hours"]:checked').getAttribute("data-h") : +t.getAttribute("data-hours");
        var n = +form.querySelector('input[name="anglers"]:checked').getAttribute("data-n");
        var amt = RATES[h] + Math.max(0, n - RATES.base) * RATES.extra;
        total.textContent = "$" + amt;
        note.textContent = h + "-hour " + (kind === "sheeps" ? "sheepshead trip" : "fishing charter") + ", " + n + (n === 1 ? " angler" : " anglers") + ". No deposit, paid to the captain on the day.";
        return "$" + amt;
      }
      if (kind === "cruise") {
        total.textContent = "$" + RATES.cruise;
        note.textContent = t.value + ", four hours, flat rate for up to 3 guests. Drinks, ice and a cooler included. No deposit.";
        return "$" + RATES.cruise;
      }
      total.textContent = "$" + RATES.boat + " per boat";
      note.textContent = "Everything included on every boat. Captain Wills replies with the number of boats for your group.";
      return "$" + RATES.boat + " per boat";
    }
    form.addEventListener("change", recalc);
    recalc();

    function show(html, isError) { status.hidden = false; status.innerHTML = html; status.classList.toggle("is-error", !!isError); status.scrollIntoView({ block: "nearest", behavior: reduceMotion ? "auto" : "smooth" }); }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var hp = form.querySelector('[name="_gotcha"]');
      if (hp && hp.value) return;
      var bad = null;
      form.querySelectorAll("[required]").forEach(function (el) {
        var ok = el.value.trim() !== "" && (el.type !== "email" || /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value.trim()));
        el.classList.toggle("is-invalid", !ok);
        el.setAttribute("aria-invalid", ok ? "false" : "true");
        if (!ok && !bad) bad = el;
      });
      if (bad) { show("Add a preferred date, a name, a mobile number and an email so Captain Wills can reply.", true); bad.focus(); return; }
      var kindNow = form.querySelector('input[name="trip"]:checked').getAttribute("data-kind");
      var sizeNow = +(form.querySelector('#bf-size') || {}).value || 0;
      if (kindNow === "cruise" && sizeNow > RATES.cruiseMax) { show("Sandbar trips and sunset cruises take up to 3 guests. For a bigger group, call Captain Wills.", true); return; }
      var btn = form.querySelector('button[type="submit"]');
      var label = btn.innerHTML;
      btn.disabled = true; btn.textContent = "Sending";
      var kind = form.querySelector('input[name="trip"]:checked').getAttribute("data-kind");
      var fd = new FormData(form);
      var body = {}; fd.forEach(function (v, k) { body[k] = v; });
      if (kind !== "fish" && kind !== "sheeps") delete body.anglers; else { delete body.group_size; delete body.company; }
      if (kind !== "sheeps") delete body.hours;
      body.quoted_total = recalc();
      body.page = location.href;
      fetch(form.getAttribute("action"), { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(body) })
        .then(function (r) { if (!r.ok) throw new Error("status " + r.status); return r.json().catch(function () { return {}; }); })
        .then(function () {
          show("Request sent. Captain Wills will reply to confirm your date and a start time.");
          form.reset(); recalc();
          track("generate_lead", { form_id: "book", trip: body.trip, value: body.quoted_total });
        })
        .catch(function () {
          var tel = form.getAttribute("data-tel"), telShow = form.getAttribute("data-tel-display");
          var call = tel ? 'Call Captain Wills at <a href="tel:' + tel + '">' + telShow + '</a>' : 'Message <a href="https://www.instagram.com/coastalvalleycharters/" rel="noopener">@coastalvalleycharters</a> on Instagram';
          var em = form.getAttribute("data-email");
          var mail = em ? ', or email <a href="mailto:' + em + '?subject=' + encodeURIComponent("Booking request: " + body.trip + ", " + body.date) + '">' + em + '</a>' : "";
          var alt = kind === "fish" ? mail + ', or lock in a fishing trip through <a href="' + CE + '" rel="noopener">instant booking on Captain Experiences</a>.' : mail + " to book.";
          show("This request could not be sent from the site right now, and nothing was submitted. " + call + alt, true);
          track("book_form_error", { trip: body.trip });
        })
        .finally(function () { btn.disabled = false; btn.innerHTML = label; });
    });
  }
})();
