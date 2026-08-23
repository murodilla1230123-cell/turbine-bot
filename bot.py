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


def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def pick_fact(sent_texts):
    facts = load_json(FACTS_FILE, [])
    fresh = [f for f in facts if f["uz"] not in sent_texts]
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
    "fact":   ("\u26a1\ufe0f", "Fakt / Fact"),
    "lesson": ("\U0001f4d8", "Mini dars / Mini lesson"),
    "quiz":   ("\u2753", "Savol / Quiz"),
}


def build_message(fact):
    uz = html.escape(fact["uz"])
    en = html.escape(fact["en"])
    kind = fact.get("type", "fact")
    cat = fact.get("cat", "")

    kemoji, klabel = KIND_LABEL.get(kind, KIND_LABEL["fact"])
    cemoji = CAT_EMOJI.get(cat, "\U0001f527")  # 🔧 default

    header = f"{kemoji} <b>{klabel}</b>"
    if cat:
        header += f"\n{cemoji} <b>{html.escape(cat)}</b>"

    return (
        f"{header}\n"
        f"\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n"
        f"\U0001f1fa\U0001f1ff {uz}\n\n"
        f"\U0001f1ec\U0001f1e7 {en}\n\n"
        f"#energetika #turbina #power #engineering"
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


def get_today_state():
    now = datetime.now(TASHKENT)
    today = now.strftime("%Y-%m-%d")
    state = load_json(STATE_FILE, {})
    if state.get("date") != today:
        state = {"date": today, "target": random.randint(3, 5), "posted": 0}
        save_json(STATE_FILE, state)
    return state, now


def should_post_now(state, now):
    target = state["target"]
    posted = state["posted"]
    if posted >= target:
        return False
    hours_left = max(1, DAY_END - now.hour + 1)
    posts_left = target - posted
    if posts_left >= hours_left:
        return True
    probability = posts_left / hours_left
    return random.random() < probability


def main():
    if not TELEGRAM_TOKEN or not CHAT_ID:
        raise SystemExit("XATO: TELEGRAM_TOKEN va CHAT_ID Secrets qilib qo'ying.")

    state, now = get_today_state()

    if now.hour < DAY_START or now.hour > DAY_END:
        print("Post oynasidan tashqarida.")
        return

    if not should_post_now(state, now):
        print(f"Hozir post yo'q. Bugun: {state['posted']}/{state['target']}, soat {now.hour}")
        return

    sent = load_json(SENT_FILE, [])
    sent_texts = {s["uz"] for s in sent}

    fact = pick_fact(sent_texts)
    if not fact:
        raise SystemExit("Fakt topilmadi.")

    send_to_telegram(build_message(fact))
    print("Yuborildi:", fact["uz"][:60])

    sent.append(fact)
    sent = sent[-1000:]
    save_json(SENT_FILE, sent)

    state["posted"] += 1
    save_json(STATE_FILE, state)
    print(f"Bugun: {state['posted']}/{state['target']}")


if __name__ == "__main__":
    main()
