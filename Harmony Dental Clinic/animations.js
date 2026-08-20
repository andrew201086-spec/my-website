/**
 * Harmony Clinic — Animations Module
 * Pure Vanilla JS, no libraries, zero render-blocking.
 * Uses IntersectionObserver (supported in all modern browsers).
 */

(function () {
  'use strict';

  /* ============================================================
   * 1. SCROLL REVEAL — fade-in + slide-up for section elements
   * ============================================================ */
  function initScrollReveal() {
    // Elements that should animate on scroll
    var selectors = [
      '.section-title',
      '.feature-item',
      '.type-item',
      '.step-item',
      '.digital-card',
      '.team-card',
      '.review-card',
      '.case-card',
      '.about-text',
      '.about-img',
      '.sterilization-text',
      '.sterilization-img',
      '.booking-strip',
      '.accordion-item',
      '.price-row',
      '.booking-form-section',
      '.hero-google-badge',
    ].join(',');

    var elements = document.querySelectorAll(selectors);

    // Add initial hidden state
    elements.forEach(function (el, i) {
      el.classList.add('hc-reveal');
      // Stagger cards in grids
      var parent = el.parentElement;
      if (parent) {
        var siblings = parent.querySelectorAll('.feature-item, .type-item, .step-item, .digital-card');
        siblings.forEach(function (sib, idx) {
          sib.style.transitionDelay = (idx * 80) + 'ms';
        });
      }
    });

    if (!('IntersectionObserver' in window)) {
      // Fallback: just show everything
      elements.forEach(function (el) { el.classList.add('hc-revealed'); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('hc-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    elements.forEach(function (el) { observer.observe(el); });
  }

  /* ============================================================
   * 2. ANIMATED COUNTERS — for stat numbers
   * ============================================================ */
  function animateCounter(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var decimals = (el.getAttribute('data-count').indexOf('.') !== -1) ? 1 : 0;
    var duration = 1600;
    var start = performance.now();

    function step(now) {
      var elapsed = now - start;
      var progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = (target * eased).toFixed(decimals);
      el.textContent = current + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function initCounters() {
    var counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    if (!('IntersectionObserver' in window)) {
      counters.forEach(function (el) { animateCounter(el); });
      return;
    }

    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting && !entry.target.classList.contains('hc-counted')) {
          entry.target.classList.add('hc-counted');
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(function (el) { counterObserver.observe(el); });
  }

  /* ============================================================
   * 3. READING PROGRESS BAR
   * ============================================================ */
  function initProgressBar() {
    var bar = document.createElement('div');
    bar.id = 'hc-progress';
    bar.setAttribute('role', 'progressbar');
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          var scrollTop = window.scrollY || document.documentElement.scrollTop;
          var docHeight = document.documentElement.scrollHeight - window.innerHeight;
          var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
          bar.style.width = pct + '%';
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  /* ============================================================
   * 4. HEADER SCROLL BEHAVIOUR — shrink + shadow on scroll
   * ============================================================ */
  function initHeaderScroll() {
    var header = document.querySelector('header');
    if (!header) return;

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          if (window.scrollY > 60) {
            header.classList.add('hc-scrolled');
          } else {
            header.classList.remove('hc-scrolled');
          }
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  /* ============================================================
   * 5. HERO PARALLAX — subtle depth on background
   * ============================================================ */
  function initHeroParallax() {
    var hero = document.querySelector('.hero');
    if (!hero) return;
    // Skip on mobile (save battery, avoid janky scroll)
    if (window.innerWidth < 768) return;

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          var scrolled = window.scrollY;
          if (scrolled < window.innerHeight) {
            // Move background 30% of scroll speed
            hero.style.backgroundPositionY = 'calc(center + ' + (scrolled * 0.3) + 'px)';
          }
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  /* ============================================================
   * 6. CARD TILT EFFECT — subtle 3D on hover (desktop only)
   * ============================================================ */
  function initCardTilt() {
    if (window.innerWidth < 768) return;

    var cards = document.querySelectorAll('.feature-item, .team-card, .review-card, .digital-card, .type-item, .step-item');

    cards.forEach(function (card) {
      card.addEventListener('mousemove', function (e) {
        var rect = card.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        var cx = rect.width / 2;
        var cy = rect.height / 2;
        var tiltX = ((y - cy) / cy) * 4;   // max 4deg
        var tiltY = ((cx - x) / cx) * 4;
        card.style.transform = 'translateY(-5px) perspective(600px) rotateX(' + tiltX + 'deg) rotateY(' + tiltY + 'deg)';
        card.style.boxShadow = '0 20px 50px rgba(82,97,84,0.18), 0 8px 20px rgba(0,0,0,0.08)';
      });

      card.addEventListener('mouseleave', function () {
        card.style.transform = '';
        card.style.boxShadow = '';
        card.style.transition = 'transform 0.5s ease, box-shadow 0.5s ease';
        setTimeout(function () { card.style.transition = ''; }, 500);
      });
    });
  }

  /* ============================================================
   * 7. HERO CONTENT ENTRANCE — staggered animation on load
   * ============================================================ */
  function initHeroEntrance() {
    var logo = document.querySelector('.hero-logo');
    var title = document.querySelector('.hero-title');
    var slogan = document.querySelector('.hero-slogan');
    var offer = document.querySelector('.hero-offer');
    var btn = document.querySelector('.hero .btn-primary');
    var badge = document.querySelector('.hero-google-badge');

    var items = [logo, title, slogan, offer, btn, badge].filter(Boolean);
    items.forEach(function (el, i) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(24px)';
      el.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
      el.style.transitionDelay = (i * 120 + 100) + 'ms';
    });

    // Trigger after a brief moment so CSS is applied first
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        items.forEach(function (el) {
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        });
      });
    });
  }

  /* ============================================================
   * 8. SMOOTH ANCHOR LINKS — enhanced smooth scroll with offset
   * ============================================================ */
  function initSmoothAnchors() {
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
      link.addEventListener('click', function (e) {
        var href = link.getAttribute('href');
        if (href === '#') return;
        var target = document.querySelector(href);
        if (!target) return;
        e.preventDefault();
        var headerH = (document.querySelector('header') || {}).offsetHeight || 80;
        var top = target.getBoundingClientRect().top + window.scrollY - headerH - 12;
        window.scrollTo({ top: top, behavior: 'smooth' });
      });
    });
  }

  /* ============================================================
   * 9. BOOKING FORM — field focus glow effect
   * ============================================================ */
  function initFormEffects() {
    document.querySelectorAll('.form-input, input[type="text"], input[type="tel"], input[type="email"], textarea').forEach(function (input) {
      input.addEventListener('focus', function () {
        var wrap = input.closest('.form-group, .input-wrap, div') || input.parentElement;
        if (wrap) wrap.classList.add('hc-input-focused');
      });
      input.addEventListener('blur', function () {
        var wrap = input.closest('.form-group, .input-wrap, div') || input.parentElement;
        if (wrap) wrap.classList.remove('hc-input-focused');
      });
    });
  }

  /* ============================================================
   * INIT — run after DOM is ready
   * ============================================================ */
  function init() {
    initScrollReveal();
    initCounters();
    initProgressBar();
    initHeaderScroll();
    initHeroParallax();
    initHeroEntrance();
    initSmoothAnchors();
    initFormEffects();

    // Card tilt only on non-touch devices
    if (!('ontouchstart' in window)) {
      initCardTilt();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
