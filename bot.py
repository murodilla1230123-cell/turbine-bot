#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@enersok_edu — ST kontent boti (tasodifiy vaqtli)

Workflow har soat ishga tushadi. Bot har kuni sutkaning tasodifiy
vaqtlarini tanlaydi va faqat o'sha vaqt kelganda post yuboradi.

Muhit o'zgaruvchilari:
    BOT_TOKEN      — BotFather tokeni                     (majburiy)
    CHANNEL_ID     — @enersok_edu yoki -100...             (majburiy)
    POSTS_PER_DAY  — kuniga nechta post                    (default 2)
    WINDOW         — ruxsat etilgan soatlar                (default 0-23)
    MIN_GAP_HOURS  — postlar orasidagi eng kam farq        (default 4)
    TZ_OFFSET      — mahalliy vaqt siljishi                (default 5)
    LANGS          — tillar, vergul bilan                  (default uz,ru,en)
    DRY_RUN        — 1 bo'lsa yubormaydi
    FORCE          — 1 bo'lsa jadvalga qaramay yuboradi
"""

import html
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).parent
POSTS_FILE = ROOT / "posts.json"
STATE_FILE = ROOT / "state.json"

API = "https://api.telegram.org/bot{token}/sendMessage"
TG_LIMIT = 4096
FLAG = {"uz": "🇺🇿", "ru": "🇷🇺", "en": "🇬🇧"}


# ---------------------------------------------------------------- vaqt

def now_local() -> datetime:
    off = int(os.environ.get("TZ_OFFSET", "5"))
    return datetime.now(timezone.utc) + timedelta(hours=off)


def parse_window() -> tuple:
    """WINDOW='0-23' yoki '7-22' ni (boshlanish, tugash) ga o'giradi."""
    raw = os.environ.get("WINDOW", "0-23").strip()
    m = re.fullmatch(r"(\d{1,2})\s*-\s*(\d{1,2})", raw)
    if not m:
        return 0, 23
    a, b = int(m.group(1)), int(m.group(2))
    a, b = max(0, min(23, a)), max(0, min(23, b))
    return (a, b) if a <= b else (b, a)


def make_schedule(day: str) -> dict:
    """Kun uchun tasodifiy vaqtlar tanlaydi."""
    n = max(1, int(os.environ.get("POSTS_PER_DAY", "2")))
    lo, hi = parse_window()
    gap = int(os.environ.get("MIN_GAP_HOURS", "4"))

    span = hi - lo + 1
    n = min(n, span)

    # oyna tor bo'lsa gap ni kamaytiramiz
    while gap > 0 and lo + gap * (n - 1) > hi:
        gap -= 1

    # urug' kunga bog'langan — bir kunda qayta hisoblansa ham bir xil chiqadi
    rnd = random.Random(f"{day}:{n}:{lo}:{hi}")

    hours = None
    for _ in range(300):
        pick = sorted(rnd.sample(range(lo, hi + 1), n))
        if all(pick[i + 1] - pick[i] >= gap for i in range(n - 1)):
            hours = pick
            break
    if hours is None:
        step = max(1, span // n)
        hours = [min(hi, lo + i * step) for i in range(n)]

    slots = [{"h": h, "m": rnd.randint(0, 59), "done": False} for h in hours]
    return {"date": day, "slots": slots}


def due_slots(schedule: dict, now: datetime) -> list:
    """Vaqti kelgan va hali bajarilmagan slot indekslari."""
    out = []
    for i, s in enumerate(schedule["slots"]):
        if s["done"]:
            continue
        if (now.hour, now.minute) >= (s["h"], s["m"]):
            out.append(i)
    return out


# ---------------------------------------------------------------- formatlash

def to_html(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text, flags=re.S)
    text = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"<i>\1</i>", text, flags=re.S)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text, flags=re.S)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_message(post: dict, lang: str) -> str:
    block = post[lang]
    head = f"{FLAG[lang]} <b>{html.escape(block['title'])}</b>"
    body = to_html(block["text"])
    tags = " ".join("#" + t for t in post.get("tags", [])[:6])
    parts = [head, body]
    if tags:
        parts.append(tags)
    return "\n\n".join(parts)


def split_message(text: str, limit: int = TG_LIMIT) -> list:
    if len(text) <= limit:
        return [text]
    chunks, buf = [], ""
    for para in text.split("\n\n"):
        candidate = para if not buf else buf + "\n\n" + para
        if len(candidate) <= limit:
            buf = candidate
            continue
        if buf:
            chunks.append(buf)
        while len(para) > limit:
            cut = para.rfind("\n", 0, limit)
            if cut <= 0:
                cut = limit
            chunks.append(para[:cut])
            para = para[cut:].lstrip("\n")
        buf = para
    if buf:
        chunks.append(buf)
    return chunks


