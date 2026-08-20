/* Harmony Clinic — Unified Site Header (works identically on every page) */
(function () {
    'use strict';

    /**
     * Determines the relative path prefix based on the page's location.
     * Pages in /blog/ subdirectory need "../" to reach the root, all others use "".
     */
    function getBasePath() {
        const path = (window.location.pathname || '').toLowerCase();
        if (path.indexOf('/blog/') !== -1) return '../';
        return '';
    }

    /**
     * Returns true when the current page IS index.html (the home page),
     * because section anchors like #team, #prices, #contacts live there.
     */
    function isHomePage() {
        const path = (window.location.pathname || '');
        const file = path.split('/').pop();
        return !file || file === '' || file === 'index.html';
    }

    /**
     * Build the header HTML.
     * - On index.html: anchors are plain "#section"
     * - On every other page: anchors become "<base>index.html#section"
     */
    /**
     * Builds the UA/RU language switcher.
     * UA is active (current page). RU links to the matching page inside /ru/.
     */
    function buildLangSwitcher(base) {
        const path = (window.location.pathname || '');
        const file = (path.split('/').pop()) || 'index.html';
        const inBlog = path.toLowerCase().indexOf('/blog/') !== -1;
        const ruFile = (file === 'maliukin-andriy.html') ? 'maliukin-andrey.html' : file;
        const ruHref = base + 'ru/' + (inBlog ? 'blog/' : '') + ruFile;
        return ''
            + '<div class="lang-switcher">'
            +     '<a href="' + file + '" class="active" aria-current="true">UA</a>'
            +     '<a href="' + ruHref + '" hreflang="ru" aria-label="Русская версия">RU</a>'
            + '</div>';
    }

    function buildHeaderHTML() {
        const base = getBasePath();
        const home = isHomePage();
        const anchorBase = home ? '' : (base + 'index.html');

        return ''
            + '<div class="container nav-wrapper">'
            +     '<a href="' + base + 'index.html" class="logo" aria-label="Harmony Clinic — Головна">'
            +         '<picture>'
            +             '<source srcset="' + base + 'images/Logo.webp" type="image/webp">'
            +             '<img loading="lazy" src="' + base + 'images/Logo.png" alt="Harmony Clinic">'
            +         '</picture>'
            +     '</a>'
            +     '<nav role="navigation" aria-label="Головне меню">'
            +         '<ul class="nav-menu" id="navMenu">'
            +             '<li><a href="' + base + 'index.html">Головна</a></li>'
            +             '<li><a href="' + base + 'services-ua.html">Послуги</a></li>'
            +             '<li><a href="' + anchorBase + '#team">Лікарі</a></li>'
            +             '<li><a href="' + anchorBase + '#works">Роботи</a></li>'
            +             '<li><a href="' + anchorBase + '#reviews">Відгуки</a></li>'
            +             '<li><a href="' + anchorBase + '#prices">Ціни</a></li>'
            +             '<li><a href="' + base + 'blog.html">Блог</a></li>'
            +             '<li><a href="' + anchorBase + '#contacts">Контакти</a></li>'
            +         '</ul>'
            +     '</nav>'
            +     '<div class="header-actions" style="display:flex; align-items:center; gap:15px;">'
            +         '<a href="tel:+380687794547" aria-label="Зателефонувати" class="header-phone desktop-only" '
            +             'onclick="return (typeof gtag_report_conversion===\'function\')?gtag_report_conversion(\'tel:+380687794547\'):true;">'
            +             '+38 068 779 45 47'
            +         '</a>'
            +         '<a href="' + anchorBase + '#booking-form" class="btn-header-cta">Записатися</a>'
            +         buildLangSwitcher(base)
            +         '<div class="mobile-toggle" onclick="toggleMenu()" role="button" tabindex="0" aria-label="Відкрити меню">☰</div>'
            +     '</div>'
            + '</div>';
    }

    function injectHeader() {
        const newHtml = buildHeaderHTML();
        let header = document.querySelector('header[role="banner"]') || document.querySelector('body > header');

        if (header) {
            // Replace contents of the existing <header>, keep its tag (so layout/CSS stay intact)
            header.setAttribute('role', 'banner');
            header.innerHTML = newHtml;
        } else {
            // No header on the page — create one and place it at the very top of <body>
            header = document.createElement('header');
            header.setAttribute('role', 'banner');
            header.innerHTML = newHtml;
            if (document.body) {
                document.body.insertBefore(header, document.body.firstChild);
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', injectHeader);
    } else {
        injectHeader();
    }
})();
