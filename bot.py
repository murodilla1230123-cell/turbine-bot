#!/usr/bin/env python3
"""
Turbine / Energy facts bot — tasodifiy kunlik posting.
- Har kuni 3-5 ta post (tasodifiy tanlanadi)
- Butun kun bo'yi tasodifiy vaqtlarda tarqaladi
- GitHub Actions har soatda ishga tushiradi; bot o'zi post qilishni hal qiladi
"""

import os
import json
import random
import html
from datetime import datetime, timezone, timedelta
import requests

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "").strip()
CHAT_ID        = os.environ.get("CHAT_ID", "").strip()

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
FACTS_FILE = os.path.join(BASE_DIR, "facts.json")
SENT_FILE  = os.path.join(BASE_DIR, "sent.json")
STATE_FILE = os.path.join(BASE_DIR, "state.json")

TASHKENT = timezone(timedelta(hours=5))
DAY_START = 0
DAY_END   = 23


def translate_to_ru(text):
    """O'zbekcha matnni rus tiliga tarjima qiladi (bepul, kalitsiz).
    Xato bo'lsa bo'sh string qaytaradi — bot baribir ishlayveradi."""
    if not text:
        return ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    # 1-usul: translate.googleapis.com
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": "uz", "tl": "ru", "dt": "t", "q": text}
        r = requests.get(url, params=params, headers=headers, timeout=15)
        r.raise_for_status()
        data = r.json()
        return "".join(part[0] for part in data[0] if part[0])
    except Exception as e:
        print(f"Tarjima 1-usul xatosi: {e}")

    # 2-usul (zaxira): clients5.google.com
    try:
        url = "https://clients5.google.com/translate_a/t"
        params = {"client": "dict-chrome-ex", "sl": "uz", "tl": "ru", "q": text}
        r = requests.get(url, params=params, headers=headers, timeout=15)
        r.raise_for_status()
        data = r.json()
        # javob format: [["tarjima", "manba"], ...] yoki {"sentences":[...]}
        if isinstance(data, list):
            if data and isinstance(data[0], list):
                return "".join(seg[0] for seg in data if seg and seg[0])
            if data and isinstance(data[0], str):
                return data[0]
        return ""
    except Exception as e:
        print(f"Tarjima 2-usul xatosi: {e}")

    # 3-usul (zaxira): MyMemory API
    try:
        url = "https://api.mymemory.translated.net/get"
        params = {"q": text, "langpair": "uz|ru"}
        r = requests.get(url, params=params, headers=headers, timeout=15)
        r.raise_for_status()
        data = r.json()
        return data.get("responseData", {}).get("translatedText", "") or ""
    except Exception as e:
        print(f"Tarjima 3-usul xatosi (o'tkazib yuborildi): {e}")
        return ""


def ensure_ru(fact):
    """Post uchun rus tarjimasini ta'minlaydi (faqat fakt/dars uchun).
    Quizlar faqat ingliz tilida bo'ladi, ularга tegmaydi."""
    if fact.get("type") == "quiz":
        return fact  # quiz ingliz tilida, tarjima kerak emas
    if not fact.get("ru"):
        fact["ru"] = translate_to_ru(fact.get("uz", ""))
    return fact


def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def fact_key(f):
    """Takrorlanmaslik uchun noyob kalit (fakt uchun 'uz', quiz uchun 'q')."""
    return f.get("uz") or f.get("q") or ""


def pick_fact(sent_texts):
    facts = load_json(FACTS_FILE, [])
    fresh = [f for f in facts if fact_key(f) not in sent_texts]
    if not fresh:
        fresh = facts
    return random.choice(fresh) if fresh else None


