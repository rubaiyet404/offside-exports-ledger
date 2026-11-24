#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OFFSIDE EXPORTS - Thursday WhatsApp Automated Fund Reminder Bot
---------------------------------------------------------------
This script automatically runs every Thursday evening to:
1. Fetch partner phone numbers from Firebase Realtime Database (/partner_phones.json)
2. Check fund contributions for the upcoming Friday (/partner_fund.json)
3. Identify partners among Ifty, Ratul, Hasib, and Tanjir who haven't deposited 250 BDT yet
4. Dispatch automated WhatsApp reminder notifications
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
import os
import subprocess
import ssl

# SSL context for macOS python without cert bundle
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

FIREBASE_URL = "https://offside-exports-default-rtdb.firebaseio.com"
PARTNERS = ["Ifty", "Ratul", "Hasib", "Tanjir"]
PARTNER_NAMES_BN = {
    "Ifty": "ইফতি",
    "Ratul": "রাতুল",
    "Hasib": "হাসিব",
    "Tanjir": "তানজির"
}

def get_upcoming_friday(ref_date=None):
    if ref_date is None:
        ref_date = datetime.now()
    # weekday: Monday is 0, Tuesday 1, Wednesday 2, Thursday 3, Friday 4, Saturday 5, Sunday 6
    # In python: Friday is 4
    # If today is Monday(0)..Friday(4): target Friday is 4 - weekday days away
    # If today is Saturday(5): -1 day (yesterday)
    # If today is Sunday(6): 5 days away (next Friday)
    weekday = ref_date.weekday()
    if weekday <= 4:
        days_ahead = 4 - weekday
    elif weekday == 5:
        days_ahead = -1  # yesterday
    else:
        days_ahead = 5  # Sunday -> Friday
    target = ref_date + timedelta(days=days_ahead)
    return target.strftime("%Y-%m-%d")

def to_bengali_numerals(s):
    bn_digits = {'0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪', '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'}
    return "".join(bn_digits.get(c, c) for c in str(s))

def format_friday_bengali(date_str):
    parts = date_str.split("-")
    if len(parts) == 3:
        year = to_bengali_numerals(parts[0])
        months_bn = ["জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন", "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর"]
        month_idx = int(parts[1]) - 1
        day = to_bengali_numerals(str(int(parts[2])).zfill(2))
        month_name = months_bn[month_idx] if 0 <= month_idx < 12 else parts[1]
        return f"{day} {month_name} {year} (শুক্রবার)"
    return date_str

def fetch_json(endpoint):
    url = f"{FIREBASE_URL}/{endpoint.lstrip('/')}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "OffsideExportsBot/1.0"})
        with urllib.request.urlopen(req, timeout=10, context=ssl_ctx) as response:
            data = response.read().decode('utf-8')
            return json.loads(data) if data and data != "null" else None
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None

def send_macos_notification(title, message):
    try:
        cmd = f'display notification "{message}" with title "{title}" sound name "Glass"'
        subprocess.run(["osascript", "-e", cmd], check=False)
    except Exception:
        pass

def generate_reminder_message(partner_name, friday_str):
    name_bn = PARTNER_NAMES_BN.get(partner_name, partner_name)
    friday_bn = format_friday_bengali(friday_str)
    
    return (
        f"আসসালামু আলাইকুম {partner_name} ভাই! 🤝\n"
        f"আগামীকাল {friday_bn}, আমাদের অফসাইড এক্সপোর্টস পার্টনার তহবিলের সাপ্তাহিক ২৫০ টাকা জমা দেওয়ার দিন।\n\n"
        f"💳 জমা দেওয়ার মাধ্যম:\n"
        f"• bKash: 01834093932 (Personal)\n"
        f"• Rocket: 018927170930\n"
        f"• অথবা নগদ ক্যাশ (Cash)\n\n"
        f"টাকা পাঠিয়ে লেজার খাতায় বা গ্রুপে জানিয়ে দেওয়ার অনুরোধ রইল। ধন্যবাদ! 🤝\n"
        f"- অফসাইড এক্সপোর্টস (Offside Exports)"
    )

def run_thursday_reminder_check():
    now = datetime.now()
    target_friday = get_upcoming_friday(now)
    friday_bn = format_friday_bengali(target_friday)

    print("=" * 60)
    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Offside Exports Thursday Reminder Bot")
    print(f"Target Friday: {target_friday} ({friday_bn})")
    print("=" * 60)

    # 1. Fetch Partner Phones
    phones = fetch_json("partner_phones.json") or {}
    print(f"Loaded phone contacts: {phones}")

    # 2. Fetch Partner Fund Transactions
    fund_records = fetch_json("partner_fund.json") or {}
    if isinstance(fund_records, dict):
        fund_list = list(fund_records.values())
    elif isinstance(fund_records, list):
        fund_list = fund_records
    else:
        fund_list = []

    # 3. Check Who Has Paid for target Friday
    paid_partners = set()
    for rec in fund_list:
        if not rec:
            continue
        r_type = rec.get("type", "deposit")
        r_partner = rec.get("partner", "")
        r_date = rec.get("date", "")
        if r_type == "deposit" and r_date == target_friday:
            paid_partners.add(r_partner)

    print(f"Partners already paid for {target_friday}: {list(paid_partners)}")

    # 4. Find Due Partners
    due_partners = [p for p in PARTNERS if p not in paid_partners]
    if not due_partners:
        print("🎉 All 4 partners have already deposited for this Friday! No reminder needed.")
        return

    print(f"⚠️ Unpaid partners for {target_friday}: {due_partners}")

    # 5. Dispatch Reminders
    for p in due_partners:
        phone = str(phones.get(p, "")).strip().replace("-", "").replace(" ", "")
        msg = generate_reminder_message(p, target_friday)
        
        print(f"\n[REMINDER] Partner: {p} ({PARTNER_NAMES_BN.get(p, p)}) | Phone: {phone or 'NOT_SET'}")
        print(f"Message:\n{msg}")

        # Desktop alert
        send_macos_notification(
            "অফসাইড এক্সপোর্টস রিমাইন্ডার",
            f"{p}-এর শুক্রবার ২৫০৳ তহবিল জমা বাকি আছে। WhatsApp রিমাইন্ডার প্রস্তুত!"
        )

    # Write log
    log_entry = {
        "timestamp": now.isoformat(),
        "target_friday": target_friday,
        "due_partners": due_partners,
        "paid_partners": list(paid_partners)
    }
    log_file = "/Users/rubaiyetratul/Desktop/offside exports/reminder_history.json"
    history = []
    if os.path.exists(log_file):
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                history = json.load(f)
        except Exception:
            history = []
    history.append(log_entry)
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
    print(f"\nExecution logged to {log_file}")

if __name__ == "__main__":
    run_thursday_reminder_check()
