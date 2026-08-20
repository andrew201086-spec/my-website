#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for All-on-4 / All-on-6 landing pages:
- Realistic, medically grounded, and ethical copy (no unrealistic promises like "never hurts", "lasts 100 years", etc.)
- Clear and transparent pricing breakdown (Alpha Dent + beam bridge)
- Painless local anesthesia explained realistically (minimizing discomfort, no general anesthesia/sleep)
- Full support for Ukrainian and Russian versions with correct relative assets paths.
"""

import os

def get_ua_html():
    return """<!DOCTYPE html>
<html lang="uk">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Analytics: dataLayer + gtag stub available immediately; heavy scripts deferred -->
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config','G-6ZP07STZJF');
    gtag('config','AW-11468618731');

    function gtag_report_conversion(url){
        var navigate=function(){ if(typeof url!=='undefined'){ window.location=url; } };
        gtag('event','conversion',{'send_to':'AW-11468618731/s-heCPmCmt0bEOv31Nwq','event_callback':navigate});
        loadDeferredTags();
        setTimeout(navigate, 700);
        return false;
    }
    var gtag_report_call = gtag_report_conversion;
    var gtag_report_messenger = gtag_report_conversion;

    var __tagsLoaded=false;
    function loadDeferredTags(){
        if(__tagsLoaded)return; __tagsLoaded=true;
        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-PBZF8G5B');
        var ga=document.createElement('script'); ga.async=true; ga.src='https://www.googletagmanager.com/gtag/js?id=G-6ZP07STZJF'; document.head.appendChild(ga);
        !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
        fbq('init','451786880568879');fbq('track','PageView');
    }
    ['pointerdown','touchstart','mousedown','keydown','scroll'].forEach(function(ev){
        window.addEventListener(ev, loadDeferredTags, {once:true, passive:true});
    });
    window.addEventListener('load', function(){ setTimeout(loadDeferredTags, 6000); });
    </script>

    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="geo.region" content="UA-51">
    <meta name="geo.placename" content="Одеса">
    <meta name="geo.position" content="46.4258;30.7488">
    <meta name="ICBM" content="46.4258, 30.7488">

    <link rel="canonical" href="https://harmonyclinic.od.ua/all-on-4-odessa.html">
    <link rel="alternate" hreflang="uk-UA" href="https://harmonyclinic.od.ua/all-on-4-odessa.html">
    <link rel="alternate" hreflang="ru-UA" href="https://harmonyclinic.od.ua/ru/all-on-4-odessa.html">
    <link rel="alternate" hreflang="x-default" href="https://harmonyclinic.od.ua/all-on-4-odessa.html">

    <title>Імплантація All-on-4 в Одесі — незнімні зуби за протоколом 1 дня | Harmony Clinic</title>
    <meta name="description"
        content="Тотальне відновлення зубів All-on-4 та All-on-6 в Одесі: німецькі імпланти Alpha Dent (350$), незнімний протез на балці (800$). Хірург Олег Швець. ☎ +38 068 779 45 47">

    <meta property="og:locale" content="uk_UA">
    <meta property="og:site_name" content="Harmony Clinic">
    <meta property="og:title" content="Імплантація All-on-4 в Одесі — незнімні зуби за протоколом 1 дня">
    <meta property="og:description" content="Незнімне відновлення зубного ряду за протоколом All-on-4 / All-on-6. Встановлення моста на балці в день операції. Хірург Олег Швець.">
    <meta property="og:url" content="https://harmonyclinic.od.ua/all-on-4-odessa.html">
    <meta property="og:image" content="https://harmonyclinic.od.ua/images/all-on-4-scheme.jpg">
    <meta property="og:type" content="website">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Імплантація All-on-4 в Одесі — Harmony Clinic">
    <meta name="twitter:description" content="Відновлення зубів на 4 або 6 імплантах. Хірург Олег Швець. Навігаційні 3D-шаблони.">
    <meta name="twitter:image" content="https://harmonyclinic.od.ua/images/all-on-4-scheme.jpg">

    <link rel="icon" type="image/png" href="images/Logo.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <link rel="manifest" href="/site.webmanifest">

    <!-- Microdata Schema.org JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Dentist",
          "@id": "https://harmonyclinic.od.ua/#org",
          "name": "Harmony Clinic",
          "url": "https://harmonyclinic.od.ua/all-on-4-odessa.html",
          "image": "https://harmonyclinic.od.ua/images/Logo.png",
          "telephone": "+380687794547",
          "priceRange": "$$$",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "вул. Новаторів, 1А",
            "addressLocality": "Одеса",
            "addressRegion": "Одеська область",
            "postalCode": "65114",
            "addressCountry": "UA"
          },
          "geo": {
            "@type": "GeoCoordinates",
            "latitude": 46.4258,
            "longitude": 30.7488
          },
          "areaServed": [
            { "@type": "City", "name": "Одеса" },
            { "@type": "AdministrativeArea", "name": "Київський район" },
            { "@type": "Place", "name": "Таїрова" },
            { "@type": "Place", "name": "Черемушки" },
            { "@type": "Place", "name": "Сьомий кілометр" }
          ],
          "openingHoursSpecification": [
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
              "opens": "09:00",
              "closes": "20:00"
            },
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": "Saturday",
              "opens": "10:00",
              "closes": "16:00"
            }
          ],
          "sameAs": [
            "https://www.instagram.com/harmony.dental.clinic.od/",
            "https://www.facebook.com/andrei.maliukin/"
          ]
        },
        {
          "@type": "Physician",
          "@id": "https://harmonyclinic.od.ua/#surgeon",
          "name": "Олег Швець",
          "jobTitle": "Хірург-імплантолог",
          "medicalSpecialty": "https://schema.org/Dentistry",
          "image": "https://harmonyclinic.od.ua/images/oleg.jpg",
          "worksFor": { "@id": "https://harmonyclinic.od.ua/#org" }
        },
        {
          "@type": "MedicalProcedure",
          "@id": "https://harmonyclinic.od.ua/all-on-4-odessa.html#procedure",
          "name": "Імплантація зубів All-on-4 та All-on-6",
          "alternateName": [
            "Протезування всі на 4",
            "Відновлення щелепи за 1 день",
            "Тотальна дентальна імплантація All-on-4"
          ],
          "procedureType": "https://schema.org/SurgicalProcedure",
          "bodyLocation": "Верхня та нижня щелепи",
          "howPerformed": "Встановлення 4 або 6 німецьких імплантів Alpha Dent за навігаційним 3D-шаблоном з фіксацією незнімного протеза на балці в день операції під сучасною місцевою анестезією.",
          "preparation": "3D КТ щелепи, цифрове внутрішньоротове сканування 3Shape TRIOS 4, віртуальне моделювання положення імплантів.",
          "followup": "Контрольні огляди на 7, 14 день, через 1, 3 та 6 місяців з можливістю встановлення постійного цирконієвого моста на балці через рік.",
          "performer": [
            { "@id": "https://harmonyclinic.od.ua/#surgeon" },
            { "@id": "https://harmonyclinic.od.ua/#org" }
          ],
          "status": "https://schema.org/ActiveActionStatus"
        },
        {
          "@type": "Service",
          "name": "Імплантація All-on-4 в Одесі під ключ",
          "provider": { "@id": "https://harmonyclinic.od.ua/#org" },
          "areaServed": [
            { "@type": "City", "name": "Одеса" },
            { "@type": "Place", "name": "Таїрова" }
          ],
          "serviceType": "Тотальна імплантація та незнімне протезування",
          "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Вартість імплантації All-on-4 та All-on-6 під ключ",
            "itemListElement": [
              {
                "@type": "Offer",
                "name": "All-on-4 Alpha Dent (Німеччина): 4 імпланти + 4 мульти-юніти + незнімний протез на балці",
                "priceCurrency": "USD",
                "price": "2400",
                "availability": "https://schema.org/InStock"
              },
              {
                "@type": "Offer",
                "name": "All-on-6 Alpha Dent (Німеччина): 6 імплантів + 6 мульти-юнітів + незнімний протез на балці",
                "priceCurrency": "USD",
                "price": "3200",
                "availability": "https://schema.org/InStock"
              },
              {
                "@type": "Offer",
                "name": "Постійний протез: Цирконієві зуби на балці (через 1 рік)",
                "priceCurrency": "USD",
                "price": "3500",
                "availability": "https://schema.org/InStock"
              }
            ]
          }
        },
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "name": "Головна",
              "item": "https://harmonyclinic.od.ua/"
            },
            {
              "@type": "ListItem",
              "position": 2,
              "name": "Послуги",
              "item": "https://harmonyclinic.od.ua/services-ua.html"
            },
            {
              "@type": "ListItem",
              "position": 3,
              "name": "Імплантація зубів",
              "item": "https://harmonyclinic.od.ua/implants-ua.html"
            },
            {
              "@type": "ListItem",
              "position": 4,
              "name": "Імплантація All-on-4 в Одесі",
              "item": "https://harmonyclinic.od.ua/all-on-4-odessa.html"
            }
          ]
        },
        {
          "@type": "FAQPage",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "Скільки коштує імплантація All-on-4 під ключ в Одесі та з чого складається ціна?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "У Harmony Dental Clinic вартість All-on-4 на німецьких імплантах Alpha Dent становить 2 400 $ за щелепу. Розрахунок прозорий: 4 імпланти Alpha Dent (4 × 350 $ = 1 400 $) + 4 мульти-юніт абатменти (4 × 50 $ = 200 $) + акриловий незнімний протез на балці (800 $). У вартість також включено планування, анестезію та контрольні огляди."
              }
            },
            {
              "@type": "Question",
              "name": "Скільки коштує імплантація All-on-6 та коли вона необхідна?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "All-on-6 на імплантах Alpha Dent коштує 3 200 $: 6 імплантів (6 × 350 $ = 2 100 $) + 6 мульти-юнітів (6 × 50 $ = 300 $) + акриловий незнімний протез на балці (800 $). Шість опор рекомендуються на верхній щелепі при м'якшій кістці або при високому жувальному навантаженні."
              }
            },
            {
              "@type": "Question",
              "name": "Скільки коштують постійні цирконієві зуби на балці через рік?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Через 6-12 місяців після повного приживлення імплантів за бажанням пацієнта виготовляється постійний монолітний міст з діоксиду цирконію на індивідуальній фрезерованій балці. Його вартість становить 3 500 $. Це довговічна конструкція з високою естетикою та зносостійкістю."
              }
            },
            {
              "@type": "Question",
              "name": "Як реалізується відновлення зубів за протоколом 1 дня?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Завдяки протоколу негайного навантаження (Immediate Loading) хірург Олег Швець встановлює 4 або 6 імплантів, а ортопед фіксує адаптаційний незнімний протез на балці в день операції. Пацієнт залишає клініку з відновленим зубним рядом."
              }
            },
            {
              "@type": "Question",
              "name": "Чи потрібне нарощування кістки (синус-ліфтинг) при All-on-4?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "У більшості випадків кісткова пластика та синус-ліфтинг не потрібні. Встановлення бічних імплантів під кутом до 45° дозволяє використати наявний об'єм кістки в обхід гайморових пазух і нервів. Точна можливість визначається лікарем за 3D-знімком КТ."
              }
            },
            {
              "@type": "Question",
              "name": "Наскільки комфортно проходить операція All-on-4?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Процедура проходить під якісною сучасною місцевою анестезією, яка надійно знеболює ділянку операції. Гострого болю під час втручання немає, відчувається лише легкий тиск та дотики інструментів. Ми не застосовуємо загальний наркоз (сон), оскільки місцевого знеболення достатньо. Після операції призначаються протизапальні та знеболювальні засоби для комфортного періоду відновлення."
              }
            },
            {
              "@type": "Question",
              "name": "Чим незнімний протез на балці відрізняється від знімного протеза?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Незнімний протез на балці фіксується гвинтами до мульти-юнітів і не зміщується під час жування чи розмови. Він не закриває піднебіння, не впливає на смакові відчуття та рівномірно розподіляє жувальне навантаження на імпланти."
              }
            },
            {
              "@type": "Question",
              "name": "Яка гарантія надається на роботу та імпланти?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "На імпланти діє офіційна гарантія виробника Alpha Dent. Клініка надає гарантію на хірургічний та ортопедичний етапи відповідно до медичних стандартів за умови дотримання рекомендацій лікаря та регулярної гігієни 2 рази на рік."
              }
            }
          ]
        }
      ]
    }
    </script>

    <style>
        /* Scoped styles for All-on-4 landing */
        .all-hero {
            position: relative;
            padding: 75px 0 65px;
            min-height: 68vh;
            display: flex;
            align-items: center;
            background: radial-gradient(circle at top right, rgba(82, 97, 84, 0.45) 0%, transparent 65%),
                        linear-gradient(135deg, #0c1210 0%, #030604 100%);
            color: #fff;
            overflow: hidden;
        }

        .all-hero .hero-grid {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 40px;
            align-items: center;
        }

        .all-hero h1 {
            font-size: clamp(30px, 4vw, 48px);
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -0.5px;
            margin-bottom: 20px;
        }

        .all-hero .hero-lead {
            font-size: 17px;
            color: rgba(255, 255, 255, 0.85);
            line-height: 1.6;
            margin-bottom: 30px;
        }

        .hero-usps {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-bottom: 35px;
        }

        .usp-pill {
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 12px 18px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
            backdrop-filter: blur(8px);
            font-size: 14px;
            font-weight: 600;
        }

        .usp-pill svg {
            width: 24px;
            height: 24px;
            fill: #c49b66;
            flex-shrink: 0;
        }

        .hero-cta-btns {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }

        .hero-card-preview {
            position: relative;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            background: #111a13;
        }

        .hero-card-preview img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
        }

        .hero-card-badge {
            position: absolute;
            bottom: 16px;
            left: 16px;
            right: 16px;
            background: rgba(12, 18, 14, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 14px 18px;
            border-radius: 12px;
            font-size: 13px;
            line-height: 1.4;
        }

        .hero-card-badge strong {
            color: #c49b66;
            display: block;
            font-size: 15px;
            margin-bottom: 2px;
        }

        /* Content Sections */
        .section-py {
            padding: 80px 0;
        }

        .bg-light-alt {
            background-color: #f8faf8;
        }

        .section-header-center {
            text-align: center;
            max-width: 820px;
            margin: 0 auto 45px;
        }

        .section-header-center h2 {
            font-size: clamp(26px, 3.2vw, 36px);
            font-weight: 800;
            color: #191f1a;
            letter-spacing: -0.5px;
            margin-bottom: 16px;
            line-height: 1.2;
        }

        .section-header-center p {
            font-size: 16px;
            color: #556057;
            line-height: 1.6;
        }

        .eyebrow-tag {
            display: inline-block;
            background: rgba(82, 97, 84, 0.12);
            color: var(--primary);
            font-size: 13px;
            font-weight: 800;
            padding: 6px 14px;
            border-radius: 100px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 14px;
        }

        /* 2-Col Explainer */
        .explainer-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 48px;
            align-items: center;
        }

        .explainer-text h3 {
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 18px;
            color: #191f1a;
        }

        .explainer-text p {
            font-size: 16px;
            line-height: 1.7;
            color: #4a544c;
            margin-bottom: 20px;
        }

        .explainer-list {
            list-style: none;
            padding: 0;
            margin: 24px 0;
        }

        .explainer-list li {
            position: relative;
            padding-left: 32px;
            margin-bottom: 14px;
            font-size: 15px;
            color: #2b352d;
            line-height: 1.5;
        }

        .explainer-list li::before {
            content: "✓";
            position: absolute;
            left: 0;
            top: 0;
            width: 22px;
            height: 22px;
            background: var(--primary);
            color: #fff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 800;
        }

        .explainer-media {
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08);
            border: 1px solid #e3e8e3;
        }

        .explainer-media img {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Candidates Cards */
        .candidates-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 22px;
        }

        .candidate-card {
            background: #fff;
            border-radius: 18px;
            padding: 30px 24px;
            border: 1px solid #e5ebe5;
            box-shadow: 0 6px 24px rgba(0, 0, 0, 0.04);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
        }

        .candidate-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 16px 36px rgba(82, 97, 84, 0.12);
            border-color: var(--primary-light);
        }

        .candidate-icon {
            width: 52px;
            height: 52px;
            background: rgba(82, 97, 84, 0.1);
            color: var(--primary);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-bottom: 20px;
        }

        .candidate-card h3 {
            font-size: 19px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 12px;
        }

        .candidate-card p {
            font-size: 14px;
            color: #5d695f;
            line-height: 1.6;
        }

        /* Comparison Table */
        .table-responsive {
            overflow-x: auto;
            background: #fff;
            border-radius: 20px;
            border: 1px solid #e3e8e3;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }

        .custom-comp-table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 15px;
            min-width: 680px;
        }

        .custom-comp-table th {
            background: #253328;
            color: #fff;
            padding: 20px 22px;
            font-weight: 700;
            font-size: 16px;
        }

        .custom-comp-table th.highlight-col {
            background: var(--primary);
            color: #fff;
        }

        .custom-comp-table td {
            padding: 18px 22px;
            border-bottom: 1px solid #edf2ed;
            color: #374239;
            line-height: 1.5;
        }

        .custom-comp-table tr:last-child td {
            border-bottom: none;
        }

        .custom-comp-table td.highlight-col {
            background: rgba(82, 97, 84, 0.06);
            font-weight: 600;
            color: #1a221c;
        }

        .badge-pro {
            display: inline-block;
            background: #2e7d32;
            color: #fff;
            font-size: 12px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            margin-right: 6px;
        }

        .badge-con {
            display: inline-block;
            background: #c62828;
            color: #fff;
            font-size: 12px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            margin-right: 6px;
        }

        /* =======================================================
           COMPACT INTERACTIVE PRICING TABS SECTION
        ======================================================= */
        .pricing-tabs-container {
            max-width: 980px;
            margin: 0 auto;
        }

        .pricing-nav-tabs {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 28px;
            flex-wrap: wrap;
        }

        .pricing-tab-btn {
            padding: 14px 26px;
            background: #fff;
            border: 2px solid #e1e7e1;
            border-radius: 14px;
            font-weight: 700;
            font-size: 15px;
            color: #4b584d;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .pricing-tab-btn:hover {
            border-color: var(--primary-light);
            background: #fdfdfd;
        }

        .pricing-tab-btn.active {
            background: #fff;
            border-color: var(--primary);
            color: var(--primary);
            box-shadow: 0 8px 24px rgba(82, 97, 84, 0.16);
            transform: translateY(-2px);
        }

        .pricing-tab-btn.gold-active.active {
            border-color: #c49b66;
            color: #8c6732;
        }

        .pricing-content-panel {
            background: #fff;
            border: 1px solid #e1e8e1;
            border-radius: 24px;
            padding: 42px 45px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.05);
            display: none;
            animation: fadeInTab 0.3s ease;
        }

        .pricing-content-panel.active {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 40px;
            align-items: center;
        }

        @keyframes fadeInTab {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .tab-panel-left {
            border-right: 1px solid #edf2ed;
            padding-right: 35px;
        }

        .tab-tag-badge {
            display: inline-block;
            background: #eef4ee;
            color: var(--primary);
            font-size: 12px;
            font-weight: 800;
            padding: 5px 12px;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            margin-bottom: 12px;
        }

        .tab-panel-left h3 {
            font-size: 26px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 8px;
        }

        .tab-price-big {
            font-size: 44px;
            font-weight: 800;
            color: var(--primary);
            line-height: 1;
            margin: 14px 0 6px;
        }

        .tab-price-sub {
            font-size: 13.5px;
            color: #707d72;
            margin-bottom: 20px;
        }

        .tab-formula-box {
            background: #f4f7f4;
            border: 1px dashed #cad4cb;
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 24px;
            font-size: 13.5px;
            color: #38453a;
            line-height: 1.55;
        }

        .tab-formula-box strong {
            color: #191f1a;
        }

        .tab-panel-right h4 {
            font-size: 16px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 16px;
        }

        .tab-panel-right ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .tab-panel-right li {
            position: relative;
            padding-left: 26px;
            margin-bottom: 12px;
            font-size: 14px;
            color: #3f4d41;
            line-height: 1.45;
        }

        .tab-panel-right li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--primary);
            font-weight: 800;
            font-size: 15px;
        }

        /* Timeline Steps */
        .timeline-container {
            position: relative;
            max-width: 900px;
            margin: 0 auto;
        }

        .timeline-step {
            display: grid;
            grid-template-columns: 80px 1fr;
            gap: 26px;
            margin-bottom: 36px;
            position: relative;
        }

        .timeline-step:not(:last-child)::after {
            content: "";
            position: absolute;
            left: 39px;
            top: 75px;
            bottom: -25px;
            width: 2px;
            background: #d8e0d9;
        }

        .step-num-badge {
            width: 78px;
            height: 78px;
            background: #fff;
            border: 2px solid var(--primary);
            color: var(--primary);
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: 800;
            box-shadow: 0 6px 18px rgba(82, 97, 84, 0.15);
            z-index: 2;
        }

        .step-num-badge span {
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .step-card {
            background: #fff;
            border-radius: 18px;
            padding: 26px 30px;
            border: 1px solid #e3e8e3;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.04);
        }

        .step-card h3 {
            font-size: 20px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 10px;
        }

        .step-card p {
            font-size: 15px;
            color: #556257;
            line-height: 1.6;
            margin: 0;
        }

        /* Doctor Highlight (E-E-A-T) */
        .doctor-highlight-box {
            background: #fff;
            border-radius: 24px;
            border: 1px solid #e1e7e1;
            padding: 45px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.05);
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 45px;
            align-items: center;
        }

        .doc-photo-wrap {
            border-radius: 18px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }

        .doc-photo-wrap img {
            width: 100%;
            height: auto;
            display: block;
        }

        .doc-info-content h3 {
            font-size: 28px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 6px;
        }

        .doc-title-role {
            font-size: 16px;
            color: var(--primary);
            font-weight: 700;
            margin-bottom: 20px;
        }

        .doc-desc {
            font-size: 15px;
            color: #4b564d;
            line-height: 1.7;
            margin-bottom: 24px;
        }

        .doc-stats-row {
            display: flex;
            gap: 30px;
            margin-bottom: 28px;
            padding: 20px 0;
            border-top: 1px solid #edf2ed;
            border-bottom: 1px solid #edf2ed;
        }

        .doc-stat-item strong {
            display: block;
            font-size: 22px;
            color: #191f1a;
            font-weight: 800;
        }

        .doc-stat-item span {
            font-size: 13px;
            color: #728074;
        }

        /* Cases Grid */
        .cases-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
        }

        .case-card {
            background: #fff;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid #e3e8e3;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
        }

        .case-imgs-split {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2px;
            background: #ddd;
            position: relative;
        }

        .case-img-wrap {
            position: relative;
        }

        .case-img-wrap img {
            width: 100%;
            height: auto;
            display: block;
            aspect-ratio: 4/3;
            object-fit: cover;
        }

        .case-badge {
            position: absolute;
            bottom: 8px;
            left: 8px;
            background: rgba(0, 0, 0, 0.7);
            color: #fff;
            font-size: 11px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            text-transform: uppercase;
        }

        .case-body {
            padding: 24px;
        }

        .case-body h3 {
            font-size: 18px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 8px;
        }

        .case-body p {
            font-size: 14px;
            color: #556257;
            line-height: 1.6;
            margin: 0;
        }

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {
            .all-hero .hero-grid { grid-template-columns: 1fr; }
            .candidates-grid { grid-template-columns: repeat(2, 1fr); }
            .pricing-content-panel.active { grid-template-columns: 1fr; gap: 30px; }
            .tab-panel-left { border-right: none; border-bottom: 1px solid #edf2ed; padding-right: 0; padding-bottom: 25px; }
            .doctor-highlight-box { grid-template-columns: 1fr; gap: 30px; }
            .doc-photo-wrap { max-width: 320px; margin: 0 auto; }
            .explainer-grid { grid-template-columns: 1fr; }
        }

        @media (max-width: 768px) {
            .all-hero { padding: 50px 0 45px; }
            .all-hero h1 { font-size: 28px; }
            .hero-usps { grid-template-columns: 1fr; }
            .candidates-grid { grid-template-columns: 1fr; }
            .pricing-content-panel { padding: 28px 20px; }
            .tab-price-big { font-size: 36px; }
            .pricing-nav-tabs { flex-direction: column; }
            .pricing-tab-btn { justify-content: center; }
            .cases-grid { grid-template-columns: 1fr; }
            .timeline-step { grid-template-columns: 60px 1fr; gap: 16px; }
            .step-num-badge { width: 58px; height: 58px; font-size: 16px; }
            .timeline-step:not(:last-child)::after { left: 29px; }
            .doc-stats-row { flex-direction: column; gap: 14px; }
            .section-py { padding: 55px 0; }
        }
    </style>
</head>

<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PBZF8G5B"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

    <header role="banner">
        <div class="container nav-wrapper">
            <a href="index.html" class="logo">
                <picture>
                    <source srcset="images/Logo.webp" type="image/webp">
                    <img loading="lazy" src="images/Logo.png" alt="Harmony Dental Clinic" width="1072" height="1071">
                </picture>
            </a>
            <nav role="navigation">
                <ul class="nav-menu" id="navMenu">
                    <li><a href="index.html">Головна</a></li>
                    <li><a href="services-ua.html">Послуги</a></li>
                    <li><a href="implants-ua.html">Імплантація</a></li>
                    <li><a href="all-on-4-odessa.html" style="color:var(--primary);font-weight:800;">All-on-4</a></li>
                    <li><a href="index.html#team">Лікарі</a></li>
                    <li><a href="index.html#prices">Ціни</a></li>
                    <li><a href="blog.html">Блог</a></li>
                    <li><a href="#contacts">Контакти</a></li>
                </ul>
            </nav>
            <div style="display: flex; align-items: center; gap: 15px;">
                <div class="lang-switch">
                    <a href="all-on-4-odessa.html" class="active">UA</a>
                    <a href="ru/all-on-4-odessa.html">RU</a>
                </div>
                <a href="tel:+380687794547" aria-label="Зателефонувати" class="header-phone"
                    onclick="return gtag_report_call('tel:+380687794547');">+38 068 779 45 47</a>
                <div class="mobile-toggle" onclick="toggleMenu()">☰</div>
            </div>
        </div>
    </header>

    <!-- Breadcrumbs Section -->
    <div style="background:#f4f7f4; padding: 14px 0; border-bottom: 1px solid #e3e8e3;">
        <div class="container">
            <nav aria-label="Хлібні крихти" style="font-size: 13px; color: #667368;">
                <a href="index.html" style="color: inherit; text-decoration: none;">Головна</a>
                <span style="margin: 0 8px;">/</span>
                <a href="services-ua.html" style="color: inherit; text-decoration: none;">Послуги</a>
                <span style="margin: 0 8px;">/</span>
                <a href="implants-ua.html" style="color: inherit; text-decoration: none;">Імплантація зубів</a>
                <span style="margin: 0 8px;">/</span>
                <span style="color: var(--primary); font-weight: 700;">All-on-4 в Одесі</span>
            </nav>
        </div>
    </div>

    <!-- Section 1: Hero -->
    <section class="all-hero">
        <div class="container">
            <div class="hero-grid">
                <div>
                    <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); padding:7px 16px; border-radius:100px; font-size:13px; font-weight:600; margin-bottom:20px; backdrop-filter:blur(5px);">
                        <span style="width:8px; height:8px; background:#4ade80; border-radius:50%; display:inline-block;"></span>
                        Працюємо автономно: є генератор та резервне живлення
                    </div>

                    <h1>Імплантація All-on-4 та All-on-6 в Одесі — незнімні зуби за 1 день</h1>
                    
                    <p class="hero-lead">
                        Повне відновлення зубного ряду щелепи на німецьких імплантах Alpha Dent з фіксацією незнімного протеза на балці в день операції. Прозорий розрахунок вартості за фіксованим планом лікування.
                    </p>

                    <div class="hero-usps">
                        <div class="usp-pill">
                            <svg viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
                            <span>Хірург-імплантолог <strong>Олег Швець</strong></span>
                        </div>
                        <div class="usp-pill">
                            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                            <span>3D навігаційні шаблони</span>
                        </div>
                        <div class="usp-pill">
                            <svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
                            <span>Незнімний протез на балці за 1 день</span>
                        </div>
                        <div class="usp-pill">
                            <svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
                            <span>Гарантія виробника на імпланти</span>
                        </div>
                    </div>

                    <div class="hero-cta-btns">
                        <a href="#prices" class="btn" style="background:var(--primary); color:#fff; border:none; padding:15px 30px; font-weight:800; font-size:16px; border-radius:12px; text-decoration:none; display:inline-flex; align-items:center; gap:10px; box-shadow:0 10px 25px rgba(82,97,84,0.4);">
                            Розрахувати вартість під ключ
                        </a>
                        <a href="tel:+380687794547" class="btn" style="background:rgba(255,255,255,0.12); color:#fff; border:1px solid rgba(255,255,255,0.25); padding:15px 26px; font-weight:700; font-size:15px; border-radius:12px; text-decoration:none; display:inline-flex; align-items:center; gap:8px;"
                           onclick="return gtag_report_call('tel:+380687794547');">
                            📞 Зателефонувати
                        </a>
                    </div>
                </div>

                <div>
                    <div class="hero-card-preview">
                        <picture>
                            <img src="images/all-on-4-scheme.jpg" alt="Схема імплантації All-on-4 в Одесі: кутове встановлення 4 імплантів та незнімний міст" width="1376" height="768">
                        </picture>
                        <div class="hero-card-badge">
                            <strong>Концепція All-on-4 / All-on-6</strong>
                            Незнімна конструкція спирається на 4 або 6 імплантів через жорстку балку без потреби у вставних протезах.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: What is All-on-4 and How it Works -->
    <section class="section-py">
        <div class="container">
            <div class="explainer-grid">
                <div class="explainer-media">
                    <picture>
                        <img src="images/all-on-4-scheme.jpg" alt="3D анатомічна схема тотальної імплантації щелепи All-on-4" width="1376" height="768" loading="lazy">
                    </picture>
                </div>

                <div class="explainer-text">
                    <span class="eyebrow-tag">Суть методики</span>
                    <h2>Що таке технологія All-on-4 («Всі на чотирьох») та All-on-6?</h2>
                    <p>
                        <strong>All-on-4</strong> — це міжнародний протокол реабілітації зубного ряду, розроблений для пацієнтів з повною відсутністю зубів (адентією) або у випадках, коли наявні зуби не підлягають збереженню.
                    </p>
                    <p>
                        Замість встановлення імпланта під кожен окремий зуб хірург встановлює <strong>4 або 6 титанових імплантів Alpha Dent</strong> за спеціальною просторовою схемою:
                    </p>
                    <ul class="explainer-list">
                        <li><strong>Два центральних імпланти</strong> розташовуються вертикально у фронтальній ділянці, де об'єм кістки зазвичай зберігається найкраще.</li>
                        <li><strong>Два бічних (дистальних) імпланти</strong> встановлюються під кутом до 45°. Це дозволяє задіяти щільні ділянки кістки та в більшості клінічних випадків <strong>уникнути складного нарощування кістки або синус-ліфтингу</strong>.</li>
                        <li><strong>Мульти-юніт абатменти (Multi-unit):</strong> спеціальні перехідники по 50 $, які вирівнюють кут нахилу та забезпечують надійну гвинтову фіксацію незнімного протеза на балці.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 3: Candidates & Indications (Problem -> Solution) -->
    <section class="section-py bg-light-alt">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Показання</span>
                <h2>Кому підходить протокол імплантації All-on-4?</h2>
                <p>
                    Методика дозволяє відновити жувальну функцію та естетику посмішки при складних клінічних станах щелепи.
                </p>
            </div>

            <div class="candidates-grid">
                <div class="candidate-card">
                    <div class="candidate-icon">🦷</div>
                    <h3>Повна відсутність зубів</h3>
                    <p>
                        Повна адентія на верхній або нижній щелепі. Повертаємо можливість нормально харчуватися та впевнено посміхатися.
                    </p>
                </div>

                <div class="candidate-card">
                    <div class="candidate-icon">⚠️</div>
                    <h3>Рухомі та зруйновані зуби</h3>
                    <p>
                        Важкі форми пародонтиту чи генералізоване руйнування зубів. Видалення залишків зубів та встановлення імплантів проводяться за один візит.
                    </p>
                </div>

                <div class="candidate-card">
                    <div class="candidate-icon">🚫</div>
                    <h3>Дискомфорт від знімних протезів</h3>
                    <p>
                        Коли знімні протези натирають ясна, зміщуються під час розмови чи їжі та перекривають піднебіння, викликаючи блювотний рефлекс.
                    </p>
                </div>

                <div class="candidate-card">
                    <div class="candidate-icon">📉</div>
                    <h3>Дефіцит кісткової тканини</h3>
                    <p>
                        Кутове розташування бічних імплантів дозволяє надійно зафіксувати опори навіть при зменшеній висоті кісткового гребеня.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 4: Detailed Comparison Table -->
    <section class="section-py">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Об'єктивне порівняння</span>
                <h2>All-on-4 / All-on-6 vs Знімний протез vs Класична імплантація</h2>
                <p>
                    Порівняння клінічних характеристик різних методів відновлення зубного ряду.
                </p>
            </div>

            <div class="table-responsive">
                <table class="custom-comp-table">
                    <thead>
                        <tr>
                            <th>Критерій оцінки</th>
                            <th class="highlight-col">All-on-4 / All-on-6 на балці</th>
                            <th>Звичайний знімний протез</th>
                            <th>Класична імплантація (8-10 імплантів)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Термін фіксації протеза</strong></td>
                            <td class="highlight-col"><span class="badge-pro">1 день</span> Адаптаційний протез фіксується в день операції</td>
                            <td>2–4 тижні (після виготовлення в лабораторії)</td>
                            <td>4–8 місяців (після повного приживлення)</td>
                        </tr>
                        <tr>
                            <td><strong>Тип фіксації</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Стабільна</span> Гвинтова фіксація до балки та мульти-юнітів</td>
                            <td><span class="badge-con">Рухома</span> Тримається за рахунок прилягання чи кламерів</td>
                            <td><span class="badge-pro">Стабільна</span> Окремі коронки або мостоподібні протези</td>
                        </tr>
                        <tr>
                            <td><strong>Жувальний комфорт</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Високий</span> Наближений до природних відчуттів</td>
                            <td><span class="badge-con">Обмежений</span> Складно пережовувати тверду їжу</td>
                            <td><span class="badge-pro">Високий</span> Повне жувальне навантаження</td>
                        </tr>
                        <tr>
                            <td><strong>Перекриття піднебіння</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Ні</span> Піднебіння відкрите, смакові рецептори та мова вільні</td>
                            <td><span class="badge-con">Так</span> Пластиковий базис повністю закриває піднебіння</td>
                            <td><span class="badge-pro">Ні</span> Тільки зуби та ясенний край</td>
                        </tr>
                        <tr>
                            <td><strong>Потреба в синус-ліфтингу</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Зведена до мінімуму</span> Завдяки кутовим імплантам</td>
                            <td>Не потрібна</td>
                            <td><span class="badge-con">Часто необхідна</span> Обов'язкова кісткова пластика при дефіциті</td>
                        </tr>
                        <tr>
                            <td><strong>Навантаження на кістку</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Рівномірне</span> Балка розподіляє тиск між імплантами</td>
                            <td><span class="badge-con">Нерівномірне</span> Тиск на ясна може прискорювати атрофію</td>
                            <td><span class="badge-pro">Фізіологічне</span> Навантаження через окремі імпланти</td>
                        </tr>
                        <tr>
                            <td><strong>Вартість лікування</strong></td>
                            <td class="highlight-col"><strong>Фіксована за протоколом:</strong> 2 400 $ (4 оп.) / 3 200 $ (6 оп.)</td>
                            <td>Доступна спочатку, але потребує регулярних перебазувань</td>
                            <td>Висока (окремо за кожну одиницю + пластика кістки)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- Section 5: Sleek Interactive Tabs Pricing Section -->
    <section class="section-py bg-light-alt" id="prices">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Прозорий прайс</span>
                <h2>Вартість імплантації All-on-4 та All-on-6 в Одесі</h2>
                <p>
                    Оберіть відповідний варіант лікування. Чесний розрахунок на базі системи Alpha Dent (Німеччина).
                </p>
            </div>

            <div class="pricing-tabs-container">
                <!-- Segmented Tabs Navigation -->
                <div class="pricing-nav-tabs">
                    <button class="pricing-tab-btn active" onclick="switchPricingTab('all4', this)">
                        <span>🌟</span> All-on-4 Alpha Dent (2 400 $)
                    </button>
                    <button class="pricing-tab-btn" onclick="switchPricingTab('all6', this)">
                        <span>💪</span> All-on-6 Alpha Dent (3 200 $)
                    </button>
                    <button class="pricing-tab-btn gold-active" onclick="switchPricingTab('zirconia', this)">
                        <span>👑</span> Цирконій на балці (3 500 $)
                    </button>
                </div>

                <!-- Tab 1: All-on-4 Alpha Dent -->
                <div id="tab-panel-all4" class="pricing-content-panel active">
                    <div class="tab-panel-left">
                        <span class="tab-tag-badge">Базовий протокол • Німеччина</span>
                        <h3>All-on-4 Alpha Dent</h3>
                        <div class="tab-price-big">2 400 $</div>
                        <div class="tab-price-sub">за повне відновлення однієї щелепи (зуби за 1 день)</div>

                        <div class="tab-formula-box">
                            <strong>Прозорий покроковий розрахунок:</strong><br>
                            • 4 імпланти Alpha Dent (4 × 350 $) = <strong>1 400 $</strong><br>
                            • 4 мульти-юніт абатменти (4 × 50 $) = <strong>200 $</strong><br>
                            • Акриловий незнімний протез на балці = <strong>800 $</strong>
                        </div>

                        <a href="#consultation" class="btn" style="background:var(--primary); color:#fff; padding:14px 28px; border-radius:12px; font-weight:800; text-decoration:none; display:inline-block; box-shadow:0 8px 20px rgba(82,97,84,0.3);">
                            Записатися на All-on-4 (2 400 $)
                        </a>
                    </div>

                    <div class="tab-panel-right">
                        <h4>Що входить у вартість лікування:</h4>
                        <ul>
                            <li>3D комп'ютерне планування операції</li>
                            <li>Виготовлення індивідуального 3D-шаблону</li>
                            <li>4 титанових імпланти Alpha Dent (Німеччина)</li>
                            <li>4 оригінальних мульти-юніти (кутові абатменти)</li>
                            <li>Незнімний протез на балці в день операції</li>
                            <li>Місцева анестезія, накладання швів та контрольні огляди</li>
                        </ul>
                    </div>
                </div>

                <!-- Tab 2: All-on-6 Alpha Dent -->
                <div id="tab-panel-all6" class="pricing-content-panel">
                    <div class="tab-panel-left">
                        <span class="tab-tag-badge" style="background:#e5eee6; color:#2d3a2f;">Підвищена опора</span>
                        <h3>All-on-6 Alpha Dent</h3>
                        <div class="tab-price-big">3 200 $</div>
                        <div class="tab-price-sub">за повне відновлення щелепи на 6 опорах</div>

                        <div class="tab-formula-box">
                            <strong>Прозорий покроковий розрахунок:</strong><br>
                            • 6 імплантів Alpha Dent (6 × 350 $) = <strong>2 100 $</strong><br>
                            • 6 мульти-юніт абатментів (6 × 50 $) = <strong>300 $</strong><br>
                            • Акриловий незнімний протез на балці = <strong>800 $</strong>
                        </div>

                        <a href="#consultation" class="btn" style="background:var(--primary); color:#fff; padding:14px 28px; border-radius:12px; font-weight:800; text-decoration:none; display:inline-block; box-shadow:0 8px 20px rgba(82,97,84,0.3);">
                            Записатися на All-on-6 (3 200 $)
                        </a>
                    </div>

                    <div class="tab-panel-right">
                        <h4>Особливості протоколу на 6 імплантах:</h4>
                        <ul>
                            <li>Все з базового протоколу +</li>
                            <li><strong>6 імплантів</strong> для ширшого розподілу жувального навантаження</li>
                            <li>Рекомендовано для верхньої щелепи або широкого зубного ряду</li>
                            <li>6 оригінальних мульти-юніт абатментів</li>
                            <li>Незнімний адаптаційний міст на балці в день операції</li>
                            <li>Додаткова механічна підтримка конструкції</li>
                        </ul>
                    </div>
                </div>

                <!-- Tab 3: Zirconia on Bar -->
                <div id="tab-panel-zirconia" class="pricing-content-panel">
                    <div class="tab-panel-left">
                        <span class="tab-tag-badge" style="background:#fcf5ea; color:#966f38;">Постійний етап через 6–12 міс</span>
                        <h3>Цирконієві зуби на балці</h3>
                        <div class="tab-price-big" style="color:#966f38;">3 500 $</div>
                        <div class="tab-price-sub">за постійний незнімний міст на фрезерованій балці</div>

                        <div class="tab-formula-box" style="background:#fbf8f3; border-color:#e8dcce;">
                            <strong>Довговічне постійне протезування:</strong><br>
                            Виготовляється після повної остеоінтеграції імплантів з кісткою на заміну первинному протезу.
                        </div>

                        <a href="#consultation" class="btn" style="background:#966f38; color:#fff; padding:14px 28px; border-radius:12px; font-weight:800; text-decoration:none; display:inline-block; box-shadow:0 8px 20px rgba(150,111,56,0.3);">
                            Дізнатися про Цирконій (3 500 $)
                        </a>
                    </div>

                    <div class="tab-panel-right">
                        <h4>Характеристики монолітного цирконію:</h4>
                        <ul>
                            <li>Індивідуальна фрезерована балка CAD/CAM</li>
                            <li>Високоміцний діоксид цирконію</li>
                            <li>Природний зовнішній вигляд та прозорість емалі</li>
                            <li>Висока стійкість до стирання та навантажень</li>
                            <li>Матеріал не вбирає барвники та зберігає початковий колір</li>
                            <li>Тривалий термін служби при правильному догляді</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 6: Step-by-Step Timeline (Immediate Loading) -->
    <section class="section-py">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Покроковий план</span>
                <h2>Як проходить лікування за протоколом All-on-4</h2>
                <p>
                    Послідовні етапи від первинного обстеження до фіксації постійної конструкції.
                </p>
            </div>

            <div class="timeline-container">
                <!-- Step 1 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        01
                        <span>Етап 1</span>
                    </div>
                    <div class="step-card">
                        <h3>3D-діагностика та цифрове сканування 3Shape</h3>
                        <p>
                            Проводимо комп'ютерну томографію (КТ) для оцінки кісткової тканини та анатомічних структур. Скануємо порожнину рота цифровим сканером 3Shape TRIOS 4. У програмі моделюємо точне положення кожного імпланта.
                        </p>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        02
                        <span>Шаблон</span>
                    </div>
                    <div class="step-card">
                        <h3>Друк хірургічного навігаційного шаблону</h3>
                        <p>
                            За індивідуальною цифровою моделлю на 3D-принтері друкується хірургічний шаблон з направляючими втулками, який забезпечує позиціонування імплантів за заздалегідь розрахованою траєкторією.
                        </p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        03
                        <span>Операція</span>
                    </div>
                    <div class="step-card">
                        <h3>День операції: встановлення імплантів Alpha Dent</h3>
                        <p>
                            Під ефективною місцевою анестезією хірург Олег Швець атравматично видаляє залишки зубів та встановлює 4 або 6 імплантів через шаблон. Процедура проходить комфортно, без гострого болю; пацієнт відчуває лише тиск та дотики інструментів.
                        </p>
                    </div>
                </div>

                <!-- Step 4 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        04
                        <span>У той же день</span>
                    </div>
                    <div class="step-card">
                        <h3>Фіксація незнімного протеза на балці</h3>
                        <p>
                            Лікар-ортопед встановлює мульти-юніти та фіксує незнімний адаптаційний протез на балці. Пацієнт повертається додому з відновленим зубним рядом і можливістю вживати м'яку їжу.
                        </p>
                    </div>
                </div>

                <!-- Step 5 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        05
                        <span>Через 6-12 міс</span>
                    </div>
                    <div class="step-card">
                        <h3>Постійне протезування: Цирконієві зуби на балці (3 500 $)</h3>
                        <p>
                            Після повного зрощення імплантів з кісткою за бажанням пацієнта виготовляється постійний монолітний міст з оксиду цирконію на індивідуальній фрезерованій балці — надійна та естетична конструкція для довготривалого використання.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 7: Surgeon & Team (E-E-A-T) -->
    <section class="section-py bg-light-alt" id="surgeon">
        <div class="container">
            <div class="doctor-highlight-box">
                <div class="doc-photo-wrap">
                    <picture>
                        <source srcset="images/oleg.webp" type="image/webp">
                        <img src="images/oleg.jpg" alt="Хірург-імплантолог Олег Швець — операції All-on-4 в Одесі" width="725" height="1024" loading="lazy">
                    </picture>
                </div>

                <div class="doc-info-content">
                    <span class="eyebrow-tag">Хірург-імплантолог</span>
                    <h3>Олег Швець</h3>
                    <div class="doc-title-role">Провідний хірург-імплантолог Harmony Dental Clinic</div>
                    
                    <p class="doc-desc">
                        Спеціалізується на тотальній реабілітації зубного ряду, навігаційній хірургії та роботі за клінічними протоколами All-on-4 / All-on-6. Виконує атравматичне встановлення імплантів з дбайливим ставленням до м'яких і кісткових тканин для прогнозованого загоєння.
                    </p>

                    <div class="doc-stats-row">
                        <div class="doc-stat-item">
                            <strong>10+ років</strong>
                            <span>Хірургічної практики</span>
                        </div>
                        <div class="doc-stat-item">
                            <strong>3D навігація</strong>
                            <span>Цифрове планування</span>
                        </div>
                        <div class="doc-stat-item">
                            <strong>Міжнародні</strong>
                            <span>Клінічні протоколи</span>
                        </div>
                    </div>

                    <div style="display:flex; align-items:center; gap:16px;">
                        <picture>
                            <source srcset="images/andrey.webp" type="image/webp">
                            <img src="images/andrey.jpg" alt="Головний лікар Андрій Малюкін" style="width:60px; height:60px; border-radius:50%; object-fit:cover; border:2px solid var(--primary);" width="725" height="1024" loading="lazy">
                        </picture>
                        <div style="font-size:14px; color:#445046;">
                            <strong>У тандемі з головним лікарем Андрієм Малюкіним</strong><br>
                            Ортопедичне моделювання прикусу та точна посадка незнімної конструкції.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 8: Technology & Comfort -->
    <section class="section-py">
        <div class="container">
            <div class="explainer-grid">
                <div>
                    <span class="eyebrow-tag">Цифрові стандарти</span>
                    <h2>Навігаційна 3D-хірургія та комфортне лікування в Одесі</h2>
                    <p>
                        У Harmony Dental Clinic імплантація All-on-4 планується цифровим методом за допомогою 3D-шаблонів, що мінімізує хірургічну травму та скорочує час операції.
                    </p>
                    <ul class="explainer-list">
                        <li><strong>Точність позиціонування:</strong> шаблон спрямовує імплант строго на задану глибину та під розрахованим кутом через напрямні втулки.</li>
                        <li><strong>Ефективна місцева анестезія:</strong> ми використовуємо перевірені європейські анестетики, які надійно знеболюють операційне поле. Ми не застосовуємо загальний наркоз (сон) — процедура проходить у спокійній обстановці зі збереженням повної свідомості та контролю.</li>
                        <li><strong>Автономність:</strong> клініка на вул. Новаторів 1А обладнана генератором та резервним живленням для безперервної роботи медичного обладнання.</li>
                    </ul>
                </div>

                <div class="explainer-media">
                    <picture>
                        <img src="images/surgical-template.jpg" alt="3D хірургічний навігаційний шаблон для точного позиціонування імплантів All-on-4" width="1376" height="768" loading="lazy">
                    </picture>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 9: Clinical Cases Before / After -->
    <section class="section-py bg-light-alt">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Клінічні приклади</span>
                <h2>Результати тотальної імплантації щелепи До та Після</h2>
                <p>
                    Приклади відновлення зубного ряду пацієнтів у Harmony Dental Clinic.
                </p>
            </div>

            <div class="cases-grid">
                <!-- Case 1 -->
                <div class="case-card">
                    <div class="case-imgs-split">
                        <div class="case-img-wrap">
                            <picture>
                                <source srcset="images_implants/c1a.webp" type="image/webp">
                                <img src="images_implants/c1a.jpg" alt="До імплантації: відсутність зубів та зруйнований ряд" loading="lazy" width="725" height="483">
                            </picture>
                            <span class="case-badge">До</span>
                        </div>
                        <div class="case-img-wrap">
                            <picture>
                                <source srcset="images_implants/c1b.webp" type="image/webp">
                                <img src="images_implants/c1b.jpg" alt="Після імплантації All-on-4: незнімний міст та рівні зуби" loading="lazy" width="725" height="483">
                            </picture>
                            <span class="case-badge" style="background:var(--primary);">Після</span>
                        </div>
                    </div>
                    <div class="case-body">
                        <h3>Тотальна реабілітація верхньої щелепи All-on-4</h3>
                        <p>Пацієнт 56 років. Скарги на неможливість користуватися знімним протезом. Встановлено 4 імпланти Alpha Dent за навігаційним шаблоном з фіксацією незнімного протеза на балці в день операції.</p>
                    </div>
                </div>

                <!-- Case 2 -->
                <div class="case-card">
                    <div class="case-imgs-split">
                        <div class="case-img-wrap">
                            <picture>
                                <source srcset="images_implants/c2a.webp" type="image/webp">
                                <img src="images_implants/c2a.jpg" alt="До лікування: рухомість зубів та пародонтит" loading="lazy" width="725" height="483">
                            </picture>
                            <span class="case-badge">До</span>
                        </div>
                        <div class="case-img-wrap">
                            <picture>
                                <source srcset="images_implants/c2b.webp" type="image/webp">
                                <img src="images_implants/c2b.jpg" alt="Після операції All-on-6: відновлений незнімний зубний ряд" loading="lazy" width="725" height="483">
                            </picture>
                            <span class="case-badge" style="background:var(--primary);">Після</span>
                        </div>
                    </div>
                    <div class="case-body">
                        <h3>Комплексне відновлення обох щелеп All-on-6</h3>
                        <p>Пацієнтка 62 роки. Генералізований пародонтит важкого ступеня. Одномоментне видалення неспроможних зубів та встановлення 6 імплантів на кожну щелепу з незнімним протезуванням на балці.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 10: FAQ Section -->
    <section class="section-py" id="faq">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Відповіді на запитання</span>
                <h2>Часті запитання про імплантацію All-on-4 в Одесі</h2>
                <p>
                    Інформація щодо проведення процедури, знеболення та післяопераційного догляду.
                </p>
            </div>

            <div style="max-width:850px; margin:0 auto;">
                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Скільки коштує імплантація All-on-4 під ключ в Одесі та з чого складається ціна?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            У Harmony Dental Clinic вартість All-on-4 на німецьких імплантах Alpha Dent становить 2 400 $ за щелепу. Розрахунок прозорий: 4 імпланти Alpha Dent (4 × 350 $ = 1 400 $) + 4 мульти-юніт абатменти (4 × 50 $ = 200 $) + акриловий незнімний протез на балці (800 $). У вартість також включено планування, анестезію та контрольні огляди.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Скільки коштує імплантація All-on-6 та коли вона необхідна?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            All-on-6 на імплантах Alpha Dent коштує 3 200 $: 6 імплантів (6 × 350 $ = 2 100 $) + 6 мульти-юнітів (6 × 50 $ = 300 $) + акриловий незнімний протез на балці (800 $). Шість опор рекомендуються на верхній щелепі при м'якшій кістці або при високому жувальному навантаженні.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Скільки коштують постійні цирконієві зуби на балці через рік?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            Через 6-12 місяців після повного приживлення імплантів за бажанням пацієнта виготовляється постійний монолітний міст з діоксиду цирконію на індивідуальній фрезерованій балці. Його вартість становить 3 500 $. Це естетичний та довговічний матеріал з високою зносостійкістю.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Як реалізується відновлення зубів за протоколом 1 дня?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            Завдяки протоколу негайного навантаження (Immediate Loading) хірург Олег Швець встановлює 4 або 6 імплантів, а ортопед фіксує незнімний адаптаційний протез на балці в день операції. Пацієнт залишає клініку з відновленим зубним рядом.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Чи потрібне нарощування кістки (синус-ліфтинг) при All-on-4?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            У більшості випадків кісткова пластика та синус-ліфтинг не потрібні. Встановлення бічних імплантів під кутом до 45° дозволяє використати наявний об'єм кістки в обхід гайморових пазух і нервів. Точна можливість визначається лікарем за результатами 3D-знімка КТ.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Наскільки комфортно проходить операція All-on-4?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            Процедура проходить під якісною сучасною місцевою анестезією, яка надійно знеболює ділянку операції. Гострого болю під час втручання немає, відчувається лише легкий тиск та дотики інструментів. Ми не застосовуємо загальний наркоз (сон), оскільки місцевого знеболення достатньо. Після операції призначаються стандартні протизапальні та знеболювальні засоби для комфортного відновлення.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Чим незнімний протез на балці відрізняється від знімного протеза?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            Незнімний протез на балці надійно фіксується гвинтами до мульти-юнітів і не зміщується під час жування чи розмови. Він не закриває піднебіння, зберігає смакові відчуття та рівномірно розподіляє жувальне навантаження на імпланти.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Яка гарантія надається на роботу та імпланти?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            На імпланти діє офіційна гарантія виробника Alpha Dent. Клініка надає гарантію на виконану хірургічну та ортопедичну роботу відповідно до медичних стандартів за умови дотримання рекомендацій лікаря та регулярної гігієни 2 рази на рік.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 11: Crosslink Banner back to Single Implants & Clinic Location -->
    <section class="section-py bg-light-alt" id="consultation">
        <div class="container">
            <div style="background:linear-gradient(135deg, #253328 0%, #162018 100%); border-radius:24px; padding:50px; color:#fff; display:grid; grid-template-columns:1.2fr 0.8fr; gap:40px; align-items:center;">
                <div>
                    <span style="color:#c49b66; font-weight:800; text-transform:uppercase; font-size:13px; letter-spacing:1px;">Запис на прийом</span>
                    <h2 style="font-size:32px; font-weight:800; margin:10px 0 16px 0; color:#fff; line-height:1.2;">Запишіться на 3D-діагностику та розрахунок лікування All-on-4</h2>
                    <p style="font-size:16px; color:rgba(255,255,255,0.85); line-height:1.6; margin-bottom:24px;">
                        Отримайте детальний персональний план лікування від хірурга Олега Швеця та ортопеда Андрія Малюкіна у клініці на вул. Новаторів 1А (Одеса, Таїрова).
                    </p>
                    <div style="display:flex; gap:15px; flex-wrap:wrap;">
                        <a href="tel:+380687794547" class="btn" style="background:#fff; color:#191f1a; padding:14px 28px; border-radius:12px; font-weight:800; text-decoration:none; display:inline-flex; align-items:center; gap:8px;"
                           onclick="return gtag_report_call('tel:+380687794547');">
                            📞 Зателефонувати +38 068 779 45 47
                        </a>
                        <a href="https://t.me/Harmonyclinic_od" target="_blank" class="btn" style="background:#229ED9; color:#fff; padding:14px 24px; border-radius:12px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:8px;">
                            Написати в Telegram
                        </a>
                        <a href="viber://chat?number=%2B380687794547" class="btn" style="background:#7360f2; color:#fff; padding:14px 24px; border-radius:12px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:8px;">
                            Написати у Viber
                        </a>
                    </div>
                </div>

                <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:18px; padding:30px;">
                    <h3 style="font-size:18px; margin-bottom:15px; color:#fff;">📍 Як нас знайти</h3>
                    <p style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.6; margin-bottom:12px;">
                        <strong>Адреса:</strong> м. Одеса, вул. Новаторів 1А (Київський район, орієнтир — Таїрова / Черемушки).
                    </p>
                    <p style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.6; margin-bottom:12px;">
                        <strong>Графік роботи:</strong> Пн–Пт: 09:00 – 20:00, Сб: 10:00 – 16:00.
                    </p>
                    <p style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.6; margin-bottom:0;">
                        <strong>Потрібен лише один зуб?</strong><br>
                        <a href="implants-ua.html" style="color:#c49b66; text-decoration:underline;">Перейдіть на сторінку одиночної імплантації зубів →</a>
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer id="contacts" class="unified-footer" role="contentinfo">
        <div class="container">
            <div class="footer-content">
                <div>
                    <picture>
                        <source srcset="images/Logo.webp" type="image/webp">
                        <img loading="lazy" src="images/Logo.png" alt="Логотип Harmony Dental Clinic" class="footer-logo-img" width="1072" height="1071">
                    </picture>
                    <p style="margin-top:10px;">Сучасна сімейна та цифрова стоматологія в Одесі.</p>
                    <div class="social-icons">
                        <a href="viber://chat?number=%2B380687794547" title="Viber" aria-label="Viber"><svg viewBox="0 0 24 24">
                            <path d="M22.2,16.6c-0.2-0.6-1.3-1.2-2.1-1.4c-0.8-0.2-1.3-0.1-1.8,0.7c-0.5,0.7-1,1.4-1.6,1.4c-0.5,0-1.9-0.5-3.6-2c-1.3-1.2-2.3-2.6-2.5-3s-0.1-1,0.6-1.7c0.5-0.5,1.1-1.3,1.3-1.8c0.2-0.5,0.1-1,0.1-1.4S10.8,3.9,10.2,2.5C9.5,1.1,8.9,1.4,8.4,1.4c-0.5,0-1.4,0-2.2,0.8c-0.9,0.9-3.2,3.1-3.2,7.5c0,4.4,3.2,8.7,3.7,9.3c0.5,0.6,6.3,9.5,15.2,12.5c5.3,1.8,7.3,1.7,8.6,1.5c1.4-0.1,4.5-1.8,5.1-3.6C26.3,17.7,22.8,17.9,22.2,16.6z" />
                        </svg></a>
                        <a href="https://t.me/Harmonyclinic_od" target="_blank" title="Telegram" aria-label="Telegram"><svg viewBox="0 0 24 24">
                            <path d="M9.78,18.65l0.13-3.14l5.63-5.07c0.49-0.44-0.11-0.69-0.76-0.29L8.4,14.2l-3.03-0.95c-0.66-0.21-0.67-0.66,0.14-0.97L17.36,7.7c0.56-0.21,1.05,0.13,0.87,0.86L16.14,18.2c-0.12,0.59-0.87,0.72-1.41,0.45L9.78,18.65z" />
                        </svg></a>
                        <a href="https://www.instagram.com/harmony.dental.clinic.od/" target="_blank" title="Instagram" aria-label="Instagram"><svg viewBox="0 0 24 24">
                            <path d="M12,2.2c3.2,0,3.6,0,4.9,0.1c1.2,0.1,1.8,0.3,2.2,0.5c0.6,0.2,1,0.5,1.4,0.9c0.4,0.4,0.7,0.8,0.9,1.4c0.2,0.4,0.4,1.1,0.5,2.2c0.1,1.3,0.1,1.6,0.1,4.9s0,3.6-0.1,4.9c-0.1,1.2-0.3,1.8-0.5,2.2c-0.2,0.6-0.5,1-0.9,1.4c-0.4,0.4-0.8,0.7-1.4,0.9c-0.4,0.2-1.1,0.4-2.2,0.5C8.4,2.2,8.8,2.2,12,2.2 M12,0C8.7,0,8.3,0,7.1,0.1C5.8,0.1,4.9,0.3,4.1,0.6C3.4,0.9,2.7,1.3,2,2s-1.1,1.4-1.4,2.2C0.3,4.9,0.1,5.8,0.1,7.1C0,8.3,0,8.7,0,12s0,3.7,0.1,4.9c0.1,1.3,0.3,2.1,0.6,2.9c0.3,0.8,0.7,1.5,1.4,2.2c0.7,0.7,1.4,1.1,2.2,1.4c0.8,0.3,1.7,0.5,2.9,0.6c1.2,0.1,1.6,0.1,4.9,0.1s3.7,0,4.9-0.1c1.3-0.1,2.1-0.3,2.9-0.6c0.8-0.3,1.5-0.7,2.2-1.4c0.7-0.7,1.1-1.4,1.4-2.2c0.3-0.8,0.5-1.7,0.6-2.9c0.1-1.2,0.1-1.6,0.1-4.9s0-3.7-0.1-4.9c-0.1-1.3-0.3-2.1-0.6-2.9c-0.3-0.8-0.7-1.5-1.4-2.2c-0.7-0.7-1.4-1.1-2.2-1.4c-0.8-0.3-1.7-0.5-2.9-0.6C15.7,0,15.3,0,12,0z M12,5.8c-3.4,0-6.2,2.8-6.2,6.2c0,3.4,2.8,6.2,6.2,6.2s6.2-2.8,6.2-6.2C18.2,8.6,15.4,5.8,12,5.8z M12,16c-2.2,0-4-1.8-4-4s1.8-4,4-4s4,1.8,4,4S14.2,16,12,16z M18.4,4.2c-0.8,0-1.4,0.6-1.4,1.4s0.6,1.4,1.4,1.4s1.4-0.6,1.4-1.4S19.2,4.2,18.4,4.2z" />
                        </svg></a>
                    </div>
                </div>
                <div>
                    <h3>Меню</h3>
                    <div class="footer-links">
                        <a href="index.html#about">> Про клініку</a>
                        <a href="services-ua.html">> Послуги</a>
                        <a href="index.html#prices">> Ціни</a>
                        <a href="offer.html">> Оферта</a>
                    </div>
                </div>
                <div>
                    <h3>Послуги</h3>
                    <div class="footer-links">
                        <a href="implants-ua.html">> Імплантація</a>
                        <a href="all-on-4-odessa.html">> All-on-4 / All-on-6</a>
                        <a href="prosthetics-ua.html">> Протезування</a>
                        <a href="lechenie-ua.html">> Лікування</a>
                        <a href="hygiene-ua.html">> Гігієна</a>
                        <a href="orthodontics-ua.html">> Ортодонтія</a>
                        <a href="extraction-ua.html">> Видалення</a>
                    </div>
                </div>
                <div>
                    <h3>Контакти</h3>
                    <p>📍 м. Одеса, вул. Новаторів 1А</p>
                    <p style="margin-top:10px;">
                        <a href="tel:+380687794547" aria-label="Зателефонувати" style="color:#fff; font-weight:700;"
                            onclick="if(typeof gtag_report_conversion==='function'){return gtag_report_conversion('tel:+380687794547');}">📞 +38 068 779 45 47</a>
                    </p>
                </div>
            </div>
            <div class="copyright">Copyright © 2026 Harmony Clinic. All Rights Reserved.</div>
        </div>
    </footer>

    <!-- Floating Call Button -->
    <a href="tel:+380687794547" aria-label="Зателефонувати" class="floating-widget"
        onclick="if(typeof gtag_report_conversion === 'function') { return gtag_report_conversion('tel:+380687794547'); } else if(typeof gtag_report_call === 'function') { return gtag_report_call('tel:+380687794547'); }">
        <div class="widget-icon">
            <svg viewBox="0 0 24 24">
                <path d="M22.2,16.6c-0.2-0.6-1.3-1.2-2.1-1.4c-0.8-0.2-1.3-0.1-1.8,0.7c-0.5,0.7-1,1.4-1.6,1.4c-0.5,0-1.9-0.5-3.6-2c-1.3-1.2-2.3-2.6-2.5-3s-0.1-1,0.6-1.7c0.5-0.5,1.1-1.3,1.3-1.8c0.2-0.5,0.1-1,0.1-1.4S10.8,3.9,10.2,2.5C9.5,1.1,8.9,1.4,8.4,1.4c-0.5,0-1.4,0-2.2,0.8c-0.9,0.9-3.2,3.1-3.2,7.5c0,4.4,3.2,8.7,3.7,9.3c0.5,0.6,6.3,9.5,15.2,12.5c5.3,1.8,7.3,1.7,8.6,1.5c1.4-0.1,4.5-1.8,5.1-3.6C26.3,17.7,22.8,17.9,22.2,16.6z" />
            </svg>
        </div>
    </a>

    <script src="header.js" defer></script>
    <script src="mobile-menu.js" defer></script>
    <script>
    function switchPricingTab(tabKey, btn) {
        document.querySelectorAll('.pricing-tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.pricing-content-panel').forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        const targetPanel = document.getElementById('tab-panel-' + tabKey);
        if (targetPanel) {
            targetPanel.classList.add('active');
        }
    }

    function toggleAccordion(el){
        const c = el.nextElementSibling;
        const s = el.querySelector('span');
        if (c.style.maxHeight){
            c.style.maxHeight = null;
            s.textContent = "+";
        } else {
            c.style.maxHeight = c.scrollHeight + "px";
            s.textContent = "−";
        }
    }
    </script>