CAT_EMOJI = {
    "Gaz turbinasi (GT)": "\U0001f525",       # 🔥
    "Kompressor": "\U0001f4a8",                # 💨
    "Yonish / Combustor": "\U0001f9ef",        # 🧯
    "Bug' turbinasi (ST)": "\U0001f4a6",       # 💦
    "HRSG / Bug' sikli": "\u267b\ufe0f",       # ♻️
    "Kondensator / Sovutish": "\u2744\ufe0f",  # ❄️
    "Generator": "\u26a1",                     # ⚡
    "Elektr / Himoya": "\U0001f50c",           # 🔌
    "Moy / Podshipnik": "\U0001f6e2\ufe0f",    # 🛢️
    "Yordamchi tizimlar": "\u2699\ufe0f",      # ⚙️
    "Nasos / Klapan": "\U0001f6b0",            # 🚰
    "Boshqaruv / Asboblar": "\U0001f5a5\ufe0f",# 🖥️
    "Ishga tushirish / Rejim": "\U0001f7e2",   # 🟢
    "Ta'mir / Xavfsizlik": "\U0001f6e1\ufe0f", # 🛡️
    "Combined Cycle / Samaradorlik": "\U0001f4c8", # 📈
    "Energetika asoslari": "\U0001f4a1",       # 💡
}

KIND_LABEL = {
    "fact":   "Fakt / Факт / Fact",
    "lesson": "Mini dars / Мини урок / Mini lesson",
    "quiz":   "Savol / Вопрос / Quiz",
}

# Har toifa uchun mavzuga mos hashtaglar
CAT_TAGS = {
    "Gaz turbinasi (GT)": ["gazturbinasi", "GT", "turbina"],
    "Kompressor": ["kompressor", "havo", "turbina"],
    "Yonish / Combustor": ["yonish", "combustor", "yoqilgi"],
    "Bug' turbinasi (ST)": ["bugturbinasi", "ST", "bug"],
    "HRSG / Bug' sikli": ["HRSG", "bugsikli", "issiqlik"],
    "Kondensator / Sovutish": ["kondensator", "sovutish", "vakuum"],
    "Generator": ["generator", "elektr", "kuchlanish"],
    "Elektr / Himoya": ["elektr", "himoya", "kuchlanish"],
    "Moy / Podshipnik": ["moy", "podshipnik", "moylash"],
    "Yordamchi tizimlar": ["yordamchitizim", "auxiliary", "tizim"],
    "Nasos / Klapan": ["nasos", "klapan", "suyuqlik"],
    "Boshqaruv / Asboblar": ["boshqaruv", "asbob", "avtomatika"],
    "Ishga tushirish / Rejim": ["ishgatushirish", "rejim", "start"],
    "Ta'mir / Xavfsizlik": ["tamir", "xavfsizlik", "profilaktika"],
    "Combined Cycle / Samaradorlik": ["combinedcycle", "samaradorlik", "FIK"],
    "Energetika asoslari": ["energetika", "asoslar", "elektr"],
    "Releli himoya": ["relehimoya", "himoya", "rele"],
}


def build_hashtags(fact):
    cat = fact.get("cat", "")
    tags = list(fact.get("tags") or CAT_TAGS.get(cat, ["energetika", "power", "engineering"]))
    if "energetika" not in tags:
        tags.append("energetika")
    return " ".join("#" + t for t in tags)


def build_message(fact):
    uz = html.escape(fact["uz"])
    ru = html.escape(fact.get("ru", ""))
    en = html.escape(fact["en"])
    kind = fact.get("type", "fact")
    cat = fact.get("cat", "")

    klabel = KIND_LABEL.get(kind, KIND_LABEL["fact"])

    # Minimal: bitta bo'lim sarlavhasi, toifa nomi (emojisiz)
    header = f"<b>{klabel}</b>"
    if cat:
        header += f"\n<b>{html.escape(cat)}</b>"

    body = f"\U0001f1fa\U0001f1ff {uz}\n\n"
    if ru:
        body += f"\U0001f1f7\U0001f1fa {ru}\n\n"
    body += f"\U0001f1ec\U0001f1e7 {en}\n\n"

    return (
        f"{header}\n"
        f"\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n"
        f"{body}"
        f"{build_hashtags(fact)}"
    )


