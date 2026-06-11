#!/usr/bin/env python3
"""
Wiki Watch pipeline - process search results, dedupe, update wiki pages.
Corrected version: updates entities/*.md (the canonical historical files).
"""
import json
import hashlib
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path('/home/hermes/programming-wisdom')
PROFILES_PATH = WIKI_ROOT / 'watch_profiles.json'
TEMP_DIR = Path('/home/hermes/wiki/temp')

# Load profiles
with open(PROFILES_PATH, 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# Load batch results
all_results = {}
for batch_file in sorted(TEMP_DIR.glob('batch*_results.json')):
    with open(batch_file, 'r') as f:
        batch = json.load(f)
    for profile_name, results in batch['results'].items():
        all_results.setdefault(profile_name, []).extend(results)

# Load existing wiki content (entities/) to cross-check what URLs are already present
wiki_files = {
    'python-internals': WIKI_ROOT / 'wiki' / 'entities' / 'python-internals.md',
    'algorithms': WIKI_ROOT / 'wiki' / 'entities' / 'algorithms.md',
    'functional-programming': WIKI_ROOT / 'wiki' / 'entities' / 'functional-programming.md',
    'type-systems': WIKI_ROOT / 'wiki' / 'entities' / 'type-systems.md',
    'compilers': WIKI_ROOT / 'wiki' / 'entities' / 'compilers.md',
    'system-design': WIKI_ROOT / 'wiki' / 'entities' / 'system-design.md',
}

existing_urls = {}
for name, path in wiki_files.items():
    if path.exists():
        content = path.read_text()
        urls = set(re.findall(r'https?://[^\s\)]+', content))
        existing_urls[name] = urls

# Process: dedupe and aggregate by wiki_page
TODAY = datetime.now(timezone.utc).strftime('%Y-%m-%d')
now_iso = datetime.now(timezone.utc).isoformat()

new_entries_by_page = defaultdict(list)  # wiki_page -> [(profile, title, url, hash, kw)]
new_hashes_by_profile = defaultdict(list)
profile_stats = {}

profile_to_wiki_page = {name: prof['wiki_page'] for name, prof in profiles.items()}

# Track all seen hashes across profiles to avoid cross-profile dupes
seen_hashes_global = set()

for profile_name, prof in profiles.items():
    seen_hashes = set(prof['last_result_hashes'])
    wiki_page = prof['wiki_page']
    page_basename = wiki_page.split('/')[-1].replace('.md', '')

    new_count = 0
    sub_topics = []
    profile_hashes_to_add = []

    for result in all_results.get(profile_name, []):
        title = result['title']
        url = result['url']
        kw = page_basename
        h = hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

        # Skip if already in this profile's hashes
        if h in seen_hashes:
            continue
        # Skip if hash already seen in this run globally
        if h in seen_hashes_global:
            continue
        # Safety layer: check actual wiki page for URL
        if url in existing_urls.get(page_basename, set()):
            seen_hashes.add(h)
            profile_hashes_to_add.append(h)
            continue

        seen_hashes.add(h)
        seen_hashes_global.add(h)
        profile_hashes_to_add.append(h)
        new_count += 1

        entry = (profile_name, title, url, h, kw)
        new_entries_by_page[wiki_page].append(entry)
        sub_topics.append(kw)

    new_hashes_by_profile[profile_name] = profile_hashes_to_add
    profile_stats[profile_name] = {
        'new': new_count,
        'sub_topics': sorted(set(sub_topics)) if sub_topics else []
    }

print("=== Profile stats ===")
for p, s in profile_stats.items():
    print(f"  {p}: new={s['new']}")

print(f"\n=== Pages to update ===")
for page, entries in new_entries_by_page.items():
    print(f"  {page}: {len(entries)} entries")
    for p, t, u, h, kw in entries:
        print(f"    - [{p}] {t[:60]} | {u[:50]}...")

# Update each wiki page - insert at FIRST ## Updates
def update_wiki_page(wiki_page_path, entries):
    if not wiki_page_path.exists():
        print(f"  WARNING: {wiki_page_path} does not exist")
        return False

    content = wiki_page_path.read_text()
    lines = content.split('\n')

    insert_after_idx = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after_idx = i + 1
            break

    if insert_after_idx is None:
        in_fm = False
        fm_end = -1
        for i, line in enumerate(lines):
            if line.strip() == '---':
                if not in_fm:
                    in_fm = True
                else:
                    fm_end = i
                    break
        new_section = ['## Updates', '']
        lines = lines[:fm_end+1] + [''] + new_section + lines[fm_end+1:]
        insert_after_idx = fm_end + 3

    new_lines = []
    for profile_name, title, url, h, kw in entries:
        new_lines.append(f"- **{TODAY}** | [{title}]({url}) | kw: {kw}")
    new_lines.append('')

    new_content = lines[:insert_after_idx] + new_lines + lines[insert_after_idx:]
    wiki_page_path.write_text('\n'.join(new_content))
    return True

# Update wiki pages (entities files only)
print("\n=== Updating wiki pages ===")
for wiki_page, entries in new_entries_by_page.items():
    fname = wiki_page.split('/')[-1]
    target = WIKI_ROOT / 'wiki' / 'entities' / fname
    if not target.exists():
        print(f"  WARNING: {target} does not exist")
        continue
    ok = update_wiki_page(target, entries)
    print(f"  {target.name}: {'OK' if ok else 'FAILED'} ({len(entries)} entries)")

# Update watch_profiles.json with new hashes
print("\n=== Updating watch_profiles.json ===")
for profile_name, prof in profiles.items():
    new_hashes = new_hashes_by_profile.get(profile_name, [])
    combined = list(prof['last_result_hashes']) + new_hashes
    prof['last_result_hashes'] = combined[-20:]
    prof['last_run'] = now_iso
    print(f"  {profile_name}: added {len(new_hashes)} hashes (total now: {len(prof['last_result_hashes'])})")

profiles_data['last_run'] = now_iso

with open(PROFILES_PATH, 'w') as f:
    json.dump(profiles_data, f, indent=2)

# Build digest data
digest = {
    'date': TODAY,
    'time': datetime.now(timezone.utc).strftime('%H:%M'),
    'checked': len(profiles),
    'profiles': profile_stats,
    'new_entries': {p: len(e) for p, e in new_entries_by_page.items()},
}
with open(TEMP_DIR / 'digest_data.json', 'w') as f:
    json.dump(digest, f, indent=2)

# Print summary
print("\n=== DIGEST ===")
total_new = sum(s['new'] for s in profile_stats.values())
print(f"Checked: {len(profiles)} profiles, Total new: {total_new}")
for profile_name, prof in profiles.items():
    stats = profile_stats[profile_name]
    if stats['new'] > 0:
        print(f"  {profile_name}: {stats['new']} new")
print("Done.")
