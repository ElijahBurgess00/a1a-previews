/* Magic Touch: before/after slider and the estimate form (mailto; no server on the preview host). */
(function () {
  document.querySelectorAll("[data-ba]").forEach(function (ba) {
    var r = ba.querySelector("input[type=range]");
    var set = function () { ba.style.setProperty("--pos", r.value + "%"); };
    r.addEventListener("input", set); set();
  });
  var form = document.getElementById("estimate-form");
  if (!form) return;
  var status = document.getElementById("form-status");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var missing = [];
    form.querySelectorAll("[required]").forEach(function (el) { if (!el.value.trim()) missing.push(el); });
    if (missing.length) { status.hidden = false; status.classList.add("is-error"); status.textContent = "Please add your name and mobile number."; missing[0].focus(); return; }
    var svc = [].map.call(form.querySelectorAll("input[name=services]:checked"), function (i) { return i.value; });
    var v = function (n) { var el = form.elements[n]; return el ? el.value.trim() : ""; };
    var body = "Services: " + (svc.join(", ") || "Not sure yet") + "\nCity: " + v("city") + "\nAddress: " + v("address") +
      "\nName: " + v("name") + "\nPhone: " + v("phone") + "\nEmail: " + v("email") + "\n\n" + v("notes");
    status.hidden = false; status.classList.remove("is-error");
    status.textContent = "Opening your email app. If nothing opens, call or text (321) 355-9521.";
    window.location.href = "mailto:" + form.getAttribute("data-email") + "?subject=" + encodeURIComponent("Free estimate request") + "&body=" + encodeURIComponent(body);
  });
})();
