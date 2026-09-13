#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ST_POSTS.md -> st_facts.json

Har bir "## POST N — sarlavha" blokini o'qiydi, uch tilli qismlarga ajratadi
(🇺🇿 / 🇷🇺 / 🇬🇧) va bot uchun JSON element yasaydi.

Ishlatish:
    python3 build_facts.py                  # st_facts.json yaratadi
    python3 build_facts.py --merge facts.json   # mavjud facts.json ga qo'shadi
"""

import json
import re
import sys
import argparse
from pathlib import Path

SRC = Path(__file__).parent / "ST_POSTS.md"
OUT = Path(__file__).parent / "st_facts.json"

# Kirill belgilarini lotin o'zbek matnidan tozalash (chala gap muammosi)
CYR2LAT = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'j',
    'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
    'х': 'x', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh', 'ъ': "'",
    'ы': 'i', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'ё': 'yo',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ж': 'J',
    'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
    'Х': 'X', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sh', 'Ъ': "'",
    'Ы': 'I', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya', 'Ё': 'Yo',
}


def clean_latin(text: str) -> str:
    """Lotin o'zbek matnidagi tasodifiy kirill belgilarini almashtiradi."""
    out = []
    for ch in text:
        out.append(CYR2LAT.get(ch, ch))
    return "".join(out)


def strip_md(text: str) -> str:
    """Telegram HTML/oddiy matn uchun markdownni soddalashtiradi."""
    # Jadval qatorlarini " | " bilan saqlab qolamiz, ajratgich qatorini olib tashlaymiz
    lines = []
    for ln in text.split("\n"):
        if re.match(r"^\s*\|[\s\-:|]+\|\s*$", ln):
            continue
        ln = ln.strip()
        if ln.startswith("|") and ln.endswith("|"):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            cells = [c for c in cells if c and c not in {"—", "-", "–"}]
            ln = " — ".join(cells)
        if re.fullmatch(r"-{3,}", ln):
            continue
        lines.append(ln)
    text = "\n".join(lines)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)   # bold
    text = re.sub(r"\*(.+?)\*", r"\1", text)        # italic
    text = re.sub(r"`(.+?)`", r"\1", text)          # code
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse_posts(md: str):
    """Markdowndan postlarni ajratib oladi."""
    chunks = re.split(r"^## POST\s+", md, flags=re.M)[1:]
    posts = []
    for ch in chunks:
        head, _, body = ch.partition("\n")
        m = re.match(r"(\d+)\s*[—\-–]\s*(.+)", head.strip())
        if not m:
            continue
        num, title = int(m.group(1)), m.group(2).strip()

        # hashtaglar — faqat oxirgi `#...` qatoridan
        tagline = re.findall(r"`(#[^`]+)`", body)
        tags = re.findall(r"#([A-Za-z][A-Za-z0-9_]{1,})", tagline[-1]) if tagline else []

        # uch tilli bloklar
        def grab(flag, nxt):
            if nxt:
                pat = re.compile(r"\*\*" + flag + r"(.*?)(?=\*\*" + nxt + r")", re.S)
            else:
                pat = re.compile(r"\*\*" + flag + r"(.*)$", re.S)
            mm = pat.search(body)
            return mm.group(1) if mm else ""

        uz = grab("🇺🇿", "🇷🇺")
        ru = grab("🇷🇺", "🇬🇧")
        en = grab("🇬🇧", None)

        # sarlavhalarni qismlardan chiqarib olish
        def split_head(block):
            block = block.strip()
            if block.startswith("**"):
                block = block[2:]
            h, _, rest = block.partition("\n")
            return h.replace("**", "").strip(), rest.strip()

        uz_h, uz_b = split_head(uz)
        ru_h, ru_b = split_head(ru)
        en_h, en_b = split_head(en)

        # ingliz blokidan hashtag qatori va ajratgichlarni olib tashlash
        en_b = re.sub(r"(?:\n|^)\s*-{3,}\s*", "\n", en_b)
        en_b = re.sub(r"`#[^`]*`", "", en_b)
        en_b = re.sub(r"(?:\n|^)\s*#[A-Za-z0-9_][A-Za-z0-9_ #]*\s*$", "", en_b)
        en_b = re.sub(r"\s*-{3,}\s*$", "", en_b).strip()

        posts.append({
            "id": f"st-{num:03d}",
            "source": "SYR2-073-MAN-OM-3625 Rev.00 (Harbin Electric)",
            "scope": "steam_turbine",
            "title": title,
            "tags": sorted(set(tags)),
            "uz": {"title": clean_latin(uz_h), "text": clean_latin(strip_md(uz_b))},
            "ru": {"title": ru_h, "text": strip_md(ru_b)},
            "en": {"title": en_h, "text": strip_md(en_b)},
        })
    return posts


def validate(posts):
    """Sifat tekshiruvi: kirill aralashmasi, bo'sh blok, dublikat."""
    errs = []
    seen = set()
    for p in posts:
        if not p["uz"]["text"] or not p["ru"]["text"] or not p["en"]["text"]:
            errs.append(f'{p["id"]}: bo\'sh til bloki')
        bad = [w for w in re.findall(r"\b\w*[а-яА-ЯёЁ]\w*\b", p["uz"]["text"])
               if re.search(r"[a-zA-Z]", w)]
        if bad:
            errs.append(f'{p["id"]}: aralash skript {set(bad)}')
        key = p["uz"]["title"]
        if key in seen:
            errs.append(f'{p["id"]}: dublikat sarlavha "{key}"')
        seen.add(key)
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--merge", help="mavjud facts.json fayliga qo'shish")
    ap.add_argument("--flat", action="store_true",
                    help="har bir til alohida element bo'lgan tekis format")
    args = ap.parse_args()

    md = SRC.read_text(encoding="utf-8")
    posts = parse_posts(md)

    errs = validate(posts)
    if errs:
        print("XATOLAR:")
        for e in errs:
            print("  -", e)
    else:
        print(f"OK — {len(posts)} ta post, xato yo'q")

    if args.flat:
        flat = []
        for p in posts:
            for lang in ("uz", "ru", "en"):
                flat.append({
                    "id": f'{p["id"]}-{lang}',
                    "lang": lang,
                    "title": p[lang]["title"],
                    "text": p[lang]["text"],
                    "tags": p["tags"],
                    "source": p["source"],
                })
        posts_out = flat
    else:
        posts_out = posts

    OUT.write_text(json.dumps(posts_out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Yozildi: {OUT} ({OUT.stat().st_size // 1024} KB)")

    if args.merge:
        target = Path(args.merge)
        existing = json.loads(target.read_text(encoding="utf-8"))
        ids = {i.get("id") for i in existing if isinstance(i, dict)}
        added = [p for p in posts if p["id"] not in ids]
        existing.extend(added)
        target.write_text(json.dumps(existing, ensure_ascii=False, indent=2),
                          encoding="utf-8")
        print(f"{target}: {len(added)} ta yangi element qo'shildi, "
              f"jami {len(existing)}")


if __name__ == "__main__":
    main()
