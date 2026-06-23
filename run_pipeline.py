#!/usr/bin/env python3
"""Wiki watch pipeline for cron run 2026-06-23 04:16 UTC.

Reads:
  - /home/hermes/wiki/temp/watch_run_20260623_041605_batch{1,2}.json  (search results)
  - /home/hermes/wiki/watch_profiles.json                             (profiles + hashes)
  - /home/hermes/wiki/entities/*.md                                    (wiki pages)

Writes:
  - updates to /home/hermes/wiki/entities/*.md
  - updated /home/hermes/wiki/watch_profiles.json
  - /home/hermes/wiki/temp/watch_run_20260623_041605_digest.json
"""
import hashlib
import json
import os
import re
import glob
from collections import defaultdict
from datetime import datetime, timezone

WIKI_DIR = "/home/hermes/wiki"
PROFILES_PATH = f"{WIKI_DIR}/watch_profiles.json"
ENTITIES_DIR = f"{WIKI_DIR}/entities"
TEMP_DIR = f"{WIKI_DIR}/temp"
RUN_TIMESTAMP = "20260623_041605"

# Common noise words for sub-topic filtering
STOP = {
    "the","and","for","with","this","from","into","your","what","how","why","you","can","are","not","all","one","has","had","was","but","its","out","top","new","use","via","over","more","best","guide","list","every","most","good","great","real","dead","still","again","been","just","than","then","they","them","his","her","him","she","our","your","their","will","would","could","should","about","after","before","between","without","because","while","during","through","under","such","each","same","other","some","any","few","many","much","very","too","also","only","own","same","few","own","who","why","where","when","which","while","being","these","those","here","there","does","done","doing","have","having","make","makes","made","part","parts","year","years","2026","2025","2024","2023","2022","data","code","using","like","build","review","based","first","next","need","want","look","looks","keep","know","learn","ways","says","said","lets","gets","give","giving","take","taking","find","finding","help","helps","show","shows","turn","turns","start","starts","going","comes","comes","becoming","yet","though","even","really","actually","getting","things","thing","first","second","third","latest","newer","older","recent","update","updates","updated","version","versions","post","posts","article","articles","blog","blogs","read","reading","free","without","against","among","across","behind","beyond","toward","towards","upon","within","upon","since","though","unless","until","upon","per","plus","near","nearby","fewer","fewest","nearly","quite","rather","almost","already","always","never","often","sometimes","rarely","seldom","usually"
}

# 1. Load batch files
batch_files = sorted(glob.glob(f"{TEMP_DIR}/watch_run_{RUN_TIMESTAMP}_batch*.json"))
print(f"Loading {len(batch_files)} batch files: {batch_files}")
all_results = {}
for bf in batch_files:
    with open(bf) as f:
        data = json.load(f)
    for pkey, pdata in data["profiles"].items():
        all_results.setdefault(pkey, []).extend(pdata["results"])

# 2. Load profiles
with open(PROFILES_PATH) as f:
    profiles = json.load(f)

# 3. Hash dedupe (skip empty titles)
seen_hashes = set()
new_by_profile = {}
all_new_hashes = {}
new_sub_topics_per_profile = {}

for pkey, profile in profiles.items():
    results = all_results.get(pkey, [])
    last_hashes = set(profile.get("last_result_hashes", []))
    existing_sub_topics = set(profile.get("sub_topics", []))
    new_entries = []
    new_hashes_this_run = []
    new_sub_topics = []

    for r in results:
        title = (r.get("title") or "").strip()
        url = (r.get("url") or "").strip()
        if not title or not url or not url.startswith("http"):
            continue
        h = hashlib.md5(f"{title}{url}".encode("utf-8", errors="replace")).hexdigest()
        if h in seen_hashes or h in last_hashes:
            continue
        seen_hashes.add(h)
        new_entries.append({
            "hash": h, "title": title, "url": url,
            "description": r.get("description", "")
        })
        new_hashes_this_run.append(h)

        # Sub-topic discovery
        title_words = re.findall(r"[A-Za-z][A-Za-z0-9\-_/]{2,}", title)
        for w in title_words:
            if w in existing_sub_topics or w in new_sub_topics:
                continue
            if len(w) < 4:
                continue
            if w.lower() in STOP:
                continue
            new_sub_topics.append(w)

    new_by_profile[pkey] = new_entries
    all_new_hashes[pkey] = new_hashes_this_run
    new_sub_topics_per_profile[pkey] = new_sub_topics[:20]

