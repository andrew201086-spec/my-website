/* Harmony Clinic — Unified Mobile Menu (works identically on every page) */
(function () {
    'use strict';

    const MENU_ITEMS = [
        { href: 'index.html', text: 'Головна' },
        { href: 'services-ua.html', text: 'Послуги' },
        { href: 'implants-ua.html', text: 'Імплантація' },
        { href: 'prosthetics-ua.html', text: 'Протезування' },
        { href: 'orthodontics-ua.html', text: 'Ортодонтія' },
        { href: 'lechenie-ua.html', text: 'Лікування зубів' },
        { href: 'hygiene-ua.html', text: 'Гігієна' },
        { href: 'extraction-ua.html', text: 'Видалення' },
        { href: 'blog.html', text: 'Блог' },
        { href: 'index.html#contacts', text: 'Контакти' }
    ];

    const PHONE = '+380687794547';
    const PHONE_DISPLAY = '+38 068 779 45 47';

    function getCurrentPage() {
        const path = (window.location.pathname || '').split('/').pop();
        return path || 'index.html';
    }

    function buildMenu() {
        // Remove any previous instance (e.g. legacy hard-coded blocks)
        document.querySelectorAll('#mobileMenu, #mobileMenuBackdrop, .mobile-menu, .mobile-menu-backdrop').forEach(el => el.remove());

        const current = getCurrentPage();

        // Backdrop
        const backdrop = document.createElement('div');
        backdrop.id = 'mobileMenuBackdrop';
        backdrop.className = 'mobile-menu-backdrop';
        backdrop.addEventListener('click', closeMenu);

        // Menu container
        const menu = document.createElement('aside');
        menu.id = 'mobileMenu';
        menu.className = 'mobile-menu';
        menu.setAttribute('aria-label', 'Мобільне меню');
        menu.setAttribute('role', 'dialog');
        menu.setAttribute('aria-hidden', 'true');

        // Header (logo + close)
        const header = document.createElement('div');
        header.className = 'mobile-menu-header';

        const logo = document.createElement('a');
        logo.href = 'index.html';
        logo.className = 'mobile-menu-logo';
        logo.setAttribute('aria-label', 'Harmony Clinic');
        logo.innerHTML = '<img src="images/Logo.png" alt="Harmony Clinic">';
        logo.addEventListener('click', () => setTimeout(closeMenu, 50));

        const closeBtn = document.createElement('button');
        closeBtn.className = 'close-btn';
        closeBtn.type = 'button';
        closeBtn.setAttribute('aria-label', 'Закрити меню');
        closeBtn.textContent = '×'; // ×
        closeBtn.addEventListener('click', closeMenu);

        header.appendChild(logo);
        header.appendChild(closeBtn);

        // Nav links
        const nav = document.createElement('nav');
        nav.className = 'mobile-menu-nav';
        MENU_ITEMS.forEach(item => {
            const a = document.createElement('a');
            a.href = item.href;
            a.textContent = item.text;
            if (item.href.split('#')[0] === current) a.classList.add('current');
            a.addEventListener('click', () => setTimeout(closeMenu, 80));
            nav.appendChild(a);
        });

        // Footer (phone + booking CTA)
        const footer = document.createElement('div');
        footer.className = 'mobile-menu-footer';

        const phone = document.createElement('a');
        phone.href = 'tel:' + PHONE;
        phone.className = 'mobile-menu-phone';
        phone.setAttribute('aria-label', 'Зателефонувати');
        phone.innerHTML =
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">' +
            '<path d="M20 15.5c-1.25 0-2.45-.2-3.57-.57a1.02 1.02 0 0 0-1.02.24l-2.2 2.2a15.05 15.05 0 0 1-6.59-6.58l2.2-2.21c.28-.27.36-.66.25-1.01A11.36 11.36 0 0 1 8.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1z"/>' +
            '</svg>' + PHONE_DISPLAY;
        phone.addEventListener('click', () => setTimeout(closeMenu, 50));

        const cta = document.createElement('a');
        cta.href = current === 'index.html' ? '#booking-form' : 'index.html#booking-form';
        cta.className = 'mobile-menu-cta';
        cta.textContent = 'Записатися на прийом';
        cta.addEventListener('click', () => setTimeout(closeMenu, 50));

        footer.appendChild(phone);
        footer.appendChild(cta);

        menu.appendChild(header);
        menu.appendChild(nav);
        menu.appendChild(footer);

        document.body.appendChild(backdrop);
        document.body.appendChild(menu);
    }

    function openMenu() {
        let menu = document.getElementById('mobileMenu');
        if (!menu) { buildMenu(); menu = document.getElementById('mobileMenu'); }
        const bd = document.getElementById('mobileMenuBackdrop');
        if (menu) {
            menu.classList.add('active');
            menu.setAttribute('aria-hidden', 'false');
        }
        if (bd) bd.classList.add('active');
        document.body.classList.add('menu-open');
    }

    function closeMenu() {
        const menu = document.getElementById('mobileMenu');
        const bd = document.getElementById('mobileMenuBackdrop');
        if (menu) {
            menu.classList.remove('active');
            menu.setAttribute('aria-hidden', 'true');
        }
        if (bd) bd.classList.remove('active');
        document.body.classList.remove('menu-open');
    }

    function toggleMenu() {
        const menu = document.getElementById('mobileMenu');
        if (menu && menu.classList.contains('active')) closeMenu();
        else openMenu();
    }

    // ESC closes
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape' || e.keyCode === 27) closeMenu();
    });

    // Close when viewport widens past breakpoint
    window.addEventListener('resize', () => {
        if (window.innerWidth > 992) closeMenu();
    });

    function init() {
        buildMenu();
        // Make sure every existing .mobile-toggle button works,
        // even if its inline handler points at the old function.
        document.querySelectorAll('.mobile-toggle').forEach(btn => {
            btn.onclick = function (e) { e.preventDefault(); toggleMenu(); };
            btn.setAttribute('aria-label', 'Відкрити меню');
            btn.setAttribute('role', 'button');
            btn.setAttribute('tabindex', '0');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Backwards compatibility: pages already call toggleMenu()/closeMenu() inline.
    window.toggleMenu = toggleMenu;
    window.openMenu = openMenu;
    window.closeMenu = closeMenu;
})();
