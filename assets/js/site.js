/* Flowsmart Electrical — shared behaviour.
   IntersectionObserver reveals everywhere; GSAP adds hero polish on the
   landing page only (and degrades silently if the CDN is unreachable). */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) document.documentElement.classList.add("no-motion");

  /* ---------------------------------------------------- sticky header --- */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("scrolled", window.scrollY > 80);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ------------------------------------------------------- mobile nav --- */
  var burger = document.querySelector(".nav-burger");
  var mobileNav = document.querySelector(".mobile-nav");
  if (burger && mobileNav) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      mobileNav.hidden = open;
      document.body.style.overflow = open ? "" : "hidden";
    });
    mobileNav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        burger.setAttribute("aria-expanded", "false");
        mobileNav.hidden = true;
        document.body.style.overflow = "";
      }
    });
  }

  /* --------------------------------------------------- scroll reveals --- */
  var revealables = [].slice.call(document.querySelectorAll(".rv, .rv-clip, .step-card"));
  if (reduceMotion) {
    revealables.forEach(function (el) { el.classList.add("in"); });
  } else if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target); // once: true
        }
      });
    }, { rootMargin: "0px 0px -20% 0px", threshold: 0.01 }); // fires ~80% viewport
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------------------------------------------------- FAQ accordion --- */
  document.querySelectorAll(".faq-q").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var expanded = btn.getAttribute("aria-expanded") === "true";
      var panel = document.getElementById(btn.getAttribute("aria-controls"));
      // close siblings in the same list for a tidy accordion
      btn.closest(".faq, .wrap-narrow").querySelectorAll(".faq-q[aria-expanded='true']").forEach(function (other) {
        if (other !== btn) {
          other.setAttribute("aria-expanded", "false");
          var p = document.getElementById(other.getAttribute("aria-controls"));
          if (p) p.style.maxHeight = "0px";
        }
      });
      btn.setAttribute("aria-expanded", String(!expanded));
      if (panel) panel.style.maxHeight = expanded ? "0px" : panel.scrollHeight + 24 + "px";
    });
  });

  /* ------------------------------------------------- testimonial loop --- */
  var track = document.querySelector(".marquee-track");
  if (track) {
    track.innerHTML += track.innerHTML; // duplicate content for a seamless -50% loop
  }

  /* -------------------------------------------- quote form validation --- */
  document.querySelectorAll(".quote-form").forEach(function (form) {
    function validateField(input) {
      var field = input.closest(".qf-field");
      if (!field) return true;
      var ok = input.checkValidity();
      field.classList.toggle("invalid", !ok);
      return ok;
    }
    form.querySelectorAll("input, textarea").forEach(function (input) {
      input.addEventListener("blur", function () { validateField(input); });
      input.addEventListener("input", function () {
        if (input.closest(".qf-field").classList.contains("invalid")) validateField(input);
      });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var allOk = true;
      form.querySelectorAll("input[required], textarea[required]").forEach(function (input) {
        if (!validateField(input)) allOk = false;
      });
      if (!allOk) {
        var firstBad = form.querySelector(".qf-field.invalid input, .qf-field.invalid textarea");
        if (firstBad) firstBad.focus();
        return;
      }
      // NOTE: when the GHL form id is set in build.py this native form is
      // replaced by the GHL inline embed and this handler never runs.
      // Set the GHL form redirect to /thank-you for conversion tracking.
      window.location.href = form.getAttribute("data-redirect") || "/thank-you";
    });
  });

  /* ---------------------------------------------------- cookie consent --- */
  var bar = document.querySelector(".cookie-bar");
  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function read(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }

  var loaded = false;
  function loadTracking() {
    if (loaded) return;                      // never double-load
    loaded = true;
    /* --- Google Analytics 4 --- */
    if (window.FSE_GA && window.FSE_GA.indexOf("XXXX") === -1) {
      var s = document.createElement("script");
      s.async = true;
      s.src = "https://www.googletagmanager.com/gtag/js?id=" + window.FSE_GA;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("js", new Date());
      window.gtag("config", window.FSE_GA, { anonymize_ip: true });
      /* thank-you page → lead conversion */
      if ((document.body.getAttribute("data-page") || "") === "thank-you.html") {
        window.gtag("event", "generate_lead", { currency: "AUD" });
        // TODO Google Ads: uncomment + fill once the Ads account exists
        // window.gtag("event", "conversion", { send_to: "AW-XXXXXXXXX/XXXXXXX" });
      }
    }
    /* --- GoHighLevel external tracking (lead source attribution) --- */
    if (window.FSE_GHL_TRACK) {
      var g = document.createElement("script");
      g.src = "https://link.msgsndr.com/js/external-tracking.js";
      g.setAttribute("data-tracking-id", window.FSE_GHL_TRACK);
      document.body.appendChild(g);
    }
  }

  /* declining clears anything a previous visit may have set */
  function clearTrackingCookies() {
    try {
      document.cookie.split(";").forEach(function (c) {
        var name = c.split("=")[0].trim();
        if (/^(_ga|_gid|_gcl|__ptq|_fbp)/.test(name)) {
          document.cookie = name + "=; Max-Age=0; path=/";
          document.cookie = name + "=; Max-Age=0; path=/; domain=." + location.hostname.replace(/^www\./, "");
        }
      });
    } catch (e) {}
  }

  function toast(msg) {
    var t = document.createElement("div");
    t.className = "cookie-toast";
    t.setAttribute("role", "status");
    t.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 13 4 4L19 7"/></svg><span></span>';
    t.querySelector("span").textContent = msg;
    document.body.appendChild(t);
    requestAnimationFrame(function () { t.classList.add("is-in"); });
    setTimeout(function () {
      t.classList.remove("is-in");
      setTimeout(function () { t.remove(); }, 400);
    }, 2600);
  }

  function dismissBar() {
    if (!bar) return;
    bar.classList.remove("is-in");
    bar.classList.add("is-out");
    var done = false;
    function finish() { if (done) return; done = true; bar.hidden = true; }
    bar.addEventListener("transitionend", finish, { once: true });
    setTimeout(finish, 500);                 // fallback if transitionend never fires
  }

  var consent = read("fse-consent");
  if (consent === "yes") {
    loadTracking();
  } else if (bar && consent !== "no") {
    setTimeout(function () {
      bar.hidden = false;
      requestAnimationFrame(function () { bar.classList.add("is-in"); });
    }, 1000);
    bar.addEventListener("click", function (e) {
      var b = e.target.closest("[data-cookie]");
      if (!b) return;
      e.preventDefault();
      var yes = b.getAttribute("data-cookie") === "accept";
      store("fse-consent", yes ? "yes" : "no");
      dismissBar();
      if (yes) { loadTracking(); toast("Thanks — analytics on."); }
      else { clearTrackingCookies(); toast("No worries — analytics off."); }
    });
  }

  /* ----------------------------------------------- landing: GSAP layer --- */
  if (!document.body.classList.contains("landing") || reduceMotion) {
    // static hero for subpages / reduced motion
    document.querySelectorAll("[data-hero]").forEach(function (el) {
      el.style.opacity = 1; el.style.transform = "none";
    });
    return;
  }
  function heroFallback() {
    document.querySelectorAll("[data-hero]").forEach(function (el, i) {
      el.style.transition = "opacity .6s ease " + i * 130 + "ms, transform .6s cubic-bezier(.22,.7,.3,1) " + i * 130 + "ms";
      requestAnimationFrame(function () { el.style.opacity = 1; el.style.transform = "none"; });
    });
  }
  window.addEventListener("load", function () {
    if (!window.gsap) { heroFallback(); return; }
    /* hero entry: stagger fade-up, ~800ms total, ease-out */
    gsap.to("[data-hero]", {
      opacity: 1, y: 0, duration: 0.55, ease: "power3.out", stagger: 0.13
    });
    /* mouse parallax on floating shapes */
    var shapes = [].slice.call(document.querySelectorAll(".hero-shape"));
    if (shapes.length && window.matchMedia("(pointer:fine)").matches) {
      document.querySelector(".hero").addEventListener("mousemove", function (e) {
        var cx = e.clientX / window.innerWidth - 0.5;
        var cy = e.clientY / window.innerHeight - 0.5;
        shapes.forEach(function (s) {
          var d = parseFloat(s.getAttribute("data-depth") || 12);
          gsap.to(s, { x: cx * d, y: cy * d, duration: 1.1, ease: "power2.out", overwrite: "auto" });
        });
      });
    }
    /* section headline drift: a touch of extra ease on scroll (ScrollTrigger) */
    if (window.ScrollTrigger) {
      gsap.registerPlugin(ScrollTrigger);
      gsap.utils.toArray(".pull-quote blockquote").forEach(function (q) {
        gsap.from(q, {
          y: 40, opacity: 0, duration: 0.9, ease: "power3.out",
          scrollTrigger: { trigger: q, start: "top 82%", once: true }
        });
      });
      /* step numbers count-scale in */
      gsap.utils.toArray(".step-num").forEach(function (n) {
        gsap.from(n, {
          scale: 1.4, opacity: 0, duration: 0.8, ease: "power3.out",
          scrollTrigger: { trigger: n, start: "top 85%", once: true }
        });
      });
    }
  });
})();
