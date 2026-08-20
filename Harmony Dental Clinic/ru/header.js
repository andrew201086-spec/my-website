/* Harmony Clinic — Единая шапка сайта (русская версия для папки /ru/) */
(function () {
    'use strict';

    /**
     * Путь до корня сайта (для картинок, стилей, украинских страниц).
     * Страницы в /ru/blog/ требуют "../../", остальные в /ru/ — "../".
     */
    function getSiteRoot() {
        const path = (window.location.pathname || '').toLowerCase();
        if (path.indexOf('/ru/blog/') !== -1) return '../../';
        return '../';
    }

    /**
     * Путь до корня /ru/ (для русских страниц).
     * Страницы в /ru/blog/ требуют "../", остальные в /ru/ — "".
     */
    function getRuRoot() {
        const path = (window.location.pathname || '').toLowerCase();
        if (path.indexOf('/ru/blog/') !== -1) return '../';
        return '';
    }

    /**
     * true, если текущая страница — /ru/index.html (главная),
     * на которой находятся якоря #team, #prices, #contacts и т.д.
     */
    function isHomePage() {
        const path = (window.location.pathname || '');
        const file = path.split('/').pop();
        return !file || file === '' || file === 'index.html';
    }

    /**
     * Переключатель UA/RU. RU активен (текущая страница).
     * UA ведёт на соответствующую украинскую страницу в корне сайта.
     */
    function buildLangSwitcher(siteRoot) {
        const path = (window.location.pathname || '');
        const file = (path.split('/').pop()) || 'index.html';
        const inBlog = path.toLowerCase().indexOf('/ru/blog/') !== -1;
        const uaFile = (file === 'maliukin-andrey.html') ? 'maliukin-andriy.html' : file;
        const uaHref = siteRoot + (inBlog ? 'blog/' : '') + uaFile;
        return ''
            + '<div class="lang-switcher">'
            +     '<a href="' + uaHref + '" hreflang="uk" aria-label="Українська версія">UA</a>'
            +     '<a href="' + file + '" class="active" aria-current="true">RU</a>'
            + '</div>';
    }

    function buildHeaderHTML() {
        const siteRoot = getSiteRoot();
        const ruRoot = getRuRoot();
        const home = isHomePage();
        const anchorBase = home ? '' : (ruRoot + 'index.html');

        return ''
            + '<div class="container nav-wrapper">'
            +     '<a href="' + ruRoot + 'index.html" class="logo" aria-label="Harmony Clinic — Главная">'
            +         '<picture>'
            +             '<source srcset="' + siteRoot + 'images/Logo.webp" type="image/webp">'
            +             '<img loading="lazy" src="' + siteRoot + 'images/Logo.png" alt="Harmony Clinic">'
            +         '</picture>'
            +     '</a>'
            +     '<nav role="navigation" aria-label="Главное меню">'
            +         '<ul class="nav-menu" id="navMenu">'
            +             '<li><a href="' + ruRoot + 'index.html">Главная</a></li>'
            +             '<li><a href="' + ruRoot + 'services-ua.html">Услуги</a></li>'
            +             '<li><a href="' + anchorBase + '#team">Врачи</a></li>'
            +             '<li><a href="' + anchorBase + '#works">Работы</a></li>'
            +             '<li><a href="' + anchorBase + '#reviews">Отзывы</a></li>'
            +             '<li><a href="' + anchorBase + '#prices">Цены</a></li>'
            +             '<li><a href="' + ruRoot + 'blog.html">Блог</a></li>'
            +             '<li><a href="' + anchorBase + '#contacts">Контакты</a></li>'
            +         '</ul>'
            +     '</nav>'
            +     '<div class="header-actions" style="display:flex; align-items:center; gap:15px;">'
            +         '<a href="tel:+380687794547" aria-label="Позвонить" class="header-phone desktop-only" '
            +             'onclick="return (typeof gtag_report_conversion===\'function\')?gtag_report_conversion(\'tel:+380687794547\'):true;">'
            +             '+38 068 779 45 47'
            +         '</a>'
            +         '<a href="' + anchorBase + '#booking-form" class="btn-header-cta">Записаться</a>'
            +         buildLangSwitcher(siteRoot)
            +         '<div class="mobile-toggle" onclick="toggleMenu()" role="button" tabindex="0" aria-label="Открыть меню">☰</div>'
            +     '</div>'
            + '</div>';
    }

    function injectHeader() {
        const newHtml = buildHeaderHTML();
        let header = document.querySelector('header[role="banner"]') || document.querySelector('body > header');

        if (header) {
            header.setAttribute('role', 'banner');
            header.innerHTML = newHtml;
        } else {
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
