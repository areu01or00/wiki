#!/usr/bin/env python3
"""Wiki watch pipeline: process batch results, dedup, update wiki, update profiles."""
import json
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

WIKI_DIR = Path("/home/hermes/programming-wisdom/wiki")
ENTITIES_DIR = WIKI_DIR / "entities"
PROFILES_PATH = WIKI_DIR.parent / "watch_profiles.json"
TEMP_DIR = Path("/home/hermes/wiki/temp")

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

# Load profiles
with open(PROFILES_PATH) as f:
    profiles_data = json.load(f)

# Load both batch results
batch1 = json.load(open(TEMP_DIR / "watch_run_2026-06-11_03-17_batch1.json"))
batch2 = json.load(open(TEMP_DIR / "watch_run_2026-06-11_03-17_batch2.json"))

# Merge into single {profile: [results]} structure
all_results = {}
for batch in (batch1, batch2):
    for profile_name, results in batch["results"].items():
        all_results.setdefault(profile_name, []).extend(results)

print(f"Loaded {len(all_results)} profiles, total results: {sum(len(r) for r in all_results.values())}")

# Also load existing wiki page URLs for safety cross-check
def extract_urls_from_wiki(path):
    if not path.exists():
        return set()
    text = path.read_text()
    # Find all markdown links [text](url)
    return set(re.findall(r'\]\((https?://[^)]+)\)', text))

existing_urls_by_page = {}
for profile_name, profile in profiles_data["profiles"].items():
    wiki_page = profile.get("wiki_page", f"entities/{profile_name}.md")
    page_path = WIKI_DIR / wiki_page
    existing_urls_by_page[wiki_page] = extract_urls_from_wiki(page_path)

# Process each profile
new_entries_by_page = {}  # wiki_page -> [(title, url, keyword)]
new_hashes_by_profile = {}

for profile_name, profile in profiles_data["profiles"].items():
    wiki_page = profile.get("wiki_page", f"entities/{profile_name}.md")
    existing_hashes = set(profile.get("last_result_hashes", []))
    existing_urls = existing_urls_by_page.get(wiki_page, set())
    new_hashes = []
    new_entries = []
    seen_this_run = set()  # avoid dupes within the same batch

    for r in all_results.get(profile_name, []):
        title = r["title"]
        url = r["url"]
        h = hashlib.md5(f"{title}{url}".encode("utf-8", errors="replace")).hexdigest()

        # Dedup checks: hash in known list, OR url already on wiki page
        if h in existing_hashes:
            continue
        if h in seen_this_run:
            continue
        if url in existing_urls:
            continue
        # Cross-check: also try hashing with a small URL variation in case title differs
        # (Safety layer: if any existing entry has same URL, skip)

        seen_this_run.add(h)
        new_hashes.append(h)
        new_entries.append((title, url, profile_name))

    if new_entries:
        new_entries_by_page.setdefault(wiki_page, []).extend(new_entries)
    new_hashes_by_profile[profile_name] = new_hashes

# Now update wiki pages
for wiki_page, entries in new_entries_by_page.items():
    page_path = WIKI_DIR / wiki_page
    if not page_path.exists():
        print(f"  WARN: {page_path} not found, skipping")
        continue
    content = page_path.read_text()
    lines = content.split("\n")
    new_lines_block = []
    for title, url, kw in entries:
        new_lines_block.append(f"- **{today}** | [{title}]({url}) | kw: {kw}")
    # Find first `## Updates` and insert right after it
    found = False
    for i, line in enumerate(lines):
        if line.strip() == "## Updates":
            # insert after the heading
            insert_idx = i + 1
            # Skip any leading blank lines right after the heading
            j = insert_idx
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            # Insert at j (after existing leading blanks), preserving blank-line break
            new_block = new_lines_block + [""]  # trailing blank
            lines = lines[:insert_idx] + new_block + lines[insert_idx:]
            found = True
            break
    if not found:
        print(f"  WARN: '## Updates' not found in {page_path}, appending")
        lines.append("## Updates")
        lines.append("")
        lines.extend(new_lines_block)
    page_path.write_text("\n".join(lines))
    print(f"  Updated {wiki_page}: +{len(entries)} entries")

# Update watch_profiles.json
for profile_name, profile in profiles_data["profiles"].items():
    new_h = new_hashes_by_profile.get(profile_name, [])
    existing = profile.get("last_result_hashes", [])
    combined = new_h + existing  # newest first
    # Cap at 20
    profile["last_result_hashes"] = combined[:20]
    profile["last_run"] = now_iso

profiles_data["last_run"] = now_iso
profiles_data["last_updated"] = now_iso

with open(PROFILES_PATH, "w") as f:
    json.dump(profiles_data, f, indent=2)
    f.write("\n")

# Save full run results for digest
run_summary = {
    "timestamp": now_iso,
    "by_wiki": {p: len(v) for p, v in new_entries_by_page.items()},
    "total_new": sum(len(v) for v in new_entries_by_page.values()),
    "entries": {p: [{"title": t, "url": u, "keyword": k} for t, u, k in v] for p, v in new_entries_by_page.items()},
}
summary_path = TEMP_DIR / f"watch_run_2026-06-11_03-17_summary.json"
with open(summary_path, "w") as f:
    json.dump(run_summary, f, indent=2)
print(f"\nSummary: {run_summary['total_new']} new entries across {len(new_entries_by_page)} pages")
print(f"  by_wiki: {run_summary['by_wiki']}")