def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    r = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": "true",
        },
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def send_quiz_poll(fact):
    """Telegram interaktiv quiz (poll) yuboradi — faqat ingliz tilida."""
    cat = fact.get("cat", "")

    # Ingliz tilidagi savol (agar yo'q bo'lsa, o'zbekchaga qaytadi)
    q_en = fact.get("q_en") or fact.get("q", "")
    question = f"{cat}\n{q_en}" if cat else q_en
    question = question[:295]

    # Ingliz variantlari (agar yo'q bo'lsa, o'zbekcha)
    opts = fact.get("options_en") or fact.get("options", [])
    options = [o[:100] for o in opts]

    # Ingliz izohi (agar yo'q bo'lsa, o'zbekcha)
    explanation = (fact.get("explain_en") or fact.get("explain", ""))[:200]

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options, ensure_ascii=False),
        "type": "quiz",
        "correct_option_id": fact["correct"],
        "is_anonymous": "true",
    }
    if explanation:
        data["explanation"] = explanation
    r = requests.post(url, data=data, timeout=30)
    r.raise_for_status()
    return r.json()


def get_today_state():
    now = datetime.now(TASHKENT)
    today = now.strftime("%Y-%m-%d")
    state = load_json(STATE_FILE, {})
    if state.get("date") != today:
        state = {"date": today, "target": random.randint(10, 12), "posted": 0}
        save_json(STATE_FILE, state)
    return state, now


def posts_to_send_now(state, now):
    """Hozir nechta post yuborishni hal qiladi (soatiga 1 marta ishga tushishga moslangan)."""
    target = state["target"]
    posted = state["posted"]
    remaining = target - posted
    if remaining <= 0:
        return 0

    # Kun oxirigacha qolgan soatlar (imkoniyatlar)
    hours_left = max(1, DAY_END - now.hour + 1)

    # Agar qolgan postlar soatlardan ko'p bo'lsa — yetkazish uchun bir nechta yuboramiz
    if remaining >= hours_left:
        # Har soatga teng taqsimlab, ortiqchasini ham qo'shamiz
        base = remaining // hours_left
        extra = 1 if (remaining % hours_left) > 0 else 0
        return max(1, base + extra)

    # Aks holda — tasodifiy: o'rtacha remaining/hours_left ehtimol bilan 1 ta
    probability = remaining / hours_left
    return 1 if random.random() < probability else 0


def main():
    if not TELEGRAM_TOKEN or not CHAT_ID:
        raise SystemExit("XATO: TELEGRAM_TOKEN va CHAT_ID Secrets qilib qo'ying.")

    state, now = get_today_state()

    # Qo'lda ishga tushirilganda (Run workflow) majburan 1 ta post qiladi
    force = os.environ.get("FORCE_POST", "").strip() == "1"

    if force:
        n_posts = 1
    else:
        if now.hour < DAY_START or now.hour > DAY_END:
            print("Post oynasidan tashqarida.")
            return
        n_posts = posts_to_send_now(state, now)
        if n_posts <= 0:
            print(f"Hozir post yo'q. Bugun: {state['posted']}/{state['target']}, soat {now.hour}")
            return

    sent = load_json(SENT_FILE, [])
    sent_texts = {fact_key(s) for s in sent}

    yuborilgan = 0
    for _ in range(n_posts):
        # Kunlik chegaradan oshmaymiz
        if not force and state["posted"] >= state["target"]:
            break

        fact = pick_fact(sent_texts)
        if not fact:
            print("Yangi fakt qolmadi.")
            break

        # Rus tarjimasini ta'minlash (faqat fakt/dars uchun)
        fact = ensure_ru(fact)

        # Quiz -> interaktiv poll (ingliz); boshqalari -> 3 tilli xabar
        try:
            if fact.get("type") == "quiz" and fact.get("options") and "correct" in fact:
                send_quiz_poll(fact)
                print("Quiz yuborildi:", fact.get("q", "")[:60])
            else:
                send_to_telegram(build_message(fact))
                print("Yuborildi:", fact["uz"][:60])
        except Exception as e:
            print(f"Yuborishda xato: {e}")
            break

        sent.append(fact)
        sent_texts.add(fact_key(fact))
        state["posted"] += 1
        yuborilgan += 1

    # Saqlash
    sent = sent[-1000:]
    save_json(SENT_FILE, sent)
    save_json(STATE_FILE, state)
    print(f"Bu safar yuborildi: {yuborilgan} | Bugun jami: {state['posted']}/{state['target']}")


if __name__ == "__main__":
    main()
