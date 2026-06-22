#!/usr/bin/env python3
"""Wiki watch pipeline: dedupe, group by wiki page, update wiki files."""
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
RUN_TIMESTAMP = "20260622_170022"

# 1. Load all batch files
batch_files = sorted(glob.glob(f"{TEMP_DIR}/watch_run_{RUN_TIMESTAMP}_batch*.json"))
print(f"Loading {len(batch_files)} batch files: {batch_files}")
all_results = {}  # profile_key -> list of {title, url, description}
for bf in batch_files:
    with open(bf) as f:
        data = json.load(f)
    for pkey, pdata in data["profiles"].items():
        all_results.setdefault(pkey, []).extend(pdata["results"])

# 2. Load profiles
with open(PROFILES_PATH) as f:
    profiles = json.load(f)

# 3. Compute hashes and dedupe
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
        title = r["title"]
        url = r["url"]
        h = hashlib.md5(f"{title}{url}".encode("utf-8", errors="replace")).hexdigest()
        if h in seen_hashes or h in last_hashes:
            continue
        # New entry
        seen_hashes.add(h)
        new_entries.append({"hash": h, "title": title, "url": url, "description": r.get("description", "")})
        new_hashes_this_run.append(h)
        # Sub-topic discovery from title (split into words, take meaningful tokens)
        title_words = re.findall(r"[A-Za-z][A-Za-z0-9\-_/]{2,}", title)
        for w in title_words:
            if w not in existing_sub_topics and w not in new_sub_topics and len(w) >= 3:
                # Skip very common junk
                if w.lower() in {"the","and","for","with","this","from","into","your","what","how","why","you","can","are","not","all","one","has","had","was","but","its","out","top","new","use","via","over","more","best","guide","list","every","most","good","great","real","dead","still","again","been","just","than","then","they","them","his","her","him","she","our","your","their","will","would","could","should","about","after","before","between","without","because","while","during","through","under","such","each","same","other","some","any","few","many","much","very","too","also","only","own","same","few","own"}:
                    continue
                new_sub_topics.append(w)

    new_by_profile[pkey] = new_entries
    all_new_hashes[pkey] = new_hashes_this_run
    new_sub_topics_per_profile[pkey] = new_sub_topics[:20]  # cap

print("\n=== Summary of new results per profile ===")
total_new = 0
for pkey in profiles:
    n = len(new_by_profile[pkey])
    total_new += n
    print(f"  {pkey}: {n} new results, {len(new_sub_topics_per_profile[pkey])} new sub-topics")
    if new_by_profile[pkey]:
        for e in new_by_profile[pkey][:3]:
            print(f"    - {e['title'][:80]}")
print(f"TOTAL new entries: {total_new}")

# 4. Group by wiki_page (aggregate before updating)
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

    # Find FIRST "## Updates" line
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == "## Updates":
            insert_after = i + 1
            break

    if insert_after is None:
        # No Updates section — add one at the bottom
        lines.append("")
        lines.append("## Updates")
        lines.append("")
        insert_after = len(lines) - 1

    # Build new entries
    new_lines = []
    for entry in entries:
        kw = entry["profile"]
        new_lines.append(f"{date_marker} | [{entry['title']}]({entry['url']}) | kw: {kw}")

    lines = lines[:insert_after] + new_lines + [""] + lines[insert_after:]
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"UPDATED: {page} — {len(entries)} new entries (profiles: {', '.join(page_profile_map[page])})")

# 6. Update watch_profiles.json — append hashes (max 20), update last_run
now_iso = datetime.now(timezone.utc).isoformat()
for pkey, profile in profiles.items():
    new_h = all_new_hashes[pkey]
    combined = (profile.get("last_result_hashes", []) + new_h)[-20:]
    profile["last_result_hashes"] = combined
    profile["last_run"] = now_iso
    profile["last_new_count"] = len(new_by_profile[pkey])
    # Merge sub-topics
    existing = set(profile.get("sub_topics", []))
    for s in new_sub_topics_per_profile[pkey]:
        if s not in existing:
            profile.setdefault("sub_topics", []).append(s)
            existing.add(s)
    profile["new_sub_topics_this_run"] = new_sub_topics_per_profile[pkey]

with open(PROFILES_PATH, "w") as f:
    json.dump(profiles, f, indent=2, ensure_ascii=False)
print("\nUPDATED: watch_profiles.json")

# 7. Save digest data for Discord step
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
