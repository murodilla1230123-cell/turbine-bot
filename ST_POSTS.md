# @enersok_edu — ST postlar to'plami
**Manba:** SYR2-073-MAN-OM-3625 Rev.00, Harbin Electric, 371 bet
**Qamrov:** faqat bug' turbinasi (ST) va uning yordamchi tizimlari

---
---

## POST 1 — ST asosiy parametrlari

**🇺🇿 ST asosiy parametrlari — Syrdarya 2 (1600 MW CC)**

Reference site sharoitida:

| Nuqta | Bosim | Harorat | Sarf |
|---|---|---|---|
| HP stop valve kirish | 164.57 bar.a | 600°C | 972.576 t/s |
| IP stop valve kirish | 38.89 bar.a | 610°C | 1094.652 t/s |
| LP admission kirish | 4.902 bar.a | 330.4°C | 136.5516 t/s |
| LP exhaust | 0.045 bar.a | 31.014°C | 1238.328 t/s |
| Steam seal header | 1.29 bar.a | — | — |

Konfiguratsiya: **HIP–LPA2F–LPB2F** (3 korpus, LP ikki oqimli)
Chastota ish oralig'i: **48.5–51 Hz**
Upor podshipnik: tilting pad, HIP front
HP/IP journal: tilting pad | LP journal: elliptik
Turning gear: LPB orqasida
Korpuslar: gorizontal ajraladigan, HIP va LP — double casing

Ishga tushirish vaqtlari (rotor metall haroratiga qarab):
• **Cold — 170 min** (trip'dan 96 soat keyin)
• **Warm — 96 min** (48 soat keyin)
• **Hot — 30 min** (2 soat keyin)

---

**🇷🇺 Основные параметры ПТ — Сырдарья 2 (1600 МВт ПГУ)**

| Точка | Давление | Темп. | Расход |
|---|---|---|---|
| Вход ГСК ЦВД | 164.57 бар.а | 600°C | 972.576 т/ч |
| Вход ГСК ЦСД | 38.89 бар.а | 610°C | 1094.652 т/ч |
| Вход НД | 4.902 бар.а | 330.4°C | 136.5516 т/ч |
| Выхлоп НД | 0.045 бар.а | 31.014°C | 1238.328 т/ч |
| Коллектор уплотнений | 1.29 бар.а | — | — |

Конфигурация: **HIP–LPA2F–LPB2F** (3 цилиндра, ЦНД двухпоточный)
Диапазон частоты: **48.5–51 Гц**
Упорный подшипник: сегментный, перед ЦВСД
Опорные ВД/СД: сегментные | НД: эллиптические
ВПУ: за ЦНД-B

Пуски: **холодный 170 мин** (через 96 ч) / **тёплый 96 мин** (48 ч) / **горячий 30 мин** (2 ч)

---

**🇬🇧 ST Main Parameters — Syrdarya 2 (1600 MW CC)**

| Point | Pressure | Temp | Flow |
|---|---|---|---|
| HP stop valve inlet | 164.57 bar.a | 600°C | 972.576 t/h |
| IP stop valve inlet | 38.89 bar.a | 610°C | 1094.652 t/h |
| LP admission inlet | 4.902 bar.a | 330.4°C | 136.5516 t/h |
| LP exhaust | 0.045 bar.a | 31.014°C | 1238.328 t/h |
| Steam seal header | 1.29 bar.a | — | — |

Configuration: **HIP–LPA2F–LPB2F**
Frequency range: **48.5–51 Hz**
Thrust bearing: tilting pad, HIP front
HP/IP journal: tilting pad | LP journal: elliptical

Start-up: **cold 170 min / warm 96 min / hot 30 min**

`#steamturbine #parameters #syrdarya2`

---
---

## POST 2 — ST TRIP setpointlari (Table 8-1-1)

**🇺🇿 ST TRIP setpointlari — yoddan bilish shart**

**Podshipnik metalli**
• №1, 2: alarm **>116°C** | trip **>127°C**
• №3–8: alarm **>107°C** | trip **>121°C**
• Upor podshipnik: alarm **>105°C** | trip **>115°C**

**Tebranish (journal №1–8)**
• Alarm **>165 μm** | trip **>240 μm**

**Upor podshipnik o'q bo'yicha siljish**
• Alarm **>±0.762 mm** | trip **>±0.889 mm**

**Differensial kengayish (DXD №1/2)**
• H alarm **>11.07 mm** | HH trip **>12.07 mm**
• L alarm **<−8.26 mm** | LL trip **<−9.26 mm**

**Rotor kengayishi (№1/2)**
• H alarm **>44.5 mm** | HH trip **>45.5 mm**
• L alarm **<−22.1 mm** | LL trip **<−23.1 mm**

**Aylanish**
• Birlamchi overspeed trip (110%): **>3300 rpm**
• Avariya overspeed trip TCS moduldan (113%): **>3330 rpm**
• Primary/protective tezlik farqi: **>150 rpm** → trip
• Tezlanish/sekinlashish tezligi: **>450 rpm/sek** → trip

**Yog'**
• Lube oil bosim LL: **<0.04 MPa.g** → trip
• Lube oil sath LL: **<1200 mm** → trip
• Gidravlik suyuqlik sath LL: **<357 mm** → trip
• Gidravlik suyuqlik bosim LL: **<11 MPa.g** → trip

**Bug'**
• HP exhaust harorat: **>450°C, 15 min kechikish** → trip | **>470°C** → darhol trip
• LP exhaust harorat HH: **>105°C** → trip
• LP exhaust bosim: alarm **>0.35 bar.a** | trip **>0.45 bar.a**
• HP/IP bug' harorati pasayishi: **<−83°C** → trip

**Generator**
• Stator sovutish suvi sarfi LL: **<54.1 m³/s** → trip
• Stator o'ram sovutish suvi chiqish harorati HH: **>83°C** → trip

---

**🇷🇺 Уставки защит ПТ — знать наизусть**

**Металл подшипников**
• №1, 2: сигнал **>116°C** | защита **>127°C**
• №3–8: сигнал **>107°C** | защита **>121°C**
• Упорный: сигнал **>105°C** | защита **>115°C**

**Вибрация (опоры №1–8)**
• Сигнал **>165 мкм** | защита **>240 мкм**

**Осевой сдвиг**
• Сигнал **>±0.762 мм** | защита **>±0.889 мм**

**Относительное расширение (ОРС №1/2)**
• H **>11.07 мм** | HH **>12.07 мм**
• L **<−8.26 мм** | LL **<−9.26 мм**

**Расширение ротора (№1/2)**
• H **>44.5 мм** | HH **>45.5 мм**
• L **<−22.1 мм** | LL **<−23.1 мм**

**Обороты**
• Первичная защита от разгона (110%): **>3300 об/мин**
• Аварийная от выделенного модуля TCS (113%): **>3330 об/мин**
• Расхождение первичного и защитного датчиков: **>150 об/мин** → защита
• Скорость разгона/выбега: **>450 об/мин·с** → защита

**Масло**
• Давление смазки LL: **<0.04 МПа.g** → защита
• Уровень маслобака LL: **<1200 мм** → защита
• Уровень ОГ LL: **<357 мм** → защита
• Давление ОГ LL: **<11 МПа.g** → защита

**Пар**
• Темп. выхлопа ЦВД: **>450°C с выдержкой 15 мин** | **>470°C** мгновенно
• Темп. выхлопа ЦНД HH: **>105°C**
• Давление выхлопа ЦНД: сигнал **>0.35 бар.а** | защита **>0.45 бар.а**
• Снижение темп. пара ВД/СД: **<−83°C** → защита

**Генератор**
• Расход статорной воды LL: **<54.1 м³/ч** → защита
• Темп. статорной воды на выходе HH: **>83°C** → защита

---

**🇬🇧 ST Trip Settings — must know**

**Bearing metal**
• #1, 2: alarm **>116°C** | trip **>127°C**
• #3–8: alarm **>107°C** | trip **>121°C**
• Thrust: alarm **>105°C** | trip **>115°C**

**Vibration (journal #1–8)**
• Alarm **>165 μm** | trip **>240 μm**

**Thrust axial position**
• Alarm **>±0.762 mm** | trip **>±0.889 mm**

**Differential expansion #1/2**
• H **>11.07 mm** | HH **>12.07 mm** | L **<−8.26 mm** | LL **<−9.26 mm**

**Rotor expansion #1/2**
• H **>44.5 mm** | HH **>45.5 mm** | L **<−22.1 mm** | LL **<−23.1 mm**

**Speed**
• Primary overspeed trip (110%): **>3300 rpm**
• Emergency overspeed trip, dedicated TCS module (113%): **>3330 rpm**
• Primary/protective speed deviation: **>150 rpm** → trip
• Accel/decel rate: **>450 rpm/sec** → trip

**Oil**
• Lube oil pressure LL **<0.04 MPa.g** | level LL **<1200 mm**
• Hydraulic fluid level LL **<357 mm** | pressure LL **<11 MPa.g**

**Steam**
• HP exhaust temp **>450°C 15 min delay** | **>470°C** immediate
• LP exhaust temp HH **>105°C**
• LP exhaust pressure alarm **>0.35 bar.a** | trip **>0.45 bar.a**
• HP/IP steam downward temp **<−83°C** → trip

`#trip #protection #steamturbine`

---
---

## POST 3 — ST trip zanjiri: KKS teglari va ovoz berish mantiqi

**🇺🇿 ST trip — KKS teglari va 2/3 mantiqi**

Quyidagilardan **istalgan bittasi** bajarilsa ST trip bo'ladi:

**Yog' tizimi**
• Lube oil bosim LL — 10MAV40CP005A/B/C, **MED**, <0.04 MPa.g
• Lube oil sath LL — 10MAV10CL001A/B/C, **MED**, <1200 mm
• Gidravlik bosim LL — 10MAX00CL001A/B/C, **MED**, <11 MPa.g
• Gidravlik sath LL — 10MAX00CL001A/B/C, <357 mm

**Bug'**
• HP exhaust harorat — 10MAA11CT009A/B/C, >450°C 15 min yoki >470°C
• LP A exhaust — 10MAC11CT003A/B/C, >105°C
• LP B exhaust — 10MAC12CT003A/B/C, >105°C
• LP exhaust bosim — 10MAC11CP002/003A/B/C, MED, >0.45 bar.a
  *(shart: primary speed 10MAA10CS001A/B/C MED >300 rpm)*
• HP bug' harorat pasayishi — 10LBA12CT001A/B + 10LBA11CT001C, MED, 15 min
• IP bug' harorat pasayishi — 10LBB12CT001A/B + 10LBB11CT001C, MED, 15 min

**Podshipniklar**
• №1,2 metall — 10MAD11CT001, 10MAD12CT001, **1of2**, >127°C
• №3–8 metall — 10MAD13...18CT001, **1of6**, >127°C
• Upor active face — 10MAD50CT001/002, **MAX**, >115°C
• Upor inactive face — 10MAD50CT003/004, **MAX**, >115°C
• Tebranish HH — 10MAD21...28CY012X/012Y, **1/16**, >240 μm (STG VMS'dan)

**Generator**
• Stator suv sarfi LL — 10MKF09CF002A/B/C, MED, <54.1 m³/s, **15 sek kechikish**
• Stator suv chiqish harorati HH — 10MKF11CT001A/B/C, MED, >83°C, **15 sek**
• Stator suv kirish bosimi LL — 10MKF09CP001A/B/C, MED, **15 sek**

**Tezlik**
• Primary/protective farq >5% (150 rpm) — 10MAA10CS001 va CS002
• Primary va nol tezlik farqi >0.04% (**1.2 rpm**)
• Tezlanish/sekinlashish tezligi juda yuqori

**Boshqa**
• TCS ikkala kontroller trip yoki quvvat yo'qolishi
• Front standard'dagi avariya tugmasi
• Off-line ETD test trip
• Auto shutdown trip
• DCS'dan mijoz trip komandasi, **2/3**
• GPR'dan generator himoyasi lock-out, **2/3**

⚠️ **Diqqat:** podshipnik metall trip'i №1,2 uchun **1of2**, №3–8 uchun **1of6** — ya'ni bitta datchik yetarli. Tebranish esa **1/16**.

---

**🇷🇺 Защиты ПТ — KKS-теги и логика голосования**

Срабатывание **любого** условия отключает ПТ:

**Маслосистема**
• Давление смазки LL — 10MAV40CP005A/B/C, **MED**, <0.04 МПа.g
• Уровень маслобака LL — 10MAV10CL001A/B/C, **MED**, <1200 мм
• Давление ОГ LL — 10MAX00CL001A/B/C, **MED**, <11 МПа.g
• Уровень ОГ LL — 10MAX00CL001A/B/C, <357 мм

**Пар**
• Темп. выхлопа ЦВД — 10MAA11CT009A/B/C, >450°C 15 мин или >470°C
• Выхлоп ЦНД-A — 10MAC11CT003A/B/C, >105°C
• Выхлоп ЦНД-B — 10MAC12CT003A/B/C, >105°C
• Давление выхлопа ЦНД — 10MAC11CP002/003A/B/C, MED, >0.45 бар.а
  *(условие: 10MAA10CS001A/B/C MED >300 об/мин)*
• Снижение темп. пара ВД — 10LBA12CT001A/B + 10LBA11CT001C, MED, 15 мин
• Снижение темп. пара СД — 10LBB12CT001A/B + 10LBB11CT001C, MED, 15 мин

**Подшипники**
• Металл №1,2 — 10MAD11CT001, 10MAD12CT001, **1из2**, >127°C
• Металл №3–8 — 10MAD13...18CT001, **1из6**, >127°C
• Упорный рабочая сторона — 10MAD50CT001/002, **MAX**, >115°C
• Упорный нерабочая сторона — 10MAD50CT003/004, **MAX**, >115°C
• Вибрация HH — 10MAD21...28CY012X/012Y, **1/16**, >240 мкм

**Генератор**
• Расход статорной воды LL — 10MKF09CF002A/B/C, MED, <54.1 м³/ч, **15 с**
• Темп. на выходе HH — 10MKF11CT001A/B/C, MED, >83°C, **15 с**
• Давление на входе LL — 10MKF09CP001A/B/C, MED, **15 с**

**Обороты**
• Расхождение первичного и защитного >5% (150 об/мин)
• Расхождение первичного и нулевого >0.04% (**1.2 об/мин**)
• Слишком высокая скорость разгона/выбега

**Прочее**
• Отказ обоих контроллеров TCS или потеря питания
• Кнопка аварийного останова на переднем стуле
• Off-line ETD тест
• Автоматический останов
• Команда от DCS, **2/3**
• Lock-out защиты генератора от GPR, **2/3**

⚠️ Металл подшипников №1,2 — **1из2**, №3–8 — **1из6**: достаточно одного датчика. Вибрация — **1/16**.

---

**🇬🇧 ST Trip — KKS tags and voting logic**

**Any one** of the following trips the ST:

**Oil**
• Lube oil pressure LL — 10MAV40CP005A/B/C, **MED**, <0.04 MPa.g
• Lube oil level LL — 10MAV10CL001A/B/C, **MED**, <1200 mm
• Hydraulic pressure LL — 10MAX00CL001A/B/C, **MED**, <11 MPa.g
• Hydraulic level LL — 10MAX00CL001A/B/C, <357 mm

**Steam**
• HP exhaust temp — 10MAA11CT009A/B/C, >450°C 15 min or >470°C
• LP A exhaust — 10MAC11CT003A/B/C, >105°C
• LP B exhaust — 10MAC12CT003A/B/C, >105°C
• LP exhaust pressure — 10MAC11CP002/003A/B/C, MED, >0.45 bar.a
  *(AND primary speed 10MAA10CS001A/B/C MED >300 rpm)*
• HP steam downward temp — 10LBA12CT001A/B + 10LBA11CT001C, MED, 15 min
• IP steam downward temp — 10LBB12CT001A/B + 10LBB11CT001C, MED, 15 min

**Bearings**
• #1,2 metal — 10MAD11CT001, 10MAD12CT001, **1of2**, >127°C
• #3–8 metal — 10MAD13...18CT001, **1of6**, >127°C
• Thrust active — 10MAD50CT001/002, **MAX**, >115°C
• Thrust inactive — 10MAD50CT003/004, **MAX**, >115°C
• Vibration HH — 10MAD21...28CY012X/012Y, **1/16**, >240 μm

**Generator**
• Stator water flow LL — 10MKF09CF002A/B/C, MED, <54.1 m³/h, **15 s delay**
• Stator water outlet temp HH — 10MKF11CT001A/B/C, MED, >83°C, **15 s**
• Stator water inlet pressure LL — 10MKF09CP001A/B/C, MED, **15 s**

**Speed**
• Primary/protective deviation >5% (150 rpm)
• Primary vs zero speed deviation >0.04% (**1.2 rpm**)
• Accel/decel rate too high

**Other**
• Both TCS controllers trip or power fail
• Emergency trip push button, front standard
• Off-line ETD test trip | Auto shutdown trip
• Customer trip from DCS, **2/3** | Generator lock-out from GPR, **2/3**

`#trip #KKS #protection`

---
---

## POST 4 — ST Lube Oil tizimi (10MAV)

**🇺🇿 ST Lube Oil (10MAV) — setpointlar va mantiq**

**Alarm / trip jadvali**
| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Lube oil bosim L | <0.7 barg | Alarm |
| Lube oil bosim LL | <0.4 barg | **Trip** |
| Bak sath H | normal +100 mm | Alarm |
| Bak sath HH | normal +400 mm | **Trip** |
| Bak sath L | normal −100 mm | Alarm |
| Bak sath LL | normal −400 mm | **Trip** |
| Bak vakuum L | >−1.18 mbarg | Alarm |
| Filtr Δp | >0.5 bar | Alarm |
| Sovutgich chiqish harorat H | >49°C | Alarm |
| — turning gear rejimida H | >32°C | Alarm |
| Sovutgich chiqish harorat L (nominal aylanish) | <43°C | Alarm |
| — turning gear rejimida L | <10°C | Alarm |

**Ishga tushirish tartibi**
1. Vapor extractor A/B → start
2. Bak vakuumi **<−1.18 mbar** ekanini tekshir
3. Ikkinchi vapor extractor → **Auto**
4. Asosiy MOP A/B → start
5. Kollektor bosimi **1.5–1.7 bar.g** ekanini tekshir
6. Ikkinchi MOP → **Auto**
7. EBOP → **Auto** (joyidagi shchitdan!)

**Avto-ishga tushish zanjiri**
• 1-bosqich: **PS 10MAV17CP101A/B** → zaxira MOP
• 2-bosqich: **PS 10MAV40CP101A/B** → EBOP 10MAV27AP001
• EBOP AC quvvat yo'qolganda ham kiradi

**Smenada bilish kerak bo'lgan 4 nuqta**
1. Zaxira MOP past bosimda kiradi, bosim tiklanganda **o'zi to'xtamaydi** — faqat qo'lda. Sikllanishga qarshi.
2. EBOP overload relesi **trip qilmaydi, faqat alarm**. Ataylab shunday.
3. MOP-A va MOP-B **alohida mustaqil manbadan**. Bitta manbadan bo'lsa — o'tish **1 sekunddan kam** bo'lishi shart.
4. Zaxira MOP avto-kirmasa: **electrical fault / locked out / failed to start** — shu uchtasini tekshir.

**Tizimni to'xtatish shartlari — hammasi bajarilishi shart**
☑ ST to'xtagan
☑ HRSG#1 va HRSG#2 to'xtagan
☑ HP, IP, LP bypass to'liq yopiq
☑ Kondensator vakuumi olib tashlangan
☑ Gland steam ishdan chiqarilgan
☑ Turning gear ishdan chiqarilgan
☑ Jacking oil ishdan chiqarilgan
☑ Generator H2 → CO2 → havo bilan almashtirilgan

Uskuna: bak 10MAV10BB001 | MOP-A 10MAV23AP001 | MOP-B 10MAV24AP001 | EBOP 10MAV27AP001 | sovutgich 10MAV31/32AC001 | duplex filtr 10MAV33AT001

---

**🇷🇺 Маслосистема ПТ (10MAV) — уставки и логика**

| Параметр | Уставка | Действие |
|---|---|---|
| Давление масла L | <0.7 барг | Сигнал |
| Давление масла LL | <0.4 барг | **Защита** |
| Уровень бака H | норма +100 мм | Сигнал |
| Уровень бака HH | норма +400 мм | **Защита** |
| Уровень бака L | норма −100 мм | Сигнал |
| Уровень бака LL | норма −400 мм | **Защита** |
| Разрежение в баке L | >−1.18 мбарг | Сигнал |
| Δp фильтра | >0.5 бар | Сигнал |
| Темп. на выходе МО H | >49°C | Сигнал |
| — на ВПУ H | >32°C | Сигнал |
| Темп. на выходе МО L (ном. обороты) | <43°C | Сигнал |
| — на ВПУ L | <10°C | Сигнал |

**Порядок пуска**
1. Эксгаустер A/B → пуск
2. Разрежение в баке **<−1.18 мбар**
3. Второй эксгаустер → **Авто**
4. Основной МНС A/B → пуск
5. Давление в коллекторе **1.5–1.7 бар.g**
6. Второй МНС → **Авто**
7. АМН → **Авто** (с местного шкафа!)

**Цепочка АВР**
• 1 ступень: **PS 10MAV17CP101A/B** → резервный МНС
• 2 ступень: **PS 10MAV40CP101A/B** → АМН 10MAV27AP001
• АМН запускается также при потере питания AC

**4 момента для смены**
1. Резервный МНС запускается по низкому давлению, но **сам не останавливается** — только вручную.
2. Тепловое реле АМН **не отключает насос, только сигнал**. Сделано намеренно.
3. МНС-A и МНС-B от **раздельных независимых источников**. Иначе переключение **менее 1 секунды**.
4. Резервный не запустился — проверь: **electrical fault / locked out / failed to start**.

**Условия вывода системы — все обязательны**
☑ ПТ остановлена ☑ КУ №1 и №2 остановлены ☑ БРОУ ВД/СД/НД закрыты
☑ Вакуум сорван ☑ Уплотняющий пар выведен ☑ ВПУ выведено
☑ Гидроподъём выведен ☑ H2 вытеснен CO2 и воздухом

---

**🇬🇧 ST Lube Oil (10MAV) — settings and logic**

| Item | Setting | Action |
|---|---|---|
| Lube oil pressure L | <0.7 barg | Alarm |
| Lube oil pressure LL | <0.4 barg | **Trip** |
| Reservoir level H | normal +100 mm | Alarm |
| Reservoir level HH | normal +400 mm | **Trip** |
| Reservoir level L | normal −100 mm | Alarm |
| Reservoir level LL | normal −400 mm | **Trip** |
| Reservoir vacuum L | >−1.18 mbarg | Alarm |
| Filter Δp | >0.5 bar | Alarm |
| Cooler outlet temp H | >49°C | Alarm |
| — on turning gear H | >32°C | Alarm |
| Cooler outlet temp L (rated speed) | <43°C | Alarm |
| — on turning gear L | <10°C | Alarm |

**Start-up sequence**
1. Vapor extractor A/B → start
2. Confirm reservoir vacuum **<−1.18 mbar**
3. Second vapor extractor → **Auto**
4. Main lube oil pump A/B → start
5. Confirm header pressure **1.5–1.7 bar.g**
6. Second MOP → **Auto**
7. EBOP → **Auto** (site control cabinet!)

**Auto-start chain**
• Stage 1: **PS 10MAV17CP101A/B** → standby MOP
• Stage 2: **PS 10MAV40CP101A/B** → EBOP 10MAV27AP001
• EBOP also starts on loss of AC power

**4 points for the shift**
1. Standby MOP auto-starts on low pressure but **does not auto-stop** — manual only.
2. EBOP overload relay **alarms only, does not trip**. Deliberate.
3. MOP-A and MOP-B on **separate independent supplies**. Otherwise transfer must be **under 1 second**.
4. Standby didn't start — check **electrical fault / locked out / failed to start**.

**Shutdown permissives — all required**
☑ ST shut down ☑ HRSG#1 & #2 shut down ☑ HP/IP/LP bypass fully closed
☑ Condenser vacuum out ☑ Gland steam out ☑ Turning gear out
☑ Jacking oil out ☑ H2 replaced by CO2 then air

`#luboil #MOP #EBOP #10MAV`

---
---

## POST 5 — EH boshqaruv yog'i (gidravlik)

**🇺🇿 Control oil / EH — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Kollektor bosimi L | 131 bar(g) | Alarm |
| Kollektor bosimi LL | 110 bar(g) | **Trip** |
| Harorat L | 18°C | Alarm |
| Harorat H | 65.6°C | Alarm |
| Supply filtr | 8 bar(g) | Alarm |
| Conditioning filtr | 5 bar(g) | Alarm |
| Polishing filtr | 5 bar(g) | Alarm |
| Bak sath H | >657 mm | Alarm |
| Bak sath L | <457 mm | Alarm |
| Bak sath LL | <357 mm | **Trip** |

**Qizdirgich va sovutgich interloklari**
• Qizdirish **YOQ**: <29.4°C
• Qizdirish **O'CHDI**: >35°C
• Sovutish **YOQ**: >49°C
• Sovutish **O'CHDI**: <43°C

**Ishga tushirish**
1. Nasos kirish/chiqish qo'l ventillari ochiq
2. Akkumulyator drenaj ventillari yopiq
3. Bak sathi va harorati normal
4. Nasos start → **kollektor bosimi 165 bar.g** ekanini tekshir
5. Ikkinchi nasos → **Auto**

⚠️ Nominal ish bosimi **165 bar.g**, alarm **131 bar.g**da, trip **110 bar.g**da. Ya'ni nominaldan trip'gacha 55 bar zaxira bor — bosim tushayotgani ko'rinsa, trip'ni kutmasdan sabab qidiring.

Tizimni faqat **ST to'xtaganidan keyin** ishdan chiqarish mumkin.

---

**🇷🇺 Система ОГ (ЭГСР) — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Давление в коллекторе L | 131 бар(g) | Сигнал |
| Давление в коллекторе LL | 110 бар(g) | **Защита** |
| Температура L | 18°C | Сигнал |
| Температура H | 65.6°C | Сигнал |
| Фильтр подачи | 8 бар(g) | Сигнал |
| Кондиционирующий фильтр | 5 бар(g) | Сигнал |
| Полирующий фильтр | 5 бар(g) | Сигнал |
| Уровень бака H | >657 мм | Сигнал |
| Уровень бака L | <457 мм | Сигнал |
| Уровень бака LL | <357 мм | **Защита** |

**Блокировки нагрева/охлаждения**
• Нагрев **ВКЛ** <29.4°C | **ВЫКЛ** >35°C
• Охлаждение **ВКЛ** >49°C | **ВЫКЛ** <43°C

**Пуск**
1. Ручные задвижки на входе/выходе насоса открыты
2. Дренажи гидроаккумуляторов закрыты
3. Уровень и температура в баке в норме
4. Пуск насоса → **давление в коллекторе 165 бар.g**
5. Второй насос → **Авто**

⚠️ Номинал **165 бар.g**, сигнал на **131**, защита на **110**. Запас 55 бар — при падении давления ищите причину, не дожидаясь защиты.

Вывод системы только **после останова ПТ**.

---

**🇬🇧 Control Oil / EH — settings**

| Item | Setting | Action |
|---|---|---|
| Header pressure L | 131 bar(g) | Alarm |
| Header pressure LL | 110 bar(g) | **Trip** |
| Temperature L | 18°C | Alarm |
| Temperature H | 65.6°C | Alarm |
| Supply filter | 8 bar(g) | Alarm |
| Conditioning filter | 5 bar(g) | Alarm |
| Polishing filter | 5 bar(g) | Alarm |
| Tank level H | >657 mm | Alarm |
| Tank level L | <457 mm | Alarm |
| Tank level LL | <357 mm | **Trip** |

**Heater / cooler interlocks**
• Heating **ON** <29.4°C | **OFF** >35°C
• Cooling **ON** >49°C | **OFF** <43°C

**Start-up**
1. Pump inlet/outlet manual valves open
2. Accumulator drain valves closed
3. Reservoir level and temperature normal
4. Start pump → confirm header pressure **165 bar.g**
5. Second pump → **Auto**

⚠️ Normal **165 bar.g**, alarm at **131**, trip at **110** — 55 bar of margin. If pressure is drifting down, find the cause before the trip finds you.

System out of service only **after ST shutdown**.

`#EHoil #controloil #hydraulic`

---
---

## POST 6 — Jacking oil tizimi

**🇺🇿 Jacking oil — setpointlar va ketma-ketlik**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| So'rish filtri Δp H | >0.5 bar | Alarm |
| Chiqish filtri Δp H | >0.5 bar | Alarm |
| So'rish bosimi L | <0.1 bar | Alarm |
| Kollektor bosimi L | <60 bar | Alarm |

**Ishga tushirishdan oldin — ruxsat shartlari**
☑ Lube oil tizimi normal ishlayapti
☑ Lube oil → jacking oil qo'l ventili **ochiq**
☑ Nasos kirish/chiqish qo'l ventillari ochiq
☑ Nasos vent ventillari ochiq
☑ Nasos bypass qo'l ventili **yopiq**
☑ Nasos kirish bosimi **≥0.1 bar.g**
☑ Lube oil kollektor bosimi **1.7 bar.g**

**Ishga tushirish**
1. Jacking oil nasos A/B → start
2. **Kollektor bosimi 150 bar.g** ekanini tekshir
3. Ikkinchi nasos → **Auto**

⚠️ Nominal **150 bar**, alarm **60 bar**da. 60 bar juda past — bu alarm chiqsa, val allaqachon ko'tarilmayotgan bo'lishi mumkin. Turning gear ishlayotganda bu jiddiy.

⚠️ Lube oil kollektorida **1.7 bar** bo'lishi shart — jacking nasos lube oil'dan so'radi. Lube oil bosimi past bo'lsa jacking oil ham ishlamaydi.

---

**🇷🇺 Гидроподъём ротора — уставки и последовательность**

| Параметр | Уставка | Действие |
|---|---|---|
| Δp фильтра на всасе H | >0.5 бар | Сигнал |
| Δp фильтра на нагнетании H | >0.5 бар | Сигнал |
| Давление на всасе L | <0.1 бар | Сигнал |
| Давление в коллекторе L | <60 бар | Сигнал |

**Условия перед пуском**
☑ Маслосистема в нормальной работе
☑ Ручная задвижка смазка → гидроподъём **открыта**
☑ Задвижки на входе/выходе насоса открыты
☑ Воздушники насоса открыты
☑ Байпас насоса **закрыт**
☑ Давление на всасе **≥0.1 бар.g**
☑ Давление в коллекторе смазки **1.7 бар.g**

**Пуск**
1. Насос гидроподъёма A/B → пуск
2. **Давление в коллекторе 150 бар.g**
3. Второй насос → **Авто**

⚠️ Номинал **150 бар**, сигнал на **60**. Если сигнал пришёл — вал, возможно, уже не приподнят. На ВПУ это серьёзно.

⚠️ Насос гидроподъёма берёт масло из системы смазки. Нет **1.7 бар** в коллекторе смазки — не будет и гидроподъёма.

---

**🇬🇧 Jacking Oil — settings and sequence**

| Item | Setting | Action |
|---|---|---|
| Suction filter Δp H | >0.5 bar | Alarm |
| Discharge filter Δp H | >0.5 bar | Alarm |
| Suction pressure L | <0.1 bar | Alarm |
| Header pressure L | <60 bar | Alarm |

**Permissives before start**
☑ Lube oil system in normal operation
☑ Lube oil → jacking oil manual isolation **open**
☑ Pump inlet/outlet manual valves open
☑ Pump vent valves open
☑ Pump bypass manual valve **closed**
☑ Pump inlet pressure **≥0.1 bar.g**
☑ Lube oil header pressure **1.7 bar.g**

**Start-up**
1. Jacking oil pump A/B → start
2. Confirm header pressure **150 bar.g**
3. Second pump → **Auto**

⚠️ Normal **150 bar**, alarm at **60 bar**. By the time that alarm comes in, the shaft may already not be lifted. On turning gear that matters.

⚠️ The jacking pump draws from the lube oil system. No **1.7 bar** in the lube header, no jacking oil.

`#jackingoil #JOP #turninggear`

---
---

## POST 7 — Vakuum tizimi

**🇺🇿 Vakuum nasoslari — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Dvigatel podshipnik harorati H | ≥80°C | Alarm |
| Dvigatel podshipnik harorati HH | ≥90°C | **Trip** |
| Dvigatel o'ram harorati H | ≥120°C | Alarm |
| Dvigatel o'ram harorati HH | ≥135°C | **Trip** |
| Separator suv sathi L | ≤130 mm | Alarm |
| Separator suv sathi LL | ≤60 mm | **Trip** |
| Separator suv sathi H | ≥250 mm | Alarm |
| Ishchi suyuqlik harorati H | ≥45°C | Alarm |
| Dvigatel podshipnik tebranishi H | ≥4.5 mm/s | Alarm |
| Nasos podshipnik tebranishi H | ≥4.5 mm/s | Alarm |

**Ishga tushirishdan oldin ventil holati**
| Uskuna | KKS | Holat |
|---|---|---|
| Kondensator vakuum so'rish motorli ventil | 10PUE10AA001 | Ochiq |
| Kondensator vakuum so'rish motorli ventil | 10PUE10AA002 | Ochiq |
| So'rish quvuri vent ventili | 10PUE10AA501 | Yopiq |
| Vakuum so'rish qo'l ventili | 10PUE10AA004 | Ochiq |

⚠️ Separator sathi **60 mm**da nasosni trip qiladi — alarm esa **130 mm**da. Ikkalasi orasida atigi 70 mm. Sath tushayotgan bo'lsa make-up'ni tekshirishga vaqt kam.

⚠️ Ishchi suyuqlik harorati **45°C**dan oshsa vakuum yomonlashadi — LP exhaust bosimi ko'tariladi. Zanjir: ishchi suyuqlik issiq → vakuum past → LP exhaust bosim **0.35 bar.a** alarm → **0.45 bar.a** trip.

---

**🇷🇺 Вакуумные насосы — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Темп. подшипника двигателя H | ≥80°C | Сигнал |
| Темп. подшипника двигателя HH | ≥90°C | **Отключение** |
| Темп. обмотки H | ≥120°C | Сигнал |
| Темп. обмотки HH | ≥135°C | **Отключение** |
| Уровень в сепараторе L | ≤130 мм | Сигнал |
| Уровень в сепараторе LL | ≤60 мм | **Отключение** |
| Уровень в сепараторе H | ≥250 мм | Сигнал |
| Темп. рабочей жидкости H | ≥45°C | Сигнал |
| Вибрация подшипника двигателя H | ≥4.5 мм/с | Сигнал |
| Вибрация подшипника насоса H | ≥4.5 мм/с | Сигнал |

**Положение задвижек перед пуском**
10PUE10AA001 — открыта | 10PUE10AA002 — открыта
10PUE10AA501 (воздушник) — закрыта | 10PUE10AA004 — открыта

⚠️ Между сигналом (**130 мм**) и отключением (**60 мм**) всего 70 мм. При падении уровня времени на подпитку мало.

⚠️ Рабочая жидкость выше **45°C** → вакуум ухудшается → давление выхлопа ЦНД растёт: сигнал **0.35 бар.а**, защита **0.45 бар.а**.

---

**🇬🇧 Vacuum Pumps — settings**

| Item | Setting | Action |
|---|---|---|
| Motor bearing temp H | ≥80°C | Alarm |
| Motor bearing temp HH | ≥90°C | **Trip** |
| Motor winding temp H | ≥120°C | Alarm |
| Motor winding temp HH | ≥135°C | **Trip** |
| Separator level L | ≤130 mm | Alarm |
| Separator level LL | ≤60 mm | **Trip** |
| Separator level H | ≥250 mm | Alarm |
| Working fluid temp H | ≥45°C | Alarm |
| Motor bearing vibration H | ≥4.5 mm/s | Alarm |
| Pump bearing vibration H | ≥4.5 mm/s | Alarm |

**Valve line-up before start**
10PUE10AA001 open | 10PUE10AA002 open | 10PUE10AA501 (vent) closed | 10PUE10AA004 open

⚠️ Only 70 mm between separator alarm (**130 mm**) and trip (**60 mm**).

⚠️ Working fluid above **45°C** degrades vacuum → LP exhaust pressure rises: alarm **0.35 bar.a**, trip **0.45 bar.a**.

`#vacuum #condenser #LPexhaust`

---
---

## POST 8 — Gland steam tizimi

**🇺🇿 Gland steam — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Kollektor harorati L | <150°C | Alarm |
| Kollektor harorati H | >400°C | Alarm |
| Kollektor bosimi L | <10 kPa | Alarm |
| Kollektor bosimi H | >42 kPa | Alarm |
| GSC kirish bosimi L | <−15 kPa | Alarm |
| LP silindr packing harorati L | <150°C | Alarm |
| LP silindr packing harorati H | >180°C | Alarm |
| GSC chiqish harorati H | >75°C | Alarm |
| GSC sath H | >245 mm | Alarm |

⚠️ **LP packing uchun oyna juda tor: 150–180°C, atigi 30°C.** HP/IP kollektor esa 150–400°C. Ya'ni bitta kollektordan ikki xil talab — LP tomonga desuperheater orqali kondensat beriladi.

⚠️ Kollektor bosimi **10 kPa**dan past → havo so'riladi → vakuum yomonlashadi.
Kollektor bosimi **42 kPa**dan yuqori → bug' podshipnik tomonga o'tadi → **yog'ga suv tushadi**.

Nominal steam seal header: **1.29 bar.a** (Table 1-1-1).

---

**🇷🇺 Уплотняющий пар — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Темп. коллектора L | <150°C | Сигнал |
| Темп. коллектора H | >400°C | Сигнал |
| Давление коллектора L | <10 кПа | Сигнал |
| Давление коллектора H | >42 кПа | Сигнал |
| Давление на входе СП L | <−15 кПа | Сигнал |
| Темп. уплотнений ЦНД L | <150°C | Сигнал |
| Темп. уплотнений ЦНД H | >180°C | Сигнал |
| Темп. на выходе СП H | >75°C | Сигнал |
| Уровень в СП H | >245 мм | Сигнал |

⚠️ **Для уплотнений ЦНД окно всего 30°C: 150–180°C.** Для коллектора — 150–400°C. Поэтому на ЦНД идёт пароохладитель с конденсатом.

⚠️ Ниже **10 кПа** — подсос воздуха, падение вакуума.
Выше **42 кПа** — пар идёт в сторону подшипников, **обводнение масла**.

Номинал коллектора уплотнений: **1.29 бар.а**.

---

**🇬🇧 Gland Steam — settings**

| Item | Setting | Action |
|---|---|---|
| Header temp L | <150°C | Alarm |
| Header temp H | >400°C | Alarm |
| Header pressure L | <10 kPa | Alarm |
| Header pressure H | >42 kPa | Alarm |
| GSC inlet pressure L | <−15 kPa | Alarm |
| LP packing temp L | <150°C | Alarm |
| LP packing temp H | >180°C | Alarm |
| GSC outlet temp H | >75°C | Alarm |
| GSC level H | >245 mm | Alarm |

⚠️ **LP packing window is only 30°C wide: 150–180°C.** Header allows 150–400°C — hence the condensate desuperheater on the LP side.

⚠️ Below **10 kPa** — air in-leakage, vacuum degrades.
Above **42 kPa** — steam tracks toward the bearings, **oil gets wet**.

Nominal steam seal header: **1.29 bar.a**.

`#glandsteam #GSC #sealing`

---
---

## POST 9 — Yordamchi bug' tizimi

**🇺🇿 Auxiliary steam — setpointlar va ventil holati**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Yordamchi bug' bosimi H | >12.5 bar | Alarm |
| Yordamchi bug' harorati H | >360°C | Alarm |

**Kollektorga bug' berishdan oldin ventil holati**
| Uskuna | KKS | Holat |
|---|---|---|
| Kimyoviy suv sexiga ajratish motorli ventil | 10LBG13AA001 | Yopiq |
| Gland steam kollektoriga ajratish motorli ventil | 10LBG12AA001 | Yopiq |
| ST preheat bypass ajratish ventili | 10LBG11AA003 | Yopiq |
| ST preheat ajratish ventili | 10LBG11AA001 | **Ochiq** |
| ST preheat ajratish ventili | 10LBG11AA002 | **Ochiq** |
| ST preheat pnevmatik ventil | 10LBG11AA101 | Yopiq |
| Sovuq qayta qizdirishdan kollektorga motorli ventil | 10LBG01AA001 | Yopiq |
| Sovuq qayta qizdirishdan kollektorga ventil | 10LBG01AA002 | **Ochiq** |
| Yordamchi qozondan ajratish motorli ventil | 10LBG10AA001 | Yopiq |
| Kollektor drenaji | 00LBG10AA401 | **Ochiq** |
| Kollektor drenaji | 00LBG10AA403 | **Ochiq** |
| Qolgan barcha vent va drenajlar | — | Yopiq |

Bug' manbalari: **yordamchi ishga tushirish qozoni** yoki **sovuq qayta qizdirish liniyasi**.

⚠️ Drenajlar 401 va 403 **ochiq qoladi** — bu bug' berishda kondensatni chiqarish uchun. Qolganlari yopiq. Bu ro'yxatni yoddan bilmasangiz gland steam'ga suv tushadi.

---

**🇷🇺 Вспомогательный пар — уставки и положение задвижек**

| Параметр | Уставка | Действие |
|---|---|---|
| Давление вспом. пара H | >12.5 бар | Сигнал |
| Темп. вспом. пара H | >360°C | Сигнал |

**Положение задвижек перед подачей пара в коллектор**
10LBG13AA001 закрыта | 10LBG12AA001 закрыта | 10LBG11AA003 закрыта
10LBG11AA001 **открыта** | 10LBG11AA002 **открыта** | 10LBG11AA101 закрыта
10LBG01AA001 закрыта | 10LBG01AA002 **открыта** | 10LBG10AA001 закрыта
Дренажи 00LBG10AA401 и 00LBG10AA403 **открыты**, остальные вентиляции и дренажи закрыты

Источники пара: **пусковая вспомогательная котельная** или **линия холодного промперегрева**.

⚠️ Дренажи 401 и 403 остаются **открытыми** для отвода конденсата при подаче пара. Без этого вода попадёт в уплотняющий пар.

---

**🇬🇧 Auxiliary Steam — settings and valve line-up**

| Item | Setting | Action |
|---|---|---|
| Aux steam pressure H | >12.5 bar | Alarm |
| Aux steam temp H | >360°C | Alarm |

**Valve line-up before admitting steam to the header**
10LBG13AA001 closed | 10LBG12AA001 closed | 10LBG11AA003 closed
10LBG11AA001 **open** | 10LBG11AA002 **open** | 10LBG11AA101 closed
10LBG01AA001 closed | 10LBG01AA002 **open** | 10LBG10AA001 closed
Drains 00LBG10AA401 and 00LBG10AA403 **open**, all other vents and drains closed

Steam sources: **auxiliary start-up boiler** or **cold reheat line**.

⚠️ Drains 401 and 403 stay **open** to clear condensate during admission. Miss this and water reaches the gland steam header.

`#auxsteam #LBG #valvelineup`

---
---

## POST 10 — CCCWS (yopiq sikl sovutish suvi)

**🇺🇿 CCCWS — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Kengaytirish baki sath H | ≥1700 mm | Make-up pnevmatik ventil avto-yopiladi |
| Kengaytirish baki sath L | ≤500 mm | Alarm |
| Kengaytirish baki sath LL | ≤300 mm | **Nasosni trip** |
| Nasos podshipnik harorati H | ≥70°C | Alarm |
| Nasos podshipnik harorati HH | ≥75°C | **Nasosni trip** |
| Dvigatel podshipnik harorati H | ≥90°C | Alarm |
| Dvigatel podshipnik harorati HH | ≥95°C | **Dvigatelni trip** |
| Dvigatel o'ram harorati H | ≥130°C | Alarm |
| Dvigatel o'ram harorati HH | ≥140°C | **Dvigatelni trip** |
| Dvigatel podshipnik tebranishi H | ≥4.5 mm/s | Alarm |
| Dvigatel podshipnik tebranishi HH | ≥7.1 mm/s | **Trip** |
| Nasos podshipnik tebranishi H | ≥4.5 mm/s | Alarm |
| Nasos podshipnik tebranishi HH | ≥7.1 mm/s | **Trip** |
| Nasos chiqish bosimi H | ≥8.8 bar | Alarm + min-flow klapan avto-ochiladi |
| Nasos chiqish bosimi L | ≤6 bar | **Zaxira nasos avto-ishga tushadi** |
| Nasos chiqish harorati past | ≤25°C | HX bypass klapan avto-ochiladi |
| Nasos kirish filtri Δp | ≥5 kPa | Alarm |

**Uskuna**
Nasos 00PGA11/12AP001 — GSX800-19-6-HN01, 980 rpm, napor 55 m, **7200 m³/s**, 2×100%
Dvigatel YXKK560-6 — **1400 kW**, 995 r/min, **89.3 A**, η 95.7%, cos φ 0.86
Issiqlik almashgich 00PGDA21/22/23/24AC001 — plastinali, 4×50%
• Issiqlik **41 755.8 kW** | ish bosimi 16 bar.g | sinov 24 bar
• CCCW tomoni **47.3 → 37.0°C**, 3600 t/s | ACCW tomoni **33.1 → 42.6°C**, 3800 t/s
Kengaytirish baki — **10 m³**
Kirish filtri — ish bosimi 0.3 MPa, nominal Δp 0.005 MPa, ish harorati 60°C, filtrlash **4 mm**

**Ishga tushirishdan oldin suv to'ldirish**
Kengaytirish baki sathi **1000–1500 mm** oralig'ida bo'lishi shart (DM suv tizimi ishlab, sathni avto ushlab turadi). Quvurlar va nasos korpusi to'liq suv bilan to'ldirilgan, barcha yuqori nuqtalardan havo chiqarilgan.

⚠️ Sath ketma-ketligi: **1700 → 500 → 300**. Alarm va trip orasida atigi 200 mm. Make-up klapan **300 mm**da ochiladi, **1700 mm**da yopiladi — ya'ni make-up klapanning ochilish nuqtasi trip nuqtasi bilan bir xil. Sath 500'da alarm chiqsa — make-up'ni qo'lda ochish kerak bo'lishi mumkin.

---

**🇷🇺 ЗКОС (замкнутый контур охлаждающей воды) — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Уровень расширительного бака H | ≥1700 мм | Автозакрытие клапана подпитки |
| Уровень L | ≤500 мм | Сигнал |
| Уровень LL | ≤300 мм | **Отключение насоса** |
| Темп. подшипника насоса H | ≥70°C | Сигнал |
| Темп. подшипника насоса HH | ≥75°C | **Отключение** |
| Темп. подшипника двигателя H | ≥90°C | Сигнал |
| Темп. подшипника двигателя HH | ≥95°C | **Отключение** |
| Темп. обмотки H | ≥130°C | Сигнал |
| Темп. обмотки HH | ≥140°C | **Отключение** |
| Вибрация подшипника двигателя H/HH | ≥4.5 / ≥7.1 мм/с | Сигнал / **Отключение** |
| Вибрация подшипника насоса H/HH | ≥4.5 / ≥7.1 мм/с | Сигнал / **Отключение** |
| Давление на нагнетании H | ≥8.8 бар | Сигнал + автооткрытие клапана мин. расхода |
| Давление на нагнетании L | ≤6 бар | **Автопуск резервного насоса** |
| Темп. на нагнетании низкая | ≤25°C | Автооткрытие байпаса теплообменника |
| Δp фильтра на всасе | ≥5 кПа | Сигнал |

**Оборудование**
Насос 00PGA11/12AP001 — GSX800-19-6-HN01, 980 об/мин, напор 55 м, **7200 м³/ч**, 2×100%
Двигатель YXKK560-6 — **1400 кВт**, 995 об/мин, **89.3 А**, КПД 95.7%, cos φ 0.86
Теплообменник 00PGDA21/22/23/24AC001 — пластинчатый, 4×50%
• Тепло **41 755.8 кВт** | рабочее 16 бар.g | испытательное 24 бар
• Сторона ЗКОС **47.3 → 37.0°C**, 3600 т/ч | сторона ВЦОС **33.1 → 42.6°C**, 3800 т/ч
Расширительный бак — **10 м³**
Фильтр на всасе — 0.3 МПа, ном. Δp 0.005 МПа, 60°C, тонкость **4 мм**

**Заполнение перед пуском**
Уровень расширительного бака **1000–1500 мм**, ХВО в работе на автоподдержании. Трубопроводы и корпус насоса заполнены, воздух стравлен из всех верхних точек.

⚠️ Между сигналом (500 мм) и отключением (300 мм) — 200 мм. Клапан подпитки открывается на **300 мм**, то есть на уставке отключения. При сигнале на 500 мм может потребоваться ручная подпитка.

---

**🇬🇧 CCCWS — settings**

| Item | Setting | Action |
|---|---|---|
| Expansion tank level H | ≥1700 mm | Auto-close make-up valve |
| Level L | ≤500 mm | Alarm |
| Level LL | ≤300 mm | **Trip pump** |
| Pump bearing temp H/HH | ≥70 / ≥75°C | Alarm / **Trip** |
| Motor bearing temp H/HH | ≥90 / ≥95°C | Alarm / **Trip** |
| Motor winding temp H/HH | ≥130 / ≥140°C | Alarm / **Trip** |
| Motor bearing vibration H/HH | ≥4.5 / ≥7.1 mm/s | Alarm / **Trip** |
| Pump bearing vibration H/HH | ≥4.5 / ≥7.1 mm/s | Alarm / **Trip** |
| Pump outlet pressure H | ≥8.8 bar | Alarm + auto-open min flow valve |
| Pump outlet pressure L | ≤6 bar | **Auto-start standby pump** |
| Pump outlet temp low | ≤25°C | Auto-open HX bypass valve |
| Pump inlet filter Δp | ≥5 kPa | Alarm |

**Equipment**
Pump 00PGA11/12AP001 — GSX800-19-6-HN01, 980 rpm, 55 m head, **7200 m³/h**, 2×100%
Motor YXKK560-6 — **1400 kW**, 995 r/min, **89.3 A**, η 95.7%, cos φ 0.86
Heat exchanger 00PGDA21/22/23/24AC001 — plate type, 4×50%
• Duty **41,755.8 kW** | operating 16 bar.g | test 24 bar
• CCCW side **47.3 → 37.0°C**, 3600 t/h | ACCW side **33.1 → 42.6°C**, 3800 t/h
Expansion tank — **10 m³**
Inlet filter — 0.3 MPa working, rated Δp 0.005 MPa, 60°C, **4 mm** filtration

**Water filling before start**
Expansion tank level **1000–1500 mm**, DM plant in service on auto level control. Piping and pump casing fully filled, air vented from all high points.

⚠️ Only 200 mm between alarm (500 mm) and trip (300 mm). Make-up valve opens at **300 mm** — the same point as the trip. If the 500 mm alarm comes in, be ready to make up manually.

`#CCCWS #coolingwater #PGA`

---
---

## POST 11 — ACCWS (yordamchi aylanma sovutish suvi)

**🇺🇿 ACCWS — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| So'rish havzasi sathi L | ≤−1700 mm | Alarm |
| So'rish havzasi sathi LL | ≤−3200 mm | **Nasosni trip** |
| Dvigatel upor podshipnik harorati H | ≥85°C | Alarm |
| Dvigatel upor podshipnik harorati HH | ≥95°C | **Nasosni trip** |
| Dvigatel pastki podshipnik harorati H | ≥85°C | Alarm |
| Dvigatel pastki podshipnik harorati HH | ≥95°C | **Nasosni trip** |
| Dvigatel o'ram harorati H | ≥110°C | Alarm |
| Dvigatel o'ram harorati HH | ≥115°C | **Nasosni trip** |
| Dvigatel tebranishi H | ≥90 μm | Alarm |
| Dvigatel podshipnik sovutish suvi harorati H | ≥60°C | Alarm |
| Dvigatel podshipnik sovutish suvi sarfi L | ≤5.6 m³/s | Alarm |
| Gradirnya suv sathi H | ≥−0.3 m | Alarm + make-up ventil avto-yopiladi |
| Gradirnya suv sathi L | ≤−1.1 m | Alarm + make-up ventil avto-ochiladi |
| Avtomatik filtr Δp H | ≥60 kPa | Alarm + filtr avto-ishga tushadi |
| Aylanma suv o'tkazuvchanligi | ≥3000 μS/sm | — |

⚠️ **O'ram harorati H va HH orasi atigi 5°C** (110 → 115°C). Boshqa tizimlarda 10°C. Ya'ni ACCWS dvigatelida o'ram alarm chiqsa — trip juda yaqin, kutib turish mumkin emas.

⚠️ O'tkazuvchanlik **3000 μS/sm** — bu korroziya va cho'kma chegarasi. Kimyoviy rejim buzilganini birinchi ko'rsatadi.

---

**🇷🇺 ВЦОС (вспомогательная циркуляционная охлаждающая вода) — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Уровень приёмного колодца L | ≤−1700 мм | Сигнал |
| Уровень приёмного колодца LL | ≤−3200 мм | **Отключение насоса** |
| Темп. упорного подшипника двигателя H/HH | ≥85 / ≥95°C | Сигнал / **Отключение** |
| Темп. нижнего подшипника двигателя H/HH | ≥85 / ≥95°C | Сигнал / **Отключение** |
| Темп. обмотки H/HH | ≥110 / ≥115°C | Сигнал / **Отключение** |
| Вибрация двигателя H | ≥90 мкм | Сигнал |
| Темп. охл. воды подшипников H | ≥60°C | Сигнал |
| Расход охл. воды подшипников L | ≤5.6 м³/ч | Сигнал |
| Уровень градирни H | ≥−0.3 м | Сигнал + автозакрытие подпитки |
| Уровень градирни L | ≤−1.1 м | Сигнал + автооткрытие подпитки |
| Δp автофильтра H | ≥60 кПа | Сигнал + автопуск промывки |
| Электропроводность циркводы | ≥3000 мкСм/см | — |

⚠️ **Между сигналом и отключением по обмотке всего 5°C** (110 → 115°C). В других системах 10°C. Ждать нельзя.

⚠️ **3000 мкСм/см** — предел по коррозии и отложениям, первый признак нарушения ВХР.

---

**🇬🇧 ACCWS — settings**

| Item | Setting | Action |
|---|---|---|
| Suction pool level L | ≤−1700 mm | Alarm |
| Suction pool level LL | ≤−3200 mm | **Trip pump** |
| Motor thrust bearing temp H/HH | ≥85 / ≥95°C | Alarm / **Trip** |
| Motor lower bearing temp H/HH | ≥85 / ≥95°C | Alarm / **Trip** |
| Motor winding temp H/HH | ≥110 / ≥115°C | Alarm / **Trip** |
| Motor vibration H | ≥90 μm | Alarm |
| Motor bearing cooling water temp H | ≥60°C | Alarm |
| Motor bearing cooling water flow L | ≤5.6 m³/h | Alarm |
| Cooling tower level H | ≥−0.3 m | Alarm + auto-close make-up |
| Cooling tower level L | ≤−1.1 m | Alarm + auto-open make-up |
| Auto filter Δp H | ≥60 kPa | Alarm + auto-start backwash |
| Circulating water conductivity | ≥3000 μS/cm | — |

⚠️ **Only 5°C between winding alarm and trip** (110 → 115°C). Other systems give 10°C. No time to wait it out.

⚠️ **3000 μS/cm** is the corrosion/scaling limit — first indication chemistry has slipped.

`#ACCWS #coolingtower #auxcooling`

---
---

## POST 12 — CCWS (aylanma sovutish suvi)

**🇺🇿 CCWS — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| So'rish havzasi sathi L | ≤−1700 mm | Alarm |
| So'rish havzasi sathi LL | ≤−4380 mm | **Nasosni trip** |
| So'rish havzasi sathi H | ≥−900 mm | Alarm |
| Dvigatel upor podshipnik harorati H | ≥95°C | Alarm |
| Dvigatel upor podshipnik harorati HH | ≥105°C | **Nasosni trip** |
| Dvigatel pastki podshipnik harorati H | ≥95°C | Alarm |
| Dvigatel pastki podshipnik harorati HH | ≥105°C | **Nasosni trip** |
| Dvigatel o'ram harorati H | ≥130°C | Alarm |
| Dvigatel o'ram harorati HH | ≥135°C | **Nasosni trip** |
| Dvigatel tebranishi H | ≥90 μm | Alarm |
| Dvigatel podshipnik sovutish suvi harorati H | ≥60°C | Alarm |
| Dvigatel podshipnik sovutish suvi sarfi L | ≤50 m³/s | Alarm |
| Gradirnya suv sathi H | ≥−0.3 m | Alarm + make-up avto-yopiladi |
| Gradirnya suv sathi L | ≤−1.1 m | Alarm + make-up avto-ochiladi |
| Gradirnya ventilyator reduktor yog' harorati H | ≥88°C | Alarm |
| Gradirnya ventilyator reduktor yog' harorati HH | ≥92°C | **Ventilyatorni trip** |
| Gradirnya ventilyator reduktor yog' sathi L | <0.2 m | Alarm |
| Gradirnya ventilyator podshipnik harorati H | ≥90°C | Alarm |
| Gradirnya ventilyator podshipnik harorati HH | ≥95°C | **Ventilyatorni trip** |
| Gradirnya ventilyator o'ram harorati H | ≥150°C | Alarm |

Nasoslar: **2×50%** vertikal o'q oqimli.

⚠️ **Reduktor yog' harorati alarm 88°C, trip 92°C — atigi 4°C.** Bu butun ro'yxatdagi eng tor oyna. Yozda gradirnya ventilyatorlari shu sababdan tushib qoladi.

⚠️ ACCWS bilan CCWS ni chalkashtirmang: ikkalasida ham havza sathi L **−1700 mm**, lekin trip: ACCWS **−3200**, CCWS **−4380**.

---

**🇷🇺 ЦОС (циркуляционная охлаждающая вода) — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Уровень колодца L / LL / H | ≤−1700 / ≤−4380 / ≥−900 мм | Сигнал / **Отключение** / Сигнал |
| Темп. упорного подшипника двигателя H/HH | ≥95 / ≥105°C | Сигнал / **Отключение** |
| Темп. нижнего подшипника H/HH | ≥95 / ≥105°C | Сигнал / **Отключение** |
| Темп. обмотки H/HH | ≥130 / ≥135°C | Сигнал / **Отключение** |
| Вибрация двигателя H | ≥90 мкм | Сигнал |
| Темп. охл. воды подшипников H | ≥60°C | Сигнал |
| Расход охл. воды подшипников L | ≤50 м³/ч | Сигнал |
| Уровень градирни H / L | ≥−0.3 / ≤−1.1 м | Автозакрытие / автооткрытие подпитки |
| Темп. масла редуктора вентилятора H/HH | ≥88 / ≥92°C | Сигнал / **Отключение вентилятора** |
| Уровень масла редуктора L | <0.2 м | Сигнал |
| Темп. подшипника вентилятора H/HH | ≥90 / ≥95°C | Сигнал / **Отключение** |
| Темп. обмотки вентилятора H | ≥150°C | Сигнал |

Насосы: **2×50%** вертикальные осевые.

⚠️ **Масло редуктора: сигнал 88°C, отключение 92°C — всего 4°C.** Самое узкое окно во всём списке. Летом вентиляторы градирни садятся именно по этому.

⚠️ Не путайте ВЦОС и ЦОС: уровень L у обоих **−1700 мм**, но отключение — ВЦОС **−3200**, ЦОС **−4380**.

---

**🇬🇧 CCWS — settings**

| Item | Setting | Action |
|---|---|---|
| Suction pool level L / LL / H | ≤−1700 / ≤−4380 / ≥−900 mm | Alarm / **Trip** / Alarm |
| Motor thrust bearing temp H/HH | ≥95 / ≥105°C | Alarm / **Trip** |
| Motor lower bearing temp H/HH | ≥95 / ≥105°C | Alarm / **Trip** |
| Motor winding temp H/HH | ≥130 / ≥135°C | Alarm / **Trip** |
| Motor vibration H | ≥90 μm | Alarm |
| Motor bearing cooling water temp H | ≥60°C | Alarm |
| Motor bearing cooling water flow L | ≤50 m³/h | Alarm |
| Cooling tower level H / L | ≥−0.3 / ≤−1.1 m | Auto-close / auto-open make-up |
| Fan gearbox oil temp H/HH | ≥88 / ≥92°C | Alarm / **Trip fan** |
| Fan gearbox oil level L | <0.2 m | Alarm |
| Fan bearing temp H/HH | ≥90 / ≥95°C | Alarm / **Trip fan** |
| Fan winding temp H | ≥150°C | Alarm |

Pumps: **2×50%** vertical axial flow.

⚠️ **Gearbox oil: alarm 88°C, trip 92°C — 4°C of margin.** Narrowest window in the whole list. This is what drops cooling tower fans in summer.

⚠️ Don't mix up ACCWS and CCWS: level L is **−1700 mm** on both, but trip is **−3200** (ACCWS) vs **−4380** (CCWS).

`#CCWS #coolingtower #circwater`

---
---

## POST 13 — Kondensat tizimi

**🇺🇿 Kondensat tizimi — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Kondensator sathi HH | ≥2390 mm | Alarm + bypass interlok bilan yopiladi |
| Kondensator sathi H | ≥2240 mm | Alarm |
| Kondensator sathi L | ≤1490 mm | Alarm |
| Kondensator sathi LL | ≤1340 mm | **Nasosni trip** |
| Upor podshipnik harorati H | ≥90°C | Alarm |
| Upor podshipnik harorati HH | ≥95°C | **Nasosni trip** |
| Dvigatel podshipnik harorati H | ≥90°C | Alarm |
| Dvigatel podshipnik harorati HH | ≥95°C | **Dvigatelni trip** |
| O'ram harorati H | ≥125°C | Alarm |
| O'ram harorati HH | ≥130°C | **Dvigatelni trip** |
| Dvigatel pastki podshipnik tebranishi (rigid) | ≥4.5 / ≥7.1 mm/s | Alarm / **Trip** |
| Dvigatel yuqori podshipnik tebranishi (flexible) | ≥7.1 / ≥11.0 mm/s | Alarm / **Trip** |
| Nasos kirish filtri Δp | ≥10 kPa | Alarm |
| Nasos chiqish bosimi L | ≤1.5 MPa | **Zaxira nasos avto-ishga tushadi** |

**Ishga tushirishdan oldin**
• DM tizimi normal ishlayapti
• Kondensator normal sathgacha to'ldirilgan (**tag plitadan <−350 mm**)
• Nasos kirish motorli ventillari 10LCA11AA001 / 10LCA12AA001 **ochiq**
• Filtr havo chiqarish ventillari 10LCA11AA501 / 10LCA12AA501 orqali havo chiqarilgan
• Mexanik zichlash suvi ventillari ochiq: 10LCW10AA001, 10LCW11AA001/2, 10LCW12AA001/2
• Zichlash suvi bosimi **0.5–0.7 MPa** (10LCR10CP501 / 10LCR10CP502)

⚠️ **Tebranish chegarasi podshipnikka qarab farq qiladi:** pastki (rigid) 4.5/7.1 mm/s, yuqori (flexible) 7.1/11.0 mm/s. Bitta nasosda ikki xil me'yor — buni chalkashtirish keng tarqalgan xato.

---

**🇷🇺 Конденсатная система — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Уровень в конденсаторе HH | ≥2390 мм | Сигнал + закрытие БРОУ по блокировке |
| Уровень H / L | ≥2240 / ≤1490 мм | Сигнал |
| Уровень LL | ≤1340 мм | **Отключение насоса** |
| Темп. упорного подшипника H/HH | ≥90 / ≥95°C | Сигнал / **Отключение** |
| Темп. подшипника двигателя H/HH | ≥90 / ≥95°C | Сигнал / **Отключение** |
| Темп. обмотки H/HH | ≥125 / ≥130°C | Сигнал / **Отключение** |
| Вибрация нижнего подшипника (жёсткая) | ≥4.5 / ≥7.1 мм/с | Сигнал / **Отключение** |
| Вибрация верхнего подшипника (гибкая) | ≥7.1 / ≥11.0 мм/с | Сигнал / **Отключение** |
| Δp фильтра на всасе | ≥10 кПа | Сигнал |
| Давление на нагнетании L | ≤1.5 МПа | **Автопуск резервного насоса** |

**Перед пуском**
• ХВО в нормальной работе
• Конденсатор заполнен до нормального уровня (**<−350 мм от нижней плиты**)
• Задвижки на всасе 10LCA11AA001 / 10LCA12AA001 **открыты**
• Воздух стравлен через 10LCA11AA501 / 10LCA12AA501
• Задвижки уплотняющей воды открыты: 10LCW10AA001, 10LCW11AA001/2, 10LCW12AA001/2
• Давление уплотняющей воды **0.5–0.7 МПа** (10LCR10CP501 / 502)

⚠️ **Нормы вибрации разные для разных подшипников одного насоса:** нижний 4.5/7.1 мм/с, верхний 7.1/11.0 мм/с. Путают часто.

---

**🇬🇧 Condensate System — settings**

| Item | Setting | Action |
|---|---|---|
| Condenser level HH | ≥2390 mm | Alarm + interlock close bypass |
| Level H / L | ≥2240 / ≤1490 mm | Alarm |
| Level LL | ≤1340 mm | **Trip pump** |
| Thrust bearing temp H/HH | ≥90 / ≥95°C | Alarm / **Trip** |
| Motor bearing temp H/HH | ≥90 / ≥95°C | Alarm / **Trip** |
| Winding temp H/HH | ≥125 / ≥130°C | Alarm / **Trip** |
| Motor lower bearing vibration (rigid) | ≥4.5 / ≥7.1 mm/s | Alarm / **Trip** |
| Motor upper bearing vibration (flexible) | ≥7.1 / ≥11.0 mm/s | Alarm / **Trip** |
| Pump inlet filter Δp | ≥10 kPa | Alarm |
| Pump outlet pressure L | ≤1.5 MPa | **Auto-start standby pump** |

**Before start-up**
• DM plant in normal operation
• Condenser filled to normal level (**<−350 mm from bottom plate**)
• Pump inlet motor valves 10LCA11AA001 / 10LCA12AA001 **open**
• Air vented via 10LCA11AA501 / 10LCA12AA501
• Mechanical seal water valves open: 10LCW10AA001, 10LCW11AA001/2, 10LCW12AA001/2
• Seal water pressure **0.5–0.7 MPa** (10LCR10CP501 / 502)

⚠️ **Vibration limits differ between bearings on the same pump:** lower (rigid) 4.5/7.1 mm/s, upper (flexible) 7.1/11.0 mm/s. Commonly confused.

`#condensate #CEP #condenser`

---
---

## POST 14 — Generator seal oil

**🇺🇿 Seal oil — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Suyuqlik detektori sathi H | >428 mm | Alarm |
| Seal oil filtri Δp | >0.5 bar | Alarm |
| Strainer M-ST-02A Δp (TE tomoni) | >0.5 bar | Alarm |
| Strainer M-ST-02B Δp (CE tomoni) | >0.5 bar | Alarm |
| Vakuum bak sathi H | +100 mm ko'tarilish | Alarm |
| Vakuum bak sathi L | −100 mm pasayish | Alarm |
| Seal oil differensial bosimi L | <0.41 bar | Alarm |
| MSOP chiqish bosimi L | <8.5 bar | **MSOP interlok bilan ishga tushadi** |
| Seal oil umumiy bosim s/w #1 (ESOP uchun) | <7 bar | **ESOP interlok bilan ishga tushadi** |

**Ventil holati (barchasi ochiq)**
MSOP-A kirish 10MKW03AA001, chiqish 10MKW03AA002
MSOP-B kirish 10MKW03AA003, chiqish 10MKW03AA005
Xavfsizlik klapani → vakuum bakka 10MKW03AA004
Manometr ajratish 10MKW03AA301
Retsirkulyatsiya nasosi kirish 10MKW04AA015, chiqish 10MKW04AA005 va 10MKW04AA004
Seal oil kollektori 10MKW05AA002

⚠️ **Ikki bosqichli zaxira: 8.5 bar → MSOP, 7 bar → ESOP.** Orasida 1.5 bar. Differensial bosim alarm **0.41 bar** — bu H2 bosimidan seal oil bosimi qanchaga yuqori turishini ko'rsatadi. 0.41 bar'dan tushsa vodorod podshipnik tomonga o'ta boshlaydi.

⚠️ Generator korpusi suyuqlik detektori: **H >1.8 L, HH >2.0 L**. Bu seal oil generator ichiga kirayotganini ko'rsatadi.

---

**🇷🇺 Уплотняющее масло генератора — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Уровень детектора жидкости H | >428 мм | Сигнал |
| Δp фильтра уплотняющего масла | >0.5 бар | Сигнал |
| Δp сетчатого фильтра M-ST-02A (сторона ТГ) | >0.5 бар | Сигнал |
| Δp сетчатого фильтра M-ST-02B (сторона возбудителя) | >0.5 бар | Сигнал |
| Уровень вакуумного бака H / L | ±100 мм | Сигнал |
| Перепад давления уплотняющего масла L | <0.41 бар | Сигнал |
| Давление на нагнетании ОНУМ L | <8.5 бар | **Пуск ОНУМ по блокировке** |
| Общее давление, реле #1 для АНУМ | <7 бар | **Пуск АНУМ по блокировке** |

**Положение задвижек (все открыты)**
ОНУМ-A: 10MKW03AA001 / 10MKW03AA002
ОНУМ-B: 10MKW03AA003 / 10MKW03AA005
Предохранительный клапан → вакуумный бак: 10MKW03AA004
Отсечная манометра: 10MKW03AA301
Рециркуляционный насос: 10MKW04AA015 / 10MKW04AA005 / 10MKW04AA004
Коллектор уплотняющего масла: 10MKW05AA002

⚠️ **Две ступени резерва: 8.5 бар → ОНУМ, 7 бар → АНУМ.** Между ними 1.5 бар. Перепад **0.41 бар** — превышение давления масла над давлением водорода. Ниже — водород пойдёт в сторону подшипников.

⚠️ Детектор жидкости в корпусе генератора: **H >1.8 л, HH >2.0 л** — признак попадания уплотняющего масла внутрь.

---

**🇬🇧 Generator Seal Oil — settings**

| Item | Setting | Action |
|---|---|---|
| Liquid detector level H | >428 mm | Alarm |
| Seal oil filter Δp | >0.5 bar | Alarm |
| Strainer M-ST-02A Δp (TE side) | >0.5 bar | Alarm |
| Strainer M-ST-02B Δp (CE side) | >0.5 bar | Alarm |
| Vacuum tank level H / L | ±100 mm | Alarm |
| Seal oil differential pressure L | <0.41 bar | Alarm |
| MSOP discharge pressure L | <8.5 bar | **Interlock start MSOP** |
| Seal oil common pressure s/w #1 (ESOP) | <7 bar | **Interlock start ESOP** |

**Valve line-up (all open)**
MSOP-A: 10MKW03AA001 / 10MKW03AA002 | MSOP-B: 10MKW03AA003 / 10MKW03AA005
Relief to vacuum tank: 10MKW03AA004 | Gauge isolation: 10MKW03AA301
Recirculation pump: 10MKW04AA015 / 10MKW04AA005 / 10MKW04AA004
Seal oil header: 10MKW05AA002

⚠️ **Two-stage backup: 8.5 bar → MSOP, 7 bar → ESOP** — 1.5 bar apart. The **0.41 bar** differential is seal oil pressure over H2 pressure. Below that, hydrogen starts tracking toward the bearings.

⚠️ Generator casing liquid detector: **H >1.8 L, HH >2.0 L** — seal oil getting into the machine.

`#sealoil #MSOP #ESOP #generator`

---
---

## POST 15 — Generator H2 va CO2 tizimi

**🇺🇿 H2 / CO2 — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| H2 tozaligi L | <95% | Alarm |
| H2 tozaligi LL | <90% | Alarm |
| H2 bosimi L | <5.03 bar | Alarm |
| H2 bosimi H | >5.45 bar | Alarm |
| Quritgich kirishida shudring nuqtasi H | >−6.67°C | Alarm |
| Quritgich chiqishida shudring nuqtasi H | >−28.29°C | Alarm |
| Generator korpusi suyuqlik detektori H | >1.8 L | Alarm |
| Generator korpusi suyuqlik detektori HH | >2.0 L | Alarm |

**Gaz almashtirish ketma-ketligi**
Havo → **CO2** → H2 (to'ldirishda)
H2 → **CO2** → havo (bo'shatishda)

CO2 hech qachon o'tkazib yuborilmaydi — havo va H2 hech qachon bevosita almashtirilmaydi.

⚠️ **H2 bosimi oynasi juda tor: 5.03–5.45 bar, atigi 0.42 bar.** Seal oil differensiali esa 0.41 bar. Ya'ni H2 bosimi va seal oil bosimi bir-biriga juda bog'liq — biri o'zgarsa ikkinchisi darhol ta'sirlanadi.

⚠️ Tozalik **95%** alarm, **90%** LL. Tozalik tushishi — yoki havo kiryapti, yoki seal oil'dan namlik. Shudring nuqtasi bilan birga qarang: quritgich chiqishida **−28.29°C**dan yuqori bo'lsa namlik bor.

---

**🇷🇺 Водород / CO2 генератора — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Чистота H2 L | <95% | Сигнал |
| Чистота H2 LL | <90% | Сигнал |
| Давление H2 L | <5.03 бар | Сигнал |
| Давление H2 H | >5.45 бар | Сигнал |
| Точка росы на входе осушителя H | >−6.67°C | Сигнал |
| Точка росы на выходе осушителя H | >−28.29°C | Сигнал |
| Детектор жидкости в корпусе H | >1.8 л | Сигнал |
| Детектор жидкости в корпусе HH | >2.0 л | Сигнал |

**Последовательность вытеснения**
Воздух → **CO2** → H2 (при заполнении)
H2 → **CO2** → воздух (при опорожнении)

CO2 не пропускается никогда — воздух и водород напрямую не вытесняются.

⚠️ **Окно по давлению H2 всего 0.42 бар: 5.03–5.45.** Перепад уплотняющего масла — 0.41 бар. Давление водорода и уплотняющего масла жёстко связаны.

⚠️ Падение чистоты — либо подсос воздуха, либо влага из уплотняющего масла. Смотрите вместе с точкой росы: выше **−28.29°C** на выходе осушителя — влага есть.

---

**🇬🇧 Generator H2 / CO2 — settings**

| Item | Setting | Action |
|---|---|---|
| H2 purity L | <95% | Alarm |
| H2 purity LL | <90% | Alarm |
| H2 pressure L | <5.03 bar | Alarm |
| H2 pressure H | >5.45 bar | Alarm |
| Dew point at dryer inlet H | >−6.67°C | Alarm |
| Dew point at dryer outlet H | >−28.29°C | Alarm |
| Casing liquid detector H | >1.8 L | Alarm |
| Casing liquid detector HH | >2.0 L | Alarm |

**Gas changeover sequence**
Air → **CO2** → H2 (filling) | H2 → **CO2** → air (emptying)
CO2 is never skipped — air and hydrogen are never displaced directly.

⚠️ **H2 pressure window is only 0.42 bar wide: 5.03–5.45.** The seal oil differential is 0.41 bar. The two are tightly coupled — move one and the other reacts.

⚠️ Falling purity means either air in-leakage or moisture from the seal oil. Read it together with dew point: above **−28.29°C** at dryer outlet means moisture.

`#hydrogen #H2 #CO2 #generator`

---
---

## POST 16 — Stator sovutish suvi

**🇺🇿 Stator sovutish suvi — setpointlar**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Sarf L | <58 m³/s | Alarm |
| Sarf LL | <55 m³/s | Alarm |
| **Sarf LL trip** | **<54.1 m³/s, 15 sek** | **ST TRIP** |
| Bak sathi H | normal +100 | Alarm |
| Bak sathi L | normal −100 | Alarm |
| Asosiy filtr Δp H | >0.6 bar | Alarm |
| Deionizator Δp H | >0.6 bar | Alarm |
| Make-up filtr Δp H | >0.6 bar | Alarm |
| Stator o'ram sovutish suvi H | >48°C | Alarm |
| Stator o'ram chiqish harorati H | >78.2°C | Alarm |
| **Chiqish harorati HH trip** | **>83°C, 15 sek** | **ST TRIP** |
| O'tkazuvchanlik H | >0.5 μS/sm | Alarm |
| O'tkazuvchanlik HH | >9.9 μS/sm | Alarm |

⚠️ **Sarf bo'yicha uch bosqich: 58 → 55 → 54.1.** Oxirgi ikkisi orasida atigi **0.9 m³/s**. Sarf tushayotgani ko'rinsa — 58'da harakat qiling, 55'ni kutmang.

⚠️ **Chiqish harorati: alarm 78.2°C, trip 83°C — 4.8°C.** 15 sekund kechikish bor, lekin bu tekshirishga emas, shovqinni filtrlashga mo'ljallangan.

⚠️ O'tkazuvchanlik **0.5 → 9.9 μS/sm** — juda katta farq. 0.5'da deionizator ishlamayotganini bildiradi. 9.9'ga yetguncha kutish izolyatsiyaga zarar.

Stator suv kirish bosimi LL ham **ST trip** beradi (10MKF09CP001A/B/C, MED, 15 sek) — sozlamasi joyida kalibrlanadi.

---

**🇷🇺 Статорная охлаждающая вода — уставки**

| Параметр | Уставка | Действие |
|---|---|---|
| Расход L | <58 м³/ч | Сигнал |
| Расход LL | <55 м³/ч | Сигнал |
| **Расход LL защита** | **<54.1 м³/ч, 15 с** | **ОТКЛЮЧЕНИЕ ПТ** |
| Уровень бака H / L | норма ±100 | Сигнал |
| Δp основного фильтра H | >0.6 бар | Сигнал |
| Δp деионизатора H | >0.6 бар | Сигнал |
| Δp фильтра подпитки H | >0.6 бар | Сигнал |
| Темп. статорной воды H | >48°C | Сигнал |
| Темп. на выходе обмотки H | >78.2°C | Сигнал |
| **Темп. на выходе HH защита** | **>83°C, 15 с** | **ОТКЛЮЧЕНИЕ ПТ** |
| Электропроводность H / HH | >0.5 / >9.9 мкСм/см | Сигнал |

⚠️ **Три ступени по расходу: 58 → 55 → 54.1.** Между двумя последними **0.9 м³/ч**. Действуйте на 58, не ждите 55.

⚠️ **Выход: сигнал 78.2°C, защита 83°C — 4.8°C.** Выдержка 15 с нужна для отстройки от помех, а не для разбирательства.

⚠️ Электропроводность **0.5 → 9.9 мкСм/см**. На 0.5 деионизатор уже не работает. Ждать 9.9 — портить изоляцию.

Давление статорной воды на входе LL тоже даёт **отключение ПТ** (10MKF09CP001A/B/C, MED, 15 с), уставка калибруется на месте.

---

**🇬🇧 Stator Cooling Water — settings**

| Item | Setting | Action |
|---|---|---|
| Flow L | <58 m³/h | Alarm |
| Flow LL | <55 m³/h | Alarm |
| **Flow LL trip** | **<54.1 m³/h, 15 s** | **ST TRIP** |
| Tank level H / L | normal ±100 | Alarm |
| Main filter Δp H | >0.6 bar | Alarm |
| Deionizer Δp H | >0.6 bar | Alarm |
| Make-up filter Δp H | >0.6 bar | Alarm |
| Stator winding cooling water H | >48°C | Alarm |
| Winding outlet temp H | >78.2°C | Alarm |
| **Outlet temp HH trip** | **>83°C, 15 s** | **ST TRIP** |
| Conductivity H / HH | >0.5 / >9.9 μS/cm | Alarm |

⚠️ **Three flow steps: 58 → 55 → 54.1.** The last two are **0.9 m³/h** apart. Act at 58; don't wait for 55.

⚠️ **Outlet: alarm 78.2°C, trip 83°C — 4.8°C.** The 15 s delay is noise rejection, not investigation time.

⚠️ Conductivity **0.5 → 9.9 μS/cm**. At 0.5 the deionizer has already stopped doing its job. Waiting for 9.9 costs insulation life.

Stator water inlet pressure LL also gives an **ST trip** (10MKF09CP001A/B/C, MED, 15 s) — setpoint calibrated on site.

`#statorcooling #MKF #generator`

---
---

## POST 17 — Majburiy sovutish (forced cooling)

**🇺🇿 Forced cooling — ruxsat shartlari**

| Parametr | Setpoint | Ta'sir |
|---|---|---|
| Sovutish havosi harorati L | <150°C | Alarm |

**Ishga tushirish uchun barcha shartlar bajarilishi shart**
☑ ST to'xtagan
☑ Asboblar havosi tizimi tayyor, havo qizdirgichga sifatli havo beradi
☑ **ST rotor harorati <400°C**
☑ **Havo qizdirgichdan keyin havo harorati >150°C**
☑ Turning gear uzluksiz ishlayapti
☑ **Rotor kuchlanishi <70%** ruxsat etilgan nuqtadan
☑ **HP 1-bosqich bug' harorati va berilayotgan havo harorati farqi ≤250°C**
☑ **IP 1-bosqich bug' harorati va berilayotgan havo harorati farqi ≤250°C**
☑ **Rotor differensial kengayish detektori 1/2 <80%** ruxsat etilgan nuqtadan (**−7.4 mm**)
☑ Lube oil tizimi ishlayapti, turning gear ulangan
☑ Gland steam ishga tushirilgan
☑ Vakuum yaratilgan

⚠️ **Ikki tomonlama chegara:** havo **150°C**dan issiq bo'lishi shart (alarm past haroratda), lekin bug' bilan farqi **250°C**dan oshmasligi kerak. Ya'ni oyna rotor haroratiga qarab siljiydi.

⚠️ DXD **−7.4 mm** — bu 80% chegara. Trip esa **−9.26 mm**. Forced cooling paytida DXD manfiy tomonga ketadi, shuning uchun bu shart ayni shu yo'nalishda qo'yilgan.

---

**🇷🇺 Принудительное расхолаживание — условия пуска**

| Параметр | Уставка | Действие |
|---|---|---|
| Темп. охлаждающего воздуха L | <150°C | Сигнал |

**Все условия обязательны**
☑ ПТ остановлена
☑ Система КИПиА готова подать качественный воздух в воздухоподогреватель
☑ **Темп. ротора ПТ <400°C**
☑ **Темп. воздуха после подогревателя >150°C**
☑ ВПУ работает непрерывно
☑ **Напряжения в роторе <70%** допустимого
☑ **Разница темп. пара 1-й ступени ЦВД и подаваемого воздуха ≤250°C**
☑ **Разница темп. пара 1-й ступени ЦСД и подаваемого воздуха ≤250°C**
☑ **ОРС 1/2 <80%** допустимого (**−7.4 мм**)
☑ Маслосистема в работе, ВПУ включено
☑ Уплотняющий пар подан ☑ Вакуум набран

⚠️ **Двусторонний предел:** воздух должен быть горячее **150°C**, но разница с паром не выше **250°C**. Окно смещается вместе с температурой ротора.

⚠️ ОРС **−7.4 мм** — это 80%. Защита на **−9.26 мм**. При расхолаживании ОРС уходит в минус, поэтому условие задано именно в эту сторону.

---

**🇬🇧 Forced Cooling — permissives**

| Item | Setting | Action |
|---|---|---|
| Cooling air temp L | <150°C | Alarm |

**All conditions required to start**
☑ ST shut down
☑ Instrument air ready to supply qualified air to the air heater
☑ **ST rotor temperature <400°C**
☑ **Air temperature after heater >150°C**
☑ Turning gear running continuously
☑ **Rotor stress <70%** of allowable
☑ **HP 1st stage steam temp vs supply air temp differential ≤250°C**
☑ **IP 1st stage steam temp vs supply air temp differential ≤250°C**
☑ **Differential expansion detector 1/2 <80%** of allowable (**−7.4 mm**)
☑ Lube oil in service, turning gear engaged
☑ Gland steam in service ☑ Vacuum established

⚠️ **Two-sided limit:** air must be hotter than **150°C**, yet within **250°C** of the steam. The window moves with rotor temperature.

⚠️ DXD **−7.4 mm** is the 80% point; the trip is **−9.26 mm**. Differential expansion runs negative during forced cooling — which is why the permissive is written on that side.

`#forcedcooling #DXD #shutdown`

---
---

## POST 18 — Tebranish: sabab va belgi

**🇺🇿 Tebranish diagnostikasi — chastota belgisi bo'yicha**

Chegaralar (ISO 20816-2 bo'yicha): alarm **>165 μm**, trip **>240 μm**, 1/16 ovoz berish.

**Muvozanatsizlik**
• Har doim aylanish tezligi bilan **sinxron (1×)**
• Bir xil tezlik va yuklamada **fazasi va amplitudasi o'zgarmas**
• Aylanish chastotasidan boshqa chastotadagi tebranish muvozanatsizlik EMAS
⚠️ **Sinxron tebranish to'satdan o'zgarsa** — bu ichki shikast, masalan kurak qopqog'i uchgan bo'lishi mumkin

**Ishqalanish (rubbing)**
• Ko'pincha kritik tezlik yaqinida yuzaga keladi
• **Birinchi kritik tezlikdan past**: rotor egilishi → muvozanatsizlik ortadi → egilish yanada ortadi (o'z-o'zini kuchaytiruvchi zanjir)
• **Birinchi kritik tezlikdan yuqori**: egilishdan kelib chiqqan muvozanatsizlik rotor og'ishini kamaytiradi, ishqalanish yengillashadi
• Shuning uchun birinchi kritik tezlikni **tez o'tish** kerak

⚠️ **Agar birinchi kritik tezlikdan past yoki uning yaqinida ishqalanish sababli tebranish keskin oshib trip bo'lsa — tezlikni oshirishni to'xtating va turning gear'da kamida 4 SOAT aylantiring.** Bu rotorni to'g'rilash va zarbadan xalos qilish uchun.

**Oil whip**
• Xarakterli chastota — **aylanish tezligining taxminan yarmi (0.5×)**
• To'satdan tebranish oshishining asosiy sabablaridan biri
• Sabab: podshipnik yuklamasining kamayishi yoki yog' qovushqoqligining ortishi
• Qovushqoqlik harorat pasayishi bilan ortadi
⚠️ Yog' haroratini ko'tarish oil whip amplitudasini kamaytirishi mumkin, **lekin keskin ko'tarilsa qovushqoqlik tushib podshipnik shikastlanadi**

**Nomutanosiblik (misalignment)**
• Oil whip, tebranish beqarorligi
• **Kritik tezlikning ko'zga ko'rinarli siljishi**
• Kritik tezlikdagi g'ayritabiiy yuqori tebranish
• Kritik tezlik tebranishi keng tezlik diapazonida o'zgarishi
• **Podshipnik metallining g'ayritabiiy harorati** ham nomutanosiblikdan bo'lishi mumkin
• Mufta konsentrikligining yo'qligi — qo'shni rotorlarda "bukilish"ga olib keladi

**Termik sezuvchanlik**
• Rotor harorat o'zgarishiga sezgir bo'lib qoladi
• Sezilarli egilish va vaqtinchalik muvozanatsizlik beradi

⚠️ Yuqori tebranish ko'pincha **bitta emas, bir nechta sababning birikmasi**dan kelib chiqadi.

⚠️ **Kritik tezlikda ushlab turish yoki qayta ishga tushirish TAQIQLANADI.** Agar turbina ish tezligi diapazonida ushlab turilmagan bo'lsa, qayta ishga tushirishdan oldin tezlikni **partial hold speed**gacha tushirish shart.

---

**🇷🇺 Диагностика вибрации — по частотному признаку**

Пределы (по ISO 20816-2): сигнал **>165 мкм**, защита **>240 мкм**, голосование 1/16.

**Небаланс**
• Всегда **синхронен оборотам (1×)**
• При одинаковых оборотах и нагрузке **фаза и амплитуда постоянны**
• Вибрация на других частотах — это не небаланс
⚠️ **Резкое изменение синхронной вибрации** — вероятно внутреннее повреждение, например срыв бандажа

**Задевание**
• Чаще возникает вблизи критической частоты
• **Ниже первой критической**: изгиб ротора → рост небаланса → усиление изгиба (самоусиление)
• **Выше первой критической**: небаланс от изгиба уменьшает прогиб, задевание ослабевает
• Поэтому первую критическую проходят **быстро**

⚠️ **Если ниже или вблизи первой критической произошло отключение по резкому росту вибрации от задевания — прекратите разворот и вращайте на ВПУ не менее 4 ЧАСОВ.**

**Масляная вибрация (oil whip)**
• Характерная частота — **около половины оборотной (0.5×)**
• Одна из главных причин внезапного роста вибрации
• Причина: снижение нагрузки на подшипник или рост вязкости масла
• Вязкость растёт при снижении температуры
⚠️ Подъём температуры масла может снизить амплитуду, **но резкий подъём уронит вязкость и повредит подшипник**

**Расцентровка**
• Масляная вибрация, неустойчивость
• **Заметное смещение критической частоты**
• Аномально высокая вибрация на критической
• Вибрация критической меняется в широком диапазоне оборотов
• **Аномальная температура баббита** тоже может быть от расцентровки
• Отсутствие концентричности муфты — «излом» в соседних роторах

**Термочувствительность**
• Ротор реагирует на изменение температуры изгибом и временным небалансом

⚠️ Высокая вибрация чаще результат **сочетания нескольких причин**, а не одной.

⚠️ **Задерживаться на критической частоте или повторно пускать в этом диапазоне ЗАПРЕЩЕНО.** Если турбина не удержана в рабочем диапазоне — сбросить обороты до **partial hold speed** перед повторным разворотом.

---

**🇬🇧 Vibration Diagnosis — by frequency signature**

Limits (per ISO 20816-2): alarm **>165 μm**, trip **>240 μm**, 1/16 voting.

**Unbalance**
• Always **synchronous with running speed (1×)**
• **Constant phase and magnitude** at the same speed and similar load
• Vibration at any other frequency is not unbalance
⚠️ **A sudden change in synchronous vibration** points to internal damage — e.g. a lost bucket cover

**Rubbing**
• Most likely near critical speed
• **Below first critical**: rotor bow → more unbalance → more deflection → more rubbing (self-reinforcing)
• **Above first critical**: bow-induced unbalance reduces deflection and relieves rubbing
• Hence: pass the first critical **quickly**

⚠️ **If a trip occurs from rapidly rising vibration due to rubbing below or near first critical — stop the speed-up and run on turning gear for at least 4 HOURS** to straighten the rotor and relieve the impact.

**Oil whip**
• Characteristic frequency — **about half running speed (0.5×)**
• A major cause of sudden vibration increase
• Driven by reduced bearing load or increased oil viscosity
• Viscosity rises as temperature falls
⚠️ Raising oil temperature can reduce whip amplitude, **but a sharp rise drops viscosity and damages the bearing**

**Misalignment**
• Oil whipping, vibration instability
• **Visible shift in critical speed**
• Abnormally high critical speed vibration
• Critical speed vibration varying over a wide speed range
• **Abnormal bearing metal temperature** can also be misalignment
• Lack of coupling concentricity puts a slight bend into adjacent rotors

**Thermal sensitivity**
• Rotor responds to temperature change with bowing and temporary unbalance

⚠️ High vibration is often a **combination of causes**, not a single one.

⚠️ **Dwelling at or restarting within the critical speed range is forbidden.** If the turbine was not held within the operating speed range, let speed fall to **partial hold speed** before restarting.

`#vibration #oilwhip #rubbing #misalignment`

---
---

## POST 19 — Kirish bug' bosimi va haroratining ruxsat etilgan o'zgarishi

**🇺🇿 Bug' bosimi va harorati — 12 oylik limitlar**

**BOSIM**
• 12 oylik **o'rtacha** bosim nominaldan oshmasligi shart
• O'rtacha saqlanganda joriy bosim **105%**dan oshmasligi kerak
• Tasodifiy chetlanish **125%**gacha ruxsat etiladi, lekin 12 oyda jami **12 soatdan** oshmasligi shart

**HARORAT**
• 12 oylik **o'rtacha** harorat nominaldan oshmasligi shart
• Odatda nominaldan **+8°C**dan ortmaydi
• **+8...+14°C** oralig'i: 12 oyda jami **400 soatdan** oshmasin
• **+14...+28°C** oralig'i: bir marta **15 daqiqagacha**, 12 oyda jami **80 soatdan** oshmasin
• **Nominaldan +28°C dan yuqoriga hech qanday sharoitda chiqmasin**

**Parallel quvurlar**
• Bir nuqtaga ikki yoki undan ortiq quvurdan bug' berilsa, ular orasidagi harorat farqi **14°C**dan oshmasin
• **42°C**gacha farq ruxsat etiladi, lekin har 4 soatda **15 daqiqadan** oshmagan holda
• Eng issiq quvurdagi harorat yuqoridagi umumiy chegaralardan chiqmasligi shart

⚠️ Bu limitlar smenaviy emas — **yillik hisob**. Ya'ni siz +20°C da 15 daqiqa ishlagan bo'lsangiz, u 80 soatlik yillik byudjetdan yeyiladi. Jurnalda qayd qilinmasa, byudjet qayerda ekanini hech kim bilmaydi.

---

**🇷🇺 Давление и температура острого пара — 12-месячные пределы**

**ДАВЛЕНИЕ**
• **Среднее** за 12 месяцев не выше номинала
• При соблюдении среднего текущее не выше **105%**
• Случайные отклонения до **125%**, суммарно не более **12 часов** за 12 месяцев

**ТЕМПЕРАТУРА**
• **Среднее** за 12 месяцев не выше номинала
• Обычно не более **+8°C** от номинала
• **+8...+14°C**: суммарно не более **400 часов** за 12 месяцев
• **+14...+28°C**: разово до **15 минут**, суммарно не более **80 часов** за 12 месяцев
• **Выше +28°C от номинала — ни при каких условиях**

**Параллельные трубопроводы**
• Разница температур между ними не более **14°C**
• До **42°C** допускается, но не дольше **15 минут** в любые 4 часа
• Температура в самом горячем трубопроводе не выходит за общие пределы

⚠️ Это не сменные, а **годовые** лимиты. 15 минут на +20°C съедаются из годового бюджета в 80 часов. Без записи в журнале никто не знает, сколько бюджета осталось.

---

**🇬🇧 Inlet Steam Pressure and Temperature — 12-month limits**

**PRESSURE**
• **Average** over any 12 months must not exceed nominal
• With that average held, pressure must not exceed **105%**
• Accidental excursions to **125%** allowed, total not exceeding **12 hours** in any 12 months

**TEMPERATURE**
• **Average** over any 12 months must not exceed nominal
• Normally not more than **+8°C** above nominal
• **+8 to +14°C**: total not exceeding **400 hours** in any 12 months
• **+14 to +28°C**: excursions up to **15 minutes**, total not exceeding **80 hours** in any 12 months
• **Never more than +28°C above nominal, under any circumstances**

**Parallel pipelines**
• Temperature difference between pipelines feeding one connection: max **14°C**
• Up to **42°C** allowed for excursions no longer than **15 minutes** in any 4 hours
• The hottest pipeline must still stay within the limits above

⚠️ These are **annual** budgets, not shift limits. Fifteen minutes at +20°C comes out of an 80-hour yearly allowance. If it isn't logged, nobody knows how much is left.

`#steamlimits #allowable #lifetime`

---
---

## POST 20 — Main / reheat harorat farqi va harorat pasayishi

**🇺🇿 Harorat farqi va tushish tezligi**

**Main va reheat bug' harorati farqi (7.2.6)**
Farq = main bug' harorati − reheat bug' harorati
Qarama-qarshi oqimli HP-IP turbina uchun chegaralangan (Fig 7-2-1):
• **Zona (b)** — ruxsat etilgan: hot reheat main'dan issiq
• **Zona (c)** — ruxsat etilgan: main hot reheat'dan issiq
• **Zona (a) va (d)** — **ruxsat etilmagan**. Qisqa muddatli o'tkinchi rejimda qabul qilinishi mumkin, lekin uzoq ishlash **ishqalanish va yuqori tebranishga** olib keladi
Ikkala harorat ham turbina klapanlari kirishida o'lchanadi.

**Harorat pasayishi (7.2.7)**
Pasayish = joriy harorat − 15 daqiqa oldingi harorat
• **−56°C yoki past** → qozonni boshqarib farqni kamaytirish kerak
• **−83°C yoki past** → turbinani **darhol to'xtatish yoki trip qilish**

**Yuklama tushirishda harorat tushish tezligi (Table 7-2-6)**
• 50% → min yuklama: **≤5%/min**
• Main / hot reheat harorati tushish tezligi: **<1.5°C/min**

⚠️ **−83°C — bu trip setpointi (Table 8-1-1, №33-34).** Ya'ni −56°C bu ogohlantirish emas, **harakat qilish nuqtasi**. −56 va −83 orasida 27°C bor, lekin bug' harorati tez tushganda bu masofa daqiqalar ichida yopiladi.

⚠️ Bug' harorati keskin tushsa **termik kuchlanish va differensial kengayish tez ortadi** — DXD trip'i (+12.07 / −9.26 mm) bug' harorat trip'idan oldin ishlashi mumkin.

---

**🇷🇺 Разница температур и скорость снижения**

**Разница главного и промперегретого пара (7.2.6)**
Разница = темп. главного пара − темп. промперегрева
Для ЦВД-ЦСД встречного потока ограничено (Fig 7-2-1):
• **Зона (b)** — допустима: промперегрев горячее главного
• **Зона (c)** — допустима: главный горячее промперегрева
• **Зоны (a) и (d)** — **недопустимы**. Кратковременно в переходных режимах возможно, длительная работа ведёт к **задеваниям и высокой вибрации**
Обе температуры измеряются на входе в клапаны турбины.

**Снижение температуры (7.2.7)**
Снижение = текущая − температура 15 минут назад
• **−56°C и ниже** → регулировать котёл, уменьшить разницу
• **−83°C и ниже** → **немедленный останов или отключение**

**Скорость снижения при разгрузке (Table 7-2-6)**
• 50% → мин. нагрузка: **≤5%/мин**
• Скорость снижения темп. главного / промперегретого пара: **<1.5°C/мин**

⚠️ **−83°C — это уставка защиты** (Table 8-1-1, №33-34). Значит −56°C не сигнал, а **точка действия**. Между ними 27°C, но при быстром падении это минуты.

⚠️ При резком падении температуры **термонапряжения и ОРС растут быстро** — защита по ОРС (+12.07 / −9.26 мм) может сработать раньше защиты по температуре пара.

---

**🇬🇧 Main / Reheat Differential and Downward Temperature Change**

**Main-to-reheat temperature difference (7.2.6)**
Difference = main steam temp − reheat steam temp
Limited for the opposed-flow HP-IP turbine (Fig 7-2-1):
• **Zone (b)** — allowable: hot reheat hotter than main
• **Zone (c)** — allowable: main hotter than hot reheat
• **Zones (a) and (d)** — **not allowable**. Acceptable briefly in transients; long-term operation causes **unexpected rubbing and high vibration**
Both measured at the turbine valve inlets.

**Downward temperature change (7.2.7)**
Downward = current temperature − temperature 15 minutes ago
• **−56°C or lower** → control the boiler to reduce the difference
• **−83°C or lower** → **shut down or trip the turbine immediately**

**Rate limits during unloading (Table 7-2-6)**
• 50% → min load: **≤5%/min**
• Main / hot reheat temperature decreasing rate: **<1.5°C/min**

⚠️ **−83°C is the trip setpoint** (Table 8-1-1, items 33-34). So −56°C is not a warning — it's the **action point**. There is 27°C between them, and a fast-falling steam temperature closes that in minutes.

⚠️ A sharp temperature drop raises **thermal stress and differential expansion quickly** — the DXD trip (+12.07 / −9.26 mm) can act before the steam temperature trip does.

`#steamtemp #thermalstress #DXD`

---
---

## POST 21 — LP exhaust bosimi: chegaralar va vaqt byudjeti

**🇺🇿 Exhaust bosimi — bosqichlar va ruxsat etilgan vaqt**

| Holat | Pout [bar] |
|---|---|
| **H1** Alarm | 0.33 |
| **H2** Kechiktirilgan trip | 0.35 |
| **H3** Trip | 0.45 |

**Ish vaqti chegaralari (Table 7-2-5)**
| Diapazon | Bir marta maksimal | Umumiy chegara |
|---|---|---|
| H1 < Pout < H2 | **10 soat** | **100 soat** |
| H2 < Pout < H3 | **5 daqiqa** | **10 soat** |
| H3 < Pout | **Darhol trip** | — |

**Nima uchun cheklangan**
• Yuqori exhaust bosimi loyihadan tashqari oqim hosil qiladi → **oxirgi bosqich kuraklarida tebranish javobi ortadi** → yuqori siklli charchash sinishi
• Yuqori exhaust bosimida past sarf → **windage tufayli kurak harorati ko'tariladi** → kurak strukturasi, bikirligi va demplerlariga salbiy ta'sir

⚠️ **Exhaust bosimi faqat exhaust hood'da o'lchanadi.** Kondensatorda yoki hot well'da o'lchangan qiymat alarm va trip uchun **ishlatilmaydi**.

⚠️ **Qo'shni hood'lar orasidagi bosim farqi 0.068 bar**dan oshmasligi shart.

⚠️ Alarm va trip bosimi **vakuumda o'lchanadi** — shuning uchun sozlamalar stansiya **balandligiga qarab** hisobga olinishi kerak.

---

**🇷🇺 Давление выхлопа ЦНД — ступени и бюджет времени**

| Условие | Pout [бар] |
|---|---|
| **H1** Сигнал | 0.33 |
| **H2** Защита с выдержкой | 0.35 |
| **H3** Защита | 0.45 |

**Пределы по времени (Table 7-2-5)**
| Диапазон | Разово | Суммарно |
|---|---|---|
| H1 < Pout < H2 | **10 часов** | **100 часов** |
| H2 < Pout < H3 | **5 минут** | **10 часов** |
| H3 < Pout | **Немедленное отключение** | — |

**Почему ограничено**
• Высокое давление выхлопа → нерасчётный поток → **рост вибрационного отклика лопаток последней ступени** → многоцикловая усталость
• Малый расход при высоком давлении → **нагрев лопатки от вентиляционных потерь** → ухудшение структуры, жёсткости и демпфирования

⚠️ **Давление выхлопа измеряется только в выхлопном патрубке.** Значения с конденсатора или конденсатосборника для сигнала и защиты **не используются**.

⚠️ Разница давлений между соседними патрубками не более **0.068 бар**.

⚠️ Уставки заданы **по вакууму** — учитывайте **высоту площадки** над уровнем моря.

---

**🇬🇧 LP Exhaust Pressure — steps and time budget**

| Condition | Pout [bar] |
|---|---|
| **H1** Alarm | 0.33 |
| **H2** Delayed trip | 0.35 |
| **H3** Trip | 0.45 |

**Operating limits (Table 7-2-5)**
| Range | Max per occurrence | Total limit |
|---|---|---|
| H1 < Pout < H2 | **10 hours** | **100 hours** |
| H2 < Pout < H3 | **5 minutes** | **10 hours** |
| H3 < Pout | **Immediate trip** | — |

**Why limited**
• High exhaust pressure gives off-design flow → **increased blade vibration response on the last stage** → high cycle fatigue failure
• Low flow at high exhaust pressure → **blade temperature rises from windage** → affects blade structure, stiffness and damping

⚠️ **Exhaust pressure is measured in the exhaust hood.** Values from the condenser or hot well **must not be used** for the turbine exhaust alarm and trip.

⚠️ Maximum pressure difference from an adjacent hood: **0.068 bar**.

⚠️ Alarm and trip pressures are **measured in vacuum** — the setting must be factored for plant **altitude**.

`#LPexhaust #backpressure #LSB`

---
---

## POST 22 — Chastota bo'yicha ish chegaralari

**🇺🇿 Off-frequency — ruxsat etilgan diapazonlar va vaqt**

| Chastota diapazoni | Maks. quvvat (%) | Bir marta maks. | Xizmat muddati uchun jami |
|---|---|---|---|
| 46.0–47.0 Hz | 70 | **30 sekund** | **30 daqiqa** |
| 47.0–48.0 Hz | 100 | **15 daqiqa** | **120 daqiqa** |
| 48.0–48.5 Hz | 100 | **30 daqiqa** | **600 daqiqa** |
| **48.5–51.0 Hz** | — | **Doimiy ish** | — |
| 51.0–52.0 Hz | 100 | **30 daqiqa** | **600 daqiqa** |
| 52.0–52.5 Hz | 100 | **2 daqiqa** | **120 daqiqa** |
| 52.5–53.5 Hz | 70 | **30 sekund** | **30 daqiqa** |

**Chegaralovchi element — uzun kuraklar**
Ularning quyi tebranish modalari ish tezligining quyi garmonikalaridan ajratilgan (Campbell diagrammasi, Fig 7-2-4). Chastota nominal qiymatdan chetlashsa, bu **ish tezligi (A)** va **kurak rezonans chastotasining bug' garmonikasi bilan mos kelishi (B)** orasidagi zaxiraga kirib boradi.

Mos kelish sodir bo'lsa — kurakdagi javob kuchlanishi **egri chiziqning cho'qqisiga** ko'tariladi (Fig 7-2-5).

⚠️ **Jami byudjet turbinaning butun xizmat muddatiga.** 46–47 Hz uchun 30 daqiqa — bu bir yilga emas, 30 yilga. Har bir hodisa qayd qilinishi shart.

⚠️ 48.5–51.0 Hz — bu **Table 1-1-1**dagi ish diapazoni bilan bir xil. Undan tashqarida ishlash har doim vaqt byudjetini yeydi.

---

**🇷🇺 Работа на отклоняющейся частоте — диапазоны и время**

| Диапазон частоты | Макс. мощность (%) | Разово | Суммарно за срок службы |
|---|---|---|---|
| 46.0–47.0 Гц | 70 | **30 секунд** | **30 минут** |
| 47.0–48.0 Гц | 100 | **15 минут** | **120 минут** |
| 48.0–48.5 Гц | 100 | **30 минут** | **600 минут** |
| **48.5–51.0 Гц** | — | **Постоянная работа** | — |
| 51.0–52.0 Гц | 100 | **30 минут** | **600 минут** |
| 52.0–52.5 Гц | 100 | **2 минуты** | **120 минут** |
| 52.5–53.5 Гц | 70 | **30 секунд** | **30 минут** |

**Ограничивающий элемент — длинные лопатки**
Их низшие формы колебаний отстроены от низших гармоник оборотной частоты (диаграмма Кэмпбелла). Отклонение частоты съедает запас между **рабочими оборотами (A)** и **совпадением резонанса лопатки с соседней паровой гармоникой (B)**.

При совпадении отклик напряжения в лопатке выходит **на пик кривой**.

⚠️ **Суммарный бюджет — на весь срок службы.** 30 минут для 46–47 Гц это не в год, а на 30 лет. Каждый случай надо фиксировать.

⚠️ 48.5–51.0 Гц совпадает с рабочим диапазоном из **Table 1-1-1**. Всё, что вне — расходует бюджет.

---

**🇬🇧 Off-Frequency Operation — bands and time limits**

| Frequency band | Max output (%) | Max per occurrence | Total for service life |
|---|---|---|---|
| 46.0–47.0 Hz | 70 | **30 seconds** | **30 minutes** |
| 47.0–48.0 Hz | 100 | **15 minutes** | **120 minutes** |
| 48.0–48.5 Hz | 100 | **30 minutes** | **600 minutes** |
| **48.5–51.0 Hz** | — | **Permanent operation** | — |
| 51.0–52.0 Hz | 100 | **30 minutes** | **600 minutes** |
| 52.0–52.5 Hz | 100 | **2 minutes** | **120 minutes** |
| 52.5–53.5 Hz | 70 | **30 seconds** | **30 minutes** |

**Limiting components — the long buckets**
Their lower vibration modes are separated from the lower harmonics of running speed (Campbell diagram). Off-frequency operation encroaches on the margin between **rated operating speed (A)** and **coincidence of bucket resonance with its adjacent steam harmonic (B)**.

At coincidence, bucket response stress rises to **the peak of the curve**.

⚠️ **The total budget is for the whole service life.** Thirty minutes at 46–47 Hz is not per year — it's for thirty years. Every occurrence must be logged.

⚠️ 48.5–51.0 Hz matches the operating range in **Table 1-1-1**. Anything outside spends budget.

`#offfrequency #Campbell #LSB`

---
---

## POST 23 — Bug' sifati: normal va ishga tushirish

**🇺🇿 Bug' sifati — chegaralar**

**Ishga tushirish uchun (Table 7-2-3, superheat va reheat bug')**
| Parametr | Birlik | Chegara |
|---|---|---|
| Kation o'tkazuvchanligi (25°C) | μS/sm | **≤1.0** |
| Natriy, Na | μg/kg | **≤12** |
| Kremnezyom, SiO₂ | μg/kg | **≤40** |
| Xlorid, Cl⁻ | μg/kg | **≤12** |
| Sulfat, SO₄²⁻ | μg/kg | **≤12** |
| Umumiy organik uglerod, TOC | μg/kg | **≤200** |

Agar ishga tushirishda barcha ko'rsatkichlar shu chegaralar ichida bo'lsa — **chetlanish vaqti yillik jami soatlarga hisoblanmaydi**.

**Gland steam sifati (7.2.3)**
Standartda alohida belgilanmagan. Qayta qizdirish qozoni uchun oziqlantiruvchi suv sifatiga mos bo'lishi kerak (10 bargacha, EN 12952-12):
• Tiniq, muallaq zarrachalarsiz
• pH **>9.2**
• Umumiy qattiqlik **<0.02 mmol/l**
• Temir (Fe) **<0.05 mg/l**
• Mis (Cu) **<0.02 mg/l**
• Erigan kislorod (O₂) **<0.02 mg/l**
• Kation o'tkazuvchanligi **maks. 0.3 μS/sm**
• Natriy (Na) **<0.01 mg/l**
• Kremnezyom (SiO₂) **<0.02 mg/l**
• TOC **<0.2 mg/l**

⚠️ Gland steam sifati past bo'lishi mumkin, **lekin cho'kma hosil qilmasligi shart** — cho'kma keyinchalik ishchi bug' sifatini tushiradi.

---

**🇷🇺 Качество пара — нормальная работа и пуск**

**Для пусков (Table 7-2-3, перегретый и промперегретый пар)**
| Параметр | Ед. | Предел |
|---|---|---|
| Катионная проводимость (25°C) | мкСм/см | **≤1.0** |
| Натрий, Na | мкг/кг | **≤12** |
| Кремнезём, SiO₂ | мкг/кг | **≤40** |
| Хлорид, Cl⁻ | мкг/кг | **≤12** |
| Сульфат, SO₄²⁻ | мкг/кг | **≤12** |
| Общий органический углерод, TOC | мкг/кг | **≤200** |

Если при пуске все параметры в этих пределах — **время отклонения не засчитывается в годовые часы**.

**Качество уплотняющего пара (7.2.3)**
Отдельно не нормируется. Должно соответствовать питательной воде котла промперегрева (до 10 бар, EN 12952-12):
• Прозрачная, без взвесей | pH **>9.2** | Общая жёсткость **<0.02 ммоль/л**
• Fe **<0.05 мг/л** | Cu **<0.02 мг/л** | O₂ **<0.02 мг/л**
• Катионная проводимость **макс. 0.3 мкСм/см**
• Na **<0.01 мг/л** | SiO₂ **<0.02 мг/л** | TOC **<0.2 мг/л**

⚠️ Уплотняющий пар может быть хуже рабочего, **но не должен давать отложений** — они потом ухудшат качество рабочего пара.

---

**🇬🇧 Steam Purity — normal operation and start-up**

**Start-up guidelines (Table 7-2-3, superheat and reheat steam)**
| Parameter | Unit | Target |
|---|---|---|
| Cation conductivity (25°C) | μS/cm | **≤1.0** |
| Sodium, Na | μg/kg | **≤12** |
| Silica, SiO₂ | μg/kg | **≤40** |
| Chloride, Cl⁻ | μg/kg | **≤12** |
| Sulfate, SO₄²⁻ | μg/kg | **≤12** |
| Total organic carbon, TOC | μg/kg | **≤200** |

If all target parameters stay within these limits during start-up, **the excursion time is not counted in the cumulative hours per year**.

**Gland steam quality (7.2.3)**
Not specified in any standard. Should meet feed water quality for the reheater boiler (up to 10 bar, EN 12952-12):
• Clear, free of suspended solids | pH **>9.2** | Total hardness **<0.02 mmol/l**
• Fe **<0.05 mg/l** | Cu **<0.02 mg/l** | O₂ **<0.02 mg/l**
• Cation conductivity **max 0.3 μS/cm**
• Na **<0.01 mg/l** | SiO₂ **<0.02 mg/l** | TOC **<0.2 mg/l**

⚠️ Gland steam may be lower quality than driving steam, **but must not create deposits** — those later degrade operational steam quality.

`#steampurity #chemistry #startup`

---
---

## POST 24 — Suv kirishini aniqlash

**🇺🇿 Suv kirishi — qanday aniqlanadi**

**Birinchi belgilar**
• Qiyin ishga tushish (rough start)
• Bug' quvurlarida **zarba (hammering)**
• Rotor ekssentrisitetining oshishi
• Katta differensial kengayish
• Tebranishning keskin oshishi

**Suv aniqlash termoparalari**
• HP va reheat korpuslarida **juftlab** o'rnatilgan — yuqori va pastki, bir necha o'q bo'yicha nuqtada
• Normal holatda juftlikdagi yuqori va pastki termopara **taxminan bir xil** haroratni ko'rsatadi
• **Pastki termopara haroratining keskin tushishi**, yoki juftlik orasida sezilarli farq — bu suv borligi va korpus deformatsiyasi belgisi

**Alarm sozlamasi**
• Juftlikdagi **yuqori** termopara **pastki**dan **28°C** yoki ko'proq issiq bo'lganda alarm
• **28°C — boshlang'ich nuqta.** Normal ish ma'lumotlari to'plangandan keyin **56°C**gacha ko'tarish mumkin
• Ba'zi hollarda suv bo'lmasa ham farq 28°C dan oshadi

**Steam seal kollektorida**
• Suv yoki sovuq bug' **juda past harorat** yoki **haroratning keskin o'zgarishi** bilan aniqlanadi
• Sababni aniqlash oson: harorat o'zgarishini admission klapan ishlashi yoki seal bug' manbasining o'zgarishi bilan bog'lang

**Thrust bearing wear detector**
• Bug' quvuriga suv "tiqini" (slug) kirib, HP yoki reheat bowl orqali turbinaga tushsa — suvning zichligi yuqoriligi sababli **katta o'q kuchi** hosil bo'ladi
• Thrust alarm yoki trip bo'lsa: **bowl haroratlarini keskin tushish uchun tekshiring**, va (agar diafragma bilan o'lchansa) **bug' sarfida keskin sakrash** bor-yo'qligini tekshiring

---

**🇷🇺 Обнаружение попадания воды**

**Первые признаки**
• Тяжёлый пуск • **Гидроудары** в паропроводах • Рост эксцентриситета ротора
• Большое относительное расширение • Резкий рост вибрации

**Термопары обнаружения воды**
• В корпусах ЦВД и промперегрева установлены **парами** — верх и низ, в нескольких точках по оси
• В норме верхняя и нижняя термопары пары показывают **примерно одинаково**
• **Резкое падение нижней**, либо существенная разница в паре — признак воды и деформации корпуса

**Уставка сигнализации**
• Сигнал, когда **верхняя** термопара горячее **нижней** на **28°C** и более
• **28°C — стартовая точка.** По накоплении опыта эксплуатации можно поднять до **56°C**
• Иногда разница превышает 28°C и без воды

**В коллекторе уплотняющего пара**
• Вода или холодный пар видны по **очень низкой температуре** или **резкому её изменению**
• Причину найти легко: связать изменение с работой клапана подачи или сменой источника уплотняющего пара

**Датчик износа упорного подшипника**
• Пробка воды через ЦВД или паровпуск промперегрева даёт **большое осевое усилие** из-за высокой плотности воды
• При сигнале или защите по упорному: проверить **резкое падение температур паровпускных камер** и **всплеск расхода пара** (если измеряется диафрагмой)

---

**🇬🇧 Detecting Water Induction**

**First signs**
• Rough starts • **Hammering of steam lines** • High rotor eccentricity
• Large differential expansions • Large vibration increases

**Water detection thermocouples**
• Fitted in **pairs** — uppers and lowers, at several axial points in the HP and reheat outer shells
• Under normal conditions, top and bottom of a pair read **approximately the same**
• An **abrupt decrease in the bottom thermocouple**, or a substantial upper-to-lower differential, indicates water and resulting shell distortion

**Alarm setting**
• Alarm when the **upper** thermocouple of any pair exceeds the **lower** by **28°C** or more
• **28°C is a starting point** — adjust upwards to **56°C** as normal operating data justifies it
• In some cases upper-to-lower exceeds 28°C even without water

**In the steam seal header**
• Water or cold steam shows as **very low temperature** or **abrupt temperature change** on the recorder
• Cause is easily established by relating the change to admission valve operation or transfer of the sealing steam source

**Thrust bearing wear detector**
• A slug of water carrying into the steam piping and entering through the HP or reheat bowls causes **large axial thrust** because of the higher density
• On a thrust alarm or trip: check turbine **bowl temperatures for sudden drops**, and check **steam flow for sudden spikes** (if measured with an orifice device)

`#waterinduction #thermocouple #thrust`

---
---

## POST 25 — Suv kirganda operator harakati

**🇺🇿 Suv kirdi — nima qilish kerak**

Manualda ochiq yozilgan: **eng jiddiy shikast ko'pincha suv kirishining birinchi belgisidan ancha keyin yuzaga keladi va operatorning harakati (yoki harakatsizligi) natijasi bo'ladi.**

Operator ta'sir qila oladigan 3 omil: **suv miqdori, bug' sarfi, aylanish tezligi.**

**1. Suv miqdori**
Birinchi belgidayoq manbani yopish va suvni turbina hamda bug' quvurlaridan chiqarish kerak.

**2. Bug' sarfi**
Turbina yuklama ostida ishlayotganda bug' oqimi suvni **bir tekis taqsimlaydi va deformatsiyani kamaytiradi**. Suv chiqarilgandan keyin korpus bug' oqimi saqlansa **tezroq to'g'rilanadi**.
Shuning uchun: **yuklama ostida suv kirsa — turbinani ishlatishda davom eting**, agar yuqori tebranish, katta differensial kengayish yoki boshqa jiddiy holat to'xtatishni talab qilmasa. Suv manbasi darhol yopiladi.

**3. Tezlik**
• **Turning gear'da sekin aylantirish eng yaxshisi** — ishqalanishdan hosil bo'lgan issiqlik doimiy egilishga yetarli bo'lmaydi
• **Nominal tezlikdan past tezlanayotganda suv kirsa — trip qiling va turning gear'ga qo'ying**
• **Kritik tezliklar diapazoni va undan pastda ishqalanish juda halokatli** — rotor ishqalanish kuchini oshiradigan tomonga egiladi
• ⚠️ **Bir necha yuz rpm'da uzoq ishlatish orqali egilgan rotorni to'g'rilashga urinish — xato tushuncha. Shu yo'l bilan jiddiy shikast yetkazilgan.**
• Kritik tezlikdan **ancha yuqorida** ishqalanish bo'lsa, rotor ishqalanishni **kamaytiradigan** tomonga egiladi — bu ham nominal tezlikda ishlashni davom ettirish foydali bo'lishining sababi

**Turning gear'da qancha ushlash**
• Suv manbasi aniqlanib yopilgunicha
• Val ekssentrisiteti normal bo'lgunicha
• Yuqori va pastki korpus orasida sezilarli harorat farqi qolmagunicha
• Doimiy egilish bo'lmasa ekssentrisitet **2–6 soatda** normaga qaytadi
• **Korpus "dombaygan" bo'lsa — ancha ko'proq vaqt kerak**
• Suv aniqlash termoparalari yo'q bo'lsa: korpus dastlab **260°C**dan issiq bo'lgan holatda suv kirgan bo'lsa — ishga tushirishdan oldin **24 soat turning gear** tavsiya etiladi

**Yakuniy tartib**
1. Birinchi belgidayoq harakat qiling
2. Nominal tezlikda bo'lsangiz — jiddiy holat majbur qilmasa, ishlashda davom eting
3. Nominaldan past tezlikda bo'lsangiz — **darhol to'xtating**
4. Har qanday holatda — **suv manbasini yoping va drenajni oching**
5. Turning gear'ga qo'yilgach, quyidagilarsiz **hech qachon qayta ishga tushirmang**: ekssentrisitet normal + suv manbasi aniqlanib yopilgan va takrorlanmasligiga ishonch bor
6. ⚠️ **Turning gear dvigateli rotorni aylantira olmasa — har soatda bir marta qayta urinib ko'ring. Kran yordamida yoki turbinaga bug' berib qotib qolgan rotorni ozod qilishga URINMANG.**

---

**🇷🇺 Вода попала в турбину — действия оператора**

В руководстве прямо сказано: **самые тяжёлые повреждения обычно наносятся заметно позже первого признака и являются прямым следствием действий или бездействия оператора.**

Три фактора, на которые влияет оператор: **количество воды, расход пара, обороты.**

**1. Количество воды**
При первом же признаке — перекрыть источник и дренировать турбину и паропроводы.

**2. Расход пара**
Под нагрузкой поток пара **равномерно распределяет воду и уменьшает коробление**. При сохранении расхода корпус **быстрее выпрямляется** после удаления воды.
Поэтому: **если вода попала под нагрузкой — продолжать работу**, если только высокая вибрация, большое ОРС или иное серьёзное состояние не требуют останова. Источник воды перекрыть немедленно.

**3. Обороты**
• **Медленное вращение на ВПУ — наилучший вариант**: тепла от задевания не хватит для остаточного изгиба
• **Если вода попала при разгоне ниже номинала — отключить и поставить на ВПУ**
• **В зоне критических и ниже задевание особенно разрушительно** — ротор изгибается в сторону усиления задевания
• ⚠️ **Попытка «выправить» изогнутый ротор длительной работой на нескольких сотнях об/мин — заблуждение. Так наносили тяжёлые повреждения.**
• Существенно **выше критической** ротор изгибается в сторону **ослабления** задевания — ещё одна причина не сбрасывать обороты

**Сколько держать на ВПУ**
• Пока источник не найден и не перекрыт
• Пока эксцентриситет не придёт в норму
• Пока не исчезнет заметная разница верх/низ корпуса
• Без остаточного изгиба эксцентриситет возвращается за **2–6 часов**
• **Покоробленный корпус выпрямляется значительно дольше**
• Без термопар обнаружения воды: если корпус изначально был выше **260°C** — рекомендуется **24 часа на ВПУ** до пуска

**Итоговый порядок**
1. Действовать при первом признаке
2. На номинале — продолжать работу, если нет серьёзных условий для останова
3. Ниже номинала — **немедленный останов**
4. В любом случае — **перекрыть источник и дренировать**
5. После постановки на ВПУ **не пускать**, пока: эксцентриситет в норме + источник найден, перекрыт и повтор исключён
6. ⚠️ **Если ВПУ не проворачивает ротор — повторять попытки раз в час. НЕ пытаться освободить заклиненный ротор краном или подачей пара.**

---

**🇬🇧 Water Has Entered — operator action**

The manual states it plainly: **the most serious damage is often done a considerable time after the first indication, and is a direct result of the action, or inaction, taken.**

Three factors the operator influences: **quantity of water, steam flow, speed.**

**1. Quantity of water**
Shut off the source and drain the water out of the turbine and steam lines immediately on the first indication.

**2. Steam flow**
Under load, steam flow helps by **uniformly distributing the water and minimizing distortion**. The casing also **restraightens more quickly** with steam flow maintained.
Therefore: **a turbine carrying load when water enters should be kept running** unless high vibration, high differential expansion or another serious condition requires shutdown. Shut the water source off immediately.

**3. Speed**
• **Slow rotation on turning gear is best** — rubbing heat is not enough to cause permanent bowing
• **If accelerating below rated speed when water enters, trip and place on turning gear**
• **Rubbing at and below critical speed range is very destructive** — the rotor bows in a direction that increases rub intensity
• ⚠️ **Sustained operation at several hundred rpm in the belief a bowed rotor straightens faster there has caused serious damage.**
• Well **above** critical speed the rotor bows in a direction that **reduces** rub intensity — another reason to keep running rather than coast down through the critical range

**How long on turning gear**
• Until the water source is identified and shut off
• Until shaft eccentricity is normal
• Until there is no significant upper-to-lower shell temperature difference
• Without permanent bowing, eccentricity returns to normal in **2 to 6 hours**
• **A humped shell may take much longer**
• Without water detection thermocouples: if the casing was initially above **260°C**, **24 hours on turning gear** is recommended before start-up

**Summary**
1. Act at the first indication
2. At rated speed, keep running unless serious conditions force shutdown
3. Below rated speed, shut down immediately
4. In any case, shut off the source and drain immediately
5. Once on turning gear, never restart until eccentricity is normal and the source is identified, shut off, with assurance it will not repeat
6. ⚠️ **If the turning gear motor cannot turn the rotor, retry once per hour. Do NOT free a locked rotor with a crane or by admitting steam.**

`#waterinduction #turninggear #rotorbow`

---
---

## POST 26 — Rotor prewarming

**🇺🇿 HP rotorni oldindan qizdirish**

**Qachon kerak**
Sovuq ishga tushirishda **HP rotor bore harorati <150°C** bo'lsa.
Qizdirish **>155°C** bo'lguncha davom etadi (joyida sozlash talab qilinadi).
Bu **minimal** maqsad. Yuqoriroq qizdirish ishga tushirish vaqtini qisqartiradi va rotor hamda korpus resurs sarfini kamaytiradi, chunki o'tkinchi jarayonlar yumshoqroq bo'ladi.

**Shartlar**
• Turbina **turning gear**da
• Val bug' zichlashlari berilgan va kondensator **vakuumi yaratilgan** bo'lishi bilan bosim berish boshlanadi
• **Barcha drenaj klapanlari ochiq**, **HPEV yopiq** ekanini tekshiring

**Usullar (afzallik tartibida)**
1. **HSPV** orqali — tavsiya etiladi, chunki asosiy bug' generatoridan bug' talab qilmaydi va ishga tushirish vaqtini qisqartiradi
2. **RFV** orqali

Ikkala klapanda ham qizdirish tezligini nazorat qilish uchun **bosim cheklovi** bor. Qizdiruvchi bug' HP bo'limining **exhaust bowl**iga beriladi.

**Jarayon**
HP bo'lim harorati bosimga mos **to'yinish haroratigacha** ko'tariladi — asosan **kondensatsiya issiqlik almashinuvi** hisobiga. Bug' HP bo'limida suvga aylanadi, kondensat **HP korpus drenaj klapanlari** orqali chiqariladi.

**Avtomatik to'xtatish**
Agar turning gear uzilib, tezlik **200 rpm yoki undan yuqori** bo'lsa — boshqaruv tizimi prewarming klapanini **avtomatik yopadi** va jarayon to'xtaydi. Klapan pozitsiyasi oxirgi qiymatning **80–90%**iga qaytariladi (HP bo'limdagi bosimni tushirish uchun) va prewarming qaytadan boshlanadi.

**IP tomoni**
• Ishga tushirish ruxsat shartlaridan biri — **IP rotor metall harorati >55°C**
• IP yuqoridagidek bosim berib qizdirilmaydi. U **kondensator to'yinish haroratigacha kondensatsiya** va **seal bug' haroratidan issiqlik o'tkazish** hisobiga qiziydi
• ⚠️ **IP rotorining 55°C ga chiqishi HP rotorining 155°C ga chiqishidan uzoqroq davom etishi mumkin** — ya'ni ishga tushirishni HP emas, IP kechiktirishi mumkin

⚠️ Boshqaruv klapanining sizmasligi tasdiqlanmagunicha — prewarming davomida turbinani **turning gear**da ushlab turish tavsiya etiladi.

---

**🇷🇺 Предварительный прогрев ротора ЦВД**

**Когда нужен**
При холодном пуске, если **температура расточки ротора ЦВД <150°C**.
Прогрев ведут до **>155°C** (требуется настройка на месте). Это **минимум**; более высокий прогрев сокращает время пуска и расход ресурса за счёт более плавных переходных режимов.

**Условия**
• Турбина на **ВПУ**
• Подача давления начинается после подачи уплотняющего пара и **набора вакуума**
• **Все дренажи открыты**, **HPEV закрыт**

**Способы (по приоритету)**
1. Через **HSPV** — рекомендуется: не требует пара от основного парогенератора, сокращает время пуска
2. Через **RFV**

Оба клапана имеют **ограничение по давлению** для контроля скорости прогрева. Греющий пар подаётся в **выхлопную камеру** ЦВД.

**Процесс**
Температура ЦВД растёт до **температуры насыщения** при данном давлении — в основном за счёт **конденсационного теплообмена**. Пар конденсируется, конденсат отводится через **дренажи корпуса ЦВД**.

**Автоматическое прекращение**
Если ВПУ расцеплено и обороты достигли **200 об/мин и выше** — система управления **автоматически закрывает** клапан прогрева. Положение клапана сбрасывается до **80–90%** от последнего, чтобы снизить давление в ЦВД, и прогрев возобновляется.

**Сторона ЦСД**
• Одно из разрешающих условий пуска — **температура металла ротора ЦСД >55°C**
• ЦСД так не наддувается: греется **конденсацией до температуры насыщения в конденсаторе** и **теплопроводностью от уплотняющего пара**
• ⚠️ **Выход ЦСД на 55°C может занять больше времени, чем выход ЦВД на 155°C** — пуск задержит именно ЦСД

⚠️ Пока не подтверждена плотность регулирующего клапана — держать турбину на **ВПУ** во время прогрева.

---

**🇬🇧 HP Rotor Prewarming**

**When required**
On cold start-up when **HP rotor bore temperature is below 150°C**.
Prewarming continues until above **155°C** (site tuning required). This is the **minimum** target — warming higher shortens start-up time and reduces rotor and shell life expenditure because transients are more gradual.

**Conditions**
• Turbine on **turning gear**
• Pressurizing can begin as soon as shaft steam seals are applied and condenser **vacuum is established**
• Confirm **all drain valves open** and **HPEV closed**

**Methods (in order of preference)**
1. Using **HSPV** — recommended: does not require steam from the main steam generator and reduces unit start-up time
2. Using **RFV**

Both valves have **pressurization limitation** to control the warming rate. Warming steam is admitted into the **exhaust bowl** of the HP section.

**Process**
HP section temperature rises to the **saturation temperature** corresponding to the pressurizing pressure, primarily by **condensing heat transfer**. Steam condenses into water in the HP section; the condensate is removed through the **HP casing drain valves**.

**Automatic stop**
If turning gear is disengaged and speed reaches **200 rpm or higher**, the turbine control system **automatically closes** the prewarming valve and the process stops. Valve position is reset to **80–90%** of the latest position to reduce HP section pressure, and prewarming restarts.

**IP side**
• A start-up permissive is **IP rotor metal temperature above 55°C**
• The IP cannot be pressurized this way — it warms by **condensation up to condenser saturation temperature** and **conduction from the steam seal**
• ⚠️ **The time for the IP rotor to reach 55°C may exceed the time to prewarm the HP rotor to 155°C** — the IP, not the HP, may be what holds up the start

⚠️ Until control valve tightness is verified, keep the turbine on **turning gear** during prewarming.

`#prewarming #coldstart #HSPV #RFV`

---
---

## POST 27 — Drenaj klapanlari mantiqi

**🇺🇿 Drenaj klapanlari — A va B guruhlari**

Drenajlar bug' liniyasining past nuqtalarida, boshqaruv klapan kamerasida va turbina korpusida joylashgan. Har bir bug' liniyasi umumiy drenaj kollektoriga ulanishi mumkin, u esa masofadan boshqariladigan klapan orqali kondensatorga yo'naltiriladi.

**Barcha drenajlar ochiq bo'lishi kerak:** ishga tushirishda, to'xtatishda va **yuklamasiz ish davrida** — hattoki turbina yuqori yuklamadan shu holatga kelgan bo'lsa ham.

**Table 7-1-4 — drenaj klapanlari ishlash tamoyili**
| Guruh | ST tezlanish | RFM → FFM | Yuklama 15% | ST Trip |
|---|---|---|---|---|
| **A** | Ochiq | **Yopiq** | Yopiq | Ochiq |
| **B** | Ochiq | **Ochiq** | Yopiq | Ochiq |

**Guruh A**
• HP dynamic strainer a drenaj klapani
• HPCV kamerasini qizdirish drenaj klapani
• HPSV liniyasini qizdirish drenaj klapani
• IP dynamic strainer a drenaj klapani

**Guruh B**
a) HP turbina 1-bosqich drenaj klapani
b) HP kirish soplo adapteri drenaj klapani
c) HP tashqi korpus drenaj klapani
d) IP soplo adapteri drenaj klapani
e) IP TBN kirish B drenaj klapani
f) IP TBN kirish D drenaj klapani
g) LPSV seat orqasidagi drenaj klapani
h) LPCV chiqishidagi drenaj klapani
i) N1 packing 2-leak off drenaj liniyasi klapani
j) LP A TBN korpus drenaj klapani
k) LP B TBN korpus drenaj klapani

⚠️ **A va B guruhi faqat bitta holatda farq qiladi — RFM'dan FFM'ga o'tishda.** A yopiladi, B ochiq qoladi. Boshqa barcha rejimlarda ular bir xil ishlaydi. Shu bitta farq esa reverse flow rejimidan chiqishda HP tomonini himoya qiladi.

⚠️ Drenajlar ochiq turganda operator **turbina ichiga qaytib kirishning oldini olishga** e'tibor berishi kerak.

---

**🇷🇺 Дренажные клапаны — группы A и B**

Дренажи расположены в нижних точках паропроводов, в коробке регулирующих клапанов и на корпусе турбины. Паропроводы могут быть заведены на общий дренажный коллектор с дистанционно управляемым клапаном на конденсатор.

**Все дренажи должны быть открыты:** при пуске, останове и **на холостом ходу** — даже если турбина пришла в это состояние с высокой нагрузки.

**Table 7-1-4 — принцип работы дренажей**
| Группа | Разворот ПТ | RFM → FFM | Нагрузка 15% | Отключение ПТ |
|---|---|---|---|---|
| **A** | Открыт | **Закрыт** | Закрыт | Открыт |
| **B** | Открыт | **Открыт** | Закрыт | Открыт |

**Группа A**
Дренаж сетчатого фильтра ЦВД | Дренаж прогрева коробки РК ВД | Дренаж прогрева линии ГСК ВД | Дренаж сетчатого фильтра ЦСД

**Группа B**
a) Дренаж 1-й ступени ЦВД | b) Дренаж адаптера сопла на входе ЦВД | c) Дренаж наружного корпуса ЦВД | d) Дренаж адаптера сопла ЦСД | e) Дренаж входа B ЦСД | f) Дренаж входа D ЦСД | g) Дренаж за седлом ГСК НД | h) Дренаж за РК НД | i) Дренаж линии 2-го отсоса уплотнения N1 | j) Дренаж корпуса ЦНД-A | k) Дренаж корпуса ЦНД-B

⚠️ **Группы отличаются ровно в одном режиме — при переходе RFM → FFM.** A закрывается, B остаётся открытой. Во всех остальных режимах логика одинакова. Именно это отличие защищает ЦВД при выходе из режима обратного потока.

⚠️ При открытых дренажах оператор должен следить, **чтобы не было заброса обратно в турбину**.

---

**🇬🇧 Drain Valves — Groups A and B**

Drains are at low points of the steam line, the control valve chest and the turbine shell. Each steam line may be piped to a common drain manifold routed to the condenser through a power-operated manifold drain valve arranged for remote operation.

**All drain valves should be open** during start-up, shutdown and **periods of no-load operation** — even if the turbine reached that condition from high load.

**Table 7-1-4 — drain valve operating principle**
| Group | ST speed-up | RFM → FFM | Load 15% | ST Trip |
|---|---|---|---|---|
| **A** | Open | **Close** | Close | Open |
| **B** | Open | **Open** | Close | Open |

**Group A**
HP dynamic strainer a drain | HPCV chamber warming drain | HPSV line warming drain | IP dynamic strainer a drain

**Group B**
a) HP turbine 1st stage drain | b) HP inlet nozzle adaptor drain | c) HP outer casing drain | d) IP nozzle adaptor drain | e) IP TBN inlet B drain | f) IP TBN inlet D drain | g) LPSV after seat drain | h) LPCV downstream drain | i) N1 packing 2nd leak-off drain | j) LP A TBN casing drain | k) LP B TBN casing drain

⚠️ **The groups differ in exactly one mode — the RFM to FFM transfer.** A closes, B stays open. Everywhere else the logic is identical. That single difference is what protects the HP section coming out of reverse flow.

⚠️ While drains are open, watch to **prevent backing up into the turbine**.

`#drains #RFM #FFM`

---
---

## POST 28 — Seal steam va self-sealing

**🇺🇿 Zichlash bug'i — ishga tushirishdan self-sealing'gacha**

**Vazifasi**
• Kondensator vakuumini yaratish
• Turbina uchki packinglarini zichlash: **havo atmosferadan past bo'limga kirmasin**, va **HP bo'limdagi ortiqcha bug' mashina zaliga yoki podshipnik korpuslariga chiqib yog'ni ifloslantirmasin**

**Ishga tushirish va past yuklama**
• Manba — **yordamchi bug'**
• Kollektor bosimi **SSAFV** orqali boshqariladi
• Bug' oraliq packing halqalari orasiga beriladi, tashqi halqalar orasidan **gland exhauster**ga chiqariladi, issiqlik almashgichning birlamchi tomonidagi sovuq oziqlantiruvchi suv bilan kondensatsiyalanadi

**Self-sealing'ga o'tish**
Yuklama oshgani sayin HP va reheat bo'limlarining uchki packinglaridan chiqayotgan bug' oqimi **LP uchki packinglari uchun 100% yetarli** bo'ladigan nuqtaga yetadi. Shu yuklamadan yuqorida turbina **"self-sealed"** deyiladi.

**N1 va N3 packing**dan sizayotgan bug' ikkala LP uchki packing talabidan oshsa:
• **SSAFV yopiladi**
• Ortiqcha bug' **SPUV** orqali **GSC**ga chiqariladi

**Self-sealed rejimida**
Steam seal regulyatori kollektor bosimini **doimiy 0.28 bar.g** da ushlab turadi — SSAFV orqali bug' qo'shib yoki SPUV orqali chiqarib.

**Gland exhauster**
Ikki tashqi packing halqasi orasida **atmosferadan past bosim** yaratadi. Tashqi leak-off kamerasida yengil vakuum saqlanadi: **havo oxirgi packing halqasi orqali ichkariga so'riladi**, bug' esa qarama-qarshi tomondan shu kameraga kiradi. Bug'-havo aralashmasi **GSC**ga boriladi, u yerda bug' kondensatsiyalanadi, havo **markazdan qochma yuritgich** bilan chiqariladi.

⚠️ Uch xil raqam: **1.29 bar.a** (Table 1-1-1 nominal), **0.28 bar.g** (3.7 — TCS doimiy ushlab turadigan qiymat), **32 kPa** (5.7.3 — ishga tushirishda dastlabki rostlash). Aniq qiymat **ishga tushirish muhandisi tomonidan vent kameralaridagi o'lchangan bosimlarga qarab belgilanadi** — LP glandlarni barcha rejimlarda yetarli bo'g'ish va val bo'ylab bug' chiqishini oldini olish uchun.

⚠️ **Steam seal kollektor harorati (10MAW11CT001A/001B) steam seal yoqilgan har qanday vaqtda 149°C dan yuqori bo'lishi SHART** — turbinaga suv/ho'l bug' kirishining oldini olish uchun.

⚠️ Harorat diapazoni ichida qayerga qo'yish kerak: **sovuq start — pastga** (uzun rotor differensial kengayishi va rotor charchash resursini boshqarish uchun), **iliq start — o'rtaga**, **issiq start — yuqoriga** (qisqa rotor differensial kengayishi, charchash resursi va radial zazor nazorati uchun).

---

**🇷🇺 Уплотняющий пар — от пуска до самоуплотнения**

**Назначение**
• Набор вакуума в конденсаторе
• Уплотнение концевых уплотнений: **воздух не подсасывается** в вакуумную часть, **избыточный пар ЦВД не выбивается** в машзал и в корпуса подшипников (обводнение масла)

**Пуск и малые нагрузки**
• Источник — **вспомогательный пар**
• Давление коллектора регулируется через **SSAFV**
• Пар подаётся между промежуточными кольцами уплотнений, отсасывается между наружными кольцами в **эксгаустер уплотнений** и конденсируется холодной питательной водой в первичном контуре теплообменника

**Переход на самоуплотнение**
С ростом нагрузки протечка через концевые уплотнения ЦВД и ЦСД достигает уровня, покрывающего **100% потребности концевых уплотнений ЦНД**. Выше этой нагрузки турбина **самоуплотняется**.

Когда протечка через уплотнения **N1 и N3** превышает потребность обоих концевых уплотнений ЦНД:
• **SSAFV закрывается**
• Избыток сбрасывается через **SPUV** в **СП (GSC)**

**В режиме самоуплотнения**
Регулятор поддерживает давление коллектора **постоянно 0.28 бар.g**, подавая через SSAFV или сбрасывая через SPUV.

**Эксгаустер уплотнений**
Создаёт **разрежение** между двумя наружными кольцами. **Воздух подсасывается через последнее кольцо**, пар входит в ту же камеру с противоположной стороны. Смесь идёт в **СП**, пар конденсируется, воздух удаляется **центробежной воздуходувкой**.

⚠️ Три разных числа: **1.29 бар.а** (номинал Table 1-1-1), **0.28 бар.g** (п. 3.7 — постоянное значение TCS), **32 кПа** (п. 5.7.3 — начальная регулировка при пуске). Точное значение **определяет пусконаладчик по давлениям в вентиляционных камерах**.

⚠️ **Температура коллектора (10MAW11CT001A/001B) при поданном уплотняющем паре ОБЯЗАНА быть выше 149°C** — против заброса воды и влажного пара.

⚠️ Где держать в диапазоне: **холодный пуск — ниже**, **тёплый — середина**, **горячий — выше** (управление ОРС, усталостным ресурсом и радиальными зазорами).

---

**🇬🇧 Seal Steam — from start-up to self-sealing**

**Purpose**
• Establish condenser vacuum
• Seal the end packings so **air does not leak into the sub-atmospheric section**, and **excess HP section steam does not blow into the turbine room or bearing housings** contaminating the lube oil

**Start-up and low load**
• Source is **auxiliary steam**
• Header pressure controlled by **SSAFV**
• Steam is introduced between intermediate packing rings, vented between outer rings to a **gland exhauster**, and condensed by cold feed water through the primary side of a heat exchanger

**Transition to self-sealing**
As load increases, leakage from the HP and reheat end packings reaches the point where it provides **100% of the sealing steam for the LP end packings**. Above that load the turbine is **"self-sealed"**.

When leakage from the **N1 and N3 packings** exceeds the requirement of both LP end packings:
• **SSAFV closes**
• Surplus steam is discharged to **GSC** through **SPUV**

**During self-sealed operation**
A steam seal regulator holds the manifold at a constant **0.28 bar.g**, admitting through SSAFV or dumping through SPUV.

**Gland exhauster**
Establishes **sub-atmospheric pressure** between the two outer packing rings. **Air is drawn in through the last packing ring**; steam enters the same cell from the opposite direction. The mixture is piped to **GSC** where steam condenses and air is evacuated by a **centrifugal blower**.

⚠️ Three different figures: **1.29 bar.a** (Table 1-1-1 nominal), **0.28 bar.g** (section 3.7 — the constant TCS maintains), **32 kPa** (section 5.7.3 — initial regulation at start-up). The precise value is **determined by the testing engineer at commissioning according to pressures measured in the vent spaces**, to ensure sufficient choking of the LP glands in all operating modes and prevent steam escaping along the shaft.

⚠️ **Steam seal header temperature (10MAW11CT001A/001B) must be above 149°C at all times when steam seals are on** — to prevent water/wet steam induction into the turbine.

⚠️ Where to sit in the band: **cold starts low** (to manage long rotor differential expansion and rotor fatigue life), **warm starts middle**, **hot starts high** (short rotor differential expansion, fatigue life, radial clearance control).

`#glandsteam #selfsealed #SSAFV #SPUV`

---
---

## POST 29 — LP exhaust spray

**🇺🇿 LP exhaust purkash — klapan mantiqi**

**Nima uchun kerak**
Ishga tushirish, to'xtatish va past yuklama rejimlarida turbina bug'dan **kam energiya oladi** — natijada **LP korpus harorati g'ayrioddiy yuqori** darajaga chiqadi. Bu oxirgi bosqich kuraklari, ichki korpus va LP tashqi korpusining mexanik xususiyatlariga ta'sir qiladi.

**Purkash tizimi**
Soplolar oxirgi bosqich kuraklaridan **bevosita keyin** o'rnatilgan. Suv **kondensat tizimidan** olinadi, olish nuqtasi **deminerallashtirgichlardan keyin** bo'lishi shart.

**Klapan mantiqi — haroratga proporsional**
| Exhaust hood harorati | Klapan holati |
|---|---|
| **<60°C** | To'liq yopiq |
| **60°C** | Ocha boshlaydi |
| **60...80°C** | Haroratga proporsional ochiladi |
| **80°C** | **To'liq ochiq** |
| **90°C** | Boshqaruv tizimi operatorga **ogohlantirish** beradi |
| **105°C** | Boshqaruv tizimi **TRIP** beradi |

Harorat 60°C dan oshsa, LP tashqi korpusidagi harorat o'sishi boshqaruv klapan diafragmasiga **rostlangan havo bosimini** beradi. Diafragmadagi bosim ortishi klapanni asta ochib, kondensatni **tuman purkash soplolariga** yuboradi. Harorat tushganda transmitter klapani yopila boshlaydi va havo bosimini kamaytiradi.

⚠️ **105°C — bu Table 8-1-1'dagi LP exhaust trip setpointi bilan bir xil.** Ya'ni spray to'liq ochiq (80°C) bo'lgandan trip'gacha atigi **25°C** bor. Agar spray to'liq ochiq bo'lsa-yu harorat ko'tarilishda davom etsa — bu spray yetishmayotganini emas, **vakuum yo'qolayotganini** anglatadi.

⚠️ Suv **deminerallashtirgichdan keyin** olinishi shart — aks holda LP korpusga tuz olib kirasiz.

---

**🇷🇺 Впрыск в выхлоп ЦНД — логика клапана**

**Зачем**
При пусках, остановах и малых нагрузках турбина **отбирает мало энергии** — температура корпуса ЦНД поднимается **необычно высоко**, что влияет на механические свойства лопаток последней ступени, внутреннего и наружного корпуса.

**Система впрыска**
Форсунки установлены **сразу за лопатками последней ступени**. Вода берётся из **конденсатной системы**, отбор обязательно **после обессоливающей установки**.

**Логика клапана — пропорционально температуре**
| Температура выхлопного патрубка | Положение клапана |
|---|---|
| **<60°C** | Полностью закрыт |
| **60°C** | Начинает открываться |
| **60...80°C** | Пропорционально температуре |
| **80°C** | **Полностью открыт** |
| **90°C** | **Сигнал** оператору |
| **105°C** | **ОТКЛЮЧЕНИЕ** |

Выше 60°C рост температуры наружного корпуса подаёт **регулируемое давление воздуха** на мембрану клапана. Рост давления постепенно открывает клапан и подаёт конденсат на **туманообразующие форсунки**. При снижении температуры давление воздуха уменьшается, клапан закрывается.

⚠️ **105°C совпадает с уставкой защиты по выхлопу ЦНД из Table 8-1-1.** От полностью открытого впрыска (80°C) до защиты всего **25°C**. Если впрыск открыт полностью, а температура продолжает расти — дело не во впрыске, а в **потере вакуума**.

⚠️ Отбор воды строго **после обессоливания** — иначе соли пойдут в корпус ЦНД.

---

**🇬🇧 LP Exhaust Spray — valve logic**

**Why**
During starting, shutdowns and low load operation the turbine **removes little energy** from the steam, so **LP casing temperature reaches an exceptionally high level**, affecting the mechanical characteristics of the last stage buckets, inner casing and LP outer casing.

**Spray system**
Nozzles are installed **just downstream of the last stage buckets**. Water comes from the **condensate system**, taken **downstream of any demineralizers**.

**Valve logic — proportional to temperature**
| Exhaust hood temperature | Valve position |
|---|---|
| **Below 60°C** | Fully closed |
| **60°C** | Begins to open |
| **60 to 80°C** | Opens in proportion to temperature |
| **80°C** | **Fully open** |
| **90°C** | Control system **alerts the operator** |
| **105°C** | Control system **initiates TRIP** |

Above 60°C, rising LP outer casing temperature admits **regulated air pressure** to the control valve diaphragm. Increased diaphragm pressure gradually opens the valve, admitting condensate to the fog spray nozzles. As temperature falls, the transmitter valve reduces air pressure and closes the flow.

⚠️ **105°C matches the LP exhaust trip setpoint in Table 8-1-1.** From fully open spray (80°C) to trip is only **25°C**. If the spray is fully open and temperature is still climbing, the problem is not the spray — it's **vacuum being lost**.

⚠️ Water must be taken **downstream of demineralizers** — otherwise you spray salts into the LP casing.

`#LPspray #exhausthood #desuperheat`

---
---

## POST 30 — Turning gear va rotor ekssentrisiteti

**🇺🇿 Turning gear — vaqt va ekssentrisitet qoidalari**

**Nima uchun**
• To'xtash paytida **termik deformatsiya yoki rotorning o'z og'irligi** sabab vaqtinchalik egilishning oldini olish
• Rotorda **aylana bo'ylab bir tekis harorat** holatini olish
Vaqtinchalik egilish rotor yuzasi bilan zichlash tishi orasidagi zazorga va dinamik muvozanatsizlikka ta'sir qiladi.

**Ketma-ketlik**
Turning gear **seal bug' berishdan va bosimli rotor qizdirishdan OLDIN** ishga tushirilishi shart. Turning gear ishlayotganda **jacking oil va lube oil tizimlari ishlashi shart**.

**Vaqt qoidalari**
• Dastlabki ishga tushirishda: normal ekssentrisitet aniqlangunicha **8 soat yoki ko'proq**
• Turning gear vaqti = **to'xtash vaqtining 10 barobari**
• Maksimal vaqt qayta ishga tushirishdan oldin **4 soat**
• Qisqa to'xtashlarda, qayta ishga tushirish kutilsa — **uzluksiz turning gear** tavsiya etiladi

**Eng past rotor metall harorati 260°C dan yuqori bo'lganda**
• Turning gear to'xtatilsa, to'xtash vaqti **10 daqiqadan** oshmasligi tavsiya etiladi — **qotib qolgan rotor** holatidan qochish uchun
• Iloji bo'lmasa — **podshipnik metall harorati 150°C dan oshmasligi** uchun lube oil tizimi ishlashi shart
• Tajribaga ko'ra rotor metall harorati **260°C dan past** bo'lganda turning gear ishlamasa ham bu qizib ketish yuz bermaydi

**Uzoq to'xtash (haftalar, oylar)**
Uzluksiz turning gear shart emas. Aylanuvchi qismlarning keraksiz yeyilishini kamaytirish va **rotor journali hamda podshipnik padlarining himoya yuzasini saqlash** uchun:
• **Haftasiga kamida yarim soat** jacking oil va lube oil tizimlarini ishlating
• Shu davrda turbogeneratorni **taxminan 5 daqiqa** turning gear'da aylantiring

**Ekssentrisitet**
• Turning gear'da val ekssentrisitet ko'rsatkichi **rotor egilish darajasini** ko'rsatadi
• Normal qiymat dastlabki turning gear ishida **8 soat yoki ko'proq uzluksiz** ishlashdan keyin aniqlanadi
• Qayta ishga tushirishdan oldin ekssentrisitet normal qiymatga yetib, **1 soat davomida** shunday turishi shart
• ⚠️ **Normal qiymatdan PAST ekssentrisitet ham yuqori qiymat kabi nomaqbul** — val normal diapazonga kirgunicha turning gear'da qolishi kerak
• ⚠️ **G'ayritabiiy ekssentrisitet bilan turbinani aylantirish yuqori tebranish va radial ishqalanishga, hamda rotorning doimiy egilishiga olib kelish ehtimoli yuqori**

⚠️ Turning gear biror sababga ko'ra ishlamasa ham — **podshipnik padlarining qizib ketmasligi uchun lube oil ishlashi shart**.

---

**🇷🇺 ВПУ и эксцентриситет ротора**

**Зачем**
• Предотвратить **временный изгиб** от термической деформации или собственного веса при останове
• Обеспечить **равномерную по окружности температуру** ротора
Временный изгиб влияет на зазор ротор–гребень уплотнения и на динамический небаланс.

**Последовательность**
ВПУ включают **ДО подачи уплотняющего пара и до наддува для прогрева ротора**. При работе ВПУ **обязательно работают гидроподъём и маслосистема**.

**Правила по времени**
• При первичном пуске — **8 часов и более**, пока не определён нормальный эксцентриситет
• Время ВПУ = **10-кратное время простоя**
• Максимум перед повторным пуском — **4 часа**
• При коротких простоях с ожидаемым пуском — **непрерывная работа ВПУ**

**Если минимальная температура металла ротора выше 260°C**
• Перерыв в работе ВПУ **не более 10 минут** — иначе риск **заклинивания ротора**
• Если невозможно — маслосистема должна работать, чтобы **температура баббита не превысила 150°C**
• По опыту, при температуре металла **ниже 260°C** такой перегрев не возникает

**Длительный простой (недели, месяцы)**
Непрерывная работа ВПУ не нужна. Для снижения износа и **сохранения защитной поверхности шеек и вкладышей**:
• **Не менее получаса в неделю** работа гидроподъёма и маслосистемы
• В это же время **около 5 минут** проворот на ВПУ

**Эксцентриситет**
• На ВПУ показание эксцентриситета отражает **степень изгиба ротора**
• Нормальное значение определяют при первичной работе ВПУ после **8 и более часов непрерывно**
• Перед пуском эксцентриситет должен прийти в норму и держаться **в течение часа**
• ⚠️ **Значение НИЖЕ нормы так же нежелательно, как и выше** — держать на ВПУ до входа в нормальный диапазон
• ⚠️ **Разворот с ненормальным эксцентриситетом с высокой вероятностью даст сильную вибрацию, радиальные задевания и остаточный изгиб ротора**

⚠️ Даже если ВПУ по какой-то причине не в работе — **маслосистема должна работать**, чтобы не перегреть вкладыши.

---

**🇬🇧 Turning Gear and Rotor Eccentricity**

**Purpose**
• Prevent **temporary rotor bow** from thermal distortion or rotor gravity when shut down
• Obtain a **circumferentially uniform temperature** in the rotor
Temporary bow affects seal clearance between rotor surface and seal tooth, and dynamic mass unbalance.

**Sequence**
Turning gear must be running **BEFORE steam seal is admitted and before pressurized rotor warming**. Jacking oil and lube oil systems **must be in operation** while turning gear runs.

**Time rules**
• Initial turbine start-up: **8 hours or more** until normal eccentricity is determined
• Turning gear time = **10 times the outage time**
• Maximum is **four hours** before restarting
• For short outages where restart is expected, **continuous turning gear** is recommended

**When lowest rotor metal temperature exceeds 260°C**
• If turning gear is discontinued, stopping time should be **no longer than 10 minutes** — to avoid a **locked rotor** condition
• If not possible, the lube oil system must be in service to keep **bearing metal below 150°C**
• In experience this overheating does not occur with rotor metal **below 260°C**

**Extended outages (weeks or months)**
Continuous turning gear is not needed. To minimize unnecessary wear and **maintain protective surfaces on rotor journals and bearing pads**:
• Run jacking oil and lube oil **at least half an hour per week**
• Put the turbine-generator on turning gear for **about five minutes** during that oil run

**Eccentricity**
• On turning gear, the shaft eccentricity indicator shows **the degree of rotor bowing**
• The normal value is determined at initial turning gear operation after **8 hours or more continuous run**
• Before restarting, eccentricity must reach normal and **hold for one hour**
• ⚠️ **A value BELOW normal is just as undesirable as above** — stay on turning gear until it is within range
• ⚠️ **Rolling with abnormal eccentricity will very likely cause excessive vibration and radial rub damage, with the possibility of permanently bowing the rotor**

⚠️ Even if turning gear is out of service for any reason, **lube oil must be in service** to prevent overheating of bearing pads.

`#turninggear #eccentricity #rotorbow`

---
---

## POST 31 — Vakuumni buzish va overspeed test

**🇺🇿 Vakuum buzish va overspeed test — chegaralar**

**Vakuum buzish (7.1.11)**
Nominal tezlikda, tarmoqdan ajratilgandan keyin vakuum buzish klapanlarini ochish **to'satdan tormozlanish** hisobiga **LSB (oxirgi bosqich kuraklari) shikastlanishiga** olib keladi.

⚠️ **Vakuum turbina tezligi 2000 rpm dan pastga tushmaguncha buzilmasligi tavsiya etiladi** — yuqori tebranish kabi avariya holati birlikni imkon qadar tez to'xtatishni talab qilmasa.

**Overspeed test (7.1.12)**
Sovuq ishga tushirishda overspeed test uchun tavsiya etiladi:
• **HP/IP 1-rotor bore harorati >121°C**, **YOKI**
• Turbina **25% dan yuqori yuklamada taxminan 3 soat** ishlagan bo'lsin

Maqsad — rotorlarning **yetarlicha qizdirilganligini** ta'minlash.

Bu yuklamaga erishib bo'lmasa, ishlab chiqaruvchi mavjud bug' generatori va turbina metall haroratlarini ko'rib chiqib, ko'p hollarda **pastroq yuklama va uzoqroq ushlab turish** kombinatsiyasini taklif qilishi mumkin.

**Bog'liq trip setpointlari (Table 8-1-1)**
• Birlamchi overspeed trip (110%): **>3300 rpm**
• Avariya overspeed trip, TCS'dagi maxsus moduldan (113%): **>3330 rpm**

⚠️ **Agar tezlik 3300 rpm ga chiqsa-yu overspeed himoyasi ishlamasa** — markazdan qochma kuch tufayli rotorning parchalanishining oldini olish uchun **qo'lda trip va vakuum buzish darhol bajarilishi shart** (10.2.2.3).

---

**🇷🇺 Срыв вакуума и испытание на разгон**

**Срыв вакуума (7.1.11)**
Открытие клапанов срыва вакуума на номинальных оборотах после отключения от сети даёт **резкое торможение** и **повреждение лопаток последней ступени**.

⚠️ **Вакуум рекомендуется не срывать, пока обороты не снизятся ниже 2000 об/мин** — кроме аварий (например, высокая вибрация), когда нужен максимально быстрый останов.

**Испытание на разгон (7.1.12)**
При холодном пуске для испытания рекомендуется:
• **Температура расточки 1-х роторов ЦВД/ЦСД >121°C**, **ЛИБО**
• Турбина отработала **около 3 часов при нагрузке выше 25%**

Цель — достаточный прогрев роторов.

Если такая нагрузка недостижима, изготовитель рассматривает текущие температуры металла и обычно предлагает комбинацию **меньшей нагрузки и большей выдержки**.

**Связанные уставки (Table 8-1-1)**
• Первичная защита от разгона (110%): **>3300 об/мин**
• Аварийная от выделенного модуля TCS (113%): **>3330 об/мин**

⚠️ **Если обороты дошли до 3300 об/мин, а защита не сработала** — немедленно ручное отключение и срыв вакуума, чтобы не допустить разрушения ротора центробежными силами (10.2.2.3).

---

**🇬🇧 Vacuum Breaking and Overspeed Test**

**Vacuum breaking (7.1.11)**
Opening the vacuum breaking valves at rated speed after separation from the grid causes **LSB damage due to the sudden braking action**.

⚠️ **Vacuum should not be broken until turbine speed is below 2000 rpm** — unless an emergency such as high vibration requires the fastest possible shutdown.

**Overspeed test (7.1.12)**
For a cold start, before an overspeed test it is recommended that either:
• **HP/IP 1st rotor bore temperatures are above 121°C**, **OR**
• The turbine has operated **above 25% load for about 3 hours**

The purpose is to ensure the rotors are **adequately warmed**.

If that load is not attainable, the manufacturer will review prevailing steam generator and turbine metal temperatures and in most cases offer an alternative combination of **lower load and longer hold time**.

**Related trip settings (Table 8-1-1)**
• Primary overspeed trip (110%): **>3300 rpm**
• Emergency overspeed trip from dedicated TCS module (113%): **>3330 rpm**

⚠️ **If speed rises to 3300 rpm without overspeed protection acting**, manual trip and vacuum breaking must be performed immediately to prevent rotor burst from centrifugal force (10.2.2.3).

`#overspeed #vacuumbreaking #LSB`

---
---

## POST 32 — HP evacuation valve

**🇺🇿 HPEV — ochilish va yopilish mantiqi**

**Nima uchun bor**
Turbinaning **HP exhaust qismidagi harorat kurakni shikastlashi mumkin**. HP exhaust bo'limida harorat quyidagi hollarda ko'tariladi:
• **Reverse Flow rejimida ishlash**
• **Reverse Flow'dan Forward Flow'ga o'tish**
• **Past yuklamada ishlash**

**HPEV OCHILADI, agar quyidagilarning HAMMASI bajarilsa:**
☑ HP exhaust NRV **yopiq** holatda
☑ Rotor prewarming holati **EMAS**
☑ Forward Flow rejimi **EMAS**

**HPEV YOPILADI, agar quyidagilardan BIRORTASI bajarilsa:**
• Forward Flow rejimi holati
• Rotor prewarming holati

⚠️ Ochilish uchun **uchala shart ham** kerak (AND), yopilish uchun **bittasi yetarli** (OR). Ya'ni mantiq **yopilish tomonga og'ishgan** — shubhali holatda klapan yopiladi.

⚠️ **Rotor prewarming davomida HPEV yopiq bo'lishi tekshiriladi** (7.1.6). Prewarming'da qizdiruvchi bug' aynan HP exhaust bowl'ga beriladi — HPEV ochiq bo'lsa bug' chiqib ketadi va qizdirish bo'lmaydi.

⚠️ HP exhaust harorati trip setpointlari (Table 8-1-1): **>450°C 15 daqiqa kechikish bilan**, **>470°C darhol**.

---

**🇷🇺 Клапан эвакуации ЦВД (HPEV) — логика**

**Зачем**
**Температура в выхлопной части ЦВД может повредить лопатку.** Температура растёт при:
• Работе в **режиме обратного потока**
• **Переходе с обратного на прямой поток**
• **Работе на малой нагрузке**

**HPEV ОТКРЫВАЕТСЯ, если выполнены ВСЕ условия:**
☑ Обратный клапан выхлопа ЦВД **закрыт**
☑ **НЕ** режим прогрева ротора
☑ **НЕ** режим прямого потока

**HPEV ЗАКРЫВАЕТСЯ, если выполнено ЛЮБОЕ:**
• Режим прямого потока
• Режим прогрева ротора

⚠️ Для открытия нужны **все три** условия (AND), для закрытия достаточно **одного** (OR). Логика смещена **в сторону закрытия**.

⚠️ **При прогреве ротора проверяется, что HPEV закрыт** (7.1.6). Греющий пар подаётся именно в выхлопную камеру ЦВД — при открытом HPEV прогрева не будет.

⚠️ Уставки защиты по температуре выхлопа ЦВД: **>450°C с выдержкой 15 мин**, **>470°C мгновенно**.

---

**🇬🇧 HP Evacuation Valve — open/close logic**

**Why it exists**
The **temperature of the HP exhaust part can damage the bucket**. HP exhaust temperature may rise under:
• **Reverse Flow Operation**
• **Transferring from Reverse Flow to Forward Flow**
• **Low Load Operation**

**HPEV OPENS when ALL of the following are satisfied:**
☑ HP exhaust NRV **closed** status
☑ **NOT** Rotor Prewarming status
☑ **NOT** Forward Flow Mode status

**HPEV CLOSES when ANY of the following is satisfied:**
• Forward Flow Mode status
• Rotor Prewarming status

⚠️ Opening needs **all three** (AND); closing needs **only one** (OR). The logic is deliberately **biased toward closed**.

⚠️ **During rotor prewarming, HPEV closed is a checked item** (7.1.6). Warming steam is admitted into the HP exhaust bowl — with HPEV open there is no warming.

⚠️ HP exhaust temperature trip settings: **>450°C with 15 min delay**, **>470°C immediate**.

`#HPEV #reverseflow #HPexhaust`

---
---

## POST 33 — Avariya to'xtatish: vakuum buzish bilan

**🇺🇿 Vakuum buzib to'xtatish — 7 qadam**

**1-qadam: Qo'lda trip**
"Emergency shutdown" tugmasini bosing va quyidagilar ishga tushganini tasdiqlang:
☑ HPSV, HPCV, IPSV, IPCV, LPSV, LPCV **yopildi**
☑ HP exhaust **check valve'lar yopildi**
☑ **HP vent klapani ochildi**
☑ Generator va **ikkala HRSG** interlok bilan trip bo'ldi
☑ **GCB ochildi**
☑ HRSG#1 va HRSG#2 **kirish diverter damperlari yopildi** (CC → SC rejimiga o'tish)
☑ HP, IP, LP **bypass klapanlari yopildi**

**2-qadam:** Emergency lube oil nasosni ishga tushiring, muvaffaqiyatli ishga tushganini tasdiqlang.

**3-qadam:** Vakuumni buzing — vacuum breaker klapanini oching, vakuum nasosni to'xtating, rotorning bo'shashishini tezlashtiring.

**4-qadam:** Tezlik **400 rpm**dan pastga tushganda **jacking oil nasoslari avtomatik ishga tushganini** tekshiring — podshipnik yog' plyonkasini saqlash uchun.

⚠️ **Agar yog' sizib yong'in chiqqan bo'lsa — avval emergency lube oil nasosni ishga tushiring, KEYIN asosiy lube oil nasosni to'xtating.**

**5-qadam:** Asosiy parametrlarni kuzating — **bo'shashish vaqti (coastdown time)** va **rotor ekssentrisiteti**ni yozib boring, podshipnik harorati va o'q siljishi o'zgarishlarini diqqat bilan kuzating.

**6-qadam:** Rotor tezligi **0 rpm**ga tushgandan keyin turning gear **avtomatik ishga tushganini** tekshiring.

**7-qadam:** Turning gear tezligi **7 rpm/min** ekanini tasdiqlang.

---

**🇷🇺 Аварийный останов со срывом вакуума — 7 шагов**

**Шаг 1: Ручное отключение**
Нажать «аварийный останов» и подтвердить:
☑ ГСК и РК ВД, СД, НД **закрыты**
☑ **Обратные клапаны выхлопа ЦВД закрыты**
☑ **Клапан сброса ЦВД открыт**
☑ Генератор и **оба КУ** отключены по блокировке
☑ **ГВ отключён**
☑ **Входные шиберы КУ №1 и №2 закрыты** (переход ПГУ → ГТУ)
☑ **БРОУ ВД, СД, НД закрыты**

**Шаг 2:** Пустить аварийный маслонасос, убедиться в успешном пуске.

**Шаг 3:** Сорвать вакуум — открыть клапан срыва, остановить вакуумный насос, ускорить выбег.

**Шаг 4:** Проверить **автоматический пуск насосов гидроподъёма** при снижении оборотов ниже **400 об/мин**.

⚠️ **При утечке масла с возгоранием — сначала пустить аварийный маслонасос, ЗАТЕМ остановить основной.**

**Шаг 5:** Контроль параметров — записать **время выбега** и **эксцентриситет**, следить за температурой подшипников и осевым сдвигом.

**Шаг 6:** После выбега до **0 об/мин** проверить **автоматическое включение ВПУ**.

**Шаг 7:** Убедиться, что частота вращения ВПУ **7 об/мин**.

---

**🇬🇧 Emergency Shutdown With Vacuum Breaking — 7 steps**

**Step 1: Manual trip**
Press the "emergency shutdown" button and confirm the following are triggered:
☑ HPSV, HPCV, IPSV, IPCV, LPSV, LPCV **closed**
☑ HP exhausting **check valves closed**
☑ **HP vent valve opened**
☑ Generator and **both HRSGs** tripped by interlock
☑ **GCB opened**
☑ HRSG#1 and HRSG#2 **inlet diverter dampers closed** (CC to SC transfer)
☑ HP, IP, LP **bypass valves closed**

**Step 2:** Start the emergency lube oil pump; confirm it starts successfully.

**Step 3:** Break the vacuum — open the vacuum breaker valve, stop the vacuum pump, accelerate rotor coast down.

**Step 4:** Check the **jacking oil pumps auto-activate** below **400 rpm** to maintain the bearing oil film.

⚠️ **If lube oil has leaked and caught fire — start the emergency lube oil pump FIRST, then stop the main lube oil pump.**

**Step 5:** Monitor key parameters — record **coastdown time** and **rotor eccentricity**; closely watch bearing temperature and axial displacement.

**Step 6:** After the rotor coasts to **0 rpm**, confirm the turning gear device **operates automatically**.

**Step 7:** Confirm turning gear speed is **7 rpm/min**.

`#emergency #tripprocedure #coastdown`

---
---

## POST 34 — Vakuum buzishni talab qiladigan 13 holat

**🇺🇿 Vakuum buzib darhol to'xtatish — qachon**

**1. Ichki metall ishqalanish yoki zarba tovushi**
Turbina ichidan aniq metall ishqalanish yoki zarba tovushi eshitilsa **va podshipnik korpusi tebranishi 100 μm dan oshsa**, himoya esa ishlamasa — aylanuvchi va harakatsiz qismlar orasida ishqalanish bor. **Val egilishi yoki kurak sinishining oldini olish uchun vakuum darhol buziladi.**

**2. Ortiqcha val tebranishi**
Val tebranishi **240 μm**ga yetsa yoki podshipnik tebranishi **100 μm**dan oshsa — birlik keskin beqaror holatda.

**3. Overspeed himoyasining ishlamasligi**
Tezlik **3300 rpm** (110%) ga chiqib overspeed himoyasi ishlamasa.

**4. Podshipnik haroratining g'ayritabiiyligi**
• №1/2 journal babbiti **>127°C**
• №3/4/5/6/7/8 journal babbiti **>121°C**
• Upor podshipnik padlari **>115°C**
• **Yoki yog' qaytish harorati 75°C ga yetib, tutun chiqsa** — podshipniklar kuyish arafasida

**5. Yog' bosimining g'ayritabiiyligi**
Yog' bosimi **0.04 MPa**ga tushib zaxira nasos ishga tushmasa, yoki asosiy yog' baki sathi **1200 mm**dan pastga keskin tushib tiklanmasa.

**6. Yog' tizimida xavfsizlikka tahdid soluvchi yong'in**
Yong'in qisqa vaqtda o'chirilmasa va asosiy yog' bakiga yoki yuqori haroratli quvurlarga tarqalish ehtimoli bo'lsa.
⚠️ **DC lube oil nasosni ishga tushiring, asosiy nasosni to'xtating** — sizish holatida yog' berish vaqtini uzaytirish uchun. **DC nasosni faqat rotor 0 ga tushgandan keyin to'xtatish mumkin.**

**7. Ortiqcha o'q siljishi**
HP upor podshipnik o'q pozitsiyasi **±0.889 mm**ga yetib himoya ishlamasa — upor podshipnik ortiqcha yuklanadi, o'q zazori yo'qoladi.

**8. Ortiqcha differensial kengayish**
DXD **>+12.07 mm** yoki **<−9.26 mm**, rotor kengayishi **>+45.5 mm** yoki **<−23.1 mm**.

**9. Kondensator vakuumining to'satdan tushishi**
Vakuum **−55 kPa**dan pastga tushib (absolyut ~45 kPa) past vakuum himoyasi ishlamasa.

**10. LP exhaust haroratining oshishi**
Vakuum tizimida katta havo sizishi vakuumni ushlab turishni imkonsiz qilsa va exhaust harorati **105°C**dan yuqoriga tez ko'tarilsa, spray desuperheating esa samarasiz bo'lsa.

**11. Bug' haroratining tez tushishi**
Main yoki reheat bug' harorati **15 daqiqada 83°C**dan ko'proq keskin tushsa, yoki quvurlarda aniq **gidravlik zarba tovushi** eshitilsa.

**12. Korpuslar orasidagi ortiqcha harorat farqi**
Yuqori va pastki korpus harorati farqi **50°C**dan oshsa, yoki val zichlashidan **oq to'yinmagan bug'** chiqsa, yoki flanets birikmalarida suv sizsa.

**13. Generatorning ichki nosozliklari**
Generator tutasa yoki yonsa, vodorod tizimi portlasa, yoki stator sovutish suvi himoya ishlamagan holda yo'qolsa.

**14. Val zichlashida uchqun yoki kuchli sizish**
Val zichlashida uchqun yoki katta bug' sizishi yog' tizimini yoqishi yoki rotorni mahalliy qizdirib yuborishi mumkin.

---

**🇷🇺 Немедленный останов со срывом вакуума — когда**

**1. Металлический шум трения или удары внутри**
Отчётливый шум трения/удара **и вибрация корпуса подшипника выше 100 мкм** без срабатывания защит — задевание ротора о статор. **Срыв вакуума немедленно** во избежание изгиба вала и обрыва лопаток.

**2. Чрезмерная вибрация вала**
Вибрация вала **240 мкм** или вибрация подшипника выше **100 мкм**.

**3. Отказ защиты от разгона**
Обороты дошли до **3300 об/мин** (110%), защита не сработала.

**4. Аномальные температуры подшипников**
• Баббит №1/2 **>127°C** • Баббит №3–8 **>121°C** • Колодки упорного **>115°C**
• **Или температура слива масла 75°C с дымом** — подшипники на грани выплавления

**5. Аномальное давление масла**
Давление упало до **0.04 МПа**, резервный насос не пустился; либо уровень главного маслобака резко ниже **1200 мм** и не восстанавливается.

**6. Пожар в маслосистеме, угрожающий безопасности**
Не тушится быстро, есть риск распространения на маслобак или горячие трубопроводы.
⚠️ **Пустить насос постоянного тока, остановить основной.** **Остановить насос ПТ только после выбега до 0.**

**7. Чрезмерный осевой сдвиг**
Осевое положение **±0.889 мм** без срабатывания защиты — перегрузка упорного, потеря осевых зазоров.

**8. Чрезмерное относительное расширение**
ОРС **>+12.07 мм** или **<−9.26 мм**; расширение ротора **>+45.5 мм** или **<−23.1 мм**.

**9. Резкое падение вакуума**
Вакуум ниже **−55 кПа** (абс. ~45 кПа) без срабатывания защиты по вакууму.

**10. Высокая температура выхлопа ЦНД**
Массовые присосы не дают держать вакуум, температура быстро растёт выше **105°C**, впрыск неэффективен.

**11. Быстрое падение температуры пара**
Главный или промперегретый пар упал более чем на **83°C за 15 минут**, либо слышны **гидроудары** в трубопроводах.

**12. Чрезмерная разница температур цилиндра**
Верх/низ более **50°C**, либо **белый ненасыщенный пар** из уплотнений, либо течь по разъёму фланцев.

**13. Внутренние повреждения генератора**
Дым или возгорание, взрыв водородной системы, потеря статорной воды без срабатывания защиты.

**14. Искры или сильная течь из уплотнения вала**
Могут поджечь маслосистему или вызвать локальный перегрев ротора.

---

**🇬🇧 Immediate Vacuum Breaking and Trip — when**

**1. Internal metal friction or impact noise**
Obvious metal friction or impact noise inside the turbine **and bearing housing vibration exceeding 100 μm** without the protection system activating — rubbing between rotating and stationary components. **Break vacuum immediately** to prevent shaft bending or blade fracture.

**2. Excessive shaft vibration**
Shaft vibration reaches **240 μm** or bearing vibration exceeds **100 μm**.

**3. Failure of overspeed protection**
Speed rises to **3300 r/min** (110%) without overspeed protection activating.

**4. Abnormal bearing temperatures**
• No.1/2 journal babbitt **>127°C** • No.3–8 journal babbitt **>121°C** • Thrust pads **>115°C**
• **Or bearing oil return temperature reaching 75°C with smoke** — bearings on the verge of burnout

**5. Abnormal lube oil pressure**
Pressure drops to **0.04 MPa** without the standby pump starting, or main oil tank level drops sharply below **1200 mm** and cannot be restored.

**6. Oil system fire threatening safety**
Fire cannot be extinguished quickly and may spread to the main oil tank or high-temperature pipelines.
⚠️ **Start the DC lube oil pump and stop the main lube oil pump.** **Stop the DC pump only after coastdown to 0.**

**7. Excessive axial displacement**
HP thrust bearing axial position reaches **±0.889 mm** with protection failing — thrust bearing overloaded, axial clearance lost.

**8. Excessive differential expansion**
DXD **>+12.07 mm** or **<−9.26 mm**; rotor expansion **>+45.5 mm** or **<−23.1 mm**.

**9. Sudden drop in condenser vacuum**
Vacuum below **−55 kPa** (absolute approx. 45 kPa) without low vacuum protection activating.

**10. High LP exhaust temperature**
Massive air leakage makes vacuum impossible to hold, exhaust temperature rises rapidly above **105°C**, spray desuperheating ineffective.

**11. Fast steam temperature drop**
Main or reheat steam drops by more than **83°C within 15 minutes**, or obvious **water hammer noise** is heard in pipelines.

**12. Excessive cylinder temperature differential**
Upper-to-lower difference exceeds **50°C**, or **white non-saturated steam** emitted from the shaft seal, or water seeps at flange joints.

**13. Internal generator faults**
Generator smokes or catches fire, hydrogen system explodes, or stator cooling water is lost without protection activating.

**14. Sparks or severe leakage from the shaft seal**
May ignite the oil system or cause local overheating of the rotor.

`#emergency #vacuumbreak #tripconditions`

---
---

## POST 35 — Generator asosiy ko'rsatkichlari

**🇺🇿 Generator — nominal ma'lumotlar**

| Parametr | Qiymat |
|---|---|
| Qutblar soni | 2 |
| Nominal chastota | 50 Hz |
| Nominal to'liq quvvat | **640 000 kVA** |
| Aylanish tezligi | 3000 rpm |
| Nominal terminal kuchlanish | **21 kV** |
| Nominal stator toki | **17 595 A** |
| Quvvat koeffitsienti (lagging/leading) | **0.85 / 0.9** |
| H2 gaz bosimi | **5.17 bar.g** |
| Hisoblangan maks. kVA, 0 PF (over/under exc.) | **+487 550 / −258 000** |
| H2 bosimi ish oralig'i (maks/min) | **5.17 / 3.10 bar.g** |

**Generator doimiylari**
• Yuklamasiz qo'zg'atish toki, IFNL: **1410 A**
• Qisqa tutashuv qo'zg'atish toki, IFSI: **2475 A**
• To'liq yuklama qo'zg'atish toki, IFFL: **4125 A**
• To'liq yuklama qo'zg'atish kuchlanishi, VFFL: **647 V** (125°C da)
• Qisqa tutashuv nisbati: **0.57**
• Kuchlanish rostlash, nominal PF / 1.0 PF: **28.9 / 23.6 %**
• To'yinish funksiyasi S(1.0) / S(1.2): **0.1939 / 0.859**
• O'ram qarshiligi 25°C, armatura / qo'zg'atish: **0.001615 / 0.1133 Ω**
• Armatura o'ram sig'imi, faza-yer: **0.2011 μF**
• Telefon garmonik buzilishi: **<5%**
• Uzluksiz teskari ketma-ketlik, I₂: **7.03 %**
• Qisqa muddatli teskari ketma-ketlik, I₂²T: **6.42 sek**
• Harorat ko'tarilishi / izolyatsiya klassi: **F / F**

⚠️ **I₂ = 7.03%** — nomutanosib yuklamada uzluksiz ruxsat etilgan chegara. **I₂²T = 6.42 sek** — bu qisqa tutashuvdagi vaqt byudjeti. Nomutanosiblik alarm chiqsa, birinchi bu ikkisini eslang.

⚠️ Manualda 1.2.1 bo'limida generator **TEWAC (havo bilan sovutiladigan)** deb yozilgan, lekin 1.2.2.1 da **H2 bosimi 5.17 bar.g** va H2 sovutgichlar keltirilgan, 6-bobda esa to'liq H2/CO2 tizimi bor. **1.2.1 va 2.2.4 bo'limlari havo bilan sovutiladigan shablondan qolgan matn.** Amalda mashina vodorod bilan sovutiladi.

---

**🇷🇺 Генератор — номинальные данные**

| Параметр | Значение |
|---|---|
| Число полюсов | 2 |
| Номинальная частота | 50 Гц |
| Полная мощность | **640 000 кВА** |
| Обороты | 3000 об/мин |
| Номинальное напряжение | **21 кВ** |
| Номинальный ток статора | **17 595 А** |
| cos φ (отстающий/опережающий) | **0.85 / 0.9** |
| Давление водорода | **5.17 бар.g** |
| Расчётная макс. кВА при 0 PF | **+487 550 / −258 000** |
| Диапазон давления H2 (макс/мин) | **5.17 / 3.10 бар.g** |

**Постоянные генератора**
• Ток возбуждения XX, IFNL: **1410 А** • КЗ, IFSI: **2475 А** • Полная нагрузка, IFFL: **4125 А**
• Напряжение возбуждения при полной нагрузке: **647 В** (при 125°C)
• ОКЗ: **0.57** • Регулирование напряжения ном. PF / 1.0 PF: **28.9 / 23.6 %**
• Насыщение S(1.0) / S(1.2): **0.1939 / 0.859**
• Сопротивление обмоток при 25°C, якорь / возбуждение: **0.001615 / 0.1133 Ом**
• Ёмкость обмотки якоря фаза-земля: **0.2011 мкФ**
• Телефонные гармоники: **<5%**
• Длительная обратная последовательность I₂: **7.03 %**
• Кратковременная I₂²T: **6.42 с**
• Класс нагревостойкости / изоляции: **F / F**

⚠️ **I₂ = 7.03%** — предел по несимметрии длительно. **I₂²T = 6.42 с** — бюджет времени при КЗ.

⚠️ В п. 1.2.1 генератор описан как **TEWAC (воздушное охлаждение)**, но в 1.2.2.1 указано **давление водорода 5.17 бар.g** и водородные охладители, а в главе 6 — полная система H2/CO2. **Разделы 1.2.1 и 2.2.4 — остаток шаблона воздушной машины.** Фактически охлаждение водородное.

---

**🇬🇧 Generator — rating data**

| Item | Value |
|---|---|
| Number of poles | 2 |
| Rated frequency | 50 Hz |
| Rated apparent power | **640,000 kVA** |
| Rotation speed | 3000 rpm |
| Rated terminal voltage | **21 kV** |
| Rated stator current | **17,595 A** |
| Power factor lagging/leading | **0.85 / 0.9** |
| Hydrogen gas pressure | **5.17 bar.g** |
| Calculated max kVA at 0 PF | **+487,550 / −258,000** |
| H2 pressure operating range max/min | **5.17 / 3.10 bar.g** |

**Generator constants**
• No load field current IFNL **1410 A** • Short circuit IFSI **2475 A** • Full load IFFL **4125 A**
• Full load field voltage VFFL **647 V** at 125°C
• Short circuit ratio **0.57** • Voltage regulation rated/1.0 PF **28.9 / 23.6 %**
• Saturation S(1.0)/S(1.2) **0.1939 / 0.859**
• Winding resistance at 25°C armature/field **0.001615 / 0.1133 Ω**
• Armature capacitance 1 phase to ground **0.2011 μF**
• Telephone harmonic distortion **<5%**
• Continuous negative phase sequence I₂ **7.03 %**
• Short-time negative phase sequence I₂²T **6.42 sec**
• Temperature rise / insulation class **F / F**

⚠️ **I₂ = 7.03%** is the continuous unbalance limit. **I₂²T = 6.42 sec** is the short-time budget.

⚠️ Section 1.2.1 describes a **TEWAC (air-cooled)** generator, yet 1.2.2.1 gives **H2 pressure 5.17 bar.g** with hydrogen coolers, and Chapter 6 has a full H2/CO2 system. **Sections 1.2.1 and 2.2.4 are leftover air-cooled template text.** The machine is hydrogen cooled.

`#generator #rating #nameplate`

---
---

## POST 36 — Generator qobiliyat cheklovlari

**🇺🇿 Maksimal qobiliyat — cheklovlar**

| Holat | Nominal quvvatning % |
|---|---|
| **Bitta H2 sovutgich ishdan chiqsa** | **80%** |
| **Stator o'rami orqali sovutish suvi bo'lmasa** | **27.9%** |

**H2 sovutgichlar (1.2.2.4)**
• Turi / soni: **Simplex / birlik uchun 4 ta**
• Quvur o'lchami: **15.9 mm × 18 BWG**
• Quvur materiali: **90-10 Cu-Ni**
• Quvur plitasi: uglerodli po'lat, epoksid qoplamali
• H2 kirish / chiqish harorati: **58.7 / 40.0°C**
• Kutilgan sovutish suvi kirish harorati oralig'i: **5–37°C**
• Sovutish suvi umumiy sarfi: **406 m³/s** (30.0°C da)
• **Quvur ifloslanishini oldini olish uchun min. sarf: 186 m³/s**
• Sovutish suvi kirish / chiqish: **30.0 / 40.5°C**
• H2 sovutgichlar bo'ylab bosim tushishi: **0.8 bar**
• Suv tomoni loyihaviy bosim: **10.0 bar**
• O'rnatilishi: gorizontal, stator ramasi ustida

⚠️ **Bitta sovutgich chiqsa 80%** — ya'ni 640 MVA dan 512 MVA. Bu avtomatik emas, **operator yuklamani tushirishi kerak**.

⚠️ **Stator suvi yo'qolsa 27.9%** — lekin amalda stator suvi sarfi **54.1 m³/s** dan tushsa **ST trip** bo'ladi. Ya'ni 27.9% loyihaviy imkoniyat, himoya undan oldin ishlaydi.

⚠️ **186 m³/s** — bu quvurlar ifloslanmasligi uchun minimal sarf. Undan past sarfda ishlash sovutgichni sekin ishdan chiqaradi, bu darhol ko'rinmaydi.

---

**🇷🇺 Максимальная нагрузочная способность — ограничения**

| Условие | % от номинала |
|---|---|
| **Один водородный охладитель выведен** | **80%** |
| **Нет циркуляции воды через обмотку статора** | **27.9%** |

**Водородные охладители (1.2.2.4)**
• Тип / количество: **Simplex / 4 на блок** • Трубки: **15.9 мм × 18 BWG**, **90-10 Cu-Ni**
• Трубная доска: углеродистая сталь с эпоксидным покрытием
• Температура H2 вход/выход: **58.7 / 40.0°C**
• Диапазон температуры охлаждающей воды на входе: **5–37°C**
• Суммарный расход воды: **406 м³/ч** при 30.0°C
• **Минимальный расход против загрязнения трубок: 186 м³/ч**
• Вода вход/выход: **30.0 / 40.5°C** • Потеря давления: **0.8 бар**
• Расчётное давление водяной стороны: **10.0 бар** • Установка горизонтальная

⚠️ **80% при одном выведенном охладителе** — с 640 МВА до 512 МВА. Автоматики нет, **разгружает оператор**.

⚠️ **27.9% без статорной воды** — но фактически при расходе ниже **54.1 м³/ч** идёт **отключение ПТ**. 27.9% это проектная возможность, защита срабатывает раньше.

⚠️ **186 м³/ч** — минимум против загрязнения трубок. Работа ниже медленно выводит охладитель из строя, и это не видно сразу.

---

**🇬🇧 Maximum Capability — limits**

| Condition | % of rating |
|---|---|
| **With one H2 cooler out of service** | **80%** |
| **Without coolant circulation through stator winding** | **27.9%** |

**Hydrogen coolers (1.2.2.4)**
• Type / quantity: **Simplex / 4 per unit** • Tube size **15.9 mm × 18 BWG**, **90-10 Cu-Ni**
• Tube sheet: carbon steel, epoxy coated
• H2 temp entering/leaving: **58.7 / 40.0°C**
• Expected inlet cooling water temp range: **5–37°C**
• Total cooling water flow: **406 m³/h** at 30.0°C
• **Min cooling water flow to avoid tube fouling: 186 m³/h**
• Water entering/leaving: **30.0 / 40.5°C** • Pressure drop: **0.8 bar**
• Design pressure water side: **10.0 bar** • Mounted horizontally on stator frame

⚠️ **80% on one cooler out** — 640 MVA down to 512 MVA. There is no automatic action; **the operator unloads**.

⚠️ **27.9% without stator water** — but in practice stator flow below **54.1 m³/h** gives an **ST trip**. The 27.9% is design capability; protection acts first.

⚠️ **186 m³/h** is the anti-fouling minimum. Running below it degrades the cooler slowly and invisibly.

`#generator #H2cooler #capability`

---
---

## POST 37 — ST podshipniklari: konstruksiya

**🇺🇿 Podshipniklar — turi va o'lchash nuqtalari**

**Turlari va joylashuvi**
• **Tilting pad** — HIP rotorining **ikkala uchida**. Sababi: o'z-o'zini tekislash qobiliyati katta, yuklama tebranishi kuchli yoki katta nomutanosiblik bo'ladigan joyda ishlatiladi
• **Elliptik** — **LP rotori** uchun, yuklama ko'tarish qobiliyati yuqori bo'lgani sababli
• **Upor podshipnik** — **tilting pad**, ikkala yo'nalishdagi muvozanatlanmagan o'q kuchini boshqaradi, **o'q bo'yicha sozlanadi**

**Material**
Sirpanish qismining qoplamasi — **qalay asosli oq metall (babbit)**.

**Jacking oil**
Yuqori bosimli jacking yog' **journal podshipniklarining pastki qismiga** yo'naltiriladi — ishga tushirish va turning gear davrida yog' plyonkasi hosil qilish uchun.

**Harorat o'lchash — qayerda**
• Journal podshipniklarda: termopara **pastki qobiqdagi oq metall qoplamasining bevosita ostida**
• Upor podshipnikda: **diametral qarama-qarshi ikkita padda**, **active va non-active** tomonlarda

**Xizmat ko'rsatish**
Journal va upor podshipniklarni **rotorni yechmasdan** ko'zdan kechirish mumkin.

**Generator podshipniklari (2.2.3)**
Ikki tomonlama tilting bearing. Pedestal tarkibi: ichki oil deflector, podshipnik uzeli, tashqi oil deflector, va generatorga yog' kirishini oldini oluvchi havo shlanglari.
Oil deflector ikki tish to'plami orasida **to'r bilan jihozlangan tutgich cho'ntagi**ga ega — yog'ni ushlaydi va aylanishini kamaytiradi.
Rotor yuzasida **yog' ariqchalari** frezalangan: rotorga yopishgan yog' deflector tashqarisiga siljiganda ariqchaga duch kelib yuzadan ajraladi.

⚠️ Trip setpointi №1,2 uchun **127°C**, №3–8 uchun **121°C** — chunki 1 va 2 tilting pad, qolganlari boshqa tipda. **Bu tasodifiy emas.**

---

**🇷🇺 Подшипники — тип и точки измерения**

**Типы и расположение**
• **Сегментные (tilting pad)** — на **обоих концах ротора ЦВСД**: высокая самоустанавливающаяся способность при сильных колебаниях нагрузки и расцентровке
• **Эллиптические** — на **роторе ЦНД** из-за высокой несущей способности
• **Упорный** — **сегментный**, воспринимает осевое усилие в обе стороны, **регулируется по оси**

**Материал**
Заливка скользящей части — **баббит на оловянной основе**.

**Гидроподъём**
Масло высокого давления подаётся **в нижнюю часть опорных подшипников** — для создания плёнки при развороте и на ВПУ.

**Где измеряется температура**
• Опорные: термопара **непосредственно под баббитом нижнего вкладыша**
• Упорный: **на двух диаметрально противоположных колодках**, на **рабочей и нерабочей** сторонах

**Обслуживание**
Осмотр опорных и упорного подшипников возможен **без выемки ротора**.

**Подшипники генератора (2.2.3)**
Двойные сегментные. Стул содержит внутренний маслоотбойник, узел подшипника, наружный маслоотбойник и шланги подвода воздуха против попадания масла в генератор.
Маслоотбойник имеет **улавливающий карман с сеткой** между двумя рядами гребней.
На поверхности ротора **проточены канавки**: масло, увлекаемое поверхностью, отрывается на канавке.

⚠️ Уставка защиты для №1,2 — **127°C**, для №3–8 — **121°C**: №1 и 2 сегментные, остальные другого типа. **Это не случайность.**

---

**🇬🇧 Bearings — types and measurement points**

**Types and location**
• **Tilting pad** — **both ends of the HIP rotor**: greater self-alignment capability, used where load fluctuation is severe or large misalignment occurs
• **Elliptical** — **LP rotor**, chosen for high load capacity
• **Thrust** — **tilting pads**, manages unbalanced thrust in both directions, **axially adjustable**

**Material**
Sliding portion lining is **tin-based white metal**.

**Jacking oil**
High-pressure jacking oil is routed to the **bottom part of the journal bearings** to create an oil film during rotor start-up and turning gear operation.

**Where temperature is measured**
• Journal bearings: thermocouple **directly under the white metal lining of the bottom shell**
• Thrust bearing: **two diametrically opposed pads**, on **active and non-active** sides

**Maintenance**
Inspection of journal and thrust bearings is possible **without removal of the rotor**.

**Generator bearings (2.2.3)**
Double tilting bearings. The pedestal includes inner oil deflector, bearing assembly, outer oil deflector and air feed hoses to prevent oil leaking into the generator.
The oil deflector has a **catch pocket with a screen** between two sets of teeth.
**Oil grooves are machined into the rotor surface** so oil clinging to the rotor separates when it meets the groove.

⚠️ Trip is **127°C** for #1,2 and **121°C** for #3–8 — #1 and #2 are tilting pad, the rest are not. **That difference is deliberate.**

`#bearings #tiltingpad #babbitt`

---
---

## POST 38 — Stop va control klapanlar

**🇺🇿 HP/IP/LP klapanlar — konstruksiya va yopilish mantiqi**

**HP Stop Valve (HPSV)**
• 2 ta, HIP korpusining ikkala tomonida, **vertikal**
• HPCV bilan **umumiy kamera**da, HPCV dan yuqoriroqda
• Ikkala HP klapan kamerasi o'zaro **bog'langan** — bug' parametrlarini tenglashtirish uchun va **klapanlar orqali bug' oqimini uzmasdan** HPSV ishlashini tekshirish imkonini beradi
• Konus (disk) ichida **kichik ichki konus** bor — katta konusni ochish uchun kerak bo'lgan kuchni kamaytiradi
• Shpindel **maxsus grafit halqalar** bilan zichlanadi, halqalar **tarelka prujinalari** bilan tarangdir
• **Gidravlik aktuatorlar** bilan yuritiladi, ochilish High-Pressure Hydraulic Power Unit orqali
• ⚠️ **Solenoid ostiga bosim berilganda ochiladi, PRUJINA kuchi bilan yopiladi** — bu gidravlik bosim yo'qolganda ham, boshqaruv signali uzilganda ham **avtomatik yopilishni ta'minlaydi**
• Holati **LVDT** bilan kuzatiladi

**HP Control Valve (HPCV)**
2 ta, HPSV dan keyin, HP bo'limga bug' miqdorini boshqaradi. Gidravlik aktuator, grafit halqali zichlash. Bug' kirishi **bitta kanal** orqali. HIP korpusga **qattiq flanets va shpilka** bilan mahkamlanadi.

**IP Stop Valve (IPSV) / IP Control Valve (IPCV)**
2 tadan, HIP korpusining ikkala tomonida, **gorizontal**. IPCV bug'ni **ikkita soplo va lead pipe** orqali kiritadi — biri yuqorida, biri pastda. IP klapanlar **to'rt quloqli support** bilan tayanadi.

**LP Stop Valve (LPSV)**
**Nosimmetrik butterfly** turi. Boshqaruv funksiyasi **ikki holatli (ochiq/yopiq)**. Servomotor porsheni ostiga bosim berilganda ochiladi, **prujina kuchi bilan yopiladi**.

**LP Control Valve (LPCV)**
**Simmetrik butterfly**, servomotor bilan pozitsiyalanadi. HRSG dan LP bug' miqdorini boshqaradi.

**NRV (Non-Return Valve)**
HP exhaust ning **sovuq qayta qizdirish** quvurida. Normal ishda oldinga oqim uchun ochiq. **Trip yoki uskuna nosozligida bug' va suvning HP turbinaga kirishini oldini oladi.**

⚠️ Barcha stop klapanlar **prujina bilan yopiladi** — gidravlika yo'qolsa ular o'zi yopiladi. Shuning uchun **gidravlik bosim LL trip 110 bar.g** shunchalik muhim: bu chegaradan pastda klapanlar nazoratsiz yopila boshlaydi.

---

**🇷🇺 Стопорные и регулирующие клапаны — конструкция и логика закрытия**

**ГСК ВД (HPSV)**
• 2 шт по обеим сторонам корпуса ЦВСД, **вертикально**, в **общей камере** с РК ВД
• Камеры обоих клапанов **соединены** — выравнивание параметров и проверка ГСК **без прерывания расхода** через РК
• В конусе — **малый внутренний конус** для снижения усилия открытия
• Шток уплотнён **графитовыми кольцами** с поджатием **тарельчатыми пружинами**
• Привод **гидравлический**, открытие от блока высокого давления
• ⚠️ **Открывается подачей давления под соленоид, закрывается ПРУЖИНОЙ** — автоматическое закрытие и при потере гидравлики, и при обрыве сигнала
• Положение контролируется **LVDT**

**РК ВД (HPCV)**
2 шт за ГСК, регулируют расход в ЦВД. Гидропривод, графитовое уплотнение штока, вход пара **по одному каналу**, крепление к корпусу **жёстким фланцем со шпильками**.

**ГСК/РК СД**
По 2 шт с обеих сторон, **горизонтально**. РК СД вводит пар **через два сопла и перепускные трубы** — верхнее и нижнее. Опора клапанов **на четырёх лапах**.

**ГСК НД (LPSV)**
**Несимметричная поворотная заслонка**, **два положения (откр/закр)**. Открывается подачей под поршень сервомотора, **закрывается пружиной**.

**РК НД (LPCV)**
**Симметричная поворотная заслонка**, позиционируется сервомотором.

**Обратный клапан (NRV)**
На линии холодного промперегрева выхлопа ЦВД. В работе открыт по прямому потоку. **Предотвращает попадание пара и воды в ЦВД при отключениях и отказах.**

⚠️ Все стопорные закрываются **пружиной** — при потере гидравлики закроются сами. Поэтому уставка **давления ОГ LL 110 бар.g** так важна: ниже неё клапаны начнут закрываться неуправляемо.

---

**🇬🇧 Stop and Control Valves — construction and closing logic**

**HP Stop Valves (HPSV)**
• Two, both sides of the HIP casing, **vertical**, sharing **common chambers** with the HP control valves
• Both HP valve chambers are **interconnected** to level steam parameters and to check HPSV operability **without interrupting steam flow** through the control valves
• The cone (disc) has a **small internal cone** to reduce the force needed to open the large cone
• Spindle sealed with **special graphite rings**, pretensioned by **dish type springs**
• Driven by **hydraulic actuators**; opening arranged by the High-Pressure Hydraulic Power Unit
• ⚠️ **Opens when pressure medium is let under the solenoid valve, closes by SPRING force** — assuring automatic closing on hydraulic pressure loss and on control signal breakdown
• Position monitored by **LVDT**

**HP Control Valves (HPCV)**
Two, downstream of HPSV, controlling steam quantity to the HP section. Hydraulic actuators, graphite ring spindle seals, steam entry via **one channel**, mounted to the HIP casing by **rigid flange and stud bolt**.

**IP Stop / Control Valves**
Two each, both sides of the HIP casing, **horizontal**. IPCV admits steam via **two nozzles and lead pipes**, one upper and one lower. Supported by valve support with **four lugs**.

**LP Stop Valve (LPSV)**
**Asymmetrical butterfly** type, **two positions (open/close)**. Opens with pressure medium under the servomotor piston, **closes by spring force**.

**LP Control Valve (LPCV)**
**Symmetrical butterfly**, positioned by servomotor.

**NRV (Non-Return Valve)**
On the cold reheat pipeline of the HP exhaust. Open to forward flow in normal operation. **Prevents steam and water entering the HP turbine during trips or equipment failure.**

⚠️ Every stop valve **closes by spring** — lose hydraulics and they close themselves. That is why the **hydraulic pressure LL trip at 110 bar.g** matters: below it the valves start closing without command.

`#valves #HPSV #NRV #hydraulic`

---
---

## POST 39 — LP relief diaphragm

**🇺🇿 LP korpus xavfsizlik membranasi**

**Nima uchun**
LP exhaust hood ichidagi **ortiqcha bosimdan** turbina qismlarini himoya qilish. **4 ta rupture disk** LP tashqi korpusining tepasida.

**Konstruksiya**
• Tayanch panjara LP tashqi korpusidagi o'yiqqa o'rnatiladi
• **Rezina qalqon va alyuminiy membrana** kombinatsiyasi panjarada **qisqich halqa** bilan ushlab turiladi, halqa LP tashqi korpusiga boltlanadi

**Ishlashi**
• Normal ishda membrana **atmosfera bosimi bilan ichkariga** tayanch panjaraga bosilgan holda turadi
• Vakuum yo'qolib ichki bosim ko'tarilsa, membrana **tashqariga** itariladi va uzeldagi **kesuvchi pichoqqa** tegib, membranadan disk kesib olinadi
• Bu exhaust bosimini atmosferaga chiqaradi
• **Yo'naltiruvchi shtanga** kesilgan diskning uzoqqa uchib ketishiga yo'l qo'ymaydi

**Yorilish bosimi**
⚠️ **Taxminan 5 psi.g** (≈0.34 bar.g)

**Ortiqcha bosimning asosiy sababi**
Kondensatorning **aylanma sovutish suvi yo'qolishi** tufayli issiqlik yukini qabul qila olmasligi. Issiqlik yuki qozon/bug' generatorlari, oziqlantiruvchi suv qizdirgichlari va tizim quvurlaridagi **katta bug' va suv zaxirasidan** keladi.

**Qachon yuzaga keladi**
Odatda **stansiyani ishga tushirish va to'xtatishda**, aylanma nasoslar o'chirilganda, **yoki birlik ishlayotganda aylanma nasoslar ishdan chiqqanda**.

⚠️ LP exhaust bosim trip **0.45 bar.a** (vakuumda), membrana esa **~0.34 bar.g** (atmosferadan yuqori) da yoriladi. Ikkalasi butunlay boshqa masshtabda — membrana **himoyaning oxirgi chizig'i**, trip esa ancha oldin ishlaydi. Membrana yorilgan bo'lsa, demak trip ishlamagan yoki bug' oqimi to'xtamagan.

---

**🇷🇺 Предохранительная мембрана корпуса ЦНД**

**Зачем**
Защита деталей турбины от **избыточного давления** в выхлопном патрубке ЦНД. **4 разрывные мембраны** на верхней половине наружного корпуса.

**Конструкция**
Опорная решётка в выточке корпуса; **резиновый щит и алюминиевая мембрана** удерживаются **прижимным кольцом** на болтах.

**Работа**
• В нормальном режиме мембрана **вдавлена внутрь атмосферным давлением** на решётку
• При потере вакуума и росте внутреннего давления мембрана выдавливается **наружу** на **режущий нож**, из неё вырезается диск, давление сбрасывается в атмосферу
• **Направляющая штанга** не даёт диску улететь далеко

**Давление разрыва**
⚠️ **Около 5 psi.g** (≈0.34 бар.g)

**Основная причина превышения давления**
Конденсатор не принимает тепловую нагрузку из-за **потери циркуляционной воды**. Тепло приходит от **больших запасов пара и воды** в котлах, ПВД и трубопроводах.

**Когда происходит**
Обычно при **пусках и остановах**, когда циркнасосы отключены, **или при их отказе на работающем блоке**.

⚠️ Защита по давлению выхлопа — **0.45 бар.а** (по вакууму), мембрана рвётся при **~0.34 бар.g** (выше атмосферы). Совершенно разные шкалы: мембрана — **последний рубеж**, защита срабатывает намного раньше. Порванная мембрана означает, что защита не отработала или пар не был отсечён.

---

**🇬🇧 LP Casing Relief Diaphragm**

**Purpose**
Protect turbine components from damage due to **over pressurization within the exhaust hood**. **Four rupture disks** on top of the LP outer casing.

**Construction**
Supporting grating fits a recess in the LP outer casing; an arrangement of **rubber shield and aluminium diaphragm** is held on the grid by a **clamp ring** bolted to the casing.

**Operation**
• In normal operation the diaphragm is **dished inward against the supporting grating by atmospheric pressure**
• If vacuum fails and internal hood pressure rises, the diaphragm is forced **outward against the cutting knife**, cutting a disc free and relieving exhaust pressure to atmosphere
• A **guide bar** prevents the disc from travelling far after rupturing

**Rupture pressure**
⚠️ **Approximately 5 psi.g** (≈0.34 bar.g)

**Major cause of over pressurization**
Inability of the condenser to accept heat load due to **loss of circulating cooling water**. The heat comes from the **large inventories of steam and water** in the boiler/steam generators, feed water heaters and system piping.

**When it happens**
Typically during **plant start-ups and shutdowns** when circulating pumps are off, **or when circulating pumps fail while the unit is operating**.

⚠️ The LP exhaust trip is **0.45 bar.a** (in vacuum); the diaphragm bursts at **~0.34 bar.g** (above atmosphere). Different scales entirely — the diaphragm is the **last line of defence**, the trip acts long before. A burst diaphragm means the trip did not act or steam was not cut off.

`#reliefdiaphragm #rupturedisk #LPhood`

---
---

## POST 40 — Kondensator

**🇺🇿 Sirt tipidagi kondensator — spetsifikatsiya**

KKS: **10MAG01AC001** | Model: **N-38080-1** | Turi: sirt tipida

| Parametr | Qiymat |
|---|---|
| Issiqlik almashinuv yuzasi | **38 080 m²** |
| ST exhaust sarfi | **1238.328 t/s** |
| Turbina exhaust entalpiyasi | **2347.3 kJ/kg** |
| **Kondensator qarshi bosimi** | **4.5 kPa(a)** |
| Terminal farq | **3.1°C** |
| Aylanma suv harorat ko'tarilishi | **8.82°C** |
| Sovutish suvi loyihaviy harorati | **19.12°C** |
| Sovutish suvi sarfi | **74 516 t/s** |
| Tozalik koeffitsienti | **0.9** |
| Quvur materiali | **TP316L** |
| Quvur o'lchami | tashqi Ø **28.575 mm**, devor **0.5 / 0.7 mm** |
| 0.5 mm quvurlar soni | **26 454** |
| 0.7 mm quvurlar soni | **1454** |
| **Jami quvurlar** | **27 908** |
| Yuklamasiz og'irlik | **942.9 t** |
| Ish yuklamasi og'irligi | **1668.5 t** |
| To'liq yuklama og'irligi | **2775 t** |

**Konstruksiya**
• **Bo'yin kengaytirish uzeli** — katta tortqi shtanga konstruksiyasi, kondensator va LP silindr orasidagi **vertikal va gorizontal** termik kengayish farqini qabul qiladi. Kondensator LP silindr bilan birga exhaust yo'nalishida siljiydi
• **Bo'yin** — bug' va drenajni yo'naltiradi, bug' quvur bog'lamining ichiga imkon qadar **bir tekis** kirishi uchun. Ichida vertikal va gorizontal tayanch ferma. Bypass bug'ini sovutish uchun **suv pardasi purkash qurilmasi**
• **Korpus** — quvurlar **ikki guruh UT tipida** joylashgan. Quvur bog'lamining markaziy qismi **havo-sovutish zonasi**, u asosiy kondensatsiya zonasidan **bug' to'sig'i** bilan ajratilgan. Vakuum quvuri shu zonaga ulanadi
• **Hot well** — korpus tagida, to'rtburchak. Kondensat chiqishi normal sathda butun kondensatni **1 soat ichida** chiqara oladi

⚠️ Loyihaviy qarshi bosim **4.5 kPa(a) = 0.045 bar.a** — bu Table 1-1-1 dagi LP exhaust bosimi bilan bir xil. Alarm **0.33 bar.a** da, ya'ni loyihaviy qiymatdan **7 barobar** yuqorida.

⚠️ Aylanma suv sarfi **74 516 t/s** — CCWS gradirnyasidan. Bir nasos yo'qolsa bu sarf yarmiga tushadi, qarshi bosim darhol ko'tariladi.

---

**🇷🇺 Поверхностный конденсатор — спецификация**

KKS **10MAG01AC001** | Модель **N-38080-1**

| Параметр | Значение |
|---|---|
| Поверхность теплообмена | **38 080 м²** |
| Расход выхлопа ПТ | **1238.328 т/ч** |
| Энтальпия выхлопа | **2347.3 кДж/кг** |
| **Противодавление** | **4.5 кПа(а)** |
| Температурный напор | **3.1°C** |
| Нагрев циркводы | **8.82°C** |
| Расчётная температура циркводы | **19.12°C** |
| Расход циркводы | **74 516 т/ч** |
| Коэффициент чистоты | **0.9** |
| Материал трубок | **TP316L** |
| Размер трубок | Ø **28.575 мм**, стенка **0.5 / 0.7 мм** |
| Количество 0.5 мм | **26 454** | 
| Количество 0.7 мм | **1454** |
| **Всего трубок** | **27 908** |
| Вес без нагрузки / рабочий / полный | **942.9 / 1668.5 / 2775 т** |

**Конструкция**
• **Компенсатор горловины** — на больших тягах, воспринимает разницу теплового расширения конденсатора и ЦНД по **вертикали и горизонтали**
• **Горловина** — распределяет пар **равномерно** по трубному пучку, внутри опорные фермы, есть **водяная завеса** для охлаждения байпасного пара
• **Корпус** — трубки в **двух пучках типа UT**, центральная зона — **воздухоохлаждающая**, отделена **паровым щитом**, к ней подключён вакуумный трубопровод
• **Конденсатосборник** — прямоугольный, внизу корпуса, при нормальном уровне выдаёт весь конденсат **за 1 час**

⚠️ Проектное противодавление **4.5 кПа(а) = 0.045 бар.а** совпадает с Table 1-1-1. Сигнал на **0.33 бар.а** — **в 7 раз** выше проектного.

⚠️ Расход циркводы **74 516 т/ч** от градирни ЦОС. Потеря одного насоса — расход вдвое, противодавление растёт сразу.

---

**🇬🇧 Surface Condenser — specification**

KKS **10MAG01AC001** | Model **N-38080-1**

| Item | Value |
|---|---|
| Heat exchange area | **38,080 m²** |
| ST exhaust flow | **1238.328 t/h** |
| Exhaust enthalpy | **2347.3 kJ/kg** |
| **Back pressure** | **4.5 kPa(a)** |
| Terminal difference | **3.1°C** |
| Circulating water temperature rise | **8.82°C** |
| Cooling water design temperature | **19.12°C** |
| Cooling water flow | **74,516 t/h** |
| Cleaning factor | **0.9** |
| Tube material | **TP316L** |
| Tube size | OD **28.575 mm**, wall **0.5 / 0.7 mm** |
| Qty 0.5 mm / 0.7 mm | **26,454 / 1454** |
| **Total tubes** | **27,908** |
| Weight unloaded / operating / full | **942.9 / 1668.5 / 2775 t** |

**Construction**
• **Neck expansion joint** — large pull rod structure accommodating thermal expansion differences between condenser and LP cylinder **vertically and horizontally**
• **Neck** — guides steam evenly into the tube bundle, internal support truss, **water curtain spray** to cool bypass steam
• **Shell** — tubes in **two UT type groups**, central **air-cooling zone** separated by a **steam baffle**, vacuum pipe connects there
• **Hot well** — rectangular, at the shell bottom; the condensate outlet can discharge all condensate **within 1 hour** at normal level

⚠️ Design back pressure **4.5 kPa(a) = 0.045 bar.a**, matching Table 1-1-1. Alarm is at **0.33 bar.a** — **seven times** design.

⚠️ Circulating water **74,516 t/h** from the CCWS tower. Lose one pump and that halves, back pressure moves immediately.

`#condenser #backpressure #MAG`

---
---

## POST 41 — Vakuum nasos spetsifikatsiyasi

**🇺🇿 Vakuum nasos va uskuna**

**Nasos — KKS 10PUE21/22AP001**
• Ishlab chiqaruvchi: **Gardner Denver NASH**
• Model: **konus tipidagi suyuq halqali vakuum nasos**
• Quvvat (holding) 2.6 / 4.5 / 7.6 kPa da: **61.2 / 77 / 92 kg/s**
• Val quvvati: **104 / 106 / 112 kW**
• **Tezlik: 500 rpm**
• Nasos FIK: **25%**
• Korpus loyihaviy / gidravlik sinov: **0.02 / 0.03 MPa**
• Sovutish suvi harorati: **8.85–33.1°C**
• Sovutish suvi sarfi: **85 t/s**
• **Suyuq halqa harorati: 21.2°C**
• Ishchi suyuqlik harorati: **21.2°C**
• Ishchi g'ildirak diametri: **762 mm**
• Zichlash: **mexanik** | Podshipnik: **konusli rolikli**
• O'lchamlari: 6520 × 2200 × 2700 mm

**Dvigatel — WEG**
• Nominal quvvat: **185 kW** | IP55 | 400 V / 3 faza / 50 Hz
• **Nominal tezlik: 1485 rpm** (nasos 500 rpm — **reduktor orqali**)
• Izolyatsiya klassi: **F** | Ish rejimi: **S1**
• To'liq yuklama toki / cos φ: **329 A / 0.89**
• Qulflangan rotor toki: **7.1 barobar**
• FIK to'liq yuklamada: **0.958**
• Podshipnik moyi: **EP2** | Harorat datchigi: **PT100**
• Isitgich: **140 W / 230 V**

**Issiqlik almashgich — Alfalaval**
• Plastinali, **17 m²**, **74 plastina**, qalinlik **0.4 mm**, material **SS316L**
• Sovutish suvi bosim tushishi: **0.05 MPa**
• Sovutish suvi sarfi / harorati: **≤85 t/s / 19.2°C**
• Issiqlik almashinuv zaxirasi: **20%**

⚠️ **Suyuq halqa harorati 21.2°C** loyihaviy, **alarm 45°C**. Bu 24°C zaxira, lekin yozda gradirnya suvi issiq bo'lganda issiqlik almashgich yetishmay qoladi. Alarm chiqmasa ham 30°C dan yuqori suyuq halqa **vakuumni sekin yomonlashtiradi**.

⚠️ Nasos **500 rpm**, dvigatel **1485 rpm** — orasida reduktor bor. Reduktor tebranish va shovqini alohida kuzatiladi.

---

**🇷🇺 Вакуумный насос — спецификация**

**Насос 10PUE21/22AP001** — **Gardner Denver NASH**, конусный водокольцевой
• Производительность при 2.6 / 4.5 / 7.6 кПа: **61.2 / 77 / 92 кг/ч**
• Мощность на валу: **104 / 106 / 112 кВт** • **Обороты 500 об/мин** • КПД **25%**
• Корпус расчёт/гидроиспытание: **0.02 / 0.03 МПа**
• Охлаждающая вода: **8.85–33.1°C**, расход **85 т/ч**
• **Температура жидкостного кольца: 21.2°C** • Рабочая жидкость: **21.2°C**
• Диаметр рабочего колеса: **762 мм** • Уплотнение **механическое** • Подшипники **конические роликовые**

**Двигатель WEG** — **185 кВт**, IP55, 400 В/3/50 Гц, **1485 об/мин**, изоляция **F**, режим **S1**
• Ток полной нагрузки / cos φ: **329 А / 0.89** • Пусковой ток **7.1×** • КПД **0.958**
• Смазка **EP2** • Датчик **PT100** • Подогреватель **140 Вт / 230 В**

**Теплообменник Alfalaval** — пластинчатый **17 м²**, **74 пластины**, **0.4 мм**, **SS316L**
• Потеря давления **0.05 МПа** • Вода **≤85 т/ч / 19.2°C** • Запас поверхности **20%**

⚠️ Проектная температура кольца **21.2°C**, сигнал на **45°C**. Запас 24°C, но летом теплообменника не хватает. Даже без сигнала кольцо выше 30°C **медленно ухудшает вакуум**.

⚠️ Насос **500 об/мин**, двигатель **1485 об/мин** — между ними редуктор. Его вибрацию и шум контролируют отдельно.

---

**🇬🇧 Vacuum Pump — specification**

**Pump 10PUE21/22AP001** — **Gardner Denver NASH**, cone type liquid ring
• Capacity (holding) at 2.6 / 4.5 / 7.6 kPa: **61.2 / 77 / 92 kg/h**
• Shaft power: **104 / 106 / 112 kW** • **Speed 500 rpm** • Efficiency **25%**
• Pump body design / hydro: **0.02 / 0.03 MPa**
• Cooling water: **8.85–33.1°C**, flow **85 t/h**
• **Liquid ring temperature: 21.2°C** • Operating liquid: **21.2°C**
• Impeller diameter **762 mm** • **Mechanical seal** • **Tapered roller** bearings

**Motor WEG** — **185 kW**, IP55, 400 V/3/50 Hz, **1485 rpm**, insulation **F**, duty **S1**
• Full load current / PF: **329 A / 0.89** • Locked rotor **7.1×** • Efficiency **0.958**
• Grease **EP2** • **PT100** • Space heater **140 W / 230 V**

**Heat exchanger Alfalaval** — plate, **17 m²**, **74 plates**, **0.4 mm**, **SS316L**
• Water pressure drop **0.05 MPa** • Flow **≤85 t/h / 19.2°C** • Area margin **20%**

⚠️ Design ring temperature **21.2°C**, alarm at **45°C**. That's 24°C of margin, but in summer the exchanger runs out of duty. Even without an alarm, a ring above 30°C **degrades vacuum quietly**.

⚠️ Pump runs at **500 rpm**, motor at **1485 rpm** — there is a gearbox between them, monitored separately for noise and vibration.

`#vacuumpump #NASH #liquidring`

---
---

## POST 42 — HP bypass boshqaruv rejimlari

**🇺🇿 HP bypass — 8 ta rejim**

Tizim HP kollektor bug' bosimini setpointda ushlaydi, **bir konturli PID**.

| Rejim | Faollashish sharti | Bosim maqsadi |
|---|---|---|
| **a. To'liq yopiq** | HRSG ishga tushgandan keyin, avto rejim | **5 bar** |
| **b. Minimal bosim** | HP asosiy bug' bosimi **>5 bar** | **5 bar**, klapan asta ochiladi |
| **c. Bosim ko'tarilishi** | Klapan ochilishi > start ochilishi | Maqsad **haqiqiy bosimni kuzatadi**, ochilish deyarli o'zgarmaydi, bosim ko'tariladi |
| **d. Doimiy bosim** | Klapan ochilishi > start ochilishi **VA** asosiy bug' bosimi > **69 bar** | Qat'iy **69 bar** (turbina roll bosimi) |
| **e. Sirpanuvchi bosim** | Sinxronizatsiyadan keyin **VA yuklama >40%** | Sirpanuvchi egri chiziq, setpoint **TCS dan AO orqali** |
| **f. Issiq zaxira** | Sinxronizatsiya **VA** klapan fikri **<5%** | **Min(turbina setpointi +10 bar, tez ochilish chegarasi)** |
| **g. HRSG trip** | HRSG trip bo'lganda | HRSG tiklanganda chiqadi |
| **h. Qozon to'xtamasdan turbina trip** | Issiq zaxira rejimida, turbina trip yoki yuklama tashlash, HRSG trip shartlarisiz | Klapan **tez ochiladi**, keyin **69 bar** ni avto ushlaydi |

**Rejim d dan chiqish**
Haqiqiy bosim maqsaddan **±5 bar** ichida bo'lganda avtomatik doimiy bosim rejimiga o'tadi. Operator maqsadga yaqinlashish uchun **qo'lda bias** qo'sha oladi.

**Rejim h dan chiqish shartlari**
HRSG trip rejimi, bosim ko'tarilish rejimi, yoki doimiy bosim rejimi faollashishi.

**HP bypass harorat boshqaruvi**
Bir konturli. Operator qo'lda kiritgan setpoint HP bypass dan keyingi harorat bilan solishtiriladi.
⚠️ **Setpoint chegarasi: joriy HP bypass pasaytirilgan bosimidagi to'yinish harorati + 30°C.** Ya'ni siz istagan haroratni qo'ya olmaysiz — tizim uni to'yinishdan 30°C yuqorida cheklaydi.

⚠️ **69 bar — turbina roll bosimi.** Bu raqamni yodda tuting: HP bypass shu qiymatga qulflanadi, va ST roll-off shu bosimda boshlanadi.

---

**🇷🇺 БРОУ ВД — 8 режимов**

Система держит давление коллектора ВД на уставке, **одноконтурный ПИД**.

| Режим | Условие | Уставка давления |
|---|---|---|
| **a. Полностью закрыт** | После пуска КУ, авторежим | **5 бар** |
| **b. Минимальное давление** | Давление ВД **>5 бар** | **5 бар**, клапан постепенно открывается |
| **c. Подъём давления** | Открытие > пускового | Уставка **следит за фактическим**, открытие почти неизменно |
| **d. Постоянное давление** | Открытие > пускового **И** давление > **69 бар** | Фиксированно **69 бар** |
| **e. Скользящее давление** | После синхронизации **И нагрузка >40%** | Скользящая кривая, уставка **из TCS по AO** |
| **f. Горячий резерв** | Синхронизация **И** обратная связь клапана **<5%** | **Min(уставка турбины +10 бар, порог быстрого открытия)** |
| **g. Отключение КУ** | При отключении КУ | Выход при восстановлении КУ |
| **h. Отключение ПТ без останова котла** | Из горячего резерва, при отключении/сбросе нагрузки без условий отключения КУ | Клапан **быстро открывается**, затем держит **69 бар** |

**Переход в режим d**
Автоматически, когда фактическое давление в пределах **±5 бар** от уставки. Оператор может задать **ручной bias**.

**Выход из режима h**
Активация режима отключения КУ, подъёма давления или постоянного давления.

**Регулирование температуры БРОУ ВД**
Одноконтурное, уставка задаётся оператором.
⚠️ **Ограничение уставки: температура насыщения при текущем давлении за БРОУ + 30°C.**

⚠️ **69 бар — давление разворота турбины.** БРОУ ВД фиксируется на нём, и с него начинается разворот ПТ.

---

**🇬🇧 HP Bypass — 8 control modes**

Maintains HP header steam pressure at setpoint, **single-loop PID**.

| Mode | Activation | Pressure target |
|---|---|---|
| **a. Bypass fully closed** | After HRSG starts, auto mode | **5 bar** |
| **b. Minimum pressure** | HP main steam pressure **>5 bar** | **5 bar**, valve opens gradually |
| **c. Pressure ramp-up** | Valve opening > startup opening | Target **tracks actual pressure**, opening near constant |
| **d. Constant pressure** | Opening > startup opening **AND** main steam > **69 bar** | Fixed at **69 bar** (turbine rolling pressure) |
| **e. Sliding pressure** | After synchronization **AND load >40%** | Sliding curve, setpoint **from TCS via AO** |
| **f. Hot standby** | Synchronized **AND** valve feedback **<5%** | **Min(turbine setpoint +10 bar, rapid-opening threshold)** |
| **g. HRSG trip** | On HRSG trip | Exits when HRSG resumes |
| **h. Turbine trip without boiler shutdown** | From hot standby: turbine trip or load rejection, no HRSG trip | Valve **opens rapidly**, then auto-holds **69 bar** |

**Entering mode d**
Switches automatically when actual pressure is within **±5 bar** of target. Operator can apply a **manual bias**.

**Exiting mode h**
Activation of HRSG trip mode, pressure ramp-up mode, or constant pressure mode.

**HP bypass temperature control**
Single loop; setpoint manually configured by the operator.
⚠️ **Setpoint is constrained to the saturation temperature of the current HP bypass reduced pressure plus 30°C.**

⚠️ **69 bar is the turbine rolling pressure.** The HP bypass locks onto it, and ST roll-off starts there.

`#HPbypass #BROU #rollingpressure`

---
---

## POST 43 — IP va LP bypass

**🇺🇿 IP bypass — rejimlar va farqlar**

| Rejim | Faollashish sharti | Bosim maqsadi |
|---|---|---|
| **a. To'liq yopiq** | HRSG ishga tushgandan keyin | **1 bar** |
| **b. Minimal bosim** | IP asosiy bug' bosimi **>5 bar** | **5 bar** |
| **c. Bosim ko'tarilishi** | Klapan ochilishi > start ochilishi | Haqiqiy bosimni kuzatadi |
| **d. Doimiy bosim** | Ochilish > start **VA** bosim > **10 bar** | Qat'iy **10 bar** |
| **e. Sirpanuvchi bosim** | Sinxronizatsiya **VA yuklama >10%** | Oldindan belgilangan sirpanuvchi egri chiziq |
| **f. Issiq zaxira** | Sinxronizatsiya **VA** klapan fikri **<5%** | **Min(haqiqiy IP bosimi +5 bar, tez ochilish chegarasi)** |
| **g. HRSG trip** | HRSG trip | — |
| **h. Qozon to'xtamasdan turbina trip** | Issiq zaxiradan | Tez ochiladi, **10 bar** ni ushlaydi |

**Rejim d ga o'tish oynasi: ±2 bar** (HP da **±5 bar**).

**HP va IP orasidagi asosiy farqlar**
| | HP | IP |
|---|---|---|
| To'liq yopiq rejim maqsadi | **5 bar** | **1 bar** |
| Roll bosimi | **69 bar** | **10 bar** |
| Doimiy bosimga o'tish oynasi | **±5 bar** | **±2 bar** |
| Sirpanuvchi bosim yuklamasi | **>40%** | **>10%** |
| Issiq zaxira formulasi | setpoint **+10 bar** | haqiqiy **+5 bar** |
| Sirpanuvchi setpoint manbasi | **TCS dan AO** | oldindan belgilangan egri chiziq |

**LP bypass**
• Faqat **doimiy bosim rejimi**, bir konturli PID
• Bosim setpointi **operator tomonidan qo'lda** kiritiladi
• Harorat boshqaruvi ham bir konturli, setpoint qo'lda

⚠️ IP sirpanuvchi bosimga **10% yuklamada** o'tadi, HP esa **40%** da. Ya'ni 10–40% oralig'ida IP allaqachon sirpanuvchi, HP hali **69 bar** da qulflangan. Bu oraliqda HP bypass hali ochiq bo'lishi normal.

⚠️ LP bypass **avtomatik rejimlar zanjiriga ega emas** — bosim setpointini butunlay operator qo'yadi. Bu unutiladigan joy.

---

**🇷🇺 БРОУ СД — режимы и отличия**

| Режим | Условие | Уставка |
|---|---|---|
| **a. Полностью закрыт** | После пуска КУ | **1 бар** |
| **b. Минимальное давление** | Давление СД **>5 бар** | **5 бар** |
| **c. Подъём давления** | Открытие > пускового | Следит за фактическим |
| **d. Постоянное давление** | Открытие > пускового **И** давление > **10 бар** | **10 бар** |
| **e. Скользящее** | Синхронизация **И нагрузка >10%** | Заданная кривая |
| **f. Горячий резерв** | Синхронизация **И** обратная связь **<5%** | **Min(факт. +5 бар, порог быстрого открытия)** |
| **g/h** | Как у ВД | Держит **10 бар** |

**Окно перехода в режим d: ±2 бар** (у ВД **±5 бар**).

**Ключевые отличия ВД / СД**
Закрытый режим **5 / 1 бар** | Давление разворота **69 / 10 бар** | Окно **±5 / ±2 бар** | Скользящее с **40% / 10%** нагрузки | Горячий резерв **+10 / +5 бар** | Источник уставки **TCS / заданная кривая**

**БРОУ НД**
Только **режим постоянного давления**, одноконтурный ПИД, уставка **вручную оператором**. Регулирование температуры тоже ручной уставкой.

⚠️ СД переходит на скользящее при **10%**, ВД при **40%**. В диапазоне 10–40% СД уже скользит, а ВД ещё держит **69 бар** — открытый БРОУ ВД в этом диапазоне нормален.

⚠️ У БРОУ НД **нет автоматической цепочки режимов** — уставку задаёт только оператор. Об этом забывают.

---

**🇬🇧 IP and LP Bypass**

| Mode | Activation | Target |
|---|---|---|
| **a. Fully closed** | After HRSG starts | **1 bar** |
| **b. Minimum pressure** | IP main steam **>5 bar** | **5 bar** |
| **c. Ramp-up** | Opening > startup opening | Tracks actual |
| **d. Constant pressure** | Opening > startup **AND** pressure > **10 bar** | **10 bar** |
| **e. Sliding pressure** | Synchronized **AND load >10%** | Predefined sliding curve |
| **f. Hot standby** | Synchronized **AND** feedback **<5%** | **Min(actual IP +5 bar, rapid-opening threshold)** |
| **g/h** | As HP | Holds **10 bar** |

**Entry window into mode d: ±2 bar** (HP uses **±5 bar**).

**Key HP vs IP differences**
Closed-mode target **5 / 1 bar** | Rolling pressure **69 / 10 bar** | Entry window **±5 / ±2 bar** | Sliding from **40% / 10%** load | Hot standby **+10 / +5 bar** | Setpoint source **TCS AO / predefined curve**

**LP bypass**
**Constant-pressure mode only**, single-loop PID, setpoint **manually configured by the operator**. Temperature control likewise on a manual setpoint.

⚠️ IP goes sliding at **10%** load, HP at **40%**. Between 10 and 40% the IP is already sliding while HP is still locked at **69 bar** — an open HP bypass there is normal.

⚠️ The LP bypass has **no automatic mode chain** — the operator sets the pressure. That is the one people forget.

`#IPbypass #LPbypass #slidingpressure`

---
---

## POST 44 — EH tizimi spetsifikatsiyasi

**🇺🇿 Gidravlik boshqaruv yog' tizimi — uskuna**

**Tizim ma'lumotlari**
• O'lchamlari: 3390 W × 4050 L × 2390 H mm | Quruq og'irligi: **9200 kg**
• **Bak hajmi: 1514 litr**
• **Suyuqlik: Triaryl-fosfat efir** (yong'inga chidamli)
• Nasoslar: **o'zgaruvchan ish hajmli porshenli**
• Dvigatellar: **55 kW**, 3 faza
• Akkumulyatorlar: **porshenli**
• **Tizim loyihaviy bosimi: 207 bar(g)**
• **Tizim ish bosimi: 165 bar(g)**
• Sovutgich: **yog'-havo**
• Filtrlash: **3 mikron** bosim filtrlari

**HCFP — gidravlik boshqaruv suyuqlik nasosi**
Turi **A10VSO 32-B** | Aylanish **soat yo'nalishi** (yetakchi valdan qarab)
**Nominal bosim: 140 bar** | **Maksimal bosim: 160 bar**

**HCFM — dvigatel**
HLP | Sovutish **IC411(FC)** | 50 Hz | Izolyatsiya **F** | **400 V**
Tok **99.8 A**, qulflangan rotor **650%** | Tezlik **1482 rpm** | FIK **94.6%**

**HCCP — sovutish konturi nasosi**
PGH5-3X080RE11VE4 | O'lcham 80 | **Sarf 116.9 l/min** | 1450 rpm | **P = 10 bar**

**HCCM — dvigatel**
Tok **13.0 A** | 1460 rpm | FIK **89.6%** | **5 kW** | 400 V

**TAFP — o'tkazish va filtrlash nasosi**
PGF-V | 1450 rpm | **10 bar** | **Sarf 7.2 L/min**

**TAFM — dvigatel**
Tok **1.9 A** | 1460 rpm | FIK **82.5%** | **0.75 kW**

**Boshqaruv strategiyasi**
Bitta nasos ishda, ikkinchisi zaxirada. **Ishlayotgan nasos trip bo'lsa YOKI kollektor bosimi past alarm setpointiga yetsa — zaxira nasos avto ishga tushadi.**

⚠️ **Nasosning nominal bosimi 140 bar, maksimal 160 bar, tizim ish bosimi esa 165 bar(g).** Ya'ni tizim nasosning maksimal bosimidan yuqorida ishlaydi — bu akkumulyatorlar hisobiga. Akkumulyator azoti tushsa bosim ushlanmaydi, lekin nasos ayibdor emas.

⚠️ Suyuqlik **fosfat efir** — mineral yog' EMAS. Aralashtirish taqiqlanadi, uskunalar va zichlashlar boshqacha.

---

**🇷🇺 Система ОГ — оборудование**

**Данные системы**
• Габариты 3390 × 4050 × 2390 мм | Сухой вес **9200 кг**
• **Объём бака: 1514 л** | **Жидкость: триарилфосфат** (огнестойкая)
• Насосы: **аксиально-поршневые регулируемые** | Двигатели **55 кВт**, 3 фазы
• Гидроаккумуляторы **поршневые**
• **Расчётное давление 207 бар(g)** | **Рабочее 165 бар(g)**
• Охладитель **масло-воздух** | Фильтрация **3 мкм**

**HCFP** A10VSO 32-B, вращение **по часовой**, **номинал 140 бар**, **максимум 160 бар**
**HCFM** HLP, IC411(FC), 50 Гц, **F**, **400 В**, **99.8 А**, пуск **650%**, **1482 об/мин**, КПД **94.6%**
**HCCP** PGH5-3X080RE11VE4, размер 80, **116.9 л/мин**, 1450 об/мин, **10 бар**
**HCCM** **13.0 А**, 1460 об/мин, КПД **89.6%**, **5 кВт**
**TAFP** PGF-V, 1450 об/мин, **10 бар**, **7.2 л/мин**
**TAFM** **1.9 А**, 1460 об/мин, КПД **82.5%**, **0.75 кВт**

**Стратегия управления**
Один насос в работе, второй в резерве. **Автопуск резервного при отключении рабочего ИЛИ при достижении уставки низкого давления в коллекторе.**

⚠️ **Номинал насоса 140 бар, максимум 160, а рабочее давление системы 165 бар(g).** Система работает выше максимума насоса — за счёт гидроаккумуляторов. Просел азот — давление не держится, насос ни при чём.

⚠️ Жидкость — **фосфатный эфир**, НЕ минеральное масло. Смешивание запрещено, уплотнения и оснастка другие.

---

**🇬🇧 EH Control Oil System — equipment**

**System data**
• Size 3390 W × 4050 L × 2390 H mm | Dry weight **9200 kg**
• **Reservoir volume: 1514 litre** | **Fluid: triaryl-phosphate ester** (fire resistant)
• Pumps: **variable displacement piston** | Motors: **55 kW**, 3-phase
• Accumulators: **piston type**
• **System design pressure 207 bar(g)** | **System operating pressure 165 bar(g)**
• Cooler: **oil-air** | Filtration: **3-micron** pressure filters

**HCFP** A10VSO 32-B, **clockwise** viewed on drive shaft, **nominal 140 bar**, **maximum 160 bar**
**HCFM** HLP, IC411(FC), 50 Hz, class **F**, **400 V**, **99.8 A**, locked-rotor **650%**, **1482 rpm**, **94.6%**
**HCCP** PGH5-3X080RE11VE4, size 80, **116.9 l/min**, 1450 rpm, **10 bar**
**HCCM** **13.0 A**, 1460 rpm, **89.6%**, **5 kW**
**TAFP** PGF-V, 1450 rpm, **10 bar**, **7.2 L/min**
**TAFM** **1.9 A**, 1460 rpm, **82.5%**, **0.75 kW**

**Control strategy**
One pump running, the other on standby. **The standby auto-starts when the running pump trips OR header pressure reaches the low alarm setpoint.**

⚠️ **Pump nominal is 140 bar, maximum 160 bar, yet system operating pressure is 165 bar(g).** The system runs above pump maximum — the accumulators carry it. Lose accumulator nitrogen and pressure won't hold; the pump isn't at fault.

⚠️ The fluid is **phosphate ester**, NOT mineral oil. No mixing; seals and handling equipment are different.

`#EHoil #phosphateester #accumulator`

---
---

## POST 45 — Lube oil va jacking oil uskunalari

**🇺🇿 Yog' nasoslari — aniq ko'rsatkichlar**

**AC lube oil nasos (MOP) — 10MAV23/24AP001**
• Suyuqlik: **VG32** | **Sarf: 7585 L/min**
• Nasos harorati: **27–70°C** | **Chiqish bosimi: 5.5 bar.g**
• FIK: **61.2%** | Nominal quvvat: **113.3 kW** | Tezlik: **1450 rpm**
• Aylanish: **CW** (yetakchidan qaraganda)
• Dvigatel: **132 kW**, **400 V**, **to'liq yuklama toki 232.6 A**
• Qulflangan rotor toki: **650%** | FIK 100% yuklamada: **94.7%** | **IP55**

**DC lube oil nasos (EBOP) — 10MAV27AP001**
• Suyuqlik: **VG32** | **Sarf: 5272 L/min**
• Nasos harorati: **27–70°C** | **Chiqish bosimi: 3.0 bar.g**
• FIK: **58.8%** | Nominal quvvat: **44.7 kW** | Tezlik: **1450 rpm**
• Dvigatel: **55 kW**, **220 V DC**, **1500 rpm**, **IP54**
• **Nominal tok: 284 A** | Izolyatsiya: **F**

**Vapor extractor — 10MAV76/77AN401**
Quvvat: **17.6 m³/min**

**Jacking oil (3.13)**
• **So'rish bosimi: ~0.15 MPa** — lube oil filtridan keyingi yog', kavitatsiyaga qarshi
• **Kollektor bosimi: ~15.0 MPa**
• Yog' droselli klapan va check valve orqali podshipniklarga boradi
• **Droselni sozlash orqali** har bir podshipnikga sarf va bosim boshqariladi
• Nasoslar: **2 × 100%**, yuqori bosimli **o'zgaruvchan** nasoslar, umumiy kollektor
• Zaxira ishga tushirish: **PIT 10MAV10CP002A/B**
• **Nasos rotorni turbogenerator tezligi ~400 rpm dan past bo'lganda ko'taradi**
• **So'rish filtri: duplex, 50 mikron**, bir elementi doim ishda, Δp **PDIT-03** bilan kuzatiladi
• Filtr tiqilsa operator **qo'lda ikkinchi tomonga o'tkaza oladi**

⚠️ **DC nasosning chiqish bosimi 3.0 bar.g, AC niki 5.5 bar.g.** EBOP kirganda kollektor bosimi tabiiy ravishda pastroq bo'ladi — bu nosozlik emas.

⚠️ **DC nasos toki 284 A, 220 V.** Akkumulyator batareyasi shu tokni ushlab tura olishini bilish kerak — EBOP ishlashi butunlay batareyaga bog'liq.

⚠️ **Jacking oil bosim ~15.0 MPa = 150 bar**, alarm esa **60 bar**. Ish oralig'i ishga tushirishda **100–150 bar** (Step 35).

---

**🇷🇺 Масляные насосы — точные данные**

**МНС переменного тока 10MAV23/24AP001**
**VG32** | **7585 л/мин** | **27–70°C** | **5.5 бар.g** | КПД **61.2%** | **113.3 кВт** | **1450 об/мин** | **CW**
Двигатель **132 кВт**, **400 В**, **232.6 А**, пуск **650%**, КПД **94.7%**, **IP55**

**АМН постоянного тока 10MAV27AP001**
**VG32** | **5272 л/мин** | **27–70°C** | **3.0 бар.g** | КПД **58.8%** | **44.7 кВт** | **1450 об/мин**
Двигатель **55 кВт**, **220 В DC**, **1500 об/мин**, **IP54**, **284 А**, изоляция **F**

**Эксгаустеры 10MAV76/77AN401** — **17.6 м³/мин**

**Гидроподъём**
• **Давление на всасе ~0.15 МПа** (масло после фильтра смазки, против кавитации)
• **Давление в коллекторе ~15.0 МПа**
• Через дроссель и обратный клапан к подшипникам; **дросселем регулируют** расход и давление на каждый подшипник
• Насосы **2 × 100%**, высоконапорные **регулируемые**, общий коллектор
• Автопуск резервного по **PIT 10MAV10CP002A/B**
• **Работают, пока обороты ниже ~400 об/мин**
• **Фильтр на всасе: сдвоенный, 50 мкм**, Δp по **PDIT-03**, переключение **вручную**

⚠️ **Напор АМН 3.0 бар.g против 5.5 у МНС.** При работе АМН давление в коллекторе закономерно ниже — это не дефект.

⚠️ **Ток АМН 284 А при 220 В.** Работа АМН полностью зависит от аккумуляторной батареи.

⚠️ **Гидроподъём ~15.0 МПа = 150 бар**, сигнал на **60 бар**, при пуске рабочий диапазон **100–150 бар**.

---

**🇬🇧 Oil Pumps — hard numbers**

**AC lube oil pump (MOP) 10MAV23/24AP001**
**VG32** | **7585 L/min** | **27–70°C** | **5.5 barg** | Efficiency **61.2%** | **113.3 kW** | **1450 rpm** | **CW**
Motor **132 kW**, **400 V**, full load **232.6 A**, locked rotor **650%**, efficiency **94.7%**, **IP55**

**DC lube oil pump (EBOP) 10MAV27AP001**
**VG32** | **5272 L/min** | **27–70°C** | **3.0 barg** | Efficiency **58.8%** | **44.7 kW** | **1450 rpm**
Motor **55 kW**, **220 V DC**, **1500 rpm**, **IP54**, rated **284 A**, insulation **F**

**Vapor extractors 10MAV76/77AN401** — **17.6 m³/min**

**Jacking oil**
• **Suction pressure ~0.15 MPa** — oil taken after the lube oil filter, preventing pump cavitation
• **Header pressure ~15.0 MPa**
• Pressure oil passes a throttle valve and check valve to each bearing; **adjusting the throttle** sets flow and pressure per bearing
• Pumps: **2 × 100%** high-pressure **variable** pumps on a common header
• Standby start from **PIT 10MAV10CP002A/B**
• **Runs while turbine generator speed is below approx. 400 rpm**
• **Suction filter: duplex, 50 micron**, one element always in service, Δp on **PDIT-03**, **manual** changeover

⚠️ **EBOP discharge is 3.0 barg against 5.5 barg for the MOPs.** Header pressure is legitimately lower on EBOP — not a fault.

⚠️ **EBOP draws 284 A at 220 V DC.** Its availability rests entirely on the battery.

⚠️ **Jacking oil header ~15.0 MPa = 150 bar**, alarm at **60 bar**, start-up working range **100–150 bar**.

`#luboil #jackingoil #pumpdata`

---
---

## POST 46 — Turning gear va forced cooling uskunasi

**🇺🇿 Turning gear — spetsifikatsiya**

**Dvigatel**
• Kuchlanish: **400 V AC** | Quvvat: **27.6 kW**
• **Nominal tok: 125 A** | 50 Hz
• Tezlik: **1470 rpm** | **Moment: 179.3 Nm**

**Reduktor**
• **Nisbat: 220.7**

**Tishli g'ildirak (ring gear)**
• **Tishlar soni: 248** | **Normal modul: 5.0 mm**
• **Tip diametri: 1240 mm**
• **Normal backlash: 0.4–0.5 mm**
• **Nominal tezlik: 6.66 rpm**
• **Nominal moment: 63 350 Nm** | **Maksimal moment: 68 859 Nm**

**Yog'**
• Turi: **ISO VG32** | Harorat: **35–60°C**
• Bosim: **1–2 bar(g)** | **Sarf talabi: 30 l/min**

**Joylashuvi va bloklash**
LP old pedestal tepasida, LP rotorining tishli g'ildiragiga **shesternya** bilan tishlashadi. AC dvigatel, **qo'lda ishlatish imkoniyati** bor. Moylash **bevosita lube oil tizimidan**.
⚠️ **Bosim relesi turning gear ichidagi yog' bosimini o'lchaydi va dvigatel starter zanjirini blokirovkalaydi** — yetarli yog' bo'lmasa turning gear ishga tushmaydi.

**Forced cooling havo qizdirgichi (3.15.4.1)**
• Kuchlanish: **AC 400 V** | **Qizdirish quvvati: 30 kW**
• **Kirish harorati: 5°C** | **Chiqish harorati: 150°C**
• **Ish bosimi: 7.5 bar.g**

Majburiy sovutish tabiiy sovutishga nisbatan sovutish muddatini **1–2 kunga** qisqartiradi.
Qizdirgichni ishlatish HP va IP rotorlari **400°C dan past** bo'lganda mumkin.

⚠️ **Nominal turning gear tezligi 6.66 rpm**, avariya protsedurasida esa **7 rpm/min** deb tekshiriladi (Step 7) va Step 35 da **~7 rpm** deyilgan. Manualda birlik ikki xil yozilgan — amalda **~7 aylanish/daqiqa**.

⚠️ **Backlash 0.4–0.5 mm.** Turning gear shovqini o'zgargan bo'lsa, birinchi shu tekshiriladi. Nominal moment 63 350 Nm, maksimal 68 859 — orasi atigi **8.7%**. Rotor qotib qolgan bo'lsa turning gear uni zo'rlab aylantira olmaydi.

---

**🇷🇺 ВПУ — спецификация**

**Двигатель** **400 В AC**, **27.6 кВт**, **125 А**, 50 Гц, **1470 об/мин**, **момент 179.3 Н·м**
**Редуктор** — **передаточное 220.7**
**Зубчатый венец** — **248 зубьев**, модуль **5.0 мм**, диаметр вершин **1240 мм**, **боковой зазор 0.4–0.5 мм**, **6.66 об/мин**, **момент 63 350 Н·м**, **максимум 68 859 Н·м**
**Масло** **ISO VG32**, **35–60°C**, **1–2 бар(g)**, **30 л/мин**

Расположено на верху переднего стула ЦНД, шестерня входит в венец ротора ЦНД. Смазка **напрямую из маслосистемы**.
⚠️ **Реле давления в ВПУ блокирует цепь пускателя** — без масла ВПУ не запустится.

**Воздухоподогреватель расхолаживания** — **AC 400 В**, **30 кВт**, вход **5°C**, выход **150°C**, **7.5 бар.g**
Принудительное расхолаживание сокращает время на **1–2 суток**. Работа подогревателя возможна при роторах ЦВД и ЦСД **ниже 400°C**.

⚠️ Номинал ВПУ **6.66 об/мин**, в аварийной процедуре проверяют **7 об/мин** — в руководстве единицы записаны по-разному, фактически **~7 оборотов в минуту**.

⚠️ **Боковой зазор 0.4–0.5 мм** — первое, что проверяют при изменении шума ВПУ. Между номинальным и максимальным моментом всего **8.7%**: заклиненный ротор ВПУ не провернёт.

---

**🇬🇧 Turning Gear and Forced Cooling — specification**

**Motor** **400 V AC**, **27.6 kW**, **125 A**, 50 Hz, **1470 rpm**, **torque 179.3 Nm**
**Gearbox** ratio **220.7**
**Ring gear** — **248 teeth**, normal module **5.0 mm**, tip diameter **1240 mm**, **normal backlash 0.4–0.5 mm**, nominal speed **6.66 rpm**, **nominal torque 63,350 Nm**, **maximum 68,859 Nm**
**Lube oil** **ISO VG32**, **35–60°C**, **1–2 bar(g)**, **30 l/min**

Mounted on top of the LP front pedestal, pinion meshing into the cogged wheel on the LP rotor. Lubrication **directly from the lube oil system**.
⚠️ **A pressure switch senses oil pressure within the turning gear and interlocks the motor starter circuit** — no adequate oil, no turning gear.

**Forced cooling air heater** — **AC 400 V**, **30 kW**, inlet **5°C**, outlet **150°C**, working pressure **7.5 barg**
Forced cooling cuts cooling time by **about 1 to 2 days** versus natural cooling. Heater operation is possible with HP and IP rotors **below 400°C**.

⚠️ Nominal turning gear speed is **6.66 rpm**, while the emergency procedure checks **7 rpm/min** — the manual writes the unit two ways; in practice it's **~7 revolutions per minute**.

⚠️ **Backlash 0.4–0.5 mm** is the first check when turning gear noise changes. Nominal to maximum torque is only **8.7%** apart — a locked rotor will not be forced round by the turning gear.

`#turninggear #ringgear #forcedcooling`

---
---

## POST 47 — Rotor prewarming: mo'rtlik chegarasi

**🇺🇿 Nima uchun prewarming majburiy — mo'rt-plastik o'tish harorati**

Manual buni ochiq yozadi. Prewarming 3 sababga ko'ra muhim:

**1. Siklik resurs sarfi**
Rotor va korpus yuzalarining siklik resurs sarfi **kamayadi**, chunki qizdirish yumshoqroq o'tkinchi jarayonlar bilan amalga oshiriladi.

**2. Bore dagi termik kuchlanish**
Bore ni asta qizdirish orqali termik kuchlanish kamayadi, natijada **bore dagi termik va markazdan qochma kuchlanishlarning yig'indisi ortiqcha bo'lmaydi**.

**3. Mo'rt-plastik o'tish harorati (eng muhimi)**
Rotor va korpuslar **o'tish haroratidan yuqori** bo'lishi uchun qizdiriladi.

⚠️ **O'tish harorati — bu material undan pastda MO'RT, undan yuqorida chidamli va plastik bo'ladigan harorat.** Undan yuqorida material mumkin bo'lgan defektlarga ancha bardoshli va termik hamda markazdan qochma kuchlanishlarni ancha yaxshi ko'taradi.

**Aniq raqamlar**
• **Zamonaviy yuqori haroratli rotorlar uchun boshlang'ich o'tish harorati: 90–120°C**
• Ba'zi eski rotorlarda o'tish harorati **ancha yuqori** bo'lgan
• ⚠️ **Barcha rotorlar vaqt o'tishi bilan mo'rtlashadi — o'tish harorati xizmat muddati davomida OSHIB boradi.** Shuning uchun eski birliklar prewarming ga **ko'proq e'tibor** talab qiladi

**Mo'rt rotor portlashi**
Rotor portlamasdan ko'tara oladigan **bore yorig'ining o'lchami** uning **harorati va kuchlanish darajasi** bilan aniqlanadi, ayniqsa bore yaqinida. Aynan shu sababdan ishga tushirish yo'riqnomasi prewarming protsedurasini va **Bore Stress Limit** ni cheklashni belgilaydi.

**Cold start ta'rifi**
Turbina bir necha kun ishdan chiqqan, rotor harorati **xona haroratiga yaqin**, ya'ni **mo'rt-plastik o'tish haroratidan ancha past**.

**Tavsiya etilgan prewarming — bu MINIMUM**
Bu daraja portlash ehtimolini minimallashtiradi, **agar oldingi o'tkinchi jarayonlarda Bore Stress Limit oshib ketmagan bo'lsa**. Tavsiya etilgandan **yuqoriroq** qizdirish mo'rt portlashga qarshi **qo'shimcha zaxira** beradi.

**Maqsad haroratlar (3.16.3)**
• **HP prewarming maqsadi: 150°C**
• **IP prewarming maqsadi: 55°C**
• Bosim berish **rotor bore harorati 150°C dan past bo'lganda** ishlatilishi kerak

**RFV va HSPV farqi**
• **RFV** — qizdiruvchi bug'ni HP exhaust bo'limiga yo'naltiradi, tezroq qizdirish uchun afzal joy
• **HSPV** — yordamchi qozon bug'idan foydalanadi. **Asosiy bug' generatori va bypass tizimi tayyor bo'lmasa ham prewarming mumkin**
• ⚠️ **Prewarming davomida ruxsat etilgan aylanish tezligi <200 rpm.** Birinchi kritik tezlikdan past tezliklarda aylantirish packing ishqalanishi tufayli rotorning egilishiga sabab bo'ladi, **ayniqsa yangi packing bilan**

---

**🇷🇺 Почему прогрев обязателен — температура хрупко-вязкого перехода**

Руководство называет три причины:

**1. Расход циклического ресурса**
Снижается за счёт более плавных переходных режимов.

**2. Термонапряжения в расточке**
Постепенный прогрев расточки снижает термонапряжения, **сумма термических и центробежных напряжений в расточке не становится чрезмерной**.

**3. Температура хрупко-вязкого перехода (главное)**

⚠️ **Ниже этой температуры материал ХРУПКИЙ, выше — вязкий и пластичный**, гораздо терпимее к возможным дефектам и намного лучше держит термические и центробежные напряжения.

**Конкретика**
• **Для современных высокотемпературных роторов начальная температура перехода 90–120°C**
• У ряда старых роторов она была **существенно выше**
• ⚠️ **Все роторы охрупчиваются со временем — температура перехода РАСТЁТ в процессе эксплуатации.** Старым блокам нужен **более тщательный** прогрев

**Хрупкое разрушение ротора**
Размер трещины в расточке, который ротор выдержит без разрушения, определяется его **температурой и уровнем напряжений**. Отсюда и требование прогрева, и ограничение **Bore Stress Limit**.

**Что такое холодный пуск**
Турбина простояла несколько суток, температура ротора **близка к комнатной**, то есть **намного ниже температуры перехода**.

**Рекомендуемый прогрев — это МИНИМУМ**
Он минимизирует вероятность разрушения **при условии, что Bore Stress Limit не был превышен в предшествующих режимах**. Прогрев **выше** рекомендованного даёт **дополнительный запас**.

**Целевые температуры**
**ЦВД: 150°C** | **ЦСД: 55°C** | Наддув применяют при температуре расточки **ниже 150°C**

**RFV и HSPV**
• **RFV** направляет пар в выхлопную часть ЦВД — предпочтительное место для быстрого прогрева
• **HSPV** использует пар вспомогательного котла: **прогрев возможен, даже когда основной парогенератор и БРОУ не готовы**
• ⚠️ **Допустимые обороты при прогреве <200 об/мин.** Разворот ниже первой критической даёт изгиб ротора от задеваний, **особенно с новыми уплотнениями**

---

**🇬🇧 Why Prewarming Is Mandatory — the transition temperature**

The manual gives three reasons:

**1. Cyclic life expenditure**
Rotor and shell surface life expenditure is **reduced** because warming happens through more gradual transients.

**2. Thermal stress at the bore**
Gradual bore-warming reduces thermal stress so that **combined thermal and centrifugal stresses at the bore will not be excessive**.

**3. The transition temperature (the important one)**

⚠️ **The transition temperature is that below which the material is brittle, and above which it is tough and ductile** — much more tolerant of possible defects and much better able to withstand thermal and centrifugal stresses.

**Actual numbers**
• **For most modern high temperature rotors, initial transition temperature is 90–120°C**
• Some older rotors had **considerably higher** transition temperatures
• ⚠️ **All rotors experience some embrittlement — the transition temperature INCREASES with time in service.** Older units require **even more attention** to prewarming

**Brittle rotor burst**
The size of a bore crack a rotor can tolerate without bursting is determined by its **temperature and stress level**, particularly near the bore. That is why the instructions define both a prewarming procedure and a **Bore Stress Limit**.

**Definition of a cold start**
Made after the turbine has been out of service for several days so rotor temperature is **near room temperature, well below the brittle-to-ductile transition temperature**.

**The recommended prewarming is the MINIMUM**
It minimizes burst probability **provided the Bore Stress Limit has not been exceeded during preceding transients**. Prewarming **higher** than recommended provides **additional margin** against brittle bursting.

**Target temperatures**
**HP: 150°C** | **IP: 55°C** | Pressurization should be used whenever rotor bore temperature is **below 150°C**

**RFV vs HSPV**
• **RFV** directs warming steam to the HP exhaust section — the preferred location for faster warming
• **HSPV** uses auxiliary boiler steam: **prewarming is possible even when the main steam generator and bypass system are not prepared**
• ⚠️ **Allowable turbine rolling speed during preheating is below 200 rpm.** Rolling below first critical causes rotor bowing from packing rubs, **especially with new packing**

`#prewarming #brittlefracture #borestress`

---
---

## POST 48 — Seal oil bosim kaskadi

**🇺🇿 Seal oil — bosimlar zanjiri va qaytish yo'li**

**Normal ishda oqim yo'li**
Seal oil **lube oil kollektoridan** ta'minlanadi → **duplex strainer 10MKW18AT001** → **vakuum bak 10MKW10BB101**

**Bosimlar**
• Lube oil tizimidan keladigan yog' bosimi: **1.7 bar.g**
• Float trap dagi drenaj yog'i bosimi: **0.3 bar.g**
• Shu sababli check valve **10MKW18AA002, 003** ning **yuqori tomonida 0.3 bar.g**, **o'ng tomonida 1.7 bar.g** bo'ladi → **check valve YOPILADI**
• Lube oil o'ng tomon orqali vakuum bakka oqadi
• **BDE (Bearing Drain Enlargement)** va float trap uchun statik napor: **~0.14 bar.g** → float trap dan drenajlangan yog' **BDE ga qaytadi**

**Qaytish sikli**
Seal oil **BDE orqali turbina lube oil tizimiga qaytadi** → **turbina lube oil sovutgichida sovitiladi** → yana vakuum bakka beriladi.
Vakuum bakka oqim **bakning vakuumi bilan yordamlashadi**. Seal oil bakning **pastidan** kiradi, avval ichkaridagi **float valve 10MKW18AA103** orqali, keyin spray orqali.

**Suyuqlik detektori (10MKW21BZ001)**
SODE uchun. **Seal oil drain enlargement dagi sath ko'tarilishidan** ogohlantiradi — bu yog'ning **generator korpusiga qaytib kirishiga** olib kelishi mumkin.
Detektor — **float switch uzeli**, ko'rish oynasi, drenaj liniyasi va sinov uchun to'ldirish ulanishi bilan.
⚠️ **Suyuqlik detektori TCMS ga yuqori alarm bersa — operator BIRINCHI NAVBATDA float trap ni tekshirishi kerak.**

**H2 tomoni seal oil sarfini o'lchash**
**25.4 mm (1 dyuym) sath ko'tarilish vaqti** o'lchanadi → natija **H2 tomoni seal oil sarfini (litr/daqiqa)** beradi.

**Uskuna (4.1.3)**
| Uskuna | KKS | Ma'lumot |
|---|---|---|
| Vakuum bak | 10MKW10BB001 | Gorizontal silindrik, 1×100%, **4.92 m³** |
| MSOP A/B | 10MKW03AP001/002 | Positive screw, 2×100%, **40.6 m³/s**, **Δp 9.8 bar**, **18.5 kW** |
| ESOP | 10MKW19AP001 | Positive screw, 1×100%, **38.12 m³/s**, **Δp 9.8 bar**, **15 kW** |
| Retsirkulyatsiya nasosi | 10MKW04AP001 | Positive screw, 1×100%, **44.0 m³/s**, **Δp 2.7 bar**, **7.5 kW** |
| Vakuum nasos | 10MKW01AP001 | **Rotary vane** |

⚠️ **Retsirkulyatsiya nasosining sarfi (44.0) MSOP dan (40.6) YUQORI**, lekin bosimi ancha past (2.7 vs 9.8 bar). Bu ikki xil vazifa — chalkashtirmang.

⚠️ Bosim kaskadi **1.7 → 0.3 → 0.14 bar.g**. Bu farqlar check valve va float trap ishlashini belgilaydi. **Lube oil kollektor bosimi 1.5 bar.g ga tushsa** (alarm chegarasi) bu kaskad buziladi.

---

**🇷🇺 Уплотняющее масло — каскад давлений и путь возврата**

**Путь в нормальном режиме**
Из **коллектора смазки** → **сдвоенный фильтр 10MKW18AT001** → **вакуумный бак 10MKW10BB101**

**Давления**
• Масло из системы смазки: **1.7 бар.g**
• Дренажное масло на поплавковом конденсатоотводчике: **0.3 бар.g**
• Поэтому на обратных клапанах **10MKW18AA002, 003** сверху **0.3 бар.g**, справа **1.7 бар.g** → **клапаны ЗАКРЫВАЮТСЯ**
• Статический напор для **BDE** и поплавкового отводчика: **~0.14 бар.g** → дренаж **возвращается в BDE**

**Цикл возврата**
Уплотняющее масло **возвращается в маслосистему турбины через BDE** → **охлаждается турбинным маслоохладителем** → снова в вакуумный бак. Поток поддерживается **разрежением в баке**. Вход **снизу бака**, через внутренний **поплавковый клапан 10MKW18AA103**, затем через распылитель.

**Детектор жидкости 10MKW21BZ001**
Предупреждает о росте уровня в дренажном расширителе, что может привести к **забросу масла в корпус генератора**. Поплавковый выключатель со смотровым стеклом, дренажом и штуцером для проверки.
⚠️ **При сигнале в TCMS оператор ПЕРВЫМ ДЕЛОМ проверяет поплавковый конденсатоотводчик.**

**Замер расхода масла со стороны H2**
Замеряется **время подъёма уровня на 25.4 мм (1 дюйм)** → даёт **расход масла со стороны H2 в л/мин**.

**Оборудование**
Вакуумный бак **4.92 м³** | ОНУМ A/B винтовые 2×100%, **40.6 м³/ч**, **Δp 9.8 бар**, **18.5 кВт** | АНУМ **38.12 м³/ч**, **9.8 бар**, **15 кВт** | Рециркуляционный **44.0 м³/ч**, **2.7 бар**, **7.5 кВт** | Вакуумный насос **пластинчато-роторный**

⚠️ Расход рециркуляционного (44.0) **выше** ОНУМ (40.6), но напор много ниже. Разные задачи.

⚠️ Каскад **1.7 → 0.3 → 0.14 бар.g** определяет работу обратных клапанов и отводчика. **Падение коллектора смазки до 1.5 бар.g** этот каскад ломает.

---

**🇬🇧 Seal Oil — pressure cascade and return path**

**Normal flow path**
Seal oil is supplied by the **lube oil header** → **duplex strainer 10MKW18AT001** → **vacuum tank 10MKW10BB101**

**Pressures**
• Oil from the lube oil system: **1.7 barg**
• Drain oil at the float trap: **0.3 barg**
• So check valves **10MKW18AA002, 003** see **0.3 barg** on the upside and **1.7 barg** on the right side → the check valves **CLOSE**
• Static head for the **BDE (Bearing Drain Enlargement)** and float trap is approx. **0.14 barg** → oil drained from the float trap **returns to BDE**

**Return cycle**
Seal oil **returns to the turbine lube oil system via BDE** → **cooled by the turbine lube oil cooler** → supplied to the vacuum tank again. Flow into the tank is **aided by the tank vacuum**. Seal oil enters at the **bottom of the vacuum tank**, first through internal **float valve 10MKW18AA103**, then through a spray.

**Liquid detector (10MKW21BZ001)**
Warns of an increasing level in the seal oil drain enlargement which could lead to **oil backing up into the generator casing**. It is a float switch assembly with sight glass, drain line and a filler connection for testing.
⚠️ **If the liquid detector gives a high alarm to TCMS, the operator must check the float trap FIRST.**

**Measuring H2-side seal oil flow**
The **measured rise time for a 25.4 mm (1 inch) level rise** gives the **H2 side seal oil flow rate in litre/min**.

**Equipment**
Vacuum tank **4.92 m³** | MSOP A/B positive screw 2×100%, **40.6 m³/h**, **Δp 9.8 bar**, **18.5 kW** | ESOP **38.12 m³/h**, **9.8 bar**, **15 kW** | Recirculation pump **44.0 m³/h**, **2.7 bar**, **7.5 kW** | Vacuum pump **rotary vane**

⚠️ The recirculation pump flow (44.0) is **higher** than the MSOPs (40.6) but at far lower head. Different jobs.

⚠️ The cascade **1.7 → 0.3 → 0.14 barg** is what makes the check valves and float trap work. **Lube oil header falling to 1.5 barg** breaks it.

`#sealoil #BDE #floattrap #pressurecascade`

---
---

## POST 49 — Stator sovutish suvi uskunasi

**🇺🇿 Stator suvi — uskuna va loyihaviy qiymatlar**

**Loyihaviy ma'lumotlar (1.2.2.5)**
• **Stator o'rami orqali sarf: 63.6 m³/s**
• Stator o'rami bulk suv kirish harorati, min–maks / alarm: **30–46°C / 48°C**
• **Stator o'rami bo'ylab bosim tushishi: 1.94 bard** (= 28.07 psid)
• **Kutilgan stator o'rami kirish bosimi: 2.49 bar.g** (= 36.07 psig)
• Chiqish yuqori harorat alarm / run back: **78.0 / 83.0°C**
• Kirish past sarf alarm / run back: **57.2 / 54.2 m³/s**
• Kirish past bosim alarm / run back: **past sarfdagi ish bosimini o'qing**

**Uskuna (4.3.3)**
| Uskuna | KKS | Ma'lumot |
|---|---|---|
| Bak | 10MKF01BB001 | Gorizontal silindrik, 1×100%, **3.1 m³**, **zanglamaydigan po'lat** |
| Nasos | 10MKF02/03AP001 | Gorizontal markazdan qochma, 2×100%, **130.13 m³/s**, **chiqish 6.9 bar.g**, **45 kW** |
| Sovutgich | 10MKF06/07AC001 | Plastinali, 2×100%, **SCW sarfi 99.9 m³/s**, **SCW 77.1 → 46.0°C**, **CCW kirish 35.0°C** |
| Asosiy filtr | 10MKF09AT001 | Vertikal, **99.9 m³/s**, **3 mikron**, paxta-viskoza, **filtr uchun 26 dona** |
| Make-up filtr | 10MKF10AT001 | Vertikal, **22.7 m³/s**, **3 mikron**, **6 dona** |
| Deionizator | 10MKF10AW001 | Vertikal, **22.7 m³/s**, **smola 566 litr** |

**Smola haqida**
⚠️ Smola — **sarflanadigan material**, muddati tugasa almashtiriladi. Ishlab chiqaruvchi tavsiya qilgan **loyihaviy muddat ~2 yil**. **Smolani ishlab turgan holda, to'xtatmasdan almashtirish mumkin.**

**Make-up yo'li**
Make-up suv liniyasi **avval yuviladi**, keyin barcha make-up suv **filtr va deionizatordan o'tib** stator o'rami sovutish suvi bakiga kiradi.

**Ishga tushirish ruxsati (4.3.5.1)**
☑ Stator o'rami sovutish suvi bakida sath past emas (**10MKF01CL101**)

**Zaxira nasos avto-ishga tushishi (4.3.5.2)**
Stator sovutish nasosi A yoki B **chiqish bosimi past** (nasos nosozligi yoki dvigatel trip)

⚠️ **Nasos sarfi 130.13 m³/s, lekin o'ram orqali faqat 63.6 m³/s** o'tadi. Farq — retsirkulyatsiya va deionizator konturi. Ya'ni nasos sarfi tushmasa ham **o'ram sarfi tushishi mumkin**.

⚠️ **Sovutgichda SCW kirishi 77.1°C.** Bu chiqish alarmi (78.2°C) ga juda yaqin — loyihaviy holatda ham zaxira **1.1°C**. CCW harorati 35°C dan oshsa bu zaxira darhol yo'qoladi.

---

**🇷🇺 Статорная вода — оборудование и проектные данные**

**Проектные данные**
• **Расход через обмотку: 63.6 м³/ч**
• Температура на входе мин–макс / сигнал: **30–46°C / 48°C**
• **Потеря давления в обмотке: 1.94 бар** • **Давление на входе: 2.49 бар.g**
• Выход, сигнал / разгрузка: **78.0 / 83.0°C**
• Расход, сигнал / разгрузка: **57.2 / 54.2 м³/ч**

**Оборудование**
Бак **3.1 м³**, нержавеющая сталь | Насосы 2×100%, **130.13 м³/ч**, **6.9 бар.g**, **45 кВт** | Охладители пластинчатые 2×100%, **99.9 м³/ч**, **77.1 → 46.0°C**, вход ЗКОС **35.0°C** | Основной фильтр **99.9 м³/ч**, **3 мкм**, **26 элементов** | Фильтр подпитки **22.7 м³/ч**, **3 мкм**, **6 элементов** | Деионизатор **22.7 м³/ч**, **смола 566 л**

⚠️ Смола — **расходный материал**, проектный срок **~2 года**, **меняется без останова блока**.

**Разрешение на пуск** — уровень в баке не низкий (**10MKF01CL101**)
**Автопуск резервного** — низкое давление на нагнетании насоса A или B

⚠️ **Насос даёт 130.13 м³/ч, а через обмотку идёт только 63.6 м³/ч.** Разница — рециркуляция и контур деионизатора. Расход насоса может быть в норме, а **расход через обмотку упасть**.

⚠️ **Вход в охладитель 77.1°C** при сигнале на выходе **78.2°C** — проектный запас всего **1.1°C**. При воде ЗКОС выше 35°C запас исчезает.

---

**🇬🇧 Stator Cooling Water — equipment and design data**

**Design data (1.2.2.5)**
• **Flow through stator winding: 63.6 m³/h**
• Bulk water inlet temp min–max / alarm: **30–46°C / 48°C**
• **Pressure drop across winding: 1.94 bard** (28.07 psid)
• **Expected winding inlet pressure: 2.49 barg** (36.07 psig)
• Outlet high temp alarm / run back: **78.0 / 83.0°C**
• Low inlet flow alarm / run back: **57.2 / 54.2 m³/h**

**Equipment (4.3.3)**
Tank **3.1 m³** stainless | Pumps 2×100% horizontal centrifugal, **130.13 m³/h**, **6.9 barg**, **45 kW** | Coolers plate 2×100%, **99.9 m³/h**, **77.1 → 46.0°C**, CCW inlet **35.0°C** | Main filter **99.9 m³/h**, **3 micron**, cotton/rayon wound, **26 elements** | Make-up filter **22.7 m³/h**, **3 micron**, **6 elements** | Deionizer **22.7 m³/h**, **resin 566 litre**

⚠️ Resin is **consumable**, design life **about 2 years**, and **can be changed without shutting the unit down**.

**Start permissive (4.3.5.1)** — stator winding cooling water tank level not low (**10MKF01CL101**)
**Standby pump auto start (4.3.5.2)** — pump A or B discharge pressure low (pump fault or motor trip)

⚠️ **Pump flow is 130.13 m³/h but only 63.6 m³/h passes through the winding.** The rest is recirculation and the deionizer loop. Pump flow can look fine while **winding flow falls**.

⚠️ **Cooler SCW inlet is 77.1°C** against a 78.2°C outlet alarm — **1.1°C** of design margin. CCW above 35°C erases it.

`#statorwater #MKF #deionizer`

---
---

## POST 50 — ST ishga tushirish: Step 35 tekshiruv ro'yxati

**🇺🇿 Ishga tushirishdan oldin — yordamchi tizimlar holati**

**TCS** — boshqaruv tizimi quvvatlangan

**Lube oil**
• Bosim: **1.5–1.7 bar**
• Harorat **har bir rpm bo'yicha** boshqariladi

**Jacking oil**
• **Bosim: 100–150 bar**

**Seal oil**
• **Differensial bosim: <0.55 bar.g**
• **Umumiy chiqish bosimi: >0.85 bar** (L alarm **8.5 bar**, LL alarm **7.0 bar**)

**H2 tizimi**
• Havo–CO2–H2 almashtirish **tugallangan**
• **H2 bosimi: 4.14 bar**
• **H2 tozaligi: >98%** (L alarm **<95%**, LL alarm **<90%**)

**Turning gear**
• **Tezlik: ~7 rpm**
• **Rotor ekssentrisiteti: <0.075 μm**
• Normal ekssentrisitet qiymati dastlabki turning gear ishida **8 soat yoki ko'proq** uzluksiz ishlashdan keyin aniqlanadi
• ⚠️ **Ishga tushirish uchun ekssentrisitet ruxsati: < normal ekssentrisitet + 0.038 μm**

**Gidravlik quvvat bloki (control oil)**
• **Harorat: 29°C ≤ T ≤ 49°C**
• **Bosim: 160 bar.g ≤ P ≤ 170 bar.g** (Alarm L **<131 bar.g**, Trip LL **<110 bar.g**)

**Drenaj tizimi**
• **Barcha drenaj klapanlari ochiq**

**Steam seal**
• **Kollektor bosimi: 0.32 bar.g**
• Kollektor harorati egri chiziqqa muvofiq

**Kondensator vakuumi**
• Vacuum breaker klapani **to'liq yopiq**, vakuum nasos normal ishlayapti
• **ST exhaust bosimi <0.33 bar** (H alarm >0.33, HH >0.35 bar.g 5 daqiqa kechikish bilan trip, HHH 0.45 bar trip)

⚠️ **Bu ro'yxatdagi H2 bosimi 4.14 bar** — 6-bobdagi alarm chegaralari (5.03–5.45 bar) va 1.2.2.1 dagi nominal (5.17 bar.g) dan **past**. Ishga tushirishda H2 bosimi to'liq nominalda emas — bu normal, keyin ko'tariladi.

⚠️ **Ekssentrisitet ruxsati normal qiymatdan +0.038 μm.** Bu absolyut raqam emas, **sizning birligingizning normal qiymatiga nisbatan**. Normal qiymat 8 soatlik turning gear ishidan aniqlangan bo'lishi shart.

---

**🇷🇺 Перед пуском — состояние вспомогательных систем**

**TCS** — под напряжением

**Маслосистема** — **1.5–1.7 бар**, температура регулируется по оборотам
**Гидроподъём** — **100–150 бар**
**Уплотняющее масло** — **перепад <0.55 бар.g**, **общее давление >0.85 бар** (L **8.5 бар**, LL **7.0 бар**)
**Водород** — замещение воздух–CO2–H2 **завершено**, **давление 4.14 бар**, **чистота >98%** (L **<95%**, LL **<90%**)
**ВПУ** — **~7 об/мин**, **эксцентриситет <0.075 мкм**, норма определяется после **8+ часов** непрерывной работы ВПУ
⚠️ **Разрешение на пуск: эксцентриситет < норма + 0.038 мкм**
**ОГ** — **29°C ≤ T ≤ 49°C**, **160 ≤ P ≤ 170 бар.g** (сигнал **<131**, защита **<110**)
**Дренажи** — **все открыты**
**Уплотняющий пар** — **коллектор 0.32 бар.g**, температура по кривой
**Вакуум** — клапан срыва **полностью закрыт**, насос в работе, **давление выхлопа <0.33 бар**

⚠️ **Давление H2 в этом перечне 4.14 бар** — ниже уставок главы 6 (5.03–5.45) и номинала 5.17 бар.g. При пуске это нормально, потом поднимают.

⚠️ **Разрешение по эксцентриситету — норма +0.038 мкм**, не абсолютное число. Норму определяют по 8-часовой работе ВПУ.

---

**🇬🇧 Before Start — auxiliary system state check**

**TCS** — control system powered on

**Lube oil** — pressure **1.5–1.7 bar**, temperature controlled per rpm
**Jacking oil** — **100–150 bar**
**Seal oil** — **differential <0.55 barg**, **common discharge >0.85 bar** (L alarm **8.5 bar**, LL **7.0 bar**)
**H2 system** — Air–CO2–H2 replacement **complete**, **pressure 4.14 bar**, **purity >98%** (L **<95%**, LL **<90%**)
**Turning gear** — **~7 rpm**, **rotor eccentricity <0.075 μm**, normal value determined after **8+ hours** continuous turning gear run
⚠️ **Eccentricity permissive for start: < normal eccentricity + 0.038 μm**
**Hydraulic power unit** — **29°C ≤ T ≤ 49°C**, **160 ≤ P ≤ 170 barg** (alarm **<131**, trip **<110**)
**Drains** — **all drain valves open**
**Steam seal** — **header 0.32 barg**, header temperature per curve
**Condenser vacuum** — breaker valve **fully closed**, pump running, **exhaust pressure <0.33 bar**

⚠️ **H2 pressure in this list is 4.14 bar** — below the Chapter 6 alarms (5.03–5.45) and the 5.17 barg rating. That's normal at start; it is raised afterwards.

⚠️ **The eccentricity permissive is normal +0.038 μm**, not an absolute figure. The normal value must come from an 8-hour turning gear run.

`#startup #permissive #Step35`

---
---

## POST 51 — ST ishga tushirish: roll-off dan FSNL gacha

**🇺🇿 Step 36–42 — aniq raqamlar**

**Step 36 — Prewarming (sovuq ishga tushirish uchun)**
a) **HPEV yopiq** ekanini tekshir
b) HSPV yoki RFV ni och
• Maqsad haroratlar: **>155°C (HP)**, **>55°C (IP)**
• **Bosim berish bosimi: 3.8–10 bar.g**
c) Prewarming tugagach HSPV/RFV ni yop
d) **HPEV ochiq** ekanini tekshir
e) **Barcha drenaj klapanlari ochiq** ekanini tekshir

**Step 37 — Roll-off ruxsat shartlari**
☑ Turbina holati (Reset)
☑ Turning gear holati (Engage)
☑ Drenaj klapanlari (guruh A va B)
☑ Kirish bug' sharoiti (bosim, harorat, qizdirish darajasi)
☑ **Kondensator vakuumi <0.33 bar.a** — ⚠️ **ishga tushirishda tavsiya: 0.133 bar.a yoki past**
☑ Steam seal kollektor harorati
☑ **Lube oil harorati — roll-off dan oldin tavsiya: 27°C**
☑ LP rotor kengayishi
☑ Turbina kuchlanishlari
☑ **Tebranish normal (alarmda emas)**
☑ HP/IP differensial kengayish
☑ Boshqaruv tizimi normal (nosozliksiz, hold list bo'sh)

**Step 38 — Rub check (faqat dastlabki ishga tushirishda)**
a) Tezlik tempi: **150 rpm/min**
b) IPCV ochiq, turning gear uzilgan
c) **Tezlik 200 rpm ga yetgach IPCV ni yop yoki master trip.** Har bir gland seal da **g'ayritabiiy shovqin yo'q**ligini tasdiqla
d) Turning gear ulanganini tekshir
e) ⚠️ Rub-check **uzoq to'xtash yoki ta'mirdan keyin** shart. To'xtash qisqa va ST ga ish qilinmagan bo'lsa **o'tkazib yuborish mumkin**

**Step 39 — 800 rpm gacha**
a) Startup Permissive ni tekshir
b) **Tezlik tempi: 150 rpm/min** (Warm/Hot/Restart: **300 rpm/min**)
c) 800 rpm tanla
d) IPCV ochiq, turning gear uziladi
• ⚠️ **JOP tezlik 400 rpm dan yuqori bo'lgach to'xtaydi**

**Step 40 — 2500 rpm**

**Step 41 — 3000 rpm**
a) ⚠️ **Lube oil harorati 38°C dan yuqori** ekanini tekshir
b) 3000 rpm tanla

**Step 42 — FSNL**
⚠️ **FSNL ga yetgach birlik keraksiz cho'zmasdan, iloji boricha tez (30 daqiqa yoki kam) sinxronlanishi kerak.**
• FSNL da uzoq ishlash **HIP korpus va N2 packing uzelining nomutanosib qizishi va deformatsiyasiga** olib keladi → **radial ishqalanish tufayli tebranish**
• **Hot start** da FSNL da uzoq turish **L-1 bug' harorati va LP exhaust haroratini ko'taradi**

⚠️ Lube oil harorati zanjiri: **roll-off da 27°C → 3000 rpm da >38°C → sinxronizatsiyada 43–49°C**. Uchta bosqich, uchta talab.

---

**🇷🇺 Шаги 36–42 — конкретные цифры**

**Шаг 36 — Прогрев (холодный пуск)**
HPEV **закрыт** → открыть HSPV или RFV → цели **>155°C (ЦВД)**, **>55°C (ЦСД)**, **наддув 3.8–10 бар.g** → закрыть → HPEV **открыт** → **все дренажи открыты**

**Шаг 37 — Разрешения на разворот**
Турбина Reset | ВПУ Engage | Дренажи A и B | Параметры пара | **Вакуум <0.33 бар.а**, ⚠️ **рекомендуется 0.133 бар.а и ниже** | Температура коллектора уплотнений | **Температура масла — рекомендуется 27°C** | Расширение ротора ЦНД | Напряжения | **Вибрация в норме** | ОРС ЦВД/ЦСД | TCS без отказов и hold list

**Шаг 38 — Проверка на задевание (только первичный пуск)**
Темп **150 об/мин·мин** → IPCV открыт, ВПУ расцеплено → **при 200 об/мин закрыть IPCV или мастер-трип**, убедиться в **отсутствии шума** в уплотнениях → ВПУ сцеплено
⚠️ Нужна **после длительного простоя или ремонта**; при коротком простое без работ **можно опустить**

**Шаг 39 — до 800 об/мин**
Темп **150 об/мин·мин** (тёплый/горячий/повторный: **300**) | ⚠️ **Гидроподъём останавливается выше 400 об/мин**

**Шаг 40 — 2500 об/мин**

**Шаг 41 — 3000 об/мин** — ⚠️ проверить **температуру масла выше 38°C**

**Шаг 42 — FSNL**
⚠️ **Синхронизировать без затягивания, за 30 минут или быстрее.**
Длительная работа на FSNL → **несимметричный нагрев и коробление корпуса ЦВСД и уплотнения N2** → **вибрация от радиальных задеваний**. При **горячем пуске** — рост температуры L-1 и выхлопа ЦНД.

⚠️ Цепочка по маслу: **27°C на развороте → >38°C на 3000 → 43–49°C на синхронизации**.

---

**🇬🇧 Steps 36–42 — the numbers**

**Step 36 — Prewarming (cold start)**
Check **HPEV closed** → open HSPV or RFV → targets **>155°C (HP)**, **>55°C (IP)**, **pressurizing pressure 3.8–10 barg** → close after complete → check **HPEV open** → check **all drains open**

**Step 37 — Rolling permissives**
Turbine Reset | Turning gear Engage | Drains group A & B | Inlet steam conditions | **Condenser vacuum <0.33 bara**, ⚠️ **recommended on start-up: 0.133 bara or lower** | Steam seal header temperature | **Lube oil temperature — recommended before roll-off: 27°C** | LP rotor expansion | Turbine stresses | **Vibration normal (not in alarm)** | HP/IP differential expansion | TCS normal, no hold list

**Step 38 — Rub check (initial start-up only)**
Speed rate **150 rpm/min** → IPCV open, turning gear disengaged → **at 200 rpm close IPCV or master trip**, confirm **no abnormal noise** at each gland seal → turning gear engaged
⚠️ Necessary **after a long shutdown or maintenance**; can be omitted if the outage was short with no work done

**Step 39 — roll to 800 rpm**
Speed rate **150 rpm/min** (Warm/Hot/Restart: **300 rpm/min**) | ⚠️ **JOP stops once speed exceeds 400 rpm**

**Step 40 — 2500 rpm**

**Step 41 — 3000 rpm** — ⚠️ check **lube oil temperature above 38°C**

**Step 42 — FSNL**
⚠️ **Synchronize as soon as possible, 30 minutes or lower, without unnecessary extension.**
Long FSNL operation causes **asymmetric heating and distortion of the HIP shell and N2 packing** → **radial rub induced vibration**. On a **hot start** it also raises **L-1 steam temperature and LP exhaust temperature**.

⚠️ Lube oil temperature chain: **27°C at roll-off → above 38°C at 3000 rpm → 43–49°C at synchronization**.

`#startup #rolloff #FSNL #rubcheck`

---
---

## POST 52 — Sinxronizatsiya va yuklama

**🇺🇿 Step 43–47 — sinxronizatsiya**

**Step 43 — Sinxronizatsiya ruxsat shartlari**
1. HP, IP **ruxsat etilgan bug' harorati oralig'i**ni tekshir
2. ⚠️ **Lube oil harorati 43–49°C**

**Step 44 — Sinxronizatsiyani boshlash**
1. Qo'zg'atish rejimi: **"AVR"**
2. Qo'zg'atgichni ishga tushir
3. Sinxronizatsiya rejimi: **"auto"**
4. Vyklyuchatel: **"GCB"**
5. Vyklyuchatelni yop, tasdiqla
6. ⚠️ **STCS sinxronizatsiyadan darhol keyin turbina yuklama uzatmasini avtomatik 4–6% ga oshiradi. Dastlabki yuklama tempi: 1%/sek**

**Step 45 — Sinxronizatsiyadan keyin HPCV ochilishini tekshir**
⚠️ **Reverse flow → forward flow o'tishi: IPCV 50% dan yuqori**

**Step 46 — Barcha drenaj klapanlari holatini tekshir**
| Guruh | Tezlanish | RFM→FFM | Yuklama 15% | ST Trip |
|---|---|---|---|---|
| A | Ochiq | Yopiq | Yopiq | Ochiq |
| B | Ochiq | Ochiq | Yopiq | Ochiq |

**Step 47 — Nominal yuklamagacha ko'tarish**

**To'xtatish — yuklama tushirish tezligi (8.2.1)**
| Rejim | Maksimal tezlik | Izoh |
|---|---|---|
| **100% → 50%** | **≤10% / min** | Main / hot reheat bug' haroratlari nominal sharoitda saqlanishi kerak |
| **50% → min yuklama** | **≤5% / min** | Main / hot reheat harorat pasayish tezligi **<1.5°C/min** |

**Trip qilish tavsiyasi**
Turbina **istalgan yuklamada** trip qilinishi mumkin. Tavsiya: yuklama **nominal yuklamaning 10–15%** ichida bo'lganda qo'lda yoki masofadan trip qilish.
⚠️ **Tajriba shuni ko'rsatadiki, yuklama ostida turbogeneratorni trip qilishda tezlik oshmaydi.** Trip dan keyin barcha kirish klapanlari tez yopiladi, generator tarmoqdan uziladi — **keraksiz motoring**dan qochish uchun.

⚠️ **Sinxronizatsiyadan keyin +4–6% yuklama AVTOMATIK.** Bu operator qo'shadigan narsa emas. 1%/sek tempda ko'tariladi.

⚠️ **RFM → FFM o'tishi IPCV 50% da.** Shu nuqtada A guruh drenajlari yopiladi, B guruh ochiq qoladi.

---

**🇷🇺 Шаги 43–47 — синхронизация**

**Шаг 43** — проверить **допустимый диапазон температур пара ВД/СД**, ⚠️ **температура масла 43–49°C**

**Шаг 44** — режим возбуждения **AVR** → пуск возбудителя → синхронизация **auto** → выключатель **ГВ** → закрыть, подтвердить
⚠️ **STCS сразу после синхронизации автоматически поднимает задание нагрузки на 4–6%, темп начальной нагрузки 1%/с**

**Шаг 45** — проверить открытие РК ВД. ⚠️ **Переход обратный → прямой поток: РК СД выше 50%**

**Шаг 46** — проверить положение дренажей (таблица A/B)

**Шаг 47** — набор до номинала

**Разгрузка при останове**
**100% → 50%: ≤10%/мин**, температуры главного и промперегретого пара держать на номинале
**50% → мин: ≤5%/мин**, скорость снижения температур **<1.5°C/мин**

**Про отключение**
Турбину можно отключить **при любой нагрузке**. Рекомендуется — при **10–15% номинала**.
⚠️ **Опыт показывает: при отключении под нагрузкой обороты не растут.** После отключения все стопорные быстро закрываются, генератор отделяется от сети во избежание **моторного режима**.

⚠️ **Подъём на 4–6% после синхронизации — АВТОМАТИЧЕСКИЙ.**
⚠️ **Переход RFM → FFM при РК СД 50%** — там же закрываются дренажи группы A.

---

**🇬🇧 Steps 43–47 — synchronization**

**Step 43** — check **HP and IP allowable steam temperature range**, ⚠️ **lube oil temperature 43–49°C**

**Step 44** — exciter mode **"AVR"** → start exciter → synchronization mode **"auto"** → breaker **"GCB"** → close, confirm
⚠️ **STCS automatically increases the turbine load reference by 4–6% immediately after synchronization; initial load rate is 1%/sec**

**Step 45** — check HPCV opens. ⚠️ **Reverse flow → forward flow changing: IPCV above 50%**

**Step 46** — check all drain valve status (A/B table)

**Step 47** — load up to rated load

**Unloading rates on shutdown (8.2.1)**
**100% → 50%: ≤10%/min**, main/hot reheat steam temperatures maintained at rated conditions
**50% → min load: ≤5%/min**, main/hot reheat temperature decreasing rate **<1.5°C/min**

**On tripping**
The turbine **can be tripped at any load**. Recommended when load is within **10–15% of rated**.
⚠️ **Experience indicates turbine speed will not increase when tripping the turbine-generator under load.** After tripping, all steam inlet valves close quickly and the generator is disconnected to avoid **unnecessary motoring**.

⚠️ **The 4–6% load step after synchronization is AUTOMATIC** — not an operator action.
⚠️ **RFM → FFM transfer happens at IPCV above 50%**, which is also where group A drains close.

`#synchronization #loading #unloading`

---
---

## POST 53 — ST to'xtatish ketma-ketligi

**🇺🇿 To'xtatish — 13 qadam**

**1. Yuklamani 10% dan pastga asta tushirish**
⚠️ Bug' generatori yuklamasini **30–50%** ga yetgach ushlab turish tavsiya etiladi (joyida sozlash) — bug' harorati pasayishidan kelib chiqadigan **turbina rotoridagi qabul qilib bo'lmas termik kuchlanishning** oldini olish uchun
• Drenajlar TBN yuklamasiga qarab avtomatik ochiladi/yopiladi

**2. EBOP [AUTO] rejimida ekanini tasdiqla**

**3. Avariya tugmasi bilan trip**
• Yuklama maqsadli qiymatga (tavsiya: **10% dan past**) yetgach turbina darhol trip qilinadi
• **HPSV, HPCV, IPSV, IPCV to'liq yopiq** ekanini tekshir

**4. JOP @ 380 rpm da ishga tushganini tekshir**
⚠️ ST tezligi **380 rpm** ga tushganda jacking oil nasos ishga tushishi shart
*(Diqqat: avariya protsedurasida 400 rpm deyilgan, normal to'xtatishda 380 rpm)*

**5. Tezlik 0 rpm ga tushgach turning gear ulanganini tekshir**
• Turning gear ishga tushdi
• **Ekssentrisitet normal**
• Turning gear ishlashini davom ettir

**6. Ikkala HRSG to'xtatiladi**
• HRSG 1 va HRSG 2 **kirish diverter damperlari yopiq**

**7. Bypass klapanlari to'liq ishdan chiqariladi**
• HP, IP, LP bypass klapanlari yopiq
• **Kondensatorga boradigan barcha drenajlar yopiq**

**8. Vakuumni buzish**
• Vakuum nasosni to'xtat
• Vacuum breaker klapanini och
• ⚠️ **Kondensator qarshi bosimi 80 kPa dan yuqori** ekanini tekshir

**9. Val zichlash bug' tizimini ishdan chiqarish**
• Yordamchi bug'dan gland steam kollektoriga rostlash klapani **to'liq yopiq**
• **Gland steam extraction fan** ni to'xtat

**10. Turning gear ni ishdan chiqarish**
⚠️ **Turning gear faqat ST harorati 150 dan past bo'lganda ishdan chiqarilishi mumkin**

**11. Jacking oil ni ishdan chiqarish**
⚠️ **Faqat turning gear ishdan chiqarilgandan keyin**

**12. H2–CO2–havo almashtirish**
⚠️ ST uzoq vaqt to'xtatilsa va yaqin muddatda ishga tushirilmasa, yoki ta'mir bajarilsa — **vodorod sizishining oldini olish uchun** almashtiriladi
• **Umumiy jarayon: H2 bosimini 10–30 kPa ga tushirish → H2 ni CO2 bilan almashtirish → CO2 ni havo bilan almashtirish → bosimni 5–10 kPa ga tushirish**

**13. Seal oil tizimini ishdan chiqarish**
⚠️ **Faqat H2–CO2–havo almashtirish tugagandan va havo bosimi tushirilgandan keyin**

⚠️ Ketma-ketlik **qat'iy bog'langan**: turning gear → jacking oil → gaz almashtirish → seal oil → lube oil. Har biri oldingisiga bog'liq. **Lube oil eng oxirida** (POST 4 dagi 8 ta shart).

---

**🇷🇺 Останов — 13 шагов**

**1.** Разгрузка ниже 10%. ⚠️ Рекомендуется держать нагрузку котла при **30–50%** во избежание **недопустимых термонапряжений в роторе**. Дренажи работают автоматически по нагрузке.
**2.** АМН в режиме **[AUTO]**
**3.** Отключение кнопкой при нагрузке **ниже 10%**; проверить полное закрытие ГСК и РК ВД/СД
**4.** ⚠️ Проверить пуск гидроподъёма при **380 об/мин** *(в аварийной процедуре указано 400)*
**5.** После выбега до 0 — ВПУ включено, **эксцентриситет в норме**, ВПУ оставить в работе
**6.** Оба КУ остановлены, **входные шиберы закрыты**
**7.** БРОУ ВД/СД/НД закрыты, **все дренажи в конденсатор закрыты**
**8.** Срыв вакуума: остановить насос, открыть клапан срыва, ⚠️ **противодавление выше 80 кПа**
**9.** Вывод уплотняющего пара: регулятор подачи **полностью закрыт**, **эксгаустер остановлен**
**10.** ⚠️ **ВПУ выводится только при температуре ПТ ниже 150**
**11.** ⚠️ Гидроподъём — **только после вывода ВПУ**
**12.** Замещение H2–CO2–воздух: ⚠️ **снизить давление H2 до 10–30 кПа → вытеснить CO2 → вытеснить воздухом → снизить до 5–10 кПа**
**13.** ⚠️ Система уплотняющего масла — **только после завершения замещения**

⚠️ Цепочка жёсткая: ВПУ → гидроподъём → замещение газа → уплотняющее масло → маслосистема. **Маслосистема выводится последней.**

---

**🇬🇧 Shutdown Sequence — 13 steps**

**1.** Decrease load below 10%. ⚠️ Recommended to hold steam generator load after reaching **30–50%** (site tuning) to prevent **unacceptable thermal stress at the turbine rotor** from falling steam temperature. Drains operate automatically per TBN load.
**2.** Verify **EBOP in [AUTO]**
**3.** Trip by emergency push button at target load (**below 10% recommended**); check HPSV, HPCV, IPSV, IPCV fully closed
**4.** ⚠️ Check **JOP started at 380 rpm** *(the emergency procedure states 400 rpm)*
**5.** After coastdown to 0 rpm — turning gear started, **eccentricity normal**, keep turning gear running
**6.** Both HRSGs shut down, **inlet diverter dampers closed**
**7.** HP/IP/LP bypass valves closed, **all drains leading into the condenser closed**
**8.** Break vacuum: stop the vacuum pump, open the breaker valve, ⚠️ check **condenser back pressure above 80 kPa**
**9.** Gland steam out of service: aux steam regulation valve **fully closed**, **gland steam extraction fan stopped**
**10.** ⚠️ **Turning gear can be out of service only if steam turbine temperature is less than 150**
**11.** ⚠️ Jacking oil — **only after turning gear is out of service**
**12.** H2–CO2–air replacement: ⚠️ **decrease H2 pressure to 10–30 kPa → replace H2 with CO2 → replace CO2 with air → decrease pressure to 5–10 kPa**
**13.** ⚠️ Seal oil system — **only after replacement is complete and air pressure reduced**

⚠️ The chain is strict: turning gear → jacking oil → gas replacement → seal oil → lube oil. **Lube oil goes last** (the 8 conditions in POST 4).

`#shutdown #sequence #gasreplacement`

---
---

## POST 54 — HP/IP klapan onlayn testi

**🇺🇿 Klapan testi — kunlik majburiyat**

⚠️ **HPSV va HPCV onlayn testi mashinadagi HAR BIR juftlik uchun HAR KUNI bajarilishi shart.** IPSV/IPCV uchun ham shunday.

**Test nimani tasdiqlaydi**
• Birlik trip bo'lsa **stop klapanlar erkin yopila oladimi**
• Overspeed holatida **har bir control klapan erkin yopila oladimi**

**Test qanday kechadi**
• Har bir stop/control juftlik **alohida** sinaladi → **kichik ruxsat etilgan bosim ko'tarilishi** va mos ravishda **kichik yuklama tushishi** bo'ladi
• Test boshlanganda boshqaruv tizimi **boshqa juftlikni test qilishdan bloklaydi**
• Avval **control klapan** yopiladi. "Quick close" solenoid yoki servoklapan bo'lsa — **oxirgi 10% yurishda tez yopilish**
• Control klapan yopilgach **stop klapan** sinaladi. "Dump test" solenoid bo'lsa — **oxirgi 10% da tez yopilish**
• "Test OFF" tanlanganda stop klapan **to'liq ochiq** holatga qaytadi, keyin control klapan ochiladi. **Ikkalasi to'liq ochilganda test tugaydi**

**Protsedura**
1. Operator interfeysida **Valve Test** ekranini tanla
2. Ikkala stop va control klapan **OCHIQ** ekanini tekshir
3. Kerakli juftlikni tanla → **"Test ON"**
4. Ikkalasi yopiq holatga kelgach → **"Test OFF"**
5. Ikkalasi yana OCHIQ ko'rsatilganda test tugaydi
6. Ikkinchi juftlik uchun takrorla
*(Testni to'xtatish kerak bo'lsa — "Test OFF")*

**Alarm xabarlari**
| Xabar | Ma'nosi |
|---|---|
| **HP CONTROL VALVE # TEST FAILED** | Control klapan berilgan vaqtda yopilmadi |
| **HPCV # QUICK CLOSE SOLENOID FAILURE** | Quick close solenoid vaqtida yopmadi |
| **HPCV # MAINTENANCE REQUIRED** | Klapan to'liq yopildi, lekin stop qismi davomida **ochilish tomon siljidi** |
| **HPSV # TEST FAILED TO CLOSE IN TIME** | Stop klapan vaqtida yopilmadi yoki test davomida tizim trip bo'ldi |
| **HPSV # DUMP TEST SOLENOID FAILURE** | Dump test solenoid vaqtida yopmadi |

**Test muvaffaqiyatsiz bo'lsa**
• Klapanlar oqilona vaqt ichida kerakli holatga yetmasligi — **test muvaffaqiyatsizligi**
• ⚠️ **Eng ehtimolli sabab — klapan shtokining yopishib qolishi**
• Nosozlik **klapanga darhol ta'mir kerakligini** bildiradi
• Sabab **test zanjiridagi elektr nosozligi emasligini** tekshir
• ⚠️ **Agar mexanik muammo tasdiqlansa — turbogeneratorni yuklamadan tushirib DARHOL to'xtatishni boshlang. YUKLAMA OSTIDA BIRLIKNI TRIP QILMANG.**

⚠️ **Muhim ogohlantirish (manualdan):** bu test bilan bog'liq alarmlar operatorni **faqat qo'pol nosozlikdan** ogohlantiradi. **Testning muvaffaqiyatli tugashi kelajakdagi ishlashni kafolatlamaydi**, lekin trip paytida tizimning to'g'ri ishlash ehtimolini oshiradi.

---

**🇷🇺 Испытание клапанов — ежедневная обязанность**

⚠️ **Онлайн-испытание ГСК и РК ВД проводится ЕЖЕДНЕВНО для КАЖДОЙ пары.** То же для СД.

**Что проверяется** — свободно ли закрываются стопорные при отключении и регулирующие при разгоне.

**Ход испытания**
Каждая пара испытывается **отдельно** → **небольшой допустимый рост давления** и **небольшое снижение нагрузки**. Система **блокирует** испытание второй пары. Сначала закрывается **РК** (при наличии quick close — быстрое закрытие на **последних 10%** хода), затем **ГСК** (при наличии dump test — то же). По «Test OFF» ГСК открывается полностью, затем РК; испытание завершено при полном открытии обоих.

**Процедура**
Экран Valve Test → убедиться, что оба открыты → выбрать пару → **Test ON** → после закрытия обоих **Test OFF** → завершение при индикации OPEN → повторить для второй пары

**Сообщения**
**CONTROL VALVE # TEST FAILED** — РК не закрылся вовремя
**CV # QUICK CLOSE SOLENOID FAILURE** — не сработал соленоид быстрого закрытия
**CV # MAINTENANCE REQUIRED** — РК закрылся, но **пополз на открытие** во время испытания ГСК
**SV # TEST FAILED TO CLOSE IN TIME** — ГСК не закрылся вовремя или блок отключился
**SV # DUMP TEST SOLENOID FAILURE** — не сработал dump test соленоид

**При отказе**
⚠️ **Наиболее вероятная причина — заедание штока.** Требуется **немедленный ремонт**. Проверить, что дело не в электрической цепи испытания.
⚠️ **При подтверждённом механическом дефекте — начать немедленный останов разгрузкой. НЕ ОТКЛЮЧАТЬ БЛОК ПОД НАГРУЗКОЙ.**

⚠️ Из руководства: сигналы испытания предупреждают **только о грубых отказах**. **Успешное испытание не гарантирует работоспособность в будущем**, но повышает вероятность правильной работы при отключении.

---

**🇬🇧 HP/IP Valve Online Test — daily requirement**

⚠️ **The on-line test of the HP stop and control valve must be performed DAILY for EACH pair** on the machine. Same for IP.

**What it verifies** — that stop valves are free to close if the unit is tripped, and each control valve is free to close in an overspeed situation.

**How it runs**
Each pair is tested **separately**, causing **a small allowable pressure rise with a corresponding small drop in load**. The control system **locks out the other pair** until complete. The **control valve** closes first (with "quick close" solenoids or servo valves there is rapid closure in the **last 10% of stroke**), then the **stop valve** is tested (same for a "dump test" solenoid). On "Test OFF" the stop valve reopens wide, then the control valve; the test completes when both are full open.

**Procedure**
Valve Test screen → verify both open → select the pair → **Test ON** → once both closed, **Test OFF** → complete when both indicate OPEN → repeat for the second pair

**Alarm messages**
**HP CONTROL VALVE # TEST FAILED** — control valve did not close in the time allowed
**HPCV # QUICK CLOSE SOLENOID FAILURE** — quick close solenoid did not close it in time
**HPCV # MAINTENANCE REQUIRED** — valve reached full closed but **drifted toward open** during the stop valve portion
**HPSV # TEST FAILED TO CLOSE IN TIME** — stop valve did not close in time, or the system tripped during test
**HPSV # DUMP TEST SOLENOID FAILURE** — dump test solenoid did not close it in time

**On failure**
⚠️ **The most likely cause is a sticking valve stem.** Failure indicates the valve **requires immediate maintenance**. Verify the cause is not an electrical fault in the test circuit.
⚠️ **If it is a mechanical problem with the HPCV or HPSV, begin immediate shutdown by unloading the turbine-generator. DO NOT TRIP THE UNIT WITH LOAD ON THE MACHINE.**

⚠️ From the manual: these alarms alert the operator **only of gross malfunction**. **Successful completion does not guarantee future operability**, but does increase the probability of proper operation during a trip event.

`#valvetest #HPSV #dailytest`

---
---

## POST 55 — ETD testi (offline va online)

**🇺🇿 ETD — elektr trip qurilmalari testi**

**OFFLINE ETD test (9.5)**

Protsedura:
1. Operator interfeysida **ETD Test** ekranini tanla
2. ⚠️ **Generator vyklyuchateli OCHIQ**, ETD lar **reset**, bosim relelarida **to'liq gidravlik bosim** borligini tekshir
3. **Off-line ETD 1-2 Test** tugmasini tanla
4. Quyidagi hodisalar ketma-ketligini kuzat:
 • ETD #1 ko'rsatkichi **"Reset" → "Tripped"**
 • ETD #1 "Tripped" dan keyin ETD #2 **"Reset" → "Tripped"**
 • ⚠️ **Gidravlik kollektor bosimi yo'qoladi va barcha klapanlar yopiladi**
5. Qolgan ETD juftliklarini sinash uchun takrorla

Alarmlar: **ETD1 trip time excessive**, **ETD2 trip time excessive**, **Unexpected trip problem with ETD#1 or ETD#2**
Testni **istalgan vaqtda cancel** funksiyasi bilan to'xtatish mumkin.

**ONLINE ETD test (9.6)**

⚠️ **Turbinani haqiqatan trip qilmasdan** har bir ETD ni alohida quvvatsizlantirish va ishlashini tekshirish imkonini beradi.
⚠️ **Turbinani trip qilish uchun 2/3 mantiq talab qilinadi** — bitta ETD ni quvvatsizlantirish gidravlik trip kollektori bosimini yo'qotmaydi. **Test davomida trip kerak bo'lsa, qolgan ETD lar normal ishlaydi va turbinani trip qiladi.**
Test generator vyklyuchateli **ochiq yoki yopiq** holatda bajarilishi mumkin.

Protsedura:
1. ETD test ekranini tanla
2. ETD lar reset va barcha bosim relelarida to'liq gidravlik bosim borligini tekshir
3. **On-line ETD #1 test** ni tanla
4. Kuzat: ETD #1 **"Reset" → "Tripped"** → holati **"Reset"** ga qaytadi

Alarmlar: **ETD1 trip time excessive** yoki **ETD2 trip time excessive**

⚠️ **Test davomida VA undan keyin stop klapanlarni kuzating. Har qanday klapan harakati NORMAL EMAS va muammoni bildiradi.** Bu holat **sust ETD to'liq reset bo'lmayotganini** va natijada klapanga gidravlik bosimning bir qismi yo'qolganini ko'rsatishi mumkin.

**Nosozlikda nima qilish**
• **Bitta ETD sust ishlasa yoki umuman ishlamasa** → birlik ta'mir uchun to'xtatilishi kerak
• Birlikni to'xtatib bo'lmasa → **bu testni har kuni bajaring**. ⚠️ **Ko'pincha ETD larni test bilan takror-takror ishlatish sustlik holatini yaxshilaydi**
• ⚠️ **Ikkita ETD sust ishlasa yoki ishlamasa → turbogeneratorni yuklamadan tushirib DARHOL to'xtatishni boshlang. YUKLAMA OSTIDA BIRLIKNI TRIP QILMANG.**

⚠️ Offline test **barcha klapanlarni yopadi** — ya'ni faqat to'xtagan birlikda. Online test **hech narsani yopmaydi** — 2/3 mantiq buni ta'minlaydi. Ikkalasini chalkashtirish qimmatga tushadi.

---

**🇷🇺 Испытание ЭМВ (ETD)**

**OFFLINE (9.5)**
Экран ETD Test → ⚠️ **выключатель генератора ОТКРЫТ**, ETD в **Reset**, на реле давления **полное гидравлическое давление** → **Off-line ETD 1-2 Test** → наблюдать:
• ETD #1 **Reset → Tripped** • затем ETD #2 **Reset → Tripped**
• ⚠️ **Давление в гидроколлекторе теряется, все клапаны закрываются**
Повторить для остальных пар.
Сигналы: **ETD1/ETD2 trip time excessive**, **Unexpected trip problem**. Отмена в любой момент.

**ONLINE (9.6)**
⚠️ Позволяет обесточить каждый ETD **без фактического отключения турбины**.
⚠️ **Для отключения нужна логика 2 из 3** — снятие питания с одного ETD не приводит к потере давления. **Если во время испытания потребуется отключение, оставшиеся ETD отработают штатно.**
Можно проводить при **любом положении** выключателя генератора.

Процедура: экран ETD test → проверить Reset и полное давление → **On-line ETD #1 test** → ETD #1 **Reset → Tripped → Reset**
Сигналы: **ETD1 / ETD2 trip time excessive**

⚠️ **Наблюдайте за стопорными клапанами ВО ВРЕМЯ и ПОСЛЕ испытания. Любое движение клапана — НЕ норма.** Это признак того, что **вялый ETD не сбрасывается полностью** и часть давления к клапану потеряна.

**При отказе**
• **Один вялый или неработающий ETD** → останов на ремонт
• Останов невозможен → **проводить испытание ежедневно**. ⚠️ **Многократное срабатывание часто улучшает вялое состояние**
• ⚠️ **Два вялых или неработающих ETD → немедленный останов разгрузкой. НЕ ОТКЛЮЧАТЬ ПОД НАГРУЗКОЙ.**

⚠️ Offline **закрывает все клапаны** — только на остановленном блоке. Online **ничего не закрывает** благодаря 2/3. Путать нельзя.

---

**🇬🇧 ETD Test — offline and online**

**OFFLINE ETD test (9.5)**
Select **ETD Test** screen → ⚠️ verify **generator breaker is open**, ETDs are **reset**, and **full hydraulic pressure** exists at the pressure switches → select **Off-line ETD 1-2 Test** → observe:
• ETD #1 changes **"Reset" → "Tripped"**
• Following that, ETD #2 changes **"Reset" → "Tripped"**
• ⚠️ **Hydraulic header pressure is lost and all valves are closed**
Repeat to test the remaining ETD pairs.
Alarms: **ETD1 trip time excessive**, **ETD2 trip time excessive**, **Unexpected trip problem with ETD#1 or ETD#2**. The test may be aborted at any time.

**ONLINE ETD test (9.6)**
⚠️ Provides the capability of individually de-energizing each ETD and verifying correct operation **without actually tripping the unit**.
⚠️ **Two out of three tripping logic is required to trip the turbine**, so de-energizing one ETD will not cause loss of hydraulic trip header pressure. **Should a trip be required during testing, the remaining ETDs will operate normally and trip the turbine.**
Can be performed with the generator breaker **either open or closed**.

Procedure: ETD test screen → verify ETDs reset and full hydraulic pressure at all pressure switches → select **on-line ETD #1 test** → ETD #1 goes **"Reset" → "Tripped" → back to "Reset"**
Alarms: **ETD1 trip time excessive or ETD2 trip time excessive**

⚠️ **Observe the stop valves both during and after the test. Any valve movement is not normal and indicates a problem.** It may indicate a **sluggish ETD is not fully resetting**, so some hydraulic pressure to the valve was lost.

**On failure**
• **A single sluggish or non-operating ETD** → shut the unit down for maintenance
• If the unit cannot be shut down → **perform this test every day**. ⚠️ **Quite often, exercising the ETDs repeatedly with the test will improve a sluggish condition**
• ⚠️ **If two ETDs operate sluggishly or fail → begin immediate shutdown by unloading. DO NOT TRIP THE UNIT WITH LOAD ON THE MACHINE.**

⚠️ The offline test **closes every valve** — unit stopped only. The online test **closes nothing**, thanks to 2/3 voting. Confusing the two is expensive.

`#ETD #trip #dailytest #2of3`

---
---

## POST 56 — Rotor egilishi

**🇺🇿 Rotor egilishi — belgi, sabab, harakat**

Manual buni **kombinatsion siklda eng jiddiy avariyalardan biri** deb ataydi.

**BELGILAR**

*Ishga tushirish bosqichida*
⚠️ **Kritik tezlikdan o'tishda tebranish amplitudasi keskin oshadi**, himoya qiymatidan oshishi mumkin: **val tebranishi >0.254 mm** yoki **podshipnik tebranishi >0.1 mm** → to'xtatish himoyasi ishlaydi

*Ish bosqichida*
**1× chastota tebranish komponenti sezilarli oshadi, faza barqaror**

*To'xtatishdan keyin*
• **Turning gear toki oshadi**, tebranadi yoki g'ayritabiiy shovqin chiqaradi
• **Rotor ekssentrisiteti chegaradan oshadi** (masalan **>0.076 mm**)
• Hatto **turning gear normal ishga tushmasligi mumkin**

*Ishqalanish belgilari*
• Metall ishqalanish tovushi, ayniqsa **val zichlashi va diafragma bug' zichlashida**
• Val zichlashida bug' sizishi yoki g'ayritabiiy harorat taqsimoti — masalan **mahalliy qizib ketish rotor yuzasi rangini o'zgartiradi**

*Harorat va o'q siljishi*
• Yuqori va pastki korpus harorati farqi ruxsat etilgan qiymatdan oshadi (masalan **>42°C**) → **"mushuk beli" (cat-back) deformatsiyasi** → rotor-stator zazori kamayadi
• **Manfiy o'q siljishi farqining oshishi** — sovuq bug' kirishi yoki val zichlashiga bug' berishning kechikishidan bo'lishi mumkin

*Parametr monitoringi*
⚠️ **Rotor runout (egilish qiymati) dastlabki qiymatdan ±0.02 mm ga oshadi** yoki ishlab chiqaruvchi belgilagan qiymatdan: **yangi birlik runout ≤0.02 mm**, **ish davridagi journal runout ≤0.03 mm**
• Podshipnik harorati ko'tariladi, ayniqsa **ishqalanayotgan vkladish harorati keskin oshishi mumkin**

**SABABLAR**

*Rotor-stator ishqalanishi*
• Val zichlash zazori **juda kichik sozlangan**, bug' zichlash elementining chekinish zazori yetarli emas, yoki **korpus "mushuk panjasi" kengayishida issiq holatdagi markaz o'zgarishi hisobga olinmagan**
• **Uzoq muddatli tebranish** → rotorning mahalliy qizib ketishi → **material oquvchanlik chegarasining pasayishi** → doimiy deformatsiya

*Sovuq bug' yoki sovuq suv kirishi*
HRSG nosozligi yoki drenaj tizimidagi anomaliya past haroratli bug' yoki kondensatning **rotorga purkalishiga** olib keladi → **mahalliy keskin sovish va qisqarish** → plastik deformatsiya

*Turning gear uzilishi yoki operatsion xatolar*
• To'xtatishdan keyin turning gear o'z vaqtida ishga tushirilmasligi yoki nosozligi → **statik holatda o'z og'irligi yoki harorat farqidan egilish**
• ⚠️ **Issiq ishga tushirishda avval vakuum tortilib, keyin val zichlashiga bug' berilsa — sovuq havo val zichlashi bo'ylab korpusga kiradi va rotorni qisqartiradi**

⚠️ Eng muhim amaliy xulosa: **hot start da gland steam VAKUUMDAN OLDIN berilishi kerak.** Aks holda sovuq havo rotorni qisqartiradi va egilish beradi.

---

**🇷🇺 Изгиб ротора — признаки, причины, действия**

Руководство называет это **одной из тяжелейших аварий ПГУ**.

**ПРИЗНАКИ**
*При пуске* — ⚠️ **резкий рост вибрации на критической**, возможно выше защиты: **вибрация вала >0.254 мм** или **подшипника >0.1 мм**
*В работе* — **рост составляющей 1× при стабильной фазе**
*После останова* — **рост, колебания или шум тока ВПУ**, **эксцентриситет >0.076 мм**, иногда **ВПУ не включается**
*Задевание* — металлический шум у **уплотнений вала и диафрагм**, течь пара или **локальный перегрев с изменением цвета поверхности ротора**
*Температура и осевой сдвиг* — разница верх/низ **>42°C** → **деформация «кошачья спина»** → потеря зазоров; **рост отрицательного осевого сдвига** от захолаживания или запоздалой подачи пара на уплотнения
*Мониторинг* — ⚠️ **биение ротора выше исходного на ±0.02 мм** или сверх заводского: **новый блок ≤0.02 мм**, **по шейке в работе ≤0.03 мм**; рост температуры **задевающего вкладыша**

**ПРИЧИНЫ**
*Задевание* — **слишком малый зазор уплотнений**, недостаточный отжимной зазор, **не учтено смещение горячего центра при расширении по «кошачьим лапам»**; **длительная вибрация** → локальный перегрев → снижение предела текучести → остаточная деформация
*Захолаживание* — отказ КУ или дренажей → **попадание низкотемпературного пара или конденсата на ротор** → локальное сжатие → пластическая деформация
*ВПУ и ошибки* — несвоевременное включение или отказ ВПУ → изгиб от собственного веса; ⚠️ **при горячем пуске сначала набрали вакуум, потом дали пар на уплотнения — холодный воздух пошёл по уплотнениям в цилиндр и сжал ротор**

⚠️ Главный практический вывод: **при горячем пуске уплотняющий пар подают ДО набора вакуума.**

---

**🇬🇧 Rotor Bending — phenomena, causes, action**

The manual calls it **one of the major malignant accidents in combined cycle plants**.

**PHENOMENA**
*Start-up* — ⚠️ **vibration amplitude increases sharply passing critical speed**, may exceed protection: **shaft vibration >0.254 mm** or **bearing vibration >0.1 mm**
*Operation* — **the 1× frequency component increases significantly and the phase is stable**
*After shutdown* — **turning gear current increases, fluctuates or makes abnormal noise**, **eccentricity exceeds limit (e.g. >0.076 mm)**, and **turning gear may not start normally**
*Rub signs* — metal friction sound, especially at **shaft seal and diaphragm steam seal**; steam leakage or abnormal temperature distribution such as **local overheating discolouring the rotor surface**
*Temperature and axial* — upper-to-lower cylinder difference **over 42°C** → **"cat-back" deformation** reducing rotor-stator clearance; **increase of negative axial displacement difference**, possibly from cold steam ingress or delayed steam supply to the shaft seal
*Monitoring* — ⚠️ **rotor runout exceeds the original by ±0.02 mm** or the manufacturer's value: **new unit runout ≤0.02 mm**, **journal runout in operation ≤0.03 mm**; bearing temperature rises, and **the rubbing bush may rise sharply**

**CAUSES**
*Rotor-stator rub* — **shaft seal clearance adjusted too small**, insufficient seal piece retreat clearance, or **cylinder cat's paw expansion not accounting for hot-state centre change**; **long-term vibration** → local overheating → **decrease in material yield strength** → permanent deformation
*Cold steam or water ingress* — HRSG failures or abnormal drainage **spray low-temperature steam or condensed water onto the rotor** → local sudden cooling and contraction → plastic deformation
*Turning gear interruption or operational errors* — failure to engage in time or turning gear failure → bow from self-weight or temperature difference; ⚠️ **during hot start-up, drawing vacuum first before supplying steam to the shaft seal lets cold air enter along the seal and contracts the rotor**

⚠️ The practical takeaway: **on a hot start, gland steam goes on BEFORE vacuum is drawn.**

`#rotorbend #eccentricity #hotstart`

---
---

## POST 57 — Yog' tizimi yong'ini

**🇺🇿 Yog' yong'ini — ustuvorlik tartibi**

⚠️ **Operatsiya ustuvorligi: to'xtatish > o't o'chirish > izolyatsiya > himoya**

**A. AVARIYA TO'XTATISH (birinchi bajariladi)**

*1. Darhol avariya to'xtatish*
**ETS avariya tugmasini qo'lda bosing**, "steam turbine trip" signalini tasdiqlang, va **kondensator vakuumini buzing** (vacuum breaker klapanini oching, vakuum nasosni to'xtating) — birlikning tezlik pasayishini tezlashtirish uchun.

*2. Yog' nasoslari — ikki xil holat*
⚠️ **Yog' tizimida SIZISH BOR bo'lsa:** **emergency lube oil nasosni ishga tushiring va asosiy nasosni to'xtating.** ST **0 ga bo'shashguncha** emergency nasos ishlaydi, shundan keyingina to'xtatiladi.
⚠️ **Sizish YO'Q bo'lsa:** **asosiy nasosni ishlashda qoldiring**, va emergency nasosning muvaffaqiyatli ishga tusha olishini sinab ko'ring.

*3. Bug'ning uzilishini tasdiqlash*
HPSV, HPCV, IPSV, IPCV, LPSV, LPCV **yopiq**, HP exhaust check valve'lar **yopiq**, HP vent klapani **ochiq**.

*4. Rotor holatini kuzatish*
To'xtatish davomida tezlik pasayish tendensiyasini diqqat bilan kuzating. **Yog' uzilishi tufayli podshipnikning kuyishi yoki rotorning qotib qolishidan** saqlaning.
⚠️ **Yong'in nazorat ostida bo'lsa** — tezlik turning gear ishga tushish qiymatiga tushganda turning gear ni ishga tushiring. **Yong'in nazoratsiz bo'lsa — turning gear ni to'xtatib turing.**

**B. O'T O'CHIRISH VA IZOLYATSIYA (bir vaqtda)**

*O'chirish vositasi*
**Quruq kukunli, karbonat angidridli yoki ko'pikli** o'chirgichlar.
⚠️ **Suvni bevosita purkash QAT'IYAN TAQIQLANADI** — yog' suvdan yengil va yong'inni tarqatadi.

*Maqsadli operatsiyalar*
• **Bak yong'ini** — bak og'zini **yong'in adyoli** bilan yoping, bo'g'ib o'chiring
• **Quvur sizishi yong'ini** — o'chirish vositasini **yong'in manbasining tagiga** purkang, yog'ning oqib tarqalishini **yong'in qumi** bilan to'sing

*Izolyatsiya*
Yog' tizimi bilan boshqa uskunalar orasidagi ulanish klapanlarini yoping, **yong'in zonasiga elektr ta'minotini uzing** (elektr uchqunlari yog' va gazni yoqmasligi uchun), atrofdagi yonuvchi materiallarni (izolyatsiya, yog' dog'lari) tozalang.

*Sovutish himoyasi*
Yonmagan lekin yaqin turgan **yog' quvurlari va bak devorlariga suv purkab soviting** — yuqori harorat yong'in doirasini kengaytirmasligi uchun.

**C. XAVFSIZLIK VA KEYINGI ISHLAR**

*Shaxsiy himoya*
Olovbardosh kiyim, himoya niqobi, issiqlikka chidamli qo'lqop. Yuqori haroratli qismlarga yoki olovga bevosita tegmang. **Yong'in nazoratdan chiqsa — darhol xavfsiz zonaga chiqing.**

*Ventilyatsiya va portlashning oldini olish*
⚠️ **Ventilyatsiyani yoqing, LEKIN yuqori bosimli (musbat bosimli) ventilyatsiya QAT'IYAN TAQIQLANADI.**
⚠️ Yong'in zonasida **mobil telefon, ratsiya va uchqun berishi mumkin bo'lgan boshqa uskunalarni ishlatish taqiqlanadi.**

*Keyingi tekshiruv*
Yong'in o'chirilgach yog' tizimi sizish nuqtalarini, podshipnik shikastini, korpusning yuqori haroratdan deformatsiyalanganini tekshiring. **Faqat qayta alangalanish xavfi yo'qligi tasdiqlangandan keyin** sizish nuqtalarini bartaraf eting va joyni tozalang.

*Qayd va hisobot*
To'xtatish vaqti, yong'in joyi, o'chirish jarayoni va uskuna holatini batafsil qayd eting. **Birlikni qayta ishga tushirish faqat nosozlik butunlay bartaraf etilgandan va tekshiruvdan o'tgandan keyin ko'rib chiqiladi.**

---

**🇷🇺 Пожар в маслосистеме — порядок приоритетов**

⚠️ **Приоритет: останов > тушение > изоляция > защита**

**A. АВАРИЙНЫЙ ОСТАНОВ (первым делом)**
**1.** Нажать кнопку ETS, подтвердить сигнал отключения, **сорвать вакуум** для ускорения выбега
**2.** ⚠️ **Есть течь:** пустить аварийный маслонасос, **остановить основной**; аварийный работает **до выбега до 0**
⚠️ **Течи нет:** **основной оставить в работе**, проверить пуск аварийного
**3.** Убедиться: все стопорные и регулирующие **закрыты**, обратные клапаны выхлопа ЦВД **закрыты**, клапан сброса ЦВД **открыт**
**4.** Следить за выбегом, не допустить **выплавления вкладышей или заклинивания**. ⚠️ **Пожар управляем** — включить ВПУ на соответствующих оборотах; **неуправляем — ВПУ не включать**

**B. ТУШЕНИЕ И ИЗОЛЯЦИЯ (одновременно)**
**Порошковые, углекислотные или пенные** огнетушители. ⚠️ **Прямая подача воды СТРОГО ЗАПРЕЩЕНА** — масло легче воды, пожар растечётся.
**Бак** — накрыть горловину **кошмой**. **Течь на трубопроводе** — подавать в **корень очага**, растекание перекрыть **песком**.
Закрыть связи с другим оборудованием, **снять питание с зоны пожара**, убрать горючее (изоляция, замасленность).
**Охлаждать водой** соседние негорящие маслопроводы и стенки бака.

**C. БЕЗОПАСНОСТЬ И ПОСЛЕДУЮЩИЕ ДЕЙСТВИЯ**
Огнестойкая одежда, маска, термостойкие перчатки. При потере контроля — **немедленная эвакуация**.
⚠️ **Вентиляция включается, но наддув (положительное давление) СТРОГО ЗАПРЕЩЁН.**
⚠️ **Мобильные телефоны, рации и прочее искрообразующее в зоне пожара запрещены.**
После тушения — проверить течи, повреждение подшипников, коробление корпуса. **Только при отсутствии риска повторного возгорания** устранять течи и убирать место.
Зафиксировать время останова, место, ход тушения, состояние оборудования. **Пуск только после полного устранения дефекта и проверки.**

---

**🇬🇧 Oil System Fire — order of priority**

⚠️ **Operation priority: shutdown > fire extinguishing > isolation > protection**

**A. EMERGENCY SHUTDOWN (executed first)**
**1.** Manually press the **ETS emergency shutdown button**, confirm the "steam turbine trip" signal, and **break condenser vacuum** (open the breaker valve, stop the vacuum pump) to accelerate speed reduction
**2.** ⚠️ **If the lube oil system is leaking:** start the emergency lube oil pump and **stop the main lube oil pump**; run the emergency pump **until the turbine coasts down to 0**
⚠️ **If there is no leakage:** **keep the main pump in operation** and test that the emergency pump can start successfully
**3.** Confirm steam cutoff — HPSV, HPCV, IPSV, IPCV, LPSV, LPCV **closed**, HP exhaust check valves **closed**, HP vent valve **open**
**4.** Monitor rotor status closely during coastdown. Avoid **bearing burnout or jamming of the rotor due to oil cutoff**. ⚠️ **If the fire is controllable**, put the turning gear into operation at its activation speed; **if uncontrollable, suspend turning gear**

**B. FIRE EXTINGUISHING AND ISOLATION (simultaneous)**
Use **dry powder, carbon dioxide, or foam** extinguishers. ⚠️ **Directly spraying water is strictly prohibited** — oil is lighter than water and will spread the fire.
**Oil tank fire** — cover the tank opening with a **fire blanket** to suffocate it. **Pipe leakage fire** — spray at the **root of the fire source**, use **fire sand** to block oil from flowing and spreading.
Close connecting valves between the oil system and other equipment, **cut off power to the fire area** (to avoid electrical sparks igniting oil and gas), clear flammable materials nearby.
**Spray water to cool** unignited but adjacent oil pipes and tank walls.

**C. ON-SITE SAFETY AND FOLLOW-UP**
Fire-resistant clothing, protective mask, heat-resistant gloves. If the fire gets out of control, **evacuate immediately**.
⚠️ **Turn on ventilation, but positive pressure ventilation is strictly prohibited.**
⚠️ **Mobile phones, walkie-talkies and other spark-prone equipment are prohibited in the fire area.**
After extinguishing, check oil leakage points, bearing damage, and whether the casing is deformed by high temperature. **Only after confirming no risk of re-ignition**, handle the leakage points and clean up.
Record shutdown time, fire location, extinguishing process and equipment status. **Restart only after the fault is completely eliminated and inspection passed.**

`#oilfire #emergency #EBOP`

---
---

## POST 58 — Generator vodorod sizishi

**🇺🇿 H2 sizishi — aniqlash va harakat**

⚠️ **Vodorod portlash chegarasi: 4%–75%**
Javob mantig'i: **tez aniqlash va lokalizatsiya → izolyatsiya va portlashning oldini olish → manbani nazorat qilish → standart bartaraf etish**

**BELGILAR**
1. Vodorod tizimida **g'ayritabiiy bosim tushishi**, **to'ldirish chastotasining sezilarli oshishi**, nominal H2 bosimini ushlab turolmaslik
2. **Vodorod tozaligining tez pasayishi**, ruxsat etilgan diapazondan chiqishi (odatda **≥96%**), havodagi **kislorod miqdorining ortishi (≤2%)**
3. Sizish nuqtasidagi xarakterli belgilar: flanets va birikmalarda **yengil shivirlash**; **sovunli suv qo'yilganda uzluksiz pufakchalar**; yopiq joyda **o'tkir hid** — ⚠️ **vodorodning o'zi hidsiz, hid odatda uchuvchi yog'dan keladi**
4. **Vodorod sizish detektorlari alarmi** (statsionar yoki portativ) — alarm zonalari **generator uchki qopqoqlari, seal oil tizimi, vodorod quvurlari va klapan birikmalarida** to'plangan
5. Yopiq joylarda (generator otseki) **yonuvchi gaz alarmi**, o'ta og'ir holatlarda **mahalliy harorat ko'tarilishi**

**SABABLAR**
1. **Zichlash tizimi nosozliklari** — zichlash vkladishining yeyilishi, deformatsiyasi yoki ortiqcha zazori; **seal oil bosimining yetarli emasligi yoki tebranishi** → val zichlashidan sizish
2. **Konstruksiya defektlari** — quvur, klapan va flanetslar prokladkalarining eskirishi; **bolt bo'shashishi**; generator uchki qopqoqlarining yomon zichlanishi; **payvand yoriqlari**
3. **Noto'g'ri ekspluatatsiya** — vodorod to'ldirish va purgada **bosimni juda tez boshqarish** → quvurga zarba; ta'mirdan keyin zichlash yuzalarining to'liq tozalanmasligi, montaj chetlanishlari, **talab qilingan sinov va sizish tekshiruvining o'tkazilmasligi**
4. **Tashqi omillar** — **birlikning ortiqcha tebranishi** → birikmalarning bo'shashishi; **vodorod sovutgichlaridagi sizish** (vodorod va suv tomonlari orasida); korroziya → quvur devorining yupqalashishi
5. **Monitoring nosozligi** — detektorlarning kalibrlash chetlanishi yoki datchik nosozligi → erta sizishni aniqlamaslik

**HARAKAT — erta sizish, yonish/portlash yo'q**

*1. Shaxsiy himoya va izolyatsiya*
• Aloqasi yo'q xodimlarni **darhol chiqaring**
• Operatorlar **antistatik kiyim** va **portlashga chidamli asboblar** ishlatishi shart
• ⚠️ **Mobil telefon, ratsiya va uchqun beruvchi uskunalar taqiqlanadi**
• Generator otseki kabi yopiq joylarni yoping va **portlashga chidamli ventilyatsiyani yoqing**
• ⚠️ **Musbat bosimli ventilyatsiya QAT'IYAN TAQIQLANADI**

*2. Xavfli ishlarni to'xtatish*
Generator yaqinida **issiq ishlar, elektr payvandni darhol to'xtating**; zonadagi portlashga chidamli bo'lmagan elektr ta'minotini uzing, **ogohlantirish zonasini** o'rnating

*3. Manbani nazorat qilish*
• Generator vodorod bosimini **ruxsat etilgan minimal qiymatgacha tushiring** — sizishni kamaytirish uchun
• **Vodorod to'ldirishni to'xtating**, vodorod quvurlarining ajratish klapanlarini yoping
• ⚠️ **Seal oil tizimining normal ishlashini saqlang, seal oil bosimini vodorod bosimidan belgilangan farqga yuqori qilib sozlang**

*4. Aniqlash va lokalizatsiya*
**Portativ vodorod detektorlari** bilan sizish nuqtasini aniq toping, diapazonni belgilang, **sizish tezligini** aniqlang

**KEYINGI ISHLOV — sizish nazorat ostiga olingach**

*Darajaga qarab*
• **Kichik sizish** (bosim sekin tushadi, tozalik barqaror) → birlikni **past yuklamada ishlatgan holda** maqsadli ta'mir (boltlarni tortish, prokladka almashtirish)
• **Jiddiy sizish** (bosim tez tushadi, tozalik keskin pasayadi) → ⚠️ **birlikni darhol to'xtating** va protsedura bo'yicha vodorodni **CO2 yoki azot** oraliq muhiti bilan purga qiling va almashtiring

*Ta'mir*
⚠️ **Vodorod almashtirish sifatli bo'lgandan keyin (vodorod miqdori ≤0.4%)** sizish nuqtasini ta'mirlang — shikastlangan zichlash va prokladkalarni almashtiring, zichlash vkladishi yoki quvurlarni ta'mirlang, payvand yoriqlarini payvandlang, **bosim sinovini o'tkazing**

*Qayta tekshirish*
Ta'mirdan keyin **germetiklik sinovi**, **sovunli suv yoki detektor bilan to'liq tekshiruv**.
⚠️ **Vodorod qayta to'ldirilayotganda bosim ko'tarilish tezligini nazorat qiling: ≤0.02 MPa/min**, nominal bosim va tozalikni **asta tiklang**

**OLDINI OLISH**
• **Kunlik:** detektorlarni, bosim/tozalik asboblarini muntazam kalibrlang; **seal oil bosimi, H2 bosimi va tozaligini har kuni tekshiring, tendensiyani qayd eting**
• **Muntazam TO:** prokladka va seal oil filtrlarini davriy almashtiring; zichlash vkladishi holatini tekshiring; **har bir TO siklida vodorod quvurlari va klapanlarining germetiklik sinovi**
• **Standart operatsiya:** to'ldirish va purgada **"bosimni sekin ko'tarish/tushirish va to'liq almashtirish"** tamoyiliga qat'iy rioya qiling. Ta'mirdan keyin **uch bosqichli sizish tekshiruvi (sovunli suv, detektor, gaz tahlili)** ishga tushirishdan oldin bajarilishi shart
• **Muhit:** generator zonasini quruq va yaxshi shamollatilgan holda saqlang; **birlik tebranishini ruxsat etilgan diapazonda ushlang** — birikmalar bo'shashmasligi uchun

---

**🇷🇺 Утечка водорода — обнаружение и действия**

⚠️ **Пределы взрываемости водорода: 4%–75%**
Логика: **быстрое обнаружение и локализация → изоляция и взрывобезопасность → контроль источника → штатное устранение**

**ПРИЗНАКИ**
Аномальное **падение давления**, рост частоты подпитки, невозможность держать номинал | **Быстрое падение чистоты** (норма **≥96%**), **рост кислорода (≤2%)** | **Шипение** на фланцах, **пузыри** от мыльного раствора, **резкий запах** в замкнутом объёме — ⚠️ **сам водород без запаха, запах даёт летучее масло** | **Сигналы газоанализаторов** у **торцевых щитов, системы уплотняющего масла, водородных трубопроводов и арматуры** | **Сигнал горючего газа** в отсеках, в крайних случаях — локальный нагрев

**ПРИЧИНЫ**
Износ, деформация или увеличенный зазор **уплотняющего вкладыша**; **недостаточное или колеблющееся давление уплотняющего масла** | Старение прокладок, **ослабление болтов**, плохое уплотнение торцевых щитов, **трещины сварных швов** | **Слишком быстрое изменение давления** при заполнении и вытеснении; невычищенные поверхности после ремонта, отклонения при сборке, **непроведённые опрессовка и течеискание** | **Повышенная вибрация**, **межконтурная течь водородных охладителей**, коррозионное утонение стенок | **Отказ или расстройка газоанализаторов**

**ДЕЙСТВИЯ (ранняя утечка, без возгорания)**
Вывести посторонних, **антистатическая одежда**, **взрывобезопасный инструмент**; ⚠️ **телефоны и рации запрещены**; закрыть отсеки, включить **взрывозащищённую вентиляцию**; ⚠️ **наддув СТРОГО ЗАПРЕЩЁН**
Немедленно прекратить **огневые и сварочные работы**, снять невзрывозащищённое питание, выставить **ограждение**
**Снизить давление водорода до минимально допустимого**, прекратить подпитку, закрыть отсечные; ⚠️ **держать уплотняющее масло выше давления водорода на заданный перепад**
**Портативным течеискателем** найти точку, отметить зону, определить **скорость утечки**

**ПОСЛЕДУЮЩЕЕ**
**Малая утечка** (медленное падение, чистота стабильна) → ремонт **на пониженной нагрузке** | **Сильная утечка** → ⚠️ **немедленный останов**, вытеснение через **CO2 или азот**
⚠️ **Ремонт после качественного замещения (водород ≤0.4%)**: замена уплотнений и прокладок, ремонт вкладыша и трубопроводов, заварка трещин, **опрессовка**
После ремонта — **испытание на плотность**, полное течеискание. ⚠️ **Скорость подъёма давления при заполнении ≤0.02 МПа/мин**

**ПРОФИЛАКТИКА**
Регулярная поверка газоанализаторов; **ежедневный контроль давления уплотняющего масла, давления и чистоты H2 с записью тренда** | Периодическая замена прокладок и фильтров, осмотр вкладыша, **опрессовка трубопроводов каждый ремонтный цикл** | ⚠️ **«Медленный подъём/сброс давления и полное замещение»**; после ремонта — **трёхуровневое течеискание (мыльный раствор, течеискатель, газовый анализ)** | Сухая вентилируемая зона, **вибрация в допуске**

---

**🇬🇧 Generator Hydrogen Leakage — detection and response**

⚠️ **Hydrogen explosion limit: 4%–75%**
Core logic: **rapid detection and positioning → isolation and explosion prevention → source control and risk reduction → standardized disposal**

**PHENOMENA**
Abnormal **pressure drop**, significantly increased replenishment frequency, rated pressure cannot be maintained | **Rapid decrease in purity** beyond the allowable range (generally **≥96%**), **excessive oxygen content (≤2%)** | Leak point signs: **slight hissing** at flanges and joints, **continuous bubbles** with soapy water, a **pungent odour** in enclosed spaces — ⚠️ **hydrogen itself is odourless; the smell usually comes from volatile oil** | **Leak detector alarms** concentrated at **generator end covers, seal oil systems, hydrogen pipelines and valve interfaces** | **Combustible gas alarms** in enclosed areas, with local temperature rise in extreme cases

**COMMON CAUSES**
**Seal system failures** — wear, deformation or excessive clearance of the sealing bush; **insufficient or fluctuating seal oil pressure** | **Structural defects** — aged gaskets, **loose bolts**, poor end cover sealing, **cracked welds** | **Improper operation** — **excessively fast pressure control** during charging and purging causing pipeline impact damage; incomplete cleaning after maintenance, assembly deviations, **pressure testing and leak detection not performed** | **External factors** — excessive vibration loosening joints, **hydrogen cooler cross-leakage**, corrosion thinning pipe walls | **Monitoring failures** — calibration deviation or sensor faults missing early leaks

**RESPONSE (early leakage, no combustion)**
Evacuate irrelevant personnel; operators wear **anti-static clothing** and use **explosion-proof tools**; ⚠️ **phones and walkie-talkies prohibited**; close enclosed spaces and activate **explosion-proof ventilation**; ⚠️ **positive pressure ventilation strictly prohibited**
Immediately stop **hot work and electric welding** near the generator; cut off non-explosion-proof supplies; set up **warning zones**
**Reduce hydrogen pressure to the minimum allowable value**; suspend replenishment; close pipeline isolation valves; ⚠️ **keep the seal oil system running with seal oil pressure above hydrogen pressure by the specified difference**
Use **portable detectors** to locate the point, mark the range, determine the **leakage rate**

**SUBSEQUENT TREATMENT**
**Minor leak** (slow pressure drop, stable purity) → targeted repair while the unit stays at **low load** | **Severe leak** (rapid drop, sharp purity decline) → ⚠️ **shut down immediately**, purge and replace using **CO2 or nitrogen** as intermediate medium
⚠️ **Repair only after qualified replacement (hydrogen content ≤0.4%)** — replace seals and gaskets, repair the sealing bush or pipelines, weld cracked welds, **conduct pressure testing**
After repair, **air tightness tests** and full detection with soapy water or detectors. ⚠️ **When recharging, control pressure rise rate at ≤0.02 MPa/min**

**PREVENTION**
Regularly calibrate detectors and pressure/purity instruments; **check seal oil pressure, H2 pressure and purity daily and record trend data** | Replace gaskets and seal oil filters periodically, inspect the sealing bush, **conduct air tightness tests on pipelines and valves each maintenance cycle** | ⚠️ Strictly follow **"slow pressure rise/drop and thorough replacement"**; after maintenance, **three-level leak detection (soapy water, leak detector, gas analysis)** before commissioning | Keep the area dry and well-ventilated; **control vibration within the allowable range**

`#hydrogen #leakage #explosionlimit #sealoil`

---
---

## POST 59 — TSI: o'q siljishi monitoringi

**🇺🇿 O'q siljishi — nima uchun bu "himoya chizig'i"**

⚠️ **Rotor va stator (diafragma, soplo, bug' zichlashi) orasidagi radial va o'q zazorlari juda kichik — odatda atigi 0.1–0.5 mm.**

**O'q siljishi chegaradan chiqsa nima bo'ladi**
• **Statik-dinamik ishqalanish** — rotor ish g'ildiragi, vtulka va diafragma, zichlash korpusi to'qnashadi → qismlar yeyiladi, deformatsiyalanadi, og'ir holatda **rotor egiladi**
• **Uskuna shikasti** — ishqalanishdan hosil bo'lgan yuqori harorat **metall qismlarni eritishi**, hatto **turbina korpusining yorilishiga** olib kelishi mumkin

**O'q siljishi nimani erta ogohlantiradi**
O'q siljishining mohiyati — **rotorning o'q kuchi muvozanatsizligining namoyon bo'lishi**. Siljishni kuzatib quyidagi yashirin nosozliklarni bilvosita aniqlash mumkin:
• **Upor podshipnik yeyilishi/kuyishi** — upor pad o'q kuchini muvozanatlaydigan asosiy element, yeyilishi bevosita rotorning o'q bo'yicha siljishiga olib keladi va siljish qiymati oshadi
• **Oqim yo'li nosozliklari** — kurak cho'kmasi, sinishi yoki diafragma deformatsiyasi bug' oqim maydonini o'zgartiradi → **o'q kuchining keskin o'zgarishi**
• **Vakuum tizimi sizishi / yuklamaning keskin o'zgarishi** — vakuum tushishi, kirish parametrlari tebranishi yoki yuklamaning keskin o'zgarishi **o'q kuchi muvozanatini buzadi**

**Ikki bosqichli himoya**
1. **"Katta o'q siljishi" alarmi** → operatorni ogohlantiradi
2. Siljish **xavf chegarasiga** yetsa → himoya tizimi **kirish bug'ini darhol uzadi** va majburiy to'xtatadi

**Setpointlar (Table 8-1-1)**: alarm **±0.762 mm**, trip **±0.889 mm**
⚠️ Zazor **0.1–0.5 mm**, trip esa **0.889 mm** — ya'ni trip nuqtasi zazordan kattaroq. Bu upor podshipnik pad qalinligi va zazor taqsimotini hisobga oladi, lekin **alarm chiqqanda allaqachon zazorlar ichida bo'lishingiz mumkin**.

---

**🇷🇺 Осевой сдвиг — почему это «рубеж обороны»**

⚠️ **Радиальные и осевые зазоры ротор-статор (диафрагмы, сопла, уплотнения) крайне малы — обычно 0.1–0.5 мм.**

**При превышении**
• **Задевание** — диски, втулки, диафрагмы, корпуса уплотнений соприкасаются → износ, деформация, в тяжёлом случае **изгиб ротора**
• **Повреждение** — тепло от трения может **расплавить металл** и даже **привести к трещине цилиндра**

**О чём предупреждает заранее**
Осевой сдвиг — это проявление **дисбаланса осевого усилия**:
• **Износ/выплавление упорного** — колодка балансирует осевое усилие, износ даёт сдвиг ротора
• **Дефекты проточной части** — отложения, обрыв лопаток, деформация диафрагм меняют поле потока → **скачок осевого усилия**
• **Присосы в вакуумной системе / резкое изменение нагрузки** — нарушают баланс осевого усилия

**Две ступени**
1. Сигнал **«большой осевой сдвиг»**
2. При достижении **опасного порога** — **немедленная отсечка пара** и останов

**Уставки**: сигнал **±0.762 мм**, защита **±0.889 мм**
⚠️ Зазоры **0.1–0.5 мм**, а защита на **0.889 мм**. Это учитывает толщину колодок и распределение зазоров, но **при появлении сигнала вы уже можете быть в зоне зазоров**.

---

**🇬🇧 Axial Displacement Monitoring — the defence line**

⚠️ **Radial and axial clearances between rotor and stator (diaphragms, nozzles, steam seals) are extremely small — usually only 0.1–0.5 mm.**

**What an overrun does**
• **Static and dynamic friction** — rotor impeller, sleeve, diaphragm and seal body collide → wear, deformation, and in serious cases **rotor bending**
• **Equipment damage** — friction heat may **melt metal parts**, or even **crack the turbine cylinder**

**What it warns about early**
Axial displacement is the expression of **axial thrust imbalance**:
• **Thrust bearing wear or burn** — the pad balances axial thrust; wear moves the rotor axially and the reading rises
• **Flow passage faults** — blade scaling, breakage, or diaphragm deformation change the steam flow field → **sudden change of axial thrust**
• **Vacuum leakage or sudden load change** — vacuum drop, inlet parameter fluctuation or load swing **destroys the axial thrust balance**

**Two protection stages**
1. **"Large axial displacement" alarm** to the operator
2. On reaching the **danger threshold**, protection **cuts off inlet steam immediately** and forces shutdown

**Settings**: alarm **±0.762 mm**, trip **±0.889 mm**
⚠️ Clearances are **0.1–0.5 mm** but the trip is at **0.889 mm**. That accounts for pad thickness and clearance distribution — but **by the time the alarm comes in you may already be inside the clearances**.

`#TSI #axialdisplacement #thrustbearing`

---
---

## POST 60 — TSI: rotor va korpus kengayishi

**🇺🇿 Rotor kengayishi va differensial kengayish — nima uchun farq qiladi**

**Rotor va korpus nega turlicha kengayadi**
1. ⚠️ **Korpus rotorga nisbatan ancha massiv** (termik massasi katta) → **yengilroq rotor haroratini va uzunligini tezroq o'zgartiradi**
2. **Korpus rotordan boshqa marka po'latdan** yasalgan → **termik kengayish koeffitsienti boshqa**
3. ⚠️ **Rotor bug' bilan o'ralgan** — issiqlik rotorga kiradi, chiqadi va o'tadi, to bug' harorati bilan tenglashguncha. **Korpus esa ichkaridan qiziydi va tashqi muhitga izolyatsiya orqali issiqlik beradi.** Natijada **korpusning o'rtacha harorati rotornikidan PAST bo'ladi**
4. Differensial kengayish datchiklari **upor podshipnikdan kamida bitta val uzoqlikdagi** nisbiy o'sishni o'lchaydi. Ba'zi datchiklar **o'q bo'yicha harakatlanadigan** qismlarga, ba'zilari **deyarli qo'zg'almas** qismlarga o'rnatilgan

**Rotor kengayishi monitoringisiz nima bo'ladi**
*Sovuq ishga tushirishda* — rotor **juda sekin** kengaysa yoki korpus **juda tez** kengaysa → o'q yoki radial zazor (zichlash, diafragma) kichrayadi → og'ir holatda **rotor bilan zichlash tishlari va diafragma orasida ishqalanish** → qism yeyiladi, **tebranish kuchayadi**
*Issiq holatda to'xtatish yoki yuklama tushirishda* — rotorning **tez qisqarishi** radial zazorning g'ayritabiiy oshishiga olib keladi. Ishqalanish darhol bo'lmasa ham **bug' zichlashi sizishi keskin oshadi va FIK tushadi**. Qisqarish notekis bo'lsa — **rotor egilish xavfi**

**Termik holat barqarormi — qanday bilish**
• Rotor kengayish egri chizig'i **loyihaviy qiymatdan chetlashsa** (masalan qizdirishda kengayish juda sekin) — bug' parametrlari anomaliyasi, **yomon drenaj** yoki qizdirish tizimi nosozligi bo'lishi mumkin
• ⚠️ **Kengayish qiymati uzoq vaqt yuklama va harorat bilan o'zgarmasa** — rotor va korpus orasida **begona jism** bo'lishi mumkin, yoki **podshipnik juda tarang o'rnatilgan**. Tekshirish uchun to'xtatish kerak

**Korpus kengayishi**
HP-IP-LP korpuslari atmosfera sharoitidan to'liq yuklamagacha haroratlari o'zgargani uchun **sezilarli kengayadi**. Kengayish **cheklangan yoki to'sib qo'yilgan** bo'lsa, natijadagi korpus deformatsiyasi **rotor o'q zazorlari, journal podshipnik tekislanishi, tebranish yoki podshipnik yuklanishida** muammo beradi.
Eski va katta birliklar uchun odatiy: **statsionar korpusning o'q bo'yicha joylashuvi turbina exhaust markaz chizig'i yaqinidagi kalitlar yoki ankerlar bilan belgilanadi**.

⚠️ **DXD setpointlari:** H **+11.07**, HH **+12.07**, L **−8.26**, LL **−9.26 mm**
⚠️ **Rotor kengayishi:** H **+44.5**, HH **+45.5**, L **−22.1**, LL **−23.1 mm**

---

**🇷🇺 Расширение ротора и ОРС — почему они расходятся**

**Почему ротор и корпус расширяются по-разному**
1. ⚠️ **Корпус массивнее ротора** (больше тепловая масса) → **лёгкий ротор меняет температуру и длину быстрее**
2. **Корпус из другой марки стали** → **другой коэффициент расширения**
3. ⚠️ **Ротор окружён паром** и прогревается насквозь до температуры пара. **Корпус греется изнутри и отдаёт тепло наружу через изоляцию.** Поэтому **средняя температура корпуса НИЖЕ, чем ротора**
4. Датчики ОРС меряют относительный рост **не ближе одного вала от упорного**; часть стоит на **осевом подвижном**, часть — на **практически неподвижном**

**Без контроля расширения ротора**
*Холодный пуск* — ротор растёт **слишком медленно** или корпус **слишком быстро** → зазоры уменьшаются → **задевание о гребни уплотнений и диафрагмы**, износ, **рост вибрации**
*Останов или разгрузка из горячего* — **быстрое сжатие ротора** → аномальный рост радиального зазора → **резкий рост протечек и падение КПД**; при неравномерном сжатии — **риск изгиба**

**Стабилен ли тепловой режим**
• Отклонение кривой расширения от проектной — аномалия параметров пара, **плохое дренирование**, отказ прогрева
• ⚠️ **Если расширение долго не меняется при изменении нагрузки и температуры** — возможен **посторонний предмет** между ротором и корпусом либо **слишком тугая посадка подшипника**. Нужен останов на осмотр

**Расширение корпуса**
Корпуса ВД-СД-НД расширяются **значительно**. При **ограничении расширения** коробление даёт проблемы с **осевыми зазорами, центровкой опорных подшипников, вибрацией и нагрузкой подшипников**. Осевое положение корпуса фиксируется **шпонками или анкерами у оси выхлопа**.

⚠️ **ОРС:** H **+11.07**, HH **+12.07**, L **−8.26**, LL **−9.26 мм**
⚠️ **Расширение ротора:** H **+44.5**, HH **+45.5**, L **−22.1**, LL **−23.1 мм**

---

**🇬🇧 Rotor and Shell Expansion Monitoring**

**Why rotor and shell grow differently**
1. ⚠️ **The shell is frequently more massive** (more thermal mass) than the rotor cross-section → **the lighter rotor changes temperature and length more rapidly**
2. **The shell is a different grade of steel** → **different thermal expansion coefficient**
3. ⚠️ **The rotor is surrounded by steam** and heat transfers into, out of and through it until it matches steam temperature. **The shell is heated from the inside and transfers heat outward through insulation.** So the **shell's average temperature is less than the rotor's**
4. DE detectors monitor relative growth **at least one shaft away from the thrust bearing**; some are mounted in components that **move axially**, some in components that are **essentially fixed**

**Without expansion monitoring**
*Cold start-up* — if the rotor expands too slowly or the cylinder too fast, **axial or radial clearance shrinks** → **friction between rotor and seal teeth or diaphragm**, component wear, **intensified vibration**
*Hot shutdown or load reduction* — **rapid rotor shrinkage** raises radial clearance abnormally. Even without direct friction it causes a **sharp increase in steam seal leakage and lower efficiency**. Non-uniform shrinkage brings **rotor bending risk**

**Is the thermal state stable**
• If the rotor expansion curve **deviates from design** (e.g. expansion too slow when heating), suspect abnormal steam parameters, **poor drainage**, or heating system failure
• ⚠️ **If the expansion value does not change with load and temperature for a long time**, there may be **foreign material between rotor and cylinder**, or the **bearing installation is too tight** — stop for inspection

**Shell expansion**
HP-IP-LP shells expand significantly from ambient to full load. If shell expansion is **restricted or limited**, the resulting distortion produces issues with **rotor axial clearances, journal bearing alignment, vibration, or bearing loading**. Shell axial location is held by **keys or anchors near the turbine exhaust centreline**.

⚠️ **DE:** H **+11.07**, HH **+12.07**, L **−8.26**, LL **−9.26 mm**
⚠️ **Rotor expansion:** H **+44.5**, HH **+45.5**, L **−22.1**, LL **−23.1 mm**

`#TSI #differentialexpansion #rotorexpansion`

---
---

## POST 61 — Turbina kuchlanish monitoringi

**🇺🇿 Stress monitoring — raqamli chegaralar**

**Ikki turdagi kuchlanish va xavfli joylar**

*1. Rotor (ayniqsa HP rotori) — termik kuchlanish (asosiy) + mexanik*
• Ishga tushirish/to'xtatish/yuklama o'zgarishida **rotorning ichki va tashqi devorlari orasidagi harorat farqi katta** — masalan sovuq ishga tushirishda **ichki devor tez, tashqi devor sekin qiziydi** → **termik cho'zuvchi kuchlanish**
• Yuqori tezlikda aylanishda **markazdan qochma kuch** (mexanik kuchlanish)

*2. Silindr (HP, IP) — termik kuchlanish asosiy*
• **Silindr devori qalinligi notekis** (flanets qalin, korpus yupqa) → qizish/sovish tezligi farqi katta → **flanets va korpus orasida termik kuchlanish**
• **Ichki va tashqi silindr orasidagi harorat farqidan cheklovchi kuchlanish**
⚠️ **HP silindrning ichki va tashqi devorlari orasidagi harorat farqini ≤30–50°C da ushlang** — silindr deformatsiyasi, bug' sizishi yoki yorilishining oldini olish uchun

**Kuchlanish qanday hisoblanadi**
Bevosita o'lchab bo'lmaydi. Harorat, tezlik va yuklama kabi **bilvosita parametrlar** ishlab chiqaruvchining **kuchlanish hisoblash modeli** bilan birlashtiriladi.
1. Termik kuchlanish **qismning ichki-tashqi devor harorat farqi** va **yuqori-pastki korpus harorat farqi**ga **to'g'ri proporsional**
2. **Ish rejimi o'zgarish tezligi orqali boshqarish:**
 • Ishga tushirish/to'xtatishda **qizdirish tezligi ≤1.5–2.5°C/min**
 • Yuklama o'zgarishida **nominal yuklamada ≤2.5%/min**
3. **Yuqori chegara material resursi bo'yicha** — rotor va silindr materialiga (masalan **CRMOV po'lati**) ko'ra **ruxsat etilgan maksimal kuchlanish** va **jamlangan charchash resursi sarfi** belgilanadi. Tizim **avtomatik alarm beradi** va ish rejimi o'zgarish tezligini cheklaydi

**Yuqori xavfli rejimlar**
1. ⚠️ **Sovuq/issiq ishga tushirish** — termik kuchlanish eng yuqori. **Sovuq ishga tushirishda main bug' harorati qizdirish tezligi ≤2°C/min**
2. ⚠️ **O'ta issiq ishga tushirish** (to'xtatishdan bir necha soat keyin qayta ishga tushirish) — rotor hali issiq, silindr tez sovigan → **rotor va silindr orasida harorat farqi** oson yuzaga keladi. Kirish bug' parametrlarini sozlab **rotorning sovishdan siquvchi kuchlanish olishini** oldini olish kerak
3. ⚠️ **Tez yuklama o'zgarishi** (tarmoq pik talabi) — **pik rostlashda yuklama o'zgarish tezligi ≤3%/min**
4. ⚠️ **Yuklama tashlash** — bug' sarfi keskin kamayadi, rotor va silindr tez soviydi, **almashuvchi termik kuchlanish** yuzaga keladi. **Ikkinchi ishga tushirishda kuchlanishlarning ustma-ust tushishining** oldini olish kerak

**Kuchlanish chegaradan chiqqanda — 3 ta harakat**
1. **Ish rejimi o'zgarish tezligini kamaytiring** — qizdirish bosqichida bo'lsa, main bug' qizdirish tezligini darhol sekinlashtiring
2. **Bug' parametrlarini barqarorlashtiring** — qozon chiqishidagi bug' harorati va bosimi barqarorligini tekshiring. ⚠️ **Main bug' harorati tebranishi ≤±5°C/min**
3. **Qizdirish/doimiy harorat vaqtini uzaytiring** — ishga tushirish/to'xtatish bosqichida bo'lsa **past tezlikda yoki yuqori tezlikda qizdirish vaqtini uzaytiring**, rotor va silindr harorati tenglashsin

⚠️ Bir joyga to'plangan tezlik chegaralari: **qizdirish 1.5–2.5°C/min** (sovuq startda **2°C/min**), **yuklama nominalda 2.5%/min**, **pik rostlashda 3%/min**, **bug' harorati tebranishi ±5°C/min**, **HP ichki-tashqi devor farqi 30–50°C**.

---

**🇷🇺 Контроль напряжений — числовые пределы**

**Два вида напряжений и опасные места**
*Ротор (особенно ЦВД)* — термические (главные) + механические: **большая разница температур внутренней и наружной стенки** при пусках и переменной нагрузке (при холодном пуске внутренняя греется быстро, наружная медленно → **термические растягивающие напряжения**) плюс **центробежные силы**
*Цилиндры ВД/СД* — термические (главные): **неравномерная толщина стенки** (фланец толстый, корпус тонкий) → разная скорость прогрева → **напряжения между фланцем и корпусом**; **стеснённые напряжения от разницы температур внутреннего и наружного цилиндров**
⚠️ **Разницу температур внутренней и наружной стенки ЦВД держать ≤30–50°C**

**Как считается**
Напрямую не измеряется. Считают по **косвенным параметрам** и модели изготовителя.
1. Термические напряжения **прямо пропорциональны** разнице температур стенок и разнице верх/низ цилиндра
2. **Управление через скорость изменения режима:** прогрев **≤1.5–2.5°C/мин**, изменение нагрузки на номинале **≤2.5%/мин**
3. **Верхний предел по ресурсу материала** (например **сталь CRMOV**): задаются **допустимое максимальное напряжение** и **накопленный расход усталостного ресурса**; система **автоматически сигнализирует** и ограничивает скорость

**Опасные режимы**
⚠️ **Холодный/горячий пуск** — при холодном **скорость прогрева главного пара ≤2°C/мин**
⚠️ **Очень горячий пуск** (через несколько часов) — ротор горячий, цилиндр остыл → **разница ротор-цилиндр**; регулировать параметры пара, не допустить **сжимающих напряжений от захолаживания**
⚠️ **Быстрое изменение нагрузки** — при пиковом регулировании **≤3%/мин**
⚠️ **Сброс нагрузки** — резкое падение расхода, ускоренное остывание, **знакопеременные напряжения**; не допускать **наложения напряжений при повторном пуске**

**При превышении — 3 действия**
1. **Снизить скорость изменения режима** — замедлить прогрев главного пара
2. **Стабилизировать параметры** — ⚠️ **колебания температуры главного пара ≤±5°C/мин**
3. **Продлить время прогрева/выдержки** на низких или высоких оборотах для выравнивания температур

⚠️ Все скорости в одном месте: **прогрев 1.5–2.5°C/мин** (холодный пуск **2**), **нагрузка 2.5%/мин**, **пик 3%/мин**, **колебания температуры ±5°C/мин**, **разница стенок ЦВД 30–50°C**.

---

**🇬🇧 Turbine Stress Monitoring — the numeric limits**

**Two kinds of stress and the high-risk parts**
*Rotor (especially HP)* — thermal (dominant) plus mechanical: **large temperature difference between inner and outer walls** during start-stop and load change (on cold start the inner wall heats quickly and the outer slowly, producing **thermal tensile stress**), plus **centrifugal force**
*Cylinders (HP, IP)* — thermal dominant: **uneven wall thickness** (flange thick, block thin) gives different heating rates → **thermal stress between flange and block**; plus **restraint stress from inner-to-outer cylinder temperature difference**
⚠️ **Control HP cylinder inner-to-outer wall temperature difference to ≤30–50°C** to prevent deformation, steam leakage or cracking

**How stress is calculated**
It cannot be measured directly. It is computed from **indirect parameters** (temperature, speed, load) with the manufacturer's preset stress model.
1. Thermal stress is **directly proportional** to inner/outer wall difference and upper/lower cylinder difference
2. **Control by rate of change of working condition:** heating rate at start-up and shutdown **≤1.5–2.5°C/min**; load change rate at rated load **≤2.5%/min**
3. **Upper limit set by material life** — for rotor and cylinder material (e.g. **CRMOV steel**) an **allowable maximum stress** and **cumulative fatigue life consumption** are set; the system **alarms automatically** and limits the rate of change

**High-risk conditions**
⚠️ **Cold/hot start** — highest thermal stress; on cold start **main steam heating rate ≤2°C/min**
⚠️ **Extremely hot start** (restart within a few hours) — rotor still hot, cylinder cooled quickly, **rotor-to-cylinder temperature difference** develops easily; adjust inlet steam parameters to prevent **compressive stress from cooling the rotor**
⚠️ **Rapid load change** (grid peak demand) — **load change rate ≤3%/min during peak load regulation**
⚠️ **Load rejection** — steam flow drops sharply, rotor and cylinder cool faster, **alternating thermal stress** occurs; prevent **stress superposition during the second start-up**

**When stress exceeds the limit — three actions**
1. **Reduce the rate of change** — in the heating stage, immediately slow the main steam heating rate
2. **Stabilize steam parameters** — ⚠️ **main steam temperature fluctuation ≤±5°C/min**
3. **Extend warm-up / constant temperature time** — extend low-speed or high-speed warm-up so rotor and cylinder temperatures even out

⚠️ All rate limits in one place: **heating 1.5–2.5°C/min** (cold start **2**), **load 2.5%/min**, **peak regulation 3%/min**, **steam temperature fluctuation ±5°C/min**, **HP wall difference 30–50°C**.

`#stressmonitoring #CRMOV #liferate`

---
---

## POST 62 — Kurak shikastlanishi

**🇺🇿 Kurak shikasti yoki sinishi — belgilar**

**1. G'ayritabiiy tebranish va shovqin**

*Tebranishning sezilarli oshishi*
Shikastlangan kurakli rotorning **radial tebranish qiymati me'yordan ancha oshadi**. Podshipnik korpusi va silindr blokida **aniq tebranish** yuzaga keladi, va **tebranish chastotasi kurak aylanish chastotasi bilan bog'liq**.

*Xarakterli shovqin*
Ish davomida **"metall zarba shovqini"**, **"ishqalanish shovqini"** yoki **"yuqori chastotali hushtak tovushi"** eshitiladi.
⚠️ **Sinib tushgan kurak oqim kanalida qotib qolsa — "qirish tovushi" qo'shiladi, va yuklama o'zgarganda shovqin kuchayadi.**

**2. G'ayritabiiy ish parametrlari**
⚠️ **Bir bosqich guruhining kirish va exhaust bug'i orasidagi harorat farqi KAMAYADI**, va bug' sarfi g'ayritabiiy bo'ladi — **bir xil yuklamada sarf yuqoriroq**. Og'ir holatda **birlik chiqishi kamayadi**.

**3. Ko'z bilan ko'riladigan izlar**

*Exhaust da begona jismlar*
⚠️ **Kondensator hot well ida yoki exhaust chiqishida metall qipiqlar va kurak parchalari (asosan tartibsiz plastinkalar) topiladi.**

*Val zichlashi bug' sizishining oshishi*
Kurak sinishi **rotor muvozanatini buzadi** → val markazi og'adi → **val zichlashi va rotor orasidagi zazor oshadi** → val zichlashi bug' sizishi ko'payadi, joyida **oq bug'** ko'rinadi.

⚠️ **Diqqat: tebranish chastotasi kurak aylanish chastotasi bilan bog'liq bo'lishi — bu 1× dan farq qiladi.** POST 18 dagi muvozanatsizlik 1× da, ishqalanish kritik tezlikda, oil whip 0.5× da. Kurak shikasti esa **kurak o'tish chastotasida** ko'rinadi. Spektrni shu bo'yicha qarang.

⚠️ **Bir bosqich guruhida harorat farqining KAMAYISHI** — bu juda o'ziga xos belgi. Kurak yo'q bo'lsa o'sha bosqichda ish bajarilmaydi, demak bug' issiqroq chiqadi.

---

**🇷🇺 Повреждение или обрыв лопаток — признаки**

**1. Аномальная вибрация и шум**
*Рост вибрации* — **радиальная вибрация ротора существенно выше нормы**, заметная вибрация корпуса подшипника и цилиндра, **частота вибрации связана с частотой вращения лопаток**
*Шум* — **металлический удар**, **трение** или **высокочастотный свист**. ⚠️ **Застрявшая в канале лопатка даёт «скребущий» звук, усиливающийся при изменении нагрузки**

**2. Аномальные параметры**
⚠️ **Разница температур на входе и выхлопе одной группы ступеней СНИЖАЕТСЯ**, расход пара аномален — **выше при той же нагрузке**. В тяжёлом случае **падает мощность**.

**3. Видимые следы**
⚠️ **В конденсатосборнике или у выхлопа находят металлическую стружку и обломки лопаток (обычно неправильной пластинчатой формы)**
Обрыв нарушает балансировку → смещение центра валопровода → **рост зазора уплотнений** → **больше протечек, белый пар у уплотнения**

⚠️ **Частота связана с лопаточной, а не с 1×.** Небаланс — 1×, задевание — на критической, масляная вибрация — 0.5×, повреждение лопаток — **на лопаточной частоте**.

⚠️ **Снижение перепада температур по группе ступеней** — очень специфичный признак: нет лопаток — нет работы на ступени, пар выходит горячее.

---

**🇬🇧 Blade Damage or Fracture — phenomena**

**1. Abnormal vibration and noise**
*Vibration increase* — radial vibration of the rotor with damaged blades **far exceeds standard**; obvious vibration at the bearing housing and cylinder block, and **the vibration frequency is related to the blade rotation frequency**
*Characteristic noise* — **"metallic impact noise"**, **"friction noise"** or **"high-frequency whistling sound"**. ⚠️ **If a fractured blade gets stuck in the flow channel it is accompanied by a "scraping sound", which becomes more intense when the load changes**

**2. Abnormal operating parameters**
⚠️ **The temperature difference between inlet and exhaust steam of the same stage group DECREASES**, and steam flow is abnormal — **higher flow under the same load**. In severe cases, **unit output decreases**.

**3. Visually observable traces**
⚠️ **Metal debris and blade fragments (mostly irregular flakes) can be found in the condenser hot well or exhaust port**
Fracture damages rotor balance → shafting centre deviates → **gap between shaft seal and rotor increases** → shaft seal steam leakage increases, **white steam visible at the shaft seal**

⚠️ **The frequency relates to blade passing, not 1×.** Unbalance is 1×, rubbing shows near critical, oil whip at 0.5×, blade damage at **blade passing frequency**. Read the spectrum accordingly.

⚠️ **A DECREASING temperature drop across a stage group** is a very specific indicator: with blades missing, that stage does no work, so steam leaves hotter.

`#bladedamage #vibration #stagegroup`

---
---

## POST 63 — Exhaust haroratining oshishi

**🇺🇿 Exhaust harorati yuqori — parametr korrelyatsiyasi**

**BELGILAR**

*1. Harorat chegaradan chiqishi*
⚠️ **Normal sharoitda exhaust harorati kondensator aylanma suvining chiqish haroratidan 3–5°C yuqori bo'lishi kerak.**
Nosozlikda exhaust harorati ko'pincha **50°C dan oshadi**, past yuklamada hatto **60°C dan** ham.

*2. Vakuumning bir vaqtda tushishi*
⚠️ **Exhaust harorati vakuum darajasi bilan teskari bog'langan: har 1°C harorat oshishiga vakuum taxminan 1–2 kPa tushadi.**
Misol: exhaust harorati **40°C dan 50°C ga** ko'tarilsa, vakuum **−95 kPa dan −85 kPa dan pastga** tushishi mumkin.

*3. Aylanma suv harorat farqining kamayishi*
Kondensator aylanma suvining kirish va chiqishi orasidagi farq (normal **3–5°C**) qisqaradi.
⚠️ **Farq <2°C bo'lsa — kondensatorning issiqlik almashinuv samaradorligi sezilarli pasaygan.**

*4. Kondensator terminal farqining oshishi*
Kondensator bosimiga mos to'yinish harorati va aylanma suv chiqish harorati orasidagi farq **6°C dan oshsa** — kondensatorning quvur yoki korpus tomonida **issiqlik almashinuv to'silgan**.
*(Loyihaviy terminal farq — 3.1°C)*

*5. Birlik iqtisodiyotining pasayishi*
Bir xil yuklamada turbinaga **bug' kirishi ko'payadi** (bug' sarf o'lchagichi yuqori ko'rsatadi), lekin **generatsiya oshmaydi, aksincha tushadi**, va **bug' sarfi tezligi 10% dan ko'proq oshadi**.

**SABABLARNI QIDIRISH TARTIBI**
⚠️ **Kondensator → vakuum tizimi → birlik ish rejimi → asboblar**

**1. Kondensatorning issiqlik almashinuv nosozligi**

*Quvur tomonida cho'kma yoki tiqilish*
Aylanma suv sifati past (qattiqlik yuqori, cho'kindi bor) → po'lat quvurlarning ichki devorida cho'kma.
⚠️ **Cho'kma qalinligi 0.5 mm dan oshsa — issiqlik almashinuvi sezilarli buziladi.**
Yoki begona modda (suv o'ti, tolalar) titan quvurlarini to'sadi.

*Korpus tomonida havo to'planishi*
Vakuum nasos quvvatining yetishmasligi kondensatsiyalanmaydigan gazlarni (havo) kondensatorda to'playdi. Bu **"havo plyonkasi"** hosil qiladi.
⚠️ **Havo miqdori 5% dan oshsa — issiqlik almashinuv samaradorligi 30% dan ko'proq tushadi.**

*Quvurlarning sizishi*
Korroziya tufayli quvur teshilishi yoki kengaytirilgan birikmada sizish → aylanma suv korpus tomoniga kirib bug' bilan aralashadi. Bu nafaqat **kondensatni suyultiradi** (suv qattiqligini oshiradi), balki quvur yuzasini **suv plyonkasi** bilan qoplaydi.

**2. Vakuum tizimi sizishi**

⚠️ Ushbu zanjirni yodda tuting: **aylanma suv sifati → cho'kma 0.5 mm → issiqlik almashinuv → exhaust harorati → vakuum 1–2 kPa/°C → LP exhaust bosim alarmi 0.33 bar.a → trip 0.45 bar.a**. Kimyoviy rejim buzilishi bir necha oy o'tib turbina tripiga aylanadi.

---

**🇷🇺 Высокая температура выхлопа — корреляция параметров**

**ПРИЗНАКИ**
⚠️ **В норме температура выхлопа на 3–5°C выше температуры циркводы на выходе.** При дефекте часто **выше 50°C**, на малой нагрузке — **выше 60°C**
⚠️ **Обратная связь с вакуумом: на каждый 1°C роста вакуум падает примерно на 1–2 кПа.** С 40°C до 50°C вакуум может уйти с −95 кПа ниже −85 кПа
Перепад циркводы (норма **3–5°C**) сужается; ⚠️ **менее 2°C — существенное падение теплообмена**
Температурный напор конденсатора **выше 6°C** — забит трубный или паровой тракт *(проектный напор 3.1°C)*
При той же нагрузке **расход пара растёт**, а **выработка падает**, **удельный расход пара растёт более чем на 10%**

**ПОРЯДОК ПОИСКА**
⚠️ **Конденсатор → вакуумная система → режим блока → приборы**

**Отказ теплообмена конденсатора**
*Отложения в трубках* — плохое качество циркводы; ⚠️ **толщина накипи более 0.5 мм существенно ухудшает теплообмен**; водоросли и волокна забивают титановые трубки
*Скопление воздуха* — недостаток производительности вакуумных насосов → **воздушная плёнка**; ⚠️ **при содержании воздуха выше 5% теплообмен падает более чем на 30%**
*Течь трубок* — коррозионное перфорирование или течь в вальцовке → циркводá в паровое пространство: **разбавление конденсата**, рост жёсткости, **водяная плёнка** на трубках

⚠️ Запомните цепочку: **качество циркводы → накипь 0.5 мм → теплообмен → температура выхлопа → вакуум 1–2 кПа/°C → сигнал 0.33 бар.а → защита 0.45 бар.а.** Нарушение ВХР через месяцы превращается в отключение турбины.

---

**🇬🇧 Excessively High Exhaust Temperature**

**PHENOMENA**
⚠️ **Under normal conditions exhaust temperature should be 3–5°C higher than the condenser circulating water outlet temperature.** During a fault it often **exceeds 50°C**, and even **60°C at low load**
⚠️ **Exhaust temperature is negatively correlated with vacuum — for every 1°C increase, vacuum decreases by approximately 1–2 kPa.** From 40°C to 50°C, vacuum may drop from −95 kPa to below −85 kPa
Circulating water temperature difference (normally **3–5°C**) shrinks; ⚠️ **below 2°C indicates a significant decline in condenser heat exchange efficiency**
Condenser terminal difference **exceeding 6°C** indicates blocked heat exchange on the tube or shell side *(design terminal difference is 3.1°C)*
Under the same load, **steam intake increases** but **generation falls**, and **steam consumption rate increases by more than 10%**

**INVESTIGATION ORDER**
⚠️ **Condenser → vacuum system → unit operating conditions → instruments**

**Condenser heat exchange failure**
*Tube-side fouling* — poor circulating water quality (high hardness, sediment); ⚠️ **a scale thickness exceeding 0.5 mm significantly impairs heat exchange**; algae and fibres block titanium tubes
*Shell-side air accumulation* — insufficient vacuum pump capacity lets non-condensable gases accumulate, forming an **"air film"**; ⚠️ **when air content exceeds 5%, heat exchange efficiency drops by more than 30%**
*Tube leakage* — corrosion perforation or leakage at expanded joints lets circulating water into the shell side: **dilutes the condensate**, raises hardness, and covers tubes with a **water film**

⚠️ Remember the chain: **circulating water chemistry → 0.5 mm scale → heat exchange → exhaust temperature → vacuum at 1–2 kPa/°C → LP exhaust alarm 0.33 bar.a → trip 0.45 bar.a.** A chemistry problem becomes a turbine trip months later.

`#exhausttemp #condenser #vacuum #fouling`

---
---

## POST 64 — Control oil suyuqligi: spetsifikatsiya va sinov

**🇺🇿 EH suyuqligi — yangi va ishlatilayotgan**

| Ko'rsatkich | Yangi suyuqlik | Ishlatilayotgan |
|---|---|---|
| **Rang, ASTM, maks** | **1.5** | **3.0** |
| Solishtirma og'irlik, 15.5–20°C | **1.13–1.155** | 1.13–1.155 |
| ISO qovushqoqlik 40°C, cSt (ISO 46) | **41.4–50.6** | 41.4–50.6 |
| Quyilish nuqtasi, maks | **−17.8°C** | −17.8°C |
| **Suv miqdori, hajm %, maks** | **0.10** | **0.10** |
| **Kislota soni, mg KOH/g, maks** | **0.10** | **0.20** |
| **Xlor miqdori, ppm, maks** | **50** | **50** |
| Alangalanish nuqtasi, min | **235°C** | 235°C |
| Yonish nuqtasi, min | **352°C** | 352°C |
| **O'z-o'zidan alangalanish harorati, min** | **566°C** | **566°C** |
| Solishtirma qarshilik 20°C, min | **100 MΩ·m** | 100 MΩ·m |
| O'tkazuvchanlik 20°C, maks | **1×10⁻⁹ S/sm** | 1×10⁻⁹ S/sm |
| **Ifloslanish (1 ml)** | **−/15/12** | **−/15/12** |

⚠️ **Yangi va ishlatilayotgan suyuqlik orasidagi yagona farqlar: RANG (1.5 → 3.0) va KISLOTA SONI (0.10 → 0.20).** Qolgan barcha talablar bir xil qoladi.

**Sinov: rang / ko'rinish**
• Usul: **vizual / ISO 2049**
• **Chastota: har oy**
• Ogohlantirish chegarasi: **tez qorayish**
⚠️ **Yog'ning sekin qorayishi — eskirish belgisi, lekin bu NORMAL. Tez qorayish esa NORMAL EMAS.**
• Harakat: **rang >4 bo'lganda va kislotalilikni past qiymatda ushlab turish qiyinlashganda** — ion almashinuvchi bilan ishlov berish

⚠️ **O'z-o'zidan alangalanish harorati 566°C** — bu fosfat efirning asosiy afzalligi. Mineral yog' bu haroratdan ancha past alangalanadi. Shuning uchun EH tizimi turbina yaqinida yuqori bosimda ishlashi mumkin.

⚠️ **Ifloslanish klassi −/15/12** — bu ISO 4406 bo'yicha. 3 mikronli filtrlar shu darajani ushlab turish uchun.

---

**🇷🇺 Жидкость ОГ — новая и рабочая**

| Показатель | Новая | Рабочая |
|---|---|---|
| **Цвет ASTM, макс** | **1.5** | **3.0** |
| Плотность 15.5–20°C | **1.13–1.155** | 1.13–1.155 |
| Вязкость 40°C, сСт (ISO 46) | **41.4–50.6** | 41.4–50.6 |
| Температура застывания, макс | **−17.8°C** | −17.8°C |
| **Вода, об. %, макс** | **0.10** | **0.10** |
| **Кислотное число, мг KOH/г, макс** | **0.10** | **0.20** |
| **Хлор, ppm, макс** | **50** | **50** |
| Температура вспышки, мин | **235°C** | 235°C |
| Температура воспламенения, мин | **352°C** | 352°C |
| **Температура самовоспламенения, мин** | **566°C** | **566°C** |
| Удельное сопротивление 20°C, мин | **100 МОм·м** | — |
| Проводимость 20°C, макс | **1×10⁻⁹ См/см** | — |
| **Загрязнённость (1 мл)** | **−/15/12** | **−/15/12** |

⚠️ **Отличия новой и рабочей только два: ЦВЕТ (1.5 → 3.0) и КИСЛОТНОЕ ЧИСЛО (0.10 → 0.20).**

**Испытание цвета** — **визуально / ISO 2049**, **ежемесячно**, порог — **быстрое потемнение**
⚠️ **Медленное потемнение — признак старения, но это НОРМА. Быстрое — НЕ норма.**
Действие: при **цвете >4 и трудности удержания низкой кислотности** — обработка ионообменником

⚠️ **Самовоспламенение 566°C** — главное преимущество фосфатного эфира; поэтому система работает под высоким давлением рядом с турбиной.
⚠️ **Класс чистоты −/15/12** по ISO 4406 — под него и стоят 3-микронные фильтры.

---

**🇬🇧 EH Fluid — new and operating specification**

| Property | New fluid | Operating fluid |
|---|---|---|
| **Colour, ASTM, max** | **1.5** | **3.0** |
| Specific gravity at 15.5–20°C | **1.13–1.155** | 1.13–1.155 |
| ISO viscosity at 40°C, cSt (ISO 46) | **41.4–50.6** | 41.4–50.6 |
| Pour point, max temp | **−17.8°C** | −17.8°C |
| **Water content, vol %, max** | **0.10** | **0.10** |
| **Acid number, mg KOH/g, max** | **0.10** | **0.20** |
| **Chlorine content, ppm, max** | **50** | **50** |
| Flash point, min | **235°C** | 235°C |
| Fire point, min | **352°C** | 352°C |
| **Auto-ignition temperature, min** | **566°C** | **566°C** |
| Resistivity at 20°C, min | **100 MΩ·m** | 100 MΩ·m |
| Conductivity at 20°C, max | **1×10⁻⁹ S/cm** | 1×10⁻⁹ S/cm |
| **Contamination (per 1 ml)** | **−/15/12** | **−/15/12** |

⚠️ **New versus operating differs in exactly two properties: COLOUR (1.5 → 3.0) and ACID NUMBER (0.10 → 0.20).** Everything else is unchanged.

**Colour / appearance test**
Method **visual / ISO 2049**, frequency **every month**, warning limit **rapid darkening**
⚠️ **A slow darkening of the oil, while a sign of deterioration, is normal. A rapid darkening is not.**
Action: when **colour is >4 and acidity is difficult to control at a low value**, treat with ion exchange

⚠️ **Auto-ignition at 566°C** is the whole point of phosphate ester — it lets a high-pressure system run right next to the turbine.
⚠️ **Contamination class −/15/12** per ISO 4406 is what the 3-micron filters exist to hold.

`#EHfluid #oilanalysis #phosphateester`

---
---

## POST 65 — Lube oil sifati: kunlik va oylik

**🇺🇿 Yog' sifati — nazorat va harakat**

**KUNLIK TEKSHIRUV**

*Yog' baki sathi (kuniga bir marta)*
Standart: **"normal yog' sathi belgisida"** ushlab turish, va **jacking oil nasos kirish bosimi normalligini** tasdiqlash
⚠️ **Sathning keskin tushishi** → **darhol quvur sizishini tekshiring — asosiy e'tibor yuqori bosimli birikmalarga**
⚠️ **Sathning sekin tushishi** → **bir xil markadagi sifatli yog' bilan to'ldiring. ARALASHTIRISH TAQIQLANADI.**

*Yog' baki harorati (kuniga bir marta)*
Standart: ish davomida oldindan belgilangan harorat qiymatiga asoslanadi
⚠️ **Harorat juda yuqori** → sovutgich tiqilganmi tekshiring (sovutish suvi quvurlaridan cho'kmani tozalang) va sovutish suvi ta'minoti yetarlimi
⚠️ **Harorat juda past** → **bak isitish qurilmasini yoqing** — yog' qovushqoqligi juda yuqori bo'lib **yog' ta'minoti yetishmay qolmasligi uchun**

*Yog' ko'rinishi (kuniga bir marta)*
Standart: **shaffof, loyqasiz, ko'piksiz, aniq aralashmalarsiz**
⚠️ **Emulsifikatsiya (sut rangida)** → **darhol vakuumli yog' tozalagichni ishga tushiring, namlik ≤0.1% bo'lguncha**
⚠️ **Qora shlam hosil bo'lishi** → oksidlanish **yog' haroratining juda yuqoriligidan** kelib chiqqanmi tekshiring, va **kislota qiymatini sinash uchun namuna oling**. ⚠️ **Kislota qiymati >0.03 mg KOH/g bo'lsa — yangi yog'ga almashtiring**

**OYLIK LABORATORIYA SINOVI**

*Chastota:* **oyiga bir marta, laboratoriya tekshiruvi**

*Majburiy ko'rsatkichlar:*
• ⚠️ **NAS tozalik klassi ≤ NAS 6**
• Namlik miqdori
• Kinematik qovushqoqlik
• Kislota qiymati

*Operatsion muhim nuqtalar:*
• ⚠️ **Namuna olish nuqtasi — "bak qaytish zonasi"** (yog'ning bir tekis aralashuvi uchun)
• ⚠️ **Namuna olishdan oldin namuna shishasini sinaladigan yog' bilan 3 marta chayqang** — ifloslanish natijaga ta'sir qilmasligi uchun
• ⚠️ **Ko'rsatkichlar standartdan chiqsa — 24 SOAT ICHIDA yog' tozalash (filtrlash, suvsizlantirish) yoki almashtirishni boshlang**

**JACKING OIL NASOSI — ishlayotgan nasosni tekshirish**
⚠️ **Har 2 soatda, 4 ta asosiy nuqta**

**Quvurlar va flanetslar — haftada bir**
1. Flanets prokladkalari va payvandlarda **yog' sizishi yo'q**
2. Quvurning tashqi devorida **korroziya yo'q**

⚠️ Ikkita kislota chegarasini chalkashtirmang: **lube oil uchun 0.03 mg KOH/g** (almashtirish), **EH suyuqligi uchun 0.20 mg KOH/g** (ishlatilayotgan chegara). Bular butunlay boshqa suyuqliklar.

---

**🇷🇺 Качество масла — контроль и действия**

**ЕЖЕДНЕВНО**
*Уровень (1×/сут)* — по **метке нормального уровня**, подтвердить **нормальное давление на всасе гидроподъёма**
⚠️ **Резкое падение** → **немедленно искать течь, в первую очередь на соединениях высокого давления**
⚠️ **Медленное падение** → долить **маслом той же марки. СМЕШИВАНИЕ ЗАПРЕЩЕНО.**
*Температура (1×/сут)* — ⚠️ **высокая** → проверить забитость охладителя (очистить накипь) и достаточность охлаждающей воды; ⚠️ **низкая** → **включить подогрев бака**, иначе вязкость не даст нужной подачи
*Внешний вид (1×/сут)* — **прозрачное, без мути, пены и включений**
⚠️ **Эмульсия (молочный цвет)** → **немедленно вакуумная маслоочистка до влаги ≤0.1%**
⚠️ **Чёрный шлам** → проверить окисление от **высокой температуры**, взять пробу на кислотное число; ⚠️ **при >0.03 мг KOH/г — замена масла**

**ЕЖЕМЕСЯЧНО (лаборатория)**
Обязательные показатели: ⚠️ **класс чистоты ≤ NAS 6**, влага, кинематическая вязкость, кислотное число
⚠️ Точка отбора — **зона слива в баке**; ⚠️ **бутыль промыть испытуемым маслом 3 раза**; ⚠️ **при выходе за норму — очистка или замена В ТЕЧЕНИЕ 24 ЧАСОВ**

**Насос гидроподъёма** — ⚠️ **осмотр работающего каждые 2 часа, 4 позиции**
**Трубопроводы и фланцы — еженедельно:** нет течей по прокладкам и швам, нет коррозии наружной стенки

⚠️ Не путать два предела по кислотности: **турбинное масло 0.03 мг KOH/г** (замена), **жидкость ОГ 0.20 мг KOH/г** (рабочий предел). Это разные жидкости.

---

**🇬🇧 Lube Oil Quality — daily and monthly**

**DAILY**
*Tank level (once a day)* — maintain at the **"normal oil level mark"**, confirm **jacking oil pump inlet pressure is normal**
⚠️ **Sudden drop** → **immediately check for pipeline leaks, focusing on high-pressure joints**
⚠️ **Slow drop** → **replenish with qualified oil of the same brand. MIXING IS PROHIBITED.**
*Tank temperature (once a day)* — ⚠️ **too high** → check whether the cooler is blocked (clean scale from cooling water pipes) and whether cooling water supply is sufficient; ⚠️ **too low** → **start the tank heating device** to avoid insufficient oil supply from excessive viscosity
*Oil appearance (once a day)* — **transparent, no turbidity, no foam, no obvious impurities**
⚠️ **Emulsification (milky white)** → **immediately start the vacuum oil purifier for dehydration until moisture ≤0.1%**
⚠️ **Black sludge formation** → check whether oxidation is caused by excessive oil temperature and sample for acid value; ⚠️ **replace with new oil when acid value >0.03 mg KOH/g**

**MONTHLY LABORATORY TEST**
Mandatory indicators: ⚠️ **NAS cleanliness class ≤ NAS 6**, moisture content, kinematic viscosity, acid value
⚠️ Sampling point is the **"oil tank return zone"** for uniform mixing; ⚠️ **rinse the sampling bottle with the oil to be tested 3 times**; ⚠️ **if indicators exceed standards, start purification or replacement WITHIN 24 HOURS**

**Jacking oil pump** — ⚠️ **inspect the running pump every 2 hours, 4 key items**
**Pipes and flanges — weekly:** no oil leakage at flange gaskets or welds, no corrosion on pipe outer wall

⚠️ Don't confuse the two acid limits: **turbine lube oil 0.03 mg KOH/g** (replace), **EH fluid 0.20 mg KOH/g** (operating limit). Different fluids entirely.

`#luboil #oilquality #NAS6 #maintenance`

---
---

## POST 66 — Stator suvi kimyoviy rejimi

**🇺🇿 Stator suvi — suv sifati boshqaruvi**

Suv sifati **stator sterjenlarining korroziyasi (mis qotishmasi) va cho'kma hosil bo'lishining** oldini olishda hal qiluvchi.

| Sinov | Chastota | Me'yor |
|---|---|---|
| **Elektr o'tkazuvchanlik** | Onlayn (real vaqt); qo'lda **kuniga 1×** | **≤0.5 μS/sm (25°C)** — past o'tkazuvchanlik **elektrokimyoviy korroziyaning** oldini oladi |
| **pH qiymati** | Onlayn (real vaqt); qo'lda **kuniga 1×** | **7.0–9.0** — ishqoriy muhit **mis korroziyasini bostiradi** |
| **Erigan kislorod** | Qo'lda **haftada 1×** | ⚠️ **2–8 ppm** |

⚠️⚠️ **ENG MUHIM NUQTA — Doosan generatori YUQORI KISLOROD suv tizimidan foydalanish uchun loyihalangan. Tizim deionlashtirilgan suvning YUQORI DARAJADA HAVOLANGAN bo'lishini, suvdagi kislorod miqdori 2–8 ppm oralig'ida bo'lishini TALAB QILADI.**

Bu odatiy energetika amaliyotidan **teskari**. Ko'p suv konturlarida kislorod **minimallashtiriladi**. Bu yerda esa **kislorod maqsadli ushlab turiladi** — mis yuzasida barqaror himoya oksid plyonkasini saqlash uchun.
⚠️ **Kislorodni "pasaytirish" uchun deaeratsiya qilish — bu tizimda ZARAR.**

**KUNLIK NAZORAT (11.13.1)**

*1. Sovutish suvi bosimi*
Stator kirish bosimini tekshirish; ⚠️ **ish davomida har 2 soatda ma'lumot qayd etish**

*2. Sovutish suvi sarfi*
Sarf o'lchagich ko'rsatkichini kuzatish (tizim kirishida o'rnatilgan); ⚠️ **sarfning loyihaviy qiymatga mosligini tekshirish**

*3. Sovutish suvi harorati*
Statorning kirish/chiqish haroratini kuzatish; **harorat rostlash klapani holatini** tekshirish

*4. Sizishni tekshirish*
Stator tizimi flanetsi, quvur birikmalari, klapan salniki va **stator sterjeni suv ulagichlarini** ko'zdan kechirish; **stator bakining suv sathini** tekshirish

*5. Filtr holati*
Stator suv filtrining **Δp** ni o'qish; filtrning **vent, drenaj va bypass klapanlari** holatini tekshirish

⚠️ **Loyihaviy sarf 63.6 m³/s, alarm 57.2, run back 54.2.** Kunlik tekshiruvda "sarf loyihaviy qiymatga mosmi" degan talab bor — ya'ni 63.6 dan sezilarli farq alarmni kutmasdan tekshirilishi kerak.

⚠️ **O'tkazuvchanlik ≤0.5 μS/sm** — bu alarm (6-bobda H **>0.5**) bilan bir xil. Ya'ni **me'yor va alarm bir joyda**. HH **9.9 μS/sm** esa allaqachon jiddiy shikast zonasi.

---

**🇷🇺 Статорная вода — водно-химический режим**

Качество воды критично против **коррозии медных стержней и отложений**.

| Показатель | Частота | Норма |
|---|---|---|
| **Электропроводность** | Онлайн; вручную **1×/сут** | **≤0.5 мкСм/см (25°C)** — против **электрохимической коррозии** |
| **pH** | Онлайн; вручную **1×/сут** | **7.0–9.0** — щелочная среда **подавляет коррозию меди** |
| **Растворённый кислород** | Вручную **1×/нед** | ⚠️ **2–8 ppm** |

⚠️⚠️ **КЛЮЧЕВОЕ: генератор Doosan спроектирован под ВЫСОКОКИСЛОРОДНУЮ водную систему. Требуется, чтобы обессоленная вода была СИЛЬНО АЭРИРОВАНА, с содержанием кислорода 2–8 ppm.**

Это **противоположно** привычной практике, где кислород минимизируют. Здесь кислород **удерживают намеренно** — для устойчивой защитной оксидной плёнки на меди.
⚠️ **Деаэрация «для снижения кислорода» в этой системе — ВРЕД.**

**ЕЖЕДНЕВНО**
Давление на входе — ⚠️ **запись каждые 2 часа** | Расход — ⚠️ **сверять с проектным** | Температура входа/выхода и положение регулирующего клапана | Течи по фланцам, соединениям, сальникам и **водяным наконечникам стержней**, уровень в баке | **Δp фильтра**, состояние воздушника, дренажа и байпаса

⚠️ **Проект 63.6 м³/ч, сигнал 57.2, разгрузка 54.2.** Требование «сверять с проектным» означает: заметное отклонение от 63.6 проверяют, не дожидаясь сигнала.

⚠️ **Норма ≤0.5 мкСм/см совпадает с уставкой сигнала.** HH **9.9 мкСм/см** — уже зона повреждения.

---

**🇬🇧 Stator Cooling Water — chemistry**

Water quality is critical to prevent **stator bar corrosion (copper alloy) and scaling**.

| Test | Frequency | Standard |
|---|---|---|
| **Electrical conductivity** | Online real-time; manual **1×/day** | **≤0.5 μS/cm (25°C)** — low conductivity avoids **electrochemical corrosion** |
| **pH value** | Online real-time; manual **1×/day** | **7.0–9.0** — alkaline environment **inhibits copper corrosion** |
| **Dissolved oxygen** | Manual **1×/week** | ⚠️ **2–8 ppm** |

⚠️⚠️ **The key point: the Doosan generator is designed to use a HIGH OXYGEN water system. The system requires that the deionized water remain HIGHLY AERATED, with oxygen content in the range of 2 to 8 ppm.**

This is the **opposite** of usual power plant practice where oxygen is minimized. Here oxygen is **maintained deliberately** to hold a stable protective oxide film on the copper.
⚠️ **De-aerating "to reduce oxygen" is damaging in this system.**

**DAILY MONITORING (11.13.1)**
*Pressure* — check stator inlet pressure; ⚠️ **record data every 2 hours during operation**
*Flow* — observe the flowmeter at the system inlet; ⚠️ **verify flow consistency with the design value**
*Temperature* — monitor stator inlet/outlet temperature; check the temperature control valve status
*Leakage* — inspect system flange, pipe joints, valve packing and **stator bar water connectors**; check stator tank water level
*Filter status* — read stator water filter **Δp**; inspect filter **vent, drain and bypass valve** status

⚠️ **Design flow is 63.6 m³/h, alarm 57.2, run back 54.2.** "Verify consistency with the design value" means a noticeable deviation from 63.6 is investigated without waiting for the alarm.

⚠️ **The ≤0.5 μS/cm standard is the same number as the alarm.** The HH at **9.9 μS/cm** is already in the damage zone.

`#statorwater #chemistry #highoxygen #Doosan`

---
---

## POST 67 — H2 tizimi kunlik TO

**🇺🇿 Vodorod tizimi — kunlik nazorat**

**1. Generator vodorod bosimi monitoringi**
• Generator tepasidagi **vodorod manometri/transmitteri**ni tekshiring
• ⚠️ **Ish davomida har 2 soatda bosimni qayd eting**
• ⚠️ **Normal bosim: 0.55 MPa** (generator yuklamasiga qarab o'zgaradi)

**2. Vodorod sizishini tekshirish**
• ⚠️ **Portativ vodorod detektori (sezgirligi ≥100 ppm)** bilan skanerlang: **flanetslar, klapan birikmalari, zichlash vtulkalari va vodorod sovutgich quvurlari**
• ⚠️ **Generator korpusini yog' dog'lariga tekshiring — vodorod bilan aralashgan yog' zichlash sizishini bildiradi**
• Me'yor: ⚠️ **sizish konsentratsiyasi ≤1% (hajm ulushi)**; korpusda **ko'zga ko'rinadigan yog'-H₂ aralashmasi yo'q**

**3. Vodorod sovutgich holatini tekshirish**

⚠️ **Bosim raqamlari bo'yicha diqqat.** Manualda uch xil raqam bor:
• **1.2.2.1 (loyihaviy):** H₂ gaz bosimi **5.17 bar.g**, ish oralig'i **5.17/3.10 bar.g**
• **6-bob (alarm):** L **<5.03 bar**, H **>5.45 bar**
• **8-bob Step 35 (ishga tushirish):** H₂ bosimi **4.14 bar**
• **11-bob (kunlik TO):** normal bosim **0.55 MPa = 5.5 bar**
Bular turli holatlarga tegishli: **5.17 loyihaviy nominal, 4.14 ishga tushirishda, 5.5 to'liq yuklamada.** Yuklamaga qarab o'zgarishi manualda ochiq yozilgan.

⚠️ **Tozalik bo'yicha ham ikki raqam bor:** 6-bobda alarm **<95%**, 10.11 da "ruxsat etilgan diapazon **≥96%**", Step 35 da **>98%**. Ishga tushirish talabi eng qat'iy.

**Xavfsizlik eslatmalari (11.12.3.1)**
• Portativ detektor sezgirligi **≥100 ppm** bo'lishi shart — undan pastroq sezgirlik erta sizishni topmaydi
• **Generator korpusidagi yog' dog'i** — bu vizual belgi, asbob talab qilmaydi. Har smenada ko'zdan kechiriladi

⚠️ Bog'lanish: **korpusda yog' → zichlash sizishi → seal oil differensiali → H₂ tozaligi → sovutish samaradorligi → stator harorati.** Bitta yog' dog'i shu zanjirning boshi.

---

**🇷🇺 Водородная система — ежедневный контроль**

**1. Давление водорода**
Проверять **манометр/датчик на верху генератора**; ⚠️ **запись каждые 2 часа**; ⚠️ **нормальное давление 0.55 МПа** (меняется с нагрузкой)

**2. Проверка на утечку**
⚠️ **Портативный течеискатель с чувствительностью ≥100 ppm** — сканировать **фланцы, соединения арматуры, уплотняющие вкладыши и трубки водородных охладителей**
⚠️ **Осматривать корпус генератора на масляные пятна — масло с водородом означает течь уплотнения**
Норма: ⚠️ **концентрация утечки ≤1% (объёмная доля)**, **без видимой смеси масло-H₂ на корпусе**

**3. Состояние водородных охладителей**

⚠️ **По давлению в руководстве четыре разных числа:**
**1.2.2.1 (проект):** **5.17 бар.g**, диапазон **5.17/3.10** | **Глава 6 (сигналы):** L **<5.03**, H **>5.45** | **Шаг 35 (пуск):** **4.14 бар** | **Глава 11 (эксплуатация):** **0.55 МПа = 5.5 бар**
Это разные состояния: **5.17 — проектный номинал, 4.14 — при пуске, 5.5 — на полной нагрузке.**

⚠️ **По чистоте тоже расхождение:** глава 6 — сигнал **<95%**, п. 10.11 — «допустимо **≥96%**», Шаг 35 — **>98%**. Пусковое требование самое жёсткое.

⚠️ Связка: **масло на корпусе → течь уплотнения → перепад уплотняющего масла → чистота H₂ → эффективность охлаждения → температура статора.**

---

**🇬🇧 Hydrogen System — daily inspection**

**1. Generator hydrogen pressure monitoring**
Check the **hydrogen pressure gauge/transmitter at the generator top**; ⚠️ **record pressure every 2 hours during operation**; ⚠️ **normal pressure 0.55 MPa** (varies by generator load)

**2. Hydrogen leak check**
⚠️ **Use a portable hydrogen detector with sensitivity ≥100 ppm** to scan **flanges, valve joints, seal bushings and hydrogen cooler tubes**
⚠️ **Inspect the generator casing for oil stains — oil mixed with hydrogen indicates seal leakage**
Standard: ⚠️ **leakage concentration ≤1% (volume fraction)**; **no visible oil-H₂ mixture on casing**

**3. Hydrogen cooler status check**

⚠️ **The manual carries four different pressure figures:**
**1.2.2.1 (design):** **5.17 barg**, operating range **5.17/3.10** | **Chapter 6 (alarms):** L **<5.03**, H **>5.45** | **Step 35 (start-up):** **4.14 bar** | **Chapter 11 (routine):** **0.55 MPa = 5.5 bar**
These belong to different states: **5.17 is the design rating, 4.14 at start-up, 5.5 at full load.** The manual says explicitly that it varies by load.

⚠️ **Purity also has three figures:** Chapter 6 alarm **<95%**, section 10.11 "generally **≥96%**", Step 35 **>98%**. The start-up requirement is the strictest.

⚠️ The chain: **oil on the casing → seal leakage → seal oil differential → H₂ purity → cooling effectiveness → stator temperature.** One oil stain is where it starts.

`#hydrogen #dailycheck #leakdetection`

---
---

## POST 68 — ACCWS kunlik TO

**🇺🇿 Yordamchi aylanma sovutish suvi — kunlik nazorat**

⚠️ **Chastota: kuniga 3 martadan kam emas. Smena qabulida MAJBURIY.**

| Tekshiriladigan qism | Nima tekshiriladi | Me'yor | Usul |
|---|---|---|---|
| **Tizim bosimi** | Nasos chiqish bosimi, kollektor bosimi | ⚠️ **Nasos chiqishi 0.25–0.35 MPa; kollektor ≥0.2 MPa** | Bosim transmitteri va joyidagi manometrni kuzatish |
| **Elektr filtr qurilmasi** | Differensial bosim ko'rsatkichi, purge klapan holati | ⚠️ **Filtr bo'ylab Δp ≤60 kPa; purge klapan sizishsiz zich yopiq** | — |

**Boshqa TO chastotalari (11.1)**
• **11.1.1** Ish davomidagi kunlik TO — **kuniga ≥3 marta**, smena qabulida majburiy
• **11.1.2** Maxsus muntazam TO — **haftada bir marta**
• **11.1.3** To'xtatishdan keyingi TO — tizim to'xtatilganda yoki kapital ta'mirda

**Shu tuzilma barcha tizimlarga tegishli**
CCCWS (11.2), CCWS (11.3), kondensat (11.4) — barchasi **"kuniga ≥3 marta + haftada 1 marta + to'xtatishda"** sxemasi bo'yicha.

**Control oil (11.8) — boshqacha**
⚠️ **11.8.1 Kunlik muntazam tekshiruv — chastota: smenada bir marta / 2–4 soatda.** Ya'ni yog' tizimlari ancha tez-tez.

**Yog' sifati (11.10)**
• Yog' baki sathi, harorati, ko'rinishi — **kuniga 1 marta**
• Jacking oil nasosi (ishlayotgan) — ⚠️ **har 2 soatda**
• Quvurlar va flanetslar — **haftada bir**
• Laboratoriya sinovi — **oyiga bir**

**H2 va stator suvi (11.12, 11.13)**
• H2 bosimi — ⚠️ **har 2 soatda qayd**
• Stator suvi bosimi va sarfi — ⚠️ **har 2 soatda qayd**

⚠️ **Umumiy chastota jadvali:**
| Nima | Qanchalik tez-tez |
|---|---|
| Control oil tekshiruvi | **2–4 soatda / smenada 1** |
| Jacking oil ishlayotgan nasos | **2 soatda** |
| H2 bosimi qayd | **2 soatda** |
| Stator suvi bosim/sarf qayd | **2 soatda** |
| ACCWS/CCCWS/CCWS/kondensat | **kuniga ≥3 marta** |
| Yog' baki sath/harorat/ko'rinish | **kuniga 1** |
| Stator suvi o'tkazuvchanlik/pH qo'lda | **kuniga 1** |
| Stator suvi erigan kislorod | **haftada 1** |
| Quvurlar/flanetslar | **haftada 1** |
| Yordamchi tizimlar maxsus TO | **haftada 1** |
| Lube oil laboratoriya | **oyiga 1** |
| Control oil rang/ko'rinish | **oyiga 1** |
| HP/IP klapan onlayn test | ⚠️ **HAR KUNI** |

---

**🇷🇺 ВЦОС — ежедневный контроль**

⚠️ **Частота: не менее 3 раз в сутки. ОБЯЗАТЕЛЬНО при приёмке смены.**

| Узел | Что | Норма |
|---|---|---|
| **Давление системы** | Нагнетание насоса, коллектор | ⚠️ **Нагнетание 0.25–0.35 МПа; коллектор ≥0.2 МПа** |
| **Электрофильтр** | Δp, состояние продувочного клапана | ⚠️ **Δp ≤60 кПа; продувочный плотно закрыт без течи** |

**Структура ТО** — **11.1.1** ежедневно ≥3 раза | **11.1.2** раз в неделю | **11.1.3** после останова/в ремонте
Та же схема для ЗКОС (11.2), ЦОС (11.3), конденсатной (11.4).
⚠️ **Система ОГ (11.8.1) — раз в смену / каждые 2–4 часа**, значительно чаще.

⚠️ **Сводная таблица частот:**
ОГ — **2–4 ч** | Гидроподъём (рабочий насос) — **2 ч** | Давление H2 — **2 ч** | Давление/расход статорной воды — **2 ч** | ВЦОС/ЗКОС/ЦОС/конденсат — **≥3 раза в сутки** | Уровень/температура/вид масла — **1×/сут** | Проводимость и pH статорной воды — **1×/сут** | Кислород статорной воды — **1×/нед** | Трубопроводы и фланцы — **1×/нед** | Спецобслуживание вспомсистем — **1×/нед** | Лаборатория по маслу — **1×/мес** | Цвет жидкости ОГ — **1×/мес** | Испытание клапанов ВД/СД — ⚠️ **ЕЖЕДНЕВНО**

---

**🇬🇧 ACCWS — daily inspection**

⚠️ **Frequency: no less than 3 times a day, mandatory during shift handover.**

| Inspection part | Content | Qualified standard |
|---|---|---|
| **System pressure** | Pump outlet pressure, header pressure | ⚠️ **Pump outlet 0.25–0.35 MPa; header ≥0.2 MPa** |
| **Electric filter device** | Differential pressure indicator, blow down valve status | ⚠️ **Δp across the filter ≤60 kPa; blow down valve closed tightly without leakage** |

**Maintenance structure** — **11.1.1** during operation, ≥3 times a day | **11.1.2** regular special maintenance, once a week | **11.1.3** post-shutdown, during shutdown or overhaul
The same structure applies to CCCWS (11.2), CCWS (11.3) and condensate (11.4).
⚠️ **Control oil (11.8.1) is once per shift / every 2–4 hours** — considerably more often.

⚠️ **Consolidated frequency table:**
Control oil — **2–4 h** | Jacking oil running pump — **2 h** | H2 pressure log — **2 h** | Stator water pressure/flow log — **2 h** | ACCWS/CCCWS/CCWS/condensate — **≥3× per day** | Lube oil level/temp/appearance — **1×/day** | Stator water conductivity and pH manual — **1×/day** | Stator water dissolved oxygen — **1×/week** | Pipes and flanges — **1×/week** | Auxiliary special maintenance — **1×/week** | Lube oil laboratory — **1×/month** | EH fluid colour — **1×/month** | HP/IP valve online test — ⚠️ **DAILY**

`#maintenance #frequency #shifthandover`

---
---

## POST 69 — Kondensator rezina shar tozalash tizimi

**🇺🇿 Rubber ball tizimi — kondensator quvurlarini tozalash**

**Nima uchun**
Kondensator quvurlarining ichki devorida **cho'kma hosil bo'lishining oldini olish**. POST 63 da ko'rganimizdek: ⚠️ **cho'kma qalinligi 0.5 mm dan oshsa issiqlik almashinuvi sezilarli buziladi** → exhaust harorati oshadi → vakuum tushadi → LP exhaust trip.

**Tarkibi (3.5.2)**
• **Rezina sharlar** (sponge ball)
• **Shar yig'gich** (ball collector)
• **Shar filtri** (ball strainer)
• **Shar nasosi** va **shar to'ri** (screen)

**Ishlash tamoyili**
Sharlar aylanma suv oqimiga kiritiladi, quvurlar ichidan o'tadi va ichki devorni **mexanik ishqalab tozalaydi**, keyin **shar yig'gichda** ushlanadi va qayta kiritiladi.

**Nazorat nuqtalari**
• **Shar sonini hisoblash** — sharlar yo'qolsa tizim samarasiz bo'ladi va yo'qolgan sharlar quvurlarni to'sishi mumkin
• **Shar holati** — yeyilgan yoki kichraygan sharlar quvur devoriga tegmaydi
• **Shar filtri Δp** — filtr tiqilsa aylanma suv qarshiligi oshadi
• **To'r holati** — yirtilgan to'r sharlarni o'tkazib yuboradi

⚠️ **Bog'lanish zanjiri operatorlar uchun:**
Rubber ball tizimi ishlamayapti → quvur cho'kmasi ortadi → **kondensator terminal farqi 3.1°C dan 6°C ga** → exhaust harorati ko'tariladi → **har 1°C ga vakuum 1–2 kPa tushadi** → LP exhaust bosim alarmi **0.33 bar.a** → kechiktirilgan trip **0.35 bar.a** → trip **0.45 bar.a**.

⚠️ Bu sekin jarayon — **haftalar va oylar**. Rubber ball tizimi "ikkinchi darajali" ko'rinadi, lekin u ishlamasa **turbina bir necha oydan keyin trip bo'ladi va sabab kondensatorda ekanini topish qiyin bo'ladi.**

**Aylanma suv sifati bilan bog'liqlik**
⚠️ **CCWS o'tkazuvchanligi ≥3000 μS/sm** — bu korroziya va cho'kma chegarasi (POST 12). O'tkazuvchanlik yuqori bo'lsa rubber ball tizimi ham yetarli bo'lmaydi.

---

**🇷🇺 Система шариковой очистки конденсатора**

**Зачем** — предотвращение **отложений на внутренней стенке трубок**. Как показано в POST 63: ⚠️ **накипь толще 0.5 мм существенно ухудшает теплообмен** → рост температуры выхлопа → падение вакуума → защита ЦНД.

**Состав** — **резиновые (губчатые) шарики**, **сборник шариков**, **фильтр шариков**, **насос** и **сетка**

**Принцип** — шарики вводятся в поток циркводы, проходят через трубки, **механически счищают** внутреннюю стенку, улавливаются **сборником** и вводятся повторно

**Точки контроля**
• **Пересчёт шариков** — потерянные шарики снижают эффективность и могут забить трубки
• **Состояние шариков** — изношенные не касаются стенки
• **Δp фильтра** — забитый фильтр повышает сопротивление
• **Состояние сетки** — порванная пропускает шарики

⚠️ **Цепочка для оператора:** система не работает → рост отложений → **температурный напор с 3.1°C до 6°C** → рост температуры выхлопа → **1–2 кПа вакуума на каждый 1°C** → сигнал **0.33 бар.а** → защита с выдержкой **0.35** → защита **0.45 бар.а**

⚠️ Процесс медленный — **недели и месяцы**. Система кажется второстепенной, но её простой **через несколько месяцев даёт отключение турбины, и связать причину с конденсатором уже трудно.**

⚠️ Связь с ВХР: **проводимость ЦОС ≥3000 мкСм/см** — предел по коррозии и отложениям. При высокой проводимости шариковой очистки уже не хватает.

---

**🇬🇧 Condenser Rubber Ball Cleaning System**

**Purpose** — prevent **fouling on the inner wall of the condenser tubes**. As in POST 63: ⚠️ **scale thickness exceeding 0.5 mm significantly impairs heat exchange** → exhaust temperature rises → vacuum falls → LP exhaust trip.

**Configuration (3.5.2)** — **sponge rubber balls**, **ball collector**, **ball strainer**, **ball pump** and **ball screen**

**Principle** — balls are injected into the circulating water flow, pass through the tubes **mechanically scrubbing** the inner wall, are caught by the **collector** and reinjected

**Control points**
• **Ball count** — lost balls reduce effectiveness and can block tubes
• **Ball condition** — worn or shrunken balls no longer contact the tube wall
• **Strainer Δp** — a clogged strainer raises circulating water resistance
• **Screen condition** — a torn screen lets balls escape

⚠️ **The chain for operators:** ball system out of service → tube fouling grows → **condenser terminal difference moves from 3.1°C toward 6°C** → exhaust temperature rises → **vacuum falls 1–2 kPa per °C** → LP exhaust alarm **0.33 bar.a** → delayed trip **0.35 bar.a** → trip **0.45 bar.a**

⚠️ It is a slow process — **weeks and months**. The ball system looks secondary, but leaving it out of service **produces a turbine trip months later, by which time tracing the cause back to the condenser is hard.**

⚠️ Chemistry link: **CCWS conductivity ≥3000 μS/cm** is the corrosion and scaling limit. Above it, ball cleaning alone is not enough.

`#rubberball #condensercleaning #fouling`

---
---

## POST 70 — Vakuum buzmasdan trip qilinadigan holatlar

**🇺🇿 Vakuum saqlangan holda trip — 8 kategoriya**

**Asosiy shart:** nosozlik birlik asosiy qismining (rotor, podshipniklar, rotor-stator zazori) **asosiy xavfsizligiga bevosita tahdid solmasligi kerak**.
⚠️ **Kondensator vakuumini saqlash rotorning termik egilishi xavfini kamaytiradi va qayta ishga tushirish siklini qisqartiradi.**

**Protsedura (6 qadam)** — POST 33 dagidan farqi: **vakuum buzish qadami YO'Q**
1. Avariya tugmasi → barcha klapanlar yopiq, HP check valve yopiq, HP vent ochiq, generator va ikkala HRSG interlok bilan trip, GCB ochiq, HRSG diverter damperlar yopiq
2. EBOP ni ishga tushir, muvaffaqiyatli ishga tushganini tasdiqla
3. Tezlik **400 rpm** dan pastda JOP avtomatik ishga tushganini tekshir
4. Bo'shashish vaqti va ekssentrisitetni qayd et, podshipnik harorati va o'q siljishini kuzat
5. 0 rpm da turning gear avtomatik ishga tushganini tekshir
6. Turning gear tezligi **7 rpm/min**

**KATEGORIYALAR**

*1. Rostlash va boshqaruv tizimi anomaliyalari*
• Rostlash klapanining yopishishi yoki nosozligi → yuklama rostlanmaydi yoki tezlik nominaldan chetlashadi, ⚠️ **lekin overspeed bo'lmaydi (110% ga yetmaydi)**
• Gidravlik boshqaruv yog' bosimining g'ayritabiiy pasayishi ⚠️ **(trip himoyasini ishga tushirmagan holda)**, yoki gidravlik servotizim nosozligi
• Avtosinxronizatsiya qurilmasi yoki DEH nosozligi → beqaror ish, ⚠️ **lekin mexanik qotib qolish yoki elektr qisqa tutashuv xavfi yo'q**

*2. Moylash tizimida halokatli bo'lmagan nosozliklar*
• Yog' bosimi minimal ruxsat etilgan qiymatga tushdi ⚠️ **(trip sozlamasiga yetmagan)** va sozlashdan keyin (zaxira nasos) tiklanmadi, ⚠️ **lekin yog' uzilishi yo'q va podshipnik metall harorati chegaradan oshmagan**
• ⚠️ **Yog' harorati keskin ko'tarildi (60°C dan oshdi)** va sovutish tizimi tushira olmayapti, ⚠️ **lekin podshipniklarda qizib ketish yoki yog' otish kabi xavfli belgilar yo'q**
• Yog' baki sathi juda past ⚠️ **(minimal sath alarm qiymatidan past emas)** va to'ldirish samarasiz, lekin yog' sirkulyatsiyasi va moylashga ta'sir qilmayapti

*3. Bug' parametrlarining jiddiy chetlanishi*
• ⚠️ **Main/reheat bug'ning ortiqcha qizishi yoki keskin tushishi (15 daqiqada 50°C dan ortiq, lekin trip qiymatiga yetmagan)** va desuperheating/reduksiya bilan tiklanmayapti, quvur birikmasi sizishi yoki metall qizib ketish xavfi yo'q
• Main/reheat bug' bosimining sezilarli oshib ketishi, xavfsizlik klapani ishlamadi yoki ishlagandan keyin qayta o'tirmadi, ⚠️ **lekin quvur yorilishi xavfi yo'q**
• Bug' sifatining jiddiy yomonlashuvi → oqim yo'lida cho'kma va korroziya, ⚠️ **lekin tebranish yoki keskin parametr o'zgarishi yo'q**

*4. Generator va elektr tizimidagi og'ir bo'lmagan nosozliklar*
• ⚠️ **Generator rotorining bir nuqtali yerga ulanishi**, ikki nuqtaliga o'smagan, stator izolyatsiyasi shikastlanmagan
• Generator stator ortiqcha yuklamasi, davomiyligi ruxsat etilgan chegaraga yaqin, yuklamani kamaytirish bilan yengillashmayapti, ⚠️ **lekin o'ram qizib ketishi yoki o'ziga xos hid yo'q**
• Qo'zg'atish tizimi nosozligi (qo'zg'atish toki anomaliyasi, kuchlanish tebranishi) → terminal kuchlanish beqaror, ⚠️ **lekin qo'zg'atishni yo'qotish yoki qisqa tutashuv yo'q**

*5. Normal ishlashga to'sqinlik qiluvchi yordamchi tizim nosozliklari*
• Oziqlantiruvchi suv tizimi nosozligi → baraban suv sathi nazoratdan chiqdi ⚠️ **(past/yuqori sath trip qiymatiga yetmagan)**
• Kondensat tizimi nosozligi (nasos tripi, kondensator suv sathi juda yuqori) ⚠️ **lekin kondensator sizishi yoki vakuumning keskin tushishi yo'q**
• Vakuum tizimi nosozligi (nasos tripi va qisqa vaqtda tiklanmaydi) → vakuum **sekin tushadi**, ⚠️ **lekin birlik hali past tezlikda ishlay oladi, manfiy bosim shikastlanish xavfi yo'q**

*6. Chegaradan chiqqan tebranish va siljish (halokatli bo'lmagan)*
• ⚠️ **3000 rpm da podshipnik tebranishining ikki amplitudasi ≥164 μm, lekin trip sozlamasiga (≥240 μm) yetmagan**, va **aniq metall ishqalanish tovushi yo'q**
• O'q siljishi ruxsat etilgan diapazondan oshdi, ⚠️ **lekin trip qiymatiga yetmagan**, upor podshipnik harorati chegaradan oshmagan, **yeyilish belgilari yo'q**

*7. Asosiy qismga xavf solmaydigan boshqa anomaliyalar*
• ⚠️ **Flanets va boltlar haroratining anomaliyasi → yuqori-pastki silindr harorat farqi 42°C dan oshdi**, lekin rotor-stator zazorining yo'qolishi yoki silindr deformatsiyasi xavfi yo'q
• LP silindr exhaust haroratining juda yuqoriligi, purkash bilan yengillashmayapti, ⚠️ **lekin notekis kengayish yoki tebranish oshishi yo'q**
• Klapan yoki quvur flanetsida **kichik sizish** (yong'in yoki zaharlanish xavfi yo'q), ⚠️ **lekin sizish hajmi ortib bormoqda va joyidagi xavfsiz ishlashga ta'sir qilmoqda**

*8. TSI parametrlarining anomaliyasi yoki nosozligi*
• ⚠️ **TSI ko'rsatkichlari keskin yomonlashmoqda** (tebranishning to'satdan oshishi, o'q siljishining tez drifti). Trip qiymatiga yetmasa ham **tendensiya aniq va qisqa vaqtda chegaradan oshishi mumkin**
• ⚠️ **Bir nechta bog'liq TSI asbobida bir vaqtda anomaliya** (masalan bitta podshipnikning ham tebranish, ham harorat asboblari noaniq yoki chegaradan oshgan) → **haqiqiy uskuna nosozligini istisno qilib bo'lmaydi**
• ⚠️ **TSI tizimining umumiy nosozligi** (quvvat uzilishi, signallarning butunlay yo'qolishi) → **asosiy parametrlar uchun monitoring asosi yo'q va birlik holatini baholab bo'lmaydi**

⚠️ **Eng muhim farq: 42°C va 50°C.** Yuqori-pastki silindr farqi **42°C** dan oshsa — vakuum buzmasdan trip (kategoriya 7). **50°C** dan oshsa — **vakuum buzib trip** (POST 34, band 12). 8°C farq ikki xil protsedurani belgilaydi.

⚠️ **Tebranish uchun ham shunday: 164 μm — vakuum buzmasdan, 240 μm — vakuum buzib.**

---

**🇷🇺 Отключение без срыва вакуума — 8 категорий**

**Условие:** дефект **не угрожает напрямую основной части блока** (ротор, подшипники, зазоры). ⚠️ **Сохранение вакуума снижает риск термического изгиба ротора и сокращает цикл повторного пуска.**

**Процедура (6 шагов)** — как в POST 33, **но БЕЗ срыва вакуума**

**КАТЕГОРИИ**
*1. Система регулирования* — заедание РК без разгона (не 110%); падение давления ОГ **без срабатывания защиты**; отказ автосинхронизации или DEH **без механического заклинивания и КЗ**
*2. Маслосистема (не фатально)* — давление на минимально допустимом **без достижения уставки защиты**, **без обрыва подачи и превышения температуры баббита**; ⚠️ **резкий рост температуры выше 60°C** без опасных признаков; низкий уровень **не ниже сигнального**
*3. Параметры пара* — ⚠️ **перегрев или падение более 50°C за 15 минут, но не до уставки защиты**; превышение давления, предохранительный не сработал или не сел, **без риска разрыва**; ухудшение качества пара **без вибрации**
*4. Генератор* — ⚠️ **однофазное замыкание ротора на землю** без перехода в двойное; перегрузка статора **без перегрева обмотки и запаха**; отказ возбуждения **без потери возбуждения и КЗ**
*5. Вспомогательные системы* — питательная вода **не до уставок по уровню барабана**; конденсатная **без течи и резкого падения вакуума**; вакуумная — **медленное падение**, блок ещё держит малые обороты
*6. Вибрация и сдвиг (не фатально)* — ⚠️ **на 3000 об/мин размах ≥164 мкм, но не 240 мкм**, **без металлического шума**; осевой сдвиг выше допуска **без достижения защиты**, температура упорного в норме
*7. Прочее* — ⚠️ **разница верх/низ выше 42°C** без риска потери зазоров; высокая температура выхлопа ЦНД без неравномерного расширения; **малая течь** с нарастанием, влияющая на безопасность на месте
*8. TSI* — ⚠️ **резкое ухудшение показаний** с явным трендом; ⚠️ **одновременные аномалии нескольких приборов одного подшипника**; ⚠️ **полный отказ TSI** — нет основы для контроля

⚠️ **Ключевое различие: 42°C и 50°C.** Разница верх/низ выше **42°C** — отключение без срыва вакуума. Выше **50°C** — **со срывом**. Восемь градусов определяют разную процедуру.
⚠️ **По вибрации так же: 164 мкм — без срыва, 240 мкм — со срывом.**

---

**🇬🇧 Trip Without Breaking Vacuum — 8 categories**

**Core premise:** the fault **does not directly threaten the core safety of the unit's main body** (rotor, bearings, rotor-stator clearance). ⚠️ **Maintaining condenser vacuum reduces the risk of rotor thermal bending and shortens the restart cycle.**

**Procedure (6 steps)** — as POST 33 but **with no vacuum-breaking step**

**CATEGORIES**
*1. Governing and control system* — governor valve sticking, load unadjustable or speed deviating, ⚠️ **without causing overspeed (not reaching 110%)**; abnormal decrease in hydraulic control oil pressure ⚠️ **(not triggering trip protection)** or servo system failure; auto-synchronizer or DEH failure giving unstable operation ⚠️ **without mechanical jamming or short-circuit risk**
*2. Non-fatal lube oil failures* — pressure at the minimum allowable value ⚠️ **(not reaching trip)** and not restored by starting the standby pump, ⚠️ **no oil cut-off and bearing metal within limits**; ⚠️ **oil temperature rising sharply above 60°C** with cooling ineffective but **no overheating or oil slinging**; tank level too low ⚠️ **(not below the minimum alarm value)** with replenishment ineffective but circulation unaffected
*3. Severe steam parameter deviation* — ⚠️ **overheating or sudden drop exceeding 50°C within 15 minutes but not reaching trip value**, unrecoverable by desuperheating, no leak or metal overheating risk; significant pressure over-limit with safety valve not actuating or not reseating, ⚠️ **but no pipe rupture risk**; severe steam quality deterioration causing scaling and corrosion ⚠️ **without vibration or sudden parameter change**
*4. Non-severe generator and electrical faults* — ⚠️ **single-point grounding of the generator rotor** not developing into two-point, stator insulation undamaged; stator overload near the allowable limit, unrelieved by reducing load, ⚠️ **but no winding overheating or peculiar smell**; excitation faults giving unstable terminal voltage ⚠️ **without loss of excitation or short circuit**
*5. Auxiliary failures preventing normal operation* — feedwater failure with drum level out of control ⚠️ **(not reaching low/high trip)**; condensate failure ⚠️ **without condenser leakage or sudden vacuum drop**; vacuum pump trip not recoverable quickly, vacuum falling **slowly**, ⚠️ **unit can still maintain low-speed operation without negative pressure damage risk**
*6. Over-limit vibration and displacement (non-fatal)* — ⚠️ **at 3000 r/min, bearing vibration double amplitude ≥164 μm but not reaching the trip setting (≥240 μm)**, with **no obvious metal friction sound**; axial displacement beyond the allowable range ⚠️ **but not reaching trip**, thrust temperature within limits, no wear signs
*7. Other abnormalities not endangering the main body* — ⚠️ **abnormal flange and bolt temperatures giving an upper-to-lower cylinder difference exceeding 42°C**, without risk of clearance loss or cylinder deformation; excessively high LP exhaust temperature unrelieved by spray, without uneven expansion or increased vibration; **minor leakage** at valves or flanges (no fire or poisoning risk) ⚠️ **but with leakage volume continuing to increase and affecting on-site safe operation**
*8. TSI abnormal or failed* — ⚠️ **TSI parameters deteriorating sharply** (sudden vibration increase, rapid axial drift); although not at trip value, **the trend is clear and may exceed the limit in a short period**; ⚠️ **simultaneous abnormalities in multiple related TSI instruments** (e.g. both vibration and temperature of the same bearing inaccurate or over limit), **making it impossible to rule out an actual equipment fault**; ⚠️ **overall failure of the TSI system** (power interruption, total loss of signals), leaving **no monitoring basis for core parameters**

⚠️ **The critical distinction: 42°C versus 50°C.** Upper-to-lower cylinder difference above **42°C** → trip without breaking vacuum. Above **50°C** → **trip with vacuum breaking** (POST 34, item 12). Eight degrees decides which procedure applies.
⚠️ **Same for vibration: 164 μm without breaking vacuum, 240 μm with.**

`#trip #vacuumretained #TSIfailure`

---
---

## POST 71 — ACCWS ishga tushirish protsedurasi

**🇺🇿 ACCW nasos — tayyorgarlik va ishga tushirish**

**Ishga tushirishdan oldin — 16 ta tekshiruv**
1. Xizmat suvi tizimi normal ishlayapti
2. Xizmat suvidan ACCW nasosga quvur klapanlari to'g'ri holatda
3. ⚠️ **Xizmat suvi sarfi (00PCM30/40CF101) normal: ≥5.6 m³/s**
4. Sarf ko'rsatkichi (00PCM30/40CF001) normal
5. Nasos dvigateli upor podshipnik sovutish suvi ishda
6. Nasos salniki moylash va sovutish suvi ishda
7. ⚠️ **Xizmat suvi harorati (00PCM30/40CP501) normal: ≤60°C**
8. ⚠️ **Dvigatel upor podshipnik sovutish suvi va salnik moylash suvi kamida 5 DAQIQA ishlab turgan bo'lishi shart**
9. ⚠️ **Salnik materialining tarangligi tekshiriladi — juda tarang ham, juda bo'sh ham bo'lmasin. Salnik qopqog'ining tekisligiga e'tibor bering**
10. Barcha issiqlik asboblari to'g'ri ko'rsatmoqda
11. Nasos so'rish havzasi tozalangan va tegishli suv bilan to'ldirilgan
12. ⚠️ **So'rish havzasi sathi normal: suv sathi >−1.7 m, nasosning minimal cho'kish chuqurligi −3.6 m**
13. ⚠️ **DCS dagi sath transmitteri joyidagi ko'rsatkich bilan mos — ikki tomonlama tasdiqlash**
14. Nasos trip himoyalari ishda
15. Nasos dvigateli izolyatsiyasi normal, dvigatel ishchi holatga qo'yilgan
16. Bog'liq tizimlar holati tekshirilgan

**Bog'liq tizimlar (Table 5-1-2)**
| Tizim | Bog'liqlik | Holat |
|---|---|---|
| Xizmat suvi | ACCWS nasosga dvigatel sovutish va podshipnik moylash suvi | **Ishda** |
| Stansiya oqava chiqindi tizimi | ACCWS dan o'tkazuvchanlik va pH monitoring oqimini qabul qiladi | **Ishga tayyor** |
| HRSG purge tizimi | ACCWS dan sovutish suvini qabul qiladi | **Ishdan tashqari** |
| HRSG purge tizimi | Purge suvini ACCWS qaytish quvuriga haydaydi | **Ishdan tashqari** |
| Kondensator CCWS | ACCWS bilan umumiy qaytish quvurini bo'lishadi | **Suv to'ldirishga tayyor** |
| Mashina zali drenaj flash baki | CCWS va ACCWS qaytish quvuriga suv chiqaradi | **Pnevmatik klapan yopiq** |
| Kondensat ortiqcha oqish drenaji | CCWS va ACCWS qaytish quvuriga chiqaradi | **Pnevmatik klapan yopiq** |
| Mexanik ventilyatsiyali gradirnya | CCWS bilan umumiy gradirnyani bo'lishadi | ⚠️ **20 ta yacheykadan kamida 2 tasi ishda** |

**Ishga tushirish**
1. DCS da ruxsat shartlarini tasdiqlang
2. ⚠️ **Birinchi nasos (00PAC11/12AP001) uchun chiqish klapanini (00PAC11/12AA002) 30° ga oching**
3. Nasosni ishga tushiring
4. ⚠️ **Nasos ishga tushgandan keyin 45 SEKUND ichida chiqish klapani uzluksiz ochilib to'liq ochilganini tasdiqlang**
5. ACCW tizimi va CCWS qaytish quvuriga suv to'ldirishni boshlang
6. To'ldirish tugagach nasos parametrlarini tekshiring
7. Zaxira nasosni **"Lock on"** holatiga qo'ying

**Avtomatik ishga tushirish jarayoni — 10 qadam**
1. Gradirnya qaytish elektr klapanini och
2. Issiqlik almashgich kirish va chiqish MOV larini och
3. Oldindan tanlangan elektr suv filtri kirish va chiqish MOV larini och
4. ACCW kollektor drenaj klapanini yop (00PAC10AA001XB12)
5. ACCW nasos sovutish suvi solenoid klapanini och (00PCM30AA002/00PCM40AA002)
6. **ACCW nasos chiqish MOV ni YOP**
7. Oldindan tanlangan ACCW nasosni ishga tushir
8. Tanlanmagan nasosni zaxira rejimiga qo'y
9. ⚠️ **ACCW nasos sovutish suvi sarfi past bo'lmasa, 30 SEKUND kechiktirib sovutish suvi solenoid klapanini yop**
10. Tugadi

⚠️ **Avtomatik jarayonda 6-qadam — chiqish MOV YOPILADI, keyin nasos ishga tushadi.** Qo'lda ishga tushirishda esa **30° ga ochiladi**. Ikki xil mantiq — chalkashtirmang.

⚠️ **To'xtatish sharti:** ACCWS faqat **CCCWS va HRSG purge tizimi sovutish suviga muhtoj bo'lmaganda** to'xtatiladi.

---

**🇷🇺 Насос ВЦОС — подготовка и пуск**

**16 проверок перед пуском**
Служебная вода в работе | задвижки в правильном положении | ⚠️ **расход служебной воды ≥5.6 м³/ч** | индикатор расхода в норме | охлаждение упорного подшипника двигателя в работе | смазка и охлаждение сальника в работе | ⚠️ **температура служебной воды ≤60°C** | ⚠️ **охлаждение и смазка работают не менее 5 МИНУТ** | ⚠️ **набивка не слишком тугая и не слишком слабая, крышка сальника ровная** | приборы показывают верно | приёмный колодец очищен и заполнен | ⚠️ **уровень >−1.7 м, минимальное погружение насоса −3.6 м** | ⚠️ **уровень в DCS совпадает с местным — двойное подтверждение** | защиты в работе | изоляция двигателя в норме | связанные системы проверены

**Связанные системы** — служебная вода **в работе** | сброс стоков **готов** | продувка КУ **выведена** (обе позиции) | ЦОС конденсатора **готова к заполнению** | дренажный расширитель машзала **клапан закрыт** | перелив конденсата **клапан закрыт** | градирня — ⚠️ **не менее 2 из 20 секций в работе**

**Пуск**
Подтвердить разрешения → ⚠️ **открыть напорную задвижку на 30°** → пустить насос → ⚠️ **за 45 СЕКУНД задвижка должна открыться полностью** → заполнение → проверка параметров → резервный в **"Lock on"**

**Автоматический пуск — 10 шагов**
Открыть обратную задвижку градирни → задвижки теплообменника → задвижки фильтра → **закрыть дренаж коллектора** → открыть соленоид охлаждения насоса → **ЗАКРЫТЬ напорную задвижку** → пустить насос → второй в резерв → ⚠️ **если расход охлаждения не низкий, через 30 СЕКУНД закрыть соленоид** → конец

⚠️ **В автоматике шаг 6 закрывает напорную задвижку, при ручном пуске она открывается на 30°.** Разная логика.
⚠️ **Останов только когда ЗКОС и продувка КУ не требуют охлаждения.**

---

**🇬🇧 ACCW Pump — preparation and start-up**

**16 checks before start**
Service water system normal | valve line-up correct | ⚠️ **service water flow to ACCW pump (00PCM30/40CF101) normal, ≥5.6 m³/h** | flow indicator (00PCM30/40CF001) normal | motor thrust bearing cooling water in service | packing lubricating and cooling water in service | ⚠️ **service water temperature (00PCM30/40CP501) normal, ≤60°C** | ⚠️ **motor thrust bearing cooling and packing lubricating water in service and fully functional for at least 5 MINUTES** | ⚠️ **check tightness of the packing material — not too tight, not too loose; pay attention to evenness of the packing cover** | all thermal instruments showing correctly | suction pool cleaned and filled with proper water | ⚠️ **pool level normal: water level >−1.7 m, minimum pump submerge depth −3.6 m** | ⚠️ **DCS level transmitter consistent with site (double confirmation)** | pump trip protections in service | motor insulation normal, motor in working position | related systems checked

**Related systems (Table 5-1-2)**
Service water **in service** | plant effluent discharge **ready** | HRSG blow down **out of service** (both entries) | condenser CCWS **ready for water filling** | turbine hall drains flash tank **pneumatic valve closed** | condensate overflow drain **pneumatic valve closed** | mechanical ventilation cooling tower — ⚠️ **at least 2 of 20 cells in service**

**Start-up**
Confirm permissives on DCS → ⚠️ **for the first pump, open the discharge valve (00PAC11/12AA002) to 30°** → start the pump → ⚠️ **confirm the outlet valve continues opening to fully open WITHIN 45 SECONDS** → start water filling into ACCW and CCWS return pipeline → check parameters → select standby pump to **"Lock on"**

**Auto process start — 10 steps**
Open cooling tower return electric valve → open heat exchanger inlet/outlet MOVs → open pre-selected electric water filter inlet/outlet MOVs → close ACCW header drain valve → open pump cooling water solenoid → **CLOSE the pump outlet MOV** → start the pre-selected pump → put the other pump in standby → ⚠️ **if cooling water flow is not low, delay 30 s and close the cooling water solenoid** → finish

⚠️ **In the auto sequence step 6 CLOSES the outlet MOV before starting; in manual start it is opened to 30° first.** Two different logics.
⚠️ **Shutdown only after CCCWS and HRSG blow down no longer need cooling water.**

`#ACCWS #startup #procedure`

---
---

## POST 72 — CCWS ishga tushirish va to'xtatish

**🇺🇿 CCW nasos — ishga tushirish ketma-ketligi**

**Birinchi nasos**
1. ⚠️ **Chiqish klapanini (00PAC21/22AA001) 30° ga oching**
2. Ishga tushiriladigan CCW nasosni tanlang
3. **"start"** → 4. **"ACK"** → 5. Nasos ishga tushdi
6. CCWS suv to'ldirishni boshladi
7. ⚠️ **Aylanma sovutish suvi quvurlari to'liq suv bilan to'lganini va quvur ichidagi barcha havo chiqarilganini tasdiqlang**
8. Nasos chiqish klapanini to'liq ochishda davom eting
9. ⚠️ **Nasos chiqish bosimi 2.0–2.7 bar oralig'ida ekanini tasdiqlang**
10. Parametrlarni tekshiring

**Ikkinchi nasos — ketma-ket ishga tushirish**
• **"sequence start"** → **"ACK"**
• ⚠️ **Ikkinchi nasos ishga tushadi, va chiqish gidravlik butterfly klapani nasos ishga tushishi bilan BIR VAQTDA ochiladi**
• Klapan to'liq ochiladi
• ⚠️ **Ikkinchi nasos chiqish bosimi ham 2.0–2.7 bar**
• Parametrlarni qayd eting: **nasos tebranishi, podshipnik harorati, chiqish kollektor bosimi, kirish filtri Δp, dvigatel o'ram harorati**

**Faqat bitta nasos kerak bo'lsa**
Ikkinchi nasosning **"Lock off"** tugmasini bosing → **"put in"** → **"Lock on"** ga o'zgaradi = zaxira holati

**To'xtatish — barcha shartlar bajarilishi shart**
☑ Bug' turbinasi to'xtagan va **turning gear** da ishlayapti
☑ **GT1, GT2 yoki ikkalasi SIMPLE CYCLE rejimida** ishlayapti
☑ HRSG lar ishdan tashqari
☑ Kondensatorga boradigan barcha HP, IP, LP bug' quvur drenaj klapanlari **yopiq va ajratilgan**
☑ HP, IP va LP bypass ishdan tashqari va hammasi yopiq
☑ Turbina gland tizimi ishdan tashqari
☑ Suv halqali vakuum nasos ishdan tashqari

**To'xtatish ketma-ketligi**
1. Barcha iste'molchilar to'xtagan
2. Zaxira CCW nasosni **"Lock off"** ga chiqaring
3. To'xtatiladigan nasosni tanlang → **"stop"** → **"ACK"**
4. ⚠️ **Chiqish gidravlik klapani TEZ yopiladi**
5. ⚠️ **Chiqish klapani 30 gradusga yopilgandan KEYIN nasos to'xtaydi**
6. ⚠️ **Chiqish klapani 30 gradusdan 0 gacha SEKIN yopilishda davom etadi**

**Avtomatik ishga tushirish (birinchi nasos) — 7 qadam**
1. Gradirnya qaytish suvi motorli klapanini och
2. Kondensator aylanma sovutish suvi kirish va chiqish motorli klapanlarini och
3. CCW nasos dvigateli xizmat sovutish suvi motorli klapanini och
4. CCW nasos chiqish kollektor purge boshqaruv klapanini yop (00PAC20AA101)
5. **CCW nasos chiqish gidravlik klapanini 30° ga och**
6. Aylanma suv nasosini ishga tushir
7. Chiqish gidravlik klapanini to'liq och

⚠️ **CCWS va ACCWS ning avtomatik mantiqi TESKARI:** ACCWS da klapan **yopiladi** keyin nasos ishga tushadi; CCWS da klapan **30° ga ochiladi** keyin nasos ishga tushadi. Nasos turi boshqa (CCWS — vertikal o'q oqimli).

⚠️ **To'xtatishda klapanning ikki bosqichli yopilishi (tez → 30° → sekin 0 gacha)** — bu gidravlik zarbadan himoya. Klapan darhol to'liq yopilsa quvurda zarba bo'ladi.

---

**🇷🇺 Насос ЦОС — пуск и останов**

**Первый насос** — ⚠️ **открыть напорную задвижку на 30°** → выбрать насос → **start** → **ACK** → заполнение → ⚠️ **убедиться, что трубопроводы заполнены и воздух стравлен** → открыть задвижку полностью → ⚠️ **давление на нагнетании 2.0–2.7 бар** → проверить параметры

**Второй насос** — **sequence start** → **ACK** → ⚠️ **насос пускается, гидравлическая заслонка открывается ОДНОВРЕМЕННО с пуском** → ⚠️ **давление тоже 2.0–2.7 бар** → записать **вибрацию, температуру подшипника, давление коллектора, Δp фильтра, температуру обмотки**
Если нужен один насос — **Lock off** → **put in** → **Lock on** = резерв

**Условия останова** — ПТ остановлена и на ВПУ | **ГТ1, ГТ2 или обе в режиме ГТУ** | КУ выведены | все дренажи ВД/СД/НД в конденсатор **закрыты и отсечены** | БРОУ выведены и закрыты | система уплотнений выведена | водокольцевой вакуумный насос выведен

**Останов** — резервный в **Lock off** → выбрать насос → **stop** → **ACK** → ⚠️ **заслонка закрывается БЫСТРО** → ⚠️ **после закрытия до 30° насос останавливается** → ⚠️ **далее заслонка МЕДЛЕННО закрывается с 30° до 0**

**Автоматический пуск — 7 шагов**
Обратная задвижка градирни → задвижки циркводы конденсатора → охлаждение двигателя → **закрыть продувку коллектора** → **открыть гидрозаслонку на 30°** → пустить насос → открыть заслонку полностью

⚠️ **Логика ЦОС и ВЦОС ПРОТИВОПОЛОЖНА:** в ВЦОС задвижка **закрывается** перед пуском, в ЦОС **открывается на 30°**.
⚠️ **Двухступенчатое закрытие при останове (быстро → 30° → медленно до 0)** — защита от гидроудара.

---

**🇬🇧 CCW Pump — start-up and shutdown**

**First pump** — ⚠️ **open the discharge valve (00PAC21/22AA001) to 30°** → click the pump → **"start"** → **"ACK"** → water filling begins → ⚠️ **confirm the pipeline is fully filled and all air vented** → continue opening the discharge valve to fully open → ⚠️ **confirm discharge pressure is 2.0–2.7 bar** → monitor parameters

**Second pump** — **"sequence start"** → **"ACK"** → ⚠️ **the pump starts and the outlet hydraulic butterfly valve opens AT THE SAME TIME as the pump starts** → ⚠️ **discharge pressure also 2.0–2.7 bar** → record **pump vibration, bearing temperature, outlet header pressure, inlet filter differential pressure, motor winding temperature**
If only one pump is required — **"Lock off"** → **"put in"** → changes to **"Lock on"** = standby

**Shutdown conditions — all required**
☑ Steam turbine shut down and running on turning gear
☑ **GT1, GT2 or both operating in SIMPLE CYCLE mode**
☑ HRSGs out of service
☑ All HP, IP, LP steam pipeline drain valves leading into the condenser **closed and isolated**
☑ HP, IP, LP bypass out of service and closed
☑ Turbine gland system out of service
☑ Water ring vacuum pump out of service

**Shutdown sequence**
All consumers stopped → release standby pump to **"Lock off"** → select the pump → **"stop"** → **"ACK"** → ⚠️ **outlet hydraulic valve closes FAST** → ⚠️ **after the valve closes to 30 degrees, the pump stops** → ⚠️ **the valve continues closing SLOWLY from 30 degrees to 0**

**Auto process start (first pump) — 7 steps**
Open cooling tower return water motor valve → open condenser circulating water inlet and outlet motor valves → open CCW pump motor service cooling water motor valve → close CCW pump outlet header blow down control valve → **open outlet hydraulic valve to 30°** → start the pump → open the valve fully

⚠️ **CCWS and ACCWS auto logic is OPPOSITE:** ACCWS **closes** the outlet valve before starting; CCWS **opens it to 30°** first. Different pump type (CCWS is vertical axial flow).
⚠️ **The two-stage closing on shutdown (fast → 30° → slow to 0)** is water hammer protection. Closing fully in one go would shock the pipeline.

`#CCWS #startup #waterhammer`

---
---

## POST 73 — Rubber ball tizimi: ishga tushirish

**🇺🇿 Shar tozalash — setpoint va tayyorgarlik**

**Setpointlar**
| Parametr | KKS | Chegara |
|---|---|---|
| Kondensator A tomoni shar filtri Δp H | 10PAB11CP101 | ⚠️ **>70 mbar** — Alarm |
| Kondensator B tomoni shar filtri Δp H | 10PAB12CP101 | ⚠️ **>70 mbar** — Alarm |

**Klapan holati — A tomoni**
| Uskuna | KKS | Holat |
|---|---|---|
| Shar filtri chiqish qo'l klapani | 10PAH01AA002 | **Ochiq** |
| Shar filtri chiqish qo'l klapani | 10PAH01AA003 | **Ochiq** |
| Shar nasosi kirish qo'l klapani | 10PAH01AA002 | **Ochiq** |
| Shar chiqish motorli klapani | 10PAH01AA004 | **Yopiq** |
| Shar yig'gich on-off klapani | 10PAH01BB001 | **Yopiq** |
| Shar yig'gich chiqish motorli klapani | 10PAH01AA005 | **Yopiq** |
| Kondensator CCW kirish quvuri shar taqsimlagich chiqish klapani | 10PAH01AA006 | **Ochiq** |
| Kondensator CCW kirish quvuri shar taqsimlagich chiqish klapani | 10PAH01AA007 | **Ochiq** |
| Shar filtri | 10PAH01AT001 | **Ochiq** |

**B tomoni** — o'sha ro'yxat, KKS **10PAH02...**, shar filtri **10PAB12AT001**

**Tayyorgarlik**
1. Klapanlar holatini tekshiring
2. ⚠️ **Kerakli miqdordagi rezina sharlarni tayyorlang va 24 SOAT HO'LLANG**
3. ⚠️ **Ho'llangandan keyin yaroqli sharlarni tanlab oling**
4. Shar yig'gich kirish va chiqish motorli klapanlarini yoping (A: 10PAH01AA004/005, B: 10PAH02AA004/005)
5. Shar yig'gich drenaj klapanini oching (A: 10PAH01AA401, B: 10PAH02AA401)
6. Shar yig'gichning yuqori qopqoq vent klapanini oching — ichidagi suvni chiqarish uchun

⚠️ **24 soatlik ho'llash majburiy.** Quruq shar o'lchamini to'liq olmaydi, quvur devoriga tegmaydi va tozalash bermaydi. Bu qadam ko'pincha o'tkazib yuboriladi.

⚠️ **"Yaroqli sharlarni tanlab olish"** — ho'llangandan keyin bir qismi noto'g'ri o'lchamda bo'ladi. Ularni tizimga qo'shish quvurlarni to'sadi.

⚠️ **Δp 70 mbar** — bu shar filtri uchun. Kondensat nasos filtri **10 kPa = 100 mbar**, CCCWS kirish filtri **5 kPa = 50 mbar**, ACCWS elektr filtri **60 kPa = 600 mbar**. Har biri boshqa — chalkashtirmang.

⚠️ **10PAH01AA002 ro'yxatda IKKI MARTA keltirilgan** — shar filtri chiqish klapani va shar nasosi kirish klapani sifatida. Manualdagi ehtimoliy xato; joyida P&ID bo'yicha tekshiring.

---

**🇷🇺 Шариковая очистка — уставки и подготовка**

**Уставки** — Δp фильтра шариков сторона A (**10PAB11CP101**) и сторона B (**10PAB12CP101**): ⚠️ **>70 мбар — сигнал**

**Положение задвижек, сторона A**
10PAH01AA002 **открыта** | 10PAH01AA003 **открыта** | вход насоса 10PAH01AA002 **открыта** | 10PAH01AA004 **закрыта** | сборник 10PAH01BB001 **закрыта** | 10PAH01AA005 **закрыта** | распределитель 10PAH01AA006 и 10PAH01AA007 **открыты** | фильтр 10PAH01AT001 **открыт**
**Сторона B** — то же, KKS **10PAH02...**, фильтр **10PAB12AT001**

**Подготовка**
Проверить задвижки → ⚠️ **подготовить шарики и ЗАМОЧИТЬ НА 24 ЧАСА** → ⚠️ **после замачивания отобрать годные** → закрыть входную и выходную задвижки сборника → открыть дренаж сборника → открыть воздушник верхней крышки сборника

⚠️ **24 часа замачивания обязательны.** Сухой шарик не набирает размер, не касается стенки и не чистит. Этот шаг часто пропускают.
⚠️ **Отбор годных** — часть шариков после замачивания имеет неверный размер и забьёт трубки.
⚠️ **70 мбар — только для фильтра шариков.** Фильтр КЭН — **10 кПа**, фильтр ЗКОС — **5 кПа**, электрофильтр ВЦОС — **60 кПа**.
⚠️ **10PAH01AA002 указан в списке ДВАЖДЫ** — как выход фильтра и как вход насоса. Вероятная ошибка руководства; сверьте по P&ID.

---

**🇬🇧 Rubber Ball Cleaning System — settings and preparation**

**Settings**
Condenser side A ball strainer Δp (**10PAB11CP101**) and side B (**10PAB12CP101**): ⚠️ **>70 mbar — Alarm**

**Valve state, condenser A side**
Ball strainer outlet manual 10PAH01AA002 **Open** | 10PAH01AA003 **Open** | ball pump inlet manual 10PAH01AA002 **Open** | ball outlet motor 10PAH01AA004 **Close** | ball collector on-off 10PAH01BB001 **Close** | collector outlet motor 10PAH01AA005 **Close** | CCW inlet pipeline distributor outlet 10PAH01AA006 and 10PAH01AA007 **Open** | ball strainer 10PAH01AT001 **Open**
**B side** — same list, KKS **10PAH02...**, strainer **10PAB12AT001**

**Preparation**
Check valve states → ⚠️ **prepare a certain number of rubber balls and SOAK THEM FOR 24 HOURS** → ⚠️ **select the qualified rubber balls after soaking** → close the ball collector inlet and outlet motor valves → open the ball collector drain valve → open the top cover vent valve of the collector to drain water inside

⚠️ **The 24-hour soak is mandatory.** A dry ball does not reach full size, does not contact the tube wall, and does not clean. This step gets skipped often.
⚠️ **"Select the qualified balls"** — after soaking some are the wrong size; putting those into the system blocks tubes.
⚠️ **70 mbar applies to the ball strainer only.** Condensate pump inlet filter is **10 kPa**, CCCWS inlet filter **5 kPa**, ACCWS electric filter **60 kPa**.
⚠️ **10PAH01AA002 appears TWICE in the manual's list** — as strainer outlet and as ball pump inlet. Probable manual error; verify against the site P&ID.

`#rubberball #condensercleaning #PAH`

---
---

## POST 74 — Gland steam ishga tushirish

**🇺🇿 Val zichlash bug'ini berish — aniq qiymatlar**

**Ketma-ketlik**
1. ⚠️ **Elektr qizdirgichni ishga tushiring**, va yordamchi bug'dan gland steam kollektoriga bosim rostlash klapanini oching
2. ⚠️ **Kollektor bosimini 32 kPa da rostlang**
3. Kollektor bug' haroratini Fig 5-7-1 dagi chegaraga muvofiq sozlang
4. Ishga tushiriladigan blowerni tanlang
5. **Blower A/B ni ishga tushiring**, ikkinchisini **avto boshqaruvga** qo'ying
6. ⚠️ **Blower kirish klapanini bug'ning val packinglaridan atmosferaga sizib chiqishini oldini oladigan qilib sozlang. Normal packing zazorlarida taxminan −0.035 ~ −0.04 barg vakuum ko'rsatkichi odatda yetarli**
7. ⚠️ **TCS turbinaning orqa gland bo'ynidagi haroratni (10MAW11CT006) TCV (10LCE12AA101) ochilishini o'zgartirib taxminan 150–180°C da ushlab turadi**

**To'xtatish shartlari — hammasi bajarilishi shart**
☑ Bug' turbinasi to'xtagan
☑ HRSG1 va HRSG2 ikkalasi ham to'xtagan
☑ HP, IP va LP bypass bosim rostlash klapanlari yopiq
☑ Vakuum nasos A va B ikkalasi ham to'xtagan
☑ ⚠️ **Kondensator vakuumi 0 kPa gacha tushayapti**
☑ ⚠️ **Bug' turbinasi lube oil, seal oil, jacking oil va turning gear tizimlari ISHDA**

**To'xtatish ketma-ketligi**
1. Zaxira gland steam kondensator blowerini chiqaring
2. Blowerni to'xtating
3. Yordamchi bug'dan gland steam kollektoriga bosim rostlash klapanini yoping
4. Elektr qizdirgichni to'xtating

⚠️ **Uch xil bosim qiymati bir tizimda:**
• **32 kPa = 0.32 barg** — ishga tushirishda kollektor rostlash qiymati (5.7.3) va self-sealed rejim setpointi (3.8)
• **1.29 bar.a** — Table 1-1-1 dagi steam seal header nominal qiymati
• **10–42 kPa** — 6-bobdagi alarm chegaralari
Birinchi ikkitasi turli o'lchov bazasida (gauge va absolute), uchinchisi alarm oynasi.

⚠️ **−0.035 ~ −0.04 barg** — bu blower vakuumi, **kollektor bosimi emas**. Lube oil bak vakuumi esa **−1.18 mbarg** — 30 barobar kichikroq. Uchalasi butunlay boshqa qiymatlar.

⚠️ **150–180°C — LP packing oynasi** (POST 8 dagi 30°C li tor oyna). TCV **10LCE12AA101** kondensat orqali desuperheating qiladi. Bu klapan ishlamasa LP packing haroratini ushlab bo'lmaydi.

⚠️ **To'xtatishda lube/seal/jacking/turning gear ISHDA bo'lishi shart** — gland steam ulardan oldin chiqariladi, keyin emas. POST 53 dagi 13 qadamli ketma-ketlikda bu 9-qadam.

---

**🇷🇺 Подача уплотняющего пара — точные значения**

**Последовательность**
⚠️ **Пустить электроподогреватель**, открыть регулятор подачи вспомогательного пара → ⚠️ **держать давление коллектора 32 кПа** → температура по кривой Fig 5-7-1 → выбрать эксгаустер → **пустить A/B, второй в авто** → ⚠️ **отрегулировать входную задвижку эксгаустера так, чтобы пар не выбивался в атмосферу; при нормальных зазорах достаточно разрежения примерно −0.035 ~ −0.04 барг** → ⚠️ **TCS держит температуру на задней горловине уплотнения (10MAW11CT006) около 150–180°C изменением открытия TCV (10LCE12AA101)**

**Условия останова** — ПТ остановлена | оба КУ остановлены | БРОУ закрыты | оба вакуумных насоса остановлены | ⚠️ **вакуум снижается до 0 кПа** | ⚠️ **маслосистема, уплотняющее масло, гидроподъём и ВПУ В РАБОТЕ**

**Останов** — вывести резервный эксгаустер → остановить эксгаустер → закрыть регулятор подачи → остановить электроподогреватель

⚠️ **Три разных значения давления:** **32 кПа = 0.32 барг** (пуск и самоуплотнение) | **1.29 бар.а** (номинал Table 1-1-1) | **10–42 кПа** (уставки сигналов главы 6)
⚠️ **−0.035 ~ −0.04 барг — разрежение эксгаустера, а не коллектора.** Разрежение маслобака — **−1.18 мбарг**, в 30 раз меньше.
⚠️ **150–180°C — окно уплотнений ЦНД.** TCV **10LCE12AA101** делает впрыск конденсата; без него окно не удержать.
⚠️ **При останове масло, уплотняющее масло, гидроподъём и ВПУ должны БЫТЬ В РАБОТЕ** — уплотняющий пар выводится раньше них.

---

**🇬🇧 Leading Steam into the Gland Steam System**

**Sequence**
⚠️ **Start the electric heater**, open the auxiliary steam to gland steam header pressure control valve → ⚠️ **regulate the gland steam header pressure at 32 kPa** → adjust header steam temperature to the limit in Fig 5-7-1 → click the blower to be started → **start blower A/B, put the other into auto control** → ⚠️ **adjust the blower inlet valve to prevent steam leaking to atmosphere from the shaft packings. With normal packing clearances a vacuum reading of approximately −0.035 to −0.04 barg is usually adequate** → ⚠️ **TCS maintains adjusted temperature (10MAW11CT006) at the turbine rear gland neck at about 150–180°C by means of TCV (10LCE12AA101) opening change**

**Shutdown conditions — all required**
☑ Steam turbine shut down ☑ Both HRSG1 and HRSG2 shut down ☑ HP, IP, LP bypass pressure control valves closed ☑ Both vacuum pumps A and B stopped ☑ ⚠️ **Condenser vacuum decreasing to 0 kPa** ☑ ⚠️ **Steam turbine lube oil, sealing oil, jacking oil and turning gear systems IN OPERATION**

**Shutdown sequence**
Release the standby gland steam condenser blower → stop the blower → close the pressure control valve from auxiliary steam to gland steam header → stop the electric heater

⚠️ **Three different pressure figures in one system:** **32 kPa = 0.32 barg** (start-up regulation and self-sealed setpoint) | **1.29 bar.a** (Table 1-1-1 nominal) | **10–42 kPa** (Chapter 6 alarm window). The first two use different reference bases.
⚠️ **−0.035 to −0.04 barg is the blower vacuum, not the header pressure.** Lube oil reservoir vacuum is **−1.18 mbarg** — thirty times smaller. Three completely different numbers.
⚠️ **150–180°C is the LP packing window** (the 30°C-wide window from POST 8). TCV **10LCE12AA101** desuperheats with condensate; without it the window cannot be held.
⚠️ **At shutdown, lube oil, seal oil, jacking oil and turning gear must be IN SERVICE** — gland steam comes out before them, not after. This is step 9 of the 13-step sequence in POST 53.

`#glandsteam #startup #blower #TCV`

---
---

## POST 75 — Podshipnik harorati oshishi

**🇺🇿 Podshipnik harorati yuqori — sabab va harakat**

⚠️ **Mohiyati: "issiqlik hosil bo'lishi issiqlik tarqalishidan oshadi".** To'rt turdagi muammo: **moylash, yuklama, sovutish, uskunaning o'zi.**

**BELGILAR**
1. **Harorat chegaradan chiqishi** — podshipnik yog' qaytish harorati va vkladish metall harorati loyihaviy ruxsat etilgan qiymatlardan oshadi, "podshipnik harorati yuqori" alarmi ishlaydi
2. **Tebranish va g'ayritabiiy shovqin** — podshipnik korpusi tebranishi sezilarli oshadi. Joyida podshipnik ichidan **"shitirlash" ishqalanish tovushi** yoki **"g'uvillash"** eshitiladi; og'ir holatda **"metall zarba tovushi"**
3. **Moylash tizimida anomaliya** — ⚠️ **podshipnik yog' qaytish ko'rish oynasida oqimda aralashmalar yoki havo pufakchalari ko'rinadi.** Ba'zi hollarda **yog' qaytish hajmi kamayadi**, hatto **yog' sathi tez tushadi**
4. **Val tizimi parametrlarining tebranishi** — harorat ko'tarilishi ortiqcha o'q kuchidan bo'lsa, **o'q siljishining sezilarli oshishi** bilan birga keladi, bu esa podshipnik yuklamasini yanada kuchaytiradi

**SABABLAR**

*1. Moylash tizimi nosozligi (ENG KENG TARQALGAN)*
• **Yog' sifatining buzilishi** — yog' emulsifikatsiyalashadi, aralashmalar (masalan **metall qipiqlari**) bo'ladi, yoki qovushqoqligi pasayadi → **barqaror yog' plyonkasi hosil bo'lmaydi**
• **Yog' hajmi/bosimi yetarli emas** — bakda sath past, yog' nasosi nosozligi, ta'minot quvuri tiqilgan, yoki **klapan noto'g'ri yopilgan**
• ⚠️ **Barqaror bo'lmagan yog' plyonkasi** — ishga tushirishda tezlik juda past bo'lganda **jacking oil tizimi nosozligi**, yoki **podshipnik zazori juda katta/juda kichik** → **"yarim quruq ishqalanish"**

*2. Podshipnik yuklamasining anomaliyasi*
• **Ortiqcha o'q kuchi** — bug' parametrlarining tebranishi (masalan **main bug' bosimining to'satdan ko'tarilishi**), **diafragmalarda cho'kma**, yoki **kondensator vakuumining tushishi** → o'q kuchi podshipnik ko'tarish qobiliyatidan oshadi
• **Val tekislanishining chetlanishi** — montaj yoki ta'mirdan keyin **podshipnik korpusi markazi rotor bilan mos kelmaydi** → podshipnik qo'shimcha radial kuch ko'taradi

*3. Sovutish tizimi nosozligi*
• **Yog' sovutgich nosozligi** — cho'kma va tiqilish, yoki **sovutish suvi klapanining yetarli ochilmaganligi**
• **Sovutish suvi sifatining pastligi** — aralashmalar sovutgichning issiqlik almashinuv kanalini to'sadi

*4. Podshipnikning o'z defektlari*
• **Qismlarning yeyilishi** — ⚠️ **vkladish babbit qatlamining yeyilishi va ko'chib tushishi** → ishqalanish maydoni va issiqlik hosil bo'lishi ortadi
• **Ortiqcha podshipnik zazori** — uzoq ish natijasida radial/o'q zazori loyihaviy qiymatdan oshadi → **yog' plyonkasi qalinligi ushlab turilmaydi**

**HARAKAT — "avval nazorat, keyin qidiruv, oxirida ta'mir"**

*1. Avariya nazorati va yuklamani tushirish*
⚠️ **Darhol qo'lda turbina yuklamasini tushiring** — podshipnik ko'taradigan radial/o'q kuchini kamaytirish va ishqalanish issiqligini kamaytirish uchun
⚠️ **Harorat ko'tarilishda davom etsa — qat'iy avariya to'xtatishni ishga tushiring**, vkladish babbitining erishi yoki rotorning **"val qotib qolishi"** ning oldini olish uchun

*2. Avval moylash tizimini tekshiring*
• **Bak sathi va yog' bosimi** — sath past bo'lsa darhol **bir xil markadagi** yog' qo'shing; bosim past bo'lsa **zaxira nasosga o'ting** va quvur tiqilganini tekshiring
• **Yog' sifati** — podshipnik yog' qaytishidan namuna oling, **emulsifikatsiya yoki aralashma** bor-yo'qligini kuzating. Sifat buzilgan bo'lsa **darhol yog' tozalash qurilmasini ishga tushiring** yoki yangi yog'ga almashtiring

*3. Sovutish tizimini tekshiring*
⚠️ **Yog' sovutgichning sovutish suvi kirish-chiqish harorat farqini tekshiring. Farq juda kichik bo'lsa (<5°C) — sovutgichni tozalang yoki sovutish suvi klapanini oching**
• Sovutish suvi nasosi normal ishlayaptimi, bosim va sarf loyihaviy talablarga mosmi

*4. Yuklama va uskunani tekshiring*
• **O'q siljishini kuzating** — chegaradan chiqsa **kondensator vakuumi va bug' parametrlarini tekshiring**, o'q kuchini kamaytirish uchun rejimni sozlang; samarasiz bo'lsa **diafragma yoki bug' zichlashida cho'kma bor-yo'qligini tekshirish uchun to'xtating**
• **To'xtatishdan keyin podshipnikni joyida ko'zdan kechiring** — vkladish babbit qatlami yeyilganmi, zazor chegaradan oshganmi

*5. Tiklanishdan keyin tasdiqlash*
Birlikni ishga tushiring va **yuklamani asta oshiring**, podshipnik harorati, tebranishi, yog' qaytishini real vaqtda kuzating. ⚠️ **Faqat barcha ko'rsatkichlar normaga qaytgandan keyin normal ishga qo'yish mumkin.**

⚠️ **"Farq <5°C" mezoni ikki joyda:** yog' sovutgichi uchun (10.4.3.3) va CCCWS sovutgichi uchun (11.2.2, haftalik TO). Ikkalasida ham **tozalash kerakligini** bildiradi.

---

**🇷🇺 Высокая температура подшипника — причины и действия**

⚠️ **Суть: «тепловыделение превышает теплоотвод».** Четыре группы: **смазка, нагрузка, охлаждение, сам подшипник.**

**ПРИЗНАКИ**
Температура слива и баббита выше допустимых, сигнал | Рост вибрации корпуса, **«шуршащий» шум трения** или **«гул»**, в тяжёлом случае **металлический удар** | ⚠️ **В смотровом стекле слива — примеси или пузыри воздуха**, снижение объёма слива, быстрое падение уровня | При избыточном осевом усилии — **рост осевого сдвига**

**ПРИЧИНЫ**
*Смазка (самое частое)* — эмульгирование, **металлическая стружка**, падение вязкости → нет плёнки; низкий уровень, отказ насоса, забитый трубопровод, **неверно закрытая задвижка**; ⚠️ **отказ гидроподъёма на малых оборотах** или **слишком большой/малый зазор** → **полусухое трение**
*Нагрузка* — **скачок давления главного пара**, **отложения на диафрагмах**, **падение вакуума**; **расцентровка после монтажа или ремонта**
*Охлаждение* — отложения в маслоохладителе, **недооткрытая задвижка охлаждающей воды**, примеси в воде
*Сам подшипник* — ⚠️ **износ и выкрашивание баббита**, **зазор выше проектного**

**ДЕЙСТВИЯ — «сначала контроль, потом поиск, затем ремонт»**
⚠️ **Немедленно разгрузить турбину**; ⚠️ **при продолжении роста — решительно аварийный останов**, чтобы не выплавить баббит и не заклинить вал
Проверить уровень и давление: долить **масло той же марки**, перейти на резервный насос, проверить трубопровод | Взять пробу слива на **эмульсию и примеси**, при ухудшении — **маслоочистка или замена**
⚠️ **Проверить перепад по охлаждающей воде маслоохладителя: если <5°C — чистить охладитель или открыть задвижку**
Контроль осевого сдвига → проверить вакуум и параметры пара; при неэффективности — останов и проверка **отложений на диафрагмах и уплотнениях** | После останова — **разборка и осмотр вкладыша**
⚠️ **Пуск с постепенным набором нагрузки, в работу только при нормализации всех показателей**

⚠️ **Критерий «<5°C» встречается дважды:** для маслоохладителя (10.4.3.3) и для охладителя ЗКОС (11.2.2, еженедельно). В обоих случаях — **на чистку**.

---

**🇬🇧 Excessively High Bearing Temperature**

⚠️ **The essence is "heat generation exceeds heat dissipation"**, from four types of problem: **lubrication, load, cooling, and the equipment itself.**

**PHENOMENA**
Bearing oil return temperature and bush metal temperature exceed design allowable values, triggering the "high bearing temperature" alarm | Bearing housing vibration increases significantly; on site a **"rustling" friction sound** or **"hum"** is heard inside the bearing, in severe cases a **"metal impact sound"** | ⚠️ **Impurities or air bubbles are observed in the oil flow through the bearing oil return sight glass**; oil return volume decreases and oil level may drop rapidly | If the rise is caused by excessive axial thrust, it comes with a **significant increase in axial displacement**, which further intensifies bearing load

**CAUSES**
*Lubrication failure (most common)* — oil emulsifies, contains impurities such as **metal chips**, or viscosity decreases → **no stable oil film**; low tank level, pump failure, blocked supply pipeline, or **incorrect valve closure**; ⚠️ **jacking oil failure when speed is too low at start**, or bearing clearance **too large or too small** → **"semi-dry friction"**
*Abnormal bearing load* — steam parameter fluctuations (e.g. **sudden rise in main steam pressure**), **diaphragm scaling**, or **condenser vacuum drop** push axial thrust beyond bearing capacity; **shafting alignment deviation** after installation or maintenance
*Cooling failure* — oil cooler scaling and blockage, or **insufficient opening of the cooling water valve**; impurities in cooling water blocking heat exchange channels
*Bearing defects* — ⚠️ **wear and falling off of the babbitt metal layer**; **clearance exceeding design after long-term wear** so oil film thickness cannot be maintained

**HANDLING — "first control, then troubleshoot, finally repair"**
⚠️ **Immediately manually reduce turbine load** to reduce radial/axial force and frictional heat
⚠️ **If temperature continues to rise, decisively trigger emergency shutdown** to prevent babbitt melting or rotor **"shaft seizure"**
Check tank level and oil pressure — add **oil of the same model**, switch to the standby pump, check for pipeline blockage | Sample the bearing oil return for **emulsification or impurities**; if quality has deteriorated, **start the purification device immediately** or replace with new oil
⚠️ **Check the oil cooler cooling water inlet-to-outlet temperature difference. If the difference is too small (<5°C), clean the cooler or open the cooling water valve**
Monitor axial displacement — if over limit, check condenser vacuum and steam parameters and adjust to reduce thrust; if ineffective, shut down and check whether **diaphragm or steam seal is scaled** | After shutdown, **disassemble and inspect the bearing**
⚠️ **Restart with gradual load increase; only when all indicators return to normal can the unit go into normal operation**

⚠️ **The "<5°C" criterion appears twice:** for the lube oil cooler (10.4.3.3) and for the CCCWS cooler (11.2.2, weekly). Both mean **clean it**.

`#bearingtemp #babbitt #luboil #troubleshooting`

---
---

## POST 76 — O'q siljishi anomaliyasi

**🇺🇿 O'q siljishi — sabab va trip shartlari**

⚠️ **Mohiyati: "rotorning o'q kuchi muvozanatsizligi" yoki "upor podshipnik ko'tarish qobiliyatining pasayishi".**

**BELGILAR**
• Upor pad harorati **bir vaqtda ko'tariladi**
• Ortiqcha siljish aylanuvchi va harakatsiz qismlar orasida ishqalanish keltirib chiqarsa — ⚠️ **val zichlashi va diafragmada metall qirish tovushi** eshitiladi
• Bog'liq parametrlar tebranishi: **manfiy differensial kengayishning oshishi yoki musbatning kamayishi**, **kondensator vakuumining tushishi**, main/reheat bug' parametrlari tebranishi (**haroratning to'satdan tushishi, bosimning to'satdan ko'tarilishi**), yoki **yuklama keskin o'zgarganda siljishning oniy sakrashi**

**SABABLAR**

*1. Upor tizimining o'z nosozliklari (asosiy omil)*
• **Upor padlarning yeyilishi/kuyishi** — yomon moylash (**past yog' bosimi, yuqori yog' harorati, aralashmali buzilgan yog'**) yoki mahalliy ortiqcha yuklama → **babbit qatlamining tirnalishi va erishi** → ko'tarish qobiliyati yo'qoladi
• ⚠️ **Ortiqcha upor zazori** — montaj chetlanishi yoki uzoq ish yeyilishi tufayli **upor disk va upor padlar orasidagi loyihaviy zazor (odatda 0.2–0.4 mm)** ortadi → **normal o'q kuchida ham ortiqcha siljish**
• **Upor diskning deformatsiyasi/urishi** — material defekti yoki **sovuq bug'/suv zarbasi (termik shok)** → aylanishda **davriy o'q kuchi** hosil qiladi

*2. O'q kuchining g'ayritabiiy oshishi (tashqi omil)*
• ⚠️ **Main/reheat bug' haroratining to'satdan tushishi (masalan 50°C/min dan oshsa)** — bug' zichligi keskin ortadi → oqim yo'li qismlarining o'q kuchi oniy ko'tariladi. ⚠️ **Harorat to'yinish haroratidan past bo'lsa gidravlik zarba ham bo'ladi va o'q kuchini yanada kuchaytiradi**
• **Main bug' bosimining to'satdan ko'tarilishi yoki yuklamaning to'satdan oshishi** — har bosqichdagi bosim farqi ortadi, o'q kuchi mos ravishda ko'tariladi (ayniqsa **HP silindrning musbat kuchi**)
• ⚠️ **Yuklama tashlash** — HP silindr o'q kuchi keskin kamayadi, IP va LP silindrlar esa **exhaust bosimi oshgani (vakuum tushishi) sababli teskari kuch hosil qiladi** va rotorni suradi. **House load rejimida bug' kirishi juda kam bo'lsa, windage ishqalanishi ham g'ayritabiiy o'q kuchi berishi mumkin**
• **Oqim yo'li muammolari** — **kurak cho'kmasi (bug' sifati past)** profil o'zgartiradi; **ishqalanish (val zichlash zazori juda kichik)** — ishqalanishdan hosil bo'lgan yon kuch rotorni o'q bo'yicha suradi, ishqalanish issiqligi esa termik deformatsiya beradi
• ⚠️ **Kondensator vakuumining keskin tushishi** — exhaust bosimining oshishi IP va LP oxirgi bosqich kuraklaridagi bosim farqini kattalashtiradi, **teskari o'q kuchi ortadi** va rotor **HP tomonga** siljiydi

*3. O'lchov tizimining soxta alarmi*
• **Datchik nosozligi** — o'q siljish datchigi probining yeyilishi, **simlarning bo'shashishi**, yoki signal kabelidagi **elektromagnit halaqit** → o'lchangan qiymatda sakrash yoki tartibsiz o'sish, **haqiqiy rotor harakati yo'q**
• **Kalibrlash chetlanishi** — datchik o'rnatish pozitsiyasining siljishi, **preamplifier parametrlarining noto'g'ri sozlanishi**, yoki **davriy kalibrlash bajarilmasligi**

**HARAKAT**

*Alarm qiymatida:* ⚠️ **darhol yuklamani tushiring.** Bir vaqtda **upor pad harorati, tebranish va bug' parametrlarini** diqqat bilan kuzating — siljish barqarorlashayaptimi

*Trip qiymatida yoki kritik holatlarda* — ⚠️ **qo'lda trip va vakuum buzish** quyidagi hollarda:
☑ O'q siljishi **trip qiymatiga** yetdi
☑ **Upor pad harorati alarm qiymatidan oshdi**
☑ Birlikdan **metall ishqalanish shovqini** eshitiladi
☑ ⚠️ **O'q tebranishi 0.2 mm dan oshdi**

*To'xtatishdan keyin:* ⚠️ **upor pad harorati normaga tushguncha lube oil tizimini ishlatishda davom eting.** Turning gear ni ishga tushirganda **toki va rotor ekssentrisitetini kuzating.** ⚠️ **Turning gear qotib qolsa — MAJBURAN ishga tushirmang.**

*Sabab aniqlash — 3 qadam*
1. ⚠️ **Avval o'lchov tizimini istisno qiling** — datchikni standart o'lchov asboblari bilan kalibrlang (**prob zazori va ko'rsatilgan qiymatni tekshiring**), kabel ulanishi va yerga ulanishini tekshiring
2. **Upor tizimini tekshiring** — padlarni ochib ko'ring (**babbit yeyilganmi yoki eriganmi**), **upor zazorini o'lchang**, upor diskning **tekisligi va sirt tozaligini** tekshiring
3. **Tashqi omillarni aniqlang** — bug' parametrlarining tarixiy egri chizig'ini oling, kondensator vakuum tizimini tekshiring, ⚠️ **oqim yo'li qismlarini ENDOSKOP orqali kuzating (cho'kma, ishqalanish izlari)**, lube oil tizimini sinang

*Oldini olish*
• ⚠️ **Upor zazorini HAR YILI tekshiring va o'q siljish datchigini HAR YILI kalibrlang**
• Yog'ni muntazam almashtiring va filtrlarni tozalang
• ⚠️ **Operatorlar uchun o'q siljishi anomaliyasidagi avariya to'xtatish shartlarini ANIQ belgilang** — kechikkan operatsiyadan qochish uchun

⚠️ **0.2–0.4 mm upor zazori** — POST 59 dagi "rotor-stator zazori 0.1–0.5 mm" bilan bir xil masshtabda. Trip esa **0.889 mm**. Ya'ni trip nuqtasida upor zazori allaqachon ikki barobar oshgan bo'lishi mumkin.

⚠️ **"50°C/min" bu yerda, "15 daqiqada 83°C" trip jadvalida, "15 daqiqada 50°C" vakuum buzmasdan tripda.** Uchala raqam turli kontekstda — 10.6 dagi 50°C/min o'q kuchi uchun, boshqalari termik kuchlanish uchun.

---

**🇷🇺 Аномальный осевой сдвиг — причины и условия отключения**

⚠️ **Суть: «дисбаланс осевого усилия» или «снижение несущей способности упорного».**

**ПРИЗНАКИ** — одновременный рост температуры колодок | ⚠️ **металлический скребущий звук у уплотнений и диафрагм** | колебания связанных параметров: **рост отрицательного ОРС или снижение положительного**, **падение вакуума**, колебания параметров пара, **скачки сдвига при резком изменении нагрузки**

**ПРИЧИНЫ**
*Упорный узел* — **износ/выплавление колодок** от плохой смазки или локальной перегрузки; ⚠️ **увеличение зазора между упорным диском и колодками (проектно 0.2–0.4 мм)**; **деформация или биение диска** от дефекта материала или **теплового удара**
*Рост осевого усилия* — ⚠️ **падение температуры пара более 50°C/мин** → рост плотности → скачок усилия, **ниже температуры насыщения ещё и гидроудар**; **скачок давления или нагрузки**; ⚠️ **сброс нагрузки** — усилие ЦВД падает, ЦСД/ЦНД дают **обратное усилие из-за роста давления выхлопа**; **отложения на лопатках**, **задевание при малом зазоре уплотнений**; ⚠️ **резкое падение вакуума** сдвигает ротор **в сторону ЦВД**
*Ложный сигнал* — износ датчика, **ослабление проводки**, **электромагнитные помехи**; смещение установки, **неверная настройка предусилителя**, **непроведённая поверка**

**ДЕЙСТВИЯ**
*На сигнале* — ⚠️ **немедленно разгрузить**, следить за температурой колодок, вибрацией и параметрами пара
*На уставке защиты или в критической ситуации* — ⚠️ **ручное отключение со срывом вакуума** при: достижении уставки | **превышении температуры колодок** | **металлическом шуме** | ⚠️ **осевой вибрации выше 0.2 мм**
*После останова* — ⚠️ **маслосистема работает, пока температура колодок не придёт в норму**; следить за током ВПУ и эксцентриситетом; ⚠️ **при заклинивании ВПУ не пускать силой**

*Поиск причины* — ⚠️ **сначала исключить измерения** (поверка датчика, зазор проба, проводка и заземление) → **разобрать упорный узел**, измерить зазор, проверить диск → **исторические тренды пара, вакуум, ⚠️ ЭНДОСКОП проточной части, испытание маслосистемы**

*Профилактика* — ⚠️ **проверка упорного зазора ЕЖЕГОДНО и поверка датчика ЕЖЕГОДНО**; замена масла и чистка фильтров; ⚠️ **чётко закрепить за оперативным персоналом условия аварийного останова**

⚠️ **Зазор 0.2–0.4 мм** того же порядка, что и зазоры ротор-статор 0.1–0.5 мм, а защита — **0.889 мм**.
⚠️ **«50°C/мин» здесь, «83°C за 15 мин» в защитах, «50°C за 15 мин» при отключении без срыва вакуума** — три разных контекста.

---

**🇬🇧 Abnormal Axial Displacement**

⚠️ **The essence is "imbalance of rotor axial thrust" or "reduction in thrust bearing capacity".**

**PHENOMENA** — thrust pad temperature **rises simultaneously** | if excessive displacement causes rotor-stator friction, ⚠️ **metal scraping noise can be heard at the shaft seal and diaphragm** | associated fluctuations: **increase in negative differential expansion or decrease in positive**, **condenser vacuum drop**, main/reheat steam fluctuations (**sudden temperature drop, sudden pressure rise**), or **instantaneous displacement jumps when load changes abruptly**

**CAUSES**
*Thrust system itself (core inducing factor)* — **wear/burnout of thrust pads** from poor lubrication (**low oil pressure, high oil temperature, deteriorated oil with impurities**) or local overload, **scratching and melting the babbitt layer**; ⚠️ **excessive thrust clearance** — installation deviation or wear increases the designed clearance between thrust disc and pads (**usually 0.2–0.4 mm**), giving excessive displacement **even under normal thrust**; **deformation or runout of the thrust disc** from material defects or **cold steam/water impact (thermal shock)**, generating **periodic axial force**
*Abnormal increase in axial thrust* — ⚠️ **sudden drop in main/reheat steam temperature (e.g. exceeding 50°C/min)** sharply increases steam density and axial thrust; ⚠️ **if temperature falls below saturation, water hammer occurs and amplifies the axial force**; **sudden pressure rise or load increase** raises stage pressure differences (especially **HP cylinder positive thrust**); ⚠️ **load rejection** — HP thrust drops sharply while IP and LP generate **reverse thrust from increased exhaust pressure (vacuum drop)**, and on house load **windage friction** can cause abnormal axial force; **flow passage problems** — **blade fouling from poor steam quality**, and **rotor-stator friction from too-small seal clearance** whose lateral force shifts the rotor axially while frictional heat deforms it; ⚠️ **sharp vacuum drop** enlarges the pressure difference across IP and LP last-stage blades, increasing **reverse axial thrust** and moving the rotor **toward the HP end**
*False alarm* — sensor probe wear, **loose wiring**, or **electromagnetic interference** giving jumps with **no actual rotor movement**; installation offset, **incorrect preamplifier parameter setting**, or **no periodic calibration**

**HANDLING**
*At the alarm value* — ⚠️ **immediately reduce load**, closely monitoring thrust pad temperature, vibration and steam parameters to see whether displacement stabilizes
*At the trip value or in critical situations* — ⚠️ **manually trip the unit and break the vacuum** when: displacement reaches the trip value | **thrust pad temperature exceeds alarm** | **metal friction noise is heard** | ⚠️ **axial vibration exceeds 0.2 mm**
*After shutdown* — ⚠️ **keep the lube oil system running until thrust pad temperature drops to normal**; monitor turning gear current and rotor eccentricity; ⚠️ **if the turning gear jams, do not force start it**

*Cause identification* — ⚠️ **Step 1: eliminate measurement issues** (calibrate with standard tools, verify probe gap and displayed value, check cable wiring and grounding) → **Step 2: inspect the thrust system** (pads for wear or melting, measure thrust clearance, check disc flatness and finish) → **Step 3: identify external factors** (steam parameter history, vacuum system, ⚠️ **observe flow passage components through an ENDOSCOPE** for fouling and friction marks, test the lube oil system)

*Prevention* — ⚠️ **inspect thrust clearance every year and calibrate the axial displacement sensor annually**; replace lube oil and clean filters regularly; ⚠️ **clarify the emergency shutdown conditions for abnormal axial displacement** so operators do not delay

⚠️ **The 0.2–0.4 mm thrust clearance** is the same order as the 0.1–0.5 mm rotor-stator clearances, while the trip is **0.889 mm**.
⚠️ **"50°C/min" here, "83°C in 15 min" in the trip table, "50°C in 15 min" for trip without vacuum breaking** — three different contexts.

`#axialdisplacement #thrustbearing #troubleshooting`

---
---

## POST 77 — Kunlik TO me'yorlari

**🇺🇿 Nasoslar — kunlik tekshiruv raqamlari**

⚠️ **Chastota: kuniga 3 martadan kam emas, smena qabulida majburiy.**

**CCCWS nasosi (11.2.1)**
| Nima tekshiriladi | Me'yor | Usul |
|---|---|---|
| Ish tovushi | **G'ayritabiiy shovqin yo'q** | Tinglash |
| Tebranish | ⚠️ **Ikki amplituda ≤4.5 mm/s** | Tebranish o'lchagich |
| Podshipnik harorati | ⚠️ **≤70°C** | Nuqtaviy termometr |
| Mexanik zichlash | ⚠️ **Tomchilamaydi (≤3 TOMCHI/DAQIQA)** | Ko'rish |
| O'ram harorati | — | — |

**CCWS (11.3.1)**
| Nima | Me'yor |
|---|---|
| Nasos chiqish bosimi | ⚠️ **0.2–0.35 MPa** |
| Kollektor bosimi | ⚠️ **≥0.2 MPa** |
| Val vtulkasi | ⚠️ **Salnik zichlashida suv sizishi: salnik siqish gaykasining tarangligini sozlab boshqariladi. Talab — salnikdan OZ MIQDORDA SUV UZLUKSIZ chiqib turishi** |
| Dvigatel va podshipnik moylash suvi | Sarf ko'rsatkichi to'g'ri, sarf normal |
| Dvigatel holati | Ish toki, chiqish |

**ACCWS (11.1.1)**
| Nima | Me'yor |
|---|---|
| Nasos chiqish bosimi | ⚠️ **0.25–0.35 MPa** |
| Kollektor bosimi | ⚠️ **≥0.2 MPa** |
| Elektr filtr Δp | ⚠️ **≤60 kPa** |
| Purge klapan | **Sizishsiz zich yopiq** |

**HAFTALIK MAXSUS TO (11.2.2)**
• **Zaxira nasos holati** — zaxira nasos chiqish klapanining to'liq ochiq holati, dvigatel izolyatsiyasi
• ⚠️ **Sovutgich samaradorligi** — sovutgich kirish-chiqish harorat farqini qayd eting; **farq <5°C bo'lsa qayd eting va tozalashni rejalashtiring**
• ⚠️ **Asbob va interlok kalibrlash** — bosim va harorat asboblari ko'rsatkichlarining DCS bilan mosligini tekshiring; **past bosim interlokini sinang (kollektor bosimi ≤0.6 MPa bo'lganda zaxira nasos avtomatik ishga tushishi)** — ishonchli ishlashini ta'minlash uchun
• Quvur tayanchlari

⚠️ **"3 tomchi/daqiqa" va "oz miqdorda suv uzluksiz"** — bir-biriga zid ko'rinadi, lekin bular **turli zichlash turlari**: CCCWS da **mexanik zichlash** (tomchilamasligi kerak), CCWS da **salnik** (oz-oz sizishi SHART, aks holda salnik quriydi va val vtulkasi yeyiladi).

⚠️ **Nasos chiqish bosimlari:** ACCWS **0.25–0.35 MPa**, CCWS **0.2–0.35 MPa**, CCCWS zaxira interloki **0.6 MPa**. Ishga tushirishda esa CCW **2.0–2.7 bar = 0.20–0.27 MPa**. Barchasi bir-biriga yaqin, lekin har xil.

⚠️ **Tebranish me'yorlari uch xil:** CCCWS nasos TO da **4.5 mm/s**, 6-bobdagi alarm **4.5 mm/s** va trip **7.1 mm/s**, kondensat nasosining yuqori podshipnigi **7.1/11.0 mm/s**, ST journal podshipniklari **165/240 μm**. Birliklar ham boshqa (mm/s va μm).

---

**🇷🇺 Насосы — цифры ежедневного контроля**

⚠️ **Не менее 3 раз в сутки, обязательно при приёмке смены.**

**Насос ЗКОС** — шум **без отклонений** | ⚠️ **вибрация (размах) ≤4.5 мм/с** | ⚠️ **подшипник ≤70°C** | ⚠️ **механическое уплотнение без капели (≤3 КАПЛИ/МИН)**
**ЦОС** — ⚠️ **нагнетание 0.2–0.35 МПа**, **коллектор ≥0.2 МПа** | ⚠️ **сальник: регулируется затяжкой гайки, требуется НЕБОЛЬШОЕ НЕПРЕРЫВНОЕ поступление воды** | расход охлаждения и смазки | ток и выход двигателя
**ВЦОС** — ⚠️ **нагнетание 0.25–0.35 МПа**, **коллектор ≥0.2 МПа**, **Δp электрофильтра ≤60 кПа**, продувочный **плотно закрыт**

**ЕЖЕНЕДЕЛЬНО** — состояние резервного насоса (полное открытие задвижки, изоляция) | ⚠️ **перепад на охладителе: <5°C — записать и планировать чистку** | ⚠️ **сверка приборов с DCS и испытание блокировки: автопуск резервного при давлении коллектора ≤0.6 МПа** | опоры трубопроводов

⚠️ **«3 капли/мин» и «непрерывное поступление воды»** — не противоречие: в ЗКОС **механическое уплотнение** (капать не должно), в ЦОС **сальник** (обязан слегка подтекать, иначе высохнет и износит втулку).
⚠️ **Давления разные:** ВЦОС **0.25–0.35**, ЦОС **0.2–0.35**, блокировка ЗКОС **0.6 МПа**, при пуске ЦОС **2.0–2.7 бар**.
⚠️ **Нормы вибрации трёх видов:** насосы **4.5 / 7.1 мм/с**, верхний подшипник КЭН **7.1 / 11.0 мм/с**, опоры ПТ **165 / 240 мкм**.

---

**🇬🇧 Pump Routine Inspection — the numbers**

⚠️ **No less than 3 times a day, mandatory during shift handover.**

**Closed cooling water pump (11.2.1)**
Operation sound — **no abnormal noise** | ⚠️ **vibration double amplitude ≤4.5 mm/s** | ⚠️ **bearing temperature ≤70°C** | ⚠️ **mechanical seal no dripping (≤3 DROPS/MINUTE)** | winding temperature
Method: sound listening, vibration meter, spot thermometer, visual inspection

**CCWS (11.3.1)**
⚠️ **Pump outlet pressure 0.2–0.35 MPa; header pressure ≥0.2 MPa** | ⚠️ **Shaft sleeve: observe whether leakage at the packing seal is excessive; control by adjusting the tightness of the packing gland nut, subject to having A SMALL AMOUNT OF WATER CONTINUOUSLY EMERGE from the stuffing** | motor and bearing lubrication water flow correct | motor current and output

**ACCWS (11.1.1)**
⚠️ **Pump outlet 0.25–0.35 MPa; header ≥0.2 MPa** | ⚠️ **Electric filter Δp ≤60 kPa; blow down valve closed tightly without leakage**

**WEEKLY SPECIAL MAINTENANCE (11.2.2)**
Standby pump — full open status of the outlet valve, motor insulation | ⚠️ **Cooler performance — record cooler inlet-to-outlet temperature difference; if the difference <5°C, record and plan for cleaning** | ⚠️ **Instrument and interlock calibration — verify pressure and temperature indications against DCS; test the low-pressure interlock (standby pump automatically starts when header pressure ≤0.6 MPa) to ensure reliable action** | pipeline supports

⚠️ **"3 drops/minute" and "a small amount of water continuously"** are not contradictory — different seal types: CCCWS uses a **mechanical seal** (must not drip), CCWS uses **packing** (must weep slightly, or it runs dry and wears the shaft sleeve).
⚠️ **Discharge pressures:** ACCWS **0.25–0.35 MPa**, CCWS **0.2–0.35 MPa**, CCCWS standby interlock **0.6 MPa**, CCW at start-up **2.0–2.7 bar**.
⚠️ **Three sets of vibration limits:** pumps **4.5 / 7.1 mm/s**, condensate pump upper bearing **7.1 / 11.0 mm/s**, ST journal bearings **165 / 240 μm** — different units too.

`#maintenance #pumps #dailycheck #vibration`

---
---

## POST 78 — CCWS nasos va gradirnya spetsifikatsiyasi

**🇺🇿 Aylanma suv nasosi va gradirnya — to'liq ma'lumot**

**CCW nasos — 00PAC21AP001/2**
| Parametr | Qiymat |
|---|---|
| Turi | **44LKSA-31** |
| **Sarf** | **10.6 m³/sek = 37 440 m³/soat** |
| Napor | **27.1 m** |
| **Tezlik** | **370 rpm** |
| **NPSHr** | **8.41 m** |
| FIK | **88.4%** |
| ⚠️ **Minimal cho'kish chuqurligi** | **4.8 m** |
| Val quvvati | **3127.7 kW** |
| Nominal quvvat | **3600 kW** |
| Aylanish yo'nalishi | Tepadan pastga qaraganda **soat yo'nalishi** |
| Dvigatel | **YLKS3600-16** |
| **Nominal tok / kuchlanish** | **42 A / 11 kV** |
| Dvigatel sovutish | Havo-suv |

**Nasos tuzilishi (12 qism)**
1. **So'rish karnayi** — suyuqlikni so'rish havzasidan ish g'ildiragiga **bir tekis va barqaror** yo'naltiradi; so'rish samaradorligini oshirish uchun **oldindan burash parragi** bilan jihozlangan
2. Ish g'ildiragi kamerasi · 3. Ish g'ildiragi · 4. Diffuzor korpusi · 5. Tashqi va egri quvur
6. Yo'naltiruvchi parrak va quvur · 7. Asosiy val (yuqori va pastki, **mufta bilan ulangan**)
8. Dvigatel tayanchi (**ikkita lyuk** ta'mir uchun) · 9. Tayanch asos
10. **Salnik zichlash uzeli** — ⚠️ **salnik tashqaridan yuvish suviga ulanishi SHART**
11. Mufta · 12. Moylash va sovutish suvi tizimi

⚠️ **Moylash va sovutish suvi tizimi:** nasos salnigini yuvish suvi, podshipnik moylash suvi va dvigatel sovutish suvi. Manba — **tashqi toza xizmat suvi** yoki nasos chiqishidan filtrlangan toza suv. ⚠️ **Aylanma suv nasosini ishga tushirishdan oldin nasos normal ishlab ketguncha xizmat suvi bilan moylanishi SHART, faqat shundan keyin tashqi xizmat suvini o'chirish mumkin.**
Nasos moylash suvi har bir yo'naltiruvchi podshipnikdan o'tib **pastki podshipnikdan chiqariladi**. Dvigatel sovutish suvi **ikki yo'lga** bo'linadi: biri upor podshipnik sovutish kamerasiga, biri dvigatel sovutgichiga.

**Gradirnya — loyihaviy sharoit**
| Parametr | Qiymat |
|---|---|
| KKS | 00PBT10...19AC001, 00PBT20...29AC001 |
| **Har bir yacheyka sarfi** | **4362 m³/soat** |
| **Yacheykalar soni** | **20** |
| Suv kirish harorati | **24.77°C** |
| Suv chiqish harorati | **17.77°C** |
| Loyihaviy quruq termometr | **15.6°C** |
| ⚠️ **Loyihaviy ho'l termometr** | **11.33°C** |
| Barometrik bosim | **97.7 kPa** |

**Gradirnya konstruksiyasi**
Turi **qarshi oqimli RC**, modeli **NCR-L0H0A415-FB8**, yacheyka **20 m × 17 m**, havo kirish balandligi **7 m**, suv kirish balandligi **10.4 m**, yacheyka balandligi **15.2 m**, joylashuvi **orqama-orqa**, havo kirishi **bir tomondan**, bosim yo'qotishi **128.9 Pa**, nisbiy namlik **60.73%**, havo zichligi **1.173 kg/m³**, **suv yuklamasi 12.83 m³/(m²·soat)**, **havo/suv nisbati 0.878**, to'ldirgichda tezlik **2.73 m/s**

**Ventilyator**
Diametri **10 360 mm**, kurak materiali **FRP**, **har bir ventilyator havo sarfi 3 409 000 m³/soat**, statik bosim **118.1 Pa**, to'liq bosim **190.1 Pa**, val materiali **uglerod tolasi**
Dvigatel: **bir tezlikli**, **11 kV, 50 Hz, 3 faza**, **250 kW**, **1480 rpm**, izolyatsiya **F**, **IP55**, samaradorlik **IE3**

**To'ldirgich va tomchi tutgich**
To'ldirgich: **plyonkali**, model **IC-C**, material **PVC**
Tomchi tutgich: **plastinali**, model **SJ-120**, **PVC**, ⚠️ **tomchi yo'qotishi 0.001%**
Suv taqsimlash: kollektor **quvurli**, yon quvurlar **UPVC**, forsunka **IN-A2**, **ABS**

**Gidravlik butterfly klapan**
Nominal bosim **0.6 MPa**, muhit **konsentrlangan daryo suvi**, ish harorati **≤80°C**, ish bosimi **0.27 MPa**

**Boshqaruv strategiyasi**
⚠️ **Zaxira CCWS nasos umumiy kollektor bosimi 2.0 bar ga tushganda YOKI ishlayotgan nasos trip bo'lganda avtomatik ishga tushadi**
So'rish havzasida **uchta sath transmitteri** har bir nasos uchun — ishga tushirish shartlarini sozlash va ⚠️ **sath minimal cho'kish chuqurligidan past bo'lganda nasosni interlok bilan trip qilish** uchun

⚠️ **Minimal cho'kish chuqurligi: CCW 4.8 m, ACCW 3.6 m.** Ikkalasi **umumiy havzani bo'lishadi**, o'rtada devor bilan ajratilgan va tagida ulangan. Ya'ni bitta havza sathining tushishi ikkala nasosga ta'sir qiladi, lekin chegaralar boshqa.

⚠️ **Kimyoviy dozalash QO'LDA to'ldiriladi** — CCWS nasos so'rish havzasiga **gipoxlorit (NaClO)** va **cho'kmaga qarshi ingibitor** quyiladi. NaClO — dezinfeksiya va suv o'tiga qarshi; ingibitor — kalsiy karbonat va sulfat cho'kmasiga qarshi.

---

**🇷🇺 Циркуляционный насос и градирня — полные данные**

**Насос 00PAC21AP001/2** — **44LKSA-31** | **10.6 м³/с = 37 440 м³/ч** | напор **27.1 м** | **370 об/мин** | **NPSHr 8.41 м** | КПД **88.4%** | ⚠️ **минимальное погружение 4.8 м** | вал **3127.7 кВт** | номинал **3600 кВт** | **по часовой сверху вниз** | двигатель **YLKS3600-16**, **42 А / 11 кВ**, воздушно-водяное охлаждение

**Конструкция (12 узлов)** — всасывающий раструб с **предзакруткой** | камера и рабочее колесо | диффузор | наружные и отводные трубы | направляющий аппарат | верхний и нижний валы через **муфту** | опора двигателя с **двумя люками** | опорное основание | ⚠️ **сальниковый узел с ОБЯЗАТЕЛЬНОЙ внешней промывкой** | муфта | система смазки и охлаждения

⚠️ **Источник — внешняя чистая служебная вода** или фильтрат с нагнетания. ⚠️ **До выхода насоса на режим смазка ведётся служебной водой, только затем её отключают.** Смазка сливается через **нижний подшипник**; охлаждение двигателя — **двумя путями**: камера упорного и маслоохладитель двигателя.

**Градирня** — **20 секций**, **4362 м³/ч на секцию**, **24.77 → 17.77°C**, сухой термометр **15.6°C**, ⚠️ **мокрый 11.33°C**, **97.7 кПа**
Противоточная **NCR-L0H0A415-FB8**, секция **20×17 м**, вход воздуха **7 м**, вход воды **10.4 м**, высота **15.2 м**, **спина к спине**, потери **128.9 Па**, влажность **60.73%**, плотность воздуха **1.173 кг/м³**, **плотность орошения 12.83 м³/(м²·ч)**, **воздух/вода 0.878**, скорость в оросителе **2.73 м/с**
**Вентилятор** Ø**10 360 мм**, **FRP**, **3 409 000 м³/ч**, статика **118.1 Па**, полное **190.1 Па**, вал **углеволокно**; двигатель **250 кВт**, **11 кВ**, **1480 об/мин**, **F**, **IP55**, **IE3**
Ороситель плёночный **IC-C**, **PVC** | Каплеуловитель **SJ-120**, **PVC**, ⚠️ **унос 0.001%** | Распределение: **UPVC**, форсунки **IN-A2**, **ABS**
**Гидрозаслонка** — номинал **0.6 МПа**, среда **концентрированная речная вода**, **≤80°C**, рабочее **0.27 МПа**

⚠️ **Автопуск резервного при давлении коллектора 2.0 бар или отключении рабочего.** Три уровнемера в колодце на насос; ⚠️ **при уровне ниже минимального погружения — блокировочное отключение**
⚠️ **Минимальное погружение: ЦОС 4.8 м, ВЦОС 3.6 м.** Колодец **общий**, разделён стенкой и связан по низу.
⚠️ **Дозирование РУЧНОЕ** — **гипохлорит (NaClO)** и **ингибитор отложений** в приёмный колодец.

---

**🇬🇧 CCW Pump and Cooling Tower — full specification**

**CCW pump 00PAC21AP001/2**
Type **44LKSA-31** | **Flow 10.6 m³/s = 37,440 m³/h** | Head **27.1 m** | **Speed 370 rpm** | **NPSHr 8.41 m** | Efficiency **88.4%** | ⚠️ **Minimum submerged depth 4.8 m** | Shaft power **3127.7 kW** | Rated **3600 kW** | Rotation **clockwise from top to bottom** | Motor **YLKS3600-16**, **42 A / 11 kV**, air-water cooled

**Pump construction (12 components)**
Suction trumpet mouth — guides liquid **evenly and steadily** into the impeller, fitted with a **pre-swirl vane** to improve suction efficiency | impeller chamber | impeller | diffuser case | external and curved pipe | guide vane and pipe | main shaft (upper and lower via **sleeve coupling**) | motor support (**two manholes** for maintenance) | support base | ⚠️ **packing sealing component — the packing MUST be externally connected to water flushing** | sleeve coupling | lubrication and cooling water system

⚠️ **Water source is external clean service water** or filtered clean water from the pump outlet. ⚠️ **Before starting the circulating water pump it must be lubricated with service water until the pump is running normally, and only then can the external service water be turned off.** Lubrication water discharges from the **lower bearing** after passing each guide bearing. Motor cooling water splits into **two paths**: thrust bearing cooling chamber and motor cooler. A flow alarm switch sounds when flow is below the specified value.

**Cooling tower — design condition**
**20 cells**, **4362 m³/h per cell**, water **24.77 → 17.77°C**, design dry bulb **15.6°C**, ⚠️ **design wet bulb 11.33°C**, barometric **97.7 kPa**
Counter flow RC structure **NCR-L0H0A415-FB8**, cell **20 m × 17 m**, air inlet height **7 m**, water inlet height **10.4 m**, deck height **15.2 m**, **back-to-back**, air inlet **one side**, pressure loss **128.9 Pa**, relative humidity **60.73%**, air density **1.173 kg/m³**, **water loading 12.83 m³/(m²·h)**, **air-to-water ratio 0.878**, fill velocity **2.73 m/s**, fill mass velocity **3.18 kg/(m²·s)**

**Fan** — diameter **10,360 mm**, blade **FRP**, **air flow per fan 3,409,000 m³/h**, static **118.1 Pa**, total **190.1 Pa**, shaft **carbon fibre**
**Fan motor** — single speed, **11 kV, 50 Hz, 3-phase**, **250 kW**, **1480 rpm**, insulation **F**, **IP55**, **IEC60034 IE3**

**Fill** film type **IC-C**, **PVC** | **Drift eliminators** blade type **SJ-120**, **PVC**, ⚠️ **drift loss 0.001%** | **Water distribution** piping type, laterals **UPVC**, nozzle **IN-A2**, **ABS**
**Hydraulic butterfly valve** — nominal **0.6 MPa**, media **concentrated river water**, operating temp **≤80°C**, working pressure **0.27 MPa**

**Control strategy**
⚠️ **The redundant CCWS pump auto-starts when common header pressure drops to 2.0 bar, or when the operating pump trips**
Three level transmitters per pump in the suction pool for start condition adjustment and ⚠️ **interlock trip when pool level is lower than the minimum submergence depth**

⚠️ **Minimum submergence: CCW 4.8 m, ACCW 3.6 m.** Both **share a common water pool**, separated by a partition wall and connected at the bottom. One pool level affects both pumps, but with different limits.
⚠️ **Chemical dosing is manually filled** — **hypochlorite (NaClO)** and **scale inhibitor** injected to the CCWS pump suction pool. NaClO for disinfection and algae control; inhibitor against calcium carbonate and sulfate scale.

`#CCWS #coolingtower #pumpspec #dosing`

---
---

## POST 79 — Kondensat tizimi: uskuna va iste'molchilar

**🇺🇿 Kondensat — 14 ta iste'molchi va spetsifikatsiya**

**Kondensat suvi iste'molchilari (Table 3-4-1)**
| № | Iste'molchi |
|---|---|
| 1 | **6 m³ drenaj flash bakiga** desuperheating suvi |
| 2 | **Yordamchi bug' tizimiga** desuperheating suvi |
| 3 | **10 m³ drenaj flash bakiga** desuperheating suvi |
| 4 | **Gland steam** desuperheating suvi |
| 5 | **Kondensator purkash suvi** |
| 6 | **#11 IP bypass klapani** desuperheating suvi |
| 7 | **#12 IP bypass klapani** desuperheating suvi |
| 8 | **#11 LP bypass klapani** desuperheating suvi |
| 9 | **#12 LP bypass klapani** desuperheating suvi |
| 10 | **Vakuum buzish klapani zichlash suvi** |
| 11 | **Vakuum flash baki** desuperheating suvi |
| 12 | **LP silindr purkash suvi** |
| 13 | **11 HRSG LP barabani** |
| 14 | **12 HRSG LP barabani** |

**Kondensat nasos — 10LCB11/12AP001**
| Parametr | Qiymat |
|---|---|
| Turi | **Vertikal ko'p bosqichli bochka tipidagi** |
| Model | **C720-III-N** |
| **Tezlik** | **1490 rpm** |
| **Napor** | **225 m** |
| **Sarf** | **2103 m³/soat** |
| FIK | **82.5%** |
| ⚠️ **NPSHr** | **3.6 m** |
| Yo'nalish | Dvigateldan nasosga qaraganda **soat yo'nalishiga teskari** |

**Dvigatel — YLK-560-4**
**1800 kW** | **11 kV / 110 A** | **1487 rpm** | FIK **95%** | cos φ **0.86** | **IP55** | **Sovutish suvi 24 m³/soat**

**Kirish filtri — 10LCA11/12AA401**
Loyihaviy bosim **1.0 MPa** | Ish bosimi **0.6 MPa** | ⚠️ **Filtrlash aniqligi 425 μm** | **Δp <10 kPa**

**Gland steam kondensatori — 10MAW60AC001**
Quvurli issiqlik almashgich, **yuza 67 m²**
• **Korpus tomoni:** loyihaviy **0.35 & F.V bar.g**, loyihaviy harorat **300°C**, ish bosimi **0.05 barg vakuum**, ish harorati **185/65°C**, gidrosinov **1.0 bar.g**, hajm **0.73 m³**
• **Quvur tomoni:** loyihaviy **45 bar.g**, loyihaviy harorat **95°C**, ish bosimi **40 bar.a**, ish harorati **35/41.8°C**, gidrosinov **67.5 bar.g**, hajm **0.23 m³**

**Boshqaruv strategiyasi**
⚠️ **Zaxira kondensat nasos umumiy kollektor bosimi 15 bar ga tushganda YOKI ishlayotgan nasos trip bo'lganda avtomatik ishga tushadi**

⚠️ **Normal ishda kondensat nasos ish diapazoni: 525–2200 t/soat** (nominal tezlikda, ish egri chizig'iga ko'ra)
⚠️ **Nominal sharoitda normal sarf ~1482 t/soat**
⚠️ **IP va LP bypass desuperheating ishda bo'lganda 2103 t/soat**

**Minimal sarf klapani (10LCA30AA101)**
⚠️ **Suv sarfi minimal talabdan past bo'lganda KAVITATSIYANING oldini olish uchun** min-flow klapanini boshqarish muhim. Retsirkulyatsiya liniyasidagi pnevmatik klapan sarfni normal diapazonda ushlab turadi.

**Kondensator make-up klapani (10LCR10AA101/102)**
⚠️ **Uchta sath transmitteri hot well sathini uzluksiz kuzatadi.** Sath belgilangan qiymatdan chetlashsa, make-up klapan sathni belgilangan qiymatga yaqin ushlash uchun sozlanadi. Sath transmitterlari: **10MAG01CL101/2/3**

⚠️ **NPSHr atigi 3.6 m** — kondensat nasos vakuumdan so'radi, shuning uchun hot well sathi juda muhim. POST 13 dagi trip **1340 mm** — bu NPSH zaxirasini saqlash uchun.

⚠️ **Filtr 425 μm** — bu CCCWS kirish filtridan (**4 mm = 4000 μm**) **~10 barobar** nozikroq, va EH filtridan (**3 μm**) 140 barobar qo'polroq. Har bir tizimda o'z aniqligi bor.

---

**🇷🇺 Конденсатная система — 14 потребителей и спецификация**

**Потребители** — впрыск в дренажные расширители **6 м³** и **10 м³** | впрыск во **вспомогательный пар** | впрыск в **уплотняющий пар** | **впрыск в конденсатор** | впрыск в **БРОУ СД №11 и №12** | впрыск в **БРОУ НД №11 и №12** | **запирающая вода клапана срыва вакуума** | впрыск в **вакуумный расширитель** | **впрыск в ЦНД** | **барабаны НД КУ №11 и №12**

**Насос 10LCB11/12AP001** — вертикальный многоступенчатый бочкового типа **C720-III-N** | **1490 об/мин** | напор **225 м** | **2103 м³/ч** | КПД **82.5%** | ⚠️ **NPSHr 3.6 м** | **против часовой от двигателя к насосу**
**Двигатель YLK-560-4** — **1800 кВт**, **11 кВ / 110 А**, **1487 об/мин**, КПД **95%**, cos φ **0.86**, **IP55**, охлаждение **24 м³/ч**
**Фильтр на всасе** — **1.0 МПа** расчёт, **0.6 МПа** рабочее, ⚠️ **тонкость 425 мкм**, **Δp <10 кПа**
**СП 10MAW60AC001** — **67 м²**; корпус: **0.35 бар.g**, **300°C**, **0.05 барг вакуум**, **185/65°C**, гидро **1.0 бар.g**, **0.73 м³**; трубки: **45 бар.g**, **95°C**, **40 бар.а**, **35/41.8°C**, гидро **67.5 бар.g**, **0.23 м³**

⚠️ **Автопуск резервного при давлении коллектора 15 бар или отключении рабочего**
⚠️ **Рабочий диапазон 525–2200 т/ч**, ⚠️ **норма ~1482 т/ч**, ⚠️ **2103 т/ч при работе впрысков БРОУ СД и НД**
**Клапан минимального расхода 10LCA30AA101** — ⚠️ **против КАВИТАЦИИ при расходе ниже минимального**
**Подпитка 10LCR10AA101/102** — три уровнемера **10MAG01CL101/2/3** держат уровень у уставки

⚠️ **NPSHr всего 3.6 м** — насос берёт из вакуума, уровень в конденсатосборнике критичен. Защита **1340 мм** существует ради запаса NPSH.
⚠️ **425 мкм** — в ~10 раз тоньше фильтра ЗКОС (**4 мм**) и в 140 раз грубее фильтра ОГ (**3 мкм**).

---

**🇬🇧 Condensate System — 14 users and specification**

**Condensate water users (Table 3-4-1)**
De-superheating water to the **6 m³ drain flash tank**, **auxiliary steam system**, **10 m³ drain flash tank**, **gland steam** | **condenser spray water** | de-superheating to **#11 and #12 IP bypass valves** | de-superheating to **#11 and #12 LP bypass valves** | **vacuum break valve sealing water** | **vacuum flash tank** de-superheating | **LP cylinder spray water** | **11 HRSG LP drum** | **12 HRSG LP drum**

**Condensate pump 10LCB11/12AP001**
Vertical multistage barrel-type **C720-III-N** | **1490 rpm** | Head **225 m** | **2103 m³/h** | Efficiency **82.5%** | ⚠️ **NPSHr 3.6 m** | **Counter clockwise from motor to pump**
**Motor YLK-560-4** — **1800 kW**, **11 kV / 110 A**, **1487 rpm**, efficiency **95%**, PF **0.86**, **IP55**, cooling water **24 m³/h**
**Inlet filter 10LCA11/12AA401** — design **1.0 MPa**, operating **0.6 MPa**, ⚠️ **filter precision 425 μm**, **Δp <10 kPa**
**Gland steam condenser 10MAW60AC001** — tube heat exchanger, **surface 67 m²**; shell side design **0.35 & F.V bar.g**, **300°C**, operating **0.05 barg vacuum**, **185/65°C**, hydro **1.0 bar.g**, volume **0.73 m³**; tube side design **45 bar.g**, **95°C**, operating **40 bar.a**, **35/41.8°C**, hydro **67.5 bar.g**, volume **0.23 m³**

**Control strategy**
⚠️ **The redundant condensate pump auto-starts when common header pressure drops to 15 bar, or when the operating pump trips**
⚠️ **During normal operation the pump operates in the range 525 to 2200 t/h** at rated speed per the performance curve
⚠️ **Normal flow at rated speed is about 1482 t/h**, and ⚠️ **2103 t/h with IP and LP bypass de-superheating in service**
**Minimum flow valve 10LCA30AA101** — ⚠️ **prevents CAVITATION when flow is below the minimum required**
**Make-up valves 10LCR10AA101/102** — three level transmitters **10MAG01CL101/2/3** hold hot well level near setpoint

⚠️ **NPSHr is only 3.6 m** — the pump draws from vacuum, so hot well level is critical. The **1340 mm** trip exists to protect that NPSH margin.
⚠️ **425 μm** is about ten times finer than the CCCWS inlet filter (**4 mm**) and 140 times coarser than the EH filter (**3 μm**). Each system has its own precision.

`#condensate #CEP #NPSH #filters`

---
---

## POST 80 — Sponge shar: o'lcham va tur

**🇺🇿 Rezina shar — o'lcham qoidasi**

⚠️ **ENG MUHIM QOIDA: HO'L sponge sharning diametri sovutish quvurining ICHKI diametridan 1–2 mm KATTA bo'lishi SHART.**

**Shar talablari**
• **Eskirishga chidamli, yumshoq va elastik**
• ⚠️ **Sponge sharning havo teshiklari iloji boricha BIR TEKIS bo'lishi kerak**
• ⚠️ **Ho'l sharning solishtirma og'irligi suvnikiga YAQIN bo'lishi kerak**

**Ikki turi**
| Turi | Vazifasi |
|---|---|
| **Oddiy sponge shar** | Cho'kmani olib tashlash |
| ⚠️ **Korund qoplamali sponge shar** | **QATTIQ cho'kmani** quvur devoridan olib tashlash |

**Spetsifikatsiya**
• **Quruq diametri: 27.5 mm va 27 mm**
• **Qattiqlik: yumshoq**

**Hisob-kitob**
Kondensator quvuri: **tashqi Ø 28.575 mm**, devor **0.5 mm** yoki **0.7 mm**
→ **Ichki diametr: 27.575 mm** (0.5 mm devor) va **27.175 mm** (0.7 mm devor)
→ ⚠️ **Kerakli ho'l shar diametri: 28.6–29.6 mm (0.5 mm) va 28.2–29.2 mm (0.7 mm)**
→ **Quruq shar 27.5/27 mm** → ho'llanganda **~1 mm kengayishi kerak**

⚠️ **Shuning uchun 24 soatlik ho'llash MAJBURIY.** Quruq shar (27.5 mm) quvur ichki diametridan (27.575 mm) **kichikroq** — ya'ni quvurdan erkin o'tib ketadi va **hech narsa tozalamaydi**. Faqat to'liq ho'llangandan keyin u kerakli 1–2 mm ortiqchalikni beradi.

⚠️ **Ikki xil quruq o'lcham (27.5 va 27 mm) ikki xil devor qalinligi uchun.** Aralashtirib yuborilsa bir qismi samarasiz bo'ladi. 0.7 mm devorli quvurlar atigi **1454 ta** (jami 27 908 dan), ya'ni **5%**.

**Shar nasosi — 10PAH01/02AP001**
Turi **125JQ-27** | **Sarf 108 m³/soat = 30 l/s** | Napor **27 m** | **1460 rpm** | **NPSHr 7 m** | FIK **65%** | Val quvvati **13.5 kW**
Dvigatel **1LE0003-1EB23-4AA4**, **18.5 kW**

**Shar to'ri**
⚠️ **Normal Δp: <3 kPa** (alarm **>70 mbar = 7 kPa**)
Korpus va kirish/chiqish materiali **A36 korroziyaga qarshi** | To'r va yetakchi val **316L**

**Shar yig'gich tuzilishi**
Korpus, **o'tkazgich klapan**, to'r, qo'l teshigi, shar chiqarish soplosi, drenaj, vent, qopqoq va **qaytmas qopqoq**.
• Sharlar aylanayotganda **o'tkazgich klapan ochiq** — sharlar erkin o'tadi
• Sharlarni yig'ish vaqtida klapan **yig'ish pozitsiyasiga** o'tkaziladi, sharlar klapan ichi bilan to'siladi. Suv klapandagi **ikkita to'xtovsiz teshik** va to'r teshigidan chiqadi, sharlar yig'gichda qoladi
• ⚠️ **Retsirkulyatsiya nasosi ishlamayotganda va motorli klapan yopilmaganda sharlarning teskari oqishining oldini olish uchun yig'gich kirish quvurida teshikli qaytmas qopqoq o'rnatilgan**
• Qopqoqda **ko'rish oynasi** bor — tizimdagi shar harakatini kuzatish uchun; **qo'l teshigi** — tizimga shar solish uchun

⚠️ **Δp ikki qiymati:** to'rning **normal <3 kPa**, alarm esa **>7 kPa**. Ya'ni normal ish va alarm orasida **2.3 barobar** zaxira bor. Δp 3 kPa dan oshib borishi — sharlar to'rda to'planayotganini yoki to'r ifloslanayotganini bildiradi, alarmni kutmang.

---

**🇷🇺 Резиновый шарик — правило размера**

⚠️ **ГЛАВНОЕ ПРАВИЛО: диаметр МОКРОГО шарика должен быть на 1–2 мм БОЛЬШЕ ВНУТРЕННЕГО диаметра трубки.**

**Требования** — **износостойкий, мягкий, эластичный** | ⚠️ **поры максимально РАВНОМЕРНЫЕ** | ⚠️ **удельный вес мокрого шарика БЛИЗОК к воде**
**Два типа** — **обычный** (обычные отложения) | ⚠️ **с корундовым покрытием** (ТВЁРДЫЕ отложения)
**Спецификация** — **сухой диаметр 27.5 и 27 мм**, **мягкий**

**Расчёт** — трубка Ø **28.575 мм**, стенка **0.5 / 0.7 мм** → внутренний **27.575 / 27.175 мм** → ⚠️ **нужен мокрый 28.6–29.6 / 28.2–29.2 мм** → сухой **27.5 / 27 мм** должен набрать **~1 мм**

⚠️ **Поэтому 24 часа замачивания ОБЯЗАТЕЛЬНЫ.** Сухой шарик (27.5 мм) МЕНЬШЕ внутреннего диаметра (27.575 мм) — проходит свободно и **ничего не чистит**.
⚠️ **Два сухих размера — под две толщины стенки.** Трубок со стенкой 0.7 мм всего **1454** из 27 908, то есть **5%**.

**Насос 10PAH01/02AP001** — **125JQ-27**, **108 м³/ч = 30 л/с**, напор **27 м**, **1460 об/мин**, **NPSHr 7 м**, КПД **65%**, **13.5 кВт**; двигатель **1LE0003-1EB23-4AA4**, **18.5 кВт**
**Сетка** — ⚠️ **нормальный Δp <3 кПа** (сигнал **>70 мбар = 7 кПа**); корпус **A36 антикор**, сетка и вал **316L**
**Сборник** — корпус, **переключающий клапан**, сетка, лючок, сопло выгрузки, дренаж, воздушник, крышка, **обратная захлопка**. При циркуляции клапан открыт; при сборе переводится в положение сбора, вода уходит через **два непроходных отверстия** и сетку. ⚠️ **Захлопка с отверстием на входе не даёт шарикам уйти обратно при остановленном насосе и незакрытой задвижке.** В крышке **смотровое стекло**, лючок для загрузки.

⚠️ **Между нормой (<3 кПа) и сигналом (7 кПа) запас в 2.3 раза.** Рост выше 3 кПа — шарики копятся в сетке или сетка загрязняется; не ждите сигнала.

---

**🇬🇧 Sponge Ball — the sizing rule**

⚠️ **THE KEY RULE: the diameter of the WET sponge ball must be 1–2 mm LARGER than the internal diameter of the cooling tube.**

**Ball requirements** — **wear-resistant, soft and elastic** | ⚠️ **air holes as EVEN as possible** | ⚠️ **specific gravity of the wet balls NEAR that of water**
**Two kinds** — **normal sponge ball** (removes fouling) | ⚠️ **sponge ball with corundum coating** (removes HARD fouling on the tube wall)
**Specification** — **dry diameter 27.5 mm and 27 mm**, hardness **soft**

**The arithmetic** — condenser tube OD **28.575 mm**, wall **0.5 / 0.7 mm** → ID **27.575 / 27.175 mm** → ⚠️ **required wet ball 28.6–29.6 / 28.2–29.2 mm** → the dry ball at **27.5 / 27 mm** must swell about **1 mm**

⚠️ **This is why the 24-hour soak is mandatory.** A dry ball (27.5 mm) is SMALLER than the tube ID (27.575 mm) — it passes straight through and **cleans nothing**.
⚠️ **Two dry sizes for two wall thicknesses.** Only **1454** of the 27,908 tubes have 0.7 mm wall — about **5%**.

**Ball pump 10PAH01/02AP001** — **125JQ-27**, **108 m³/h = 30 l/s**, head **27 m**, **1460 rpm**, **NPSHr 7 m**, efficiency **65%**, shaft power **13.5 kW**; motor **1LE0003-1EB23-4AA4**, **18.5 kW**
**Ball screen** — ⚠️ **normal pressure differential <3 kPa** (alarm **>70 mbar = 7 kPa**); shell and connections **A36 anti-corrosion**, screen and driving shaft **316L**
**Ball collector** — shell, **changeover valve**, screen, hand hole, ball discharge nozzle, draining, venting, cover, **non-return flap**. While balls circulate the changeover valve is open; to collect, it switches to the collection position and blocks the balls with the valve trim, water flowing out through **two nonstop holes** and the screen. ⚠️ **A non-return flap with a hole in the collector inlet pipe prevents back flow of balls when the recirculating pump is not running and the motor valve is not closed.** The cover has a **sight glass** for observing ball operation; the **hand hole** is for inserting balls.

⚠️ **Normal (<3 kPa) to alarm (7 kPa) is a 2.3× margin.** Rising past 3 kPa means balls are collecting in the screen or the screen is fouling — don't wait for the alarm.

`#rubberball #spongeball #sizing #condensertubes`

---
---

## POST 81 — Yordamchi bug' manbalari

**🇺🇿 Yordamchi bug' — ikki manba va o'tish**

**Vazifasi**
Yordamchi bug' quyidagilar uchun mo'ljallangan:
1. **Turbina gland zichlashiga** zichlash bug'i berish
2. **Turbina ishga tushirishida** oldindan qizdirish bug'i
3. **Kimyoviy xom suvni** isitish bug'i

**Manba 1 — Ishga tushirish qozoni**
⚠️ **Bug' turbinasining dastlabki ishga tushirish bosqichida ishga tushirish qozoni turbina val zichlashi va oldindan qizdirish talablarini qondirish uchun bevosita bug' beradi.**
| Parametr | Qiymat |
|---|---|
| **Bosim** | **14 bar.g** |
| **Harorat** | **320°C** |
| **Sarf** | **20 t/soat** |

**Manba 2 — Sovuq qayta qizdirish (CRH)**
⚠️ **Gaz turbinasi ishga tushgandan keyin HRSG superqizdirgichi superqizdirilgan main bug' hosil qiladi. Main bug' HP bypass orqali CRH ga kiritiladi, CRH esa bug'ni HRH va IP bypass orqali kondensatorga yo'naltiradi — shu tariqa bug'-suv sikli hosil bo'ladi. Shu paytda CRH bug' bosimi va harorati yordamchi bug' talablariga javob bersa, yordamchi bug' manbasini CRH ga o'tkazish mumkin.**
| Parametr (15°C, GT 100%) | Qiymat |
|---|---|
| **Bosim** | **43.2 bar.g** |
| **Harorat** | **386°C** |
| **Sarf** | **962 t/soat** |

**Boshqaruv strategiyasi**
⚠️ **Normal holatda yordamchi bug' kollektorining manbasi — SOVUQ QAYTA QIZDIRISH.**
• **Bosim:** pnevmatik boshqaruv klapani **10LBG10AA101** yordamchi bug' kollektor bosimini ⚠️ **0.8–1.2 MPa** da ushlab turadi
• **Harorat:** sovutish suvi rostlash klapani **10LCE15AA101** bug' haroratini ⚠️ **260–350°C** diapazonida boshqaradi

⚠️ **Ikki manba orasidagi farq juda katta:** qozon **14 bar.g / 320°C / 20 t/soat**, CRH **43.2 bar.g / 386°C / 962 t/soat**. Sarf bo'yicha **48 barobar** farq. Shuning uchun CRH ga o'tish ishga tushirishning muhim bosqichi — qozon butun stansiyani ta'minlay olmaydi.

⚠️ **6-bobdagi alarm chegaralari:** bosim **>12.5 bar**, harorat **>360°C**. Boshqaruv diapazoni esa **0.8–1.2 MPa = 8–12 bar** va **260–350°C**. Ya'ni alarm boshqaruv diapazonining **yuqori chekkasidan sal yuqorida** — bu normal.

⚠️ **Ishga tushirish qozoni 14 bar.g beradi, lekin kollektor 8–12 bar da ushlanadi.** Ya'ni qozondan kelgan bug' rostlash klapanida **drossellanadi**. Qozon bosimi tushib ketsa kollektorni ushlab bo'lmaydi.

---

**🇷🇺 Вспомогательный пар — два источника**

**Назначение** — уплотняющий пар на уплотнения турбины | пар для **прогрева при пуске** | пар для **подогрева химически очищенной воды**

**Источник 1 — пусковая котельная**
⚠️ **На начальном этапе пуска ПТ котельная напрямую обеспечивает уплотнения и прогрев.**
**14 бар.g** | **320°C** | **20 т/ч**

**Источник 2 — холодный промперегрев (CRH)**
⚠️ **После пуска ГТ пароперегреватель КУ вырабатывает главный пар, который через БРОУ ВД идёт в CRH, далее через HRH и БРОУ СД в конденсатор, образуя пароводяной цикл. Когда параметры CRH удовлетворяют требованиям, источник переключают на CRH.**
**43.2 бар.g** | **386°C** | **962 т/ч** (при 15°C, ГТ 100%)

**Управление**
⚠️ **В нормальном режиме источник — ХОЛОДНЫЙ ПРОМПЕРЕГРЕВ.**
Давление: клапан **10LBG10AA101** держит ⚠️ **0.8–1.2 МПа** | Температура: клапан **10LCE15AA101** держит ⚠️ **260–350°C**

⚠️ **Разница огромна:** по расходу **в 48 раз**. Переход на CRH — ключевой этап пуска, котельная весь блок не потянет.
⚠️ **Сигналы главы 6:** давление **>12.5 бар**, температура **>360°C** — чуть выше верхней границы рабочего диапазона.
⚠️ **Котельная даёт 14 бар.g, коллектор держится на 8–12 бар** — пар дросселируется. При просадке котельной коллектор не удержать.

---

**🇬🇧 Auxiliary Steam — two sources**

**Purpose** — sealing steam to the turbine gland seal | **preheating steam for turbine startup** | heating steam for chemical raw water

**Source 1 — Start-up boiler**
⚠️ **During the initial start-up phase of the steam turbine, the start-up boiler directly supplies steam to meet the requirements of the shaft seal and preheating.**
**Pressure 14 bar.g** | **Temperature 320°C** | **Flow 20 t/h**

**Source 2 — Cold Reheat (CRH)**
⚠️ **After the gas turbine is started, the HRSG superheater generates superheated main steam. It is introduced into the cold reheat via the high-pressure bypass, and the CRH channels steam into the condenser through the hot reheat and IP bypass, forming a steam-water cycle. When CRH pressure and temperature meet the auxiliary steam requirements, the source can be switched to CRH.**
**Pressure 43.2 bar.g** | **Temperature 386°C** | **Flow 962 t/h** (at 15°C, GT 100%)

**Control strategy**
⚠️ **Normally the steam source of the auxiliary steam header is from cold reheat.**
Pressure: pneumatic control valve **10LBG10AA101** maintains ⚠️ **0.8–1.2 MPa** | Temperature: cooling water regulating valve **10LCE15AA101** holds ⚠️ **260–350°C**

⚠️ **The two sources differ enormously** — **48 times** in flow. Switching to CRH is a key start-up milestone; the boiler cannot carry the plant.
⚠️ **Chapter 6 alarms** are pressure **>12.5 bar** and temperature **>360°C** — just above the top of the control band, which is normal.
⚠️ **The boiler delivers 14 bar.g while the header holds 8–12 bar** — the steam is throttled at the control valve. If boiler pressure sags, the header cannot be held.

`#auxsteam #CRH #startupboiler`

---
---

## POST 82 — Val zichlash: harorat rejimi

**🇺🇿 Seal steam harorati — start turiga qarab**

⚠️ **Barcha bug' haroratlari bug' kollektor bosimi 0.28 barg gacha drossellangandan KEYINGI qiymatlar.**

**Mutlaq chegara**
⚠️ **Steam seal yoqilgan HAR QANDAY vaqtda steam seal kollektor harorati (10MAW11CT001A/001B) 149°C DAN YUQORI bo'lishi SHART** — turbinaga suv/ho'l bug' kirishining oldini olish uchun.

**Start turiga qarab qayerga qo'yish**
| Start turi | Harorat diapazonida qayerda | Nima uchun |
|---|---|---|
| **Sovuq start** | ⚠️ **Diapazonning PASTIDA** | **Uzun rotor differensial kengayishini** va **rotor charchash resursini** boshqarish uchun |
| **Iliq start** | ⚠️ **Diapazonning O'RTASIDA** | — |
| **Issiq start** | ⚠️ **Diapazonning YUQORISIDA** | **Qisqa rotor differensial kengayishi**, **rotor charchash resursi** va **radial zazor nazorati** uchun |

**LP bug' harorati**
⚠️ **LP bo'lim rotori va korpus materiali 400°C DAN PAST bug' sharoitiga chidashga mo'ljallangan.**
Shu sababdan quyidagi barcha holatlarda **LP packing sohasiga 180°C dan PAST zichlash bug'i berilishi SHART**:
• Turbina turning gear da, steam seal yoqilgan
• Ishga tushirishda, turbina self-sealing nuqtasidan past
• Self-sealing nuqtasidan yuqorida ishlash davomida
• To'xtatishda, kondensator vakuumi saqlanayotganda

LP Steam Seal Desuperheater — LP uchki packing sohasiga beriladigan zichlash bug'ini sovutish uchun. TCS **10MAW11CT006** haroratini **10LCE12AA101** klapani orqali **150–180°C** da ushlaydi.

**Yordamchi bug' sharoiti zichlash uchun: 0.28 bar.g, 309.6°C**

**Steam seal klapanlari**
• **Steam seal aux feed valve: 10MAW11AA101**
• **Steam packing unloading valve: 10MAW12AA101**
• Turbina val packing ulanishlariga quvur **feed va unloading klapanlari ORASIDAGI** kollektordan chiqariladi
• Bosim transmitteri **10MAW11CP001A/001B** TCS ga **20 mA** signal yuboradi
• ⚠️ **Har ikkala klapan mustaqil 4–20 mA signalda to'liq yurish bilan ishlaydi: 4 mA = to'liq yopiq, 20 mA = to'liq ochiq**

**GSC blower avto mantiqi (3.7.6.1)**
⚠️ Avtomatik ish **faqat Automatic rejimida** bajariladi.
1. **Ikkala blower dvigateli ham ishlayotgan bo'lsa** — TCS blower **"B"** ga har qanday START komandasini **olib tashlaydi**
2. **Ikkalasi ham ishlamayotgan bo'lsa** — TCS **blower A** ni ishga tushiradi
3. **Dvigatel A ishlamasa** — **dvigatel B** ishga tushiriladi
4. **Dvigatel B ishga tushmasa** — **alarm** beriladi
5. ⚠️ **GSC bosimi alarm setpointidan (−0.015 barg) yuqori bo'lsa — zaxira GSC blower ishga tushadi**

**N1 packing leak off klapani (10MAM11AA101)**
⚠️ **N1 packing leak off liniyasi IP exhaust ga ulangan. Leak off bosimi turbina yuklamasi oshgani sayin ko'tariladi, va u IP exhaust bosimidan 1 bar YUQORI ishlashga sozlangan.**
Bosim setpointi: **IP exhaust bosimi (10MAC11CP001) + 1 bar**

⚠️ **Blower throttle klapani (10MAW61AA501/10MAW62AA501)** tizim vakuumini rostlaydi — ⚠️ **ishga tushirish davrida QO'LDA sozlanadi**. Ikki blowerli tizimda **o'chirish klapanlari (10MAW61AA503/10MAW62AA503)** ishlamayotgan blowerni ajratish uchun.

---

**🇷🇺 Температура уплотняющего пара — по типу пуска**

⚠️ **Все температуры — ПОСЛЕ дросселирования до давления коллектора 0.28 барг.**

⚠️ **При поданном уплотняющем паре температура коллектора (10MAW11CT001A/001B) ОБЯЗАНА быть ВЫШЕ 149°C** — против заброса воды и влажного пара.

| Тип пуска | Где в диапазоне | Зачем |
|---|---|---|
| **Холодный** | ⚠️ **НИЖЕ** | управление **ОРС длинного ротора** и **усталостным ресурсом** |
| **Тёплый** | ⚠️ **СЕРЕДИНА** | — |
| **Горячий** | ⚠️ **ВЫШЕ** | **ОРС короткого ротора**, ресурс, **контроль радиальных зазоров** |

⚠️ **Материал ротора и корпуса ЦНД рассчитан на пар НИЖЕ 400°C**, поэтому в уплотнения ЦНД подаётся пар **НИЖЕ 180°C** во всех режимах (ВПУ с паром, пуск до самоуплотнения, работа выше него, останов с вакуумом). Пароохладитель + TCS держат **10MAW11CT006** на **150–180°C** клапаном **10LCE12AA101**.
**Параметры вспомогательного пара: 0.28 бар.g, 309.6°C**

**Клапаны** — **10MAW11AA101** (подача) и **10MAW12AA101** (сброс); трубопровод к уплотнениям отходит **МЕЖДУ ними**; датчик **10MAW11CP001A/001B** даёт **20 мА**; ⚠️ **оба клапана на независимых сигналах 4–20 мА: 4 мА = закрыт, 20 мА = открыт**

**Автологика эксгаустеров** — оба работают → снять START с **B** | ни один → пуск **A** | A не идёт → **B** | B не идёт → **сигнал** | ⚠️ **давление СП выше −0.015 барг → пуск резервного**

**Клапан N1 (10MAM11AA101)** — ⚠️ **линия отсоса N1 заведена на выхлоп ЦСД; уставка = давление выхлопа ЦСД (10MAC11CP001) + 1 бар**

⚠️ **Дроссель эксгаустера (10MAW61AA501/62AA501)** регулирует разрежение — ⚠️ **настраивается ВРУЧНУЮ при пусконаладке**; отсечные **10MAW61AA503/62AA503** изолируют неработающий.

---

**🇬🇧 Sealing Steam Temperature — by start type**

⚠️ **All steam temperatures are after steam has been throttled to header pressure of 0.28 barg.**

⚠️ **At all times when steam seals are on, steam seal header temperature (10MAW11CT001A/001B) must be above 149°C to prevent water/wet steam induction into the turbine.**

| Start type | Where in the band | Why |
|---|---|---|
| **Cold starts** | ⚠️ **Set LOW in the range** | to manage **long rotor differential expansion** and **rotor fatigue life** |
| **Warm starts** | ⚠️ **Set in the MIDDLE** | — |
| **Hot starts** | ⚠️ **Set HIGH in the range** | to manage **short rotor differential expansion**, **rotor fatigue life**, and **radial clearance control** |

**LP steam temperature**
⚠️ **The LP section rotor and casing material are designed to withstand exposure to steam conditions below 400°C.** So sealing steam **below 180°C must be supplied to the low-pressure packing** whenever: the turbine is on turning gear with steam seals on; during startup below the self-sealing point; during operation above the self-sealing point; and during shutdown when condenser vacuum is maintained.
The LP Steam Seal Desuperheater cools the sealing steam; TCS holds **10MAW11CT006** at about **150–180°C** via **10LCE12AA101**.
**Aux steam condition for sealing: 0.28 bar.g, 309.6°C**

**Steam seal valves** — **steam seal aux feed valve 10MAW11AA101** and **steam packing unloading valve 10MAW12AA101**; piping to the shaft packing runs from the header **BETWEEN the feed and unloading valves**; pressure transmitter **10MAW11CP001A/001B** sends a **20 mA** signal; ⚠️ **each valve operates full stroke on independent 4–20 mA signals: 4 mA = full closed, 20 mA = full open**

**GSC blower auto logic (3.7.6.1)** — if both running, TCS removes any START command to blower **"B"** | if neither runs, start motor **A** | if A is not running, start **B** | if B does not start, **alarm** | ⚠️ **if gland steam condenser pressure is higher than the alarm set point (−0.015 barg), the standby blower starts**

**N1 packing leak off valve (10MAM11AA101)** — ⚠️ **the N1 leak off line is connected to IP Exhaust; leak off pressure rises as turbine load increases, and it is set to operate 1 bar higher than IP exhaust pressure.** Setpoint: **IP exhaust pressure (10MAC11CP001) + 1 bar**

⚠️ **The blower throttle valve (10MAW61AA501/10MAW62AA501)** regulates system vacuum and is ⚠️ **adjusted manually during the commissioning period**; shutoff valves **10MAW61AA503/10MAW62AA503** isolate the inoperative blower.

`#glandsteam #sealsteam #GSCblower #N1packing`

---
---

## POST 83 — Bug' quvurlari va parametrlari

**🇺🇿 Main / reheat / LP bug' — quvur va spetsifikatsiya**

**Quvur o'lchamlari (diametr × devor, mm)**
| Tizim | Ulanish | O'lchamlar |
|---|---|---|
| **Main bug'** | ikkilangan-bir-ikkilangan | **356×57, 457×72, 356×57** |
| **Qayta qizdirish** | ikkilangan-bir-ikkilangan | **736.6×35, 1016×47, 711.2×35** |
| **LP bug'** | ikkilangan-bir | **660×9.53, 762×9.53** |

**Konfiguratsiya**
• **Main:** har bir HRSG superqizdirgichi chiqishida ikkita alohida quvur → **ikkita HP main bug' klapani va ikkita HP boshqaruv klapani** orqali HP silindrga
• ⚠️ **Turbina main bug' klapanidan oldin quvurda TO'XTATISH KLAPANI VA MAIN BUG' SARFINI O'LCHASH DROSSEL UZELI O'RNATILMAGAN**
• Drenaj quvurlari main bug' kollektorida va ikkala shox quvurda. **Uchala drenaj yo'li pnevmatik drenaj klapani orqali drenaj flash bakiga** yo'naltiriladi
• ⚠️ **Bug' turbinasi yuklamasi 15% DAN PAST bo'lganda drenaj klapanlari AVTOMATIK ochiladi** — turbina va quvurlarning ishonchli drenajini ta'minlash uchun

• **Qayta qizdirish:** har bir HRSG reheater chiqishida ikkita alohida quvur → **ikkita IP main bug' klapani va TO'RTTA IP boshqaruv klapani** orqali IP silindrga
• **HP exhaust check valve** sovuq qayta qizdirish kollektorida — **bypass ishida bug'ning HP silindrga qaytib oqishining oldini oladi**. **Pnevmatik boshqariladi** va **bypass bosim rostlash balans klapani** bilan jihozlangan
• ⚠️ **Turbina sinxronlanib barqaror dastlabki yuklamani ko'targandan KEYIN HP exhaust check valve ochilishi mumkin, va HP silindr exhaust ventilyatsiya klapani yopilishi mumkin**
• Check valve dan **oldin bitta, keyin ikkita drenaj baki**. ⚠️ **Drenaj klapanlarining ochilishi/yopilishi drenaj baklarining SUV SATHI VYKLYUCHATELLARI bilan boshqariladi**

• **LP:** har bir HRSG LP superqizdirgichi chiqishida ikkita alohida quvur → **bitta LP main klapan va bitta LP boshqaruv klapani** orqali LP silindrga

**Bug' spetsifikatsiyasi (Table 3-8-1) — mos nuqta: 15°C, namlik 60%, 97.7 kPa, 100% yuklama**
| Nuqta | Harorat | Bosim | Sarf |
|---|---|---|---|
| HP superqizdirgich chiqishi | **601.619°C** | **169.48 bar.a** | **486.7272 t/s** |
| IP superqizdirgich chiqishi | **324.395°C** | **42.89 bar.a** | **66.0096 t/s** |
| Sovuq qayta qizdirish kirishi | **385.25°C** | **42.410 bar.a** | **481.9104 t/s** |
| Issiq qayta qizdirish chiqishi | **611.508°C** | **40.324 bar.a** | **547.9164 t/s** |
| LP superqizdirgich chiqishi | **332.802°C** | **5.33 bar.a** | **68.6808 t/s** |

⚠️ **Bu qiymatlar BITTA HRSG uchun.** Ikkita HRSG bo'lgani uchun turbinaga kiradigan jami sarf ikki barobar: HP **486.7 × 2 = 973.5 t/s** — Table 1-1-1 dagi **972.576 t/s** bilan mos.

**Ikki quvur orasidagi harorat farqi**
⚠️ **Normal ishda main, reheat va LP superqizdirilgan bug'ning IKKI QUVURIDAGI harorat chetlanishi 14°C DAN OSHMASLIGI kerak.**
⚠️ **G'ayritabiiy sharoitda chetlanish 42°C dan oshmasligi, DAVOMIYLIGI 15 DAQIQADAN OSHMASLIGI, va keyingi hodisalar orasidagi interval 4 SOATDAN KO'P bo'lishi kerak.**

⚠️ **Bu 7.2.5 dagi qoida bilan bir xil** (POST 19): 14°C normal, 42°C 15 daqiqagacha har 4 soatda. Ikki joyda takrorlangan — demak muhim.

⚠️ **"Main bug' sarfini o'lchash drossel uzeli yo'q"** — bu POST 24 dagi thrust wear detector qismi bilan bog'liq: manual "agar diafragma bilan o'lchansa bug' sarfida keskin sakrash bor-yo'qligini tekshiring" deydi. **Bu birlikda bunday o'lchov yo'q**, shuning uchun suv kirishini sarfdan aniqlab bo'lmaydi — faqat harorat va thrust bo'yicha.

---

**🇷🇺 Паропроводы и параметры пара**

**Размеры (диаметр × стенка, мм)** — главный **356×57, 457×72, 356×57** | промперегрев **736.6×35, 1016×47, 711.2×35** | НД **660×9.53, 762×9.53**

**Конфигурация** — главный: два паропровода на КУ → **два ГСК и два РК ВД** | ⚠️ **перед ГСК НЕТ ни отсечной арматуры, ни сужающего устройства для измерения расхода** | дренажи на коллекторе и обеих ветках → расширитель; ⚠️ **при нагрузке НИЖЕ 15% дренажи открываются АВТОМАТИЧЕСКИ**
Промперегрев: два паропровода → **два ГСК и ЧЕТЫРЕ РК СД** | **обратный клапан на холодном промперегреве** против заброса в ЦВД при работе БРОУ, **пневматический**, с **балансировочным клапаном**; ⚠️ **открывается ПОСЛЕ синхронизации и набора устойчивой начальной нагрузки**, тогда же закрывается вентиляционный клапан ЦВД; **один расширитель до и два после**, ⚠️ **управление по РЕЛЕ УРОВНЯ расширителей**
НД: два паропровода → **один ГСК и один РК НД**

**Параметры (на ОДИН КУ)** — ВД **601.619°C / 169.48 бар.а / 486.7272 т/ч** | СД **324.395°C / 42.89 бар.а / 66.0096 т/ч** | холодный промперегрев **385.25°C / 42.410 бар.а / 481.9104 т/ч** | горячий **611.508°C / 40.324 бар.а / 547.9164 т/ч** | НД **332.802°C / 5.33 бар.а / 68.6808 т/ч**
⚠️ **Два КУ дают вдвое: 486.7 × 2 = 973.5 т/ч**, что совпадает с **972.576 т/ч** из Table 1-1-1.

⚠️ **Расхождение температур в ДВУХ паропроводах не более 14°C**; ⚠️ **в аномальных условиях до 42°C, не дольше 15 МИНУТ, интервал между случаями более 4 ЧАСОВ.**
⚠️ **Отсутствие расходомера на главном паре** означает, что заброс воды по расходу не отследить — только по температуре и упорному.

---

**🇬🇧 Main / Reheat / LP Steam — piping and specification**

**Pipe sizes (diameter × wall, mm)** — main steam **356×57, 457×72, 356×57** | reheat **736.6×35, 1016×47, 711.2×35** | LP steam **660×9.53, 762×9.53**

**Configuration**
Main: two separate pipelines at each HRSG superheater outlet in **double-single-double** connection → **two HP main steam valves and two HP control valves** into the HP cylinder | ⚠️ **No shut-off valve or main steam flow measurement throttling assembly is installed on the main steam pipeline before the main steam valve** | drains on the header and both branch pipes, all three paths to the drain flash tank through pneumatic drain valves | ⚠️ **when steam turbine load is below 15%, the drain valves automatically open** to ensure reliable drainage
Reheat: two pipelines per HRSG → **two IP main steam valves and FOUR IP control valves** | **HP exhaust check valve** on the cold reheat header **prevents steam flowing back into the HP cylinder during bypass operation**; **pneumatically controlled** with a **bypass pressure regulating balance valve**; ⚠️ **after the turbine is synchronized and carries a stable initial load, the check valve can be opened and the HP exhaust ventilation valve closed**; one drain tank before and two after, ⚠️ **drain valve opening/closing controlled by the WATER LEVEL SWITCHES of the drain tanks**
LP: two pipelines per HRSG in **double-single** connection → **one LP main valve and one LP control valve**

**Steam specification (Table 3-8-1) — reference: 15°C, 60% RH, 97.7 kPa, 100% load**
HP SH outlet **601.619°C / 169.48 bar.a / 486.7272 t/h** | IP SH outlet **324.395°C / 42.89 bar.a / 66.0096 t/h** | Cold reheat inlet **385.25°C / 42.410 bar.a / 481.9104 t/h** | Hot reheat outlet **611.508°C / 40.324 bar.a / 547.9164 t/h** | LP SH outlet **332.802°C / 5.33 bar.a / 68.6808 t/h**
⚠️ **These are per HRSG.** With two HRSGs the total is doubled: HP **486.7 × 2 = 973.5 t/h**, matching the **972.576 t/h** in Table 1-1-1.

**Two-pipeline temperature deviation**
⚠️ **During normal operation the allowable deviation of steam temperature in the two pipelines for main, reheat and LP superheated steam shall not exceed 14°C.**
⚠️ **Under abnormal conditions the deviation shall not exceed 42°C, with duration not exceeding 15 MINUTES, and the interval between subsequent occurrences more than 4 HOURS.**

⚠️ **Identical to the rule in 7.2.5** (POST 19) — stated in two places, which tells you it matters.
⚠️ **No main steam flow measurement** means water induction cannot be caught on flow — only on temperature and thrust (see POST 24).

`#mainsteam #reheat #piping #drains`

---
---

## POST 84 — Kondensator hot well va make-up

**🇺🇿 Hot well sath boshqaruvi va kondensat sifati**

**Sath boshqaruvi**
Kondensator hot well **sath transmitteri (LT)** bilan jihozlangan, u **10MAG01CL101/2/3** o'lchoviga asoslanib **kirish make-up pnevmatik klapanini (10LCR10AA101/10LCR10AA102)** ochadi/yopadi.

⚠️ **Uchta transmitter — MED (o'rtacha) mantiq uchun.** Bittasi noto'g'ri ko'rsatsa boshqaruv buzilmaydi.

**Sath chegaralari (POST 13 dan)**
| Holat | Qiymat | Ta'sir |
|---|---|---|
| HH | ≥2390 mm | Alarm + **bypass interlok bilan yopiladi** |
| H | ≥2240 mm | Alarm |
| L | ≤1490 mm | Alarm |
| LL | ≤1340 mm | **Nasosni trip** |

⚠️ **Ishga tushirishdan oldin to'ldirish darajasi: tag plitadan <−350 mm** (5.4.2).

**Kondensat kimyoviy dozalash (3.4.2.4)**
⚠️ **Kondensat suvi sifati qozon va turbina kabi uskunalarning xavfsiz ishlashiga BEVOSITA ta'sir qiladi.**

Dozalashning asosiy maqsadlari:
1. ⚠️ **pH ni boshqarish va kislotali korroziyani kamaytirish** — sirkulyatsiya jarayonida kondensat **karbonat angidrid kabi gazlarning erishi tufayli kislotali bo'lib qolishi** va quvur korroziyasiga olib kelishi mumkin. Dozalash pH ni oqilona diapazongacha ko'taradi
2. ⚠️ **Erigan kislorodni olib tashlash yoki bostirish** — kislorod korroziyasining oldini olish. **Kondensatga havo aralashsa kislorod eriydi va termik tizimda kislorod korroziyasini keltirib chiqaradi**
3. **Suv sifati barqarorligini saqlash, cho'kmani kamaytirish** — kondensatdagi tuz ionlari konsentratsiyasini nazorat qilish va **qozonning isitish yuzasida cho'kma hosil bo'lishini oldini olish** → termik samaradorlik yo'qotilishini kamaytirish

⚠️ **DIQQAT — ZIDLIK:** kondensat tizimida **erigan kislorod OLIB TASHLANADI**, lekin **stator sovutish suvida kislorod 2–8 ppm da SAQLANADI** (POST 66). Ikki butunlay teskari kimyoviy rejim, bitta stansiyada. Namunalarni chalkashtirmang.

**Kondensat namuna olish tizimi (3.4.2.5)**
Namuna olish tizimlari kondensatni **uzluksiz** namuna oladi va tahlil qiladi — **aralashma darajasi, ion konsentratsiyasi** va boshqa ko'rsatkichlarni o'lchaydi. Bu **korroziya, cho'kma va sizishlar** kabi potentsial muammolarni o'z vaqtida aniqlash imkonini beradi.

**Gland steam kondensatorining vazifasi (3.4.2.2)**
⚠️ **Asosiy vazifasi — turbina bug' zichlash tizimidagi bug'-gaz aralashmasini so'rib olish va sovutish, uchki zichlashlardan bug'ning turbina zaliga va YOG' TIZIMIGA chiqib ketishining oldini olish** — bu atrof-muhitni ifloslantiradi va **yog' sifatini pasaytiradi**.
Bug'-gaz aralashmasi GSC ga kiradi, u yerda **asosiy kondensat oziqlantiruvchi suvi isitiladi** va gland bug'i suvga aylantiriladi. Qolgan oz miqdordagi **kondensatsiyalanmaydigan gaz elektr ventilyator bilan siqiladi** va atmosferaga **atmosfera bosimidan biroz yuqori bosimda** chiqariladi.

⚠️ **Kondensat qaytish yo'li: GSC dan kondensat LOOP SEAL orqali kondensat tizimiga qaytadi.** Loop seal qurib qolsa GSC vakuumi buziladi.

⚠️ **Zanjir:** gland bug'i bosimi **>42 kPa** → bug' podshipnik tomonga → **yog'da suv** → **emulsifikatsiya (sut rangi)** → POST 65 dagi vakuumli yog' tozalagich **namlik ≤0.1% gacha**. Bitta klapan sozlamasi yog' tizimini buzadi.

---

**🇷🇺 Уровень в конденсатосборнике и качество конденсата**

**Управление уровнем** — **уровнемер (LT)** открывает/закрывает **клапаны подпитки 10LCR10AA101/102** по измерению **10MAG01CL101/2/3**
⚠️ **Три датчика — под логику MED.** Отказ одного не ломает регулирование.
Уставки: **HH ≥2390** (сигнал + закрытие БРОУ по блокировке) | **H ≥2240** | **L ≤1490** | **LL ≤1340** (отключение насоса)
⚠️ **Заполнение перед пуском: <−350 мм от нижней плиты**

**Дозирование в конденсат** — ⚠️ **качество конденсата ПРЯМО влияет на безопасность котла и турбины**
⚠️ **Регулирование pH против кислотной коррозии** (растворение CO₂ закисляет конденсат) | ⚠️ **удаление/подавление растворённого кислорода** против кислородной коррозии (подсос воздуха растворяет кислород) | контроль солей против **отложений на поверхностях нагрева**

⚠️ **ВНИМАНИЕ — ПРОТИВОРЕЧИЕ:** в конденсате кислород **УДАЛЯЮТ**, а в статорной воде **ДЕРЖАТ 2–8 ppm** (POST 66). Два противоположных ВХР на одном блоке.

**Пробоотбор** — **непрерывный** анализ примесей и ионов для раннего выявления **коррозии, отложений и течей**

**Назначение СП** — ⚠️ **отсос и охлаждение паровоздушной смеси, чтобы пар не уходил в машзал и В МАСЛОСИСТЕМУ** (обводнение масла). Смесь греет основной конденсат, пар конденсируется, **неконденсирующийся газ сжимается вентилятором** и сбрасывается **чуть выше атмосферного**.
⚠️ **Конденсат из СП возвращается через ГИДРОЗАТВОР.** Пересохший затвор срывает разрежение СП.

⚠️ **Цепочка:** уплотняющий пар **>42 кПа** → пар к подшипникам → **вода в масле** → **эмульсия** → вакуумная маслоочистка до **влаги ≤0.1%**.

---

**🇬🇧 Condenser Hot Well Level and Condensate Quality**

**Level control** — the hot well is provided with a **level transmitter (LT)** which opens/closes the **inlet make-up pneumatic valves (10LCR10AA101/10LCR10AA102)** based on measurement by LT **10MAG01CL101/2/3**
⚠️ **Three transmitters, for MED voting.** One failed instrument does not break control.
Limits: **HH ≥2390 mm** (alarm + interlock close bypass) | **H ≥2240** | **L ≤1490** | **LL ≤1340** (trip pump)
⚠️ **Fill level before start: <−350 mm from the bottom plate**

**Condensate chemical dosing (3.4.2.4)**
⚠️ **The quality of condensate water directly affects the safe operation of equipment such as boilers and turbines.**
⚠️ **Control pH and reduce acidic corrosion** — condensate may become acidic from dissolved gases such as carbon dioxide, leading to pipeline corrosion; dosing raises pH into a reasonable range | ⚠️ **Remove or inhibit dissolved oxygen** to prevent oxygen corrosion — if air mixes into the condensate it dissolves oxygen and causes oxygen corrosion in the thermal system | Maintain water quality stability and reduce scaling by controlling salt ion concentration, avoiding **scale on boiler heating surfaces**

⚠️ **NOTE THE CONTRADICTION:** in the condensate system oxygen is **REMOVED**, while in stator cooling water oxygen is **HELD at 2–8 ppm** (POST 66). Two opposite chemistry regimes on the same plant — don't mix up the samples.

**Condensate sampling system (3.4.2.5)** — sampling systems **continuously** sample and analyse condensate, measuring **impurity levels, ion concentrations** and other indicators, allowing timely detection of **corrosion, scaling and leaks**

**Gland steam condenser function (3.4.2.2)**
⚠️ **Its main function is to extract and cool the steam and gas mixture in the turbine's steam seal system, preventing steam from leaking from the end seals into the turbine room and OIL SYSTEM**, which pollutes the environment and **decreases the oil quality**.
The mixture enters the GSC where the **main condensate feedwater is heated** and gland steam is cooled into water. The remaining small amount of **non-condensable gas is compressed by an electric fan** and discharged to atmosphere at **slightly higher than atmospheric pressure**.

⚠️ **Condensed steam is returned to the condensate system through a LOOP SEAL.** A dried-out loop seal breaks GSC vacuum.

⚠️ **The chain:** gland steam above **42 kPa** → steam toward the bearings → **water in the oil** → **emulsification (milky white)** → vacuum purifier until **moisture ≤0.1%** (POST 65). One valve setting wrecks the oil system.

`#hotwell #condensate #chemistry #GSC #loopseal`

---
---

## POST 85 — Avariyalarni bartaraf etish tamoyillari

**🇺🇿 6 ta tamoyil — aniq raqamlar bilan**

Umumiy tamoyil: **"xavfsizlik birinchi, xavfni tez nazorat qilish, ilmiy bartaraf etish, yopiq sikl boshqaruv".**

**1. XAVFSIZLIK BIRINCHI**
⚠️ **Uchta MUMKIN EMAS (ikkilamchi shikastning oldini olish):**
• **Podshipnikda yog' yo'q bo'lganda turning gear ni MAJBURAN aylantirmang** — journal yeyilishining oldini olish uchun
• **Yog' tizimi yong'inini SUV bilan o'chirmang** — yog' yong'ini tarqalishining oldini olish uchun
• **Vakuum keskin tushganda ORTIQCHA YUKLAMADA ishlamang** — exhaust haroratining ortiqcha oshishidan kondensator shikastlanishining oldini olish uchun

**2. TEZ JAVOB**
⚠️ **Avariyalar to'satdan va tarqaluvchan: yog' yong'ini 1 DAQIQA ichida 10 METR radiusga tarqalishi mumkin.**
⚠️ **Dastlabki bartaraf etish 5–10 DAQIQA ichida boshlanishi shart.**
⚠️ **Joydagi xodim KO'RSATMA KUTMAYDI** — "avariya to'xtatish", "yog'/bug' ta'minotini uzish", "yong'in o'chirish" kabi asosiy operatsiyalarni bevosita bajaradi va **keyin** dispetcherga xabar beradi.

Operatsiyalar tartibi: ⚠️ **avval xavf manbasini uzish → keyin parametrlarni nazorat qilish → oxirida sababni qidirish**
• Yog' yong'inida: avval **yog' chiqish klapanini yop** → keyin **o't o'chir** → oxirida **sizish nuqtasini tekshir**
• Ortiqcha tebranishda: avval **yuklamani tushir** → keyin **tebranish manbasini qidir**
⚠️ **Tebranishni nazorat qilishni kechiktirib, sabab qidirishga ustuvorlik BERMANG**

**3. AVVAL NAZORAT, KEYIN QIDIRUV**
⚠️ **Exhaust harorati juda yuqori:** avval **LP silindr purkash sovutishni yoqing va haroratni 55°C DAN PAST ushlang**, keyin kondensator nosozligini qidiring
⚠️ **Podshipnik harorati ko'tarilmoqda:** avval **yuklamani 50% DAN PASTGA tushiring**, keyin moylash tizimini tekshiring
⚠️ **Tekshiruv faqat xavf nazorat ostiga olingandan keyin** — yong'in o'chirilgan, bosim tushirilgan va **harorat 60°C DAN PAST** bo'lgandan keyingina uskunani ochish mumkin

**4. ILMIY BARTARAF ETISH**
⚠️ **Asboblarga tayaning, sezgiga emas:**
• Tebranish me'yordan oshganini aniqlash uchun **qo'l bilan sezishga emas, tebranish datchigi ko'rsatkichiga** tayaning
• Yog' sifati buzilganini aniqlash uchun **faqat rangni kuzatishga emas, namuna olib qovushqoqlik va namlikni sinashga** tayaning

**5. USKUNANI HIMOYA QILISH**
⚠️ **To'xtatishdan keyin rotor harorati xavfsiz qiymatga (odatda <150°C) tushmasa — turning gear ni ishlashda qoldiring.** Mahalliy yuqori haroratdan rotor egilishining oldini olish uchun.
⚠️ **Silindr yong'inda kuygan bo'lsa — har 30 DAQIQADA rotorni QO'LDA 180° aylantiring.**
⚠️ **Rotor harakatsiz turganda MAJBURAN ishga tushirmang** — journal va podshipnik orasidagi quruq ishqalanishdan qochish uchun.
• Yog' avariyasidan keyin bak va quvurlarni **kerosin bilan yuvib** tozalang, buzilgan yog'ni almashtiring. ⚠️ **Ifloslangan yoki kokslangan yog' bilan ishga tushirmang.**
• Kondensator nosozligidan keyin ⚠️ **vakuum tiklanmaguncha ishga tushirmang** — exhaust haroratining ortiqchaligidan titan quvurlar shikastlanmasligi uchun

**Tiklanish bosqichida yuklama ko'tarish**
⚠️ **30% nominal yuklamadan boshlang. Har 10% yuklama oshirishda 30 DAQIQA barqarorlashtiring**, tebranish va haroratda anomaliya yo'qligini tasdiqlagandan keyingina davom eting.
⚠️ **Bir yo'la nominal yuklamaga sakramang** — zarbadan qismlar shikastlanadi.

**6. YOPIQ SIKL BOSHQARUV**
"Bartaraf etish → tahlil → tuzatish → o'qitish" sikli. ⚠️ **"Bevosita sabab" va "ildiz sabab"ni ajrating** — boshqaruv kamchiliklarini hal qilmasdan faqat qismni almashtirib qo'ymang.

⚠️ **Bir joyga to'plangan raqamlar:** javob **5–10 daqiqa** | yong'in tarqalishi **1 daqiqada 10 m** | exhaust **<55°C** | podshipnik uchun yuklama **<50%** | tekshiruv **<60°C** | turning gear **<150°C** | qo'lda aylantirish **30 daqiqada 180°** | qayta yuklama **30% dan, 10% / 30 daqiqa**

---

**🇷🇺 Шесть принципов ликвидации аварий — с цифрами**

**1. БЕЗОПАСНОСТЬ ПРЕЖДЕ ВСЕГО** — ⚠️ **три «НЕЛЬЗЯ»:** не проворачивать ВПУ силой при отсутствии масла | не тушить масло водой | не работать с перегрузкой при резком падении вакуума

**2. БЫСТРЫЙ ОТВЕТ** — ⚠️ **масляный пожар за 1 МИНУТУ распространяется на 10 МЕТРОВ**; ⚠️ **первые действия в течение 5–10 МИНУТ**; ⚠️ **персонал НЕ ЖДЁТ указаний** — отключение, отсечка масла/пара, тушение, и **только потом** доклад
Порядок: ⚠️ **отсечь источник → стабилизировать параметры → искать причину**

**3. СНАЧАЛА КОНТРОЛЬ, ПОТОМ ПОИСК** — ⚠️ **высокая температура выхлопа: включить впрыск и держать НИЖЕ 55°C**, потом искать | ⚠️ **рост температуры подшипника: разгрузить НИЖЕ 50%**, потом смотреть масло | ⚠️ **вскрытие только после снижения температуры НИЖЕ 60°C**

**4. ОПИРАТЬСЯ НА ПРИБОРЫ** — вибрация по датчику, а не на ощупь; качество масла по анализу, а не по цвету

**5. ЗАЩИТА ОБОРУДОВАНИЯ** — ⚠️ **держать ВПУ, пока ротор не остынет ниже 150°C**; ⚠️ **при обгоревшем цилиндре проворачивать ВРУЧНУЮ на 180° КАЖДЫЕ 30 МИНУТ**; ⚠️ **не пускать силой неподвижный ротор**; промывка керосином после масляной аварии; ⚠️ **не пускать до восстановления вакуума** (титановые трубки)
⚠️ **Набор нагрузки при восстановлении: с 30%, по 10% с выдержкой 30 МИНУТ.** Прыжок сразу на номинал запрещён.

**6. ЗАМКНУТЫЙ ЦИКЛ** — ⚠️ **разделять «прямую» и «коренную» причину**

---

**🇬🇧 Six Accident Handling Principles — with the numbers**

General principle: **"safety first, rapid risk control, scientific handling, and closed-loop management".**

**1. SAFETY FIRST** — ⚠️ **three prohibitions to prevent secondary damage:** do not force the turning gear when the bearing is out of oil (prevents journal wear) | do not use water to put out oil system fires (prevents oil fire spread) | do not operate at overload when vacuum drops sharply (prevents condenser damage from excessively high exhaust temperature)

**2. RAPID RESPONSE** — ⚠️ **accidents spread: oil fires can spread to a 10-METRE range within 1 MINUTE**; ⚠️ **initial handling must be initiated within 5–10 MINUTES**; ⚠️ **on-site personnel do not need to wait for instructions** — perform emergency shutdown, cut off oil/steam supply, extinguish fire, and report **afterwards**
Order: ⚠️ **first cut off the hazard source → then control parameters → finally investigate the cause**. Oil fire: close the oil outlet valve → extinguish → then check the leak point. Excessive vibration: reduce load → then investigate the source. ⚠️ **Do not delay controlling vibration by prioritizing cause investigation.**

**3. CONTROL FIRST, INVESTIGATE LATER** — ⚠️ **excessively high exhaust temperature: first activate LP cylinder spray cooling to control temperature BELOW 55°C**, then investigate condenser faults | ⚠️ **rising bearing temperature: first reduce load BELOW 50%**, then check the lube oil system | ⚠️ **conduct disassembly and testing only after fire extinguishment, pressure relief, and temperature drop BELOW 60°C**

**4. RELY ON PROCEDURES AND DATA** — determine vibration by sensor readings, not hand feel; determine oil deterioration by sampling viscosity and moisture, not by observing colour

**5. EQUIPMENT PROTECTION** — ⚠️ **if rotor temperature does not drop to a safe value (usually <150°C) after shutdown, keep the turning gear running** to prevent rotor bending from local high temperature; ⚠️ **manually turn the rotor 180° EVERY 30 MINUTES when the cylinder is baked by fire**; ⚠️ **do not force start when the rotor is stationary** to avoid dry friction between journal and bearings; after an oil accident flush the tank and pipelines **with kerosene** and replace deteriorated oil — ⚠️ **do not start with contaminated or coked oil**; after a condenser fault ⚠️ **do not start before vacuum is restored** to prevent titanium tube damage
⚠️ **Recovery loading: start from 30% of rated load, stabilize 30 MINUTES for every 10% increase**, continue only after confirming no vibration or temperature abnormalities. ⚠️ **Do not jump to rated load at once.**

**6. CLOSED-LOOP MANAGEMENT** — ⚠️ **distinguish "direct causes" from "root causes"**; do not just replace components without addressing management loopholes

⚠️ **All the numbers in one place:** response **5–10 min** | fire spread **10 m in 1 min** | exhaust **<55°C** | load **<50%** for bearing temp | investigation **<60°C** | turning gear **<150°C** | manual turn **180° every 30 min** | recovery **from 30%, 10% per 30 min**

`#accidenthandling #principles #emergency`

---
---

## POST 86 — To'liq stansiya ishga tushirish ketma-ketligi

**🇺🇿 BOP → GT → HRSG → ST — 34 qadam**

**BOP ishga tushirish (1–16 qadam)**
| Qadam | Tizim | Kimni ta'minlaydi |
|---|---|---|
| 1 | **Suv olish tizimi** | Dastlabki ishlov berish |
| 2 | **Dastlabki ishlov berish** | Yong'in suvi havzasi, tiniqlangan suv havzasi |
| 3 | **Xizmat suvi tizimi** | DM zavod, ACCW, CCW |
| 4 | **Gradirnya havzasi to'ldirish** | Mexanik gradirnya asosi |
| 5 | **ACCWS** | CCW |
| 6 | **Deminerallashtirilgan suv zavodi** | HVAC, vodorod stansiyasi, CCCW, kondensat |
| 7 | **CCCWS** | **GT:** kuchaytirilgan sovutish havo kompressori, control oil, lube oil, 2C sovutgich, generator H2 sovutgich · **ST:** lube oil, kondensat nasos va dvigatel, stator suvi sovutgich, H2 sovutgich · **HRSG:** oziqlantiruvchi nasos sovutgich · **Yonilg'i gazi:** kompressor bosqichlararo sovutgich, kompressor lube oil sovutgich |
| 8 | **CCWS** | Kondensator, rubber ball, vakuum nasos |
| 9 | **Kondensat tizimi** | GSC quvur tomoni, ikkala HRSG LP baraban, CCW qaytish, drenaj flash baklar, yordamchi bug', IP/LP bypass, vakuum buzish zichlash suvi, kondensator purkash, gland steam, LP silindr purkash, namuna olish, dozalash |
| 10 | **Qozon IP/HP oziqlantiruvchi nasos** | IP/HP baraban to'ldirish, **GT sovutish havo sovutgich (TCA)** |
| 11 | **Ishga tushirish qozoni** | Yordamchi bug' |
| 12 | **Yordamchi bug' tizimi** | Gland steam, **ST oldindan qizdirish**, sovuq qayta qizdirish, DM zavod filtr chiqishi suvini isitish |
| **13** | ⚠️ **ST yordamchi tizimlari KETMA-KET** | **(1) Lube oil → (2) Seal oil → (3) Jacking oil → (4) Turning gear → (5) Stator sovutish suvi → (6) Generator Air-CO2-H2 almashtirish → (7) Control oil** |
| 14 | **Gland steam tizimi** | Kondensat, kondensator, GSC, yordamchi bug' |
| 15 | **Vakuum tizimi** | CCW, kondensator, IP/LP bypass, bug' drenaji |
| 16 | **HRSG bypass damper** | ⚠️ **HRSG tomoniga to'liq ochiladi** |

⚠️ **13-qadamdagi ST ketma-ketligi QAT'IY:** lube oil birinchi (seal oil unga tayanadi), seal oil ikkinchi (H2 almashtirishdan oldin shart), jacking oil uchinchi (lube oil bosimiga tayanadi), turning gear to'rtinchi (jacking oil shart), stator suvi beshinchi, gaz almashtirish oltinchi, control oil oxirida.

**GT ishga tushirish (17–33 qadam)**
**17-qadam — GT yordamchi tizimlari:** yonilg'i gazi bosimi, asboblar havosi, CCCW, lube oil, seal oil, ⚠️ **turning gear 3 rpm da**, H2 almashtirilgan, control oil, GT package ventilyatsiya, TCA/FGH klapanlari, yonilg'i gazi oxirgi filtrlari to'liq ochiq, **SFC ishda**, generator rele paneli ishda

**Tezlik bosqichlari:**
| Tezlik | Nima sodir bo'ladi |
|---|---|
| **>3 rpm** | ⚠️ **Turning gear avtomatik ajraladi** |
| **>10% (300 rpm)** | Turning gear dvigateli o'chadi |
| **~500 rpm** | ⚠️ **Purge boshlanadi** |
| **~670 rpm** | ⚠️ **Purge taymeri hisoblanadi, GT purge tugaguncha shu tezlikni ushlaydi** |
| **~600 rpm** | ⚠️ **Alangalanish uchun tezlik pasaytiriladi.** Yonilg'i gazi shut off bypass klapani ochiladi, vent klapani yopiladi |
| **~600 rpm** | ⚠️ **Alangalanish. #12 va #13 kameralarda yonish boshlanadi, alanga cross-flame quvurlar orqali soat va soatga teskari yo'nalishda uzatiladi.** Alanga yonganidan keyin ignitor solenoidi quvvatsizlantiriladi |
| **>1944 rpm** | **HP bleed klapan yopiladi** |
| **~2000 rpm gacha** | Tezlanish **SFC va yonilg'i yonishi bilan birgalikda** |
| **~2000 rpm** | ⚠️ **SFC uziladi va to'xtaydi.** Bundan keyin GT o'z yonishi bilan FSNL gacha tezlashadi |
| **>2804 rpm** | **LP bleed klapan yopiladi** |
| **>2853 rpm** | **MP bleed klapan yopiladi** |
| **>98%** | Nominal tezlikka yaqinlashadi |
| **Sinxronizatsiya** | ⚠️ **Avtomatik sinxronizator bilan, yuklama darhol 27 MVt (GT nominal yuklamasining 5%) ga oshiriladi** |

**IGV/VV pozitsiyasi**
⚠️ **Ishga tushirish ketma-ketligida IGV (MBA01AA701) va VV (MBA01AA703) MINIMAL ochiq.** Tezlanish davrida tezlik monitori sozlamasi bo'yicha **34° va 13.6°** ochiq pozitsiyaga o'tadi. GT sinxronizatsiyasidan keyin yuklama ko'tarilishi jarayonida ochilishi boshqariladi va **oxirida to'liq ochiladi**.

**34-qadam — HRSG:** HP, IP, LP bypass tizimini ishga solish va bug' bosimi hamda haroratini rostlash

⚠️ **Purge hajmi simple cycle va combined cycle uchun HAR XIL, shuning uchun purge taymeri sozlamasi ham har xil.**

---

**🇷🇺 Полная последовательность пуска блока — 34 шага**

**BOP (шаги 1–16)** — водозабор → предочистка → служебная вода (ХВО, ВЦОС, ЦОС) → подпитка градирни → ВЦОС → ХВО (HVAC, водородная станция, ЗКОС, конденсат) → **ЗКОС** (ГТ: компрессор охлаждающего воздуха, ОГ, масло, охладитель 2C, водородные охладители; ПТ: масло, КЭН, охладители статорной воды и водорода; КУ: охладитель питательных насосов; топливный газ: межступенчатый и масляный охладители) → **ЦОС** (конденсатор, шариковая очистка, вакуумные насосы) → **конденсат** (СП, барабаны НД обоих КУ, впрыски, пробоотбор, дозирование) → питательные насосы ВД/СД (**+ охладитель охлаждающего воздуха ГТ, TCA**) → пусковая котельная → вспомогательный пар (уплотнения, **прогрев ПТ**, холодный промперегрев) → ⚠️ **шаг 13: вспомсистемы ПТ ПО ПОРЯДКУ — масло → уплотняющее масло → гидроподъём → ВПУ → статорная вода → замещение воздух-CO2-H2 → ОГ** → уплотняющий пар → вакуум → ⚠️ **байпасный шибер КУ полностью открыт на сторону КУ**

**ГТ (шаги 17–33)** — вспомсистемы, ⚠️ **ВПУ на 3 об/мин**, SFC в работе
⚠️ **>3 об/мин — ВПУ автоматически расцепляется** | **>300 об/мин — двигатель ВПУ выключается** | ⚠️ **~500 об/мин — начало вентиляции** | ⚠️ **~670 об/мин — отсчёт таймера вентиляции** | ⚠️ **~600 об/мин — снижение для розжига**; ⚠️ **розжиг в камерах №12 и №13, пламя передаётся по огнеперебросным патрубкам в обе стороны** | **>1944 — закрытие ВД сброса** | ⚠️ **~2000 — отключение SFC** | **>2804 — НД сброс** | **>2853 — СД сброс** | **>98% — выход на номинал** | ⚠️ **синхронизация, нагрузка сразу до 27 МВт (5% номинала ГТ)**
⚠️ **IGV (MBA01AA701) и VV (MBA01AA703) при пуске МИНИМАЛЬНО открыты**, при разгоне выходят на **34° и 13.6°**, после синхронизации открываются полностью
⚠️ **Объём вентиляции для ГТУ и ПГУ РАЗНЫЙ — таймеры тоже разные**

---

**🇬🇧 Full Plant Start Sequence — 34 steps**

**BOP start (steps 1–16)**
Intake water → pre-treatment (firefighting basin, clarified water basin) → service water (DM plant, ACCW, CCW) → cooling tower basin make-up → ACCWS → DM plant (HVAC, hydrogen station, CCCW, condensate) → **CCCWS** (GT: enhanced cooling air compressor, control oil, lube oil, 2C cooler, generator hydrogen cooler; ST: lube oil, condensate pump and motor, stator cooling water cooler, hydrogen cooler; HRSG: feed water pump cooling water cooler; fuel gas: compressor interstage cooler, compressor lube oil cooler) → **CCWS** (condenser, rubber ball, vacuum pumps) → **condensate** (GSC tube side, both HRSG LP drums, all de-superheating users, sampling, dosing) → boiler IP/HP feed water pumps (**plus GT cooling air cooler, TCA**) → start-up boiler → auxiliary steam (gland steam, **ST preheating**, cold reheat, DM plant filter outlet heating) → ⚠️ **step 13: ST auxiliary systems IN SEQUENCE — lube oil → sealing oil → jacking oil → turning gear → stator cooling water → generator Air-CO2-H2 replacement → control oil** → gland steam → vacuum → ⚠️ **HRSG bypass damper fully open to HRSG side**

⚠️ **The step-13 order is strict:** lube oil first (seal oil depends on it), seal oil second (required before gas replacement), jacking oil third (needs lube header pressure), turning gear fourth (needs jacking oil), stator water fifth, gas replacement sixth, control oil last.

**GT start (steps 17–33)**
Auxiliaries: fuel gas supply pressure, instrument air, CCCW, lube oil, sealing oil, ⚠️ **turning gear at 3 rpm**, H2 replacement done, control oil, package ventilation, TCA/FGH valves, fuel gas last chance filters fully open, **SFC in service**, generator control relay panel in service

| Speed | Event |
|---|---|
| **>3 rpm** | ⚠️ **running gear automatically decouples** |
| **>10% (300 rpm)** | turning motor off |
| **~500 rpm** | ⚠️ **purging starts** |
| **~670 rpm** | ⚠️ **purge timer count starts; GT holds this speed until purge complete** |
| **~600 rpm** | ⚠️ **speed decreased for ignition**; fuel gas shut off bypass valve opens, vent valve closes |
| **~600 rpm** | ⚠️ **ignition — combustion occurs at #12 and #13 combustors; the flame is transmitted clockwise and counterclockwise through cross-flame tubes**; after flame on the igniter solenoid is de-energized |
| **>1944 rpm** | **HP bleed valve closes** |
| **to ~2000 rpm** | acceleration by **both SFC and fuel gas combustion** |
| **~2000 rpm** | ⚠️ **SFC is cut and shut down**; from here GT accelerates on its own combustion to FSNL |
| **>2804 rpm** | **LP bleed valve closes** |
| **>2853 rpm** | **MP bleed valve closes** |
| **>98%** | approaching rated speed |
| **Synchronization** | ⚠️ **automatic synchronizer; load immediately increased to 27 MW (5% of GT rated load)** |

⚠️ **IGV (MBA01AA701) and VV (MBA01AA703) are at MINIMUM opening in the start-up sequence**; during acceleration they move to **34° and 13.6°** open per the speed monitor setting; after synchronization they are controlled open during load-up and finally open completely.

**Step 34 — HRSG:** put HP, IP, LP bypass into operation and regulate steam pressure and temperature

⚠️ **Required purge volumes differ for simple cycle and combined cycle, so purge timer settings also differ.**

`#startsequence #BOP #GT #HRSG #purge`

---
---

## POST 87 — H2 va CO2 almashtirish: klapan pozitsiyalari

**🇺🇿 Gaz almashtirish — uch yo'lli klapanlar**

**Ikkita uch yo'lli klapan barcha rejimni belgilaydi:**
• **10MKG21AA005** — generator tomoni (ta'minot/chiqarish)
• **10MKG21AA006** — CO2 tomoni

| Amal | 10MKG21AA006 | 10MKG21AA005 | Izoh |
|---|---|---|---|
| **Asboblar havosi to'ldirish** | **Chapga** | **Chapga** (havo ta'minoti) | Asboblar havosi ta'minot klapani **10MKG21AA004 OCHIQ**, H2 bosim boshqaruv klapani chiqish qo'l klapani **10MKG21AA003 YOPIQ** |
| **Havoni CO2 bilan almashtirish** | ⚠️ **Yuqoriga** (CO2 ta'minoti) | ⚠️ **Yuqoriga** (havo chiqarish) | — |
| **CO2 ni H2 bilan almashtirish** | ⚠️ **Chapga** (CO2 chiqarish) | ⚠️ **Chapga** (H2 ta'minoti) | — |
| **H2 ni CO2 bilan almashtirish** | ⚠️ **Yuqoriga** (CO2 ta'minoti) | ⚠️ **Yuqoriga** (H2 chiqarish) | — |
| **CO2 ni havo bilan almashtirish** | ⚠️ **Chapga** (CO2 chiqarish) | ⚠️ **Chapga** (havo ta'minoti) | — |

⚠️ **Barcha holatlarda:** H2 purge sensing klapani **10MKG21AA044 YOPIQ**, vent klapani **10MKG21AA041 OCHIQ**

⚠️ **Diqqat: 006 "yuqoriga" doim CO2 ta'minoti, "chapga" doim CO2 chiqarish.** 005 esa "yuqoriga" — chiqarish, "chapga" — ta'minot. Ikkalasi bir vaqtda bir tomonga buriladi.

**Gaz hajmlari**
⚠️ **Havo va H2 purge uchun kerakli CO2 ballonlari hajmi: 252 m³**
⚠️ **Generatorni to'ldirish uchun kerakli H2 ballonlari hajmi: 504 m³**
Gaz hajmi **1 atm bosim, 25°C** ga standartlashtirilgan.
⚠️ **Bu raqam BITTA to'liq purge sikli uchun:** generatordan barcha havoni chiqarish uchun CO2 **+** generatordan barcha H2 ni chiqarish uchun CO2.

**H2 tozaligi boshqaruvi (4.2.5.2)**
Tozalik **termik gaz analizatori (10MKG21CQ001, 002)** bilan kuzatiladi
• **<95%** → gaz tozaligi past alarmi
• **<90%** → gaz tozaligi past-past alarmi
• ⚠️ **H2 gazi manifolddan tozalik 99% DAN YUQORI bo'lguncha beriladi**

**H2 bosimi boshqaruvi (4.5.2.3)**
Bosim **10MKG21CP002** bilan kuzatiladi, **5.17 bar.g** ushlanadi
• **<5.03 bar.g** → past alarm (**10MKG21CP101**). ⚠️ **H2 manifolddan 5.17 bar.g ga yetguncha beriladi**
• **>5.45 bar.g** → yuqori alarm (**10MKG21CP102**). ⚠️ **Vent klapani (10MKG21AA501) ochilib 5.17 bar.g ga tushguncha chiqariladi, keyin yopiladi**

**H2 quritgichi (4.2.2.6)**
⚠️ **Ikkita quritish minorasi va qizdirgich, sovutgich, kondensat drenaj trap va boshqaruv paneli.** Bir minora quritadi, ikkinchisi regeneratsiya qiladi. ⚠️ **Ikki minora HAR 8 SOATDA avtomatik ravishda rollarini almashtiradi.**
Spetsifikatsiya: ikki idishli, **Z-purge** panel, avtomatik. **Desikant: faollashtirilgan alyuminiy oksidi.** Asboblar havosi sarfi **3 m³/soat** (uzluksiz). Portlashga chidamli **EX IIC T1 (zona 2)**. Quvvat **400 V AC**. **Quvvati 10 m³/soat.** Elektr qizdirgich **1.0 kW**.

**H2/CO2 manifold (4.2.2.7)**
• **Pigtail** — har bir ballon uchun bittadan, har birining manifold uchida **qaytmas klapan**
• **O'chirish klapani** — har bir ballon uchun bittadan
• ⚠️ **Bosim rostlagich klapani — ballon manifold yuqori bosimini H2 uchun ~8 barg, CO2 uchun ~7 barg gacha tushiradi**

**CO2 bug'latgich (4.2.2.8)**
⚠️ **Radiatsiyali issiqlik almashgich (issiqlik manbai — atmosfera havosi) — yashirin issiqlik tufayli CO2 tiqilishining oldini olish uchun.**

**Gaz boshqaruv klapan stansiyasi** — mexanik rostlash turi, **nominal bosim 5.17 bar.g**, uglerodli po'lat
**H2 boshqaruv shkafi** — H2/CO2/havo, **EX IIC T1 (zona 2)**, **230 V AC**

⚠️ **H2 tizimida TRIP signali YO'Q** — barcha signallar faqat monitoring va alarm uchun (4.2.5). Ishga tushirish ruxsati: **generator val zichlash tizimi oldindan ishlayotgan bo'lishi shart**.

---

**🇷🇺 Замещение газов — положения трёхходовых кранов**

**Два крана задают весь режим:** **10MKG21AA005** (сторона генератора) и **10MKG21AA006** (сторона CO2)

| Операция | 006 | 005 |
|---|---|---|
| **Заполнение КИП-воздухом** | **влево** | **влево** (подача воздуха) |
| **Вытеснение воздуха CO2** | ⚠️ **вверх** (подача CO2) | ⚠️ **вверх** (сброс воздуха) |
| **Вытеснение CO2 водородом** | ⚠️ **влево** (сброс CO2) | ⚠️ **влево** (подача H2) |
| **Вытеснение H2 углекислотой** | ⚠️ **вверх** (подача CO2) | ⚠️ **вверх** (сброс H2) |
| **Вытеснение CO2 воздухом** | ⚠️ **влево** (сброс CO2) | ⚠️ **влево** (подача воздуха) |

⚠️ **Во всех случаях:** **10MKG21AA044 ЗАКРЫТ**, **10MKG21AA041 ОТКРЫТ**

**Объёмы газа** — ⚠️ **CO2 на продувку воздуха и H2: 252 м³** | ⚠️ **H2 на заполнение: 504 м³** (при 1 атм, 25°C) — ⚠️ **на ОДИН полный цикл продувки**

**Чистота H2** — анализатор **10MKG21CQ001, 002**: **<95%** сигнал, **<90%** сигнал LL; ⚠️ **подпитка до чистоты ВЫШЕ 99%**
**Давление H2** — датчик **10MKG21CP002**, уставка **5.17 бар.g**: **<5.03** сигнал → подпитка до 5.17 | **>5.45** сигнал → сброс через **10MKG21AA501** до 5.17, затем закрытие

**Осушитель H2** — ⚠️ **две башни, ПЕРЕКЛЮЧЕНИЕ КАЖДЫЕ 8 ЧАСОВ**; **активированный оксид алюминия**, КИП-воздух **3 м³/ч**, **EX IIC T1 (зона 2)**, **400 В AC**, производительность **10 м³/ч**, нагреватель **1.0 кВт**
**Манифольд** — **пигтейлы с обратными клапанами**, отсечные на каждый баллон, ⚠️ **редуктор: H2 до ~8 барг, CO2 до ~7 барг**
**Испаритель CO2** — ⚠️ **радиационный, от атмосферного воздуха, против закупорки CO2**

⚠️ **В водородной системе НЕТ сигналов защиты** — только мониторинг и сигнализация. Разрешение на пуск: **система уплотняющего масла уже в работе**.

---

**🇬🇧 H2 and CO2 Replacement — three-way valve positions**

**Two three-way valves set every mode:** **10MKG21AA005** (generator side) and **10MKG21AA006** (CO2 side)

| Operation | 10MKG21AA006 | 10MKG21AA005 |
|---|---|---|
| **Instrument air filling** | **Handles to left** | **Handles to left** (air supply) |
| **Replacement of air with CO2** | ⚠️ **Handles to up** (CO2 supply) | ⚠️ **Handles to up** (air discharge) |
| **Replacement of CO2 with H2** | ⚠️ **Handles to left** (CO2 discharge) | ⚠️ **Handles to left** (H2 supply) |
| **Replacement of H2 with CO2** | ⚠️ **Handles to up** (CO2 supply) | ⚠️ **Handles to up** (H2 discharge) |
| **Replacement of CO2 with air** | ⚠️ **Handles to left** (CO2 discharge) | ⚠️ **Handles to left** (air supply) |

⚠️ **In every case:** H2 purge sensing valve **10MKG21AA044 closed**, vent valve **10MKG21AA041 opened**

**Gas volumes**
⚠️ **Volume of CO2 gas cylinders required for Air & H2 gas purge: 252 m³**
⚠️ **Volume of H2 gas cylinders required to fill the generator: 504 m³**
Standardized to **1 atm, 25°C**. ⚠️ **This is the total usable gas volume for ONE complete purging cycle** — the CO2 to remove all air plus the CO2 to remove all the H2.

**H2 purity control** — thermal gas analyzer **10MKG21CQ001, 002**: **<95%** low alarm, **<90%** low-low alarm; ⚠️ **H2 is supplied from the manifold until purity is above 99%**
**H2 pressure control** — transmitter **10MKG21CP002** maintains **5.17 bar.g**: **<5.03 bar.g** low alarm (**10MKG21CP101**), ⚠️ **supply until 5.17**; **>5.45 bar.g** high alarm (**10MKG21CP102**), ⚠️ **vent via 10MKG21AA501 down to 5.17, then close**

**H2 gas dryer** — two drying towers and heaters, cooler, condensate drain trap, control panel; one tower dries while the other regenerates; ⚠️ **the two towers automatically change roles every 8 HOURS**. Dual vessel, **Z-purge type panel**, automatic; desiccant **activated alumina**; instrument air **3 m³/h** continuous; **EX IIC T1 (zone 2)**; **400 V AC**; capacity **10 m³/h**; electric heater **1.0 kW**

**H2/CO2 manifold** — **pigtails** with a **check valve** on each manifold end fitting; **shut off valve** per bottle; ⚠️ **pressure regulator drops bottle manifold pressure to approximately 8 barg (H2) and 7 barg (CO2)**
**CO2 vaporizer** — ⚠️ **radiate type heat exchanger using atmospheric air, to prevent CO2 blockage by latent heat**

**Gas control valve station** — mechanical regulating type, **rated 5.17 bar.g**, carbon steel | **H2 control cabinet** — H2/CO2/air, **EX IIC T1 (zone 2)**, **230 V AC**

⚠️ **There is NO trip signal in the H2 system** — all signals are for monitoring and alarm only. Start permissive: **the generator shaft seal system must already be operating.**

`#hydrogen #CO2 #purging #threewayvalve #dryer`

---
---

## POST 88 — Jacking oil boshqaruvi va tuzatish

**🇺🇿 JOP — 380/400 rpm sirini ochamiz**

⚠️ **Bu chalkashlikni aniqlab oldik:**
• **JOP AVTO TO'XTAYDI:** ⚠️ **normal ishga tushirishda tezlik 400 rpm ga YETGANDA** (ko'tarilishda)
• **JOP AVTO ISHGA TUSHADI:** ⚠️ **turbina sekinlashib 380 rpm ga TUSHGANDA** (pasayishda)

Ya'ni **20 rpm gisterezis** bor — bu sikllanishning oldini oladi. Bir raqam ikkinchisining xatosi emas.

**JOP ishga tushirish ruxsati (3.13.4.1)**
⚠️ **MOP birinchi ishlayotgan bo'lishi, JOP so'rish bosimi 0.5 barg ga yetishi, va lube oil kollektori 1.7 barg bo'lishi SHART.**
*(Diqqat: 3.13 bo'limida so'rish bosimi ~0.15 MPa = 1.5 barg deb yozilgan, 3.13.4.1 da esa 0.5 barg. Ruxsat sharti pastroq — nasos kavitatsiyaga tushmasligi uchun minimal qiymat.)*

**Xavfsizlik klapani (3.13.2.4)**
• **1 × 100%**, jacking oil kollektor liniyasida
• ⚠️ **Sozlama bosimi: 180 bar.g**
• Kollektor bosimi sozlamadan oshsa — klapan orqali chiqariladi, **yog' lube oil bakiga qaytadi**
• ⚠️ **Bu xavfsizlik klapani — jacking nasosdan keyingi liniyalar TO'SILIB QOLSA ochiladi.** Klapan ochilganda nasos bevosita bakka haydaydi va **quvur yorilishining oldini oladi**
• ⚠️ **Dastlabki stansiya ishga tushirishda xavfsizlik klapani MAKSIMAL tizim bosimiga sozlanadi va normal ish sharoitida ochilmaydi**

**Filtrlar — ikkitasi bor, chalkashtirmang**
| Filtr | Joyi | Aniqligi | Kuzatuv |
|---|---|---|---|
| **So'rish filtri** | Nasos oldida | ⚠️ **50 mikron** | PDIT-03 |
| **Chiqish filtri** | ⚠️ **Nasosdan KEYINGI kollektor liniyasida** | ⚠️ **20 mikron, bir martalik element** | **PDIT-04** |

Ikkalasi ham **duplex**, operator tiqilgan holatda **qo'lda ikkinchi tomonga o'tkaza oladi**.

**Jacking oil manifold bloki (3.13.2.5)**
⚠️ **Ta'minlangan yog'ni HAR BIR PODSHIPNIKGA bo'lib beruvchi qurilma.** Har bir chiqish liniyasida **manometr va FCV (sarf boshqaruv klapani)** o'rnatilgan. **FCV har bir chiqish liniyasiga beriladigan yog' miqdorini boshqaradi.**

⚠️ **Uchta bosim raqami bir tizimda:** ish bosimi **~150 bar**, alarm **60 bar**, xavfsizlik klapani **180 bar**. Ishga tushirish diapazoni **100–150 bar** (Step 35). Ya'ni normaldan xavfsizlik klapanigacha atigi **30 bar**.

---

**🇷🇺 Гидроподъём — разгадка 380/400 об/мин**

⚠️ **Противоречия нет:**
• **Автоостанов** — ⚠️ **при разгоне, когда обороты ДОСТИГАЮТ 400 об/мин**
• **Автопуск** — ⚠️ **при выбеге, когда обороты СНИЖАЮТСЯ до 380 об/мин**
Гистерезис **20 об/мин** против циклирования.

**Разрешение на пуск** — ⚠️ **МНС уже работает, давление на всасе гидроподъёма 0.5 барг, коллектор смазки 1.7 барг**

**Предохранительный клапан** — 1×100% в коллекторе, ⚠️ **уставка 180 бар.g**, сброс **в маслобак**; ⚠️ **открывается при ЗАКУПОРКЕ линий за насосом**, насос сбрасывает прямо в бак, **предотвращая разрыв трубопровода**; ⚠️ **при первичной наладке настраивается на максимальное давление системы и в нормальной работе не открывается**

**Два фильтра** — на всасе **50 мкм** (PDIT-03) | ⚠️ **на нагнетании 20 мкм, одноразовый элемент** (**PDIT-04**); оба **сдвоенные**, переключение **вручную**

**Блок-манифольд** — ⚠️ **делит масло ПО ПОДШИПНИКАМ**; на каждой отводящей линии **манометр и клапан регулирования расхода (FCV)**

⚠️ **Три давления:** рабочее **~150 бар**, сигнал **60 бар**, предохранительный **180 бар**; пусковой диапазон **100–150 бар**. От нормы до предохранительного всего **30 бар**.

---

**🇬🇧 Jacking Oil — the 380/400 rpm puzzle solved**

⚠️ **There is no contradiction:**
• **JOP AUTO STOP:** ⚠️ **during normal start-up, when steam turbine speed reaches 400 rpm** (on the way up)
• **JOP AUTO START:** ⚠️ **when the turbine is decelerated and reaches 380 rpm** (on the way down)
A **20 rpm hysteresis** prevents cycling. Neither figure is a typo for the other.

**JOP start permission (3.13.4.1)**
⚠️ **When the MOP is operated first, and the JOP suction pressure is up to 0.5 barg, and the lube oil header is 1.7 barg, it is possible to start JOP.**
*(Note: section 3.13 gives suction pressure as ~0.15 MPa = 1.5 barg; 3.13.4.1 gives 0.5 barg as the permissive. The permissive is the lower figure — the minimum that keeps the pump out of cavitation.)*

**Relief valve (3.13.2.4)**
One 100% capacity relief valve in the jacking oil header line. ⚠️ **Set pressure 180 bar.g.** Oil removed through it **returns to the lube oil reservoir**.
⚠️ **This is a safety valve which opens when the set allowable pressure is exceeded — e.g. if the lines downstream of the lifting oil pump are blocked.** With it open the pump discharges directly back to the tank, **which prevents pipe bursts**.
⚠️ **During initial plant startup the relief valve is set to the maximum system pressure and does not therefore open under normal operating conditions.**

**Two filters — don't confuse them**
Suction filter, upstream of the pump, ⚠️ **50 micron**, monitored by **PDIT-03** | Discharge filter, ⚠️ **in the pump downstream header line**, ⚠️ **disposable 20-micron element**, monitored by **PDIT-04**
Both **duplex**; the operator can **manually transfer to the other side** if one clogs.

**Jacking oil manifold block (3.13.2.5)**
⚠️ **A device that divides the supplied oil into each bearing.** Each extraction line has a **pressure gauge and an FCV (flow control valve)**. **The FCV controls the amount of oil supplied to each extraction line.**

⚠️ **Three pressures in one system:** working **~150 bar**, alarm **60 bar**, relief **180 bar**; start-up range **100–150 bar**. From normal to relief is only **30 bar**.

`#jackingoil #JOP #reliefvalve #hysteresis`

---
---

## POST 89 — Seal oil sizishi va suyuqlik detektori

**🇺🇿 Generator korpusiga yog' kirishi — sekin va tez sizish**

**Nima uchun xavfli**
⚠️ **Seal oil drenaji to'sib qolsa — suyuq yog' va yog' bug'i (u oson kondensatsiyalanadi) generatorning ichki yuzalarida YOPISHQOQ QATLAM hosil qiladi.**
⚠️ **Keyin chang zarrachalari stator sterjeni izolyatsiyasiga yopishadi va oxir-oqibat uni shikastlashi mumkin.**
⚠️ **Izolyatsiyadagi suyuq suv izolyatsiya sifatini pasaytiradi.**

**Ikki xil sizish**
| Alarm | KKS | Ma'nosi | Harakat |
|---|---|---|---|
| **Yuqori sath alarmi** | **10MKG21CL101** (1.8 L) | ⚠️ **Generator korpusiga suyuqlikning SEKIN sizishi** | **Qulay vaqtda tekshiriladi** |
| **Yuqori-yuqori alarmi** | **10MKG21CL102** (2.0 L) | ⚠️ **TEZ sizish** | ⚠️ **DARHOL aniqlanib tuzatilishi shart, aks holda generator korpusi SUV BOSISHIDAN OLDIN to'xtatilishi kerak** |

⚠️ **Sekin sizish turning gear da seal oil va rotor aylanishining o'zaro ta'siri tufayli MUMKIN** — ya'ni bu holat kutilgan, lekin kuzatilishi kerak.

**Suyuqlik detektori uskunasi**
Ajratish klapani **10MKG21AA081** | Drenaj klapani **10MKG21AA421** | Ko'rish oynasi **10MKG21CL001** | **Sinov uchun to'ldirish porti** | Datchiklar **10MKG21CL101, 102**

⚠️ **"Sinov uchun to'ldirish porti" bor** — ya'ni detektorni suyuqlik quyib sinash mumkin. Bu yillik tekshiruvda bajarilishi kerak, aks holda datchik ishlayotganini bilmaysiz.

**Kunlik TO — seal oil (11.12.1)**
| Nima | Me'yor |
|---|---|
| **Seal oil bosimi** | ⚠️ **H2 bosimidan 0.05–0.08 MPa YUQORI** |
| **Seal oil bak sathi** | ⚠️ **Ko'rish oynasining 1/2–2/3 qismida** |
| **Yog' harorati** | ⚠️ **40–50°C** |
| **Filtr Δp** | ⚠️ **≤0.05 MPa** |

⚠️ **DIQQAT — ikki xil differensial:** 6-bobdagi alarm **<0.41 bar = 0.041 MPa**, 11-bobdagi kunlik me'yor **0.05–0.08 MPa = 0.5–0.8 bar**. Ya'ni **normal ish 0.5–0.8 bar, alarm 0.41 bar da.** Zaxira atigi **0.09 bar**.

**Vodorod sovutgich tekshiruvi (kunlik)**
• Vodorod sovutgichlarining sovutish suvi kirish/chiqish bosimi va haroratini tekshiring
• ⚠️ **Vodorod tomoniga suv sizishi bor-yo'qligini kuzating (drenaj klapanidan namuna olish orqali)**
• Me'yor: ⚠️ **vodorod tomoni drenaj namunasida SUV YO'Q**

⚠️ **Zanjir:** H2 sovutgich quvuri sizadi → suv H2 tomoniga → **H2 namligi oshadi** → shudring nuqtasi **>−25°C** → quritgich yetishmaydi → izolyatsiya buziladi. Kunlik drenaj namunasi shu zanjirning birinchi bo'g'ini.

---

**🇷🇺 Попадание масла в корпус генератора — медленная и быстрая течь**

⚠️ **При подпоре дренажа уплотняющего масла жидкое масло и легкоконденсирующиеся пары создают ЛИПКИЙ СЛОЙ на внутренних поверхностях.** ⚠️ **Пыль налипает на изоляцию стержней статора и со временем повреждает её.** ⚠️ **Влага на изоляции ухудшает её качество.**

| Сигнал | KKS | Значение | Действие |
|---|---|---|---|
| **Высокий** | **10MKG21CL101** (1.8 л) | ⚠️ **МЕДЛЕННАЯ течь** | **проверить при удобном случае** |
| **Высокий-высокий** | **10MKG21CL102** (2.0 л) | ⚠️ **БЫСТРАЯ течь** | ⚠️ **НЕМЕДЛЕННО найти и устранить, иначе останов ДО затопления корпуса** |

⚠️ **Медленная течь ВОЗМОЖНА из-за взаимодействия уплотняющего масла с вращением ротора на ВПУ.**

**Оборудование детектора** — отсечной **10MKG21AA081**, дренаж **10MKG21AA421**, смотровое стекло **10MKG21CL001**, ⚠️ **порт заполнения для проверки**, датчики **10MKG21CL101, 102**

**Ежедневно** — ⚠️ **давление уплотняющего масла ВЫШЕ давления H2 на 0.05–0.08 МПа** | ⚠️ **уровень бака 1/2–2/3 стекла** | ⚠️ **температура 40–50°C** | ⚠️ **Δp фильтра ≤0.05 МПа**

⚠️ **Два разных перепада:** сигнал главы 6 — **<0.41 бар**, норма главы 11 — **0.5–0.8 бар**. Запас всего **0.09 бар**.

**Водородные охладители (ежедневно)** — давление и температура охлаждающей воды; ⚠️ **проверка попадания воды в водородную сторону через дренаж**; норма ⚠️ **воды в пробе НЕТ**
⚠️ **Цепочка:** течь трубки → вода в H2 → **рост влажности** → точка росы **>−25°C** → осушитель не справляется → страдает изоляция.

---

**🇬🇧 Oil in the Generator Casing — slow and fast leaks**

⚠️ **If the seal oil drain is backed up, liquid oil and oil vapor (which easily condenses) create a STICKY SURFACE on the generator internal surfaces.** ⚠️ **Dirt particles then tend to cling to the insulation of the stator bar and may eventually damage it.** ⚠️ **Liquid water on the insulation will degrade the quality of the insulation.**

| Alarm | KKS | Meaning | Action |
|---|---|---|---|
| **High** | **10MKG21CL101** (1.8 L) | ⚠️ **a SLOW leak of liquid into the generator casing** | **investigate when convenient** |
| **High-high** | **10MKG21CL102** (2.0 L) | ⚠️ **a FAST leak** | ⚠️ **immediately identify and correct, or else shut the generator down PRIOR to casing flooding** |

⚠️ **A slow leak of oil is possible due to the interaction of seal oil with rotor rotation while on turning gear** — expected, but it must be watched.

**Liquid level detector hardware** — isolation valve **10MKG21AA081**, drain valve **10MKG21AA421**, sight glass **10MKG21CL001**, ⚠️ **fill port for test**, sensors **10MKG21CL101, 102**
⚠️ **There is a fill port for testing** — the detector can be proof-tested with liquid. Without doing it, you don't know the switch still works.

**Daily seal oil check (11.12.1)**
⚠️ **Seal oil pressure: 0.05–0.08 MPa higher than hydrogen pressure** | ⚠️ **Seal oil tank level: 1/2 to 2/3 of the sight glass** | ⚠️ **Oil temperature: 40–50°C** | ⚠️ **Filter ΔP ≤0.05 MPa**

⚠️ **Two different differentials:** the Chapter 6 alarm is **<0.41 bar (0.041 MPa)**, the Chapter 11 daily standard is **0.05–0.08 MPa (0.5–0.8 bar)**. Normal running is 0.5–0.8 bar and the alarm sits at 0.41 bar — only **0.09 bar** of margin.

**Hydrogen cooler check (daily)** — cooling water inlet/outlet pressure and temperature; ⚠️ **observe if there is water leakage into the hydrogen side (via drain valve sampling)**; standard ⚠️ **no water in hydrogen side drain sample**
⚠️ **The chain:** cooler tube leak → water into H2 → **humidity rises** → dew point **above −25°C** → dryer cannot keep up → insulation suffers. The daily drain sample is the first link.

`#sealoil #liquiddetector #generatorcasing #H2cooler`

---
---

## POST 90 — H2 gaz sifati me'yorlari

**🇺🇿 Vodorod sifati — sinov va harakat**

| Sinov | Chastota | Me'yor | Harakat |
|---|---|---|---|
| **H2 tozaligi** | Kuniga 1× (onlayn analizator); haftada 1× (qo'lda namuna) | ⚠️ **H2 ≥98% (hajm ulushi)**; ⚠️ **O₂ miqdori ≤1%** | ⚠️ **Tozalik <98%: vodorodni purge qiling (past tozalikdagi gazni chiqarib, yangi vodorod to'ldiring)**. ⚠️ **O₂ >1%: havo kirishini tekshiring (seal oil tizimi, klapan sizishlari); purge qilishdan OLDIN izolyatsiya qilib ta'mirlang** |
| **H2 namligi** | Kuniga 1× (onlayn shudring nuqtasi o'lchagich); oyiga 1× (laboratoriya) | ⚠️ **≤5 g/m³** (⚠️ **shudring nuqtasi ≤−25°C, 0.3 MPa vodorod bosimida**) | ⚠️ **>5 g/m³: vodorod quritgichini yoqing (quritgich ishlamasa adsorbentni almashtiring); vodorod tizimidan kondensatsiyalangan suvni chiqaring** |

⚠️ **Tozalik me'yorlari uch xil:** kunlik TO **≥98%**, alarm **<95%**, LL alarm **<90%**, to'ldirish **>99%** gacha davom etadi, 10.11 da "odatda **≥96%**". **Amaliy me'yor — 98%, va to'ldirish 99% gacha.**

**XAVFSIZLIK — vodorod (11.12.3.1)**
⚠️ **Portlashning oldini olish: vodorod tizimining 15 METR radiusida ochiq alanga, uchqun yoki yuqori haroratli obyektlar BO'LMASLIGI kerak.** Portlashga chidamli elektr uskunalar (chiroq, detektor) va **uchqun bermaydigan kalitlar** ishlatiladi.
⚠️ **Sizish avariyasi: vodorod konsentratsiyasi >4% (quyi portlash chegarasi) bo'lsa — portlashga chidamli ventilyatorlarni yoqing, vodorod ta'minotini uzing, ta'mirchi bo'lmagan xodimlarni chiqaring.** ⚠️ **Konsentratsiya >74% (yuqori portlash chegarasi) bo'lsa CO2 bilan suyultiring.**
⚠️ **O't o'chirish: generator yonida CO2 yoki quruq kukunli o'chirgichlar. SUV ISHLATMANG — suv vodorodni tarqatishi mumkin.** ⚠️ **Vodorod yonsa — avval vodorod manbasini uzing, keyin o't o'chiring.**

**XAVFSIZLIK — CO2 (11.12.3.2)**
⚠️ **Bo'g'ilishning oldini olish: CO2 saqlash va almashtirish joylari yaxshi shamollatilishi kerak (havo almashinuvi ≥3 marta/soat).** ⚠️ **CO2 konsentratsiya detektorlarini o'rnating — ≥1.5% hajm ulushida alarm.**
⚠️ **Ballonlarni tashish: ballon aravachasidan foydalaning (sudramang, tashlamang). Klapanlarni SEKIN oching — quvurda "suyuq zarba"ning oldini olish uchun.**
⚠️ **Bo'sh CO2 ballonlari "Bo'sh" deb belgilanib yetkazib beruvchiga qaytarilishi shart; tashlab yubormang va boshqa gaz uchun qayta ishlatmang.**

**EHTIYOT CHORALARI (11.12.4)**
1. ⚠️ **Gaz almashtirish taqiqi: vodorodni havo bilan (yoki teskarisini) TO'G'RIDAN-TO'G'RI almashtirmang — CO2 oraliq muhit sifatida ISHLATILISHI SHART** (Havo→CO2→H₂ yoki H₂→CO2→Havo), vodorod-havo portlovchi aralashmasining oldini olish uchun
2. ⚠️ **Bosim operatsiyasi: vodorod bosimini sozlaganda TEZ o'zgarishlardan qoching — tezlik ≤0.05 MPa/soat**, generator zichlashlari yoki izolyatsiyasining shikastlanishining oldini olish uchun
3. ⚠️ **Asbob aniqligi: onlayn vodorod tozaligi va namlik analizatorlarini HAR OY kalibrlang** (standart gaz bilan)
4. ⚠️ **Sovuq havoda TO: past harorat sharoitida (<0°C) CO2 quvurlarini izolyatsiya qiling — CO2 ning qotib qolishi (quruq muz) va quvur tiqilishining oldini olish uchun; kerak bo'lsa elektr tracing ishlating**

⚠️ **0.05 MPa/soat** — bu **10.11 dagi 0.02 MPa/min** dan farq qiladi. 0.02 MPa/min = 1.2 MPa/soat. **11.12.4 dagi 0.05 MPa/soat ancha qat'iyroq** — normal ekspluatatsiya uchun, 0.02 MPa/min esa ta'mirdan keyin qayta to'ldirish uchun.

---

**🇷🇺 Качество водорода — нормы и действия**

| Показатель | Частота | Норма | Действие |
|---|---|---|---|
| **Чистота H2** | 1×/сут онлайн; 1×/нед вручную | ⚠️ **≥98%**; ⚠️ **O₂ ≤1%** | ⚠️ **<98%: продувка с подпиткой**; ⚠️ **O₂ >1%: искать подсос (уплотняющее масло, арматура), изолировать и ремонтировать ДО продувки** |
| **Влажность H2** | 1×/сут онлайн; 1×/мес лаборатория | ⚠️ **≤5 г/м³** (⚠️ **точка росы ≤−25°C при 0.3 МПа**) | ⚠️ **>5 г/м³: включить осушитель (при отказе — заменить адсорбент); слить конденсат** |

⚠️ **Нормы чистоты расходятся:** ТО **≥98%**, сигнал **<95%**, LL **<90%**, подпитка до **>99%**, п. 10.11 — **≥96%**. **Рабочая норма 98%, подпитка до 99%.**

**БЕЗОПАСНОСТЬ H2** — ⚠️ **в радиусе 15 МЕТРОВ ни огня, ни искр, ни горячих предметов**; взрывозащищённое оборудование и **неискрящий инструмент** | ⚠️ **при концентрации >4% (НКПВ) — взрывозащищённая вентиляция, отсечка водорода, эвакуация**; ⚠️ **>74% (ВКПВ) — разбавление CO2** | ⚠️ **тушение CO2 или порошком, ВОДОЙ НЕЛЬЗЯ**; ⚠️ **сначала отсечь источник, потом тушить**

**БЕЗОПАСНОСТЬ CO2** — ⚠️ **вентиляция ≥3 обменов/час**, ⚠️ **сигнализация при ≥1.5%** | ⚠️ **перевозка тележкой, клапаны открывать МЕДЛЕННО против «жидкостного удара»** | ⚠️ **пустые баллоны маркировать «Пустой» и возвращать поставщику**

**МЕРЫ ПРЕДОСТОРОЖНОСТИ** — ⚠️ **никогда напрямую воздух↔H₂, только через CO2** | ⚠️ **скорость изменения давления ≤0.05 МПа/ч** | ⚠️ **поверка анализаторов ЕЖЕМЕСЯЧНО** | ⚠️ **при <0°C изолировать трубопроводы CO2 против сухого льда, при необходимости — электрообогрев**

⚠️ **0.05 МПа/ч (эксплуатация) против 0.02 МПа/мин (заполнение после ремонта)** — первое строже.

---

**🇬🇧 Hydrogen Gas Quality — standards and actions**

| Test | Frequency | Qualified standard | Treatment |
|---|---|---|---|
| **Hydrogen purity** | Once a day (online analyzer); once a week (manual sampling) | ⚠️ **H2 ≥98% (volume fraction)**; ⚠️ **O₂ content ≤1%** | ⚠️ **Purity <98%: purge hydrogen (discharge low-purity gas, replenish new hydrogen)**; ⚠️ **O₂ >1%: check for air ingress (seal oil system, valve leaks); isolate and repair BEFORE purging** |
| **Hydrogen humidity** | Once a day (online dew point meter); once a month (laboratory test) | ⚠️ **≤5 g/m³** (⚠️ **dew point ≤−25°C at 0.3 MPa hydrogen pressure**) | ⚠️ **>5 g/m³: activate the hydrogen dryer (replace adsorbent if the dryer fails); drain condensed water from the hydrogen system** |

⚠️ **Purity figures differ across the manual:** routine maintenance **≥98%**, alarm **<95%**, LL **<90%**, replenish until **>99%**, section 10.11 says generally **≥96%**. **The working standard is 98%, replenishing to 99%.**

**HYDROGEN SAFETY (11.12.3.1)**
⚠️ **Explosion prevention: no open flames, sparks, or high-temperature objects within 15 m of the hydrogen system**; use explosion-proof electrical equipment (lights, detectors) and **non-sparking tools**
⚠️ **Leakage emergency: if hydrogen concentration >4% (lower explosive limit), activate ventilation fans (explosion-proof type), shut off hydrogen supply, and evacuate non-maintenance personnel**; ⚠️ **use CO₂ to dilute if concentration >74% (upper explosive limit)**
⚠️ **Fire fighting: equip CO₂ or dry powder extinguishers near the generator — do not use water, water may spread hydrogen**; ⚠️ **if hydrogen catches fire, first cut off the hydrogen source, then extinguish**

**CARBON DIOXIDE SAFETY (11.12.3.2)**
⚠️ **Asphyxiation prevention: CO₂ storage and replacement areas must be well-ventilated (air change ≥3 times/hour)**; ⚠️ **install CO₂ concentration detectors (alarm at ≥1.5% volume fraction)**
⚠️ **Cylinder handling: use a cylinder cart (do not drag or drop); open valves slowly to avoid "liquid hammer" in pipelines**
⚠️ **Waste disposal: empty cylinders must be labelled "Empty" and returned to suppliers; do not discard or reuse for other gases**

**PRECAUTIONS (11.12.4)**
1. ⚠️ **Gas replacement prohibition: never directly replace hydrogen with air (or vice versa) — must use CO₂ as an intermediate medium** (Air→CO₂→H₂ or H₂→CO₂→Air) to avoid hydrogen-air explosive mixtures
2. ⚠️ **Pressure operation: when adjusting hydrogen pressure, avoid rapid changes (rate ≤0.05 MPa/h)** to prevent damage to generator seals or insulation
3. ⚠️ **Instrument accuracy: calibrate online hydrogen purity and humidity analyzers monthly** using standard gas
4. ⚠️ **Cold weather maintenance: in low-temperature environments (<0°C), insulate CO₂ pipelines to prevent CO₂ solidification (dry ice) and pipeline blockage; use electric tracing if necessary**

⚠️ **0.05 MPa/h here versus 0.02 MPa/min in section 10.11** — 0.02 MPa/min equals 1.2 MPa/h, so the routine-operation limit is far stricter than the post-repair refilling limit.

`#hydrogen #gasquality #safety #explosionlimits`

---
---

## POST 91 — Control oil: davriy TO jadvali

**🇺🇿 EH tizimi — chastota bo'yicha to'liq jadval**

**KUNLIK (smenada 1 marta / 2–4 soat)**
| Tekshiruv | Me'yor |
|---|---|
| **Boshqaruv yog' bosimi** | Ish bosimi nominal diapazonda (**165 bar**); ⚠️ **to'satdan tebranish yo'q — tebranish amplitudasi ≤±5 bar** |
| **Boshqaruv yog' harorati** | ⚠️ **35–45°C**; ⚠️ **g'ayritabiiy ko'tarilish yo'q — harorat o'zgarishi soatiga ≤5°C** |
| **Bak sathi** | "MIN" va "MAX" belgilari orasida; ⚠️ **sezilarli tushish yo'q — kuniga ≤5 mm** (normal sarfdan tashqari) |
| **Yog' sifati (vizual)** | Tiniq va shaffof, loyqasiz, rang o'zgarishisiz (to'q jigarrang/qora), ko'rinadigan cho'kmasiz; ⚠️ **g'ayritabiiy hid yo'q (oksidlanishdan kuygan hid)** |
| **Shovqin va tebranish** | Nasos silliq ishlaydi, g'ijirlash/chiyillash yo'q; ⚠️ **nasos asosi, quvur birikmasi va klapan korpusida tebranish amplitudasi ≤0.1 mm** |
| **Alarm va himoya** | Soxta alarmlar yo'q; avariya to'xtatish klapani va xavfsizlik klapani normal ishga tushadi (**davriy sinaladi, kunlik emas**) |

**DAVRIY TO**
| Sikl | Ish | Talab |
|---|---|---|
| **Haftalik** | **Yog' filtri Δp** | So'rish/qaytish filtrining Δp manometrini tekshiring; ⚠️ **Δp chegaradan oshsa (≥5 bar) — elementni DARHOL almashtiring** |
| **Oylik** | **Yog' namunasi (dastlabki sinov)** | Bakning namuna klapanidan namuna oling (⚠️ **namunadan oldin klapanni tozalang**); **qovushqoqlik** (portativ viskozimetr) va **namlikni** (namlik o'lchagich) sinang; ⚠️ **dastlabki spetsifikatsiya bilan solishtiring: qovushqoqlik chetlanishi ≤±10%, namlik ≤0.1%** |
| **Choraklik** | **Sovutish tizimi** | Sovutgichni tozalang: havo bilan sovutiladigan uchun **qanot yuzasidan changni siqilgan havo (bosim ≤0.6 MPa) yoki cho'tka bilan olib tashlang**; ventilyator podshipnigi moylanishini tekshiring (kerak bo'lsa **litiy asosli moy** qo'shing) |
| **Yarim yillik** | **Klapan va aktuator** | Rostlash, xavfsizlik va solenoid klapanlarining zichligini tekshiring: **shtok zichlashida yog' sizishi yo'q**; klapanni **qo'lda ochib-yopib** moslashuvchanligini sinang; ⚠️ **xavfsizlik klapanining sozlama bosimini tizim nominal bosimiga QAYTA KALIBRLANG** |
| **Yillik** | **To'liq yog' tahlili va tizimni yuvish** | Namunani **professional laboratoriyaga** yuboring: **tozalik klassi, kislota qiymati, oksidlanish darajasi, metall zarrachalar miqdori**; ⚠️ **BARCHA filtrlarni (so'rish, bosim, qaytish) almashtiring** va bak ichki devorini tekshiring (cho'kmani toza latta bilan oling) |
| **2–3 yil** | **Nasos va dvigatel** | Nasosni oching: **yeyilgan tishli g'ildirak/plastina, eskirgan zichlash va podshipniklarni almashtiring**; yig'ib bosim va sarfni sinang; ⚠️ **dvigatel izolyatsiya qarshiligini tekshiring (megommetr bilan ≥0.5 MΩ)** va podshipnik moyini almashtiring |

**EHTIYOT CHORALARI (11.8.3)**
1. ⚠️ **XAVFSIZLIK BIRINCHI: TO dan oldin yog' nasosini o'chiring (BUG' TURBINASI TO'XTAGAN HOLATDA BO'LISHI SHART), quvvatni uzing va tizim bosimini tushiring (xavfsizlik klapanini oching)** — yog' otilishi yoki qism harakatlanishining oldini olish uchun
2. ⚠️ **IFLOSLANISHNING OLDINI OLISH: yangi yog' tizim spetsifikatsiyasiga javob berishi va quyishdan OLDIN FILTRLANISHI shart (tozalik ≥NAS 6)**
3. **QAYD YURITISH:** TO jurnalini yuriting — tekshiruv ma'lumotlari, qism almashtirish sanalari, yog' tahlili natijalari
4. ⚠️ **AVARIYAGA TAYYORGARLIK: ehtiyot qismlar (filtr elementlari, zichlashlar, yog' namunalari) va asboblar (manometr, viskozimetr) zaxirada bo'lsin**

⚠️ **Filtr Δp uchun ikki raqam:** kunlik/haftalik **≥5 bar** (11.8.2) — bu almashtirish nuqtasi; 6-bobdagi alarm **supply filtr 8 bar, conditioning va polishing 5 bar**. Ya'ni supply filtr alarmi kechroq keladi.

---

**🇷🇺 Система ОГ — полный график ТО**

**ЕЖЕДНЕВНО (1×/смена, 2–4 ч)** — давление (**165 бар**, ⚠️ **колебания ≤±5 бар**) | температура ⚠️ **35–45°C**, ⚠️ **изменение ≤5°C/ч** | уровень между MIN и MAX, ⚠️ **падение ≤5 мм/сут** | вид: прозрачное, без потемнения и осадка, ⚠️ **без запаха гари** | шум и ⚠️ **вибрация ≤0.1 мм** | сигнализация без ложных срабатываний

**Еженедельно** — ⚠️ **Δp фильтра: при ≥5 бар НЕМЕДЛЕННАЯ замена элемента**
**Ежемесячно** — проба из бака (⚠️ **клапан очистить перед отбором**), вязкость и влага, ⚠️ **отклонение вязкости ≤±10%, влага ≤0.1%**
**Ежеквартально** — чистка охладителя: ⚠️ **сжатый воздух ≤0.6 МПа** или щётка; смазка подшипника вентилятора **литиевой смазкой**
**Раз в полгода** — плотность клапанов, **ручная проверка хода**, ⚠️ **ПЕРЕКАЛИБРОВКА предохранительного клапана на номинал системы**
**Ежегодно** — ⚠️ **лабораторный анализ: класс чистоты, кислотное число, степень окисления, металлические частицы**; ⚠️ **замена ВСЕХ фильтров**, осмотр внутренней стенки бака
**Раз в 2–3 года** — разборка насоса, замена изношенных шестерён/пластин, уплотнений, подшипников; ⚠️ **изоляция двигателя ≥0.5 МОм**

**МЕРЫ** — ⚠️ **до работ остановить насос (ТУРБИНА ДОЛЖНА БЫТЬ ОСТАНОВЛЕНА), снять питание, сбросить давление** | ⚠️ **новое масло фильтровать до ≥NAS 6 ПЕРЕД заливкой** | журнал ТО | ⚠️ **запас элементов, уплотнений и приборов**

⚠️ **Два числа по Δp:** замена при **≥5 бар**, а сигналы главы 6 — **8 бар** для фильтра подачи и **5 бар** для остальных.

---

**🇬🇧 Control Oil System — full maintenance schedule**

**DAILY (once per shift / 2–4 hours)**
Control oil pressure within rated range (**165 bar**), ⚠️ **no sudden fluctuations, amplitude ≤±5 bar** | Temperature ⚠️ **35–45°C**, ⚠️ **no abnormal rise, change ≤5°C per hour** | Tank level between "MIN" and "MAX", ⚠️ **no obvious drop, ≤5 mm per day** excluding normal consumption | Oil quality visual: clear and transparent, no turbidity or discolouration (dark brown/black), no visible sediment, ⚠️ **no abnormal odours such as burnt smell from oxidation** | Noise and vibration: pump runs smoothly with no grinding or squealing, ⚠️ **vibration amplitude ≤0.1 mm** at pump base, pipeline joints and valve bodies | Alarm and protection: no false alarms; emergency stop valve and relief valve trigger normally (**tested periodically, not daily**)

**PERIODIC**
**Weekly** — oil filter Δp check: ⚠️ **if Δp exceeds the limit (≥5 bar), replace the element immediately** to avoid oil flow resistance
**Monthly** — oil sample from the tank sampling valve (⚠️ **clean the valve before sampling**); test viscosity (portable viscometer) and water content (moisture meter); ⚠️ **compare with initial specifications: viscosity deviation ≤±10%, water content ≤0.1%**
**Quarterly** — cooling system: for air-cooled coolers ⚠️ **remove dust from the fin surface with compressed air (pressure ≤0.6 MPa) or a brush**; inspect fan bearing lubrication (add **lithium-based grease** if necessary) or pump seal
**Half-yearly** — valve and actuator: check tightness of regulating, relief and solenoid valves, **no oil leakage at the stem seal**; **manually test opening/closing flexibility**; ⚠️ **recalibrate the relief valve set pressure to match the system rated pressure**
**Yearly** — comprehensive oil analysis and system flushing: send samples to a professional laboratory for **cleanliness class, acid value, oxidation degree, metal particle content**; ⚠️ **replace all oil filters (suction, pressure, return)** and inspect the tank inner wall
**2–3 years** — pump and motor: disassemble to inspect internals, **replace worn gears/vanes, aged seals and bearings**; reassemble and test pressure and flow; ⚠️ **inspect motor insulation resistance (≥0.5 MΩ with a megohmmeter)** and replace motor bearing grease

**NOTES (11.8.3)**
⚠️ **Safety first: before maintenance, shut down the oil pump (THE STEAM TURBINE UNIT SHOULD BE IN SHUTDOWN STATE), cut off the power supply, and release system pressure (open the relief valve)** to avoid oil spray or component movement | ⚠️ **Contamination prevention: new oil must meet system specifications and be filtered (cleanliness ≥NAS 6) BEFORE injection** | Record-keeping: maintenance log with inspection data, replacement dates and oil analysis results | ⚠️ **Emergency preparedness: stock spare filter elements, seals, oil samples and tools (pressure gauge, viscometer)**

⚠️ **Two Δp figures:** replacement at **≥5 bar** here, while Chapter 6 alarms are **8 bar** for the supply filter and **5 bar** for conditioning and polishing filters.

`#EHoil #maintenance #schedule #NAS6`

---
---

## POST 92 — Lube oil TO va filtr almashtirish

**🇺🇿 Lube oil tizimi — chastota va protsedura**

**KUNLIK TEKSHIRUV (11.9.1)**
| Nima | Qanday |
|---|---|
| **Bak sathi** | Bak ko'rish oynasidan kuzating va **sath transmitteri bilan tasdiqlang**; ⚠️ **kunlik sath ma'lumotini QO'LDA qayd eting** |
| **Yog' bosimi** | Asosiy nasos chiqish bosimi va **podshipnik kirish yog' bosimi**; sezilarli tebranishsiz barqarormi |
| **Yog' harorati** | Bakdagi harorat va sovutgichning kirish/chiqish harorati; ⚠️ **sovutgichning sovutish suvi klapani ochilishi OQILONAMI** |
| **Nasos ishi** | ⚠️ **Nasos korpusi va dvigatel korpusiga QO'L BILAN TEGIB haroratni tekshiring**; shovqinni tinglang (g'ijirlash/chiyillash yo'q); muftaning ekssentrisitetsiz silliq aylanishini kuzating |
| **Sizish** | ⚠️ **Asosiy e'tibor: nasos zichlashlari, quvur birikmalari, klapan salniklari va val zichlashlari**; yerda yog' bor-yo'qligi va **bak nafas olgichidan yog' toshishi** |
| **Filtr Δp** | Δp qiymatini o'qing; ⚠️ **Δp o'zgarish TENDENSIYASINI qayd eting** |

**MUNTAZAM YOG' SIFATI SINOVI (11.9.2)**
| Ko'rsatkich | Chastota |
|---|---|
| **Kinematik qovushqoqlik (40°C)** | ⚠️ **Oyiga 1 marta** |
| **Namlik miqdori** | ⚠️ **Haftada 1 marta (oddiy sinov); oyiga 1 marta (laboratoriya)** |
| **Zarrachalar sanog'i** | ⚠️ **Oyiga 1 marta** |
| **Umumiy kislota soni (TAN)** | ⚠️ **3 oyda 1 marta** |

**NASOS TO (11.9.3)**
| Ish | Chastota |
|---|---|
| ⚠️ **Zaxira nasos avto-o'tish sinovi** | **Haftada 1 marta** |
| **Nasos podshipnigi moylash** | **Oyiga 1 marta** |
| **Nasos zichlashini tekshirish** | ⚠️ **2 HAFTADA 1 marta** |

**SOVUTGICH TO (11.9.4)**
• **Kunlik:** sovutgichning sovutish suvi kirish/chiqish bosimini tekshirib, suv oqimi silliqligini ta'minlang
• ⚠️ **HAR 2 HAFTADA: sovutgichning yuqori vent klapanini ochib HAVONI CHIQARING** (havo tiqilishi sovutish samaradorligiga ta'sir qilmasligi uchun) — **uzluksiz suv oqimi chiqguncha**, keyin klapanni yoping
• ⚠️ **HAR 3 OYDA: tashqi yuzadagi chang va axlatni tozalang (siqilgan havo bilan puflang); sovutish samaradorligi pasaysa quvur bog'lamini ochib tozalang — 10% LIMON KISLOTASI eritmasi bilan cho'kmani oling, keyin toza suv bilan yuving**

**FILTR TO (11.9.5)**
⚠️ **Element almashtirish yoki tozalash: Δp 0.05 MPa DAN OSHGANDA DARHOL, va 3 OYDAN KECHIKMASDAN** (Δp chegara ichida bo'lsa ham element eskirishini oldini olish uchun muntazam almashtiring)

**Almashtirish protsedurasi — 5 qadam**
① **Zaxira filtrga o'ting** → ② **Almashtiriladigan filtrning kirish/chiqish klapanlarini yoping** → ③ **Bosimni tushiring va elementni oling** → ④ **Yangi elementni o'rnating (⚠️ zichlash yuzasida axlat yo'qligiga ishonch hosil qiling)** → ⑤ **Havoni chiqaring va zaxira holatiga qaytaring**

⚠️ **Olingan elementni tekshiring:**
• **Metall qipiqlar bo'lsa** → ⚠️ **nasos/podshipnik yeyilishini tekshiring**
• **Ortiqcha shlam bo'lsa** → ⚠️ **bak tozalashni kuchaytiring**

**ASBOB KALIBRLASH (11.9.6)**
| Asbob | Chastota | Talab |
|---|---|---|
| **Yog' manometri, termometri** | **3 oyda 1** | ⚠️ **Standart kalibrator bilan; xato ≤±2%** (masalan standart bosim 0.2 MPa bo'lganda ko'rsatkich **0.196–0.204 MPa**) |
| **Sath transmitteri** | **6 oyda 1** | ⚠️ **Qo'lda yog' qo'shib/chiqarib tekshiring; chetlanish 5% dan oshsa sozlang** |
| **Bosim relesi (past yog' bosimi alarm/to'xtatish)** | ⚠️ **Oyiga 1** | ⚠️ **Past bosimni simulyatsiya qiling (bosimni SEKIN tushiring) va alarm hamda to'xtatish ishga tushish bosimlarining aniqligini tasdiqlang** |

**INTERLOK SINOVI**
⚠️ **Haftalik: "past yog' bosimi zaxira nasos ulanishi" funksiyasini sinang** — asosiy nasos chiqish bosimini sozlama nuqtasigacha tushiring, zaxira nasos avtomatik ishga tushishi kerak

**MUHIT VA XAVFSIZLIK (11.9.7)**
• ⚠️ **Kunlik: tizim atrofidagi yerni tozalang** (yog' dog'lari va axlat yo'q) — bakka chang kirmasligi uchun; TO paytida **bak lyugini yoping**
• ⚠️ **Haftalik: bak yonidagi o't o'chirgichlarni tekshiring** (normal bosim va amal qilish muddati ichida); ⚠️ **turbinaning yuqori haroratli qismlari (korpus) issiqlik izolyatsiya qatlami butunligini tasdiqlang** — sizib chiqqan yog' yuqori harorat bilan aloqaga kirmasligi uchun

⚠️ **Filtr Δp uchun uch raqam:** lube oil **0.05 MPa = 0.5 bar** (11.9.5 almashtirish), 6-bobdagi alarm **0.5 bar** — bir xil. Control oil esa **5 bar**. O'n barobar farq — tizimlar bosimi ham o'n barobar farq qiladi.

---

**🇷🇺 Маслосистема — частоты и процедуры**

**ЕЖЕДНЕВНО** — уровень (⚠️ **запись ВРУЧНУЮ**) | давление насоса и **на входе подшипников** | температура бака и охладителя, ⚠️ **разумность открытия задвижки охлаждающей воды** | ⚠️ **проверка нагрева НА ОЩУПЬ**, шум, плавность муфты | ⚠️ **течи: уплотнения насоса, соединения, сальники, уплотнения вала; масло на полу; выброс через сапун** | ⚠️ **ТРЕНД Δp фильтра**

**АНАЛИЗЫ** — вязкость **1×/мес** | ⚠️ **влага 1×/нед (экспресс), 1×/мес (лаборатория)** | счёт частиц **1×/мес** | ⚠️ **кислотное число 1× в 3 мес**
**НАСОСЫ** — ⚠️ **проверка АВР 1×/нед** | смазка **1×/мес** | ⚠️ **уплотнения 1 раз в 2 НЕДЕЛИ**
**ОХЛАДИТЕЛЬ** — давление воды ежедневно | ⚠️ **КАЖДЫЕ 2 НЕДЕЛИ выпуск воздуха через верхний воздушник до сплошной струи** | ⚠️ **КАЖДЫЕ 3 МЕСЯЦА чистка снаружи, при падении эффективности — разборка и промывка 10% ЛИМОННОЙ КИСЛОТОЙ**
**ФИЛЬТР** — ⚠️ **замена при Δp >0.05 МПа НЕМЕДЛЕННО и не позже 3 МЕСЯЦЕВ**
Порядок: ① перейти на резервный → ② закрыть задвижки → ③ сбросить давление, снять элемент → ④ установить новый (⚠️ **чистая уплотнительная поверхность**) → ⑤ выпустить воздух и в резерв
⚠️ **Стружка на элементе — проверить износ насоса/подшипников; шлам — усилить чистку бака**

**ПОВЕРКА** — манометры и термометры **1× в 3 мес**, ⚠️ **погрешность ≤±2%** | уровнемер **1× в 6 мес**, ⚠️ **отклонение >5% — настройка** | ⚠️ **реле давления ЕЖЕМЕСЯЧНО, медленным снижением давления**
⚠️ **Еженедельно — испытание АВР по низкому давлению**

**СРЕДА** — ⚠️ **ежедневная уборка, лючок бака закрыт при работах** | ⚠️ **еженедельно огнетушители и целостность изоляции горячих частей**

---

**🇬🇧 Lube Oil System — frequencies and procedures**

**DAILY INSPECTION (11.9.1)**
Tank level: observe through the sight glass and **verify with the level transmitter**; ⚠️ **manually record oil level data daily** | Pressure: main pump outlet and **bearing inlet oil pressure**, stable without obvious fluctuations | Temperature: tank and cooler inlet/outlet; ⚠️ **confirm the cooler cooling water valve opening is reasonable** | Pump operation: ⚠️ **touch the pump body and motor housing to check temperature**, listen for noise, observe coupling rotates smoothly without eccentricity | Leakage: ⚠️ **focus on pump seals, pipeline joints, valve packing and shaft seals**; oil on the ground and **oil overflowing from the tank breather** | Filter Δp: read the value, ⚠️ **record the differential pressure change trend**

**REGULAR OIL QUALITY TESTING (11.9.2)**
Kinematic viscosity (40°C) ⚠️ **once a month** | Water content ⚠️ **once a week (simple test); once a month (laboratory)** | Particle count ⚠️ **once a month** | Total Acid Number (TAN) ⚠️ **once every 3 months**

**PUMP MAINTENANCE (11.9.3)** — ⚠️ **standby pump auto-switch test once a week** | pump bearing lubrication once a month | ⚠️ **pump seal check once every 2 weeks**

**COOLER MAINTENANCE (11.9.4)**
Daily: check cooling water inlet/outlet pressure for smooth flow | ⚠️ **Every 2 weeks: open the cooler vent valve (top) to discharge air** (prevent air blockage affecting cooling efficiency) **until continuous water flow is discharged**, then close | ⚠️ **Every 3 months: clean dust and debris from the outer surface (blow with compressed air); if cooling efficiency decreases, disassemble and clean the tube bundle — descale with 10% CITRIC ACID solution, then rinse with clean water**

**FILTER MAINTENANCE (11.9.5)**
⚠️ **Replace or clean the element immediately when Δp exceeds 0.05 MPa, and no later than 3 months** (replace regularly to prevent element ageing even if Δp is within limit)
Procedure: ① **switch to the standby filter** → ② **close the inlet/outlet valves of the filter to be replaced** → ③ **relieve pressure and remove the element** → ④ **install a new element (⚠️ ensure no debris on the sealing surface)** → ⑤ **vent and restore the standby state**
⚠️ **Inspect the removed element:** metal debris → **check for pump/bearing wear**; excessive sludge → **strengthen tank cleaning**

**INSTRUMENT CALIBRATION (11.9.6)**
Oil pressure and temperature gauges: **once every 3 months**, ⚠️ **error ≤±2%** (at 0.2 MPa standard, display should read **0.196–0.204 MPa**) | Level transmitter: **once every 6 months**, ⚠️ **manually add/drain oil to verify; adjust if deviation exceeds 5%** | Pressure switch (low oil pressure alarm/shutdown): ⚠️ **once a month**, ⚠️ **simulate low oil pressure by reducing pressure slowly and confirm alarm and shutdown trigger pressures are accurate**

**INTERLOCK TESTING** — ⚠️ **weekly: test the "low oil pressure standby pump linkage"** by reducing main pump outlet pressure to the set point; the standby pump should start automatically

**ENVIRONMENT AND SAFETY (11.9.7)**
⚠️ **Daily: clean the ground around the system** (no oil stains or debris) to prevent dust entering the tank; **cover the tank manhole during maintenance** | ⚠️ **Weekly: check fire extinguishers near the tank** (normal pressure, within validity); ⚠️ **confirm the thermal insulation layer of the turbine's high-temperature components (casing) is intact** to avoid leaked oil contacting high temperatures

⚠️ **Three filter Δp figures:** lube oil **0.05 MPa = 0.5 bar** for replacement, matching the Chapter 6 alarm at **0.5 bar**; control oil is **5 bar**. Ten times apart — as are the two system pressures.

`#luboil #maintenance #filters #calibration`

---
---

## POST 93 — Stator suvi: nasos, sovutgich, smola

**🇺🇿 Stator suvi tizimi — TO jadvali**

**NASOS BOSHQARUVI (11.13.3)**
| Ish | Chastota | Talab |
|---|---|---|
| **Nasos ish holati** | **Kunlik** | ⚠️ **Nasos korpusi/dvigatel haroratiga QO'L BILAN teging (≤70°C)**; shovqinni tinglang (g'ijirlash/chiyillash yo'q; ⚠️ **≤85 dB**); ⚠️ **mufta tebranishini tekshiring (amplituda ≤0.05 mm)** |
| **Zaxira nasos avto-o'tish sinovi** | **Haftalik** | ⚠️ **Asosiy nasos nosozligini simulyatsiya qiling (masalan asosiy nasos quvvatini uzing); zaxira nasos 5 SEKUND ICHIDA ishga tushishini tasdiqlang va bosim/sarf tiklanish vaqtini qayd eting** |
| **Podshipnik moylash** | **Oylik** | Dvigatel TO qo'llanmasi bo'yicha **litiy asosli moy** qo'shing; ⚠️ **HAR 6 OYDA moyni almashtiring** |
| **Zichlashni tekshirish** | **Oylik** | ⚠️ **Mexanik zichlash: ko'zga ko'rinadigan tomchi yo'q (ozgina namlik ruxsat etiladi)** |

**SOVUTGICH BOSHQARUVI (11.13.4)**
| Ish | Chastota | Talab |
|---|---|---|
| **Issiqlik almashinuv samaradorligi** | **Haftalik** | Sovutish suvining kirish-chiqish harorat farqini hisoblang; sovutish muhiti ta'minoti yetarliligini tekshiring |
| **Quvur tozalash** | ⚠️ **Har 3 oyda yoki samaradorlikka qarab** | ⚠️ **Suv bilan sovutiladigan uchun: 10% LIMON KISLOTASI eritmasi bilan cho'kmani oling (2 SOAT sirkulyatsiya), keyin DEMINERALLASHTIRILGAN SUV bilan yuving** |
| **Sizishni tekshirish** | ⚠️ **Har oy** | ⚠️ **Sovutish muhiti stator suvi tizimiga kiryaptimi (suv sifatini aralashmalarga sinang)** |

**ION ALMASHTIRGICH BOSHQARUVI (11.13.5)**
| Ish | Chastota | Talab |
|---|---|---|
| **Smola holati** | **Haftalik** | ⚠️ **Smola rangini kuzating: KATION smola — OCH SARIQ; ANION smola — OCH JIGARRANG**; ⚠️ **smola parchalanishini tekshiring (drenaj suvida kukunsimon smola yo'q)** |
| **Smola regeneratsiyasi** | ⚠️ **O'tkazuvchanlik >0.5 μS/sm bo'lganda** | ⚠️ **Kation almashtirgichni 5% HCl eritmasi bilan; anion almashtirgichni 4% NaOH eritmasi bilan regeneratsiya qiling**; ⚠️ **chiqish o'tkazuvchanligi ≤0.1 μS/sm bo'lguncha deminerallashtirilgan suv bilan yuving** |
| **Smolani almashtirish** | ⚠️ **Har 3–5 yilda** | Eski smolani chiqaring; almashtirgich bakini tozalang; yangi smola bilan to'ldiring |

⚠️ **Smola muddati bo'yicha ikki raqam:** 4.3.3 da "loyihaviy muddat **~2 yil**", 11.13.5 da "almashtirish **har 3–5 yilda**". **2 yil — ishlab chiqaruvchining loyihaviy kafolati, 3–5 yil — amaliy almashtirish sikli.** Haqiqiy muddatni o'tkazuvchanlik tendensiyasi belgilaydi.

**Yuqori kislorodli tizim — nima uchun (11.13.2)**
⚠️ **Bu kislorod darajasi stator o'ramining ICHKI YUZALARIDA mustahkam, yopishqoq va BARQAROR MIS OKSIDI (CuO) PLYONKASINI hosil qilishga yordam beradi. Plyonka misni EROZIYA va ORTIQCHA KORROZIYADAN himoya qiladi.**

⚠️ **Regeneratsiya nuqtasi (0.5 μS/sm) me'yor bilan BIR XIL.** Ya'ni me'yorga yetganda regeneratsiya boshlanadi, oshguncha kutilmaydi. 6-bobdagi HH alarm **9.9 μS/sm** — bu allaqachon 20 barobar yuqori.

⚠️ **Zaxira nasos 5 sekund ichida ishga tushishi shart.** Stator suvi sarfi **54.1 m³/s** da ST trip bo'ladi, va trip 15 sekund kechikish bilan. Ya'ni zaxira nasos trip'dan oldin ishga tushishi uchun 5 sekundlik talab qo'yilgan.

---

**🇷🇺 Статорная вода — график ТО**

**НАСОСЫ** — ежедневно: ⚠️ **температура НА ОЩУПЬ ≤70°C**, шум ⚠️ **≤85 дБ**, ⚠️ **вибрация муфты ≤0.05 мм** | еженедельно: ⚠️ **имитация отказа, резервный пускается ЗА 5 СЕКУНД** | ежемесячно: **литиевая смазка**, ⚠️ **замена смазки каждые 6 месяцев** | ежемесячно: ⚠️ **механическое уплотнение без видимой капели (лёгкая влажность допустима)**

**ОХЛАДИТЕЛИ** — еженедельно перепад и достаточность среды | ⚠️ **раз в 3 месяца: 10% ЛИМОННАЯ КИСЛОТА, циркуляция 2 ЧАСА, промывка ОБЕССОЛЕННОЙ ВОДОЙ** | ⚠️ **ежемесячно проверка на попадание охлаждающей среды в контур статорной воды**

**ИОНООБМЕННИК** — еженедельно: ⚠️ **цвет смолы: катионит СВЕТЛО-ЖЁЛТЫЙ, анионит СВЕТЛО-КОРИЧНЕВЫЙ**, ⚠️ **нет порошка в дренаже** | ⚠️ **регенерация при проводимости >0.5 мкСм/см: катионит 5% HCl, анионит 4% NaOH, отмывка до ≤0.1 мкСм/см** | ⚠️ **замена смолы раз в 3–5 лет**

⚠️ **Два срока по смоле:** проектный **~2 года** (п. 4.3.3) и практический **3–5 лет** (п. 11.13.5). Решает тренд проводимости.

⚠️ **Зачем кислород:** ⚠️ **такой уровень способствует образованию прочной, стойкой и СТАБИЛЬНОЙ плёнки ОКСИДА МЕДИ (CuO) на внутренних поверхностях обмотки, защищающей медь от ЭРОЗИИ и ИЗБЫТОЧНОЙ КОРРОЗИИ**

⚠️ **Точка регенерации совпадает с нормой (0.5 мкСм/см)** — регенерируют по достижении, а не после превышения.
⚠️ **5 секунд на пуск резервного** — потому что защита ПТ по расходу срабатывает через 15 секунд.

---

**🇬🇧 Stator Cooling Water — maintenance schedule**

**PUMP MANAGEMENT (11.13.3)**
Daily: ⚠️ **touch pump body/motor temperature (≤70°C)**; listen for noise (no grinding/squealing, ⚠️ **≤85 dB**); ⚠️ **check coupling vibration (amplitude ≤0.05 mm)**
Weekly: ⚠️ **simulate main pump failure (e.g. close main pump power); confirm the standby pump starts WITHIN 5 SECONDS and record pressure/flow recovery time**
Monthly: add **lithium-based grease** per the motor manual; ⚠️ **replace grease every 6 months**
Monthly: ⚠️ **mechanical seal — no visible dripping (allow minor wetness)**

**COOLER MANAGEMENT (11.13.4)**
Weekly: calculate cooling water inlet-outlet temperature difference; check cooling medium supply is sufficient
⚠️ **Every 3 months or based on cooling efficiency: for water-cooled coolers use 10% CITRIC ACID solution to descale (circulate for 2 HOURS), then rinse with DEMINERALIZED WATER**
⚠️ **Every month: check if cooling medium enters the stator water system (test water quality for impurities)**

**ION EXCHANGER MANAGEMENT (11.13.5)**
Weekly: ⚠️ **observe resin colour — cation resin LIGHT YELLOW, anion resin LIGHT BROWN**; ⚠️ **check for resin degradation (no powdery resin in drain water)**
⚠️ **Regenerate when conductivity >0.5 μS/cm: cation exchanger with 5% HCl solution, anion exchanger with 4% NaOH solution; rinse with demineralized water until effluent conductivity ≤0.1 μS/cm**
⚠️ **Replace resin every 3–5 years**: drain old resin, clean the exchanger tank, refill with new resin

⚠️ **Two resin lifetimes in the manual:** section 4.3.3 gives a **design life of about 2 years**; section 11.13.5 says **replace every 3–5 years**. The 2-year figure is the manufacturer's design basis; 3–5 years is the practical replacement cycle. Conductivity trend decides the real one.

**Why high oxygen (11.13.2)**
⚠️ **This level of oxygen is conducive to the formation of a tough, tenacious and STABLE CUPRIC OXIDE (CuO) FILM on the inside surfaces of the stator winding. The film protects copper from EROSION and EXCESSIVE CORROSION.**

⚠️ **The regeneration trigger (0.5 μS/cm) equals the qualified standard** — you regenerate on reaching it, not after exceeding it. The Chapter 6 HH alarm at **9.9 μS/cm** is already twenty times higher.
⚠️ **The standby pump must start within 5 seconds** because the ST flow trip acts with a 15-second delay — five seconds leaves margin before the trip.

`#statorwater #resin #citricacid #CuOfilm`

---
---

## POST 94 — Turning gear konstruksiyasi

**🇺🇿 Turning gear — materiallar va tuzilish**

**Vazifasi**
⚠️ **Qizdirish yoki sovutish davomida turbina rotorini aylantirish uchun mo'ljallangan mexanik qurilma.** O'zining elektr dvigateli bilan yuritiladi, dvigatel turning gear tepasiga o'rnatilgan. ⚠️ **Ulanish va ajralish GIDRAVLIK SERVOMOTOR bilan boshqariladigan ROKER ARM orqali ta'minlanadi.**

**Korpus (3.14.2.1)**
• ⚠️ **Ikki qismli, CHO'YAN GG25 dan quyilgan**
• **Pastki qismida** reduktorni fundamentga mahkamlash uchun oyoqlar — **boltlar va joylashtiruvchi shtiftlar** bilan
• ⚠️ **Yuqori qismida tekshiruv qopqoqlari — konus va tsilindrik uzatmaning to'g'ri ishlashini tekshirish, hamda servomotor va roker arm pozitsiyasini sozlash imkonini beradigan joyda**
• **Ajralish yuzasi gorizontal, asosiy rotor o'qiga parallel**
• Ikkala korpus qismi **boltlar bilan ulanadi va shtiftlar bilan qotiriladi**

**Vallar va uzatma (3.14.2.2)**
• ⚠️ **Konus g'ildiraklar o'z vali bilan BIR BO'LAKDAN yasalgan**
• ⚠️ **Material: 18CrNiMo7-6, toblangan va bo'shatilgan**
• ⚠️ **Tishlar shakli: TSIKLO-PALLOID**
• ⚠️ **Tish yon yuzalari SHLIFLANMAGAN — ularning yakuniy shakli YUKLAMA OSTIDAGI DASTLABKI DAQIQALARDA hosil bo'ladi**
• **Birinchi konus g'ildirakda** dvigatel valini ulash uchun **teshik**; **ikkinchisida** planetar reduktorning quyosh g'ildiragini ulash uchun **ichki shliplar**

**Planetar uzatma**
• Tarkibi: **quyosh g'ildiragi, sayyoralar, vodilo va tashqi halqa**
• Quyosh g'ildiragi konus g'ildirak bilan **shliplar orqali** ulangan
• ⚠️ **Quyosh g'ildiragi SHARIKLI PODSHIPNIK bilan tayanadi. Bu podshipnik quyosh g'ildiragini O'Q BO'YICHA TO'LIQ va RADIAL YO'NALISHDA QISMAN tayanaydi — quvvatni BARCHA SAYYORALAR ORASIDA TAQSIMLASH imkonini berish uchun**
• ⚠️ **Quyosh g'ildiragi QO'L RICHAGINI ulash uchun ham moslashtirilgan**
• **Quyosh g'ildiragi materiali: 18CrNiMo7-6**, toblangan va bo'shatilgan, ⚠️ **tish sohasi SEMENTLANGAN va TOBLANGAN**
• **Sayyoralar** ham **18CrNiMo7-6**, toblangan, tish sohasi sementlangan

⚠️ **"Tish yon yuzalari shliflanmagan"** — bu yangi turning gear dastlabki ishga tushirilganda shovqin va tebranish bo'lishi **NORMAL** ekanini anglatadi. Bir necha daqiqadan keyin tishlar bir-biriga moslashadi. Yangi o'rnatilgan turning gear da darhol xavotir olmang.

⚠️ **"Quyosh g'ildiragi qo'l richagini ulash uchun moslashtirilgan"** — ya'ni turning gear ni **qo'lda aylantirish mumkin**. POST 85 dagi "silindr yong'inda kuygan bo'lsa har 30 daqiqada rotorni qo'lda 180° aylantiring" talabi aynan shu orqali bajariladi.

⚠️ **Sharikli podshipnik quvvatni sayyoralar orasida taqsimlaydi** — agar bu podshipnik yeyilsa, yuklama bir sayyoraga tushadi va uzatma tez ishdan chiqadi. Turning gear shovqini o'zgarishi shu podshipnikdan bo'lishi mumkin.

**Bog'liq raqamlar (POST 46 dan)**
Reduktor nisbati **220.7** | Tishlar **248** | Modul **5.0 mm** | Backlash ⚠️ **0.4–0.5 mm** | Nominal moment **63 350 Nm** | Maksimal **68 859 Nm** | Yog' **ISO VG32, 35–60°C, 1–2 barg, 30 l/min**

---

**🇷🇺 ВПУ — материалы и устройство**

⚠️ **Механическое устройство для проворота ротора при прогреве и расхолаживании**, с собственным двигателем сверху; ⚠️ **сцепление и расцепление — КАЧАЮЩИМСЯ РЫЧАГОМ от ГИДРАВЛИЧЕСКОГО СЕРВОМОТОРА**

**Корпус** — ⚠️ **двухчастный, литой ЧУГУН GG25**; лапы с болтами и штифтами; ⚠️ **сверху смотровые крышки для проверки конической и цилиндрической передач и настройки сервомотора и рычага**; ⚠️ **разъём горизонтальный, параллельный оси ротора**

**Валы и передача** — ⚠️ **конические шестерни откованы ЗАОДНО с валом**, ⚠️ **материал 18CrNiMo7-6, улучшенный**, ⚠️ **зубья ЦИКЛО-ПАЛЛОИДНЫЕ**, ⚠️ **боковые поверхности НЕ ШЛИФОВАНЫ — окончательная форма получается В ПЕРВЫЕ МИНУТЫ ПОД НАГРУЗКОЙ**

**Планетарная передача** — солнечная шестерня, сателлиты, водило, эпицикл; ⚠️ **солнечная опирается на ШАРИКОПОДШИПНИК, который держит её ПОЛНОСТЬЮ ОСЕВО и ЧАСТИЧНО РАДИАЛЬНО, чтобы РАСПРЕДЕЛИТЬ МОЩНОСТЬ МЕЖДУ ВСЕМИ САТЕЛЛИТАМИ**; ⚠️ **солнечная шестерня также приспособлена под РУЧНОЙ РЫЧАГ**; материал **18CrNiMo7-6**, ⚠️ **зона зубьев ЦЕМЕНТИРОВАНА и ЗАКАЛЕНА**

⚠️ **Нешлифованные зубья** означают, что шум и вибрация при первом пуске нового ВПУ — **НОРМА**.
⚠️ **Ручной рычаг** — именно так выполняют требование «проворачивать на 180° каждые 30 минут» из POST 85.
⚠️ **Шарикоподшипник распределяет мощность между сателлитами** — его износ перегружает один сателлит и быстро разрушает передачу.

---

**🇬🇧 Turning Gear — materials and construction**

**Function**
⚠️ **A mechanical device intended for turning the turbine rotor during heating up or cooling down.** Driven by its own electric motor mounted on top. ⚠️ **Engaging and disengaging is provided by a ROCKER ARM controlled by a HYDRAULIC SERVOMOTOR.**

**Casing (3.14.2.1)**
⚠️ **Two-part housing made as cast iron GG25** | lower part has feet for fixing to the foundation with **bolts and location dowels** | ⚠️ **upper part has inspection covers, located so that it allows checking the proper work of the bevel gear and spur gear and setting the position of servomotor and rocker arm** | ⚠️ **split face horizontal, parallel to the axis of the main rotor** | both casing parts **connected by bolts and fixed by dowels**

**Shafts and gearing (3.14.2.2)**
⚠️ **Bevel gears are forged from ONE PIECE with their shaft** | ⚠️ **Material 18CrNiMo7-6, quenched and tempered** | ⚠️ **Shape of teeth is CYCLO-PALLOID** | ⚠️ **Teeth flanks are NOT GRINDED and their final shape will be achieved DURING THE FIRST MINUTES UNDER LOAD**
First bevel gear has a **boring** for the motor shaft; the second has **internal splines** for the planetary sun gear

**Planetary gear**
Sun gear, planets, carrier and annulus | sun gear connected to the bevel gear **by splines** | ⚠️ **Support of the sun gear is provided by a BALL BEARING. This bearing supports the sun gear FULLY IN AXIAL DIRECTION and PARTLY IN RADIAL DIRECTION to allow SHARING POWER BETWEEN ALL PLANETS** | ⚠️ **The sun gear is also modified for HAND LEVER CONNECTION** | Sun gear and planets **18CrNiMo7-6**, quenched and tempered, ⚠️ **tooth area carbonized and quenched**

⚠️ **"Teeth flanks are not grinded"** means noise and vibration on the first run of a new turning gear is **NORMAL** — the flanks bed in within minutes under load. Don't panic on a freshly installed unit.
⚠️ **"Modified for hand lever connection"** is how the POST 85 requirement — "manually turn the rotor 180° every 30 minutes when the cylinder is baked by fire" — is actually carried out.
⚠️ **The ball bearing shares power between the planets.** If it wears, load concentrates on one planet and the gearing fails quickly. A change in turning gear noise can start here.

**Related figures (POST 46)** — ratio **220.7** | **248** teeth | module **5.0 mm** | backlash ⚠️ **0.4–0.5 mm** | nominal torque **63,350 Nm** | max **68,859 Nm** | oil **ISO VG32, 35–60°C, 1–2 barg, 30 l/min**

`#turninggear #construction #planetary #handlever`

---
---

## POST 95 — Yordamchi va gland bug' TO me'yorlari

**🇺🇿 Bug' tizimlari — kunlik nazorat va avtomatika tekshiruvi**

**YORDAMCHI BUG' (11.5)**
Asosiy tamoyil: ⚠️ **"bosimni barqarorlashtirish, sizishning oldini olish, aralashmalarni olib tashlash, korroziyaga qarshi turish"**

*Real vaqt monitoringi (11.5.1)*
⚠️ **Kollektor bug' bosimini (0.8–1.4 MPa) va haroratini (260–320°C) HAR 1–2 SOATDA qayd eting va kuzating**

*Zichlash va sizish (11.5.2)*
• **Kunlik aylanib chiqish:** bug' quvurlari, flanetslar va payvand birikmalari
• ⚠️ **Klapan zichlashi: globe, boshqaruv va qaytmas klapanlarning salnik quticha larida sezilarli bug' sizishi bo'lmasligi kerak. Klapan shtoklari moslashuvchan harakatlanishi va YOPILGANDAN KEYIN ICHKI SIZISH BO'LMASLIGI kerak**

*Klapan va aktuator TO (11.5.3)*
• ⚠️ **Pnevmatik klapanlar uchun havo ta'minoti bosimi: 0.4–0.7 MPa**, havo ta'minot liniyalarida sizish yo'q
• ⚠️ **Elektr klapanlar uchun: dvigatel harorati ≤70°C**, g'altakda qizib ketish yoki kuyish belgilari yo'q, ⚠️ **chegara vyklyuchatellari ANIQ kalibrlangan**
• ⚠️ **Bosim avto-boshqaruvi: sovuq qayta qizdirishdan yordamchi bug' kollektoriga bosim rostlash klapani TO'LIQ ISHLAYOTGANINI va kollektorni belgilangan bosimda (0.8–1.4 MPa) ushlay olishini tasdiqlang**
• ⚠️ **Harorat avto-boshqaruvi: desuperheating suv boshqaruv klapani bosim boshqaruvidan keyingi haroratni belgilangan qiymatda (260–320°C) ushlay olishini tasdiqlang**

*Quvur va aksessuar TO (11.5.4)*
• **Izolyatsiya:** qatlam va tashqi qoplamada shikast yoki ajralish yo'q; ⚠️ **yuqori haroratli quvurlar va tayanchlar orasidagi izolyatsiya prokladkalari BUTUN — tayanchning qizib ketishdan deformatsiyalanishining oldini olish uchun**
• ⚠️ **Haftalik: tayanch va osgichlarni bo'shashish yoki korroziyaga tekshiring**; ⚠️ **kengaytirish birikmalari erkin harakatlanishi, qotib qolmasligi va deformatsiyalanmasligi, GOFRALARDA YORIQ BO'LMASLIGI kerak**
• ⚠️ **Kunlik: bug' tutgichlarining drenaji to'siqsizligini tekshiring (CHIQARISH TOVUSHI VA HARORATI bo'yicha baholanadi)** va filtr to'rlarini muntazam tozalang
• ⚠️ **Haftada 1–2 MARTA purge klapanlarini oching** — tizim aralashmalari va to'plangan suvni chiqarish uchun

**GLAND BUG' (11.6)**
*Real vaqt monitoringi (11.6.1)*
| Nima | Me'yor | Chastota |
|---|---|---|
| **HIP rotor gland bug' bosimi** | ⚠️ **28 kPa** | Har 1–2 soat |
| **HIP rotor gland bug' harorati** | Fig 11-6-1 egri chizig'i bo'yicha | Har 1–2 soat |
| **LP rotor gland bug' bosimi** | ⚠️ **28 kPa** | Har 1–2 soat |
| **LP rotor gland bug' harorati** | ⚠️ **150–180°C** | Har 1–2 soat |
| **Gland steam kondensator bosimi** | ⚠️ **−1.5 kPa DAN YUQORI BO'LMASLIGI** | Doimiy |

*Avtomatika tekshiruvi (11.6.3)*
1. ⚠️ **Yordamchi bug'dan gland steam kollektoriga bosim boshqaruv klapani to'liq ishlayotganini va kollektorni belgilangan bosimda (20–30 kPa) ushlay olishini tasdiqlang**
2. ⚠️ **HP gland bug' sizishidan LP bug' kirishiga bosim boshqaruv klapani to'liq ishlayotganini va sizish bosimini LP kirish bug'idan 1 kPa YUQORI ushlay olishini tasdiqlang**
3. ⚠️ **LP gland bug' kollektoridan kondensatorga bosim boshqaruv klapani to'liq ishlayotganini va gland bug' kollektor bosimini 40 kPa DAN OSHMAGAN holda ushlay olishini tasdiqlang**
4. ⚠️ **Desuperheating suv boshqaruv klapani LP gland bug' haroratini belgilangan qiymatda (150–180°C) ushlay olishini tasdiqlang**

⚠️ **Gland steam kondensator bosimi uchun ikki raqam:** 11.6.1 da **−1.5 kPa dan yuqori bo'lmasligi**, 3.7.6.1 da blower avto-ishga tushish nuqtasi **−0.015 barg = −1.5 kPa**. **Bir xil qiymat, turli birlikda.** Ya'ni kunlik nazoratdagi me'yor aynan zaxira blower ishga tushadigan nuqta.

⚠️ **N1 packing bosimi uchun ham ikki raqam:** 3.7.6.2 da **IP exhaust + 1 bar**, 11.6.3 da **LP kirish bug'idan + 1 kPa**. **Bular turli klapanlar** — biri N1 packing (IP exhaust ga), ikkinchisi HP gland sizishidan LP kirishga.

---

**🇷🇺 Паровые системы — ежедневный контроль и проверка автоматики**

**ВСПОМОГАТЕЛЬНЫЙ ПАР** — ⚠️ **давление (0.8–1.4 МПа) и температура (260–320°C) КАЖДЫЕ 1–2 ЧАСА**
Плотность: обход трубопроводов и фланцев; ⚠️ **сальники без заметных пропусков, штоки подвижны, ПОСЛЕ ЗАКРЫТИЯ БЕЗ ВНУТРЕННИХ ПРОПУСКОВ**
Арматура: ⚠️ **воздух на пневмоприводы 0.4–0.7 МПа**; ⚠️ **двигатель электропривода ≤70°C**, ⚠️ **концевики ТОЧНО откалиброваны**; ⚠️ **проверка автоматики давления (0.8–1.4 МПа) и температуры (260–320°C)**
Трубопроводы: ⚠️ **изоляционные прокладки между горячими трубами и опорами ЦЕЛЫЕ**; ⚠️ **еженедельно опоры и подвески, компенсаторы без заклинивания и ТРЕЩИН В ГОФРАХ**; ⚠️ **ежедневно проверка конденсатоотводчиков ПО ЗВУКУ И ТЕМПЕРАТУРЕ**; ⚠️ **продувка 1–2 РАЗА В НЕДЕЛЮ**

**УПЛОТНЯЮЩИЙ ПАР** — ⚠️ **давление 28 кПа** для ЦВСД и ЦНД, температура ЦНД ⚠️ **150–180°C**, ⚠️ **давление СП не выше −1.5 кПа**, запись каждые 1–2 часа
Автоматика: ⚠️ **коллектор 20–30 кПа** | ⚠️ **протечка ВД на впуск НД: на 1 кПа ВЫШЕ впуска НД** | ⚠️ **сброс коллектора НД в конденсатор: не выше 40 кПа** | ⚠️ **впрыск держит 150–180°C**

⚠️ **−1.5 кПа в п. 11.6.1 = −0.015 барг в п. 3.7.6.1** — норма ежедневного контроля совпадает с точкой автопуска резервного эксгаустера.

---

**🇬🇧 Auxiliary and Gland Steam — daily standards and automation checks**

**AUXILIARY STEAM (11.5)** — core: ⚠️ **"stabilize pressure, prevent leaks, remove impurities, and resist corrosion"**
⚠️ **Record and monitor header steam pressure (0.8–1.4 MPa) and temperature (260–320°C) every 1–2 HOURS**
Seals: daily patrol of pipelines, flanges and welded joints | ⚠️ **valve seals: inspect stuffing boxes of globe, control and check valves for no significant steam leakage; valve stems should move flexibly, and there should be NO INTERNAL LEAKAGE AFTER CLOSING**
Actuators: ⚠️ **air supply pressure for pneumatic valves 0.4–0.7 MPa**, no air leaks | ⚠️ **electric valves: motor temperature ≤70°C**, no overheating or burnout in the coil, ⚠️ **limit switches calibrated accurately** | ⚠️ **confirm the CRH-to-auxiliary-header pressure regulating valve is fully functional and can maintain 0.8–1.4 MPa** | ⚠️ **confirm the de-superheating water control valve can hold downstream temperature at 260–320°C**
Piping: ⚠️ **insulation pads between high-temperature pipelines and supports intact to prevent support deformation from overheating** | ⚠️ **weekly check supports and hangers; expansion joints move freely without jamming or deformation, and NO CRACKS IN THE CORRUGATIONS** | ⚠️ **daily check steam trap drainage is unobstructed (judged by EXHAUST SOUND AND TEMPERATURE)**, clean filter screens regularly | ⚠️ **open blowdown valves 1–2 times weekly** to remove impurities and accumulated water

**GLAND STEAM (11.6)**
HIP rotor gland steam pressure ⚠️ **28 kPa** and temperature per Fig 11-6-1, recorded every 1–2 hours | LP rotor gland steam pressure ⚠️ **28 kPa** and temperature ⚠️ **150–180°C**, every 1–2 hours | ⚠️ **gland steam condenser pressure kept no higher than −1.5 kPa**

Automation checks (11.6.3)
⚠️ **Confirm the aux-steam-to-gland-header pressure control valve is fully functional and can maintain 20–30 kPa** | ⚠️ **Confirm the HP gland leakage to LP admission pressure control valve can hold the leakage pressure 1 kPa over the LP admission steam** | ⚠️ **Confirm the LP gland header to condenser pressure control valve can keep the gland header no more than 40 kPa** | ⚠️ **Confirm the de-superheating water control valve holds LP gland steam at 150–180°C**

⚠️ **Two figures for the GSC pressure:** 11.6.1 says **no higher than −1.5 kPa**; 3.7.6.1 gives the standby blower auto-start point as **−0.015 barg = −1.5 kPa**. **The same number in different units** — the daily standard is exactly the blower start point.
⚠️ **Two "+1" figures that are not the same valve:** 3.7.6.2 sets N1 packing leak off at **IP exhaust + 1 bar**; 11.6.3 sets HP gland leakage to LP admission at **+1 kPa over LP admission**. Different valves, different scales.

`#auxsteam #glandsteam #maintenance #automation`

---
---

## POST 96 — Podshipnik avariyasi: 10 daqiqada nazorat

**🇺🇿 Podshipnik nosozligi — avariya javobi va ta'mir**

⚠️ **Tamoyil: "xavfsizlikka ustuvorlik, xavfni tez nazorat qilish, ilmiy ta'mir, takrorlanishning oldini olish". To'rt bosqich: avariya javobi → ildiz sabab qidiruvi → tizimli ta'mir → avariyadan keyingi tahlil.**

**A. AVARIYA JAVOBI — 10 DAQIQA ICHIDA XAVFNI NAZORAT QILING**

*1. Avariya to'xtatish*
⚠️ **Birlik yuklamasini DARHOL 30% DAN PASTGA tushiring**, "avariya to'xtatish" tugmasini qo'lda bosing va turbina bug' kirish klapanini yoping — rotorning uzluksiz ishqalanishidan shikastning kuchayishining oldini olish uchun
⚠️ **To'xtatishdan keyin lube oil nasosni ISHLASHDA QOLDIRING (kamida 30 DAQIQA) va yog' ta'minot bosimini 0.15–0.17 MPa da ushlang** — yuqori harorat va yog' yetishmovchiligidan journal deformatsiyasining oldini olish uchun
⚠️ **Podshipnik yonsa — avval yog' nasosini o'chiring va KARBONAT ANGIDRIDLI o'chirgich ishlating (SUV TAQIQLANADI)**
⚠️ **Turning gear ni ishga tushiring (qotib qolmagan bo'lsa) va 7 r/min da past tezlikda aylantiring** — mahalliy qizib ketishdan rotor egilishining oldini olish uchun. ⚠️ **Aylantirish davomida qotib qolish yuz bersa — DARHOL TO'XTATING va majburiy aylantirishdan saqlaning**

*2. Xavfsiz izolyatsiya va ogohlantirish*
Birlik atrofiga **qizil ogohlantirish lentasi** o'rnating, **"Uskuna nosoz, ishlatish taqiqlanadi"** belgisini qo'ying. Quvvat, bug' va lube oil konturi klapanlarini uzing, tegishli nasoslarni to'xtating.

*3. Dastlabki xavf nazorati*
• Yog' sizsa — **yog' yutuvchi paxta** bilan yig'ing, joydagi yonuvchi materiallarni tozalang
• ⚠️ **Podshipnik korpusi harorati juda yuqori bo'lsa (>100°C) — sanoat ventilyatori yoki sovutish suvi quvuri bilan sovuting (ZANGLASHNING oldini olish uchun to'g'ridan-to'g'ri suv purkamang)**
• ⚠️ **Keyingi ishlarni faqat harorat 60°C DAN PASTGA tushgandan keyin boshlang**

**B. ILDIZ SABAB QIDIRUVI**

*Podshipnik va val tizimini ochish*
⚠️ **Sirpanish podshipniklari uchun: babbit qatlami erigan, ko'chgan yoki yorilganini tekshiring. Qotishma qatlamining KENG KO'LAMLI KO'CHISHI "vkladish kuyishi" avariyasini bildiradi — asosan MOYLASH UZILISHIDAN.**
⚠️ **Journal holatini o'lchash: tashqi mikrometr bilan yeyilishni, indikator bilan val og'ishini, RANGLI DEFEKTOSKOPIYA bilan yoriqlarni aniqlang**

*Moylash tizimini tekshirish*
⚠️ **Yog' tahlili: qovushqoqlik, namlik va aralashma miqdorini sinang — NAMLIK >0.1% yoki ARALASHMA >0.02% bo'lsa buzilganini bildiradi**
⚠️ **Yog' nasosini ochib tishli g'ildirak yoki ish g'ildiragi yeyilishini tekshiring; filtr to'rini tozalab METALL QIPIQLARNI tekshiring (ko'p miqdordagi qipiq JIDDIY podshipnik yeyilishini bildiradi); yog' ta'minot bosimi me'yorga mosligini tekshiring (normal diapazon 0.15–0.17 MPa)**

*Ish sharoiti va himoya tizimi*
⚠️ **DCS yozuvlarini oling: avariyadan OLDINGI 1 SOAT ichida yuklama, tezlik, podshipnik harorati va tebranish qiymatlaridagi o'zgarishlarni tekshiring** — ortiqcha yuklama yoki ortiqcha tezlanish kabi anomal sharoitlar bo'lganmi
⚠️ **Himoya qurilmalarini sinang: harorat va tebranish himoyasi normal ishga tushadimi, past lube oil bosimi himoyasi ishlamay qolganmi**

**C. TIZIMLI TA'MIR**
⚠️ **Tamoyil: "asl qism bilan almashtirish, aniqlikka rioya, bosqichma-bosqich tekshirish"**
• **Podshipnik:** ⚠️ **asl bilan bir xil model va aniqlik darajasidagi podshipnik tanlang**
• **Val tizimi:** ⚠️ **journal yeyilishini LAZERLI QOPLASH bilan ta'mirlang; val og'ishini bosim bilan to'g'rilash yoki tokarlik kesish bilan tuzating. Mufta nomutanosibligi katta bo'lsa dvigatel yoki podshipnik o'rindig'i pozitsiyasini sozlang va LAZERLI TEKISLASH ASBOBI bilan kalibrlang**
• **Moylash tizimi:** ⚠️ **yog'ni bir xil markadagi yangisiga TO'LIQ almashtiring; bak, quvur va filtr to'rini KEROSIN bilan yuving (yuvgandan keyin siqilgan havo bilan quriting); eskirgan zichlashlarni almashtiring**

**D. BOSQICHMA-BOSQICH SINOV**
| Bosqich | Talab |
|---|---|
| **Sovuq sinov** | ⚠️ **Valni QO'LDA 5–10 MARTA aylantiring** — qotib qolmaganini tasdiqlang; lube oil nasosni yoqing, ⚠️ **bosimni (0.15–0.17 MPa) va yog' qaytishi silliqligini tekshiring, 1 SOAT sizishsiz ishlating** |
| **Past tezlikda sinov** | ⚠️ **1000 r/min ga oshiring, 30 DAQIQA ishlating**, podshipnik harorati va tebranishni kuzating. Anomaliya bo'lmasa ⚠️ **2000 r/min ga oshiring va yana yarim soat ishlating** |
| **Nominal tezlikda sinov** | ⚠️ **3000 r/min ga oshiring va 1 SOAT UZLUKSIZ ishlating. HAR 10 DAQIQADA harorat, tebranish va yog' ta'minot parametrlarini qayd eting. Faqat barcha ko'rsatkichlar me'yorga javob bergandan keyin normal ishga o'ting** |

⚠️ **Lube oil bosimi uchun uchinchi raqam: 0.15–0.17 MPa = 1.5–1.7 barg.** Bu POST 4 dagi **1.5–1.7 barg** bilan bir xil. Ya'ni avariyadan keyin ham normal ish bosimi ushlanadi.

**Nosozlik sabablari — 5 o'lcham**
1. **Moylash tizimi** (eng keng tarqalgan): sath anomaliyasi (⚠️ **juda past — plyonka yo'q, metall-metallga ishqalanish; juda yuqori — yog' aralashtirish qarshiligi ortadi, qo'shimcha issiqlik**), yog' sifatining buzilishi, tiqilish yoki sizish
2. **Montaj chetlanishi:** ⚠️ **zazor juda katta — tebranish kuchayadi; juda kichik — issiqlik kengayishidan ishqalanish qarshiligi ortadi va mahalliy qizib ketadi**; val tekislanmasligi; ⚠️ **montajda notekis kuch (ortiqcha bolg'alash) halqalarni deformatsiyalaydi; podshipnik qopqog'i boltlarining notekis tortilishi korpusda notekis kuchlanish beradi**
3. **Ish sharoiti:** ortiqcha yuklama, ⚠️ **juda tez tezlanish — plyonka yuklama ko'tarishdan oldin to'liq hosil bo'lmaydi; juda keskin sekinlashish — plyonka bosimining to'satdan tushishidan vaqtinchalik QURUQ ISHQALANISH**
4. **Uskuna eskirishi:** babbit yorilishi, journal/korpus yeyilishi, ishlab chiqarish defektlari
5. **TO va muhit:** ⚠️ **TO siklining juda uzunligi**, ⚠️ **muhit ifloslanishi — chang va namlik podshipnik korpusi tirqishlaridan kiradi; mashina zalining yomon shamollatilishi yog' oksidlanishini tezlashtiradi**, ⚠️ **monitoring yetishmovchiligi**

---

**🇷🇺 Авария подшипника — контроль за 10 минут**

**A. АВАРИЙНЫЙ ОТВЕТ**
⚠️ **НЕМЕДЛЕННО разгрузить НИЖЕ 30%**, кнопка аварийного останова, закрыть впускной клапан
⚠️ **После останова маслонасос ОСТАВИТЬ В РАБОТЕ минимум 30 МИНУТ при давлении 0.15–0.17 МПа** — против деформации шейки
⚠️ **При возгорании — сначала остановить насос, тушить УГЛЕКИСЛОТОЙ (ВОДА ЗАПРЕЩЕНА)**
⚠️ **ВПУ (если не заклинило) на 7 об/мин; при заклинивании — НЕМЕДЛЕННО остановить, не проворачивать силой**
⚠️ **Корпус >100°C — охлаждать вентилятором или трубой с водой (НЕ лить воду напрямую — ржавчина); работы только НИЖЕ 60°C**

**B. ПОИСК ПРИЧИНЫ**
⚠️ **Обширное отслоение баббита = «выплавление вкладыша», чаще всего от ОБРЫВА СМАЗКИ** | ⚠️ **микрометр, индикатор, ЦВЕТНАЯ ДЕФЕКТОСКОПИЯ** | ⚠️ **масло: ВЛАГА >0.1% или ПРИМЕСИ >0.02% — деградация** | ⚠️ **много стружки на сетке = сильный износ**; давление **0.15–0.17 МПа** | ⚠️ **DCS за 1 ЧАС до аварии**; ⚠️ **проверить защиты по температуре, вибрации и низкому давлению масла**

**C. РЕМОНТ** — ⚠️ **та же модель и класс точности**; ⚠️ **ЛАЗЕРНАЯ НАПЛАВКА шейки, правка давлением или проточка, ЛАЗЕРНАЯ ЦЕНТРОВКА**; ⚠️ **полная замена масла, промывка КЕРОСИНОМ, сушка сжатым воздухом**

**D. ЭТАПНЫЕ ИСПЫТАНИЯ** — ⚠️ **ручной проворот 5–10 РАЗ, насос 1 ЧАС без течей при 0.15–0.17 МПа** → ⚠️ **1000 об/мин 30 МИНУТ → 2000 об/мин полчаса** → ⚠️ **3000 об/мин 1 ЧАС, запись КАЖДЫЕ 10 МИНУТ**

**Пять причин** — смазка (уровень, качество, закупорка) | монтаж (⚠️ **большой зазор — вибрация, малый — перегрев**; ⚠️ **удары молотком, неравномерная затяжка**) | режим (⚠️ **быстрый разгон — плёнка не успевает; резкий выбег — СУХОЕ ТРЕНИЕ**) | старение | ⚠️ **ТО и среда (пыль, влага, плохая вентиляция, недостаток мониторинга)**

---

**🇬🇧 Bearing Fault — control risks within 10 minutes**

⚠️ **Principles: prioritize safety, quickly control risks, conduct scientific repairs, prevent recurrence. Four phases: emergency response → root cause investigation → systematic repair → post-accident review.**

**A. EMERGENCY RESPONSE — CONTROL RISKS WITHIN 10 MINUTES**
⚠️ **Immediately reduce unit load to below 30%**, manually activate the emergency shutdown button, close the turbine steam inlet valve
⚠️ **After shutdown, keep the lubricating oil pump running (for at least 30 MINUTES) to maintain an oil supply pressure of 0.15–0.17 MPa**, preventing journal deformation from high temperature and oil shortage
⚠️ **If the bearing catches fire, first shut down the oil pump and use a CARBON DIOXIDE extinguisher (water is prohibited)**
⚠️ **Start the turning gear (if not jamming) and perform low-speed turning at 7 r/min** to prevent rotor bending from local overheating. ⚠️ **If jamming occurs during turning, stop immediately and avoid forced rotation**
Safety isolation: **red warning tape**, **"Equipment Fault, No Operation"** sign, cut power, steam and lube oil circuit valves
⚠️ **If bearing housing temperature is too high (>100°C), cool with an industrial fan or cooling water pipe — avoid direct water spraying to prevent rusting. Proceed only after temperature drops below 60°C**

**B. ROOT CAUSE INVESTIGATION**
⚠️ **For sliding bearings check if the Babbitt layer is melted, peeled or cracked — EXTENSIVE PEELING indicates a "bearing bush burning" accident, mostly caused by LUBRICATION INTERRUPTION**
⚠️ **Measure the journal: external micrometer for wear, dial indicator for deflection, DYE PENETRANT TESTING for cracks**
⚠️ **Oil analysis: MOISTURE >0.1% or IMPURITIES >0.02% indicates deterioration**
⚠️ **Disassemble the oil pump; clean the filter screen and check for metal debris (a large amount indicates severe bearing wear); verify oil supply pressure (normal 0.15–0.17 MPa)**
⚠️ **Retrieve DCS records: load, speed, bearing temperature and vibration within 1 HOUR before the accident**; ⚠️ **test whether temperature and vibration protection trigger normally and whether low lube oil pressure protection failed**

**C. SYSTEMATIC REPAIR** — ⚠️ **"original part replacement, precision compliance, phased verification"**: same model and precision grade bearing | ⚠️ **repair journal wear using LASER CLADDING; straighten deflection by pressure straightening or lathe cutting; calibrate coupling with a LASER ALIGNMENT TOOL** | ⚠️ **completely replace the oil with the same grade; flush tank, pipeline and filter with KEROSENE, dry with compressed air; replace aged seals**

**D. PHASED TEST RUN**
⚠️ **Cold test: manually turn the shaft 5–10 times to confirm no jamming; start the oil pump, check pressure (0.15–0.17 MPa) and return smoothness, run 1 HOUR without leakage**
⚠️ **Low-speed: 1000 r/min for 30 MINUTES, monitor bearing temperature and vibration; if no abnormalities, 2000 r/min for another half hour**
⚠️ **Rated speed: 3000 r/min continuously for 1 HOUR, record temperature, vibration and oil parameters EVERY 10 MINUTES. Only switch to normal operation after all indicators meet standards**

⚠️ **0.15–0.17 MPa equals 1.5–1.7 barg** — the same bearing header pressure as POST 4. Normal running pressure is held even in recovery.

**Five cause dimensions** — lubricating oil system (⚠️ **too low: no film, metal-to-metal; too high: agitation resistance, extra heat**), installation (⚠️ **clearance too large: vibration; too small: thermal expansion friction and local overheating**; ⚠️ **excessive hammering deforms rings; inconsistent cap bolt torque gives uneven stress**), operating conditions (⚠️ **speeding up too quickly: film not fully formed; slowing down too abruptly: temporary DRY FRICTION**), equipment ageing, ⚠️ **maintenance and environment (dust and moisture through housing gaps, poor machine room ventilation accelerating oxidation, inadequate monitoring)**

`#bearingfault #emergency #babbitt #testrun`

---
---

## POST 97 — Rotorni to'g'rilash usullari

**🇺🇿 Egilgan rotor — diagnostika va to'g'rilash**

**A. AVARIYA TO'XTATISH VA DASTLABKI TEKSHIRUV**
⚠️ **Birlikni DARHOL trip qiling: anomal tebranish, ishqalanish tovushi yoki parametr anomaliyasi topilishi bilan tez VAKUUMNI BUZING va avariya to'xtatishni bajaring** — avariyaning kengayishining oldini olish uchun
⚠️ **To'xtatishdan keyin DARHOL uzluksiz turning gear ni ishga tushiring. Turning gear toki anomal bo'lsa yoki ishga tushmasa — rotorni QO'LDA 180° aylantiring va ekssentrisitetni kuzating**
⚠️ **Tekshiruv va izolyatsiya: suv kirishiga imkon beradigan BARCHA klapanlarni yoping, nosozlik manbasini izolyatsiya qiling va parametrlarni batafsil qayd eting (harorat, tebranish, ekssentrisitet)**

**B. EGILISHNI DIAGNOSTIKA QILISH**
| Usul | Nima qilinadi |
|---|---|
| **Statik o'lchov** | ⚠️ **INDIKATOR bilan journal, upor disk va boshqa qismlarning urishini o'lchang va maksimal egilish qiymatini hisoblang** |
| **Dinamik tahlil** | ⚠️ **Tebranish spektri (1× chastota ustun), faza barqarorligi va o'q siljishi farqidagi o'zgarishlar orqali egilish turini (ELASTIK yoki DOIMIY) aniqlang** |

**C. TO'G'RILASH — uchta usul**

*1. ELASTIK egilish*
⚠️ **Termik kuchlanishni yo'qotish orqali:** uzluksiz turning gear ishi, **silindr izolyatsiyasi (yuqori va pastki silindr orasidagi harorat farqini ushlab turish uchun drenajni yopish)** yoki **qizdirish vaqtini uzaytirish** — rotor haroratini bir tekis qilish uchun

*2. DOIMIY egilish — mahalliy qizdirish usuli*
⚠️ **Egilishning BO'RTGAN QISMINI alanga yoki SANOAT CHASTOTALI INDUKSIYA bilan 650°C DAN PAST qizdiring** — metall tolalarini qisqartirish uchun, keyin **sekin sovutib** to'g'rilang
⚠️ **Bu usul egilish qiymati ≤0.1 mm bo'lganda MOS KELADI, lekin QOLDIQ KUCHLANISH qolishi mumkin**

*3. DOIMIY egilish — yuqori haroratli sudralish (creep) usuli*
⚠️ **Rotorga O'Q BO'YICHA BOSIM qo'ying va bir vaqtda ish haroratidan YUQORIGA qizdiring (masalan yangi bug' haroratidan 75–100°C YUQORI), 8–14 SOAT issiq holatda ushlang va materialning sudralishi orqali egilishni yo'qoting**
⚠️ **Bu usul KATTA egilish uchun mos (masalan 0.1–0.3 mm) va QOLDIQ KUCHLANISHI KAM**

*4. Zavodga qaytarish*
⚠️ **Egilish qiymati 0.3 mm DAN OSHSA yoki to'g'rilashdan keyin talablar bajarilmasa — rotor mexanik ishlov berish, dinamik muvozanatlash yoki qismlarni almashtirish uchun zavodga qaytarilishi SHART**

**Qisqacha jadval**
| Egilish | Usul | Qoldiq kuchlanish |
|---|---|---|
| Elastik | Turning gear, silindr izolyatsiyasi, qizdirishni uzaytirish | Yo'q |
| **≤0.1 mm** | ⚠️ **Mahalliy qizdirish, <650°C** | ⚠️ **Qolishi mumkin** |
| **0.1–0.3 mm** | ⚠️ **Creep, +75–100°C, 8–14 soat** | ⚠️ **Kam** |
| **>0.3 mm** | ⚠️ **ZAVODGA** | — |

**D. OLDINI OLISH CHORALARI**
⚠️ **Ishga tushirishdan oldin tasdiqlang:**
• **Asosiy val urishi ≤ asl qiymat ±0.02 mm**
• **Yuqori va pastki silindr harorat farqi ≤42°C**
• ⚠️ **Main bug' o'ta qizishi ≥56°C**
• ⚠️ **ISSIQ ishga tushirishda: AVVAL val zichlashiga bug' bering, KEYIN vakuum torting**
• ⚠️ **Val zichlash bug' ta'minoti harorati silindr metall haroratiga MOS KELISHI SHART**

**Ekspluatatsiyani optimallashtirish**
• Tezlanish tempini tavsiya etilgan qiymat bo'yicha boshqaring va ⚠️ **kritik tezlik yaqinida turishdan saqlaning**
• ⚠️ **Tebranish, o'q siljish farqi va harorat kabi himoya qurilmalarini MUNTAZAM KALIBRLANG**

**Uskunani ta'mirlash**
⚠️ **Val zichlash zazori, drenaj tizimi va issiqlik izolyatsiyasi butunligini muntazam tekshiring**, silindr sizishi va harorat o'lchash nuqtasi defektlarini o'z vaqtida bartaraf eting

**Xodimlarni o'qitish**
⚠️ **Qoidabuzarliklarni yo'q qiling — masalan VAL ZICHLASH BUG' TA'MINOTINI TASDIQLAMASDAN VAKUUM TORTISH.** Uskuna defektlari uchun yopiq sikl boshqaruv mexanizmini yarating.

⚠️ **56°C o'ta qizish talabi** POST 20 dagi **−56°C harorat tushishi** bilan tasodifan bir xil raqam — lekin butunlay boshqa narsa. Biri **bug' to'yinish haroratidan qancha yuqori**, ikkinchisi **15 daqiqadagi tushish**.

---

**🇷🇺 Изгиб ротора — диагностика и правка**

**A. ОСТАНОВ** — ⚠️ **немедленный срыв вакуума и аварийный останов**; ⚠️ **сразу непрерывное ВПУ; при аномальном токе или отказе — ПРОВОРОТ ВРУЧНУЮ на 180° с контролем эксцентриситета**; ⚠️ **закрыть ВСЕ клапаны возможного заброса воды, изолировать, записать параметры**

**B. ДИАГНОСТИКА** — ⚠️ **ИНДИКАТОРОМ биение шейки и упорного диска, расчёт максимального изгиба** | ⚠️ **по спектру (преобладание 1×), стабильности фазы и осевому сдвигу определить УПРУГИЙ или ОСТАТОЧНЫЙ изгиб**

**C. ПРАВКА**
*Упругий* — ⚠️ **непрерывное ВПУ, изоляция цилиндра (закрытие дренажа для удержания разницы верх/низ), удлинение прогрева**
*Остаточный, локальный нагрев* — ⚠️ **выпуклую часть греть пламенем или ИНДУКЦИЕЙ ПРОМЫШЛЕННОЙ ЧАСТОТЫ НИЖЕ 650°C, затем МЕДЛЕННОЕ охлаждение**; ⚠️ **подходит при ≤0.1 мм, но ОСТАЁТСЯ остаточное напряжение**
*Остаточный, ползучесть* — ⚠️ **осевое давление + нагрев ВЫШЕ рабочей температуры (на 75–100°C выше температуры свежего пара), выдержка 8–14 ЧАСОВ**; ⚠️ **для 0.1–0.3 мм, остаточные напряжения МАЛЫ**
*Завод* — ⚠️ **при >0.3 мм или неудачной правке — механическая обработка, динамическая балансировка или замена**

**D. ПРОФИЛАКТИКА** — ⚠️ **биение ≤ исходное ±0.02 мм**, ⚠️ **разница верх/низ ≤42°C**, ⚠️ **перегрев свежего пара ≥56°C**, ⚠️ **при ГОРЯЧЕМ пуске СНАЧАЛА пар на уплотнения, ПОТОМ вакуум**, ⚠️ **температура уплотняющего пара СООТВЕТСТВУЕТ металлу цилиндра**
⚠️ **Не задерживаться у критической**; ⚠️ **регулярная поверка защит**; ⚠️ **исключить набор вакуума без подтверждённой подачи пара на уплотнения**

---

**🇬🇧 Rotor Bending — diagnosis and straightening**

**A. EMERGENCY SHUTDOWN AND PRELIMINARY INSPECTION**
⚠️ **Trip the unit immediately: once abnormal vibration, friction sound or parameter abnormality is found, quickly BREAK THE VACUUM and shut down urgently** to prevent the accident from expanding
⚠️ **Immediately put the continuous turning gear into operation after shutdown. If turning gear current is abnormal or it cannot be put into operation, MANUALLY turn the rotor by 180° and monitor eccentricity**
⚠️ **Close ALL valves that may allow water ingress, isolate the fault source, and record detailed parameters (temperature, vibration, eccentricity)**

**B. DIAGNOSIS**
⚠️ **Static measurement: use a DIAL INDICATOR to measure runout of the journal, thrust disc and other parts, and calculate the maximum bending value**
⚠️ **Dynamic analysis: judge the bending type (ELASTIC or PERMANENT) through vibration spectrum (1× frequency dominant), phase stability and changes in axial displacement difference**

**C. STRAIGHTENING TREATMENT**
*Elastic bending* — ⚠️ **eliminate thermal stress by continuous turning gear operation, cylinder isolation (closing the drain to maintain the upper-to-lower cylinder temperature difference), or extending warm-up time** to make rotor temperature uniform
*Permanent — local heating method* — ⚠️ **heat the convex part of the bend to BELOW 650°C with flame or POWER FREQUENCY INDUCTION to shrink the metal fibres, then COOL SLOWLY for straightening**; ⚠️ **suitable for bending values ≤0.1 mm, but RESIDUAL STRESS MAY REMAIN**
*Permanent — high-temperature creep method* — ⚠️ **apply AXIAL PRESSURE to the rotor and heat it ABOVE the working temperature (e.g. 75–100°C higher than new steam temperature) at the same time, keep it warm for 8–14 HOURS, and eliminate bending through material creep**; ⚠️ **suitable for large bending (0.1–0.3 mm) and has SMALL RESIDUAL STRESS**
*Return to factory* — ⚠️ **if the bending value exceeds 0.3 mm or requirements cannot be met after straightening, the rotor must be sent back for machining, dynamic balance correction or component replacement**

| Bending | Method | Residual stress |
|---|---|---|
| Elastic | Turning gear, cylinder isolation, longer warm-up | None |
| **≤0.1 mm** | ⚠️ **Local heating, below 650°C** | ⚠️ **May remain** |
| **0.1–0.3 mm** | ⚠️ **Creep, +75–100°C, 8–14 hours** | ⚠️ **Small** |
| **>0.3 mm** | ⚠️ **RETURN TO FACTORY** | — |

**D. PREVENTIVE MEASURES**
⚠️ **Before start-up ensure: main shaft runout ≤ original value ±0.02 mm, upper-to-lower cylinder temperature difference ≤42°C, and main steam superheat ≥56°C**
⚠️ **During hot start-up, supply steam to the shaft seal FIRST before drawing vacuum, and the shaft seal steam supply temperature MUST MATCH the cylinder metal temperature**
Optimize operation: control speed-up rate by the recommended rate, ⚠️ **avoid staying near the critical speed**; ⚠️ **regularly calibrate vibration, axial displacement difference and temperature protections**
Maintenance: ⚠️ **regularly check shaft seal clearance, drainage system and thermal insulation integrity**
Training: ⚠️ **eliminate illegal operations such as DRAWING VACUUM WITHOUT CONFIRMING SHAFT SEAL STEAM SUPPLY**

⚠️ **The 56°C superheat requirement** happens to share a number with the **−56°C downward temperature change** in POST 20, but they are unrelated: one is how far above saturation the steam is, the other is a 15-minute drop.

`#rotorbend #straightening #creep #prevention`

---
---

## POST 98 — Kurak shikasti: sabab va ta'mir

**🇺🇿 Kurak — sabablar, avariya javobi va ta'mir**

**SABABLAR — 4 guruh**

*1. Loyiha va ishlab chiqarish defektlari*
• ⚠️ **Kurak kuchining yetishmasligi:** loyihada charchash yuklamasi to'liq hisobga olinmagan. Kurak juda yupqa yoki profilida **kuchlanish konsentratsiyasi nuqtalari** bor (masalan **kurak ildizida juda kichik radius**) — uzoq ish davomida yoriq beradi
• ⚠️ **Material yoki ishlov berish:** kurak uchun ishlatilgan legirlangan po'lat sifatsiz (aralashmalar ko'p), yoki ishlov berishda **chala payvand va yuza yoriqlari** bor

*2. Anomal ish sharoiti*
• ⚠️ **Ortiqcha yuklama yoki parametrning chegaradan chiqishi:** birlik uzoq vaqt nominal yuklamadan yuqorida ishlaydi yoki bug' ortiqcha qizigan/ortiqcha bosimda. Bu kurakning termik kuchlanishi va markazdan qochma kuchini loyihaviy qiymatdan ANCHA oshiradi
• ⚠️ **Suv kirishi avariyasi:** ho'l bug' turbinaga kiradi (masalan **HRSG HP/IP/LP suv sathining ortiqchaligi, desuperheater nosozligi**). Yuqori tezlikdagi suv tomchilari kuraklarga uriladi va **"eroziya" yoki bevosita sinishga** olib keladi — ⚠️ **asosan LP silindrning OXIRGI BOSQICH kuraklarida**

*3. Noto'g'ri TO va ta'mir*
• ⚠️ **Cho'kma va korroziya:** tuz cho'kmasi va aralashmalar kurak yuzasida uzoq to'planadi → **notekis oqim kanallari va ortiqcha mahalliy oqim tezligi** → kurak tebranishi. ⚠️ **Ho'l bug' sohasidagi kuraklar korroziyaga qarshi chora ko'rilmasa ELEKTROKIMYOVIY KORROZIYADAN PITTING beradi va kuchini yo'qotadi**
• ⚠️ **Rotor muvozanatining buzilishi:** ta'mirdan keyin dinamik muvozanat aniqligi yetarli emas, yoki ish davomida kurak cho'kmasi notekis → rotor tebranishi oshadi → kuraklar qo'shimcha dinamik yuklama ko'taradi

*4. Begona jism zarbasi*
• ⚠️ **Bug' bilan kelgan begona jism:** qozon yoki bug' quvurida metall bo'laklari, payvand shlaki, cho'kma va boshqalar bug' bilan turbinaga kiradi va kuraklarga yuqori tezlikda uriladi — ⚠️ **ayniqsa HP silindrning DASTLABKI BIR NECHA BOSQICHIDA** → mahalliy botiqlar, yoriqlar yoki sinish
• ⚠️ **Ta'mirdan qolgan axlat:** asboblar, boltlar va boshqa axlat ta'mirdan keyin oqim kanalida qoladi va kuraklar orasiga tiqiladi. Ishga tushirishdan keyin aylanuvchi kuraklar ularga uriladi

**AVARIYA JAVOBI**
⚠️ **Tamoyil: "xavfni nazorat qilish uchun avariya to'xtatish → keng qamrovli tekshiruv va lokalizatsiya → aniq ta'mir → uzoq muddatli oldini olish"**

*1. Yuklamani darhol tushirish*
⚠️ **Tebranish yoki g'ayrioddiy shovqin aniqlangandan keyin birlik yuklamasini TEZ 50% DAN PASTGA tushiring va parametr o'zgarishlarini kuzating. Tebranish oshishda davom etsa yoki VAKUUM TO'SATDAN TUSHSA — DARHOL avariya to'xtatishni ishga tushiring va bug' ta'minotini uzing** — singan kuraklarning silindr bloki va rotorni shikastlashining oldini olish uchun

*2. To'xtatishdan keyin izolyatsiya*
⚠️ **To'xtatishdan keyin turbinaning bug' kirish va exhaust klapanlarini yoping, kondensator aylanma suvini uzing va singan kuraklarning yanada harakatlanishining oldini oling**
⚠️ **ROTORNI AYLANTIRMANG (kurak tiqilib qolganidan shubha bo'lsa)** — majburiy aylantirishdan val tizimi egilishining oldini olish uchun

**TEKSHIRUV**
• ⚠️ **Ichki tekshiruv: ENDOSKOPni silindr oqim kanaliga kiriting va kuraklarning shikastlanish joyi, darajasi hamda PARCHALAR SONINI qayd eting**
• ⚠️ **Nurlanishsiz nazorat: shikastlanmagan kuraklarda MAGNIT ZARRACHALI (yuza yoriqlari) yoki RANGLI (yuzaga yaqin defektlar) nazorat o'tkazing — KURAK ILDIZI VA UCHI kabi kuchlanish konsentratsiyasi sohalariga e'tibor bering.** Rotorda dinamik muvozanat sinovini o'tkazib, muvozanatsizlik kurak shikastidan ekanligini tasdiqlang
• ⚠️ **Begona jism manbasini qidirish: bug' quvuri filtrini tekshirib manbani aniqlang va kondensatordagi kurak parchalari hamda begona jismlarni tozalang**

**TA'MIR**
| Shikast | Usul |
|---|---|
| ⚠️ **Kichik yoriq: uzunligi <5 mm va kurak ildiziga yetmagan** | ⚠️ **TIG (volfram-inert gaz) payvandlash bilan ta'mirlang. Payvandlangan sohani silliq charxlab profil loyihaga mos kelishini ta'minlang** |
| ⚠️ **Jiddiy shikast: kurak singan yoki yoriq 5 mm dan oshgan** | ⚠️ **Bir xil model va materialdagi kurak bilan almashtiring — OG'IRLIGI asl kurak bilan MOS KELISHI SHART (rotor muvozanatiga ta'sir qilmasligi uchun). Almashtirishdan keyin rotor dinamik muvozanatini QAYTA bajaring** |

⚠️ **Oqim kanalini tozalash: turbina oqim kanalidagi cho'kma va begona jismlarni PUXTA tozalang. Silindr bloki va diafragmalar singan kuraklardan shikastlanganini tekshiring va tirnalgan joylarni charxlab tuzating**

**UZOQ MUDDATLI OLDINI OLISH**
• ⚠️ **Muntazam nurlanishsiz nazorat: HAR BIR KAPITAL TA'MIRDA (2–3 YILDA) barcha kuraklarni tekshiring — LP silindrning OXIRGI BOSQICH kuraklari va HP silindrning DASTLABKI BIR NECHA BOSQICHIGA e'tibor bering**
• ⚠️ **Ish parametrlarini qat'iy nazorat qilish: ortiqcha harorat, ortiqcha bosim va ortiqcha yuklamada ishlash TAQIQLANADI. Bug' harorati tebranishini ±5°C ichida ushlang va suv kirishining oldini olish uchun HRSG baraban suv sathi monitoringini kuchaytiring**
• ⚠️ **Begona jismning oldini olish: ta'mirdan keyin oqim kanali tozalanishi va ENDOSKOP bilan tekshirilishi SHART**

⚠️ **Uchta "5" raqami chalkashtiriladi:** yoriq chegarasi **5 mm**, bug' harorati tebranishi **±5°C**, exhaust harorati datchik farqi **5°C**. Har biri boshqa kontekstda.

---

**🇷🇺 Повреждение лопаток — причины, действия, ремонт**

**ПРИЧИНЫ** — ⚠️ **конструктивные (тонкая лопатка, КОНЦЕНТРАТОРЫ НАПРЯЖЕНИЙ, малый радиус у корня; некачественная сталь, НЕПРОВАРЫ и поверхностные трещины)** | ⚠️ **режим (длительная перегрузка, перегрев/превышение давления; ЗАБРОС ВОДЫ — капли бьют по лопаткам, ЭРОЗИЯ или обрыв, ЧАЩЕ НА ПОСЛЕДНЕЙ СТУПЕНИ ЦНД)** | ⚠️ **ТО (отложения → неравномерный поток → вибрация; ПИТТИНГ от электрохимической коррозии во влажнопаровой зоне; недостаточная балансировка после ремонта)** | ⚠️ **посторонние предметы (окалина, шлак — ОСОБЕННО В ПЕРВЫХ СТУПЕНЯХ ЦВД; забытый инструмент после ремонта)**

**ДЕЙСТВИЯ** — ⚠️ **быстро разгрузить НИЖЕ 50%**; ⚠️ **при росте вибрации или РЕЗКОМ ПАДЕНИИ ВАКУУМА — немедленный останов с отсечкой пара**; ⚠️ **после останова закрыть впуск и выхлоп, отключить циркводу**; ⚠️ **НЕ ПРОВОРАЧИВАТЬ РОТОР при подозрении на заклинивание**

**ОСМОТР** — ⚠️ **ЭНДОСКОП: место, степень, ЧИСЛО ОБЛОМКОВ** | ⚠️ **МАГНИТОПОРОШКОВЫЙ или ЦВЕТНОЙ контроль, особенно КОРЕНЬ И ВЕРШИНА**; динамическая балансировка | ⚠️ **фильтр паропровода для поиска источника, очистка конденсатора**

**РЕМОНТ** — ⚠️ **трещина <5 мм не до корня — TIG-СВАРКА с зачисткой по профилю** | ⚠️ **обрыв или трещина >5 мм — замена той же модели и материала, ВЕС ДОЛЖЕН СОВПАДАТЬ, затем ПОВТОРНАЯ балансировка** | ⚠️ **тщательная очистка проточной части, осмотр цилиндра и диафрагм**

**ПРОФИЛАКТИКА** — ⚠️ **дефектоскопия ВСЕХ лопаток КАЖДЫЙ КАПРЕМОНТ (2–3 ГОДА)**, ⚠️ **колебания температуры пара ±5°C**, ⚠️ **контроль уровня в барабанах КУ**, ⚠️ **эндоскопия после ремонта**

---

**🇬🇧 Blade Damage — causes, response and repair**

**CAUSES**
*Design and manufacturing* — ⚠️ **insufficient blade strength: fatigue load not fully considered; blade too thin or with STRESS CONCENTRATION POINTS (e.g. excessively small fillet at the blade root)**; ⚠️ **unqualified alloy steel, INCOMPLETE WELDING and surface cracks**
*Abnormal operating conditions* — ⚠️ **long-term operation over rated load, or steam over-temperature/over-pressure, pushing thermal stress and centrifugal force FAR ABOVE design values**; ⚠️ **water induction: wet steam enters (excessive HRSG HP/IP/LP water level, desuperheater failure); high-speed droplets cause "EROSION" or direct fracture, MOSTLY ON THE LAST-STAGE BLADES OF THE LP CYLINDER**
*Improper maintenance* — ⚠️ **salt scale gives uneven flow channels and excessive local velocity, triggering blade vibration; blades in the wet steam area develop PITTING from ELECTROCHEMICAL CORROSION without anti-corrosion measures**; ⚠️ **insufficient dynamic balance accuracy after overhaul, or uneven fouling, raising vibration and dynamic loads**
*Foreign object impact* — ⚠️ **metal blocks, welding slag and scale entering with steam and impacting at high speed, ESPECIALLY THE FIRST FEW STAGES OF THE HP CYLINDER**; ⚠️ **tools and bolts left in the flow channel after overhaul**

**EMERGENCY HANDLING** — ⚠️ **"emergency shutdown to control risks → comprehensive inspection and positioning → precise repair → long-term prevention"**
⚠️ **After detecting vibration or unusual noise, quickly reduce load to BELOW 50% and observe. If vibration continues to increase or THE VACUUM DROPS SUDDENLY, trigger emergency shutdown immediately and cut off steam supply** to prevent fractured blades damaging the cylinder block and rotor
⚠️ **After shutdown close the steam inlet and exhaust valves, cut off condenser circulating water**; ⚠️ **DO NOT TURN THE ROTOR if blade jamming is suspected**, to avoid shafting bending from forced turning

**INSPECTION** — ⚠️ **insert an ENDOSCOPE to observe damage location, degree, and record the NUMBER OF FRAGMENTS** | ⚠️ **magnetic particle testing (surface cracks) or penetrant testing (near-surface defects) on undamaged blades, focusing on stress concentration areas such as BLADE ROOT AND TIP**; dynamic balance testing | ⚠️ **inspect the steam pipeline filter to identify the foreign object source, clean fragments from the condenser**

**REPAIR**
⚠️ **Minor cracks: if crack length <5 mm and it does not extend to the blade root, repair by TIG welding; grind smooth so the profile meets design requirements**
⚠️ **Severe damage: if fractured or the crack exceeds 5 mm, replace with a blade of the same model and material — THE WEIGHT MUST BE CONSISTENT with the original to avoid affecting rotor balance. Re-perform rotor dynamic balance after replacement**
⚠️ **Thoroughly clean fouling and foreign objects in the flow channel; inspect whether cylinder block and diaphragms are damaged, grind and repair scratches**

**LONG-TERM PREVENTION** — ⚠️ **non-destructive testing on all blades during each overhaul (every 2–3 YEARS), focusing on LP last-stage blades and the first few HP stages** | ⚠️ **prohibit over-temperature, over-pressure and overload; control steam temperature fluctuation within ±5°C; strengthen HRSG drum level monitoring** | ⚠️ **after overhaul the flow channel must be cleaned and inspected with an endoscope**

`#bladedamage #TIG #endoscope #NDT`

---
---

## POST 99 — Exhaust harorati: sabab bo'yicha bartaraf etish

**🇺🇿 Yuqori exhaust harorati — sabab va harakat**

**QOLGAN SABABLAR (POST 63 davomi)**

*Vakuum tizimi sizishi*
• ⚠️ **Val zichlash bug' ta'minotining yetishmasligi:** turbina val zichlashlariga (HP, IP va LP silindr) bug' ta'minoti bosimi past bo'lsa — **tashqi havo val zichlash tirqishi orqali so'riladi va kondensator vakuumini buzadi**
• ⚠️ **Vakuum tizimi qismlarining ichki sizishi:** vakuum buzish klapanining yomon zichlanishi (**egar yeyilishi yoki eskirgan prokladka**), kondensator lyuk qopqog'ining zichlash nosozligi, drenaj quvuridagi klapanlarning ichki sizishi — hammasi havo kirishiga imkon beradi
• ⚠️ **Havo so'rish quvurining tiqilishi:** begona modda vakuum nasos kirish quvurini to'sadi → kondensatordagi kondensatsiyalanmaydigan gazlar chiqarilmaydi → to'planib issiqlik almashinuvini buzadi

*Anomal ish sharoiti*
• ⚠️ **Uzoq muddat past yuklamada ishlash: yuklama nominalning 30% DAN PAST bo'lganda turbina exhaust hajmi kamayadi, kondensatorda bug' oqim tezligi sekinlashadi. Bug' o'z vaqtida kondensatsiyalanmaydi va exhaust harorati TABIIY ravishda ko'tariladi — past yuklamada LP SILINDR PURKASH SOVUTISHNI YOQISH kerak**
• ⚠️ **Aylanma suv tizimi nosozligi:** nasos quvvatining yetishmasligi (**yeyilgan ish g'ildiragi, dvigatel tezligining pasayishi**) yoki klapanning yetarli ochilmasligi → sarf loyihaviy qiymatdan past → issiqlik almashinuv quvvati yetishmaydi

*Asbob o'lchov xatolari — NOTO'G'RI BAHOLASHGA MOYIL*
• ⚠️ **Exhaust harorat datchigining nosozligi:** datchikning eskirishi yoki simlarning bo'shashishi o'lchangan qiymatni g'ayritabiiy yuqori qiladi. ⚠️ **BIR XIL KONDENSATORNING TURLI O'LCHOV NUQTALARIDAGI HARORATLARNI SOLISHTIRING — farq 5°C DAN OSHSA datchik nosoz bo'lishi mumkin**
• ⚠️ **Vakuum o'lchagichining noaniqligi:** vakuum o'lchagich yoki bosim transmitterining kalibrlash muddati o'tgan bo'lsa ko'rsatkich past bo'ladi → **"vakuum tushishi exhaust haroratini oshirdi" degan noto'g'ri xulosa**. ⚠️ **Joyida STANDART VAKUUM O'LCHAGICH bilan kalibrlash talab qilinadi**

**AVARIYA HARAKATI**
⚠️ **Tamoyil: "avval haroratni nazorat qilish, keyin sabablarni aniqlash, oxirida ta'mirlash"**

1. ⚠️ **Avariya sovutishni yoqing: LP silindr purkash sovutish tizimini ishga tushirib exhaust haroratini ≤55°C da ushlang. Aylanma suv sarfi yetarli bo'lmasa ZAXIRA AYLANMA NASOSNI ishga tushiring va aylanma suv klapanini KENGROQ oching**
2. ⚠️ **Haroratni nazorat qilish uchun yuklamani tushiring: vakuum darajasi tushishda davom etsa — exhaust hajmini kamaytirish va kondensatorning uzoq muddatli qizib ketishining oldini olish uchun birlik yuklamasini tushiring**
3. ⚠️ **Val zichlash bug' ta'minotini tekshiring: bosimni DARHOL tasdiqlang; bosim past bo'lsa val zichlash bug' ta'minoti boshqaruv klapanini KENGROQ oching yoki ZAXIRA VAL ZICHLASH BUG' MANBASINI ishga tushiring** — havo so'rilishining oldini olish uchun

**SABAB BO'YICHA BARTARAF ETISH**
| Sabab | Harakat |
|---|---|
| **Quvur tomonida cho'kma/tiqilish** | ⚠️ **Kondensatorni to'xtatib issiqlik almashinuv quvurlarini tozalang va tozalashdan keyin quvurlarning o'tkazuvchanligini tekshirish uchun SHAR O'TKAZISH SINOVI o'tkazing** |
| **Vakuum tizimi sizishi** | ⚠️ **GELIY MASS-SPEKTROMETRLI SIZISH DETEKTORI bilan val zichlashi, lyuk qopqog'i va drenaj quvurini tekshiring, sizish nuqtasini aniqlab prokladkani almashtiring yoki boltlarni torting. Havo chiqargichni ta'mirlab so'rish quvvati me'yorga mosligini ta'minlang** |
| **Aylanma suv tizimi nosozligi** | ⚠️ **Nasosni ta'mirlang (yeyilgan ish g'ildiragini almashtiring, dvigatel tasmasini sozlang); aylanma suv filtrini tozalab quvur tiqilishini yo'q qiling va sarf loyihaviy qiymatga yetishini ta'minlang** |
| **Past yuklamadan yuqori harorat** | ⚠️ **LP silindr purkash sovutishni yoqing** |

**UZOQ MUDDATLI OLDINI OLISH**
• ⚠️ **Kondensatorni muntazam TO: shar tozalash tizimini HAR HAFTA ishlating, issiqlik almashinuv quvurlari korroziyasini HAR 1 YILDA tekshiring**
• ⚠️ **Vakuum tizimi monitoringi: val zichlash bug' ta'minoti bosimi, vakuum nasos toki va kondensator terminal farqini HAR KUNI qayd eting. TERMINAL FARQ 5°C DAN OSHSA yoki VAKUUM DARAJASI 3 kPa DAN KO'PROQ TEBRANSA — sizishni darhol tekshiring**
• ⚠️ **Aylanma suv sifatini optimallashtirish: korroziya va cho'kmaga qarshi ingibitorlar qo'shing; AYLANMA SUV QATTIQLIGINI ≤3 mmol/l va MUALLAQ ZARRACHALARNI ≤20 mg/l da ushlang** — issiqlik almashinuv quvurlarining cho'kmalanishining oldini olish uchun

⚠️ **Terminal farq uchun ikki raqam:** loyihaviy **3.1°C** (POST 40), **>6°C** issiqlik almashinuv to'silganini bildiradi (POST 63), **>5°C** kunlik monitoringda sizishni tekshirish nuqtasi. **5°C — birinchi harakat nuqtasi.**

⚠️ **"5°C farq" yana bir joyda:** bir xil kondensatorning turli nuqtalaridagi harorat farqi 5°C dan oshsa **DATCHIK nosoz**. Ikkalasini chalkashtirmang — biri terminal farq, ikkinchisi datchiklar orasidagi farq.

---

**🇷🇺 Высокая температура выхлопа — устранение по причинам**

**ПРИЧИНЫ (продолжение POST 63)**
⚠️ **Недостаточная подача пара на уплотнения** → подсос воздуха через зазор | ⚠️ **внутренние неплотности (клапан срыва вакуума — износ седла, старая прокладка; люк конденсатора; дренажи)** | ⚠️ **закупорка линии отсоса** → накопление неконденсирующихся газов
⚠️ **Работа НИЖЕ 30% нагрузки** → малый расход выхлопа, ⚠️ **включить впрыск ЦНД** | ⚠️ **отказ циркуляционной системы (износ колеса, снижение оборотов, недооткрытая задвижка)**
⚠️ **Ошибки измерений:** ⚠️ **сравнить точки одного конденсатора — разница >5°C означает неисправный датчик** | ⚠️ **просроченная поверка вакуумметра — поверка ЭТАЛОННЫМ прибором на месте**

**ДЕЙСТВИЯ** — ⚠️ **«сначала температура, потом причина, затем ремонт»**
⚠️ **Впрыск ЦНД, держать ≤55°C; при нехватке циркводы — ПУСК РЕЗЕРВНОГО насоса и шире открыть задвижку** | ⚠️ **при дальнейшем падении вакуума — разгрузить** | ⚠️ **проверить давление уплотняющего пара, шире открыть или пустить РЕЗЕРВНЫЙ ИСТОЧНИК**

**ПО ПРИЧИНАМ** — ⚠️ **чистка трубок + ШАРИКОВЫЙ ПРОГОН** | ⚠️ **ГЕЛИЕВЫЙ ТЕЧЕИСКАТЕЛЬ по уплотнениям, люку и дренажам** | ⚠️ **ремонт насоса и чистка фильтра** | ⚠️ **впрыск при малой нагрузке**

**ПРОФИЛАКТИКА** — ⚠️ **шариковая очистка ЕЖЕНЕДЕЛЬНО, осмотр коррозии трубок РАЗ В ГОД** | ⚠️ **ежедневная запись давления уплотнений, тока насосов и температурного напора; при напоре >5°C или колебаниях вакуума >3 кПа — искать присосы** | ⚠️ **жёсткость циркводы ≤3 ммоль/л, взвешенные ≤20 мг/л**

---

**🇬🇧 High Exhaust Temperature — handling by cause**

**REMAINING CAUSES (continuing POST 63)**
⚠️ **Insufficient shaft seal steam supply** — low supply pressure for HP, IP and LP shaft seals causes **external air to be sucked in through the shaft seal gap, damaging condenser vacuum**
⚠️ **Internal leakage of vacuum system components** — poor sealing of the vacuum breaking valve (**valve seat wear or aging gasket**), failed condenser manhole cover sealing, internal leakage of drain pipeline valves
⚠️ **Blockage of the air extraction pipeline** — foreign matter blocks the vacuum pump inlet, so non-condensable gases accumulate and impair heat exchange
⚠️ **Long-term low-load operation** — **when load is below 30% of rated, exhaust volume decreases and steam flow slows; steam cannot condense in time and exhaust temperature rises naturally — LP CYLINDER SPRAY COOLING should be activated at low load**
⚠️ **Circulating water system failure** — insufficient pump capacity (**worn impeller, reduced motor speed**) or insufficient valve opening gives flow below design
⚠️ **Instrument measurement errors (prone to misjudgment)** — ⚠️ **sensor ageing or loose wiring gives abnormally high readings: COMPARE TEMPERATURES AT DIFFERENT MEASURING POINTS OF THE SAME CONDENSER — if the difference exceeds 5°C, the sensor is likely faulty**; ⚠️ **expired vacuum gauge calibration gives low displayed values, leading to the misjudgment that "vacuum drop causes high exhaust temperature" — on-site calibration with a STANDARD VACUUM GAUGE is required**

**HANDLING** — ⚠️ **"first controlling temperature, then identifying causes, and finally repairing"**
⚠️ **Start LP cylinder spray cooling to control exhaust temperature ≤55°C; if circulating water flow is insufficient, start the STANDBY circulating water pump and open the valve wider**
⚠️ **If vacuum continues to drop, reduce load to decrease exhaust volume and prevent long-term condenser overheating**
⚠️ **Immediately verify shaft seal steam supply pressure; if low, open the control valve wider or start the STANDBY shaft seal steam source**

**BY CAUSE** — ⚠️ **tube fouling: shut down the condenser, clean the tubes and conduct a BALL PASSING TEST afterwards** | ⚠️ **vacuum leakage: use a HELIUM MASS SPECTROMETER LEAK DETECTOR on shaft seal, manhole cover and drain pipeline, replace gaskets or tighten bolts; repair the air extractor** | ⚠️ **circulating water: overhaul the pump, clean the filter, ensure flow reaches design** | ⚠️ **low-load high temperature: activate LP cylinder spray cooling**

**LONG-TERM PREVENTION** — ⚠️ **operate the rubber ball cleaning system EVERY WEEK, inspect heat exchanger tube corrosion EVERY 1 YEAR** | ⚠️ **record shaft seal steam supply pressure, vacuum pump current and condenser terminal difference DAILY; if terminal difference exceeds 5°C or vacuum fluctuates by more than 3 kPa, promptly investigate for leaks** | ⚠️ **add corrosion and scale inhibitors; control circulating water HARDNESS ≤3 mmol/L and SUSPENDED SOLIDS ≤20 mg/L**

⚠️ **Three terminal-difference figures:** design **3.1°C**, **>6°C** means blocked heat exchange, **>5°C** is the daily investigate-for-leaks trigger. **5°C is the first action point.**
⚠️ **A different 5°C:** a spread over 5°C between measuring points of the same condenser means a **faulty SENSOR**, not a fouled condenser. Don't confuse the two.

`#exhausttemp #vacuumleak #heliumleak #ballpassing`

---
---

## POST 100 — Podshipnik va o'q siljishi: qolgan belgilar

**🇺🇿 Podshipnik nosozligining oqibatlari — nima buziladi**

**MAHALLIY SHIKAST**
*1. Podshipnikning o'zi*
⚠️ **Sirpanish podshipniklarida "VKLADISH KUYISHI" yuz beradi — yuqori haroratdan BABBIT ERIYDI VA KO'CHADI.** ⚠️ **Dumalash podshipniklarida dumalash elementlari va ichki/tashqi halqalar orasida ishqalanish ortadi → yeyilish, yoriqlar, hatto PARCHALANISH → tayanch funksiyasini TO'LIQ yo'qotadi**

*2. Val tizimi aniqligining buzilishi*
⚠️ **Podshipnik shikasti journalning barqaror tayanchini yo'qotadi → radial yoki o'q bo'yicha siljish. Uzoq ishlash journal yeyilishi, tirnalishi yoki hatto valning ruxsat etilgan to'g'riligidan oshishiga olib keladi va butun val tizimining KONSENTRIKLIGINI buzadi**

*3. Mufta shikasti*
⚠️ **Val tizimi siljishi muftaga uzatiladi → mufta boltlarida notekis kuchlanish yoki sinish, yoki mufta uch yuzasining yeyilishi va nomutanosibligi → val tizimi tebranishi va og'ishini YANADA KUCHAYTIRADI**

**BIRLIK ISHINING UMUMIY ANOMALIYASI**
*1. Nazoratsiz tebranish va shovqin*
⚠️ **Anomal podshipnik zazori yoki qism shikasti KUCHLI val tizimi tebranishini beradi — tebranish qiymatlari xavfsizlik standartlaridan ANCHA oshadi. Bir vaqtda KUCHLI METALL ISHQALANISH VA ZARBA SHOVQINLARI yuzaga keladi, og'ir holatda BUTUN BIRLIK TITRAYDI va barqaror ishlash imkonsiz bo'ladi**

*2. Zanjirli harorat ko'tarilishi*
⚠️ **Podshipnik ishqalanishining oshishi metall harorati va yog' qaytish haroratining KESKIN ko'tarilishiga olib keladi. Trip qiymatidan oshsa birlik avtomatik to'xtaydi; HIMOYA QURILMASI ISHLAMASA — yuqori harorat sizib chiqqan moylash yog'ini YOQISHI va YONG'IN XAVFINI yaratishi mumkin**

*3. Moylash tizimining ifloslanishi*
⚠️ **Podshipnik shikastidan hosil bo'lgan METALL QIPIQLARI moylash yog'iga aralashadi, yog' bilan sirkulyatsiya qilib FILTR TO'RLARINI TO'SADI, YOG' NASOSI TISHLARINI TIRNAYDI, moylash tizimida yog' yetishmovchiligi yoki yog'ning buzilishiga sabab bo'ladi va boshqa podshipniklar hamda harakatlanuvchi qismlar yeyilishini YANADA KUCHAYTIRADI — "NOSOZLIK SIKLI" hosil bo'ladi**

**XAVFSIZLIK VA IQTISODIY YO'QOTISHLAR**
⚠️ **Podshipnik TO'LIQ QOTIB QOLSA — to'satdan VAL TIZIMI SINISHIGA olib kelishi mumkin. Yuqori tezlikda aylanuvchi qism parchalari KORPUSNI TESHIB O'TISHI va USKUNA PORTLASHIGA olib kelishi mumkin. Sizib chiqqan moylash yog'i yuqori haroratli qismlar (journal, silindr) bilan aloqaga kirib YONISHI va JOYDAGI XODIMLAR HAYOTINI XAVF OSTIGA QO'YISHI mumkin**
⚠️ **Ta'mirdan keyin ham VAL TIZIMI ANIQLIGI va PODSHIPNIK O'RNATISH ZAZORI kabi asosiy ko'rsatkichlar asl holatiga TO'LIQ QAYTARILISHI QIYIN** → birlik uzoq muddat tebranish va harorat kabi parametrlar KRITIK darajada ishlaydi → boshqa qismlarning eskirishi tezlashadi va butun turbinaning xizmat muddati QISQARADI

**O'Q SILJISHI — qolgan belgilar (POST 76 davomi)**

*Tebranishning kuchayishi*
⚠️ **O'q tebranish amplitudasi SEZILARLI oshadi va ba'zi birliklarda RADIAL tebranish ham BIR VAQTDA ko'tariladi. Ortiqcha siljish aylanuvchi va harakatsiz qismlar orasida ishqalanish keltirib chiqarsa — bu yanada kuchayadi**

*Nima uchun bu halokatli*
⚠️ **Rotorning o'q kuchining oshishi upor podshipnikni ORTIQCHA YUKLAYDI, YOG' PLYONKASINI BUZADI va upor pad segmentlaridagi BABBITNING ERISHIGA olib keladi. Shu paytda rotor o'q bo'yicha harakatlanadi, o'q siljishi ortadi va turbina ichidagi aylanuvchi hamda harakatsiz qismlar orasidagi O'Q ZAZORI YO'QOLADI. Natijada ishqalanish va to'qnashuv yuz beradi — KURAKLARNING MASSAVIY SINISHI, ASOSIY VAL EGILISHI, DIAFRAGMA VA ISH G'ILDIRAGINING PARCHALANISHI kabi og'ir shikast avariyalari**
⚠️ **Rotorning OLDINGA o'q harakati ham XUDDI SHU xavflarni keltirib chiqaradi**

⚠️ **"Nosozlik sikli" tushunchasi** — bu eng muhim amaliy xulosa. Bitta podshipnik shikastlanadi → metall qipiqlari yog'ga tushadi → filtr to'siladi → yog' ta'minoti kamayadi → **boshqa podshipniklar ham shikastlana boshlaydi**. Shuning uchun POST 92 dagi **"olingan filtr elementida metall qipiqlar bo'lsa nasos/podshipnik yeyilishini tekshiring"** talabi shunchalik muhim.

⚠️ **Himoya ishlamasa yong'in** — POST 34 dagi 4-band (**yog' qaytish harorati 75°C ga yetib tutun chiqsa**) va POST 57 dagi yog' yong'ini protsedurasi shu zanjirning davomi.

---

**🇷🇺 Последствия отказа подшипника — что разрушается**

**ЛОКАЛЬНО** — ⚠️ **«ВЫПЛАВЛЕНИЕ ВКЛАДЫША»: баббит ПЛАВИТСЯ И ОТСЛАИВАЕТСЯ**; у подшипников качения — износ, трещины, ⚠️ **РАЗРУШЕНИЕ с ПОЛНОЙ потерей опорной функции** | ⚠️ **потеря опоры → радиальное и осевое смещение → износ и задиры шейки, превышение допуска прямолинейности, нарушение КОНЦЕНТРИЧНОСТИ валопровода** | ⚠️ **смещение передаётся на МУФТУ → неравномерная нагрузка или ОБРЫВ БОЛТОВ, износ торца → УСИЛЕНИЕ вибрации**

**ОБЩЕЕ** — ⚠️ **вибрация ЗНАЧИТЕЛЬНО выше норм, СИЛЬНЫЙ металлический шум и удары, в тяжёлом случае ТРЯСЁТСЯ ВЕСЬ БЛОК** | ⚠️ **РЕЗКИЙ рост температуры металла и слива; при ОТКАЗЕ ЗАЩИТЫ высокая температура может ПОДЖЕЧЬ вытекшее масло** | ⚠️ **МЕТАЛЛИЧЕСКАЯ СТРУЖКА в масле ЗАБИВАЕТ СЕТКИ, ЦАРАПАЕТ ШЕСТЕРНИ НАСОСА → «ЦИКЛ ОТКАЗА»**

**ПОСЛЕДСТВИЯ** — ⚠️ **при ПОЛНОМ ЗАКЛИНИВАНИИ возможен ОБРЫВ ВАЛОПРОВОДА; обломки могут ПРОБИТЬ КОРПУС, привести к ВЗРЫВУ; горящее масло УГРОЖАЕТ ЖИЗНИ персонала** | ⚠️ **после ремонта точность валопровода и посадочные зазоры ПОЛНОСТЬЮ НЕ ВОССТАНАВЛИВАЮТСЯ** → работа у КРИТИЧЕСКИХ значений → СОКРАЩЕНИЕ ресурса

**ОСЕВОЙ СДВИГ (продолжение POST 76)** — ⚠️ **осевая вибрация растёт ЗНАЧИТЕЛЬНО, у части блоков ОДНОВРЕМЕННО растёт и радиальная**
⚠️ **Рост осевого усилия ПЕРЕГРУЖАЕТ упорный, РАЗРУШАЕТ ПЛЁНКУ и ПЛАВИТ БАББИТ колодок. Ротор смещается, ОСЕВЫЕ ЗАЗОРЫ ИСЧЕЗАЮТ → задевание и удары → МАССОВЫЙ ОБРЫВ ЛОПАТОК, ИЗГИБ ВАЛА, РАЗРУШЕНИЕ ДИАФРАГМ И ДИСКОВ.** ⚠️ **Смещение ВПЕРЁД даёт ТЕ ЖЕ последствия**

⚠️ **«Цикл отказа»** — главный практический вывод: один подшипник → стружка → забитый фильтр → падение подачи → **страдают остальные**. Отсюда и требование POST 92 проверять стружку на снятом элементе.

---

**🇬🇧 Bearing Fault Consequences — what gets destroyed**

**LOCAL DAMAGE**
⚠️ **Sliding bearings may experience "BEARING BUSH BURNING", where Babbitt metal MELTS AND PEELS OFF due to high temperatures**; rolling bearings suffer increased friction between rolling elements and rings, ⚠️ **leading to wear, cracks or even FRAGMENTATION, ultimately losing their supporting function ENTIRELY**
⚠️ **Bearing damage causes the journal to lose stable support, resulting in radial or axial displacement. Long-term operation leads to journal wear, scratches, or even exceeding the allowable straightness of the shaft, damaging the CONCENTRICITY of the entire shafting**
⚠️ **Shafting displacement is transmitted to the coupling, causing uneven stress or FRACTURE OF COUPLING BOLTS, or wear and misalignment of the coupling end face, FURTHER AMPLIFYING shafting vibration and deviation**

**COMPREHENSIVE UNIT ABNORMALITIES**
⚠️ **Abnormal clearance or component damage causes SEVERE shafting vibration, FAR EXCEEDING safety standards. INTENSE METAL FRICTION AND IMPACT NOISES occur, and in severe cases THE ENTIRE UNIT WILL SHAKE, making stable operation impossible**
⚠️ **Increased friction causes a SHARP RISE in metal and oil return temperature. If it exceeds the trip value the unit shuts down automatically; IF THE PROTECTION DEVICE FAILS, high temperatures may IGNITE LEAKED LUBRICATING OIL, creating a fire hazard**
⚠️ **METAL DEBRIS from bearing damage mixes into the oil, circulates to BLOCK FILTER SCREENS, SCRATCH OIL PUMP GEARS, cause insufficient oil supply or oil deterioration, and further aggravate wear on other bearings and moving parts, forming a "FAULT CYCLE"**

**SAFETY AND ECONOMIC LOSSES**
⚠️ **If the bearing seizes completely, it may cause SUDDEN SHAFTING FRACTURE. High-speed rotating component fragments may PENETRATE THE CASING, leading to EQUIPMENT EXPLOSION; leaked oil in contact with high-temperature components (journals, cylinders) may IGNITE, ENDANGERING THE LIVES of on-site personnel**
⚠️ **Even after repair, key indicators such as shafting precision and bearing fit clearance CAN HARDLY BE FULLY RESTORED** — the unit then runs long-term with vibration and temperature at CRITICAL levels, accelerating ageing of other components and SHORTENING the service life of the entire turbine

**AXIAL DISPLACEMENT — remaining phenomena (continuing POST 76)**
⚠️ **The axial vibration amplitude increases SIGNIFICANTLY and the radial vibration of some units rises SIMULTANEOUSLY. If excessive displacement causes friction between rotating and stationary components, this intensifies further**
⚠️ **An increase in axial thrust will OVERLOAD the thrust bearing, DESTROY THE OIL FILM, and lead to MELTING OF THE BABBITT on the thrust pad segments. The rotor then moves axially, displacement increases, and the AXIAL CLEARANCE between rotating and stationary components DISAPPEARS. Consequently friction and collision occur, resulting in severe damage such as MASSIVE BLADE BREAKAGE, MAIN SHAFT BENDING, DIAPHRAGM AND IMPELLER FRAGMENTATION**
⚠️ **Forward axial movement of the rotor will also cause THE SAME hazards**

⚠️ **The "fault cycle" is the key practical takeaway:** one bearing fails → metal debris enters the oil → filters block → oil supply drops → **other bearings start failing too**. That is exactly why POST 92 requires checking the removed filter element for metal debris.
⚠️ **"If the protection device fails, high temperatures may ignite leaked oil"** connects directly to POST 34 item 4 (**oil return reaching 75°C with smoke**) and the oil fire procedure in POST 57.

`#bearingfault #faultcycle #axialdisplacement #consequences`

---
---

## POST 101 — Majburiy sovutish: tezlik chegarasi

**🇺🇿 Forced cooling — 10°C/soat qoidasi**

⚠️ **ENG MUHIM RAQAM: majburiy sovutish tezligi SOATIGA 10°C DAN KAM bilan cheklanadi** — **TERMIK ZARBADAN metallning shikastlanishining oldini olish uchun.**

**Harorat diapazoni**
⚠️ **Turbina 400°C GACHA tabiiy sovitiladi. Shundan keyin majburiy sovutish FAQAT 400°C dan 150°C gacha ishlatiladi.**
Ya'ni majburiy sovutish **250°C li oyna**da ishlaydi, va 10°C/soat tezlikda bu **kamida 25 SOAT** degani.

**Sovutish davomida nima kuzatiladi**
⚠️ **Sovutish davomida rotorning KUCHLANISH va DXD qiymatlari tekshiriladi** — majburiy sovutishdan kelib chiqadigan **termik deformatsiyani** aniqlash uchun.

**Asboblar havosi (3.15.2.1)**
⚠️ **Majburiy sovutish uchun beriladigan asboblar havosi TURBINA ROTORI bilan HARORAT FARQINI cheklaydi, chunki farq katta bo'lsa turbinaning ICHKI QISMLARI TERMIK DEFORMATSIYAGA uchraydi.**
⚠️ **Turbina rotori harorati 400°C bo'lganda asboblar havosi 150°C bilan cheklanadi — harorat farqi 250°C yoki undan kam.**

Bu POST 17 dagi ruxsat sharti bilan aynan mos: **HP va IP 1-bosqich bug' harorati va berilayotgan havo harorati farqi ≤250°C**.

**Ishga tushirishdan oldingi tekshiruv (5.13.2)**
☑ Main bug' **HPV va IPV YOPIQ**
☑ ⚠️ **Ikkala HRSG to'xtagan va BOSIMSIZ**
☑ ⚠️ **HP tomonidagi HPEV klapani (10LBC12AA101) OCHIQ ekanini tasdiqlang**
☑ **Rotor kuchlanishi, DXD, HP/IP rotor harorati, havo ta'minoti haroratini tekshiring**
☑ ⚠️ **HSPV klapani YOPIQ ekanini tasdiqlang**

**Ishga tushirish (5.13.3)**
1. ⚠️ **HP va IP rotor haroratining ikkalasi ham 400°C DAN PAST ekanini tekshiring** — HP tomoni **10MAA11CT005A/B/C**, IP tomoni **10MAB11CT002A/B/C**
2. ⚠️ **V-001, V-002, V-003, V-004, V-005, V-006 klapanlarini QO'LDA TO'LIQ oching**
3. **Havo qizdirgichini ishga tushiring**

⚠️ **HPEV bu yerda OCHIQ bo'lishi kerak** — POST 32 dagi mantiqqa ko'ra: rotor prewarming holati EMAS va forward flow rejimi EMAS, HP exhaust NRV yopiq → **uchala shart bajariladi → HPEV ochiladi**. Ya'ni majburiy sovutishda HPEV ochiq — sovutuvchi havo chiqib ketishi uchun.

⚠️ **Prewarming da esa HPEV YOPIQ** (POST 26). Ikkalasi bir-biriga teskari: prewarming da bug'ni ushlab qolish kerak, forced cooling da havoni o'tkazish kerak.

**Vaqt hisobi**
| Diapazon | Tezlik | Minimal vaqt |
|---|---|---|
| Ish haroratidan → **400°C** | Tabiiy | — |
| **400°C → 150°C** | ⚠️ **<10°C/soat** | ⚠️ **≥25 soat** |

⚠️ **Majburiy sovutish tabiiy sovutishga nisbatan muddatni 1–2 KUNGA qisqartiradi** (POST 46). Ya'ni tabiiy sovutish bu diapazonda **25 soat + 1–2 kun** davom etadi.

---

**🇷🇺 Принудительное расхолаживание — правило 10°C/час**

⚠️ **ГЛАВНОЕ: скорость расхолаживания ограничена МЕНЕЕ 10°C В ЧАС** — против **повреждения металла ТЕПЛОВЫМ УДАРОМ**

⚠️ **До 400°C турбина остывает естественно. Принудительное расхолаживание применяется ТОЛЬКО от 400°C до 150°C** — окно 250°C, то есть **не менее 25 ЧАСОВ**

⚠️ **В процессе контролируются НАПРЯЖЕНИЯ и ОРС ротора** — для выявления **термической деформации**

**КИП-воздух** — ⚠️ **ограничивает РАЗНИЦУ ТЕМПЕРАТУР с ротором, иначе ТЕРМИЧЕСКАЯ ДЕФОРМАЦИЯ внутренних деталей**; ⚠️ **при 400°C ротора воздух ограничен 150°C — разница не более 250°C**

**Проверки перед пуском** — ГСК ВД и СД **закрыты** | ⚠️ **оба КУ остановлены и БЕЗ ДАВЛЕНИЯ** | ⚠️ **HPEV 10LBC12AA101 ОТКРЫТ** | напряжения, ОРС, температуры | ⚠️ **HSPV ЗАКРЫТ**

**Пуск** — ⚠️ **оба ротора НИЖЕ 400°C** (ВД **10MAA11CT005A/B/C**, СД **10MAB11CT002A/B/C**) → ⚠️ **ВРУЧНУЮ полностью открыть V-001…V-006** → пуск воздухоподогревателя

⚠️ **При расхолаживании HPEV ОТКРЫТ, при прогреве ротора — ЗАКРЫТ.** Логика обратная: при прогреве пар удерживают, при расхолаживании воздух пропускают.

---

**🇬🇧 Forced Cooling — the 10°C/hour rule**

⚠️ **THE KEY FIGURE: forced cooling of the turbine is limited to a cooling rate of LESS THAN 10°C/HOUR to prevent damage to the metal due to THERMAL SHOCK.**

**Temperature window**
⚠️ **The turbine cools naturally down to 400°C. Afterwards, forced cooling can be used ONLY from 400°C to 150°C.**
That is a **250°C window** — at under 10°C/hour, **at least 25 HOURS**.

**What is monitored during cooling**
⚠️ **The stress and DXD values of the rotor during cooling are checked to detect THERMAL DEFORMATION caused by forced cooling.**

**Instrument air (3.15.2.1)**
⚠️ **Instrument air supplied for forced cooling limits the temperature difference with the turbine rotor, because if the difference is large, THERMAL DEFORMATION of the turbine's INTERNAL COMPONENTS can occur.**
⚠️ **It is limited to supplying instrument air of 150°C based on a turbine rotor temperature of 400°C — the temperature difference is limited to 250°C or less.**
This matches exactly the permissive in POST 17: **HP and IP 1st stage steam temp vs supply air temp differential ≤250°C**.

**Pre-start checks (5.13.2)**
☑ Main steam **HPV and IPV closed** ☑ ⚠️ **both HRSGs shut down and NOT PRESSURIZED** ☑ ⚠️ **confirm HPEV 10LBC12AA101 on the HP side is OPEN** ☑ check rotor stress, DXD, HP/IP rotor temperature, air supply temperature ☑ ⚠️ **confirm HSPV is CLOSED**

**Start-up (5.13.3)**
⚠️ **Check both HP and IP rotor temperatures are below 400°C** — HP **10MAA11CT005A/B/C**, IP **10MAB11CT002A/B/C** → ⚠️ **manually fully open valves V-001 through V-006** → start the air heater

⚠️ **HPEV is OPEN here, but CLOSED during rotor prewarming** (POST 26). The logic is inverted on purpose: prewarming holds steam in, forced cooling lets air through.

| Range | Rate | Minimum time |
|---|---|---|
| Operating temp → **400°C** | Natural | — |
| **400°C → 150°C** | ⚠️ **<10°C/hour** | ⚠️ **≥25 hours** |

⚠️ Forced cooling shortens the total by **1–2 days** versus natural cooling (POST 46) — so natural cooling over this window runs **25 hours plus 1–2 days**.

`#forcedcooling #thermalshock #coolingrate #HPEV`

---
---

## POST 102 — Lube oil: qolgan uskuna va mantiq

**🇺🇿 Lube oil — filtr, sovutgich, qizdirgich va EBOP mantiqi**

**Duplex yog' filtri — 10MAV33AT001A/B**
• **2 × 100%**, lube oil kollektorida **sovutgich chiqishida** joylashgan
• ⚠️ **Almashtiriladigan filtr elementlari 10 MIKRONGA hisoblangan**
• ⚠️ **Differensial bosim transmitteri PDIT 10MAV33CP010 bilan kuzatiladi** — filtr ifloslanganda alarm beradi

⚠️ **Uchta yog' filtri, uch xil aniqlik:**
| Filtr | Aniqligi | Joyi |
|---|---|---|
| **Lube oil duplex** | ⚠️ **10 mikron** | Sovutgich chiqishi, kollektor |
| **Jacking oil so'rish** | ⚠️ **50 mikron** | Nasos oldida |
| **Jacking oil chiqish** | ⚠️ **20 mikron** (bir martalik) | Nasosdan keyin |
| **EH (control oil)** | ⚠️ **3 mikron** | Bosim filtrlari |

**Yog' sovutgichlari — 10MAV31AC001 / 10MAV32AC001**
• **2 × 100%** yog'-suv sovutgichi, **asosiy yog' bakining yon tomonida**
• **Bittasi ishda, ikkinchisi zaxirada**
• ⚠️ **Bu bitta sovutgichni TURBINANI TO'XTATMASDAN ta'mir yoki almashtirish uchun chiqarish imkonini beradi**
• Sovutgichlar podshipnik kollektoriga **yuqori va quyi ajratish klapanlari** bilan ulangan. Ajratish klapani faol sovutgichni kollektorga ulaydi va nofaol sovutgichni izolyatsiya qiladi
• ⚠️ **Ikkala ajratish klapani ochiq bo'lsa — ikkala sovutgich BIR VAQTDA ishga solinishi mumkin**

**EBOP ishga tushish mantiqi (3.12.5.12)**
⚠️ **Maqsad: to'xtatish davomida AC dvigatelli nasoslar uchun QUVVAT BO'LMAGAN ba'zi avariyalarda podshipniklarga yog' berish**
⚠️ **Podshipnik yog' kollektor bosimi (PS 10MAV40CP101A/B) < 0.35 barg (Front Standard da) → EBOP dvigatelini ishga tushirish**
⚠️ **Bu mantiq EBOP starter panelidagi ELEKTR BOSHQARUV ZANJIRIDA amalga oshirilishi kerak**
⚠️ **Xavfsiz ekspluatatsiya uchun EBOP ni FAQAT JOYIDAGI STARTER PANELIDAN operator to'xtatishi mumkin**

⚠️ **Bu POST 4 dagi ma'lumotni aniqlashtiradi:** EBOP **0.35 barg** da ishga tushadi (Front Standard da o'lchanadi), trip esa **0.4 barg** da. Ya'ni EBOP trip'dan **0.05 barg oldin** kiradi.

**Botiriladigan qizdirgich boshqaruvi (3.12.5.13)**
Datchik: **TIT 10MAV10CT020A**
• ⚠️ **Harorat KO'TARILGANDA 27°C → Qizdirgich O'CHADI**
• ⚠️ **Harorat PASAYGANDA 20°C → Qizdirgich YOQILADI (ruxsat)**

⚠️ **Gisterezis 7°C.** Ishga tushirish talabi esa **bak harorati ≥10°C** (POST 4). Ya'ni qizdirgich 20°C da yoqilgani uchun bak hech qachon 10°C gacha tushmasligi kerak — agar tushgan bo'lsa, **qizdirgich ishlamayapti**.

**Vapor extractor ventilyatori (3.12.3)**
Sarf **17.6 m³/min** | ⚠️ **To'liq bosim 515 mmAq** | Val quvvati **2.7 kW** | FIK **55%** | Tezlik **2950 rpm**
Dvigatel: chiqish **3.7 kW**, **2950 rpm**, **400 V**, **50 Hz**, izolyatsiya **F**

**MOP zaxira ishga tushish mantiqi (3.12.2.2)**
⚠️ **Ishlayotgan nasos ishdan chiqsa — bosim asbobi (PIT 10MAV23AP001 / 10MAV24AP001) yog' bosimining tushishiga asoslanib zaxira nasosni ishga tushirish uchun signal beradi**
⚠️ **Bitta DC dvigatelli nasos (10MAV27AP001) IKKALA AC dvigatelli nasos ham ishdan chiqqan holatda podshipnik yog'ini ta'minlaydi**
⚠️ **Bundan tashqari, ishlayotgan nasosga QUVVAT UZILSA — zaxira nasos quvvatlanadi**

⚠️ **Ikkita mustaqil ishga tushish sababi:** bosim tushishi **VA** quvvat uzilishi. Ikkinchisi tezroq — bosim tushishini kutmaydi.

---

**🇷🇺 Маслосистема — фильтр, охладители, подогреватель и логика АМН**

**Сдвоенный фильтр 10MAV33AT001A/B** — **2×100%** в коллекторе **за охладителем**, ⚠️ **сменные элементы 10 МИКРОН**, ⚠️ **контроль по PDIT 10MAV33CP010**

⚠️ **Четыре фильтра, четыре тонкости:** смазка **10 мкм** | всас гидроподъёма **50 мкм** | нагнетание гидроподъёма **20 мкм** | ОГ **3 мкм**

**Маслоохладители 10MAV31/32AC001** — **2×100%** масло-вода сбоку бака, один в работе; ⚠️ **позволяет вывести один в ремонт БЕЗ ОСТАНОВА ТУРБИНЫ**; ⚠️ **при открытых обеих задвижках можно включить ОБА ОДНОВРЕМЕННО**

**Логика АМН** — ⚠️ **назначение: подача масла в аварии, когда НЕТ ПИТАНИЯ для насосов переменного тока**; ⚠️ **давление в коллекторе (PS 10MAV40CP101A/B) < 0.35 барг (на переднем стуле) → пуск АМН**; ⚠️ **логика реализуется в ЭЛЕКТРИЧЕСКОЙ ЦЕПИ панели АМН**; ⚠️ **останов ТОЛЬКО с МЕСТНОЙ панели**
⚠️ **АМН пускается на 0.35 барг, защита — на 0.4 барг: запас 0.05 барг**

**Погружной подогреватель (TIT 10MAV10CT020A)** — ⚠️ **при РОСТЕ до 27°C ВЫКЛ**, ⚠️ **при СНИЖЕНИИ до 20°C ВКЛ**; гистерезис **7°C**
⚠️ Пусковое требование — бак **≥10°C**; если уровень опустился ниже, **подогреватель не работает**

**Эксгаустер** — **17.6 м³/мин**, ⚠️ **полное давление 515 мм в.ст.**, вал **2.7 кВт**, КПД **55%**, **2950 об/мин**; двигатель **3.7 кВт**, **400 В**, **F**

**АВР МНС** — ⚠️ **PIT 10MAV23AP001/10MAV24AP001 по падению давления**; ⚠️ **АМН — при отказе ОБОИХ насосов переменного тока**; ⚠️ **резервный запускается ТАКЖЕ при потере питания рабочего**

---

**🇬🇧 Lube Oil — remaining equipment and logic**

**Duplex oil filters 10MAV33AT001A/B** — **2 × 100%** in the lube oil header **at the cooler discharge**; ⚠️ **replaceable filter elements are rated at 10 MICRONS**; ⚠️ **alarm monitored by differential pressure transmitter PDIT 10MAV33CP010**

⚠️ **Four oil filters, four ratings:** lube oil duplex **10 micron** | jacking oil suction **50 micron** | jacking oil discharge **20 micron** (disposable) | EH control oil **3 micron**

**Oil coolers 10MAV31AC001 / 10MAV32AC001** — **2 × 100%** oil-to-water coolers on the side of the main reservoir, one in use and one in reserve; ⚠️ **this permits removal of one cooler from service for repair or replacement WITHOUT HAVING TO SHUT DOWN THE TURBINE**; connected to the bearing header with upstream and downstream isolation valves; ⚠️ **if both isolation valves are open, both coolers may be placed in service simultaneously**

**EBOP start logic (3.12.5.12)**
⚠️ **Purpose: to supply lube oil to bearings in some emergencies when NO POWER IS AVAILABLE for the AC motor driven pumps during shutdown**
⚠️ **Bearing Oil Header Pressure (PS 10MAV40CP101A/B) < 0.35 barg (at Front Standard) → start EBOP motor**
⚠️ **This logic should be implemented by the ELECTRICAL CONTROL CIRCUIT in the EBOP starter panel**
⚠️ **For safe operation, EBOP can be stopped ONLY in the LOCAL STARTER PANEL by the operator**
⚠️ EBOP starts at **0.35 barg**, the trip is at **0.4 barg** — EBOP comes in **0.05 barg before** the trip.

**Immersion heater control (3.12.5.13)** — sensor **TIT 10MAV10CT020A**
⚠️ **Temperature INCREASING to 27°C → Heater OFF** | ⚠️ **Temperature DECREASING to 20°C → Heater ON (Enable)**
⚠️ Hysteresis is **7°C**. The start permissive is reservoir **≥10°C** — with the heater cutting in at 20°C, the tank should never reach 10°C. If it has, **the heater is not working.**

**Vapor extractor fan** — flow **17.6 m³/min**, ⚠️ **total pressure 515 mmAq**, shaft power **2.7 kW**, efficiency **55%**, speed **2950 rpm**; motor output **3.7 kW**, **2950 rpm**, **400 V**, **50 Hz**, insulation **F**

**MOP standby start logic (3.12.2.2)**
⚠️ **If the operating pump fails, a pressure instrument (PIT 10MAV23AP001 / 10MAV24AP001) will provide a signal to start the backup pump based on a drop in oil pressure**
⚠️ **One DC motor-driven pump (10MAV27AP001) provides bearing oil in the event that BOTH AC motor-driven pumps fail**
⚠️ **Additionally, if POWER to an operating pump is INTERRUPTED, the backup pump will be energized**
⚠️ Two independent triggers — pressure drop **and** power loss. The second acts faster because it doesn't wait for pressure to fall.

`#luboil #filters #EBOP #immersionheater`

---
---

## POST 103 — Zaxira nasos interloklari: barchasi bir joyda

**🇺🇿 Avtomatik ishga tushish nuqtalari — to'liq jadval**

| Tizim | Zaxira ishga tushish sharti | KKS / izoh |
|---|---|---|
| **ACCWS** | ⚠️ **Kollektor bosimi ≤0.24 MPa** | Haftalik sinaladi |
| **CCWS** | ⚠️ **Umumiy kollektor bosimi 2.0 bar** yoki ishlayotgan nasos tripi | 11.3.2 da **≤0.2 MPa** |
| **CCCWS** | ⚠️ **Nasos chiqish bosimi ≤6 bar** | Haftalik sinov **≤0.6 MPa** |
| **Kondensat** | ⚠️ **Umumiy kollektor bosimi 15 bar** yoki ishlayotgan nasos tripi | 11.4.2 da **≤1.5 MPa** |
| **Lube oil MOP** | ⚠️ **PS 10MAV17CP101A/B** past bosim | PIT 10MAV23/24AP001 |
| **Lube oil EBOP** | ⚠️ **PS 10MAV40CP101A/B < 0.35 barg** | + AC quvvat yo'qolishi |
| **Jacking oil** | ⚠️ **PIT 10MAV10CP002A/B** | JOP 380 rpm da ham |
| **Control oil (EH)** | ⚠️ **Ishlayotgan nasos tripi YOKI kollektor past bosim alarmi (131 bar)** | — |
| **Seal oil MSOP** | ⚠️ **MSOP chiqish bosimi <8.5 bar** | Interlok |
| **Seal oil ESOP** | ⚠️ **Umumiy bosim s/w #1 <7 bar** | Interlok |
| **Stator suvi** | ⚠️ **Nasos A yoki B chiqish bosimi past** | ⚠️ **5 sekund ichida ishga tushishi shart** |
| **Vakuum nasos** | ⚠️ **Kollektor bosimi ≥12 kPa** | ⚠️ **YUQORI bosim interloki — boshqalari past bosim!** |
| **Gland steam blower** | ⚠️ **GSC bosimi > −0.015 barg** | Avto-o'tish mantiqi bilan |

⚠️ **DIQQAT — vakuum nasos YAGONA istisno.** Barcha boshqa tizimlarda zaxira **BOSIM TUSHGANDA** kiradi, vakuum tizimida esa **BOSIM KO'TARILGANDA** (vakuum yomonlashganda). Interlok sinovida buni chalkashtirmang.

**Haftalik interlok sinovlari (11-bob)**
| Tizim | Sinov qiymati |
|---|---|
| **ACCWS** | ⚠️ **≤0.24 MPa** |
| **CCWS** | ⚠️ **≤0.2 MPa** |
| **CCCWS** | ⚠️ **≤0.6 MPa** |
| **Kondensat** | ⚠️ **≤1.5 MPa** |
| **Vakuum** | ⚠️ **≥12 kPa** |
| **Lube oil** | ⚠️ **Asosiy nasos bosimini sozlama nuqtasigacha tushirish** |
| **Stator suvi** | ⚠️ **Asosiy nasos quvvatini uzish, 5 sekund** |

**Zaxira nasos klapan holati — TESKARI**
| Tizim | Zaxira nasos chiqish klapani |
|---|---|
| **ACCWS** | ⚠️ **TO'LIQ OCHIQ** |
| **CCWS** | ⚠️ **TO'LIQ YOPIQ** |
| **Kondensat** | ⚠️ **TO'LIQ OCHIQ** |
| **Vakuum** | ⚠️ **Kirish pnevmatik klapani TO'LIQ YOPIQ** |

⚠️ **Bu haftalik tekshiruvda eng ko'p chalkashtiriladigan joy.** CCWS zaxira nasosining klapani yopiq turadi (gidravlik butterfly, nasos bilan birga ochiladi), ACCWS va kondensatniki esa ochiq turadi.

**Dvigatel me'yorlari — tizim bo'yicha**
| Tizim | Tebranish | Podshipnik | O'ram |
|---|---|---|---|
| **ACCWS** | ⚠️ **<50 μm** (yuritilmagan uch) | **<85°C** | **<110°C** |
| **CCWS** | ⚠️ **<50 μm** (yuritilmagan uch) | **<95°C** | **<130°C** |
| **CCCWS** | ⚠️ **≤4.5 mm/s** | **≤70°C** (nasos) | — |
| **Kondensat** | ⚠️ **<4.5 mm/s** | **<95°C** | **<125°C**, tok **≤110 A** |
| **Vakuum** | ⚠️ **<4.5 mm/s** | **<80°C** | **<120°C** |
| **Stator suvi** | ⚠️ **≤0.05 mm** (mufta) | **≤70°C** (korpus) | shovqin **≤85 dB** |

⚠️ **Birliklar ARALASH: μm, mm/s va mm.** ACCWS va CCWS **μm** da, qolganlari **mm/s** da, stator suvi **mm** da. Bir jadvalga solishtirib bo'lmaydi — har birini o'z birligida o'qing.

---

**🇷🇺 Уставки АВР — сводная таблица**

| Система | Условие пуска резервного |
|---|---|
| **ВЦОС** | ⚠️ **коллектор ≤0.24 МПа** |
| **ЦОС** | ⚠️ **коллектор 2.0 бар** или отключение рабочего |
| **ЗКОС** | ⚠️ **нагнетание ≤6 бар** |
| **Конденсат** | ⚠️ **коллектор 15 бар** или отключение рабочего |
| **МНС** | ⚠️ **PS 10MAV17CP101A/B** |
| **АМН** | ⚠️ **PS 10MAV40CP101A/B < 0.35 барг** + потеря питания |
| **Гидроподъём** | ⚠️ **PIT 10MAV10CP002A/B**, и 380 об/мин |
| **ОГ** | ⚠️ **отключение рабочего ИЛИ сигнал 131 бар** |
| **ОНУМ** | ⚠️ **<8.5 бар** | **АНУМ** ⚠️ **<7 бар** |
| **Статорная вода** | ⚠️ **низкое давление, пуск ЗА 5 СЕКУНД** |
| **Вакуумный насос** | ⚠️ **коллектор ≥12 кПа — ВЫСОКОЕ давление!** |
| **Эксгаустер СП** | ⚠️ **> −0.015 барг** |

⚠️ **Вакуумный насос — ЕДИНСТВЕННОЕ исключение: резерв включается по РОСТУ давления, а не по падению.**

**Положение задвижки резервного — РАЗНОЕ:** ВЦОС **ОТКРЫТА** | ЦОС **ЗАКРЫТА** | конденсат **ОТКРЫТА** | вакуум **вход ЗАКРЫТ**

**Нормы двигателей** — ВЦОС ⚠️ **<50 мкм / <85°C / <110°C** | ЦОС ⚠️ **<50 мкм / <95°C / <130°C** | ЗКОС ⚠️ **≤4.5 мм/с / ≤70°C** | конденсат ⚠️ **<4.5 мм/с / <95°C / <125°C / ≤110 А** | вакуум ⚠️ **<4.5 мм/с / <80°C / <120°C** | статорная вода ⚠️ **≤0.05 мм / ≤70°C / ≤85 дБ**

⚠️ **Единицы СМЕШАНЫ: мкм, мм/с и мм.** Сравнивать напрямую нельзя.

---

**🇬🇧 Standby Pump Interlocks — all in one table**

| System | Standby start condition |
|---|---|
| **ACCWS** | ⚠️ **header pressure ≤0.24 MPa** |
| **CCWS** | ⚠️ **common header 2.0 bar** or operating pump trip |
| **CCCWS** | ⚠️ **pump outlet ≤6 bar** (weekly test ≤0.6 MPa) |
| **Condensate** | ⚠️ **common header 15 bar** or operating pump trip |
| **Lube oil MOP** | ⚠️ **PS 10MAV17CP101A/B** low pressure |
| **Lube oil EBOP** | ⚠️ **PS 10MAV40CP101A/B < 0.35 barg** + AC power loss |
| **Jacking oil** | ⚠️ **PIT 10MAV10CP002A/B**, plus 380 rpm start |
| **Control oil (EH)** | ⚠️ **running pump trip OR header low pressure alarm (131 bar)** |
| **Seal oil MSOP** | ⚠️ **MSOP discharge <8.5 bar** |
| **Seal oil ESOP** | ⚠️ **common pressure s/w #1 <7 bar** |
| **Stator water** | ⚠️ **pump A or B discharge low — must start WITHIN 5 SECONDS** |
| **Vacuum pump** | ⚠️ **header pressure ≥12 kPa — a HIGH pressure interlock!** |
| **Gland steam blower** | ⚠️ **GSC pressure > −0.015 barg** |

⚠️ **The vacuum pump is the ONLY exception.** Every other system starts its standby on FALLING pressure; the vacuum system starts on RISING pressure (degrading vacuum). Don't mix them up during interlock testing.

**Standby pump valve state — it differs by system**
ACCWS ⚠️ **FULL OPEN** | CCWS ⚠️ **FULL CLOSED** | Condensate ⚠️ **FULL OPEN** | Vacuum ⚠️ **inlet pneumatic valve FULL CLOSED**
⚠️ **This is the most commonly confused item in the weekly check.** The CCWS standby outlet stays closed (hydraulic butterfly, opens with the pump); ACCWS and condensate stay open.

**Motor limits by system**
ACCWS ⚠️ **<50 μm (non-driven end) / <85°C / <110°C** | CCWS ⚠️ **<50 μm / <95°C / <130°C** | CCCWS ⚠️ **≤4.5 mm/s / ≤70°C pump bearing** | Condensate ⚠️ **<4.5 mm/s / <95°C / <125°C, current ≤110 A** | Vacuum ⚠️ **<4.5 mm/s / <80°C / <120°C** | Stator water ⚠️ **≤0.05 mm coupling / ≤70°C casing / ≤85 dB**

⚠️ **Units are MIXED: μm, mm/s and mm.** ACCWS and CCWS are in μm, most others in mm/s, stator water in mm. They cannot be compared directly.

`#interlocks #standbypump #reference #motorlimits`

---
---

## POST 104 — Kondensator sathi va uzoq to'xtash

**🇺🇿 Hot well — besh sath va konservatsiya**

**Besh sath sozlamasi (3.10.3)**
⚠️ **Kondensator hot well suv sathi sozlamasi BESH darajaga bo'lingan:**
| Daraja | Ta'sir |
|---|---|
| **Past ikkinchi sath** | ⚠️ **Zanjirli himoya (chain protection)** |
| **Past birinchi sath** | ⚠️ **Alarm va suv to'ldirish** |
| **Normal sath** | — |
| **Yuqori birinchi sath** | ⚠️ **Alarm** |
| **Yuqori ikkinchi sath** | ⚠️ **To'xtatish (shutdown)** |

Bu POST 13 dagi raqamlarga mos: **LL 1340 mm** (trip) → **L 1490 mm** (alarm + make-up) → normal → **H 2240 mm** (alarm) → **HH 2390 mm** (alarm + bypass yopilishi).

**Hot well hajmi**
⚠️ **Hot well normal sathda MA'LUM DAQIQALIK kondensat suvini saqlaydi**, va chiqish normal sathda butun kondensatni **1 SOAT ICHIDA** chiqara oladi (POST 40).

**UZOQ TO'XTASHDA KONSERVATSIYA**
⚠️ **To'xtatishdan keyin UZOQ MUDDAT to'xtatilsa — kondensatordagi SOVUTISH SUVI VA KONDENSAT SUVI CHIQARILISHI SHART, ZANGLASH KORROZIYASINING oldini olish uchun.**
⚠️ **Ayniqsa SOVUTISH QUVURINING ICHKI VA TASHQI YUZALARI PUFLAB QURITILISHI yoki quritilishi kerak — quvurning PITTING KORROZIYASINING oldini olish uchun.**

⚠️ **Bu 27 908 ta TP316L quvur haqida.** Ular ichida suv qolsa, uzoq to'xtash davomida pitting boshlanadi va keyin sizish beradi — POST 63 dagi "quvur sizishi kondensatni suyultiradi" zanjiri shundan boshlanadi.

**KONDENSATOR TAYANCHLARI (3.10.3, 4-band)**
• ⚠️ **Kondensator korpusining tagida IKKI QATOR tayanch, bo'ynida esa BIR QATOR tayanch** — turli ish sharoitlarida kondensator yuklamasini yaxshiroq ko'tarish uchun
• ⚠️ **PAST ISHQALANISH KOEFFITSIENTI kondensatorning gorizontal yo'nalishdagi TERMIK KENGAYISH QARSHILIGINI kamaytiradi**
• ⚠️ **Korpusning ikki qator tayanchi ORASIDA CHEGARALOVCHI TAYANCH o'rnatilgan — kondensatorning harakat yo'nalishini boshqaradi va kondensatorning O'Z HOLICHA TEBRANISHINING oldini oladi**

**Vakuum nasos ishlash tamoyili (3.10.4)**
⚠️ **Suyuq halqali tipda: rotor doiraviy korpus ichida METALL BILAN ALOQASIZ aylanadi, korpusda suyuq kompressor bor.**
• Rotor — **ichi bo'sh silindrik stupitsadan chiqadigan bir qator kuraklardan** iborat quyma, stupitsaga val presslangan
• ⚠️ **Kuraklar yon tomonlardan QOPLANGAN va bir qator KAMERALAR hosil qiladi**
• ⚠️ **Kuraklarning egriligi AYLANISH YO'NALISHIDA**
• ⚠️ **Korpus val markaziy chizig'idan SILJITILGAN (offset)**

Aynan shu **offset** tufayli aylanish davomida har bir kameraning hajmi o'zgaradi — so'rish va siqish shu tariqa yuzaga keladi.

**Bug' sifati namuna olish nuqtasi (7.2.1)**
⚠️ **Bug' sifati namuna olish nuqtasi turbinaga oqib kiradigan bug'ga IMKON QADAR YAQIN sharoitda — YAKUNIY SUPERQIZDIRGICH/REHEATER VA TURBINA KLAPANI ORASIDA namuna olish orqali tahlil qilinishi SHART**

**Haqiqiy bug' sifati nimaga bog'liq**
1. ⚠️ **Qozon suvi tarkibiy qismlarining UCHUVCHANLIGI** — qozon bosimiga bog'liq
2. ⚠️ **Qozon suvi tomchilarining MEXANIK O'TISHI**
3. ⚠️ **Attemperator uchun bug'ga oziqlantiruvchi suv PURKASH**
4. ⚠️ **Qozon, superqizdirgich, reheater, bug' quvurlari, klapanlar va bug' siklining boshqa qismlari yuzasidan CHO'KMA VA KORROZIYA MAHSULOTLARINING AJRALIB CHIQISHI**

**Aralashmalarning turbina materiali bilan o'zaro ta'siri**
⚠️ **Bu aralashmalarning bug'dagi ERUVCHANLIGI va ularning material yuzasida AJRALISHI hamda CHO'KISHI bilan belgilanadi.**
⚠️ **Ajralish va cho'kish HAQIQIY ARALASHMA KONSENTRATSIYASI (bug' KENGAYISHI tufayli) ERITMADAGI ERUVCHANLIK CHEGARASIDAN OSHGANDA yuz beradi.**
⚠️ **Suv tomchilari yoki suv plyonkasi hosil bo'lganda — suyuq fazaga aralashmalar KIRIB BORADI va AGRESSIV MUHIT hosil qiladi.**

⚠️ **Amaliy xulosa: bug' sifati muammosi qozonda boshlanadi, lekin ZARAR turbinada, aynan BUG' KENGAYIB ERUVCHANLIK CHEGARASIDAN OSHGAN BOSQICHDA yuzaga keladi** — shuning uchun POST 62 dagi "ho'l bug' sohasidagi kuraklar pitting beradi" mantiqiy davomi.

---

**🇷🇺 Конденсатосборник — пять уровней и консервация**

⚠️ **Уровень разделён на ПЯТЬ ступеней:** низкий второй — ⚠️ **блокировочная защита** | низкий первый — ⚠️ **сигнал и подпитка** | нормальный | высокий первый — ⚠️ **сигнал** | высокий второй — ⚠️ **останов**
Соответствует POST 13: **LL 1340 → L 1490 → норма → H 2240 → HH 2390 мм**

**КОНСЕРВАЦИЯ** — ⚠️ **при ДЛИТЕЛЬНОМ простое циркводу и конденсат СЛИТЬ против РЖАВЛЕНИЯ**; ⚠️ **внутренние и наружные поверхности трубок ПРОДУТЬ И ВЫСУШИТЬ против ПИТТИНГА**
⚠️ Речь о **27 908 трубках TP316L** — оставленная вода даёт питтинг, затем течь.

**ОПОРЫ** — ⚠️ **ДВА РЯДА снизу корпуса и ОДИН РЯД на горловине**; ⚠️ **НИЗКИЙ КОЭФФИЦИЕНТ ТРЕНИЯ снижает сопротивление горизонтальному тепловому расширению**; ⚠️ **МЕЖДУ двумя рядами — ОГРАНИЧИТЕЛЬНАЯ ОПОРА, задающая направление перемещения и не дающая конденсатору РАСКАЧИВАТЬСЯ**

**Принцип вакуумного насоса** — ⚠️ **ротор вращается БЕЗ МЕТАЛЛИЧЕСКОГО КОНТАКТА**; ⚠️ **лопатки закрыты с боков и образуют КАМЕРЫ**; ⚠️ **кривизна лопаток ПО НАПРАВЛЕНИЮ ВРАЩЕНИЯ**; ⚠️ **корпус СМЕЩЁН относительно оси вала** — именно смещение создаёт изменение объёма камер

**Пробоотбор пара** — ⚠️ **МАКСИМАЛЬНО БЛИЗКО к пару, идущему в турбину, МЕЖДУ последним пароперегревателем/промперегревателем И КЛАПАНОМ ТУРБИНЫ**
Качество определяется ⚠️ **летучестью компонентов котловой воды, механическим уносом капель, впрыском питательной воды на пароохлаждение, вымыванием отложений и продуктов коррозии**
⚠️ **Отложение происходит, когда концентрация примесей (из-за РАСШИРЕНИЯ пара) ПРЕВЫШАЕТ предел растворимости**; ⚠️ **в каплях и плёнке примеси создают АГРЕССИВНУЮ СРЕДУ**

---

**🇬🇧 Condenser Hot Well — five levels and preservation**

**Five level settings (3.10.3)**
⚠️ **The hot well water level setting is divided into five levels:** low two (⚠️ **chain protection**), low one (⚠️ **alarm and water replenishment**), normal, high one (⚠️ **alarm**), high two (⚠️ **shutdown**)
Matching POST 13: **LL 1340 → L 1490 → normal → H 2240 → HH 2390 mm**

**LONG SHUTDOWN PRESERVATION**
⚠️ **When there is a long-term shutdown, the cooling water and condensate water in the condenser MUST be discharged to prevent RUST CORROSION.**
⚠️ **Especially the INNER AND OUTER SURFACES of the cooling tubes should be BLOW-DRIED or dried to prevent PITTING CORROSION of the cooling tube.**
⚠️ This concerns **27,908 TP316L tubes**. Water left inside starts pitting during a long outage, and pitting later becomes the tube leak in the POST 63 chain.

**Condenser supports (3.10.3, item 4)**
⚠️ **TWO ROWS of bearing support at the bottom of the shell and ONE ROW at the neck**, to better bear the load under various working conditions
⚠️ **The LOW FRICTION COEFFICIENT reduces the thermal expansion resistance of the condenser in the horizontal direction**
⚠️ **A LIMIT SUPPORT is set BETWEEN the two rows of bearing supports, which controls the moving direction and prevents the condenser from SWINGING AT WILL**

**Vacuum pump working principle (3.10.4)**
⚠️ **Liquid ring type: a rotor revolves WITHOUT METAL CONTACT in a circular body that contains a liquid compressor.** The rotor is a casting consisting of a series of blades projecting from a hollow cylindrical hub through which the shaft is pressed. ⚠️ **These blades are SHROUDED at the sides and form a series of CHAMBERS.** ⚠️ **The curvature of the blades is IN THE DIRECTION OF ROTATION.** ⚠️ **The body is OFFSET from the centre line of the shaft** — that offset is what varies each chamber's volume through a revolution, creating suction and compression.

**Steam purity sampling point (7.2.1)**
⚠️ **Steam purity sampling point must be analyzed by sampling steam in conditions AS CLOSE AS POSSIBLE to the steam flowing into the turbine, BETWEEN THE FINAL SUPERHEATER/REHEATER AND THE TURBINE VALVE.**

**Actual steam quality is determined by**
⚠️ **Volatility of boiler water constituents depending on boiler pressure** | ⚠️ **Mechanical transfer of droplets of boiler water** | ⚠️ **Injection of feed water into steam for attemperator** | ⚠️ **Release of sediments and corrosion products from the surfaces of boilers, superheater, reheater, steam pipes, valves and other parts of the steam cycle**

**Interaction with turbine material**
⚠️ **Determined by the SOLUBILITY of these impurities in steam and by their SEPARATION AND DEPOSITION on material surfaces.**
⚠️ **Separation and deposition can happen when the actual impurity concentration exceeds — DUE TO STEAM EXPANSION — the solubility limit in solution.**
⚠️ **When water droplets or a water film form, impurities penetrate into the liquid phase and form an AGGRESSIVE ENVIRONMENT.**

⚠️ **The practical point: a steam purity problem starts in the boiler but the DAMAGE happens in the turbine, at exactly the stage where expansion pushes concentration past the solubility limit** — which is why blades in the wet steam area pit (POST 62).

`#hotwell #preservation #pitting #vacuumpump #steampurity`

---
---

## POST 105 — Suv kirishini aniqlashning uchinchi vazifasi

**🇺🇿 Suv detektori — yuqori oqim nosozliklarining bilvosita ogohlantirishi**

**Silindrga suv kirishining sabablari**
⚠️ **Silindrga suv kirishi KO'PINCHA DRENAJ TIZIMI NOSOZLIGIDAN (masalan drenaj klapanining tiqilishi, drenaj quvurida suv to'planishi) yoki OZIQLANTIRUVCHI/KONDENSAT TIZIMI ANOMALIYASIDAN (masalan qizdirgich sizishi) kelib chiqadi.**

**Bilvosita ogohlantirish — 2 ta zanjir**

*1. Drenaj tizimi*
⚠️ **Silindr drenaj nuqtasida (masalan HP va IP silindr drenaji, bug' quvuri drenaji) SUV ANIQLANSA — bug' tutgichi NORMAL OCHILMAYOTGANINI yoki QUVUR TIQILGANINI darhol aniqlash mumkin, va to'plangan suvning TO'SATDAN SILINDRGA KIRISHINING oldini olish mumkin.**

*2. Qizdirgich sizishining erta ogohlantirishi*
⚠️ **LP silindrda suv paydo bo'lsa — ko'pincha bu PAST BOSIMLI QIZDIRGICH QUVUR BOG'LAMINING SIZISHI (kondensat bug' tomoniga sizib silindrga kiradi). Aniqlash qizdirgichni tekshirishga turtki beradi va sizishning kengayishining oldini oladi.**

**Uchinchi vazifa — "O'Z VAQTIDALIK"**
⚠️ **Suv aniqlashning ASOSIY VAZIFASI birlikni avariya to'xtatishining "O'Z VAQTIDALIGINI" ta'minlashdir.**
⚠️ **Silindrda suv aniqlangach tizim himoya mantiqini TEZ ULAYDI.**

⚠️ **Bu POST 24 va 25 ni to'ldiradi:** POST 24 **qanday aniqlanishini**, POST 25 **operator nima qilishini**, bu post esa **detektor nima uchun ham kerakligini** ko'rsatadi — u faqat turbinani himoya qilmaydi, balki **drenaj va qizdirgich nosozligini ham oshkor qiladi**.

**Amaliy xulosa — uch bosqichli o'qish**
| Qayerda suv aniqlandi | Nima haqida ogohlantiradi |
|---|---|
| ⚠️ **HP/IP silindr drenaji** | ⚠️ **Bug' tutgichi ochilmayapti YOKI quvur tiqilgan** |
| ⚠️ **Bug' quvuri drenaji** | ⚠️ **Xuddi shu** |
| ⚠️ **LP silindr** | ⚠️ **Past bosimli qizdirgich quvur bog'lamining sizishi** |

**Tebranish chegaralari (Table 7-1-2)**
⚠️ **Bu jadval EKSPLUATATSIYA YO'RIQNOMASI sifatida berilgan va tebranish monitoring tizimining ALARM VA TRIP qiymatlari sifatida ishlatiladi.**

| Kuzatiladigan tebranish | Alarm | Trip | Izoh |
|---|---|---|---|
| **Valning nisbiy siljishi** | **165 μm** | **240 μm** | ⚠️ **Peak-Peak** |

⚠️ **"Peak-Peak" — bu muhim.** Ba'zi asboblar RMS yoki peak ko'rsatadi. **165 va 240 μm — peak-to-peak qiymatlar.** Asbob boshqa rejimda bo'lsa ko'rsatkich noto'g'ri talqin qilinadi.

**Termik sezuvchanlik haqida qo'shimcha (7.1.4)**
⚠️ **Agar shunday holat topilsa — BUTUN ISH HARORATI DIAPAZONIDA maqbul tebranish darajasini beradigan MUROSALI MUVOZANAT ishlab chiqish zarur bo'lishi mumkin.**
⚠️ **Buning oldini olish uchun KESKIN HARORAT O'ZGARISHLARIDAN QOCHISH kerak.**

⚠️ **Ya'ni termik sezuvchan rotorni "to'g'rilab" bo'lmaydi** — uni faqat **kompromis muvozanat** bilan boshqarish mumkin, va eng yaxshi chora — **haroratni sekin o'zgartirish**. POST 61 dagi barcha tezlik chegaralari (qizdirish 1.5–2.5°C/min, bug' tebranishi ±5°C/min) aynan shu uchun.

---

**🇷🇺 Детектор воды — косвенное предупреждение о дефектах выше по тракту**

⚠️ **Заброс воды ЧАЩЕ ВСЕГО от ОТКАЗА ДРЕНАЖНОЙ СИСТЕМЫ (забитый клапан, скопление воды в дренаже) или АНОМАЛИИ ПИТАТЕЛЬНОГО/КОНДЕНСАТНОГО тракта (течь подогревателя)**

⚠️ **Вода в дренаже цилиндра или паропровода → НЕМЕДЛЕННО ясно, что конденсатоотводчик НЕ ОТКРЫВАЕТСЯ или ТРУБОПРОВОД ЗАБИТ**, что позволяет не допустить ВНЕЗАПНОГО заброса
⚠️ **Вода в ЦНД → чаще всего ТЕЧЬ ТРУБНОГО ПУЧКА ПНД** (конденсат в паровое пространство), сигнал к осмотру подогревателя

⚠️ **ОСНОВНАЯ функция — обеспечить «СВОЕВРЕМЕННОСТЬ» аварийного останова**; ⚠️ **при обнаружении воды система БЫСТРО задействует защитную логику**

**Пределы вибрации (Table 7-1-2)** — ⚠️ **относительное смещение вала: сигнал 165 мкм, защита 240 мкм, РАЗМАХ (Peak-Peak)**
⚠️ **«Размах» важен** — часть приборов показывает RMS или амплитуду; при другом режиме показания истолкуют неверно

⚠️ **Термочувствительный ротор «выправить» нельзя** — нужен **КОМПРОМИССНЫЙ БАЛАНС** по всему диапазону температур, а лучшая мера — ⚠️ **ИЗБЕГАТЬ РЕЗКИХ ИЗМЕНЕНИЙ ТЕМПЕРАТУРЫ**

---

**🇬🇧 Water Detection — indirect warning of upstream faults**

**Causes of cylinder water intake**
⚠️ **Cylinder water intake is often caused by DRAIN SYSTEM FAILURE (such as drain valve blockage, drain pipe water accumulation) or FEED/CONDENSATE SYSTEM ANOMALY (such as heater leakage).**

**Two indirect warning chains**
⚠️ **If the cylinder drainage point (HP and IP cylinder drainage, steam pipe drainage) detects water, you can IMMEDIATELY DETERMINE that the trap is not opening normally or the pipeline is blocked — avoiding accumulated water suddenly entering the cylinder.**
⚠️ **Early warning of heater leakage: if the low-pressure cylinder takes water, it is most often LP HEATER TUBE BUNDLE LEAKAGE (condensate leaking into the steam side and into the cylinder). Detection triggers inspection of the heater to prevent the leakage expanding.**

**The third function — "TIMELINESS"**
⚠️ **The core function of water detection is to ensure the "TIMELINESS" of emergency unit shutdown.**
⚠️ **When water is detected in the cylinder, the system will QUICKLY LINK THE PROTECTION LOGIC.**

⚠️ **This completes POST 24 and 25:** POST 24 covers **how it is detected**, POST 25 **what the operator does**, and this post **why the detector exists at all** — it protects the turbine and simultaneously **exposes drain and heater faults**.

| Where water is detected | What it warns about |
|---|---|
| ⚠️ **HP/IP cylinder drain** | ⚠️ **Trap not opening OR pipeline blocked** |
| ⚠️ **Steam pipe drain** | ⚠️ **Same** |
| ⚠️ **LP cylinder** | ⚠️ **LP heater tube bundle leakage** |

**Vibration limits (Table 7-1-2)**
⚠️ **These are provided as an OPERATION GUIDELINE and are used as the ALARM AND TRIP values of the vibration monitoring system.**

| Vibration monitored | Alarm | Trip | Remark |
|---|---|---|---|
| **Relative shaft displacement** | **165 μm** | **240 μm** | ⚠️ **Peak-Peak** |

⚠️ **"Peak-Peak" matters.** Some instruments display RMS or single peak. **165 and 240 μm are peak-to-peak values** — a differently configured instrument will be misread.

**On thermal sensitivity (7.1.4)**
⚠️ **If such a condition is found, it might be necessary to develop a COMPROMISE BALANCE that will produce acceptable vibration levels OVER THE WHOLE OPERATING TEMPERATURE RANGE.**
⚠️ **To avoid this, ABRUPT TEMPERATURE CHANGES SHOULD BE AVOIDED.**
⚠️ In other words a thermally sensitive rotor cannot be "fixed" — it can only be managed with a compromise balance, and the real remedy is slow temperature change. That is exactly why every rate limit in POST 61 exists.

`#waterdetection #drains #LPheater #vibrationlimits #peaktopeak`
