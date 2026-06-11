#!/usr/bin/env python3
"""Wiki watch processor: dedup search results and update wiki pages."""
import hashlib
import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path("/home/hermes/programming-wisdom")
PROFILES_PATH = WIKI_ROOT / "watch_profiles.json"
TEMP_DIR = Path("/home/hermes/wiki/temp")
ENTITIES_DIR = WIKI_ROOT / "wiki" / "entities"
TS = 1781105470
NOW_UTC = datetime.fromtimestamp(TS, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
TODAY = datetime.fromtimestamp(TS, tz=timezone.utc).strftime("%Y-%m-%d")

# Load profiles
with open(PROFILES_PATH) as f:
    profiles_data = json.load(f)
profiles = profiles_data["profiles"]

# Load batch files
all_results = {}
for batch_file in sorted(TEMP_DIR.glob(f"watch_run_{TS}_batch*.json")):
    with open(batch_file) as f:
        batch = json.load(f)
    for prof_name, prof_data in batch["results"].items():
        all_results[prof_name] = prof_data

print(f"Loaded {len(all_results)} profiles from batch files")

# Step 3: Hash dedup
def h(title, url):
    return hashlib.md5(f"{title}{url}".encode("utf-8", errors="replace")).hexdigest()

# Junk URL patterns to filter
def is_junk(url):
    if not url or not url.startswith("http"):
        return True
    if "/clev?event=" in url:
        return True
    typing_sites = ["typing.com", "typingclub.com", "monkeytype.com", "typingtest.com", "typeracer.com", "10fastfingers.com", "speedtypingonline.com"]
    if any(s in url for s in typing_sites):
        return True
    return False

# Group new entries by wiki_page
new_by_page = defaultdict(list)
discarded_count = 0
junk_count = 0
new_hashes_by_profile = {}

for prof_name, prof_data in all_results.items():
    profile = profiles[prof_name]
    seen_hashes = set(profile["last_result_hashes"])
    new_hashes = []
    for item in prof_data["web"]:
        title = item["title"]
        url = item["url"]
        if is_junk(url):
            junk_count += 1
            continue
        hh = h(title, url)
        if hh in seen_hashes:
            discarded_count += 1
            continue
        kw = prof_name.replace("-", " ")
        wiki_page = profile["wiki_page"]
        new_by_page[wiki_page].append({
            "title": title,
            "url": url,
            "hash": hh,
            "kw": kw,
            "profile": prof_name,
        })
        new_hashes.append(hh)
    new_hashes_by_profile[prof_name] = new_hashes

print(f"Filtered junk: {junk_count}")
print(f"Discarded (dup) hashes: {discarded_count}")
print(f"New entries by page:")
for page, entries in new_by_page.items():
    print(f"  {page}: {len(entries)} new")

# Step 5: Update wiki pages
def update_wiki_page(wiki_page_rel, new_entries):
    path = WIKI_ROOT / "wiki" / wiki_page_rel
    if not path.exists():
        print(f"  ! Missing wiki file: {path}")
        return False
    with open(path) as f:
        content = f.read()
    lines = content.split("\n")
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == "## Updates":
            insert_after = i + 1
            break
    if insert_after is None:
        lines.append("## Updates")
        lines.append("")
        insert_after = len(lines)
    formatted = [f"- **{TODAY}** | [{e['title']}]({e['url']}) | kw: {e['kw']}" for e in new_entries]
    lines = lines[:insert_after] + formatted + [""] + lines[insert_after:]
    with open(path, "w") as f:
        f.write("\n".join(lines))
    return True

print()
print("Updating wiki pages:")
for wiki_page, entries in new_by_page.items():
    print(f"  {wiki_page} (+{len(entries)} entries)")
    update_wiki_page(wiki_page, entries)

# Step 6: Update watch_profiles.json
for prof_name, new_hashes in new_hashes_by_profile.items():
    if not new_hashes:
        continue
    profile = profiles[prof_name]
    combined = new_hashes + profile["last_result_hashes"]
    profile["last_result_hashes"] = combined[:20]
    profile["last_run"] = NOW_UTC
profiles_data["last_run"] = NOW_UTC

with open(PROFILES_PATH, "w") as f:
    json.dump(profiles_data, f, indent=2)
print()
print(f"Updated {PROFILES_PATH}")

# Step 8: Build Discord digest
print()
print("=" * 60)
print("DISCORD DIGEST")
print("=" * 60)
total_new = sum(len(v) for v in new_by_page.values())
print(f"## 🔄 Wiki Watch Digest — {NOW_UTC}")
print(f"Checked: {len(profiles)} profiles")
for prof_name, prof_data in all_results.items():
    n_new = len(new_hashes_by_profile[prof_name])
    if n_new == 0:
        continue
    profile = profiles[prof_name]
    pretty = prof_name.replace("-", " ").title()
    print(f"### {pretty}")
    print(f"New: {n_new} results")
    page = profile["wiki_page"]
    page_entries = new_by_page.get(page, [])
    prof_entries = [e for e in page_entries if e["profile"] == prof_name]
    for e in prof_entries:
        url = e["url"]
        if "arxiv" in url:
            source = "arxiv"
        elif "wikipedia" in url:
            source = "wikipedia"
        elif "github" in url:
            source = "github"
        elif "medium" in url:
            source = "medium"
        elif "youtube" in url:
            source = "youtube"
        elif "reddit" in url:
            source = "reddit"
        elif "stackoverflow" in url:
            source = "stackoverflow"
        elif "linkedin" in url:
            source = "linkedin"
        elif ".edu" in url or "acm" in url or "dl.acm" in url:
            source = "academic"
        else:
            try:
                source = url.split("/")[2]
            except IndexError:
                source = "web"
        print(f"- [{e['title']}]({e['url']}) | {source}")
    subs = [e["title"][:50] for e in prof_entries[:3]]
    print(f"Added sub-topics: {', '.join(subs)}")
    print("---")
print()
print(f"TOTAL NEW: {total_new}")
