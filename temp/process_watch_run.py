#!/usr/bin/env python3
"""Wiki watch pipeline - process search results, dedupe, update wiki pages."""
import json
import hashlib
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path('/home/hermes/programming-wisdom')
PROFILES_PATH = WIKI_ROOT / 'watch_profiles.json'
TEMP_DIR = Path('/home/hermes/wiki/temp')
ENTITIES_DIR = WIKI_ROOT / 'wiki' / 'entities'

# Load profiles
with open(PROFILES_PATH, 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# Load batch results
all_results = {}
batch_files = sorted(TEMP_DIR.glob('watch_run_2026-06-10_21-31_batch*.json'))
for batch_file in batch_files:
    with open(batch_file, 'r') as f:
        batch = json.load(f)
    for profile_name, results in batch['results'].items():
        all_results.setdefault(profile_name, []).extend(results)

# Load existing wiki content (entities/) to cross-check what URLs are already present
def url_in_file(url, path):
    if not path.exists():
        return False
    content = path.read_text()
    return url in content

TODAY = datetime.now(timezone.utc).strftime('%Y-%m-%d')
now_iso = datetime.now(timezone.utc).isoformat()

# Process: dedupe and aggregate by wiki_page
new_entries_by_page = defaultdict(list)  # wiki_page -> [(profile, title, url, hash, kw)]
new_hashes_by_profile = defaultdict(list)
profile_stats = {}

# Track all seen hashes across profiles to avoid cross-profile dupes
seen_hashes_global = set()

for profile_name, prof in profiles.items():
    # Normalize last_result_hashes: only accept strings (skip stray dicts)
    raw_hashes = prof.get('last_result_hashes', [])
    seen_hashes = set()
    for h in raw_hashes:
        if isinstance(h, str) and len(h) == 32:
            seen_hashes.add(h)
    wiki_page = prof['wiki_page']
    page_basename = wiki_page.split('/')[-1]  # 'python-internals.md'
    page_name = page_basename.replace('.md', '')  # 'python-internals'
    target_file = ENTITIES_DIR / page_basename

    new_count = 0
    sub_topics = []
    profile_hashes_to_add = []

    for result in all_results.get(profile_name, []):
        title = result['title']
        url = result['url']
        kw = page_name
        h = hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

        # Skip if already in this profile's hashes
        if h in seen_hashes:
            continue
        # Skip if hash already seen in this run globally
        if h in seen_hashes_global:
            continue
        # Safety layer: check actual wiki page for URL
        if url_in_file(url, target_file):
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
        print(f"    - [{p}] {t[:60]} | {u[:60]}...")

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
        # No Updates section - create one
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

    # Also update frontmatter updated + last_watched
    content2 = wiki_page_path.read_text()
    lines2 = content2.split('\n')
    for i, line in enumerate(lines2):
        if line.startswith('updated:'):
            lines2[i] = f"updated: {TODAY}"
        if line.startswith('last_watched:'):
            lines2[i] = f"last_watched: \"{now_iso}\""
    wiki_page_path.write_text('\n'.join(lines2))

    return True

# Update wiki pages
print("\n=== Updating wiki pages ===")
for wiki_page, entries in new_entries_by_page.items():
    fname = wiki_page.split('/')[-1]
    target = ENTITIES_DIR / fname
    if not target.exists():
        print(f"  WARNING: {target} does not exist")
        continue
    ok = update_wiki_page(target, entries)
    print(f"  {target.name}: {'OK' if ok else 'FAILED'} ({len(entries)} entries)")

# Update watch_profiles.json with new hashes
print("\n=== Updating watch_profiles.json ===")
for profile_name, prof in profiles.items():
    new_hashes = new_hashes_by_profile.get(profile_name, [])
    # Normalize existing hashes (filter non-strings)
    existing = [h for h in prof.get('last_result_hashes', []) if isinstance(h, str) and len(h) == 32]
    combined = existing + new_hashes
    prof['last_result_hashes'] = combined[-20:]
    prof['last_run'] = now_iso
    print(f"  {profile_name}: added {len(new_hashes)} hashes (total now: {len(prof['last_result_hashes'])})")

profiles_data['last_updated'] = now_iso

with open(PROFILES_PATH, 'w') as f:
    json.dump(profiles_data, f, indent=2)

# Build digest data
digest = {
    'date': TODAY,
    'time': datetime.now(timezone.utc).strftime('%H:%M'),
    'checked': len(profiles),
    'profiles': profile_stats,
    'new_entries_by_page': {p: len(e) for p, e in new_entries_by_page.items()},
    'flat_entries': [
        {'profile': p, 'title': t, 'url': u, 'wiki_page': wp}
        for wp, entries in new_entries_by_page.items()
        for (p, t, u, h, kw) in entries
    ]
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