# ---------------------------------------------------------------- Telegram

def send(token: str, chat_id: str, text: str, dry: bool = False) -> bool:
    if dry:
        print("-" * 60)
        print(text[:700])
        print(f"[DRY RUN — {len(text)} belgi]")
        return True

    payload = json.dumps({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }).encode("utf-8")

    req = urllib.request.Request(
        API.format(token=token),
        data=payload,
        headers={"Content-Type": "application/json"},
    )

    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read())
            if result.get("ok"):
                return True
            print(f"  Telegram xatosi: {result}", file=sys.stderr)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")
            print(f"  HTTP {e.code}: {detail}", file=sys.stderr)
            if e.code == 429:
                wait = 20 * attempt
                print(f"  rate limit — {wait}s kutilmoqda", file=sys.stderr)
                time.sleep(wait)
                continue
            if 400 <= e.code < 500:
                return False
        except Exception as e:
            print(f"  Tarmoq xatosi: {e}", file=sys.stderr)
        time.sleep(5 * attempt)
    return False


# ---------------------------------------------------------------- holat

def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("state.json buzilgan — noldan boshlanadi", file=sys.stderr)
    return {"sent": [], "cursor": 0}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def send_post(token, chat_id, post, langs, dry) -> bool:
    print(f"\n[{post['id']}] {post['title']}")
    for lang in langs:
        if lang not in post:
            continue
        for i, chunk in enumerate(split_message(build_message(post, lang)), 1):
            if not send(token, chat_id, chunk, dry):
                print(f"  {lang} qism {i} — YUBORILMADI", file=sys.stderr)
                return False
            print(f"  {lang} qism {i} — ok ({len(chunk)} belgi)")
            time.sleep(3)
    return True


# ---------------------------------------------------------------- asosiy

def main() -> int:
    token = os.environ.get("BOT_TOKEN", "").strip()
    chat_id = os.environ.get("CHANNEL_ID", "").strip()
    dry = os.environ.get("DRY_RUN", "").strip() == "1"
    force = os.environ.get("FORCE", "").strip() == "1"
    langs = [l.strip() for l in
             os.environ.get("LANGS", "uz,ru,en").split(",") if l.strip()]

    if not dry and (not token or not chat_id):
        print("BOT_TOKEN yoki CHANNEL_ID yo'q", file=sys.stderr)
        return 1

    posts = json.loads(POSTS_FILE.read_text(encoding="utf-8"))
    state = load_state()
    sent = set(state.get("sent", []))
    queue = [p for p in posts if p["id"] not in sent]

    now = now_local()
    today = now.strftime("%Y-%m-%d")

    # kunlik jadval
    sched = state.get("schedule")
    if not sched or sched.get("date") != today:
        sched = make_schedule(today)
        state["schedule"] = sched
        times = ", ".join(f"{s['h']:02d}:{s['m']:02d}" for s in sched["slots"])
        print(f"{today} uchun yangi jadval: {times}")
    else:
        times = ", ".join(
            f"{s['h']:02d}:{s['m']:02d}{' ok' if s['done'] else ''}"
            for s in sched["slots"]
        )
        print(f"{today} jadvali: {times}")

    print(f"Hozir: {now.strftime('%H:%M')} | navbatda {len(queue)} ta post")

    if not queue:
        print(f"Barcha {len(posts)} ta post yuborilgan. Yangi kontent kerak.")
        if not dry:
            save_state(state)
        return 0

    ready = list(range(len(sched["slots"]))) if force else due_slots(sched, now)
    if not ready:
        nxt = [s for s in sched["slots"] if not s["done"]]
        if nxt:
            print(f"Hali vaqt emas. Keyingisi: "
                  f"{nxt[0]['h']:02d}:{nxt[0]['m']:02d}")
        else:
            print("Bugungi postlar yuborilgan.")
        if not dry:
            save_state(state)
        return 0

    posted = 0
    for idx in ready:
        if not queue:
            break
        post = queue.pop(0)
        if not send_post(token, chat_id, post, langs, dry):
            print(f"  {post['id']} to'liq yuborilmadi — to'xtatildi",
                  file=sys.stderr)
            break
        sent.add(post["id"])
        sched["slots"][idx]["done"] = True
        posted += 1
        if posted < len(ready):
            time.sleep(5)

    state["sent"] = sorted(sent)
    state["cursor"] = len(sent)
    state["total"] = len(posts)
    state["remaining"] = len(posts) - len(sent)
    if not dry:
        save_state(state)

    print(f"\nYuborildi: {posted} | Jami: {len(sent)}/{len(posts)} | "
          f"Qoldi: {len(posts) - len(sent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
