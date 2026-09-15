// Source-aware booking links and click counting (ADR 0020).
//
// 1. Read the channel from ?utm_source= on the landing URL, remember it for the
//    session, fall back to the referrer host, else "direct".
// 2. Point every booking link at that channel's Google Calendar schedule, so the
//    booked event itself tells us where the lead came from.
// 3. Count clicks on booking and email links, and form submits, as GoatCounter
//    events named "<event>-<source>". No cookies, no identity, no consent banner.
(function () {
  "use strict";

  // One schedule per channel, identical to the visitor; only the URL differs.
  var CALENDARS = {
    site: "https://calendar.app.google/FEXpdugSUPuZpBtg6",
    linkedin: "https://calendar.app.google/bBushU4HFchrVNR48",
    substack: "https://calendar.app.google/wz5ugX2Letg92BH89"
  };
  var STORAGE_KEY = "ttc_source";

  function fromQuery() {
    var m = /[?&]utm_source=([^&#]*)/.exec(window.location.search);
    if (!m) return "";
    return decodeURIComponent(m[1]).toLowerCase().replace(/[^a-z0-9-]/g, "").slice(0, 32);
  }

  function fromReferrer() {
    var ref = document.referrer || "";
    if (!ref) return "";
    if (/(^|\.)linkedin\.com\//.test(ref)) return "linkedin";
    if (/substack\.com\/|writing\.tilinthecloud\.com\//.test(ref)) return "substack";
    if (/(^|\.)google\.[a-z.]+\//.test(ref)) return "google";
    if (/tilinthecloud\.com\//.test(ref)) return "";
    return "referral";
  }

  function remember(source) {
    try { window.sessionStorage.setItem(STORAGE_KEY, source); } catch (e) { /* storage blocked: fine */ }
  }

  function recall() {
    try { return window.sessionStorage.getItem(STORAGE_KEY) || ""; } catch (e) { return ""; }
  }

  function resolveSource() {
    var source = fromQuery();
    if (source) { remember(source); return source; }
    source = recall();
    if (source) return source;
    source = fromReferrer() || "direct";
    remember(source);
    return source;
  }

  function count(name, source) {
    var gc = window.goatcounter;
    if (!gc || typeof gc.count !== "function") return;
    gc.count({ path: name + "-" + source, title: name, event: true });
  }

  function wire() {
    var source = resolveSource();
    var calendar = CALENDARS[source] || CALENDARS.site;
    var links = document.querySelectorAll("a[href]");

    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      var href = a.getAttribute("href") || "";
      if (href.indexOf("https://calendar.app.google/") === 0) {
        a.setAttribute("href", calendar);
        a.addEventListener("click", count.bind(null, "click-book", source));
      } else if (href.indexOf("mailto:") === 0) {
        a.addEventListener("click", count.bind(null, "click-email", source));
      }
    }

    var forms = document.querySelectorAll("form");
    for (var j = 0; j < forms.length; j++) {
      var field = forms[j].querySelector('input[name="source"]');
      if (field) { field.value = source; field.setAttribute("value", source); }
      forms[j].addEventListener("submit", count.bind(null, "submit-form", source));
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wire);
  } else {
    wire();
  }
})();