</body>

</html>
"""

def get_ru_html():
    return """<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Analytics: dataLayer + gtag stub available immediately; heavy scripts deferred -->
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config','G-6ZP07STZJF');
    gtag('config','AW-11468618731');

    function gtag_report_conversion(url){
        var navigate=function(){ if(typeof url!=='undefined'){ window.location=url; } };
        gtag('event','conversion',{'send_to':'AW-11468618731/s-heCPmCmt0bEOv31Nwq','event_callback':navigate});
        loadDeferredTags();
        setTimeout(navigate, 700);
        return false;
    }
    var gtag_report_call = gtag_report_conversion;
    var gtag_report_messenger = gtag_report_conversion;

    var __tagsLoaded=false;
    function loadDeferredTags(){
        if(__tagsLoaded)return; __tagsLoaded=true;
        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-PBZF8G5B');
        var ga=document.createElement('script'); ga.async=true; ga.src='https://www.googletagmanager.com/gtag/js?id=G-6ZP07STZJF'; document.head.appendChild(ga);
        !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
        fbq('init','451786880568879');fbq('track','PageView');
    }
    ['pointerdown','touchstart','mousedown','keydown','scroll'].forEach(function(ev){
        window.addEventListener(ev, loadDeferredTags, {once:true, passive:true});
    });
    window.addEventListener('load', function(){ setTimeout(loadDeferredTags, 6000); });
    </script>

    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="geo.region" content="UA-51">
    <meta name="geo.placename" content="Одесса">
    <meta name="geo.position" content="46.4258;30.7488">
    <meta name="ICBM" content="46.4258, 30.7488">

    <link rel="canonical" href="https://harmonyclinic.od.ua/ru/all-on-4-odessa.html">
    <link rel="alternate" hreflang="uk-UA" href="https://harmonyclinic.od.ua/all-on-4-odessa.html">
    <link rel="alternate" hreflang="ru-UA" href="https://harmonyclinic.od.ua/ru/all-on-4-odessa.html">
    <link rel="alternate" hreflang="x-default" href="https://harmonyclinic.od.ua/all-on-4-odessa.html">

    <title>Имплантация All-on-4 в Одессе — несъемные зубы по протоколу 1 дня | Harmony Clinic</title>
    <meta name="description"
        content="Тотальное восстановление зубов All-on-4 и All-on-6 в Одессе: немецкие импланты Alpha Dent (350$), несъемный протез на балке (800$). Хирург Олег Швец. ☎ +38 068 779 45 47">

    <meta property="og:locale" content="ru_UA">
    <meta property="og:site_name" content="Harmony Clinic">
    <meta property="og:title" content="Имплантация All-on-4 в Одессе — несъемные зубы по протоколу 1 дня">
    <meta property="og:description" content="Несъемное восстановление зубного ряда по протоколу All-on-4 / All-on-6. Установка моста на балке в день операции. Хирург Олег Швец.">
    <meta property="og:url" content="https://harmonyclinic.od.ua/ru/all-on-4-odessa.html">
    <meta property="og:image" content="https://harmonyclinic.od.ua/images/all-on-4-scheme.jpg">
    <meta property="og:type" content="website">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Имплантация All-on-4 в Одессе — Harmony Clinic">
    <meta name="twitter:description" content="Восстановление зубов на 4 или 6 имплантах. Хирург Олег Швец. Навигационные 3D-шаблоны.">
    <meta name="twitter:image" content="https://harmonyclinic.od.ua/images/all-on-4-scheme.jpg">

    <link rel="icon" type="image/png" href="../images/Logo.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles.css">
    <link rel="manifest" href="/site.webmanifest">

    <!-- Microdata Schema.org JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Dentist",
          "@id": "https://harmonyclinic.od.ua/#org",
          "name": "Harmony Clinic",
          "url": "https://harmonyclinic.od.ua/ru/all-on-4-odessa.html",
          "image": "https://harmonyclinic.od.ua/images/Logo.png",
          "telephone": "+380687794547",
          "priceRange": "$$$",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "ул. Новаторов, 1А",
            "addressLocality": "Одесса",
            "addressRegion": "Одесская область",
            "postalCode": "65114",
            "addressCountry": "UA"
          },
          "geo": {
            "@type": "GeoCoordinates",
            "latitude": 46.4258,
            "longitude": 30.7488
          },
          "areaServed": [
            { "@type": "City", "name": "Одесса" },
            { "@type": "AdministrativeArea", "name": "Киевский район" },
            { "@type": "Place", "name": "Таирова" },
            { "@type": "Place", "name": "Черемушки" },
            { "@type": "Place", "name": "Седьмой километр" }
          ],
          "openingHoursSpecification": [
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
              "opens": "09:00",
              "closes": "20:00"
            },
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": "Saturday",
              "opens": "10:00",
              "closes": "16:00"
            }
          ],
          "sameAs": [
            "https://www.instagram.com/harmony.dental.clinic.od/",
            "https://www.facebook.com/andrei.maliukin/"
          ]
        },
        {
          "@type": "Physician",
          "@id": "https://harmonyclinic.od.ua/#surgeon",
          "name": "Олег Швец",
          "jobTitle": "Хирург-имплантолог",
          "medicalSpecialty": "https://schema.org/Dentistry",
          "image": "https://harmonyclinic.od.ua/images/oleg.jpg",
          "worksFor": { "@id": "https://harmonyclinic.od.ua/#org" }
        },
        {
          "@type": "MedicalProcedure",
          "@id": "https://harmonyclinic.od.ua/ru/all-on-4-odessa.html#procedure",
          "name": "Имплантация зубов All-on-4 и All-on-6",
          "alternateName": [
            "Протезирование все на 4",
            "Восстановление челюсти за 1 день",
            "Тотальная дентальная имплантация All-on-4"
          ],
          "procedureType": "https://schema.org/SurgicalProcedure",
          "bodyLocation": "Верхняя и нижняя челюсти",
          "howPerformed": "Установка 4 или 6 немецких имплантов Alpha Dent по навигационному 3D-шаблону с фиксацией несъемного протеза на балке в день операции под современной местной анестезией.",
          "preparation": "3D КТ челюсти, цифровое внутриротовое сканирование 3Shape TRIOS 4, виртуальное моделирование положения имплантов.",
          "followup": "Контрольные осмотры на 7, 14 день, через 1, 3 и 6 месяцев с возможностью установки постоянного циркониевого моста на балке через год.",
          "performer": [
            { "@id": "https://harmonyclinic.od.ua/#surgeon" },
            { "@id": "https://harmonyclinic.od.ua/#org" }
          ],
          "status": "https://schema.org/ActiveActionStatus"
        },
        {
          "@type": "Service",
          "name": "Имплантация All-on-4 в Одессе под ключ",
          "provider": { "@id": "https://harmonyclinic.od.ua/#org" },
          "areaServed": [
            { "@type": "City", "name": "Одесса" },
            { "@type": "Place", "name": "Таирова" }
          ],
          "serviceType": "Тотальная имплантация и несъемное протезирование",
          "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Стоимость имплантации All-on-4 и All-on-6 под ключ",
            "itemListElement": [
              {
                "@type": "Offer",
                "name": "All-on-4 Alpha Dent (Германия): 4 импланта + 4 мульти-юнита + несъемный протез на балке",
                "priceCurrency": "USD",
                "price": "2400",
                "availability": "https://schema.org/InStock"
              },
              {
                "@type": "Offer",
                "name": "All-on-6 Alpha Dent (Германия): 6 имплантов + 6 мульти-юнитов + несъемный протез на балке",
                "priceCurrency": "USD",
                "price": "3200",
                "availability": "https://schema.org/InStock"
              },
              {
                "@type": "Offer",
                "name": "Постоянный протез: Циркониевые зубы на балке (через 1 год)",
                "priceCurrency": "USD",
                "price": "3500",
                "availability": "https://schema.org/InStock"
              }
            ]
          }
        },
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "name": "Главная",
              "item": "https://harmonyclinic.od.ua/ru/"
            },
            {
              "@type": "ListItem",
              "position": 2,
              "name": "Услуги",
              "item": "https://harmonyclinic.od.ua/ru/services-ua.html"
            },
            {
              "@type": "ListItem",
              "position": 3,
              "name": "Имплантация зубов",
              "item": "https://harmonyclinic.od.ua/ru/implants-ua.html"
            },
            {
              "@type": "ListItem",
              "position": 4,
              "name": "Имплантация All-on-4 в Одессе",
              "item": "https://harmonyclinic.od.ua/ru/all-on-4-odessa.html"
            }
          ]
        },
        {
          "@type": "FAQPage",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "Сколько стоит имплантация All-on-4 под ключ в Одессе и из чего состоит цена?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "В Harmony Dental Clinic стоимость All-on-4 на немецких имплантах Alpha Dent составляет 2 400 $ за челюсть. Расчет прозрачный: 4 импланта Alpha Dent (4 × 350 $ = 1 400 $) + 4 мульти-юнит абатмента (4 × 50 $ = 200 $) + акриловый несъемный протез на балке (800 $). В стоимость также включено планирование, анестезия и контрольные осмотры."
              }
            },
            {
              "@type": "Question",
              "name": "Сколько стоит имплантация All-on-6 и когда она необходима?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "All-on-6 на имплантах Alpha Dent стоит 3 200 $: 6 имплантов (6 × 350 $ = 2 100 $) + 6 мульти-юнитов (6 × 50 $ = 300 $) + акриловый несъемный протез на балке (800 $). Шесть опор рекомендуются на верхней челюсти при более мягкой кости или при повышенной жевательной нагрузке."
              }
            },
            {
              "@type": "Question",
              "name": "Сколько стоят постоянные циркониевые зубы на балке через год?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Через 6-12 месяцев после полного приживления имплантов по желанию пациента изготавливается постоянный монолитный мост из диоксида циркония на индивидуальной фрезерованной балке. Его стоимость составляет 3 500 $. Это прочный и эстетичный материал с высокой износостойкостью."
              }
            },
            {
              "@type": "Question",
              "name": "Как реализуется восстановление зубов по протоколу 1 дня?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Благодаря протоколу немедленной нагрузки (Immediate Loading) хирург Олег Швец устанавливает 4 или 6 имплантов, а ортопед фиксирует адаптационный несъемный протез на балке в день операции. Пациент уходит домой с восстановленным зубным рядом."
              }
            },
            {
              "@type": "Question",
              "name": "Нужно ли наращивание кости (синус-лифтинг) при All-on-4?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "В большинстве случаев костная пластика и синус-лифтинг не требуются. Установка боковых имплантов под углом до 45° позволяет задействовать имеющийся объем кости в обход гайморовых пазух и нервов. Точная возможность определяется врачом по результатам 3D КТ."
              }
            },
            {
              "@type": "Question",
              "name": "Насколько комфортно проходит операция All-on-4?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Процедура проходит под качественной современной местной анестезией, которая надежно обезболивает область операции. Острой боли во время вмешательства нет, ощущается лишь легкое давление и прикосновения инструментов. Мы не применяем общий наркоз (сон), так как местного обезболивания достаточно. После операции назначаются стандартные противовоспалительные и обезболивающие препараты для комфортного восстановления."
              }
            },
            {
              "@type": "Question",
              "name": "Чем несъемный протез на балке отличается от съемного протеза?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Несъемный протез на балке надежно фиксируется винтами к мульти-юнітам и не смещается во время еды или разговора. Он не закрывает нёбо, сохраняет вкусовые ощущения и равномерно распределяет жевательную нагрузку на импланты."
              }
            },
            {
              "@type": "Question",
              "name": "Какая гарантия предоставляется на работу и импланты?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "На импланты действует официальная гарантия производителя Alpha Dent. Клиника предоставляет гарантию на выполненную хирургическую и ортопедическую работу в соответствии с медицинскими стандартами при условии соблюдения рекомендаций врача и регулярной гигиены 2 раза в год."
              }
            }
          ]
        }
      ]
    }
    </script>

    <style>
        /* Scoped styles for All-on-4 landing */
        .all-hero {
            position: relative;
            padding: 75px 0 65px;
            min-height: 68vh;
            display: flex;
            align-items: center;
            background: radial-gradient(circle at top right, rgba(82, 97, 84, 0.45) 0%, transparent 65%),
                        linear-gradient(135deg, #0c1210 0%, #030604 100%);
            color: #fff;
            overflow: hidden;
        }

        .all-hero .hero-grid {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 40px;
            align-items: center;
        }

        .all-hero h1 {
            font-size: clamp(30px, 4vw, 48px);
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: -0.5px;
            margin-bottom: 20px;
        }

        .all-hero .hero-lead {
            font-size: 17px;
            color: rgba(255, 255, 255, 0.85);
            line-height: 1.6;
            margin-bottom: 30px;
        }

        .hero-usps {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-bottom: 35px;
        }

        .usp-pill {
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 12px 18px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
            backdrop-filter: blur(8px);
            font-size: 14px;
            font-weight: 600;
        }

        .usp-pill svg {
            width: 24px;
            height: 24px;
            fill: #c49b66;
            flex-shrink: 0;
        }

        .hero-cta-btns {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }

        .hero-card-preview {
            position: relative;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            background: #111a13;
        }

        .hero-card-preview img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
        }

        .hero-card-badge {
            position: absolute;
            bottom: 16px;
            left: 16px;
            right: 16px;
            background: rgba(12, 18, 14, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 14px 18px;
            border-radius: 12px;
            font-size: 13px;
            line-height: 1.4;
        }

        .hero-card-badge strong {
            color: #c49b66;
            display: block;
            font-size: 15px;
            margin-bottom: 2px;
        }

        /* Content Sections */
        .section-py {
            padding: 80px 0;
        }

        .bg-light-alt {
            background-color: #f8faf8;
        }

        .section-header-center {
            text-align: center;
            max-width: 820px;
            margin: 0 auto 45px;
        }

        .section-header-center h2 {
            font-size: clamp(26px, 3.2vw, 36px);
            font-weight: 800;
            color: #191f1a;
            letter-spacing: -0.5px;
            margin-bottom: 16px;
            line-height: 1.2;
        }

        .section-header-center p {
            font-size: 16px;
            color: #556057;
            line-height: 1.6;
        }

        .eyebrow-tag {
            display: inline-block;
            background: rgba(82, 97, 84, 0.12);
            color: var(--primary);
            font-size: 13px;
            font-weight: 800;
            padding: 6px 14px;
            border-radius: 100px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 14px;
        }

        /* 2-Col Explainer */
        .explainer-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 48px;
            align-items: center;
        }

        .explainer-text h3 {
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 18px;
            color: #191f1a;
        }

        .explainer-text p {
            font-size: 16px;
            line-height: 1.7;
            color: #4a544c;
            margin-bottom: 20px;
        }

        .explainer-list {
            list-style: none;
            padding: 0;
            margin: 24px 0;
        }

        .explainer-list li {
            position: relative;
            padding-left: 32px;
            margin-bottom: 14px;
            font-size: 15px;
            color: #2b352d;
            line-height: 1.5;
        }

        .explainer-list li::before {
            content: "✓";
            position: absolute;
            left: 0;
            top: 0;
            width: 22px;
            height: 22px;
            background: var(--primary);
            color: #fff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 800;
        }

        .explainer-media {
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08);
            border: 1px solid #e3e8e3;
        }

        .explainer-media img {
            width: 100%;
            height: auto;
            display: block;
        }

        /* Candidates Cards */
        .candidates-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 22px;
        }

        .candidate-card {
            background: #fff;
            border-radius: 18px;
            padding: 30px 24px;
            border: 1px solid #e5ebe5;
            box-shadow: 0 6px 24px rgba(0, 0, 0, 0.04);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
        }

        .candidate-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 16px 36px rgba(82, 97, 84, 0.12);
            border-color: var(--primary-light);
        }

        .candidate-icon {
            width: 52px;
            height: 52px;
            background: rgba(82, 97, 84, 0.1);
            color: var(--primary);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-bottom: 20px;
        }

        .candidate-card h3 {
            font-size: 19px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 12px;
        }

        .candidate-card p {
            font-size: 14px;
            color: #5d695f;
            line-height: 1.6;
        }

        /* Comparison Table */
        .table-responsive {
            overflow-x: auto;
            background: #fff;
            border-radius: 20px;
            border: 1px solid #e3e8e3;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }

        .custom-comp-table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 15px;
            min-width: 680px;
        }

        .custom-comp-table th {
            background: #253328;
            color: #fff;
            padding: 20px 22px;
            font-weight: 700;
            font-size: 16px;
        }

        .custom-comp-table th.highlight-col {
            background: var(--primary);
            color: #fff;
        }

        .custom-comp-table td {
            padding: 18px 22px;
            border-bottom: 1px solid #edf2ed;
            color: #374239;
            line-height: 1.5;
        }

        .custom-comp-table tr:last-child td {
            border-bottom: none;
        }

        .custom-comp-table td.highlight-col {
            background: rgba(82, 97, 84, 0.06);
            font-weight: 600;
            color: #1a221c;
        }

        .badge-pro {
            display: inline-block;
            background: #2e7d32;
            color: #fff;
            font-size: 12px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            margin-right: 6px;
        }

        .badge-con {
            display: inline-block;
            background: #c62828;
            color: #fff;
            font-size: 12px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            margin-right: 6px;
        }

        /* =======================================================
           COMPACT INTERACTIVE PRICING TABS SECTION
        ======================================================= */
        .pricing-tabs-container {
            max-width: 980px;
            margin: 0 auto;
        }

        .pricing-nav-tabs {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 28px;
            flex-wrap: wrap;
        }

        .pricing-tab-btn {
            padding: 14px 26px;
            background: #fff;
            border: 2px solid #e1e7e1;
            border-radius: 14px;
            font-weight: 700;
            font-size: 15px;
            color: #4b584d;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .pricing-tab-btn:hover {
            border-color: var(--primary-light);
            background: #fdfdfd;
        }

        .pricing-tab-btn.active {
            background: #fff;
            border-color: var(--primary);
            color: var(--primary);
            box-shadow: 0 8px 24px rgba(82, 97, 84, 0.16);
            transform: translateY(-2px);
        }

        .pricing-tab-btn.gold-active.active {
            border-color: #c49b66;
            color: #8c6732;
        }

        .pricing-content-panel {
            background: #fff;
            border: 1px solid #e1e8e1;
            border-radius: 24px;
            padding: 42px 45px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.05);
            display: none;
            animation: fadeInTab 0.3s ease;
        }

        .pricing-content-panel.active {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 40px;
            align-items: center;
        }

        @keyframes fadeInTab {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .tab-panel-left {
            border-right: 1px solid #edf2ed;
            padding-right: 35px;
        }

        .tab-tag-badge {
            display: inline-block;
            background: #eef4ee;
            color: var(--primary);
            font-size: 12px;
            font-weight: 800;
            padding: 5px 12px;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            margin-bottom: 12px;
        }

        .tab-panel-left h3 {
            font-size: 26px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 8px;
        }

        .tab-price-big {
            font-size: 44px;
            font-weight: 800;
            color: var(--primary);
            line-height: 1;
            margin: 14px 0 6px;
        }

        .tab-price-sub {
            font-size: 13.5px;
            color: #707d72;
            margin-bottom: 20px;
        }

        .tab-formula-box {
            background: #f4f7f4;
            border: 1px dashed #cad4cb;
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 24px;
            font-size: 13.5px;
            color: #38453a;
            line-height: 1.55;
        }

        .tab-formula-box strong {
            color: #191f1a;
        }

        .tab-panel-right h4 {
            font-size: 16px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 16px;
        }

        .tab-panel-right ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .tab-panel-right li {
            position: relative;
            padding-left: 26px;
            margin-bottom: 12px;
            font-size: 14px;
            color: #3f4d41;
            line-height: 1.45;
        }

        .tab-panel-right li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--primary);
            font-weight: 800;
            font-size: 15px;
        }

        /* Timeline Steps */
        .timeline-container {
            position: relative;
            max-width: 900px;
            margin: 0 auto;
        }

        .timeline-step {
            display: grid;
            grid-template-columns: 80px 1fr;
            gap: 26px;
            margin-bottom: 36px;
            position: relative;
        }

        .timeline-step:not(:last-child)::after {
            content: "";
            position: absolute;
            left: 39px;
            top: 75px;
            bottom: -25px;
            width: 2px;
            background: #d8e0d9;
        }

        .step-num-badge {
            width: 78px;
            height: 78px;
            background: #fff;
            border: 2px solid var(--primary);
            color: var(--primary);
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: 800;
            box-shadow: 0 6px 18px rgba(82, 97, 84, 0.15);
            z-index: 2;
        }

        .step-num-badge span {
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .step-card {
            background: #fff;
            border-radius: 18px;
            padding: 26px 30px;
            border: 1px solid #e3e8e3;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.04);
        }

        .step-card h3 {
            font-size: 20px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 10px;
        }

        .step-card p {
            font-size: 15px;
            color: #556257;
            line-height: 1.6;
            margin: 0;
        }

        /* Doctor Highlight (E-E-A-T) */
        .doctor-highlight-box {
            background: #fff;
            border-radius: 24px;
            border: 1px solid #e1e7e1;
            padding: 45px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.05);
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 45px;
            align-items: center;
        }

        .doc-photo-wrap {
            border-radius: 18px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }

        .doc-photo-wrap img {
            width: 100%;
            height: auto;
            display: block;
        }

        .doc-info-content h3 {
            font-size: 28px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 6px;
        }

        .doc-title-role {
            font-size: 16px;
            color: var(--primary);
            font-weight: 700;
            margin-bottom: 20px;
        }

        .doc-desc {
            font-size: 15px;
            color: #4b564d;
            line-height: 1.7;
            margin-bottom: 24px;
        }

        .doc-stats-row {
            display: flex;
            gap: 30px;
            margin-bottom: 28px;
            padding: 20px 0;
            border-top: 1px solid #edf2ed;
            border-bottom: 1px solid #edf2ed;
        }

        .doc-stat-item strong {
            display: block;
            font-size: 22px;
            color: #191f1a;
            font-weight: 800;
        }

        .doc-stat-item span {
            font-size: 13px;
            color: #728074;
        }

        /* Cases Grid */
        .cases-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
        }

        .case-card {
            background: #fff;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid #e3e8e3;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
        }

        .case-imgs-split {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2px;
            background: #ddd;
            position: relative;
        }

        .case-img-wrap {
            position: relative;
        }

        .case-img-wrap img {
            width: 100%;
            height: auto;
            display: block;
            aspect-ratio: 4/3;
            object-fit: cover;
        }

        .case-badge {
            position: absolute;
            bottom: 8px;
            left: 8px;
            background: rgba(0, 0, 0, 0.7);
            color: #fff;
            font-size: 11px;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            text-transform: uppercase;
        }

        .case-body {
            padding: 24px;
        }

        .case-body h3 {
            font-size: 18px;
            font-weight: 800;
            color: #191f1a;
            margin-bottom: 8px;
        }

        .case-body p {
            font-size: 14px;
            color: #556257;
            line-height: 1.6;
            margin: 0;
        }

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {
            .all-hero .hero-grid { grid-template-columns: 1fr; }
            .candidates-grid { grid-template-columns: repeat(2, 1fr); }
            .pricing-content-panel.active { grid-template-columns: 1fr; gap: 30px; }
            .tab-panel-left { border-right: none; border-bottom: 1px solid #edf2ed; padding-right: 0; padding-bottom: 25px; }
            .doctor-highlight-box { grid-template-columns: 1fr; gap: 30px; }
            .doc-photo-wrap { max-width: 320px; margin: 0 auto; }
            .explainer-grid { grid-template-columns: 1fr; }
        }

        @media (max-width: 768px) {
            .all-hero { padding: 50px 0 45px; }
            .all-hero h1 { font-size: 28px; }
            .hero-usps { grid-template-columns: 1fr; }
            .candidates-grid { grid-template-columns: 1fr; }
            .pricing-content-panel { padding: 28px 20px; }
            .tab-price-big { font-size: 36px; }
            .pricing-nav-tabs { flex-direction: column; }
            .pricing-tab-btn { justify-content: center; }
            .cases-grid { grid-template-columns: 1fr; }
            .timeline-step { grid-template-columns: 60px 1fr; gap: 16px; }
            .step-num-badge { width: 58px; height: 58px; font-size: 16px; }
            .timeline-step:not(:last-child)::after { left: 29px; }
            .doc-stats-row { flex-direction: column; gap: 14px; }
            .section-py { padding: 55px 0; }
        }
    </style>
</head>

<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PBZF8G5B"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

    <header role="banner">
        <div class="container nav-wrapper">
            <a href="index.html" class="logo">
                <picture>
                    <source srcset="../images/Logo.webp" type="image/webp">
                    <img loading="lazy" src="../images/Logo.png" alt="Harmony Dental Clinic" width="1072" height="1071">
                </picture>
            </a>
            <nav role="navigation">
                <ul class="nav-menu" id="navMenu">
                    <li><a href="index.html">Главная</a></li>
                    <li><a href="services-ua.html">Услуги</a></li>
                    <li><a href="implants-ua.html">Имплантация</a></li>
                    <li><a href="all-on-4-odessa.html" style="color:var(--primary);font-weight:800;">All-on-4</a></li>
                    <li><a href="index.html#team">Врачи</a></li>
                    <li><a href="index.html#prices">Цены</a></li>
                    <li><a href="blog.html">Блог</a></li>
                    <li><a href="#contacts">Контакты</a></li>
                </ul>
            </nav>
            <div style="display: flex; align-items: center; gap: 15px;">
                <div class="lang-switch">
                    <a href="../all-on-4-odessa.html">UA</a>
                    <a href="all-on-4-odessa.html" class="active">RU</a>
                </div>
                <a href="tel:+380687794547" aria-label="Позвонить" class="header-phone"
                    onclick="return gtag_report_call('tel:+380687794547');">+38 068 779 45 47</a>
                <div class="mobile-toggle" onclick="toggleMenu()">☰</div>
            </div>
        </div>
    </header>

    <!-- Breadcrumbs Section -->
    <div style="background:#f4f7f4; padding: 14px 0; border-bottom: 1px solid #e3e8e3;">
        <div class="container">
            <nav aria-label="Хлебные крошки" style="font-size: 13px; color: #667368;">
                <a href="index.html" style="color: inherit; text-decoration: none;">Главная</a>
                <span style="margin: 0 8px;">/</span>
                <a href="services-ua.html" style="color: inherit; text-decoration: none;">Услуги</a>
                <span style="margin: 0 8px;">/</span>
                <a href="implants-ua.html" style="color: inherit; text-decoration: none;">Имплантация зубов</a>
                <span style="margin: 0 8px;">/</span>
                <span style="color: var(--primary); font-weight: 700;">All-on-4 в Одессе</span>
            </nav>
        </div>
    </div>

    <!-- Section 1: Hero -->
    <section class="all-hero">
        <div class="container">
            <div class="hero-grid">
                <div>
                    <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); padding:7px 16px; border-radius:100px; font-size:13px; font-weight:600; margin-bottom:20px; backdrop-filter:blur(5px);">
                        <span style="width:8px; height:8px; background:#4ade80; border-radius:50%; display:inline-block;"></span>
                        Работаем автономно: есть генератор и резервное питание
                    </div>

                    <h1>Имплантация All-on-4 и All-on-6 в Одессе — несъемные зубы за 1 день</h1>
                    
                    <p class="hero-lead">
                        Полное восстановление зубного ряда челюсти на немецких имплантах Alpha Dent с фиксацией несъемного протеза на балке в день операции. Прозрачный расчет стоимости по фиксированному плану лечения.
                    </p>

                    <div class="hero-usps">
                        <div class="usp-pill">
                            <svg viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
                            <span>Хирург-имплантолог <strong>Олег Швец</strong></span>
                        </div>
                        <div class="usp-pill">
                            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                            <span>3D навигационные шаблоны</span>
                        </div>
                        <div class="usp-pill">
                            <svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
                            <span>Несъемный протез на балке за 1 день</span>
                        </div>
                        <div class="usp-pill">
                            <svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
                            <span>Гарантия производителя на импланты</span>
                        </div>
                    </div>

                    <div class="hero-cta-btns">
                        <a href="#prices" class="btn" style="background:var(--primary); color:#fff; border:none; padding:15px 30px; font-weight:800; font-size:16px; border-radius:12px; text-decoration:none; display:inline-flex; align-items:center; gap:10px; box-shadow:0 10px 25px rgba(82,97,84,0.4);">
                            Рассчитать стоимость под ключ
                        </a>
                        <a href="tel:+380687794547" class="btn" style="background:rgba(255,255,255,0.12); color:#fff; border:1px solid rgba(255,255,255,0.25); padding:15px 26px; font-weight:700; font-size:15px; border-radius:12px; text-decoration:none; display:inline-flex; align-items:center; gap:8px;"
                           onclick="return gtag_report_call('tel:+380687794547');">
                            📞 Позвонить
                        </a>
                    </div>
                </div>

                <div>
                    <div class="hero-card-preview">
                        <picture>
                            <img src="../images/all-on-4-scheme.jpg" alt="Схема имплантации All-on-4 в Одессе: угловая установка 4 имплантов и несъемный мост" width="1376" height="768">
                        </picture>
                        <div class="hero-card-badge">
                            <strong>Концепция All-on-4 / All-on-6</strong>
                            Несъемная конструкция опирается на 4 или 6 имплантов через жесткую балку без необходимости во вставных протезах.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: What is All-on-4 and How it Works -->
    <section class="section-py">
        <div class="container">
            <div class="explainer-grid">
                <div class="explainer-media">
                    <picture>
                        <img src="../images/all-on-4-scheme.jpg" alt="3D анатомическая схема тотальной имплантации челюсти All-on-4" width="1376" height="768" loading="lazy">
                    </picture>
                </div>

                <div class="explainer-text">
                    <span class="eyebrow-tag">Суть методики</span>
                    <h2>Что такое технология All-on-4 («Все на четырех») и All-on-6?</h2>
                    <p>
                        <strong>All-on-4</strong> — это международный протокол реабилитации зубного ряда, разработанный для пациентов с полным отсутствием зубов (адентией) или когда оставшиеся зубы не подлежат сохранению.
                    </p>
                    <p>
                        Вместо установки отдельного импланта под каждый зуб хирург устанавливает <strong>4 или 6 титановых имплантов Alpha Dent</strong> по специальной пространственной схеме:
                    </p>
                    <ul class="explainer-list">
                        <li><strong>Два центральных импланта</strong> устанавливаются вертикально во фронтальном отделе, где объем кости обычно сохраняется лучше всего.</li>
                        <li><strong>Два боковых (дистальных) импланта</strong> располагаются под углом до 45°. Это позволяет задействовать плотные участки кости и в большинстве случаев <strong>избежать сложного наращивания кости или синус-лифтинга</strong>.</li>
                        <li><strong>Мульти-юнит абатменты (Multi-unit):</strong> специальные переходники по 50 $, выравнивающие угол наклона и обеспечивающие надежную винтовую фиксацию несъемного протеза на балке.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 3: Candidates & Indications (Problem -> Solution) -->
    <section class="section-py bg-light-alt">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Показания</span>
                <h2>Кому подходит протокол имплантации All-on-4?</h2>
                <p>
                    Методика позволяет восстановить жевательную функцию и эстетику улыбки при сложных клинических ситуациях.
                </p>
            </div>

            <div class="candidates-grid">
                <div class="candidate-card">
                    <div class="candidate-icon">🦷</div>
                    <h3>Полное отсутствие зубов</h3>
                    <p>
                        Полная адентия на верхней или нижней челюсти. Возвращаем возможность нормально питаться и открыто улыбаться.
                    </p>
                </div>

                <div class="candidate-card">
                    <div class="candidate-icon">⚠️</div>
                    <h3>Подвижные и разрушенные зубы</h3>
                    <p>
                        Тяжелый пародонтит или генерализованное разрушение корней. Удаление оставшихся зубов и установка имплантов проводятся за один визит.
                    </p>
                </div>

                <div class="candidate-card">
                    <div class="candidate-icon">🚫</div>
                    <h3>Дискомфорт от съемных протезов</h3>
                    <p>
                        Когда съемные протезы натирают десну, смещаются при разговоре или еде и перекрывают нёбо, вызывая рвотный рефлекс.
                    </p>
                </div>

                <div class="candidate-card">
                    <div class="candidate-icon">📉</div>
                    <h3>Дефицит костной ткани</h3>
                    <p>
                        Наклонное положение боковых опор позволяет надежно зафиксировать импланты даже при уменьшенной высоте кости.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 4: Detailed Comparison Table -->
    <section class="section-py">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Объективное сравнение</span>
                <h2>All-on-4 / All-on-6 vs Съемный протез vs Классическая имплантация</h2>
                <p>
                    Сравнение клинических характеристик различных методов восстановления челюсти.
                </p>
            </div>

            <div class="table-responsive">
                <table class="custom-comp-table">
                    <thead>
                        <tr>
                            <th>Критерий оценки</th>
                            <th class="highlight-col">All-on-4 / All-on-6 на балке</th>
                            <th>Обычный съемный протез</th>
                            <th>Классическая имплантация (8-10 имплантов)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Срок фиксации протеза</strong></td>
                            <td class="highlight-col"><span class="badge-pro">1 день</span> Адаптационный протез фиксируется в день операции</td>
                            <td>2–4 недели (после изготовления в лаборатории)</td>
                            <td>4–8 месяцев (после полного приживления)</td>
                        </tr>
                        <tr>
                            <td><strong>Тип фиксации</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Стабильная</span> Винтовая фиксация к балке и мульти-юнитам</td>
                            <td><span class="badge-con">Подвижная</span> Держится за счет присасывания или кламмеров</td>
                            <td><span class="badge-pro">Стабильная</span> Отдельные коронки или мостовидные протезы</td>
                        </tr>
                        <tr>
                            <td><strong>Жевательный комфорт</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Высокий</span> Максимально приближен к естественным зубам</td>
                            <td><span class="badge-con">Ограниченный</span> Затруднено пережевывание твердой пищи</td>
                            <td><span class="badge-pro">Высокий</span> Полная жевательная нагрузка</td>
                        </tr>
                        <tr>
                            <td><strong>Перекрытие нёба</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Нет</span> Нёбо открыто, вкусовые рецепторы и речь свободны</td>
                            <td><span class="badge-con">Да</span> Пластмассовый базис полностью закрывает нёбо</td>
                            <td><span class="badge-pro">Нет</span> Только зубы и десневой контур</td>
                        </tr>
                        <tr>
                            <td><strong>Потребность в синус-лифтинге</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Сведена к минимуму</span> Благодаря угловым имплантам</td>
                            <td>Не требуется</td>
                            <td><span class="badge-con">Часто необходима</span> Обязательная костная пластика при дефиците</td>
                        </tr>
                        <tr>
                            <td><strong>Нагрузка на кость</strong></td>
                            <td class="highlight-col"><span class="badge-pro">Равномерная</span> Балка распределяет давление между опорами</td>
                            <td><span class="badge-con">Неравномерная</span> Давление на десну может ускорять атрофию</td>
                            <td><span class="badge-pro">Физиологичная</span> Нагрузка через отдельные импланты</td>
                        </tr>
                        <tr>
                            <td><strong>Стоимость лечения</strong></td>
                            <td class="highlight-col"><strong>Фиксированная по протоколу:</strong> 2 400 $ (4 оп.) / 3 200 $ (6 оп.)</td>
                            <td>Доступная сначала, но требует частых перебазировок</td>
                            <td>Высокая (отдельно за каждую единицу + пластика кости)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- Section 5: Sleek Interactive Tabs Pricing Section -->
    <section class="section-py bg-light-alt" id="prices">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Прозрачный прайс</span>
                <h2>Стоимость имплантации All-on-4 и All-on-6 в Одессе</h2>
                <p>
                    Выберите подходящий вариант лечения. Честный расчет на базе системы Alpha Dent (Германия).
                </p>
            </div>

            <div class="pricing-tabs-container">
                <!-- Segmented Tabs Navigation -->
                <div class="pricing-nav-tabs">
                    <button class="pricing-tab-btn active" onclick="switchPricingTab('all4', this)">
                        <span>🌟</span> All-on-4 Alpha Dent (2 400 $)
                    </button>
                    <button class="pricing-tab-btn" onclick="switchPricingTab('all6', this)">
                        <span>💪</span> All-on-6 Alpha Dent (3 200 $)
                    </button>
                    <button class="pricing-tab-btn gold-active" onclick="switchPricingTab('zirconia', this)">
                        <span>👑</span> Цирконий на балке (3 500 $)
                    </button>
                </div>

                <!-- Tab 1: All-on-4 Alpha Dent -->
                <div id="tab-panel-all4" class="pricing-content-panel active">
                    <div class="tab-panel-left">
                        <span class="tab-tag-badge">Базовый протокол • Германия</span>
                        <h3>All-on-4 Alpha Dent</h3>
                        <div class="tab-price-big">2 400 $</div>
                        <div class="tab-price-sub">за полное восстановление одной челюсти (зубы за 1 день)</div>

                        <div class="tab-formula-box">
                            <strong>Прозрачный пошаговый расчет:</strong><br>
                            • 4 импланта Alpha Dent (4 × 350 $) = <strong>1 400 $</strong><br>
                            • 4 мульти-юнит абатмента (4 × 50 $) = <strong>200 $</strong><br>
                            • Акриловый несъемный протез на балке = <strong>800 $</strong>
                        </div>

                        <a href="#consultation" class="btn" style="background:var(--primary); color:#fff; padding:14px 28px; border-radius:12px; font-weight:800; text-decoration:none; display:inline-block; box-shadow:0 8px 20px rgba(82,97,84,0.3);">
                            Записаться на All-on-4 (2 400 $)
                        </a>
                    </div>

                    <div class="tab-panel-right">
                        <h4>Что входит в стоимость лечения:</h4>
                        <ul>
                            <li>3D компьютерное планирование операции</li>
                            <li>Изготовление индивидуального 3D-шаблона</li>
                            <li>4 титановых импланта Alpha Dent (Германия)</li>
                            <li>4 оригинальных мульти-юнита (угловые абатменты)</li>
                            <li>Несъемный протез на балке в день операции</li>
                            <li>Местная анестезия, наложение швов и контрольные осмотры</li>
                        </ul>
                    </div>
                </div>

                <!-- Tab 2: All-on-6 Alpha Dent -->
                <div id="tab-panel-all6" class="pricing-content-panel">
                    <div class="tab-panel-left">
                        <span class="tab-tag-badge" style="background:#e5eee6; color:#2d3a2f;">Повышенная опора</span>
                        <h3>All-on-6 Alpha Dent</h3>
                        <div class="tab-price-big">3 200 $</div>
                        <div class="tab-price-sub">за полное восстановление челюсти на 6 опорах</div>

                        <div class="tab-formula-box">
                            <strong>Прозрачный пошаговый расчет:</strong><br>
                            • 6 имплантов Alpha Dent (6 × 350 $) = <strong>2 100 $</strong><br>
                            • 6 мульти-юнит абатментов (6 × 50 $) = <strong>300 $</strong><br>
                            • Акриловый несъемный протез на балке = <strong>800 $</strong>
                        </div>

                        <a href="#consultation" class="btn" style="background:var(--primary); color:#fff; padding:14px 28px; border-radius:12px; font-weight:800; text-decoration:none; display:inline-block; box-shadow:0 8px 20px rgba(82,97,84,0.3);">
                            Записаться на All-on-6 (3 200 $)
                        </a>
                    </div>

                    <div class="tab-panel-right">
                        <h4>Особенности протокола на 6 имплантах:</h4>
                        <ul>
                            <li>Все из базового протокола +</li>
                            <li><strong>6 имплантов</strong> для более широкого распределения жевательной нагрузки</li>
                            <li>Рекомендовано для верхней челюсти или широкого зубного ряда</li>
                            <li>6 оригинальных мульти-юнит абатментов</li>
                            <li>Несъемный адаптационный мост на балке в день операции</li>
                            <li>Дополнительная механическая поддержка конструкции</li>
                        </ul>
                    </div>
                </div>

                <!-- Tab 3: Zirconia on Bar -->
                <div id="tab-panel-zirconia" class="pricing-content-panel">
                    <div class="tab-panel-left">
                        <span class="tab-tag-badge" style="background:#fcf5ea; color:#966f38;">Постоянный этап через 6–12 мес</span>
                        <h3>Циркониевые зубы на балке</h3>
                        <div class="tab-price-big" style="color:#966f38;">3 500 $</div>
                        <div class="tab-price-sub">за постоянный несъемный мост на фрезерованной балке</div>

                        <div class="tab-formula-box" style="background:#fbf8f3; border-color:#e8dcce;">
                            <strong>Долговечное постоянное протезирование:</strong><br>
                            Изготавливается после полной остеоинтеграции имплантов с костью на замену первичному протезу.
                        </div>

                        <a href="#consultation" class="btn" style="background:#966f38; color:#fff; padding:14px 28px; border-radius:12px; font-weight:800; text-decoration:none; display:inline-block; box-shadow:0 8px 20px rgba(150,111,56,0.3);">
                            Узнать о Цирконии (3 500 $)
                        </a>
                    </div>

                    <div class="tab-panel-right">
                        <h4>Характеристики монолитного циркония:</h4>
                        <ul>
                            <li>Индивидуальная фрезерованная балка CAD/CAM</li>
                            <li>Высокопрочный диоксид циркония</li>
                            <li>Естественный внешний вид и прозрачность эмали</li>
                            <li>Высокая устойчивость к истиранию и нагрузкам</li>
                            <li>Материал не впитывает красители и сохраняет цвет</li>
                            <li>Длительный срок службы при правильном уходе</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 6: Step-by-Step Timeline (Immediate Loading) -->
    <section class="section-py">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Пошаговый план</span>
                <h2>Как проходит лечение по протоколу All-on-4</h2>
                <p>
                    Последовательные этапы от первичного обследования до фиксации постоянной конструкции.
                </p>
            </div>

            <div class="timeline-container">
                <!-- Step 1 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        01
                        <span>Этап 1</span>
                    </div>
                    <div class="step-card">
                        <h3>3D-диагностика и цифровое сканирование 3Shape</h3>
                        <p>
                            Проводим компьютерную томографию (КТ) для оценки костной ткани и анатомических структур. Сканируем полость рта цифровым сканером 3Shape TRIOS 4. В программе моделируем точное положение каждого импланта.
                        </p>
                    </div>
                </div>

                <!-- Step 2 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        02
                        <span>Шаблон</span>
                    </div>
                    <div class="step-card">
                        <h3>Печать хирургического навигационного шаблона</h3>
                        <p>
                            По индивидуальной цифровой модели на 3D-принтере печатается хирургический шаблон с направляющими втулками, который обеспечивает позиционирование имплантов по заранее рассчитанной траектории.
                        </p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        03
                        <span>Операция</span>
                    </div>
                    <div class="step-card">
                        <h3>День операции: установка имплантов Alpha Dent</h3>
                        <p>
                            Под эффективной местной анестезией хирург Олег Швец атравматично удаляет остатки зубов и устанавливает 4 или 6 имплантов через шаблон. Процедура проходит комфортно, без острой боли; пациент ощущает лишь давление и прикосновения инструментов.
                        </p>
                    </div>
                </div>

                <!-- Step 4 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        04
                        <span>В тот же день</span>
                    </div>
                    <div class="step-card">
                        <h3>Фиксация несъемного протеза на балке</h3>
                        <p>
                            Врач-ортопед устанавливает мульти-юниты и фиксирует несъемный адаптационный протез на балке. Пациент возвращается домой с восстановленным зубным рядом и возможностью принимать мягкую пищу.
                        </p>
                    </div>
                </div>

                <!-- Step 5 -->
                <div class="timeline-step">
                    <div class="step-num-badge">
                        05
                        <span>Через 6-12 мес</span>
                    </div>
                    <div class="step-card">
                        <h3>Постоянное протезирование: Циркониевые зубы на балке (3 500 $)</h3>
                        <p>
                            После полного приживления имплантов по желанию пациента изготавливается постоянный монолитный мост из диоксида циркония на индивидуальной фрезерованной балке — надежная и эстетичная конструкция для долговременного использования.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 7: Surgeon & Team (E-E-A-T) -->
    <section class="section-py bg-light-alt" id="surgeon">
        <div class="container">
            <div class="doctor-highlight-box">
                <div class="doc-photo-wrap">
                    <picture>
                        <source srcset="../images/oleg.webp" type="image/webp">
                        <img src="../images/oleg.jpg" alt="Хирург-имплантолог Олег Швец — операции All-on-4 в Одессе" width="725" height="1024" loading="lazy">
                    </picture>
                </div>

                <div class="doc-info-content">
                    <span class="eyebrow-tag">Хирург-имплантолог</span>
                    <h3>Олег Швец</h3>
                    <div class="doc-title-role">Ведущий хирург-имплантолог Harmony Dental Clinic</div>
                    
                    <p class="doc-desc">
                        Специализируется на тотальной реабилитации зубного ряда, навигационной хирургии и работе по клиническим протоколам All-on-4 / All-on-6. Выполняет атравматичную установку имплантов с бережным отношением к мягким и костным тканям для прогнозируемого заживления.
                    </p>

                    <div class="doc-stats-row">
                        <div class="doc-stat-item">
                            <strong>10+ лет</strong>
                            <span>Хирургической практики</span>
                        </div>
                        <div class="doc-stat-item">
                            <strong>3D навигация</strong>
                            <span>Цифровое планирование</span>
                        </div>
                        <div class="doc-stat-item">
                            <strong>Международные</strong>
                            <span>Клинические протоколы</span>
                        </div>
                    </div>

                    <div style="display:flex; align-items:center; gap:16px;">
                        <picture>
                            <source srcset="../images/andrey.webp" type="image/webp">
                            <img src="../images/andrey.jpg" alt="Главный врач Андрей Малюкин" style="width:60px; height:60px; border-radius:50%; object-fit:cover; border:2px solid var(--primary);" width="725" height="1024" loading="lazy">
                        </picture>
                        <div style="font-size:14px; color:#445046;">
                            <strong>В тандеме с главным врачом Андреем Малюкиным</strong><br>
                            Ортопедическое моделирование прикуса и точная посадка несъемной конструкции.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 8: Technology & Comfort -->
    <section class="section-py">
        <div class="container">
            <div class="explainer-grid">
                <div>
                    <span class="eyebrow-tag">Цифровые стандарты</span>
                    <h2>Навигационная 3D-хирургия и комфортное лечение в Одессе</h2>
                    <p>
                        В Harmony Dental Clinic имплантация All-on-4 планируется цифровым методом с помощью 3D-шаблонов, что минимизирует хирургическую травму и сокращает время операции.
                    </p>
                    <ul class="explainer-list">
                        <li><strong>Точность позиционирования:</strong> шаблон направляет имплант строго на заданную глубину и под рассчитанным углом через направляющие втулки.</li>
                        <li><strong>Эффективная местная анестезия:</strong> мы используем проверенные европейские анестетики, которые надежно обезболивают операционное поле. Мы не применяем общий наркоз (сон) — процедура проходит в спокойной обстановке с сохранением полного сознания и контроля.</li>
                        <li><strong>Автономность:</strong> клиника на ул. Новаторов 1А оборудована генератором и резервным питанием для непрерывной работы медицинского оборудования.</li>
                    </ul>
                </div>

                <div class="explainer-media">
                    <picture>
                        <img src="../images/surgical-template.jpg" alt="3D хирургический навигационный шаблон для точного позиционирования имплантов All-on-4" width="1376" height="768" loading="lazy">
                    </picture>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 9: Clinical Cases Before / After -->
    <section class="section-py bg-light-alt">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Клинические примеры</span>
                <h2>Результаты тотальной имплантации челюсти До и После</h2>
                <p>
                    Примеры восстановления зубного ряда пациентов в Harmony Dental Clinic.
                </p>
            </div>

            <div class="cases-grid">
                <!-- Case 1 -->
                <div class="case-card">
                    <div class="case-imgs-split">
                        <div class="case-img-wrap">
                            <picture>
                                <source srcset="../images_implants/c1a.webp" type="image/webp">
                                <img src="../images_implants/c1a.jpg" alt="До имплантации: отсутствие зубов и разрушенный ряд" loading="lazy" width="725" height="483">
                            </picture>
                            <span class="case-badge">До</span>
                        </div>
                        <div class="case-img-wrap">
                            <picture>
                                <source srcset="../images_implants/c1b.webp" type="image/webp">
                                <img src="../images_implants/c1b.jpg" alt="После имплантации All-on-4: несъемный мост и ровные зубы" loading="lazy" width="725" height="483">
                            </picture>
                            <span class="case-badge" style="background:var(--primary);">После</span>
                        </div>
                    </div>
                    <div class="case-body">
                        <h3>Тотальная реабилитация верхней челюсти All-on-4</h3>
                        <p>Пациент 56 лет. Жалобы на невозможность пользоваться съемным протезом. Установлено 4 импланта Alpha Dent по навигационному шаблону с фиксацией несъемного протеза на балке в день операции.</p>
                    </div>
                </div>

                <!-- Case 2 -->
                <div class="case-card">
                    <div class="case-imgs-split">
                        <div class="case-img-wrap">
                            <picture>
                                <source srcset="../images_implants/c2a.webp" type="image/webp">
                                <img src="../images_implants/c2a.jpg" alt="До лечения: подвижность зубов и пародонтит" loading="lazy" width="725" height="483">
                            </picture>
                            <span class="case-badge">До</span>
                        </div>
                        <div class="case-img-wrap">
                            <picture>
                                <source srcset="../images_implants/c2b.webp" type="image/webp">
                                <img src="../images_implants/c2b.jpg" alt="После операции All-on-6: восстановленный несъемный зубной ряд" loading="lazy" width="725" height="483">
                            </picture>
                            <span class="case-badge" style="background:var(--primary);">После</span>
                        </div>
                    </div>
                    <div class="case-body">
                        <h3>Комплексное восстановление обеих челюстей All-on-6</h3>
                        <p>Пациентка 62 года. Генерализованный пародонтит тяжелой степени. Одномоментное удаление несостоятельных зубов и установка 6 имплантов на каждую челюсть с несъемным протезированием на балке.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 10: FAQ Section -->
    <section class="section-py" id="faq">
        <div class="container">
            <div class="section-header-center">
                <span class="eyebrow-tag">Ответы на вопросы</span>
                <h2>Частые вопросы об имплантации All-on-4 в Одессе</h2>
                <p>
                    Информация о проведении процедуры, обезболивании и послеоперационном уходе.
                </p>
            </div>

            <div style="max-width:850px; margin:0 auto;">
                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Сколько стоит имплантация All-on-4 под ключ в Одессе и из чего состоит цена?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            В Harmony Dental Clinic стоимость All-on-4 на немецких имплантах Alpha Dent составляет 2 400 $ за челюсть. Расчет прозрачный: 4 импланта Alpha Dent (4 × 350 $ = 1 400 $) + 4 мульти-юнит абатмента (4 × 50 $ = 200 $) + акриловый несъемный протез на балке (800 $). В стоимость также включено планирование, анестезия и контрольные осмотры.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Сколько стоит имплантация All-on-6 и когда она необходима?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            All-on-6 на имплантах Alpha Dent стоит 3 200 $: 6 имплантов (6 × 350 $ = 2 100 $) + 6 мульти-юнитов (6 × 50 $ = 300 $) + акриловый несъемный протез на балке (800 $). Шесть опор рекомендуются на верхней челюсти при более мягкой кости или при повышенной жевательной нагрузке.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Сколько стоят постоянные циркониевые зубы на балке через год?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            Через 6-12 месяцев после полного приживления имплантов по желанию пациента изготавливается постоянный монолитный мост из диоксида циркония на индивидуальной фрезерованной балке. Его стоимость составляет 3 500 $. Это прочный и эстетичный материал с высокой износостойкостью.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Как реализуется восстановление зубов по протоколу 1 дня?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            Благодаря протоколу немедленной нагрузки (Immediate Loading) хирург Олег Швец устанавливает 4 или 6 имплантов, а ортопед фиксирует адаптационный несъемный протез на балке в день операции. Пациент уходит домой с восстановленным зубным рядом.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Нужно ли наращивание кости (синус-лифтинг) при All-on-4?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            В большинстве случаев костная пластика и синус-лифтинг не требуются. Установка боковых имплантов под углом до 45° позволяет задействовать имеющийся объем кости в обход гайморовых пазух и нервов. Точная возможность определяется врачом по результатам 3D КТ.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Насколько комфортно проходит операция All-on-4?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            Процедура проходит под качественной современной местной анестезией, которая надежно обезболивает область операции. Острой боли во время вмешательства нет, ощущается лишь легкое давление и прикосновения инструментов. Мы не применяем общий наркоз (сон), так как местного обезболивания достаточно. После операции назначаются стандартные противовоспалительные и обезболивающие препараты для комфортного восстановления.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Чем несъемный протез на балке отличается от съемного протеза?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            Несъемный протез на балке надежно фиксируется винтами к мульти-юнитам и не смещается во время еды или разговора. Он не закрывает нёбо, сохраняет вкусовые ощущения и равномерно распределяет жевательную нагрузку на импланты.
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <div class="accordion-header" onclick="toggleAccordion(this)">
                        Какая гарантия предоставляется на работу и импланты?
                        <span>+</span>
                    </div>
                    <div class="accordion-content">
                        <div style="padding:20px 25px; line-height:1.7; color:#4a544c; border-top:1px solid #f2f5f2;">
                            На импланты действует официальная гарантия производителя Alpha Dent. Клиника предоставляет гарантию на выполненную хирургическую и ортопедическую работу в соответствии с медицинскими стандартами при условии соблюдения рекомендаций врача и регулярной гигиены 2 раза в год.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 11: Crosslink Banner back to Single Implants & Clinic Location -->
    <section class="section-py bg-light-alt" id="consultation">
        <div class="container">
            <div style="background:linear-gradient(135deg, #253328 0%, #162018 100%); border-radius:24px; padding:50px; color:#fff; display:grid; grid-template-columns:1.2fr 0.8fr; gap:40px; align-items:center;">
                <div>
                    <span style="color:#c49b66; font-weight:800; text-transform:uppercase; font-size:13px; letter-spacing:1px;">Запись на прием</span>
                    <h2 style="font-size:32px; font-weight:800; margin:10px 0 16px 0; color:#fff; line-height:1.2;">Запишитесь на 3D-диагностику и расчет лечения All-on-4</h2>
                    <p style="font-size:16px; color:rgba(255,255,255,0.85); line-height:1.6; margin-bottom:24px;">
                        Получите детальный персональный план лечения от хирурга Олега Швеца и ортопеда Андрея Малюкина в клинике на ул. Новаторов 1А (Одесса, Таирова).
                    </p>
                    <div style="display:flex; gap:15px; flex-wrap:wrap;">
                        <a href="tel:+380687794547" class="btn" style="background:#fff; color:#191f1a; padding:14px 28px; border-radius:12px; font-weight:800; text-decoration:none; display:inline-flex; align-items:center; gap:8px;"
                           onclick="return gtag_report_call('tel:+380687794547');">
                            📞 Позвонить +38 068 779 45 47
                        </a>
                        <a href="https://t.me/Harmonyclinic_od" target="_blank" class="btn" style="background:#229ED9; color:#fff; padding:14px 24px; border-radius:12px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:8px;">
                            Написать в Telegram
                        </a>
                        <a href="viber://chat?number=%2B380687794547" class="btn" style="background:#7360f2; color:#fff; padding:14px 24px; border-radius:12px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:8px;">
                            Написать в Viber
                        </a>
                    </div>
                </div>

                <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:18px; padding:30px;">
                    <h3 style="font-size:18px; margin-bottom:15px; color:#fff;">📍 Как нас найти</h3>
                    <p style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.6; margin-bottom:12px;">
                        <strong>Адрес:</strong> г. Одесса, ул. Новаторов 1А (Киевский район, ориентир — Таирова / Черемушки).
                    </p>
                    <p style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.6; margin-bottom:12px;">
                        <strong>График работы:</strong> Пн–Пт: 09:00 – 20:00, Сб: 10:00 – 16:00.
                    </p>
                    <p style="font-size:14px; color:rgba(255,255,255,0.85); line-height:1.6; margin-bottom:0;">
                        <strong>Нужен только один зуб?</strong><br>
                        <a href="implants-ua.html" style="color:#c49b66; text-decoration:underline;">Перейдите на страницу одиночной имплантации зубов →</a>
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer id="contacts" class="unified-footer" role="contentinfo">
        <div class="container">
            <div class="footer-content">
                <div>
                    <picture>
                        <source srcset="../images/Logo.webp" type="image/webp">
                        <img loading="lazy" src="../images/Logo.png" alt="Логотип Harmony Dental Clinic" class="footer-logo-img" width="1072" height="1071">
                    </picture>
                    <p style="margin-top:10px;">Современная семейная и цифровая стоматология в Одессе.</p>
                    <div class="social-icons">
                        <a href="viber://chat?number=%2B380687794547" title="Viber" aria-label="Viber"><svg viewBox="0 0 24 24">
                            <path d="M22.2,16.6c-0.2-0.6-1.3-1.2-2.1-1.4c-0.8-0.2-1.3-0.1-1.8,0.7c-0.5,0.7-1,1.4-1.6,1.4c-0.5,0-1.9-0.5-3.6-2c-1.3-1.2-2.3-2.6-2.5-3s-0.1-1,0.6-1.7c0.5-0.5,1.1-1.3,1.3-1.8c0.2-0.5,0.1-1,0.1-1.4S10.8,3.9,10.2,2.5C9.5,1.1,8.9,1.4,8.4,1.4c-0.5,0-1.4,0-2.2,0.8c-0.9,0.9-3.2,3.1-3.2,7.5c0,4.4,3.2,8.7,3.7,9.3c0.5,0.6,6.3,9.5,15.2,12.5c5.3,1.8,7.3,1.7,8.6,1.5c1.4-0.1,4.5-1.8,5.1-3.6C26.3,17.7,22.8,17.9,22.2,16.6z" />
                        </svg></a>
                        <a href="https://t.me/Harmonyclinic_od" target="_blank" title="Telegram" aria-label="Telegram"><svg viewBox="0 0 24 24">
                            <path d="M9.78,18.65l0.13-3.14l5.63-5.07c0.49-0.44-0.11-0.69-0.76-0.29L8.4,14.2l-3.03-0.95c-0.66-0.21-0.67-0.66,0.14-0.97L17.36,7.7c0.56-0.21,1.05,0.13,0.87,0.86L16.14,18.2c-0.12,0.59-0.87,0.72-1.41,0.45L9.78,18.65z" />
                        </svg></a>
                        <a href="https://www.instagram.com/harmony.dental.clinic.od/" target="_blank" title="Instagram" aria-label="Instagram"><svg viewBox="0 0 24 24">
                            <path d="M12,2.2c3.2,0,3.6,0,4.9,0.1c1.2,0.1,1.8,0.3,2.2,0.5c0.6,0.2,1,0.5,1.4,0.9c0.4,0.4,0.7,0.8,0.9,1.4c0.2,0.4,0.4,1.1,0.5,2.2c0.1,1.3,0.1,1.6,0.1,4.9s0,3.6-0.1,4.9c-0.1,1.2-0.3,1.8-0.5,2.2c-0.2,0.6-0.5,1-0.9,1.4c-0.4,0.4-0.8,0.7-1.4,0.9c-0.4,0.2-1.1,0.4-2.2,0.5C8.4,2.2,8.8,2.2,12,2.2 M12,0C8.7,0,8.3,0,7.1,0.1C5.8,0.1,4.9,0.3,4.1,0.6C3.4,0.9,2.7,1.3,2,2s-1.1,1.4-1.4,2.2C0.3,4.9,0.1,5.8,0.1,7.1C0,8.3,0,8.7,0,12s0,3.7,0.1,4.9c0.1,1.3,0.3,2.1,0.6,2.9c0.3,0.8,0.7,1.5,1.4,2.2c0.7,0.7,1.4,1.1,2.2,1.4c0.8,0.3,1.7,0.5,2.9,0.6c1.2,0.1,1.6,0.1,4.9,0.1s3.7,0,4.9-0.1c1.3-0.1,2.1-0.3,2.9-0.6c0.8-0.3,1.5-0.7,2.2-1.4c0.7-0.7,1.1-1.4,1.4-2.2c0.3-0.8,0.5-1.7,0.6-2.9c0.1-1.2,0.1-1.6,0.1-4.9s0-3.7-0.1-4.9c-0.1-1.3-0.3-2.1-0.6-2.9c-0.3-0.8-0.7-1.5-1.4-2.2c-0.7-0.7-1.4-1.1-2.2-1.4c-0.8-0.3-1.7-0.5-2.9-0.6C15.7,0,15.3,0,12,0z M12,5.8c-3.4,0-6.2,2.8-6.2,6.2c0,3.4,2.8,6.2,6.2,6.2s6.2-2.8,6.2-6.2C18.2,8.6,15.4,5.8,12,5.8z M12,16c-2.2,0-4-1.8-4-4s1.8-4,4-4s4,1.8,4,4S14.2,16,12,16z M18.4,4.2c-0.8,0-1.4,0.6-1.4,1.4s0.6,1.4,1.4,1.4s1.4-0.6,1.4-1.4S19.2,4.2,18.4,4.2z" />
                        </svg></a>
                    </div>
                </div>
                <div>
                    <h3>Меню</h3>
                    <div class="footer-links">
                        <a href="index.html#about">> О клинике</a>
                        <a href="services-ua.html">> Услуги</a>
                        <a href="index.html#prices">> Цены</a>
                        <a href="offer.html">> Оферта</a>
                    </div>
                </div>
                <div>
                    <h3>Услуги</h3>
                    <div class="footer-links">
                        <a href="implants-ua.html">> Имплантация</a>
                        <a href="all-on-4-odessa.html">> All-on-4 / All-on-6</a>
                        <a href="prosthetics-ua.html">> Протезирование</a>
                        <a href="lechenie-ua.html">> Лечение</a>
                        <a href="hygiene-ua.html">> Гигиена</a>
                        <a href="orthodontics-ua.html">> Ортодонтия</a>
                        <a href="extraction-ua.html">> Удаление</a>
                    </div>
                </div>
                <div>
                    <h3>Контакты</h3>
                    <p>📍 г. Одесса, ул. Новаторов 1А</p>
                    <p style="margin-top:10px;">
                        <a href="tel:+380687794547" aria-label="Позвонить" style="color:#fff; font-weight:700;"
                            onclick="if(typeof gtag_report_conversion==='function'){return gtag_report_conversion('tel:+380687794547');}">📞 +38 068 779 45 47</a>
                    </p>
                </div>
            </div>
            <div class="copyright">Copyright © 2026 Harmony Clinic. All Rights Reserved.</div>
        </div>
    </footer>

    <!-- Floating Call Button -->
    <a href="tel:+380687794547" aria-label="Позвонить" class="floating-widget"
        onclick="if(typeof gtag_report_conversion === 'function') { return gtag_report_conversion('tel:+380687794547'); } else if(typeof gtag_report_call === 'function') { return gtag_report_call('tel:+380687794547'); }">
        <div class="widget-icon">
            <svg viewBox="0 0 24 24">
                <path d="M22.2,16.6c-0.2-0.6-1.3-1.2-2.1-1.4c-0.8-0.2-1.3-0.1-1.8,0.7c-0.5,0.7-1,1.4-1.6,1.4c-0.5,0-1.9-0.5-3.6-2c-1.3-1.2-2.3-2.6-2.5-3s-0.1-1,0.6-1.7c0.5-0.5,1.1-1.3,1.3-1.8c0.2-0.5,0.1-1,0.1-1.4S10.8,3.9,10.2,2.5C9.5,1.1,8.9,1.4,8.4,1.4c-0.5,0-1.4,0-2.2,0.8c-0.9,0.9-3.2,3.1-3.2,7.5c0,4.4,3.2,8.7,3.7,9.3c0.5,0.6,6.3,9.5,15.2,12.5c5.3,1.8,7.3,1.7,8.6,1.5c1.4-0.1,4.5-1.8,5.1-3.6C26.3,17.7,22.8,17.9,22.2,16.6z" />
            </svg>
        </div>
    </a>

    <script src="../header.js" defer></script>
    <script src="../mobile-menu.js" defer></script>
    <script>
    function switchPricingTab(tabKey, btn) {
        document.querySelectorAll('.pricing-tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.pricing-content-panel').forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        const targetPanel = document.getElementById('tab-panel-' + tabKey);
        if (targetPanel) {
            targetPanel.classList.add('active');
        }
    }

    function toggleAccordion(el){
        const c = el.nextElementSibling;
        const s = el.querySelector('span');
        if (c.style.maxHeight){
            c.style.maxHeight = null;
            s.textContent = "+";
        } else {
            c.style.maxHeight = c.scrollHeight + "px";
            s.textContent = "−";
        }
    }
    </script>
</body>

</html>
"""

def main():
    root = "/Users/doc/Desktop/Сайт"
    ua_path = os.path.join(root, "Harmony Dental Clinic", "all-on-4-odessa.html")
    ru_path = os.path.join(root, "Harmony Dental Clinic", "ru", "all-on-4-odessa.html")

    with open(ua_path, "w", encoding="utf-8") as f:
        f.write(get_ua_html())
    print("Updated:", ua_path)

    with open(ru_path, "w", encoding="utf-8") as f:
        f.write(get_ru_html())
    print("Updated:", ru_path)

if __name__ == "__main__":
    main()
