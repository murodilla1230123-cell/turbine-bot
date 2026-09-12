# @enersok_edu — ST kontent boti

Syrdarya 2 bug' turbinasi bo'yicha **105 ta uch tilli post** (o'zbek / rus / ingliz).
GitHub Actions kuniga **2 ta post** joylaydi — **sutkaning tasodifiy vaqtlarida**.
Server kerak emas, bepul.

**Manba:** SYR2-073-MAN-OM-3625 Rev.00, Harbin Electric, 371 bet — to'liq o'qilgan.
**Auditoriya:** 5–15 yillik tajribali stansiya operatorlari.

---

## Ishga tushirish — 5 qadam

### 1. Bot yarating
Telegramda [@BotFather](https://t.me/BotFather) ga yozing:
```
/newbot
```
Nom va username bering. **Token**ni saqlang — `123456789:AAH...` ko'rinishida.

### 2. Botni kanalga qo'shing
Kanal → Administrators → Add Admin → botingizni tanlang.
Ruxsat: **Post Messages** (yetarli).

### 3. Repoga yuklang
```bash
git init
git add .
git commit -m "enersok edu bot"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

### 4. Secrets qo'shing
GitHub → repo → **Settings → Secrets and variables → Actions → New repository secret**

| Nomi | Qiymati |
|---|---|
| `BOT_TOKEN` | BotFather bergan token |
| `CHANNEL_ID` | `@enersok_edu` yoki `-1001234567890` |

### 5. Sinab ko'ring
**Actions → Kunlik post → Run workflow** → `dry_run` ni `1` qiling → Run.
Log da post matni ko'rinadi, lekin kanalga yuborilmaydi.

Hammasi joyida bo'lsa `dry_run` ni `0` qilib qayta ishga tushiring.

---

## Jadval — tasodifiy

Workflow **har soat** ishga tushadi (`17 * * * *`), lekin har safar post
yubormaydi. Bot har kuni ertalab **2 ta tasodifiy vaqt** tanlaydi va faqat
o'sha vaqt kelganda post qo'yadi.

Misol — ketma-ket kunlar:
```
2026-09-12   08:21   22:17
2026-09-13   17:01   23:20
2026-09-14   00:35   19:18
2026-09-15   05:23   20:28
2026-09-16   02:43   10:04
```

Jadval `state.json` ichida saqlanadi va **har kuni yangilanadi**. Kun davomida
workflow necha marta ishlashidan qat'i nazar jadval o'zgarmaydi — urug' kun
sanasiga bog'langan.

**105 post ÷ 2 = ~53 kun** (taxminan 1.8 oy).

### Sozlash

`.github/workflows/post.yml` dagi `env:` blokida:

| O'zgaruvchi | Default | Nima qiladi |
|---|---|---|
| `POSTS_PER_DAY` | `2` | Kuniga nechta post |
| `WINDOW` | `0-23` | Ruxsat etilgan soatlar. `7-22` — faqat kunduzi |
| `MIN_GAP_HOURS` | `4` | Postlar orasidagi eng kam farq |
| `TZ_OFFSET` | `5` | Toshkent = UTC+5 |
| `LANGS` | `uz,ru,en` | Faqat o'zbekcha kerak bo'lsa: `uz` |

⚠️ **Kechasi post kerak bo'lmasa** `WINDOW` ni `7-22` qiling — tasodifiylik
saqlanadi, lekin faqat 07:00–22:00 oralig'ida.

⚠️ **Aniq vaqt kafolatlanmaydi.** Ikki sabab: bot soatiga bir marta tekshiradi,
va GitHub Actions cron odatda 5–20 daqiqa kechikadi. Ya'ni 08:21 ga
rejalashtirilgan post amalda 09:00–09:30 orasida chiqadi. Kunlar bo'yicha
vaqtlar baribir tasodifiy taqsimlanadi.

### Darhol yuborish

Actions → **Tasodifiy post** → Run workflow → `force` ni `1` qiling.
Jadvalga qaramay bugungi barcha slotlar yuboriladi.

---

## Fayllar

| Fayl | Nima |
|---|---|
| `bot.py` | Posting boti |
| `posts.json` | 105 ta post, uch tilda |
| `state.json` | Yuborilganlar ro'yxati — **avtomatik yangilanadi** |
| `ST_POSTS.md` | Manba matn, o'qish uchun qulay |
| `build_facts.py` | `ST_POSTS.md` → `posts.json` konvertori |
| `.github/workflows/post.yml` | Jadval — har soat tekshiradi |

`state.json` ni **qo'lda tahrirlamang** — bot unga yuborilganlar ro'yxatini va
kunlik tasodifiy jadvalni yozadi, keyin commit qiladi.

---


---

## Mahalliy sinov

```bash
# jadvalni ko'rish, yubormasdan
DRY_RUN=1 python3 bot.py

# jadvalga qaramay sinash
DRY_RUN=1 FORCE=1 python3 bot.py

# haqiqiy yuborish
export BOT_TOKEN="123456789:AAH..."
export CHANNEL_ID="@enersok_edu"
python3 bot.py
```

---

## Kontentni tahrirlash

1. `ST_POSTS.md` ni tahrirlang
2. Qayta yig'ing:
```bash
python3 build_facts.py
mv st_facts.json posts.json
```
3. Commit va push

Yangi post qo'shish uchun `ST_POSTS.md` oxiriga shu qolipda yozing:

```markdown
---
---

## POST 106 — Sarlavha

**🇺🇿 O'zbekcha sarlavha**

matn...

---

**🇷🇺 Русский заголовок**

текст...

---

**🇬🇧 English title**

text...

`#tag1 #tag2`
```

ID avtomatik `st-106` bo'ladi. `state.json` ga tegmang — yangi ID navbatga qo'shiladi.

---

## Tekshiruvlar

`build_facts.py` har yig'ishda tekshiradi:
- lotin matnda kirill belgisi yo'qligi
- uchala til bloki bo'sh emasligi
- sarlavhalar takrorlanmasligi

`bot.py` ichida:
- 4096 belgidan uzun xabarlar **abzats chegarasida** bo'linadi (HTML teglar buzilmaydi)
- Telegram `429` (rate limit) da **3 marta qayta uriniladi**
- Post to'liq yuborilmasa **yuborilgan deb belgilanmaydi** — keyingi safar qaytadan uriniladi

---

## Muammolar

**Post kelmadi** → Actions → oxirgi run → log. Ko'p uchraydigan sabab: bot kanalda admin emas.

**`Bad Request: chat not found`** → `CHANNEL_ID` xato. Ommaviy kanal uchun `@username`, yopiq kanal uchun `-100...` raqami.

**`Bad Request: can't parse entities`** → matnda buzilgan HTML. `DRY_RUN=1` bilan qaysi postligini toping.

**Ikki marta yuborildi** → ikkita workflow bir vaqtda ishlagan. `concurrency` bloki buni to'xtatadi; agar takrorlansa `state.json` ni tekshiring.

**Post kechikdi** → normal. GitHub cron kafolatlangan emas; yuk katta bo'lganda
20–30 daqiqa kechikadi. Slot bajarilmaguncha keyingi har soatlik ishga tushishda
qayta uriniladi.

**Bugun post chiqmadi** → log da `Hali vaqt emas` yozilgan bo'lsa, jadval kechroqqa
tushgan. `state.json` dagi `schedule` ni ko'ring.

**Postlar tugadi** → bot `"Barcha 105 ta post yuborilgan"` deb yozadi va to'xtaydi. Yangi kontent qo'shing yoki `state.json` dagi `sent` ro'yxatini bo'shatib qaytadan boshlang.

---

## Eslatma

Manual ichki hujjat. KKS kodlari va setpointlarni ochiq kanalga joylashtirish
kompaniya qoidalariga mos kelishini nashrdan oldin tasdiqlang.
