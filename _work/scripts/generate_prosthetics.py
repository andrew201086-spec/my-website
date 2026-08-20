#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for Dental Prosthetics landing pages:
- /Users/doc/Desktop/Сайт/Harmony Dental Clinic/prosthetics-ua.html (Ukrainian)
- /Users/doc/Desktop/Сайт/Harmony Dental Clinic/ru/prosthetics-ua.html (Russian)

Key Directives:
- NO microscope mentions.
- NO general anesthesia / sleep / sedation mentions.
- NO inlays / onlays / overlays / вкладки / накладки (per Dr. Andrei Malyukin directive).
- NO populist marketing fluff ("100% цифровий", "без болю", "довічна гарантія", "3000+ зубів").
- Doctor: Andrei Malyukin (sole featured orthopedist, Founder & Chief Doctor, 15+ years exp).
- Equipment: 3Shape TRIOS 4 digital intraoral scanner, CAD/CAM exocad modeling.
- Core Web Vitals optimization: Deferred analytics loader (GA4, GTM, FB Pixel).
- Complete Schema.org @graph (Dentist, Physician, MedicalProcedure, OfferCatalog, FAQPage, BreadcrumbList).
- High-resolution anatomical infographic: "Crown on natural tooth vs Crown on implant".
- Fixed Hero section: .prosthetics-hero with dark luxury emerald gradient for 100% readability.
"""

import os
import json

def get_html(lang='ua'):
    is_ua = (lang == 'ua')
    
    # Path prefixes
    img_pfx = "" if is_ua else "../"
    root_pfx = "" if is_ua else "../"
    lang_code = "uk" if is_ua else "ru"
    canonical_url = "https://harmonyclinic.od.ua/prosthetics-ua.html" if is_ua else "https://harmonyclinic.od.ua/ru/prosthetics-ua.html"
    
    # Navigation links
    home_link = "index.html"
    services_link = "services-ua.html"
    implants_link = "implants-ua.html"
    prosthetics_link = "prosthetics-ua.html"
    treatment_link = "lechenie-ua.html"
    hygiene_link = "hygiene-ua.html"
    whitening_link = "otbilyuvannya-ua.html"
    ortho_link = "orthodontics-ua.html"
    extraction_link = "extraction-ua.html"
    all_on_4_link = "all-on-4-odessa.html"
    blog_link = "blog.html"
    doctor_link = "maliukin-andriy.html"
    
    # Language switcher URL
    other_lang_url = "ru/prosthetics-ua.html" if is_ua else "../prosthetics-ua.html"
    other_lang_label = "RU" if is_ua else "UA"
    current_lang_label = "UA" if is_ua else "RU"

    # Texts
    t_title = "Протезування зубів в Одесі — коронки, вініри, мости | Ціни Harmony Clinic" if is_ua else "Протезирование зубов в Одессе — коронки, виниры, мосты | Цены Harmony Clinic"
    t_desc = "Протезування зубів в Одесі на Таїрова: цирконієві коронки, кераміка E-max, мостоподібні протези та коронки на імплантах. 3D-сканер 3Shape без зліпків. ☎ Запис!" if is_ua else "Протезирование зубов в Одессе на Таирова: циркониевые коронки, керамика E-max, мостовидные протезы и коронки на имплантах. 3D-сканер 3Shape без слепков. ☎ Запись!"
    
    t_og_title = "Протезування зубів в Одесі — коронки, вініри, мости | Harmony Clinic" if is_ua else "Протезирование зубов в Одессе — коронки, виниры, мосты | Harmony Clinic"
    t_og_desc = "Цифрове 3D-протезування: цирконій Multi-layer, кераміка E-max, мости та протези на імплантах. Без зліпків завдяки сканеру 3Shape TRIOS 4." if is_ua else "Цифровое 3D-протезирование: цирконий Multi-layer, керамика E-max, мосты и протезы на имплантах. Без слепков благодаря сканеру 3Shape TRIOS 4."

    # Hero texts
    h_pre = "Протезування зубів в Одесі · Таїрова / Черемушки" if is_ua else "Протезирование зубов в Одессе · Таирова / Черемушки"
    h_h1 = "Протезування зубів в Одесі: коронки, вініри, мости та протези на імплантах" if is_ua else "Протезирование зубов в Одессе: коронки, виниры, мосты и протезы на имплантах"
    h_sub = "Цифрове 3D-сканування 3Shape TRIOS 4 замість зліпочних мас. Індивідуальне моделювання анатомії зуба та узгодження форми посмішки до початку роботи." if is_ua else "Цифровое 3D-сканирование 3Shape TRIOS 4 вместо слепочных масс. Индивидуальное моделирование анатомии зуба и согласование формы улыбки до начала работы."
    
    b_1 = "Комфортне сканування без нудоти та зліпків" if is_ua else "Комфортное сканирование без тошноты и слепков"
    b_2 = "Узгодження форми та кольору зубів до початку роботи" if is_ua else "Согласование формы и цвета зубов до начала работы"
    b_3 = "Цирконій Multi-layer та прес-кераміка E-max — термін служби 10–15+ років" if is_ua else "Цирконий Multi-layer и пресс-керамика E-max — срок службы 10–15+ лет"
    b_btn = "Записатися на консультацію" if is_ua else "Записаться на консультацию"

    # Services texts
    srv_h2 = "Види ортопедичного відновлення зубів" if is_ua else "Виды ортопедического восстановления зубов"
    srv_sub = "Підбираємо конструкцію під ваш клінічний випадок: від одиночної естетичної коронки до повного відновлення зубного ряду" if is_ua else "Подбираем конструкцию под ваш клинический случай: от одиночной эстетической коронки до полного восстановления зубного ряда"

    # Features / Tech section
    tech_h2 = "Стандарти цифрового протезування в Harmony Clinic" if is_ua else "Стандарты цифрового протезирования в Harmony Clinic"
    
    # Anatomy Infographic section
    anatomy_h2 = "Будова коронки: на власному зубі vs на імпланті" if is_ua else "Строение коронки: на своем зубе vs на импланте"
    anatomy_sub = "Наочна анатомічна схема фіксації ортопедичної коронки при збереженому власному корені та при повній заміні зуба імплантом" if is_ua else "Наглядная анатомическая схема фиксации ортопедической коронки при сохраненном своем корне и при полной замене зуба имплантом"
    anatomy_alt = "Схема будови коронки на власному корені зуба та коронки на дентальному імпланті" if is_ua else "Схема строения коронки на собственном корне зуба и коронки на дентальном импланте"

    # Comparison table
    comp_h2 = "Який матеріал коронки обрати?" if is_ua else "Какой материал коронки выбрать?"

    # Cases
    cases_h2 = "Результати протезування: До / Після" if is_ua else "Результаты протезирования: До / После"
    cases_sub = "Реальні клінічні випадки відновлення зубів коронками, вінірами та мостоподібними конструкціями" if is_ua else "Реальные клинические случаи восстановления зубов коронками, винирами и мостовидными конструкциями"

    # Pricing
    price_h2 = "Ціни на протезування зубів" if is_ua else "Цены на протезирование зубов"
    price_sub = "Фіксована вартість «під ключ» без прихованих платежів: включає 3D-сканування, виготовлення, примірку та фіксацію" if is_ua else "Фиксированная стоимость «под ключ» без скрытых платежей: включает 3D-сканирование, изготовление, примерку и фиксацию"

    # Stages
    stages_h2 = "Етапи протезування зубів" if is_ua else "Этапы протезирования зубов"
    stages_sub = "5 чітких кроків від первинного 3D-сканування до фіксації постійної конструкції" if is_ua else "5 четких шагов от первичного 3D-сканирования до фиксации постоянной конструкции"

    # Doctor
    doc_h2 = "Хто виконує ваше протезування" if is_ua else "Кто выполнит ваше протезирование"
    doc_name = "Малюкін Андрій Віталійович" if is_ua else "Малюкин Андрей Витальевич"
    doc_role = "Стоматолог-ортопед · Засновник і головний лікар Harmony Clinic" if is_ua else "Стоматолог-ортопед · Основатель и главный врач Harmony Clinic"
    doc_desc = "Спеціалізується на естетичному та функціональному протезуванні за цифровим CAD/CAM протоколом. Особисто проводить 3D-сканування, моделювання та фінішну фіксацію коронок, вінірів та протезів на імплантах." if is_ua else "Специализируется на эстетическом и функциональном протезировании по цифровому CAD/CAM протоколу. Лично проводит 3D-сканирование, моделирование и финишную фиксацию коронок, виниров и протезов на имплантах."

    # FAQ
    faq_h2 = "Часті запитання щодо протезування" if is_ua else "Частые вопросы о протезировании"
    
    # Location
    loc_h2 = "Наша локація в Одесі" if is_ua else "Наша локация в Одессе"

    # JSON-LD Schema objects
    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Dentist",
                "@id": "https://harmonyclinic.od.ua/#org",
                "name": "Harmony Clinic",
                "image": "https://harmonyclinic.od.ua/images/Logo.png",
                "url": canonical_url,
                "telephone": "+380687794547",
                "priceRange": "$$",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "вул. Новаторів, 1А" if is_ua else "ул. Новаторов, 1А",
                    "addressLocality": "Одеса" if is_ua else "Одесса",
                    "addressRegion": "Одеська область" if is_ua else "Одесская область",
                    "postalCode": "65114",
                    "addressCountry": "UA"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 46.4089,
                    "longitude": 30.7185
                },
                "openingHoursSpecification": [
                    {
                        "@type": "OpeningHoursSpecification",
                        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                        "opens": "09:00",
                        "closes": "19:00"
                    }
                ],
                "areaServed": [
                    {"@type": "City", "name": "Одеса" if is_ua else "Одесса"},
                    {"@type": "Place", "name": "Таїрова" if is_ua else "Таирова"},
                    {"@type": "Place", "name": "Черемушки" if is_ua else "Черемушки"},
                    {"@type": "AdministrativeArea", "name": "Київський район" if is_ua else "Киевский район"}
                ]
            },
            {
                "@type": "Physician",
                "@id": "https://harmonyclinic.od.ua/#malyukin",
                "name": doc_name,
                "jobTitle": "Головний лікар, стоматолог-ортопед" if is_ua else "Главный врач, стоматолог-ортопед",
                "image": "https://harmonyclinic.od.ua/images/andrey.jpg",
                "worksFor": {"@id": "https://harmonyclinic.od.ua/#org"},
                "medicalSpecialty": "Dentistry",
                "description": "Спеціаліст із цифрового протезування (CAD/CAM, 3Shape TRIOS 4), естетичної реставрації керамікою E-max, цирконієвими коронками та протезування на імплантах з досвідом понад 15 років." if is_ua else "Специалист по цифровому протезированию (CAD/CAM, 3Shape TRIOS 4), эстетической реставрации керамикой E-max, циркониевыми коронками и протезированию на имплантах с опытом более 15 лет."
            },
            {
                "@type": "MedicalProcedure",
                "@id": f"{canonical_url}#procedure",
                "name": "Протезування зубів в Одесі" if is_ua else "Протезирование зубов в Одессе",
                "procedureType": "https://schema.org/TherapeuticProcedure",
                "bodyLocation": "Зуби та щелепа" if is_ua else "Зубы и челюсть",
                "howPerformed": "Встановлення коронок із діоксиду цирконію та кераміки E-max, мостоподібних протезів, коронок на імплантах та знімних конструкцій за цифровим протоколом 3Shape TRIOS 4." if is_ua else "Установка коронок из диоксида циркония и керамики E-max, мостовидных протезов, коронок на имплантах и съемных конструкций по цифровому протоколу 3Shape TRIOS 4.",
                "performer": {"@id": "https://harmonyclinic.od.ua/#malyukin"}
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Головна" if is_ua else "Главная",
                        "item": "https://harmonyclinic.od.ua/" if is_ua else "https://harmonyclinic.od.ua/ru/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Послуги" if is_ua else "Услуги",
                        "item": "https://harmonyclinic.od.ua/services-ua.html" if is_ua else "https://harmonyclinic.od.ua/ru/services-ua.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": "Протезування" if is_ua else "Протезирование",
                        "item": canonical_url
                    }
                ]
            },
            {
                "@type": "OfferCatalog",
                "name": "Прайс-лист на протезування зубів" if is_ua else "Прайс-лист на протезирование зубов",
                "itemListElement": [
                    {
                        "@type": "Offer",
                        "name": "Первинна консультація стоматолога-ортопеда + фотопротокол" if is_ua else "Первичная консультация стоматолога-ортопеда + фотопротокол",
                        "price": "0",
                        "priceCurrency": "UAH",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Металокерамічна коронка" if is_ua else "Металлокерамическая коронка",
                        "price": "110",
                        "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Цирконієва коронка на боковий (жувальний) зуб" if is_ua else "Циркониевая коронка на боковой (жевательный) зуб",
                        "price": "170",
                        "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Цирконієва коронка Multi-layer на передній зуб" if is_ua else "Циркониевая коронка Multi-layer на передний зуб",
                        "price": "300",
                        "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Керамічна коронка / вінір E-max" if is_ua else "Керамическая коронка / винир E-max",
                        "price": "300",
                        "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Коронка з цирконію на імплантаті" if is_ua else "Коронка из циркония на имплантате",
                        "price": "250",
                        "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Тимчасова естетична коронка (PMMA)" if is_ua else "Временная эстетическая коронка (PMMA)",
                        "price": "2000",
                        "priceCurrency": "UAH",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Акриловий знімний протез" if is_ua else "Акриловый съемный протез",
                        "price": "8500",
                        "priceCurrency": "UAH",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Нейлоновий протез" if is_ua else "Нейлоновый протез",
                        "price": "12000",
                        "priceCurrency": "UAH",
                        "availability": "https://schema.org/InStock"
                    },
                    {
                        "@type": "Offer",
                        "name": "Бюгельний протез на кламерах або замках" if is_ua else "Бюгельный протез на кламмерах или замках",
                        "price": "500",
                        "priceCurrency": "USD",
                        "availability": "https://schema.org/InStock"
                    }
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "Чи обов'язково видаляти нерв перед встановленням коронки?" if is_ua else "Обязательно ли удалять нерв перед установкой коронки?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Ні. Сучасний цифровий протокол та робота з безметалевою керамікою (цирконій, E-max) дозволяють зберігати зуб живим. Ми проводимо щадне препарування з водним охолодженням і знімаємо мінімальний шар емалі. Депульпування проводиться виключно за прямими клінічними показаннями (глибокий карієс із ураженням пульпи або запалення)." if is_ua else "Нет. Современный цифровой протокол и работа с безметалловой керамикой (цирконий, E-max) позволяют сохранять зуб живым. Мы проводим щадящее препарирование с обильным водяным охлаждением и снимаем минимальный слой эмали. Депульпирование проводится исключительно по прямым клиническим показаниям (глубокий кариес с поражением пульпы или воспаление)."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Чим діоксид цирконію відрізняється від кераміки E-max та металокераміки?" if is_ua else "Чем диоксид циркония отличается от керамики E-max и металлокерамики?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Цирконій має найвищу міцність (до 1200 МПа) та біосумісність, тому ідеально підходить для жувальних зубів, мостів та коронок на імплантах. Кераміка E-max (дисилікат літію) має неперевершену світлопроникність і максимально повторює оптичні властивості живої емалі — це найкращий вибір для фронтальних зубів та вінірів. Металокераміка має металевий каркас, через що з часом може з'являтися темна смужка біля ясен." if is_ua else "Цирконий обладает максимальной прочностью (до 1200 МПа) и биосовместимостью, поэтому идеально подходит для жевательных зубов, мостов и коронок на имплантах. Керамика E-max (дисиликат лития) обладает непревзойденной светопроницаемостью и максимально повторяет оптику живой эмали — это лучший выбор для передних зубов и виниров. Металлокерамика имеет металлический каркас, из-за чего со временем может появляться темная полоска у десны."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Чи буде видно темний край коронки біля ясен?" if is_ua else "Будет ли виден темный край коронки возле десны?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "При встановленні цирконієвих коронок та кераміки E-max темний край неможливий, оскільки в матеріалах повністю відсутній метал. Коронка препарується з круговим уступом, завдяки чому край конструкції плавно ховається під ясенний контур, а ясна зберігають природний рожевий колір." if is_ua else "При установке циркониевых коронок и керамики E-max темный край невозможен, так как в материалах полностью отсутствует металл. Коронка препарируется с круговым уступом, благодаря чему край конструкции плавно прячется под десневой контур, а десна сохраняет естественный розовый цвет."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Що краще при відсутності одного зуба: мостоподібний протез чи імплант?" if is_ua else "Что лучше при отсутствии одного зуба: мостовидный протез или имплант?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Імплантація — це золотий стандарт сучасної стоматології, оскільки вона дозволяє відновити втрачений зуб без обточування сусідніх здорових зубів та запобігає атрофії кістки. Мостоподібний протез є надійною альтернативою, якщо сусідні зуби вже мають великі пломби або коли імплантація тимчасово протипоказана." if is_ua else "Имплантация — это золотой стандарт современной стоматологии, так как она позволяет восстановить утраченный зуб без обточки соседних здоровых зубов и предотвращает атрофию кости. Мостовидный протез является надежной альтернативой, если соседние зубы уже имеют большие пломбы или когда имплантация временно противопоказана."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Скільки часу займає виготовлення коронки або моста?" if is_ua else "Сколько времени занимает изготовление коронки или моста?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Завдяки цифровому скануванню 3Shape TRIOS 4 та лабораторному CAD/CAM моделюванню виготовлення постійної коронки займає 5–7 робочих днів. На цей період пацієнту одразу встановлюється тимчасова естетична коронка, яка захищає зуб від температурних подразників та відновлює естетику." if is_ua else "Благодаря цифровому сканированию 3Shape TRIOS 4 и лабораторному CAD/CAM моделированию изготовление постоянной коронки занимает 5–7 рабочих дней. На этот период пациенту сразу устанавливается временная эстетическая коронка, которая защищает зуб от температурных раздражителей и восстанавливает эстетику."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Чи боляче обточувати зуби під коронку?" if is_ua else "Больно ли обтачивать зубы под коронку?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Процедура проходить абсолютно комфортно. Ми використовуємо сучасні карпульні анестетики артикаїнового ряду, які повністю блокують больову чутливість. Для депульпованих зубів процедура взагалі безболісна." if is_ua else "Процедура проходит абсолютно комфортно. Мы используем современные карпульные анестетики артикаинового ряда, которые полностью блокируют болевую чувствительность. Для депульпированных зубов процедура полностью безболезненна."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Що входить у ціну коронки «під ключ»?" if is_ua else "Что входит в стоимость коронки «под ключ»?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "У вартість, зазначену у прайсі, включено повний комплекс робіт: цифрове 3D-сканування 3Shape, виготовлення коронки в зуботехнічній лабораторії, примірка, корекція по прикусу та остаточна фіксація на адгезивний цемент. Якщо потрібне попереднє лікування каналів або відновлення кукси зуба штифтом, це розраховується окремо після огляду." if is_ua else "В стоимость, указанную в прайсе, включен полный комплекс работ: цифровое 3D-сканирование 3Shape, изготовление коронки в зуботехнической лаборатории, примерка, коррекция по прикусу и окончательная фиксация на адгезивный цемент. Если требуется предварительное лечение каналов или восстановление культи зуба штифтом, это рассчитывается отдельно после осмотра."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Який термін служби цирконієвих та керамічних коронок?" if is_ua else "Какой срок службы циркониевых и керамических коронок?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "При регулярній домашній гігієні та профілактичному чищенні кожні 6 місяців цирконієві коронки служать 10–15+ років. Матеріал не стирається, не вбирає харчові барвники і не втрачає первинного блиску." if is_ua else "При регулярной домашней гигиене и профилактической чистке каждые 6 месяцев циркониевые коронки служат 10–15+ лет. Материал не истирается, не впитывает пищевые красители и не теряет первоначального блеска."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Чи можна ставити коронки при бруксизмі (стисканні зубів)?" if is_ua else "Можно ли ставить коронки при бруксизме (сжатии зубов)?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Так. Для пацієнтів із підвищеною стираністю та бруксизмом найкращим вибором є монолітний діоксид цирконію. Він має екстремальну міцність до механічних навантажень. Додатково після протезування ми виготовляємо індивідуальну нічну захисну капу." if is_ua else "Да. Для пациентов с повышенной стираемостью и бруксизмом лучшим выбором является монолитный диоксид циркония. Он обладает экстремальной прочностью к механическим нагрузкам. Дополнительно после протезирования мы изготавливаем индивидуальную ночную защитную каппу."
                        }
                    }
                ]
            }
        ]
    }

    schema_json = json.dumps(schema_graph, ensure_ascii=False, indent=4)

    # HTML string construction
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">

<head>
    <meta charset="UTF-8">
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','GTM-PBZF8G5B');</script>
    <!-- End Google Tag Manager -->

    <!-- Deferred Analytics Loader for Core Web Vitals Optimization -->
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());

        let analyticsLoaded = false;
        function loadAnalytics() {{
            if (analyticsLoaded) return;
            analyticsLoaded = true;

            var gaScript = document.createElement('script');
            gaScript.async = true;
            gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-6ZP07STZJF';
            document.head.appendChild(gaScript);

            gaScript.onload = function() {{
                gtag('config', 'G-6ZP07STZJF');
                gtag('config', 'AW-11468618731');
            }};

            !function(f,b,e,v,n,t,s)
            {{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
            n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
            if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
            n.queue=[];t=b.createElement(e);t.async=!0;
            t.src=v;s=b.getElementsByTagName(e)[0];
            s.parentNode.insertBefore(t,s)}}(window, document,'script',
            'https://connect.facebook.net/en_US/fbevents.js');
            fbq('init', '451786880568879');
            fbq('track', 'PageView');
        }}

        ['scroll', 'touchstart', 'click', 'pointermove'].forEach(function(e) {{
            window.addEventListener(e, loadAnalytics, {{ once: true, passive: true }});
        }});
        setTimeout(loadAnalytics, 3500);

        function gtag_report_call(url) {{
            if (typeof gtag === 'function') {{
                gtag('event', 'conversion', {{
                    'send_to': 'AW-11468618731/s-heCPmCmt0bEOv31Nwq',
                    'event_callback': function() {{ if (url) window.location = url; }}
                }});
            }}
            return true;
        }}

        function gtag_report_messenger(url) {{
            if (typeof gtag === 'function') {{
                gtag('event', 'conversion', {{
                    'send_to': 'AW-11468618731/s-heCPmCmt0bEOv31Nwq',
                    'event_callback': function() {{ if (url) window.location = url; }}
                }});
            }}
            return true;
        }}
    </script>

    <link rel="canonical" href="{canonical_url}">
    <link rel="alternate" hreflang="uk-UA" href="https://harmonyclinic.od.ua/prosthetics-ua.html">
    <link rel="alternate" hreflang="ru-UA" href="https://harmonyclinic.od.ua/ru/prosthetics-ua.html">
    <link rel="alternate" hreflang="x-default" href="https://harmonyclinic.od.ua/prosthetics-ua.html">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t_title}</title>
    <meta name="description" content="{t_desc}">

    <link rel="icon" type="image/png" href="{img_pfx}images/Logo.png">

    <!-- Open Graph / Social -->
    <meta property="og:type" content="website">
    <meta property="og:locale" content="{ 'uk_UA' if is_ua else 'ru_UA' }">
    <meta property="og:title" content="{t_og_title}">
    <meta property="og:description" content="{t_og_desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:image" content="https://harmonyclinic.od.ua/images-coron/prosthetics-case1-after.jpg">
    <meta property="og:site_name" content="Harmony Clinic">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{t_og_title}">
    <meta name="twitter:description" content="{t_og_desc}">
    <meta name="twitter:image" content="https://harmonyclinic.od.ua/images-coron/prosthetics-case1-after.jpg">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{root_pfx}styles.css">

    <!-- Structured Data Schema.org Graph -->
    <script type="application/ld+json">
{schema_json}
    </script>

    <style>
        :root {{
            --header-bg: #000000;
            --header-text: #ffffff;
            --primary: #526154;
            --primary-dark: #3c493d;
            --text-dark: #1a1a1a;
            --text-grey: #666666;
            --bg-light: #faf9f6;
            --border: rgba(82, 97, 84, 0.15);
            --radius: 20px;
            --radius-btn: 100px;
            --gold: #c5a059;
            --font-heading: 'Manrope', sans-serif;
            --font-body: 'Manrope', sans-serif;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: var(--font-body);
            color: var(--text-dark);
            background-color: var(--bg-light);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        .container {{
            max-width: 1140px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        h1, h2, h3, h4 {{
            font-family: var(--font-heading);
            letter-spacing: -0.01em;
        }}

        .section-title {{
            font-size: clamp(28px, 4vw, 40px);
            font-weight: 700;
            text-align: center;
            margin-bottom: 15px;
            color: var(--text-dark);
        }}

        .section-subtitle {{
            text-align: center;
            max-width: 760px;
            margin: 0 auto 50px;
            color: var(--text-grey);
            font-size: 16px;
        }}

        /* Buttons */
        .btn-primary {{
            background: var(--primary);
            color: #fff !important;
            padding: 16px 36px;
            border-radius: var(--radius-btn);
            font-weight: 700;
            font-size: 15px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(82, 97, 84, 0.25);
            text-decoration: none;
        }}

        .btn-primary:hover {{
            background: var(--primary-dark);
            transform: translateY(-2px);
            box-shadow: 0 12px 25px rgba(82, 97, 84, 0.35);
        }}

        .btn-outline {{
            background: transparent !important;
            color: var(--primary) !important;
            border: 2px solid var(--primary) !important;
            padding: 14px 32px;
            border-radius: var(--radius-btn);
            font-weight: 700;
            font-size: 15px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            transition: all 0.3s ease;
        }}

        .btn-outline:hover {{
            background: var(--primary) !important;
            color: #fff !important;
        }}

        /* Header */
        header {{
            background-color: var(--header-bg);
            color: var(--header-text);
            padding: 14px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #222;
        }}

        .nav-wrapper {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .logo img {{
            height: auto;
            max-height: 52px;
            filter: brightness(0) invert(1);
        }}

        .nav-menu {{
            display: flex;
            gap: 18px;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            list-style: none;
        }}

        .nav-menu a {{
            color: #ffffff;
            transition: color 0.2s;
        }}

        .nav-menu a:hover {{
            color: #c5a059;
        }}

        .lang-switch {{
            color: #fff;
            font-weight: 700;
            font-size: 12px;
            padding: 5px 10px;
            border: 1px solid rgba(255,255,255,0.4);
            border-radius: 4px;
            text-decoration: none;
            transition: 0.2s;
        }}

        .lang-switch:hover {{
            background: #fff;
            color: #000;
        }}

        .header-phone {{
            color: #fff;
            font-weight: 700;
            border: 1px solid #fff;
            padding: 8px 16px;
            border-radius: 4px;
            font-size: 13px;
            text-decoration: none;
        }}

        .mobile-toggle {{
            display: none;
            font-size: 26px;
            cursor: pointer;
            color: #fff;
        }}

        /* Breadcrumbs */
        .breadcrumbs {{
            padding: 16px 0;
            font-size: 13px;
            color: var(--text-grey);
        }}

        .breadcrumbs a {{
            color: var(--primary);
            text-decoration: none;
        }}

        .breadcrumbs span {{
            margin: 0 8px;
            opacity: 0.5;
        }}

        /* Custom Prosthetics Hero Section (100% Readable Emerald Luxury Gradient) */
        .prosthetics-hero {{
            position: relative;
            padding: 70px 0 80px;
            min-height: 60vh;
            display: flex;
            align-items: center;
            background: radial-gradient(circle at 80% 20%, rgba(82, 97, 84, 0.45) 0%, transparent 65%),
                        linear-gradient(135deg, #111a14 0%, #060a07 100%) !important;
            background-image: radial-gradient(circle at 80% 20%, rgba(82, 97, 84, 0.45) 0%, transparent 65%),
                        linear-gradient(135deg, #111a14 0%, #060a07 100%) !important;
            color: #ffffff !important;
            overflow: hidden;
        }}

        .prosthetics-hero .hero-grid {{
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 45px;
            align-items: center;
            position: relative;
            z-index: 2;
            width: 100%;
        }}

        .prosthetics-hero .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.1);
            color: #e2e8e3;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 6px 14px;
            border-radius: 100px;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 18px;
            backdrop-filter: blur(8px);
        }}

        .prosthetics-hero .hero-pretitle {{
            font-weight: 700;
            color: #c5a059;
            font-size: 15px;
            margin-bottom: 8px;
            letter-spacing: 0.02em;
        }}

        .prosthetics-hero h1 {{
            font-size: clamp(28px, 3.6vw, 44px);
            line-height: 1.2;
            font-weight: 800;
            margin-bottom: 18px;
            color: #ffffff !important;
            letter-spacing: -0.02em;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}

        .prosthetics-hero .sub-headline {{
            font-size: 16.5px;
            color: rgba(255, 255, 255, 0.88) !important;
            margin-bottom: 26px;
            display: block;
            line-height: 1.6;
        }}

        .prosthetics-hero .hero-benefits {{
            margin-bottom: 32px;
        }}

        .prosthetics-hero .hero-benefits ul {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}

        .prosthetics-hero .hero-benefits li {{
            position: relative;
            padding-left: 28px;
            margin-bottom: 12px;
            font-size: 15px;
            font-weight: 500;
            color: rgba(255, 255, 255, 0.95) !important;
        }}

        .prosthetics-hero .hero-benefits li::before {{
            content: "✓";
            position: absolute;
            left: 0;
            top: 0;
            color: #c5a059;
            font-weight: 800;
            font-size: 16px;
        }}

        .prosthetics-hero .hero-actions {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .prosthetics-hero .btn-primary {{
            background: var(--primary);
            color: #fff !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
        }}

        .prosthetics-hero .btn-primary:hover {{
            background: #627464;
            transform: translateY(-2px);
        }}

        .prosthetics-hero .btn-outline {{
            background: transparent !important;
            color: #ffffff !important;
            border: 2px solid rgba(255, 255, 255, 0.5) !important;
            padding: 14px 32px;
            border-radius: var(--radius-btn);
            font-weight: 700;
            font-size: 15px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            transition: all 0.3s ease;
        }}

        .prosthetics-hero .btn-outline:hover {{
            background: rgba(255, 255, 255, 0.15) !important;
            border-color: #ffffff !important;
            color: #ffffff !important;
        }}

        .prosthetics-hero .hero-image-card {{
            position: relative;
            background: #19241c;
            padding: 12px;
            border-radius: var(--radius);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.15);
        }}

        .prosthetics-hero .hero-image-card img {{
            width: 100%;
            height: auto;
            border-radius: calc(var(--radius) - 6px);
            display: block;
            object-fit: cover;
            aspect-ratio: 4/5;
        }}

        .prosthetics-hero .hero-image-badge {{
            position: absolute;
            bottom: 25px;
            left: 25px;
            right: 25px;
            background: rgba(12, 18, 14, 0.88);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 14px 18px;
            border-radius: 14px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            font-size: 13px;
            color: #ffffff;
        }}

        .prosthetics-hero .hero-image-badge strong {{
            display: block;
            color: #c5a059;
            font-size: 15px;
        }}

        /* Services Grid */
        .services-section {{
            padding: 70px 0;
            background: #fff;
        }}

        .services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 24px;
        }}

        .service-card {{
            background: var(--bg-light);
            border-radius: var(--radius);
            padding: 30px;
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.3s ease;
        }}

        .service-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.08);
            border-color: var(--primary);
        }}

        .service-card-tag {{
            font-size: 11px;
            text-transform: uppercase;
            font-weight: 800;
            letter-spacing: 0.05em;
            color: var(--primary);
            background: rgba(82, 97, 84, 0.1);
            padding: 4px 10px;
            border-radius: 6px;
            align-self: flex-start;
            margin-bottom: 14px;
        }}

        .service-card h3 {{
            font-size: 20px;
            margin-bottom: 12px;
            color: var(--text-dark);
        }}

        .service-card p {{
            font-size: 14px;
            color: var(--text-grey);
            margin-bottom: 20px;
            line-height: 1.6;
        }}

        .service-card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 18px;
            border-top: 1px solid rgba(82, 97, 84, 0.1);
            margin-top: auto;
        }}

        .service-price {{
            font-size: 18px;
            font-weight: 800;
            color: var(--primary-dark);
        }}

        /* Standards Section */
        .tech-section {{
            padding: 80px 0;
            background: var(--bg-light);
        }}

        .tech-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 24px;
        }}

        .tech-card {{
            background: #fff;
            padding: 30px;
            border-radius: var(--radius);
            border: 1px solid var(--border);
            transition: 0.3s;
        }}

        .tech-card:hover {{
            box-shadow: 0 10px 25px rgba(0,0,0,0.06);
        }}

        .tech-icon {{
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: rgba(82, 97, 84, 0.1);
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 18px;
        }}

        .tech-icon svg {{
            width: 24px;
            height: 24px;
        }}

        .tech-card h3 {{
            font-size: 18px;
            margin-bottom: 10px;
            color: var(--text-dark);
        }}

        .tech-card p {{
            font-size: 14px;
            color: var(--text-grey);
            line-height: 1.6;
        }}

        /* Anatomy Infographic Section */
        .anatomy-section {{
            padding: 80px 0;
            background: #fff;
        }}

        .anatomy-card {{
            background: var(--bg-light);
            border-radius: var(--radius);
            border: 1px solid var(--border);
            padding: 36px;
            box-shadow: 0 12px 35px rgba(0,0,0,0.05);
        }}

        .anatomy-image-box {{
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid var(--border);
            background: #fff;
            margin-bottom: 36px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.04);
        }}

        .anatomy-image-box img {{
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
        }}

        .anatomy-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 32px;
        }}

        .anatomy-col {{
            background: #fff;
            padding: 28px;
            border-radius: 16px;
            border: 1px solid var(--border);
        }}

        .anatomy-col-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 12px;
        }}

        .anatomy-tag {{
            background: rgba(82, 97, 84, 0.12);
            color: var(--primary-dark);
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            padding: 4px 10px;
            border-radius: 6px;
        }}

        .anatomy-col h3 {{
            font-size: 19px;
            color: var(--text-dark);
            margin: 0;
        }}

        .anatomy-col-desc {{
            font-size: 14px;
            color: var(--text-grey);
            margin-bottom: 18px;
            line-height: 1.5;
        }}

        .anatomy-list {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}

        .anatomy-list li {{
            margin-bottom: 14px;
            font-size: 14px;
            line-height: 1.55;
            color: #444;
            padding-left: 16px;
            border-left: 2px solid var(--primary);
        }}

        .anatomy-list li:last-child {{
            margin-bottom: 0;
        }}

        .anatomy-list strong {{
            color: var(--text-dark);
            display: block;
            margin-bottom: 2px;
        }}

        /* Comparison Table */
        .comparison-section {{
            padding: 80px 0;
            background: var(--bg-light);
        }}

        .comp-table-wrapper {{
            overflow-x: auto;
            border-radius: var(--radius);
            border: 1px solid var(--border);
            background: #fff;
            box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        }}

        .comp-table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}

        .comp-table th, .comp-table td {{
            padding: 16px 20px;
            font-size: 14px;
            border-bottom: 1px solid rgba(82, 97, 84, 0.1);
        }}

        .comp-table th {{
            background: #f4f3ee;
            font-weight: 700;
            color: var(--text-dark);
            font-size: 15px;
        }}

        .comp-table tr:last-child td {{
            border-bottom: none;
        }}

        .comp-table tr:hover td {{
            background: rgba(82, 97, 84, 0.03);
        }}

        /* Carousel Cases */
        .gallery-section {{
            padding: 80px 0;
            background: #fff;
        }}

        .carousel-container {{
            max-width: 1000px;
            margin: 0 auto;
            overflow: hidden;
            position: relative;
        }}

        .carousel-track {{
            display: flex;
            transition: transform 0.5s ease;
        }}

        .carousel-slide {{
            flex: 0 0 50%;
            max-width: 50%;
            padding: 0 12px;
            box-sizing: border-box;
        }}

        .ba-card {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            background: #fff;
            padding: 12px;
            border-radius: var(--radius);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
            border: 1px solid var(--border);
        }}

        .ba-image {{
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            width: 100%;
            aspect-ratio: 4 / 3;
            background: #eee;
        }}

        .ba-image img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }}

        .ba-label {{
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(4px);
            color: #fff;
            padding: 4px 12px;
            border-radius: 100px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }}

        .ba-label.after {{
            background: var(--primary);
        }}

        .carousel-nav {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 16px;
            margin-top: 30px;
        }}

        .carousel-dots {{
            display: flex;
            gap: 8px;
            align-items: center;
        }}

        .carousel-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(82, 97, 84, 0.25);
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }}

        .carousel-dot.active {{
            background: var(--primary);
            width: 24px;
            border-radius: 4px;
        }}

        .carousel-btn {{
            background: #fff;
            border: 1px solid var(--border);
            width: 44px;
            height: 44px;
            border-radius: 50%;
            font-size: 18px;
            cursor: pointer;
            transition: 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-dark);
        }}

        .carousel-btn:hover {{
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
        }}

        /* Pricing Section */
        .prices-section {{
            padding: 80px 0;
            background: var(--bg-light);
        }}

        .price-category {{
            max-width: 860px;
            margin: 0 auto 30px;
            background: #fff;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            overflow: hidden;
        }}

        .price-category-title {{
            background: #f4f3ee;
            padding: 16px 24px;
            font-size: 18px;
            font-weight: 700;
            color: var(--text-dark);
            border-bottom: 1px solid var(--border);
        }}

        .price-list {{
            padding: 10px 24px;
        }}

        .price-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 0;
            border-bottom: 1px solid rgba(82, 97, 84, 0.1);
            font-size: 15px;
        }}

        .price-row:last-child {{
            border-bottom: none;
        }}

        .price-name {{
            font-weight: 500;
            color: #333;
        }}

        .price-val {{
            font-weight: 800;
            color: var(--primary-dark);
            font-size: 16px;
            white-space: nowrap;
            margin-left: 20px;
        }}

        /* Stages Timeline */
        .stages-section {{
            padding: 80px 0;
            background: #fff;
        }}

        .stages-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}

        .stage-card {{
            background: var(--bg-light);
            padding: 24px;
            border-radius: var(--radius);
            border: 1px solid var(--border);
            position: relative;
        }}

        .stage-num {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--primary);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 16px;
            margin-bottom: 16px;
        }}

        .stage-card h3 {{
            font-size: 17px;
            margin-bottom: 8px;
            color: var(--text-dark);
        }}

        .stage-card p {{
            font-size: 13px;
            color: var(--text-grey);
            line-height: 1.5;
        }}

        /* Doctor Section */
        .doctor-section {{
            padding: 80px 0;
            background: var(--bg-light);
        }}

        .doctor-card {{
            max-width: 960px;
            margin: 0 auto;
            background: #fff;
            border-radius: var(--radius);
            border: 1px solid var(--border);
            padding: 36px;
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 36px;
            align-items: center;
        }}

        .doctor-photo img {{
            width: 100%;
            border-radius: calc(var(--radius) - 6px);
            display: block;
            object-fit: cover;
            aspect-ratio: 4/5;
        }}

        .doctor-info h3 {{
            font-size: 24px;
            margin-bottom: 6px;
            color: var(--text-dark);
        }}

        .doctor-role {{
            color: var(--primary);
            font-weight: 700;
            font-size: 14px;
            margin-bottom: 16px;
        }}

        .doctor-facts {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 24px 0;
        }}

        .doctor-fact {{
            background: var(--bg-light);
            padding: 12px 16px;
            border-radius: 12px;
            border: 1px solid var(--border);
        }}

        .doctor-fact strong {{
            display: block;
            color: var(--primary-dark);
            font-size: 15px;
        }}

        .doctor-fact span {{
            font-size: 12px;
            color: var(--text-grey);
        }}

        /* FAQ Accordion */
        .faq-section {{
            padding: 80px 0;
            background: #fff;
        }}

        .faq-container {{
            max-width: 860px;
            margin: 0 auto;
        }}

        .accordion-item {{
            background: var(--bg-light);
            border: 1px solid var(--border);
            border-radius: 14px;
            margin-bottom: 14px;
            overflow: hidden;
        }}

        .accordion-header {{
            padding: 18px 24px;
            cursor: pointer;
            font-weight: 700;
            font-size: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            user-select: none;
            color: var(--text-dark);
        }}

        .accordion-header:hover {{
            color: var(--primary);
        }}

        .accordion-icon {{
            font-size: 20px;
            font-weight: 400;
            transition: transform 0.3s ease;
        }}

        .accordion-content {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
            background: var(--bg-light);
        }}

        .accordion-body {{
            padding: 0 24px 20px;
            color: #555;
            font-size: 15px;
            line-height: 1.6;
        }}

        /* Responsive */
        @media (max-width: 992px) {{
            .prosthetics-hero {{
                padding: 50px 0 60px;
            }}
            .prosthetics-hero .hero-grid {{
                grid-template-columns: 1fr;
                text-align: center;
            }}
            .prosthetics-hero .hero-benefits {{
                text-align: left;
                display: inline-block;
            }}
            .prosthetics-hero .hero-actions {{
                justify-content: center;
            }}
            .anatomy-grid {{
                grid-template-columns: 1fr;
            }}
            .doctor-card {{
                grid-template-columns: 1fr;
                text-align: center;
            }}
            .doctor-photo {{
                max-width: 260px;
                margin: 0 auto;
            }}
            .doctor-facts {{
                text-align: left;
            }}
            .nav-menu {{
                display: none;
            }}
            .mobile-toggle {{
                display: block;
            }}
        }}

        @media (max-width: 768px) {{
            .carousel-slide {{
                flex: 0 0 100%;
                max-width: 100%;
            }}
            .anatomy-card {{
                padding: 20px;
            }}
            .doctor-facts {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>

<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PBZF8G5B"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->

    <header>
        <div class="container nav-wrapper">
            <a href="{home_link}" class="logo">
                <picture>
                    <source srcset="{img_pfx}images/Logo.webp" type="image/webp">
                    <img src="{img_pfx}images/Logo.png" alt="Harmony Clinic" width="1072" height="1071" decoding="async">
                </picture>
            </a>
            <nav>
                <ul class="nav-menu" id="navMenu">
                    <li><a href="{home_link}">{"Головна" if is_ua else "Главная"}</a></li>
                    <li><a href="{services_link}">{"Послуги" if is_ua else "Услуги"}</a></li>
                    <li><a href="{implants_link}">{"Імплантація" if is_ua else "Имплантация"}</a></li>
                    <li><a href="{treatment_link}">{"Лікування" if is_ua else "Лечение"}</a></li>
                    <li><a href="{home_link}#team">{"Лікарі" if is_ua else "Врачи"}</a></li>
                    <li><a href="{home_link}#works">{"Роботи" if is_ua else "Работы"}</a></li>
                    <li><a href="{home_link}#reviews">{"Відгуки" if is_ua else "Отзывы"}</a></li>
                    <li><a href="{home_link}#contacts">{"Контакти" if is_ua else "Контакты"}</a></li>
                </ul>
            </nav>
            <div style="display: flex; align-items: center; gap: 12px;">
                <a href="{other_lang_url}" class="lang-switch" title="Перемкнути мову">{other_lang_label}</a>
                <a href="tel:+380687794547" class="header-phone" onclick="return gtag_report_call('tel:+380687794547');">+38 068 779 45 47</a>
                <div class="mobile-toggle" id="mobileToggle" onclick="toggleMenu()">☰</div>
            </div>
        </div>
    </header>

    <main id="main">
        <!-- Breadcrumbs -->
        <div class="container">
            <nav class="breadcrumbs" aria-label="Breadcrumb">
                <a href="{home_link}">{"Головна" if is_ua else "Главная"}</a>
                <span>/</span>
                <a href="{services_link}">{"Послуги" if is_ua else "Услуги"}</a>
                <span>/</span>
                <span>{"Протезування зубів" if is_ua else "Протезирование зубов"}</span>
            </nav>
        </div>

        <!-- Hero Section -->
        <section class="prosthetics-hero">
            <div class="container hero-grid">
                <div class="hero-text">
                    <div class="hero-badge">⚡ {"Клініка працює з генератором · 3Shape TRIOS 4" if is_ua else "Клиника работает с генератором · 3Shape TRIOS 4"}</div>
                    <div class="hero-pretitle">{h_pre}</div>
                    <h1>{h_h1}</h1>
                    <span class="sub-headline">{h_sub}</span>
                    <div class="hero-benefits">
                        <ul>
                            <li>{b_1}</li>
                            <li>{b_2}</li>
                            <li>{b_3}</li>
                        </ul>
                    </div>
                    <div class="hero-actions">
                        <a href="https://t.me/+380687794547" target="_blank" rel="noopener" class="btn-primary" onclick="return gtag_report_messenger('https://t.me/+380687794547');">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M9.78,18.65l0.13-3.14l5.63-5.07c0.49-0.44-0.11-0.69-0.76-0.29L8.4,14.2l-3.03-0.95c-0.66-0.21-0.67-0.66,0.14-0.97L17.36,7.7c0.56-0.21,1.05,0.13,0.87,0.86L16.14,18.2c-0.12,0.59-0.87,0.72-1.41,0.45L9.78,18.65z"/></svg>
                            {b_btn}
                        </a>
                        <a href="#prices" class="btn-outline">{"Дивитися ціни" if is_ua else "Смотреть цены"}</a>
                    </div>
                </div>
                <div class="hero-image-card">
                    <picture>
                        <source srcset="{img_pfx}images/andrey.webp" type="image/webp">
                        <img src="{img_pfx}images/andrey.jpg" alt="{doc_name} — стоматолог-ортопед в Одесі" width="725" height="1024" decoding="async">
                    </picture>
                    <div class="hero-image-badge">
                        <strong>{doc_name}</strong>
                        <span>{"Головний лікар · Провідний ортопед (15+ років практики)" if is_ua else "Главный врач · Ведущий ортопед (15+ лет практики)"}</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Services Grid -->
        <section class="services-section" id="types">
            <div class="container">
                <h2 class="section-title">{srv_h2}</h2>
                <p class="section-subtitle">{srv_sub}</p>
                
                <div class="services-grid">
                    <!-- 1. Цирконієві коронки -->
                    <div class="service-card">
                        <div>
                            <span class="service-card-tag">{"Надміцний вибір" if is_ua else "Сверхпрочный выбор"}</span>
                            <h3>{"Цирконієві коронки (Multi-layer)" if is_ua else "Циркониевые коронки (Multi-layer)"}</h3>
                            <p>{"Монолітний діоксид цирконію з плавним градієнтом прозорості. Витримує колосальне жувальне навантаження, біосумісний, не темніє і не викликає алергії. Ідеальний для жувальних та передніх зубів." if is_ua else "Монолитный диоксид циркония с плавным градиентом прозрачности. Выдерживает колоссальную жевательную нагрузку, биосовместим, не темнеет и не вызывает аллергии. Идеален для жевательных и передних зубов."}</p>
                        </div>
                        <div class="service-card-footer">
                            <span class="service-price">{"від 170 $" if is_ua else "от 170 $"}</span>
                            <a href="#prices" class="btn-outline" style="padding: 8px 18px; font-size: 13px;">{"Детальніше" if is_ua else "Подробнее"}</a>
                        </div>
                    </div>

                    <!-- 2. Кераміка E-max та вініри -->
                    <div class="service-card">
                        <div>
                            <span class="service-card-tag">{"Естетика №1" if is_ua else "Эстетика №1"}</span>
                            <h3>{"Керамічні коронки та вініри E-max" if is_ua else "Керамические коронки и виниры E-max"}</h3>
                            <p>{"Пресована кераміка (дисилікат літію) з максимальною світлопроникністю, що повністю імітує живу зубну емаль. Золотий стандарт для зони посмішки, усунення сколів, плям та проміжків." if is_ua else "Прессованная керамика (дисиликат лития) с максимальной светопроницаемостью, полностью имитирующая живую зубную эмаль. Золотой стандарт для зоны улыбки, устранения сколов, пятен и промежутков."}</p>
                        </div>
                        <div class="service-card-footer">
                            <span class="service-price">{"300 $" if is_ua else "300 $"}</span>
                            <a href="#prices" class="btn-outline" style="padding: 8px 18px; font-size: 13px;">{"Детальніше" if is_ua else "Подробнее"}</a>
                        </div>
                    </div>

                    <!-- 3. Металокерамічні коронки -->
                    <div class="service-card">
                        <div>
                            <span class="service-card-tag">{"Доступна класика" if is_ua else "Доступная классика"}</span>
                            <h3>{"Металокерамічні коронки" if is_ua else "Металлокерамические коронки"}</h3>
                            <p>{"Класична перевірена конструкція з литим металевим каркасом та пошаровим нанесенням кераміки. Надійний та бюджетний варіант для відновлення жувальних зубів." if is_ua else "Классическая проверенная конструкция с литым металлическим каркасом и послойным нанесением керамики. Надежный и бюджетный вариант для восстановления жевательных зубов."}</p>
                        </div>
                        <div class="service-card-footer">
                            <span class="service-price">{"110 $" if is_ua else "110 $"}</span>
                            <a href="#prices" class="btn-outline" style="padding: 8px 18px; font-size: 13px;">{"Детальніше" if is_ua else "Подробнее"}</a>
                        </div>
                    </div>

                    <!-- 4. Мостоподібні протези -->
                    <div class="service-card">
                        <div>
                            <span class="service-card-tag">{"Відновлення ряду" if is_ua else "Восстановление ряда"}</span>
                            <h3>{"Мостоподібні протези (мости)" if is_ua else "Мостовидные протезы (мосты)"}</h3>
                            <p>{"Незнімна конструкція для заміщення 1–2 відсутніх зубів із фіксацією на сусідні опорні зуби або імпланти. Повертає повноцінне жування та анатомічну безперервність зубного ряду." if is_ua else "Несъемная конструкция для замещения 1–2 отсутствующих зубов с фиксацией на соседние опорные зубы или импланты. Возвращает полноценное жевание и анатомическую непрерывность зубного ряда."}</p>
                        </div>
                        <div class="service-card-footer">
                            <span class="service-price">{"від 110 $/од." if is_ua else "от 110 $/ед."}</span>
                            <a href="#prices" class="btn-outline" style="padding: 8px 18px; font-size: 13px;">{"Детальніше" if is_ua else "Подробнее"}</a>
                        </div>
                    </div>

                    <!-- 5. Протезування на імплантах -->
                    <div class="service-card">
                        <div>
                            <span class="service-card-tag">{"Без обточування сусідніх" if is_ua else "Без обточки соседних"}</span>
                            <h3>{"Коронки та протези на імплантах" if is_ua else "Коронки и протезы на имплантах"}</h3>
                            <p>{"Встановлення цирконієвих коронок на індивідуальних абатментах із гвинтовою фіксацією. Зберігає сусідні зуби абсолютно неушкодженими. Також реалізуємо повні балочні конструкції All-on-4 / All-on-6." if is_ua else "Установка циркониевых коронок на индивидуальных абатментах с винтовой фиксацией. Сохраняет соседние зубы абсолютно нетронутыми. Также реализуем полные балочные конструкции All-on-4 / All-on-6."}</p>
                        </div>
                        <div class="service-card-footer">
                            <span class="service-price">{"від 250 $" if is_ua else "от 250 $"}</span>
                            <a href="{implants_link}" class="btn-outline" style="padding: 8px 18px; font-size: 13px;">{"Про імпланти" if is_ua else "Об имплантах"}</a>
                        </div>
                    </div>

                    <!-- 6. Знімні та бюгельні протези -->
                    <div class="service-card">
                        <div>
                            <span class="service-card-tag">{"Повне жування" if is_ua else "Полное жевание"}</span>
                            <h3>{"Знімне та бюгельне протезування" if is_ua else "Съемное и бюгельное протезирование"}</h3>
                            <p>{"Сучасні акрилові, нейлонові та бюгельні протези на мікрозамках або кламерах при втраті великої кількості або всіх зубів на щелепі. Легкі, адаптивні та комфортні у щоденному використанні." if is_ua else "Современные акриловые, нейлоновые и бюгельные протезы на микрозамках или кламмерах при потере большого количества или всех зубов на челюсти. Легкие, адаптивные и комфортные в ежедневном использовании."}</p>
                        </div>
                        <div class="service-card-footer">
                            <span class="service-price">{"від 8 500 грн" if is_ua else "от 8 500 грн"}</span>
                            <a href="#prices" class="btn-outline" style="padding: 8px 18px; font-size: 13px;">{"Детальніше" if is_ua else "Подробнее"}</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Standards / Equipment -->
        <section class="tech-section">
            <div class="container">
                <h2 class="section-title">{tech_h2}</h2>
                <p class="section-subtitle">{"Застосовуємо передові технології точного позиціонування та цифрового 3D-моделювання" if is_ua else "Применяем передовые технологии точного позиционирования и цифрового 3D-моделирования"}</p>
                
                <div class="tech-grid">
                    <div class="tech-card">
                        <div class="tech-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
                        </div>
                        <h3>{"3D-сканер 3Shape TRIOS 4" if is_ua else "3D-сканер 3Shape TRIOS 4"}</h3>
                        <p>{"Створення надточної цифрової моделі щелеп за 2–3 хвилини без гіпсових зліпків, липких мас та блювотного рефлексу." if is_ua else "Создание сверхточной цифровой модели челюстей за 2–3 минуты без гипсовых слепков, липких масс и рвотного рефлекса."}</p>
                    </div>

                    <div class="tech-card">
                        <div class="tech-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                        </div>
                        <h3>{"CAD/CAM та exocad моделювання" if is_ua else "CAD/CAM и exocad моделирование"}</h3>
                        <p>{"Комп'ютерне проектування коронки з точністю до мікронів. Ідеальне крайове прилягання захищає зуб від затікання слини та вторинного карієсу." if is_ua else "Компьютерное проектирование коронки с точностью до микронов. Идеальное краевое прилегание защищает зуб от затекания слюны и вторичного кариеса."}</p>
                    </div>

                    <div class="tech-card">
                        <div class="tech-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                        </div>
                        <h3>{"Щадне препарування з уступом" if is_ua else "Щадящее препарирование с уступом"}</h3>
                        <p>{"Формуємо плавний круговий уступ під ясенним краєм. Це зберігає максимальний об'єм власних тканин та запобігає посинінню чи травмуванню ясен." if is_ua else "Формируем плавный круговой уступ под десневым краем. Это сохраняет максимальный объем собственных тканей и предотвращает посинение или травмирование десны."}</p>
                    </div>

                    <div class="tech-card">
                        <div class="tech-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                        </div>
                        <h3>{"Digital Smile Design (DSD)" if is_ua else "Digital Smile Design (DSD)"}</h3>
                        <p>{"Можливість оцінити та узгодити форму, колір та пропорції майбутніх зубів на екрані ще до початку виготовлення постійної конструкції." if is_ua else "Возможность оценить и согласовать форму, цвет и пропорции будущих зубов на экране еще до начала изготовления постоянной конструкции."}</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Anatomy Infographic Section -->
        <section class="anatomy-section" id="anatomy">
            <div class="container">
                <h2 class="section-title">{anatomy_h2}</h2>
                <p class="section-subtitle">{anatomy_sub}</p>

                <div class="anatomy-card">
                    <div class="anatomy-image-box">
                        <picture>
                            <source srcset="{img_pfx}images/crown-vs-implant.webp" type="image/webp">
                            <img src="{img_pfx}images/crown-vs-implant.jpg" alt="{anatomy_alt}" width="1376" height="768" loading="lazy">
                        </picture>
                    </div>

                    <div class="anatomy-grid">
                        <!-- Left: Natural Tooth -->
                        <div class="anatomy-col">
                            <div class="anatomy-col-header">
                                <div class="anatomy-tag">{"Варіант 1" if is_ua else "Вариант 1"}</div>
                                <h3>{"Коронка на власному зубі" if is_ua else "Коронка на собственном зубе"}</h3>
                            </div>
                            <p class="anatomy-col-desc">{"Застосовується, коли корінь зуба надійний і здоровий, але коронкова частина зруйнована більш ніж на 50%:" if is_ua else "Применяется, когда корень зуба надежен и здоров, но коронковая часть разрушена более чем на 50%:"}</p>
                            <ul class="anatomy-list">
                                <li>
                                    <strong>{"1. Керамічна або цирконієва коронка:" if is_ua else "1. Керамическая или циркониевая коронка:"}</strong>
                                    {"Монолітна естетична конструкція, що повністю повторює анатомію зуба, відновлює жування та захищає зуб від сколів." if is_ua else "Монолитная эстетическая конструкция, полностью повторяющая анатомию зуба, восстанавливающая жевание и защищающая зуб от сколов."}
                                </li>
                                <li>
                                    <strong>{"2. Препарована кукса зуба:" if is_ua else "2. Препарированная культя зуба:"}</strong>
                                    {"Зуб обробляється з круговим уступом під ясна для ідеального крайового прилягання без щілин і затікання бактерій." if is_ua else "Зуб обрабатывается с круговым уступом под десну для идеального краевого прилегания без щелей и затекания бактерий."}
                                </li>
                                <li>
                                    <strong>{"3. Природний корінь у кістці:" if is_ua else "3. Естественный корень в кости:"}</strong>
                                    {"Зберігає природний зв'язковий апарат (періодонт), забезпечуючи фізіологічну амортизацію при жуванні." if is_ua else "Сохраняет естественный связочный аппарат (периодонт), обеспечивая физиологическую амортизацию при жевании."}
                                </li>
                            </ul>
                        </div>

                        <!-- Right: Implant -->
                        <div class="anatomy-col">
                            <div class="anatomy-col-header">
                                <div class="anatomy-tag">{"Варіант 2" if is_ua else "Вариант 2"}</div>
                                <h3>{"Коронка на імплантаті" if is_ua else "Коронка на имплантате"}</h3>
                            </div>
                            <p class="anatomy-col-desc">{"Застосовується при повній втраті зуба для його 100% відновлення без обточування сусідніх здорових зубів:" if is_ua else "Применяется при полной потере зуба для его 100% восстановления без обточки соседних здоровых зубов:"}</p>
                            <ul class="anatomy-list">
                                <li>
                                    <strong>{"1. Цирконієва коронка з фіксацією:" if is_ua else "1. Циркониевая коронка с фиксацией:"}</strong>
                                    {"Надміцна коронка, яка фіксується за допомогою гвинтового з'єднання через шахту абатмента або на адгезивний цемент." if is_ua else "Сверхпрочная коронка, которая фиксируется с помощью винтового соединения через шахту абатмента или на адгезивный цемент."}
                                </li>
                                <li>
                                    <strong>{"2. Індивідуальний абатмент:" if is_ua else "2. Индивидуальный абатмент:"}</strong>
                                    {"Титановий або цирконієвий перехідний елемент, який з'єднує коронку з імплантом і формує гарний контур ясен." if is_ua else "Титановый или циркониевый переходный элемент, соединяющий коронку с имплантом и формирующий красивый контур десны."}
                                </li>
                                <li>
                                    <strong>{"3. Титановий імплант у кістці:" if is_ua else "3. Титановый имплант в кости:"}</strong>
                                    {"Штучний корінь із чистого титану, що повністю інтегрується в щелепну кістку та зупиняє її атрофію." if is_ua else "Искусственный корень из чистого титана, который полностью интегрируется в челюстную кость и останавливает ее атрофию."}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Material Comparison Table -->
        <section class="comparison-section">
            <div class="container">
                <h2 class="section-title">{comp_h2}</h2>
                <p class="section-subtitle">{"Порівняння основних матеріалів ортопедичних коронок за ключовими параметрами" if is_ua else "Сравнение основных материалов ортопедических коронок по ключевым параметрам"}</p>
                
                <div class="comp-table-wrapper">
                    <table class="comp-table">
                        <thead>
                            <tr>
                                <th>{"Параметр" if is_ua else "Параметр"}</th>
                                <th>{"Металокераміка" if is_ua else "Металлокерамика"}</th>
                                <th>{"Цирконій Multi-layer" if is_ua else "Цирконий Multi-layer"}</th>
                                <th>{"Кераміка E-max" if is_ua else "Керамика E-max"}</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>{"Естетика та прозорість" if is_ua else "Эстетика и прозрачность"}</strong></td>
                                <td>{"Базова (не пропускає світло)" if is_ua else "Базовая (не пропускает свет)"}</td>
                                <td>{"Висока (градієнт відтінку)" if is_ua else "Высокая (градиент оттенка)"}</td>
                                <td>{"Максимальна (імітація емалі)" if is_ua else "Максимальная (имитация эмали)"}</td>
                            </tr>
                            <tr>
                                <td><strong>{"Міцність на злам" if is_ua else "Прочность на излом"}</strong></td>
                                <td>{"~400–500 МПа" if is_ua else "~400–500 МПа"}</td>
                                <td>{"800–1200 МПа (екстремальна)" if is_ua else "800–1200 МПа (экстремальная)"}</td>
                                <td>{"400–500 МПа (висока)" if is_ua else "400–500 МПа (высокая)"}</td>
                            </tr>
                            <tr>
                                <td><strong>{"Відсутність металу та синюшності ясен" if is_ua else "Отсутствие металла и синюшности десны"}</strong></td>
                                <td>{"Ні (містить металевий каркас)" if is_ua else "Нет (содержит металл)"}</td>
                                <td>{"Так (100% біосумісний)" if is_ua else "Да (100% биосовместим)"}</td>
                                <td>{"Так (100% прес-кераміка)" if is_ua else "Да (100% пресс-керамика)"}</td>
                            </tr>
                            <tr>
                                <td><strong>{"Точність крайового прилягання" if is_ua else "Точность краевого прилегания"}</strong></td>
                                <td>{"Стандартна ручна" if is_ua else "Стандартная ручная"}</td>
                                <td>{"Мікронна (фрезерування CAD/CAM)" if is_ua else "Микронная (фрезерование CAD/CAM)"}</td>
                                <td>{"Мікронна (фрезерування / пресування)" if is_ua else "Микронная (фрезерование / прессование)"}</td>
                            </tr>
                            <tr>
                                <td><strong>{"Рекомендована зона застосування" if is_ua else "Рекомендуемая зона применения"}</strong></td>
                                <td>{"Жувальні зуби (бічні)" if is_ua else "Жевательные зубы (боковые)"}</td>
                                <td>{"Жувальні, передні, мости, імпланти" if is_ua else "Жевательные, передние, мосты, импланты"}</td>
                                <td>{"Зона посмішки, вініри, фронтальні" if is_ua else "Зона улыбки, виниры, фронтальные"}</td>
                            </tr>
                            <tr>
                                <td><strong>{"Орієнтовний термін служби" if is_ua else "Ориентировочный срок службы"}</strong></td>
                                <td>{"7–10 років" if is_ua else "7–10 лет"}</td>
                                <td>{"10–15+ років" if is_ua else "10–15+ лет"}</td>
                                <td>{"10–15+ років" if is_ua else "10–15+ лет"}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- Cases Carousel -->
        <section class="gallery-section" id="works">
            <div class="container">
                <h2 class="section-title">{cases_h2}</h2>
                <p class="section-subtitle">{cases_sub}</p>
                
                <div class="carousel-container">
                    <div class="carousel-track" id="carouselTrack">
                        <!-- Case 1 -->
                        <div class="carousel-slide">
                            <div class="ba-card">
                                <div class="ba-image">
                                    <span class="ba-label">{"До" if is_ua else "До"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case1-before.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case1-before.jpg" alt="Зуби до протезування коронками" width="1280" height="853" loading="lazy">
                                    </picture>
                                </div>
                                <div class="ba-image">
                                    <span class="ba-label after">{"Після" if is_ua else "После"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case1-after.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case1-after.jpg" alt="Результат відновлення цирконієвими коронками" width="1280" height="853" loading="lazy">
                                    </picture>
                                </div>
                            </div>
                        </div>

                        <!-- Case 2 -->
                        <div class="carousel-slide">
                            <div class="ba-card">
                                <div class="ba-image">
                                    <span class="ba-label">{"До" if is_ua else "До"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case4-before.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case4-before.jpg" alt="Передні зуби до встановлення вінірів" width="1280" height="853" loading="lazy">
                                    </picture>
                                </div>
                                <div class="ba-image">
                                    <span class="ba-label after">{"Після" if is_ua else "После"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case4-after.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case4-after.jpg" alt="Естетична реставрація вінірами E-max" width="1280" height="853" loading="lazy">
                                    </picture>
                                </div>
                            </div>
                        </div>

                        <!-- Case 3 -->
                        <div class="carousel-slide">
                            <div class="ba-card">
                                <div class="ba-image">
                                    <span class="ba-label">{"До" if is_ua else "До"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case5-before.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case5-before.jpg" alt="Зруйнований жувальний зуб" width="1065" height="450" loading="lazy">
                                    </picture>
                                </div>
                                <div class="ba-image">
                                    <span class="ba-label after">{"Після" if is_ua else "После"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case5-after.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case5-after.jpg" alt="Жувальний зуб відновлений цирконієвою коронкою" width="1280" height="592" loading="lazy">
                                    </picture>
                                </div>
                            </div>
                        </div>

                        <!-- Case 4 -->
                        <div class="carousel-slide">
                            <div class="ba-card">
                                <div class="ba-image">
                                    <span class="ba-label">{"До" if is_ua else "До"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case2-before.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case2-before.jpg" alt="Дефект зубного ряду" width="1280" height="852" loading="lazy">
                                    </picture>
                                </div>
                                <div class="ba-image">
                                    <span class="ba-label after">{"Після" if is_ua else "После"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case2-after.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case2-after.jpg" alt="Відновлення зубного ряду мостоподібним протезом" width="892" height="597" loading="lazy">
                                    </picture>
                                </div>
                            </div>
                        </div>

                        <!-- Case 5 -->
                        <div class="carousel-slide">
                            <div class="ba-card">
                                <div class="ba-image">
                                    <span class="ba-label">{"До" if is_ua else "До"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case3-before.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case3-before.jpg" alt="Стерті та потемнілі передні зуби" width="1280" height="832" loading="lazy">
                                    </picture>
                                </div>
                                <div class="ba-image">
                                    <span class="ba-label after">{"Після" if is_ua else "После"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case3-after.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case3-after.jpg" alt="Природна посмішка після коронок E-max" width="1280" height="824" loading="lazy">
                                    </picture>
                                </div>
                            </div>
                        </div>

                        <!-- Case 6 -->
                        <div class="carousel-slide">
                            <div class="ba-card">
                                <div class="ba-image">
                                    <span class="ba-label">{"До" if is_ua else "До"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case6-before.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case6-before.jpg" alt="Зуби зі старими сколеними реставраціями" width="1280" height="853" loading="lazy">
                                    </picture>
                                </div>
                                <div class="ba-image">
                                    <span class="ba-label after">{"Після" if is_ua else "После"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case6-after.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case6-after.jpg" alt="Комплексне естетичне протезування" width="1280" height="853" loading="lazy">
                                    </picture>
                                </div>
                            </div>
                        </div>

                        <!-- Case 7 -->
                        <div class="carousel-slide">
                            <div class="ba-card">
                                <div class="ba-image">
                                    <span class="ba-label">{"До" if is_ua else "До"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case7-before.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case7-before.jpg" alt="Відсутні зуби до встановлення імплантів" width="1280" height="853" loading="lazy">
                                    </picture>
                                </div>
                                <div class="ba-image">
                                    <span class="ba-label after">{"Після" if is_ua else "После"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case7-after.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case7-after.jpg" alt="Цирконієві коронки на імплантах" width="1280" height="853" loading="lazy">
                                    </picture>
                                </div>
                            </div>
                        </div>

                        <!-- Case 8 -->
                        <div class="carousel-slide">
                            <div class="ba-card">
                                <div class="ba-image">
                                    <span class="ba-label">{"До" if is_ua else "До"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case9-before.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case9-before.jpg" alt="Потемнілі нерівні зуби" width="771" height="1024" loading="lazy">
                                    </picture>
                                </div>
                                <div class="ba-image">
                                    <span class="ba-label after">{"Після" if is_ua else "После"}</span>
                                    <picture>
                                        <source srcset="{img_pfx}images-coron/prosthetics-case9-after.webp" type="image/webp">
                                        <img src="{img_pfx}images-coron/prosthetics-case9-after.jpg" alt="Ідеальна біла посмішка після вінірів" width="768" height="1024" loading="lazy">
                                    </picture>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="carousel-nav">
                        <button class="carousel-btn" onclick="moveSlide(-1)" aria-label="Попередній слайд">❮</button>
                        <div class="carousel-dots" id="carouselDots"></div>
                        <button class="carousel-btn" onclick="moveSlide(1)" aria-label="Наступний слайд">❯</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Pricing Section -->
        <section class="prices-section" id="prices">
            <div class="container">
                <h2 class="section-title">{price_h2}</h2>
                <p class="section-subtitle">{price_sub}</p>

                <!-- Category 1: Коронки та вініри -->
                <div class="price-category">
                    <div class="price-category-title">{"Незнімне протезування (коронки, вініри, мости)" if is_ua else "Несъемное протезирование (коронки, виниры, мосты)"}</div>
                    <div class="price-list">
                        <div class="price-row">
                            <span class="price-name">{"Первинна консультація стоматолога-ортопеда + фотопротокол" if is_ua else "Первичная консультация стоматолога-ортопеда + фотопротокол"}</span>
                            <span class="price-val">{"Безкоштовно" if is_ua else "Бесплатно"}</span>
                        </div>
                        <div class="price-row">
                            <span class="price-name">{"Металокерамічна коронка" if is_ua else "Металлокерамическая коронка"}</span>
                            <span class="price-val">110 $</span>
                        </div>
                        <div class="price-row">
                            <span class="price-name">{"Цирконієва коронка на боковий (жувальний) зуб" if is_ua else "Циркониевая коронка на боковой (жевательный) зуб"}</span>
                            <span class="price-val">170 $</span>
                        </div>
                        <div class="price-row">
                            <span class="price-name">{"Цирконієва коронка Multi-layer на передній зуб" if is_ua else "Циркониевая коронка Multi-layer на передний зуб"}</span>
                            <span class="price-val">300 $</span>
                        </div>
                        <div class="price-row">
                            <span class="price-name">{"Керамічна коронка / вінір E-max" if is_ua else "Керамическая коронка / винир E-max"}</span>
                            <span class="price-val">300 $</span>
                        </div>
                        <div class="price-row">
                            <span class="price-name">{"Коронка з діоксиду цирконію на імплантаті" if is_ua else "Коронка из диоксида циркония на имплантате"}</span>
                            <span class="price-val">{"від 250 $" if is_ua else "от 250 $"}</span>
                        </div>
                        <div class="price-row">
                            <span class="price-name">{"Тимчасова естетична коронка (PMMA)" if is_ua else "Временная эстетическая коронка (PMMA)"}</span>
                            <span class="price-val">2 000 грн</span>
                        </div>
                    </div>
                </div>

                <!-- Category 2: Знімне протезування -->
                <div class="price-category">
                    <div class="price-category-title">{"Знімне та комбіноване протезування" if is_ua else "Съемное и комбинированное протезирование"}</div>
                    <div class="price-list">
                        <div class="price-row">
                            <span class="price-name">{"Акриловий знімний протез (повний або частковий)" if is_ua else "Акриловый съемный протез (полный или частичный)"}</span>
                            <span class="price-val">8 500 грн</span>
                        </div>
                        <div class="price-row">
                            <span class="price-name">{"Нейлоновий протез (еластичний базис)" if is_ua else "Нейлоновый протез (эластичный базис)"}</span>
                            <span class="price-val">12 000 грн</span>
                        </div>
                        <div class="price-row">
                            <span class="price-name">{"Бюгельний протез на кламерах або замках" if is_ua else "Бюгельный протез на кламмерах или замках"}</span>
                            <span class="price-val">{"від 500 $" if is_ua else "от 500 $"}</span>
                        </div>
                    </div>
                </div>

                <div style="text-align: center; margin-top: 30px;">
                    <a href="https://t.me/+380687794547" target="_blank" rel="noopener" class="btn-primary" onclick="return gtag_report_messenger('https://t.me/+380687794547');">
                        {"Записатися на безкоштовну консультацію" if is_ua else "Записаться на бесплатную консультацию"}
                    </a>
                </div>
            </div>
        </section>

        <!-- Stages -->
        <section class="stages-section" id="stages">
            <div class="container">
                <h2 class="section-title">{stages_h2}</h2>
                <p class="section-subtitle">{stages_sub}</p>

                <div class="stages-grid">
                    <div class="stage-card">
                        <div class="stage-num">1</div>
                        <h3>{"Консультація та 3D-скан" if is_ua else "Консультация и 3D-скан"}</h3>
                        <p>{"Огляд, прицільна діагностика, цифрове 3D-сканування щелепи сканером 3Shape TRIOS 4. Складання плану лікування." if is_ua else "Осмотр, прицельная диагностика, цифровое 3D-сканирование челюсти сканером 3Shape TRIOS 4. Составление плана лечения."}</p>
                    </div>

                    <div class="stage-card">
                        <div class="stage-num">2</div>
                        <h3>{"Підготовка зуба" if is_ua else "Подготовка зуба"}</h3>
                        <p>{"Щадне препарування з формуванням кругового уступу. Встановлення тимчасової коронки для захисту зуба." if is_ua else "Щадящее препарирование с формированием кругового уступа. Установка временной коронки для защиты зуба."}</p>
                    </div>

                    <div class="stage-card">
                        <div class="stage-num">3</div>
                        <h3>{"CAD/CAM виготовлення" if is_ua else "CAD/CAM изготовление"}</h3>
                        <p>{"Лабораторне комп'ютерне моделювання та прецизійне фрезерування коронки з монолітного цирконію або прес-кераміки (5–7 днів)." if is_ua else "Лабораторное компьютерное моделирование и прецизионное фрезерование коронки из монолитного циркония или пресс-керамики (5–7 дней)."}</p>
                    </div>

                    <div class="stage-card">
                        <div class="stage-num">4</div>
                        <h3>{"Примірка та контроль" if is_ua else "Примерка и контроль"}</h3>
                        <p>{"Перевірка точності посадки, контактних пунктів із сусідніми зубами, кольору та прикусу." if is_ua else "Проверка точности посадки, контактных пунктов с соседними зубами, цвета и прикуса."}</p>
                    </div>

                    <div class="stage-card">
                        <div class="stage-num">5</div>
                        <h3>{"Фінішна фіксація" if is_ua else "Финишная фиксация"}</h3>
                        <p>{"Надійна адгезивна фіксація на постійний цемент, полірування меж та рекомендації щодо щоденного догляду." if is_ua else "Надежная адгезивная фиксация на постоянный цемент, полировка границ и рекомендации по ежедневному уходу."}</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Doctor Spotlight -->
        <section class="doctor-section" id="doctor">
            <div class="container">
                <h2 class="section-title">{doc_h2}</h2>
                <div class="doctor-card">
                    <div class="doctor-photo">
                        <picture>
                            <source srcset="{img_pfx}images/andrey.webp" type="image/webp">
                            <img src="{img_pfx}images/andrey.jpg" alt="{doc_name}" width="725" height="1024" loading="lazy">
                        </picture>
                    </div>
                    <div class="doctor-info">
                        <h3>{doc_name}</h3>
                        <div class="doctor-role">{doc_role}</div>
                        <p>{doc_desc}</p>
                        <div class="doctor-facts">
                            <div class="doctor-fact">
                                <strong>{"15+ років" if is_ua else "15+ лет"}</strong>
                                <span>{"клінічної практики в ортопедії" if is_ua else "клинической практики в ортопедии"}</span>
                            </div>
                            <div class="doctor-fact">
                                <strong>{"3Shape TRIOS 4" if is_ua else "3Shape TRIOS 4"}</strong>
                                <span>{"цифровий протокол без зліпків" if is_ua else "цифровой протокол без слепков"}</span>
                            </div>
                            <div class="doctor-fact">
                                <strong>{"ОНМедУ" if is_ua else "ОНМедУ"}</strong>
                                <span>{"Одеський національний медичний університет" if is_ua else "Одесский национальный медицинский университет"}</span>
                            </div>
                            <div class="doctor-fact">
                                <strong>{"CAD/CAM & exocad" if is_ua else "CAD/CAM & exocad"}</strong>
                                <span>{"цифрове 3D-моделювання посмішки" if is_ua else "цифровое 3D-моделирование улыбки"}</span>
                            </div>
                        </div>
                        <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-top: 20px;">
                            <a href="https://t.me/+380687794547" target="_blank" rel="noopener" class="btn-primary" onclick="return gtag_report_messenger('https://t.me/+380687794547');">
                                {"Записатися до лікаря" if is_ua else "Записаться к врачу"}
                            </a>
                            <a href="{doctor_link}" class="btn-outline">
                                {"Детальніше про лікаря →" if is_ua else "Подробнее о враче →"}
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ Section -->
        <section class="faq-section" id="faq">
            <div class="container">
                <h2 class="section-title">{faq_h2}</h2>
                <p class="section-subtitle">{"Відповідаємо на найпоширеніші запитання пацієнтів щодо протезування, вибору матеріалів та догляду" if is_ua else "Отвечаем на самые распространенные вопросы пациентов о протезировании, выборе материалов и уходе"}</p>

                <div class="faq-container">
                    <!-- Q1 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Чи обов'язково видаляти нерв перед встановленням коронки?" if is_ua else "Обязательно ли удалять нерв перед установкой коронки?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"Ні. Сучасний цифровий протокол та робота з безметалевою керамікою (цирконій, E-max) дозволяють зберігати зуб живим. Ми проводимо щадне препарування з обов'язковим водним охолодженням і знімаємо мінімальний шар емалі. Депульпування проводиться виключно за прямими клінічними показаннями (глибокий карієс із ураженням пульпи або хронічне запалення)." if is_ua else "Нет. Современный цифровой протокол и работа с безметалловой керамикой (цирконий, E-max) позволяют сохранять зуб живым. Мы проводим щадящее препарирование с обильным водяным охлаждением и снимаем минимальный слой эмали. Депульпирование проводится исключительно по прямым клиническим показаниям (глубокий кариес с поражением пульпы или хроническое воспаление)."}
                            </div>
                        </div>
                    </div>

                    <!-- Q2 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Чим діоксид цирконію відрізняється від кераміки E-max та металокераміки?" if is_ua else "Чем диоксид циркония отличается от керамики E-max и металлокерамики?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"Цирконій має найвищу міцність (до 1200 МПа) та біосумісність, тому ідеально підходить для жувальних зубів, мостів та коронок на імплантах. Кераміка E-max (дисилікат літію) має неперевершену світлопроникність і максимально повторює оптичні властивості живої емалі — це найкращий вибір для фронтальних зубів та вінірів. Металокераміка має металевий каркас, через що з часом може з'являтися темна смужка біля ясен." if is_ua else "Цирконий обладает максимальной прочностью (до 1200 МПа) и биосовместимостью, поэтому идеально подходит для жевательных зубов, мостов и коронок на имплантах. Керамика E-max (дисиликат лития) обладает непревзойденной светопроницаемостью и максимально повторяет оптику живой эмали — это лучший выбор для передних зубов и виниров. Металлокерамика имеет металлический каркас, из-за чего со временем может появляться темная полоска у десны."}
                            </div>
                        </div>
                    </div>

                    <!-- Q3 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Чи буде видно темний край коронки біля ясен?" if is_ua else "Будет ли виден темный край коронки возле десны?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"При встановленні цирконієвих коронок та кераміки E-max темний край неможливий, оскільки в матеріалах повністю відсутній метал. Коронка препарується з круговим уступом, завдяки чому край конструкції плавно ховається під ясенний контур, а ясна зберігають природний рожевий колір." if is_ua else "При установке циркониевых коронок и керамики E-max темный край невозможен, так как в материалах полностью отсутствует металл. Коронка препарируется с круговым уступом, благодаря чему край конструкции плавно прячется под десневой контур, а десна сохраняет естественный розовый цвет."}
                            </div>
                        </div>
                    </div>

                    <!-- Q4 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Що краще при відсутності одного зуба: мостоподібний протез чи імплант?" if is_ua else "Что лучше при отсутствии одного зуба: мостовидный протез или имплант?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"Імплантація — це золотий стандарт сучасної стоматології, оскільки вона дозволяє відновити втрачений зуб без обточування сусідніх здорових зубів та запобігає атрофії кістки. Мостоподібний протез є надійною альтернативою, якщо сусідні зуби вже мають великі пломби або коли імплантація тимчасово протипоказана." if is_ua else "Имплантация — это золотой стандарт современной стоматологии, так как она позволяет восстановить утраченный зуб без обточки соседних здоровых зубов и предотвращает атрофию кости. Мостовидный протез является надежной альтернативой, если соседние зубы уже имеют большие пломбы или когда имплантация временно противопоказана."}
                            </div>
                        </div>
                    </div>

                    <!-- Q5 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Скільки часу займає виготовлення коронки або моста?" if is_ua else "Сколько времени занимает изготовление коронки или моста?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"Завдяки цифровому скануванню 3Shape TRIOS 4 та лабораторному CAD/CAM моделюванню виготовлення постійної коронки займає 5–7 робочих днів. На цей період пацієнту одразу встановлюється тимчасова естетична коронка, яка захищає зуб від температурних подразників та відновлює естетику." if is_ua else "Благодаря цифровому сканированию 3Shape TRIOS 4 и лабораторному CAD/CAM моделированию изготовление постоянной коронки занимает 5–7 рабочих дней. На этот период пациенту сразу устанавливается временная эстетическая коронка, которая защищает зуб от температурных раздражителей и восстанавливает эстетику."}
                            </div>
                        </div>
                    </div>

                    <!-- Q6 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Чи боляче обточувати зуби під коронку?" if is_ua else "Больно ли обтачивать зубы под коронку?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"Процедура проходить абсолютно комфортно. Ми використовуємо сучасні карпульні анестетики артикаїнового ряду, які повністю блокують больову чутливість. Для депульпованих зубів процедура взагалі безболісна." if is_ua else "Процедура проходит абсолютно комфортно. Мы используем современные карпульные анестетики артикаинового ряда, которые полностью блокируют болевую чувствительность. Для депульпированных зубов процедура полностью безболезненна."}
                            </div>
                        </div>
                    </div>

                    <!-- Q7 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Що входить у ціну коронки «під ключ»?" if is_ua else "Что входит в стоимость коронки «под ключ»?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"У вартість, зазначену у прайсі, включено повний комплекс робіт: цифрове 3D-сканування 3Shape, виготовлення коронки в зуботехнічній лабораторії, примірка, корекція по прикусу та остаточна фіксація на адгезивний цемент. Якщо потрібне попереднє лікування каналів або відновлення кукси зуба штифтом, це розраховується окремо після огляду." if is_ua else "В стоимость, указанную в прайсе, включен полный комплекс работ: цифровое 3D-сканирование 3Shape, изготовление коронки в зуботехнической лаборатории, примерка, коррекция по прикусу и окончательная фиксация на адгезивный цемент. Если требуется предварительное лечение каналов или восстановление культи зуба штифтом, это рассчитывается отдельно после осмотра."}
                            </div>
                        </div>
                    </div>

                    <!-- Q8 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Який термін служби цирконієвих та керамічних коронок?" if is_ua else "Какой срок службы циркониевых и керамических коронок?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"При регулярній домашній гігієні та профілактичному чищенні кожні 6 місяців цирконієві коронки служать 10–15+ років. Матеріал не стирається, не вбирає харчові барвники і не втрачає первинного блиску." if is_ua else "При регулярной домашней гигиене и профилактической чистке каждые 6 месяцев циркониевые коронки служат 10–15+ лет. Материал не истирается, не впитывает пищевые красители и не теряет первоначального блеска."}
                            </div>
                        </div>
                    </div>

                    <!-- Q9 -->
                    <div class="accordion-item">
                        <div class="accordion-header" onclick="toggleAccordion(this)">
                            <span>{"Чи можна ставити коронки при бруксизмі (стисканні зубів)?" if is_ua else "Можно ли ставить коронки при бруксизме (сжатии зубов)?"}</span>
                            <span class="accordion-icon">+</span>
                        </div>
                        <div class="accordion-content">
                            <div class="accordion-body">
                                {"Так. Для пацієнтів із підвищеною стираністю та бруксизмом найкращим вибором є монолітний діоксид цирконію. Він має екстремальну міцність до механічних навантажень. Додатково після протезування ми виготовляємо індивідуальну нічну захисну капу." if is_ua else "Да. Для пациентов с повышенной стираемостью и бруксизмом лучшим выбором является монолитный диоксид циркония. Он обладает экстремальной прочностью к механическим нагрузкам. Дополнительно после протезирования мы изготавливаем индивидуальную ночную защитную каппу."}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Location Section -->
        <section class="tech-section">
            <div class="container">
                <h2 class="section-title">{loc_h2}</h2>
                <p class="section-subtitle">{"м. Одеса, вул. Новаторів, 1А (Київський район / Таїрова / Черемушки)" if is_ua else "г. Одесса, ул. Новаторов, 1А (Киевский район / Таирова / Черемушки)"}</p>
                <div style="border-radius: var(--radius); overflow: hidden; border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.06);">
                    <iframe
                        src="https://maps.google.com/maps?q=Harmony%20Dental%20Clinic%20Odesa%20Novatoriv%201A&t=&z=17&ie=UTF8&iwloc=&output=embed"
                        width="100%" height="420" style="border:0; display: block;" allowfullscreen="" loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer id="contacts" class="unified-footer" role="contentinfo">
        <div class="container">
            <div class="footer-content">
                <div>
                    <picture>
                        <source srcset="{img_pfx}images/Logo.webp" type="image/webp">
                        <img loading="lazy" src="{img_pfx}images/Logo.png" alt="Логотип Harmony Clinic" class="footer-logo-img" width="1072" height="1071">
                    </picture>
                    <p style="margin-top:10px;">{"Сучасна цифрова стоматологія в Одесі." if is_ua else "Современная цифровая стоматология в Одессе."}</p>
                    <div class="social-icons">
                        <a href="viber://chat?number=%2B380687794547" title="Viber" aria-label="Viber">
                            <svg viewBox="0 0 24 24"><path d="M22.2,16.6c-0.2-0.6-1.3-1.2-2.1-1.4c-0.8-0.2-1.3-0.1-1.8,0.7c-0.5,0.7-1,1.4-1.6,1.4c-0.5,0-1.9-0.5-3.6-2c-1.3-1.2-2.3-2.6-2.5-3s-0.1-1,0.6-1.7c0.5-0.5,1.1-1.3,1.3-1.8c0.2-0.5,0.1-1,0.1-1.4S10.8,3.9,10.2,2.5C9.5,1.1,8.9,1.4,8.4,1.4c-0.5,0-1.4,0-2.2,0.8c-0.9,0.9-3.2,3.1-3.2,7.5c0,4.4,3.2,8.7,3.7,9.3c0.5,0.6,6.3,9.5,15.2,12.5c5.3,1.8,7.3,1.7,8.6,1.5c1.4-0.1,4.5-1.8,5.1-3.6C26.3,17.7,22.8,17.9,22.2,16.6z" /></svg>
                        </a>
                        <a href="https://t.me/Harmonyclinic_od" target="_blank" title="Telegram" aria-label="Telegram">
                            <svg viewBox="0 0 24 24"><path d="M9.78,18.65l0.13-3.14l5.63-5.07c0.49-0.44-0.11-0.69-0.76-0.29L8.4,14.2l-3.03-0.95c-0.66-0.21-0.67-0.66,0.14-0.97L17.36,7.7c0.56-0.21,1.05,0.13,0.87,0.86L16.14,18.2c-0.12,0.59-0.87,0.72-1.41,0.45L9.78,18.65z" /></svg>
                        </a>
                        <a href="https://www.instagram.com/harmony.dental.clinic.od/" target="_blank" title="Instagram" aria-label="Instagram">
                            <svg viewBox="0 0 24 24"><path d="M12,2.2c3.2,0,3.6,0,4.9,0.1c1.2,0.1,1.8,0.3,2.2,0.5c0.6,0.2,1,0.5,1.4,0.9c0.4,0.4,0.7,0.8,0.9,1.4c0.2,0.4,0.4,1.1,0.5,2.2c0.1,1.3,0.1,1.6,0.1,4.9s0,3.6-0.1,4.9c-0.1,1.2-0.3,1.8-0.5,2.2c-0.2,0.6-0.5,1-0.9,1.4c-0.4,0.4-0.8,0.7-1.4,0.9c-0.4,0.2-1.1,0.4-2.2,0.5C8.4,2.2,8.8,2.2,12,2.2 M12,0C8.7,0,8.3,0,7.1,0.1C5.8,0.1,4.9,0.3,4.1,0.6C3.4,0.9,2.7,1.3,2,2s-1.1,1.4-1.4,2.2C0.3,4.9,0.1,5.8,0.1,7.1C0,8.3,0,8.7,0,12s0,3.7,0.1,4.9c0.1,1.3,0.3,2.1,0.6,2.9c0.3,0.8,0.7,1.5,1.4,2.2c0.7,0.7,1.4,1.1,2.2,1.4c0.8,0.3,1.7,0.5,2.9,0.6c1.2,0.1,1.6,0.1,4.9,0.1s3.7,0,4.9-0.1c1.3-0.1,2.1-0.3,2.9-0.6c0.8-0.3,1.5-0.7,2.2-1.4c0.7-0.7,1.1-1.4,1.4-2.2c0.3-0.8,0.5-1.7,0.6-2.9c0.1-1.2,0.1-1.6,0.1-4.9s0-3.7-0.1-4.9c-0.1-1.3-0.3-2.1-0.6-2.9c-0.3-0.8-0.7-1.5-1.4-2.2c-0.7-0.7-1.4-1.1-2.2-1.4c-0.8-0.3-1.7-0.5-2.9-0.6C15.7,0,15.3,0,12,0z M12,5.8c-3.4,0-6.2,2.8-6.2,6.2c0,3.4,2.8,6.2,6.2,6.2s6.2-2.8,6.2-6.2C18.2,8.6,15.4,5.8,12,5.8z M12,16c-2.2,0-4-1.8-4-4s1.8-4,4-4s4,1.8,4,4S14.2,16,12,16z M18.4,4.2c-0.8,0-1.4,0.6-1.4,1.4s0.6,1.4,1.4,1.4s1.4-0.6,1.4-1.4S19.2,4.2,18.4,4.2z" /></svg>
                        </a>
                    </div>
                </div>
                <div>
                    <h3>{"Меню" if is_ua else "Меню"}</h3>
                    <div class="footer-links">
                        <a href="{home_link}#about">> {"Про клініку" if is_ua else "О клинике"}</a>
                        <a href="{home_link}#prices">> {"Ціни" if is_ua else "Цены"}</a>
                        <a href="{root_pfx}offer.html">> {"Оферта" if is_ua else "Оферта"}</a>
                    </div>
                </div>
                <div>
                    <h3>{"Послуги" if is_ua else "Услуги"}</h3>
                    <div class="footer-links">
                        <a href="{implants_link}">> {"Імплантація" if is_ua else "Имплантация"}</a>
                        <a href="{prosthetics_link}">> {"Протезування" if is_ua else "Протезирование"}</a>
                        <a href="{treatment_link}">> {"Лікування" if is_ua else "Лечение"}</a>
                        <a href="{hygiene_link}">> {"Гігієна" if is_ua else "Гигиена"}</a>
                        <a href="{whitening_link}">> {"Відбілювання" if is_ua else "Отбеливание"}</a>
                        <a href="{ortho_link}">> {"Ортодонтія" if is_ua else "Ортодонтия"}</a>
                        <a href="{extraction_link}">> {"Видалення" if is_ua else "Удаление"}</a>
                    </div>
                </div>
                <div>
                    <h3>{"Контакти" if is_ua else "Контакты"}</h3>
                    <p>📍 {"м. Одеса, вул. Новаторів 1А" if is_ua else "г. Одесса, ул. Новаторов 1А"}</p>
                    <p style="margin-top:10px;">
                        <a href="tel:+380687794547" style="color:#fff; font-weight:700;" onclick="return gtag_report_call('tel:+380687794547');">📞 +38 068 779 45 47</a>
                    </p>
                </div>
            </div>
            <div class="copyright">Copyright © 2026 Harmony Clinic. All Rights Reserved.</div>
        </div>
    </footer>

    <!-- Floating Quick Call / Message Widget -->
    <a href="tel:+380687794547" class="floating-widget" onclick="return gtag_report_call('tel:+380687794547');" aria-label="Зателефонувати">
        <div class="widget-icon">
            <svg viewBox="0 0 24 24"><path d="M22.2,16.6c-0.2-0.6-1.3-1.2-2.1-1.4c-0.8-0.2-1.3-0.1-1.8,0.7c-0.5,0.7-1,1.4-1.6,1.4c-0.5,0-1.9-0.5-3.6-2c-1.3-1.2-2.3-2.6-2.5-3s-0.1-1,0.6-1.7c0.5-0.5,1.1-1.3,1.3-1.8c0.2-0.5,0.1-1,0.1-1.4S10.8,3.9,10.2,2.5C9.5,1.1,8.9,1.4,8.4,1.4c-0.5,0-1.4,0-2.2,0.8c-0.9,0.9-3.2,3.1-3.2,7.5c0,4.4,3.2,8.7,3.7,9.3c0.5,0.6,6.3,9.5,15.2,12.5c5.3,1.8,7.3,1.7,8.6,1.5c1.4-0.1,4.5-1.8,5.1-3.6C26.3,17.7,22.8,17.9,22.2,16.6z"/></svg>
        </div>
    </a>

    <!-- Interactive Carousel & Accordion Script -->
    <script>
        let currentSlide = 0;
        function getSlidesPerView() {{
            return window.innerWidth <= 768 ? 1 : 2;
        }}

        function updateCarousel() {{
            const track = document.getElementById('carouselTrack');
            const slides = document.querySelectorAll('.carousel-slide');
            const totalSlides = slides.length;
            if (!track || totalSlides === 0) return;

            const slidesPerView = getSlidesPerView();
            const maxSlide = Math.max(0, totalSlides - slidesPerView);

            if (currentSlide > maxSlide) currentSlide = maxSlide;
            if (currentSlide < 0) currentSlide = 0;

            const slideWidth = 100 / slidesPerView;
            track.style.transform = `translateX(-${{currentSlide * slideWidth}}%)`;
            renderDots(maxSlide);
        }}

        function renderDots(maxSlide) {{
            const dotsBox = document.getElementById('carouselDots');
            if (!dotsBox) return;
            const total = maxSlide + 1;
            if (dotsBox.children.length !== total) {{
                dotsBox.innerHTML = '';
                for (let i = 0; i < total; i++) {{
                    const b = document.createElement('button');
                    b.className = 'carousel-dot';
                    b.setAttribute('aria-label', `Слайд ${{i + 1}}`);
                    b.addEventListener('click', () => {{ currentSlide = i; updateCarousel(); }});
                    dotsBox.appendChild(b);
                }}
            }}
            [...dotsBox.children].forEach((d, i) => {{
                d.classList.toggle('active', i === currentSlide);
            }});
        }}

        function moveSlide(direction) {{
            const slides = document.querySelectorAll('.carousel-slide');
            const maxSlide = Math.max(0, slides.length - getSlidesPerView());
            currentSlide += direction;
            if (currentSlide < 0) currentSlide = maxSlide;
            if (currentSlide > maxSlide) currentSlide = 0;
            updateCarousel();
        }}

        window.addEventListener('resize', updateCarousel);
        document.addEventListener('DOMContentLoaded', updateCarousel);

        function toggleAccordion(header) {{
            const item = header.parentElement;
            const content = item.querySelector('.accordion-content');
            const icon = header.querySelector('.accordion-icon');
            const isOpen = item.classList.contains('active');

            document.querySelectorAll('.accordion-item').forEach(el => {{
                el.classList.remove('active');
                const c = el.querySelector('.accordion-content');
                if (c) c.style.maxHeight = null;
                const ic = el.querySelector('.accordion-icon');
                if (ic) ic.textContent = '+';
            }});

            if (!isOpen) {{
                item.classList.add('active');
                content.style.maxHeight = content.scrollHeight + 'px';
                if (icon) icon.textContent = '−';
            }}
        }}

        function toggleMenu() {{
            const menu = document.getElementById('navMenu');
            if (menu) {{
                menu.classList.toggle('active');
            }}
        }}
    </script>
</body>
</html>"""

def main():
    ua_path = "/Users/doc/Desktop/Сайт/Harmony Dental Clinic/prosthetics-ua.html"
    ru_path = "/Users/doc/Desktop/Сайт/Harmony Dental Clinic/ru/prosthetics-ua.html"
    
    with open(ua_path, "w", encoding="utf-8") as f:
        f.write(get_html('ua'))
    print(f"Updated UA: {ua_path}")
    
    with open(ru_path, "w", encoding="utf-8") as f:
        f.write(get_html('ru'))
    print(f"Updated RU: {ru_path}")

if __name__ == "__main__":
    main()
