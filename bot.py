#!/usr/bin/env python3
"""
Turbine / Energy daily facts bot — GitHub Actions versiyasi.
- facts.json dan hali yuborilmagan faktni tanlaydi (takrorlanmaydi)
- Telegram kanalga post qiladi
- sent.json ni yangilaydi (GitHub Actions uni repoga saqlaydi)
Token va CHAT_ID GitHub Secrets orqali keladi.
"""

import os
import json
import random
import html
import requests

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "").strip()
CHAT_ID        = os.environ.get("CHAT_ID", "").strip()

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
FACTS_FILE = os.path.join(BASE_DIR, "facts.json")
SENT_FILE  = os.path.join(BASE_DIR, "sent.json")


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
    if not fresh:                      # hammasi tugasa -> qaytadan
        fresh = facts
    return random.choice(fresh) if fresh else None


def build_message(fact):
    uz = html.escape(fact["uz"])
    en = html.escape(fact["en"])
    return (
        f"⚡️ <b>Kunlik fakt / Fact of the day</b>\n\n"
        f"🇺🇿 {uz}\n\n"
        f"🇬🇧 {en}\n\n"
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


def main():
    if not TELEGRAM_TOKEN or not CHAT_ID:
        raise SystemExit("XATO: TELEGRAM_TOKEN va CHAT_ID Secrets qilib qo'ying.")

    sent = load_json(SENT_FILE, [])
    sent_texts = {s["uz"] for s in sent}

    fact = pick_fact(sent_texts)
    if not fact:
        raise SystemExit("Fakt topilmadi.")

    send_to_telegram(build_message(fact))
    print("Yuborildi:", fact["uz"][:60])

    sent.append(fact)
    sent = sent[-500:]
    save_json(SENT_FILE, sent)


if __name__ == "__main__":
    main()
