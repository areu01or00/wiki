#!/usr/bin/env python3
"""Send wiki watch digest to Discord channel 1491398499521003622."""
import urllib.request
import urllib.error
import json
import re
from datetime import datetime, timezone
from urllib.parse import urlparse

# Load .env
with open('/home/hermes/.hermes/.env') as f:
    env_content = f.read()

def get_env(key):
    m = re.search(rf'^{re.escape(key)}=(.*?)$', env_content, re.MULTILINE)
    return m.group(1).strip() if m else None

DISCORD_TOKEN = get_env('DISCORD_BOT_TOKEN') or get_env('DISCORD_TOKEN')
CHANNEL_ID = "1491398499521003622"

# Load digest
DIGEST_PATH = '/home/hermes/wiki/temp/digest_1781120784.json'
with open(DIGEST_PATH) as f:
    digest = json.load(f)

# Topic display names
DISPLAY_TOPIC = {
    'python-internals': 'Python Internals',
    'algorithms': 'Algorithms & Data Structures',
    'functional-programming': 'Functional Programming',
    'type-systems': 'Type Systems',
    'compilers': 'Compilers & LLVM',
    'system-design': 'System Design',
}

# Build digest in the required format
lines = []
lines.append(f"## 🔄 Wiki Watch Digest — {digest['date_utc']}")
lines.append(f"Checked: {digest['checked']} profiles")

# Group entries by profile
by_profile = {}
for e in digest['new_entries']:
    by_profile.setdefault(e['profile'], []).append(e)

# Order: standard profile order
profile_order = ['python-internals', 'algorithms', 'functional-programming',
                 'type-systems', 'compilers', 'system-design']
for prof in profile_order:
    if prof not in by_profile:
        continue
    entries = by_profile[prof]
    topic = DISPLAY_TOPIC.get(prof, prof)
    lines.append(f"### {topic}")
    lines.append(f"New: {len(entries)} results")
    for e in entries:
        try:
            host = urlparse(e['url']).netloc.replace('www.', '')
            source = host
        except Exception:
            source = prof
        lines.append(f"- [{e['title']}]({e['url']}) | {source}")
    sub_topics = digest.get('sub_topics', {}).get(prof, [])
    if sub_topics:
        lines.append(f"Added sub-topics: {', '.join(sub_topics)}")
    else:
        lines.append("Added sub-topics: (none)")
    lines.append("---")

if not by_profile:
    lines.append("### All topics")
    lines.append("New: 0 results")
    lines.append("No new entries across any profile. All search results already in their respective wiki pages.")
    lines.append("Added sub-topics: (none)")
    lines.append("---")

msg = "\n".join(lines)
print(f"Message length: {len(msg)} chars")
print("---")
print(msg)
print("---")

# Save draft
draft_path = '/home/hermes/wiki/temp/discord_digest_1781120784.md'
with open(draft_path, 'w') as f:
    f.write(msg)
print(f"Draft saved to {draft_path}")

# Send to Discord
def send_chunk(text, label=""):
    if not DISCORD_TOKEN:
        print("No DISCORD_TOKEN, skipping")
        return False
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    payload = json.dumps({"content": text}).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": "Bot " + DISCORD_TOKEN,
        "User-Agent": "DiscordBot (hermes-agent, 1.0)",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())
            print(f"  {label}Delivered: {resp.status} - id: {result.get('id', 'unknown')}")
            return True
    except urllib.error.HTTPError as e:
        print(f"  {label}HTTP Error: {e.code} {e.reason}")
        try:
            print(f"  Body: {e.read().decode()[:500]}")
        except Exception:
            pass
        return False
    except Exception as e:
        print(f"  {label}Error: {type(e).__name__} {e}")
        return False

if DISCORD_TOKEN:
    print(f"Token starts with: {DISCORD_TOKEN[:10]}...")
    if len(msg) <= 2000:
        send_chunk(msg, "[digest] ")
    else:
        chunks = []
        current = ""
        for line in msg.split("\n"):
            if len(current) + len(line) + 1 > 1900:
                chunks.append(current)
                current = line
            else:
                current = current + "\n" + line if current else line
        if current:
            chunks.append(current)
        for i, chunk in enumerate(chunks):
            send_chunk(chunk, f"[part {i+1}/{len(chunks)}] ")
else:
    print("DISCORD_BOT_TOKEN not set - skipping send")
