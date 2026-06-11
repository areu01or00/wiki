#!/usr/bin/env python3
"""Wiki watch pipeline: dedup, update pages, update profiles."""
import json, hashlib, datetime, os, sys

TIMESTAMP = "2026-06-11_11-00"
PROFILES_PATH = "/home/hermes/programming-wisdom/watch_profiles.json"
WIKI_ROOT = "/home/hermes/programming-wisdom/wiki"
BATCH1 = f"/home/hermes/wiki/temp/watch_run_{TIMESTAMP}_batch1.json"
BATCH2 = f"/home/hermes/wiki/temp/watch_run_{TIMESTAMP}_batch2.json"

# Load profiles
with open(PROFILES_PATH, 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# Load batch results
all_results = {}
for path in [BATCH1, BATCH2]:
    with open(path, 'r') as f:
        batch = json.load(f)
        for profile_name, results in batch.items():
            if profile_name not in all_results:
                all_results[profile_name] = []
            all_results[profile_name].extend(results)

# Compute hashes and dedup
new_by_profile = {}
new_hashes_by_profile = {}
for profile_name, results in all_results.items():
    existing_hashes = set(profiles[profile_name]['last_result_hashes'])
    new_results = []
    new_hashes = []
    for r in results:
        title = r['title']
        url = r['url']
        h = hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()
        if h not in existing_hashes:
            new_results.append(r)
            new_hashes.append(h)
    new_by_profile[profile_name] = new_results
    new_hashes_by_profile[profile_name] = new_hashes

# Print summary
total_new = 0
for p, results in new_by_profile.items():
    print(f"{p}: {len(results)} new results")
    total_new += len(results)
print(f"\nTotal new results: {total_new}")

# Group by wiki_page for aggregation
page_groups = {}  # wiki_page -> [(profile_name, result)]
for profile_name, results in new_by_profile.items():
    if results:
        wiki_page = profiles[profile_name]['wiki_page']
        if wiki_page not in page_groups:
            page_groups[wiki_page] = []
        for r in results:
            page_groups[wiki_page].append((profile_name, r))

# Update wiki pages
today = datetime.datetime.now().strftime('%Y-%m-%d')
for wiki_page, entries in page_groups.items():
    filepath = f"{WIKI_ROOT}/{wiki_page}"
    if not os.path.exists(filepath):
        print(f"WARNING: {filepath} does not exist, skipping")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find ## Updates section
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is None:
        # Append at end
        insert_after = len(lines)
        lines.append('')
        lines.append('## Updates')
        lines.append('')
        insert_after = len(lines)
    
    # Build entries
    new_lines = []
    for profile_name, r in entries:
        title = r['title']
        url = r['url']
        source = profile_name
        # Extract a keyword from the title/description
        keyword = title.split('|')[0].strip()[:40]
        new_lines.append(f"- **{today}** | [{title}]({url}) | kw: {keyword} | source: {source}")
    
    lines = lines[:insert_after] + new_lines + [''] + lines[insert_after:]
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Updated {wiki_page}: added {len(new_lines)} entries")

# Update watch_profiles.json - append new hashes (max 20)
now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
for profile_name, hashes in new_hashes_by_profile.items():
    if hashes:
        current = profiles[profile_name]['last_result_hashes']
        current.extend(hashes)
        # Keep max 20
        profiles[profile_name]['last_result_hashes'] = current[-20:]
        profiles[profile_name]['last_run'] = now_iso

profiles_data['profiles'] = profiles
profiles_data['last_run'] = now_iso
profiles_data['last_updated'] = now_iso

with open(PROFILES_PATH, 'w') as f:
    json.dump(profiles_data, f, indent=2)

print(f"\nUpdated {PROFILES_PATH}")

# Generate digest data
digest = {
    "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M'),
    "checked": len(profiles),
    "new_by_profile": {},
    "total_new": total_new
}

for profile_name, results in new_by_profile.items():
    if results:
        digest["new_by_profile"][profile_name] = {
            "count": len(results),
            "results": [{"title": r['title'], "url": r['url']} for r in results]
        }

with open(f"/home/hermes/wiki/temp/digest_data_{TIMESTAMP}.json", 'w') as f:
    json.dump(digest, f, indent=2)

print(f"Saved digest data to digest_data_{TIMESTAMP}.json")
print("\nDONE")