print("\n=== Summary of new results per profile ===")
total_new = 0
for pkey in profiles:
    n = len(new_by_profile[pkey])
    total_new += n
    nsub = len(new_sub_topics_per_profile[pkey])
    print(f"  {pkey}: {n} new results, {nsub} new sub-topics")
    for e in new_by_profile[pkey][:3]:
        print(f"    - {e['title'][:80]}")
print(f"TOTAL new entries: {total_new}")

# 4. Group by wiki_page
page_entries = defaultdict(list)
page_profile_map = defaultdict(list)
for pkey, entries in new_by_profile.items():
    page = profiles[pkey]["wiki_page"]
    for e in entries:
        page_entries[page].append({"profile": pkey, **e})
        if pkey not in page_profile_map[page]:
            page_profile_map[page].append(pkey)

# 5. Update wiki pages
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
date_marker = f"- **{TODAY}**"

for page, entries in page_entries.items():
    path = f"{ENTITIES_DIR}/{page}"
    if not os.path.exists(path):
        print(f"SKIP: {page} does not exist")
        continue

    with open(path, "r") as f:
        content = f.read()
    lines = content.split("\n")

    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == "## Updates":
            insert_after = i + 1
            break
    if insert_after is None:
        lines.extend(["", "## Updates", ""])
        insert_after = len(lines) - 1

    new_lines = []
    for entry in entries:
        kw = entry["profile"]
        new_lines.append(f"{date_marker} | [{entry['title']}]({entry['url']}) | kw: {kw}")

    lines = lines[:insert_after] + new_lines + [""] + lines[insert_after:]
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"UPDATED: {page} — {len(entries)} new entries (profiles: {', '.join(page_profile_map[page])})")

# 6. Update watch_profiles.json
now_iso = datetime.now(timezone.utc).isoformat()
for pkey, profile in profiles.items():
    new_h = all_new_hashes[pkey]
    combined = (profile.get("last_result_hashes", []) + new_h)[-20:]
    profile["last_result_hashes"] = combined
    profile["last_run"] = now_iso
    profile["last_new_count"] = len(new_by_profile[pkey])
    existing = set(profile.get("sub_topics", []))
    for s in new_sub_topics_per_profile[pkey]:
        if s not in existing:
            profile.setdefault("sub_topics", []).append(s)
            existing.add(s)
    profile["new_sub_topics_this_run"] = new_sub_topics_per_profile[pkey]

with open(PROFILES_PATH, "w") as f:
    json.dump(profiles, f, indent=2, ensure_ascii=False)
print("\nUPDATED: watch_profiles.json")

# 7. Save digest
digest = {
    "timestamp": now_iso,
    "total_new": total_new,
    "profiles": {}
}
for pkey in profiles:
    digest["profiles"][pkey] = {
        "wiki_page": profiles[pkey]["wiki_page"],
        "new_count": len(new_by_profile[pkey]),
        "entries": new_by_profile[pkey],
        "new_sub_topics": new_sub_topics_per_profile[pkey],
    }
with open(f"{TEMP_DIR}/watch_run_{RUN_TIMESTAMP}_digest.json", "w") as f:
    json.dump(digest, f, indent=2, ensure_ascii=False)
print(f"WROTE: watch_run_{RUN_TIMESTAMP}_digest.json")