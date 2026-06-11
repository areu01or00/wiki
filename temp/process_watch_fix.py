#!/usr/bin/env python3
"""Wiki watch pipeline - fix: update correct wiki entities."""
import json
import hashlib
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path('/home/hermes/programming-wisdom')
ENTITIES_DIR = WIKI_ROOT / 'wiki' / 'entities'
PROFILES_PATH = WIKI_ROOT / 'watch_profiles.json'
TEMP_DIR = Path('/home/hermes/wiki/temp')

# Load profiles
with open(PROFILES_PATH, 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# Load batch results from this run
all_results = {}
for batch_file in sorted(TEMP_DIR.glob('watch_run_2026-06-11_07-01_*.json')):
    with open(batch_file, 'r') as f:
        batch = json.load(f)
    for profile_name, data in batch.items():
        results = data.get('results', [])
        all_results.setdefault(profile_name, []).extend(results)

print(f"Loaded {sum(len(v) for v in all_results.values())} search results across {len(all_results)} profiles")

# Load existing wiki content to cross-check URLs
existing_urls = {}
for name, prof in profiles.items():
    wiki_page = prof['wiki_page']
    page_file = ENTITIES_DIR / wiki_page.split('/')[-1]
    if page_file.exists():
        content = page_file.read_text()
        urls = set(re.findall(r'https?://[^\s\)]+', content))
        existing_urls[name] = urls
    else:
        existing_urls[name] = set()

TODAY = datetime.now(timezone.utc).strftime('%Y-%m-%d')
now_iso = datetime.now(timezone.utc).isoformat()

new_entries_by_page = defaultdict(list)
new_hashes_by_profile = defaultdict(list)
profile_stats = {}
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
        
        if h in seen_hashes:
            continue
        if h in seen_hashes_global:
            continue
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

print("\nProfile stats:")
for p, s in profile_stats.items():
    print(f"  {p}: new={s['new']}, sub_topics={s['sub_topics']}")

print(f"\nPages to update:")
for page, entries in new_entries_by_page.items():
    print(f"  {page}: {len(entries)} entries")

# Update wiki pages
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
        # Add new section after frontmatter
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

print("\nUpdating wiki pages:")
total_new = 0
for wiki_page, entries in new_entries_by_page.items():
    fname = wiki_page.split('/')[-1]
    target = ENTITIES_DIR / fname
    if not target.exists():
        print(f"  WARNING: {target} does not exist")
        continue
    ok = update_wiki_page(target, entries)
    print(f"  {target.name}: {'OK' if ok else 'FAILED'} ({len(entries)} entries)")
    total_new += len(entries)

# Update watch_profiles.json
print("\nUpdating watch_profiles.json:")
for profile_name, prof in profiles.items():
    new_hashes = new_hashes_by_profile.get(profile_name, [])
    combined = list(prof['last_result_hashes']) + new_hashes
    prof['last_result_hashes'] = combined[-20:]
    prof['last_run'] = now_iso
    print(f"  {profile_name}: added {len(new_hashes)} hashes (total now: {len(prof['last_result_hashes'])})")

profiles_data['last_run'] = now_iso
profiles_data['last_updated'] = now_iso

with open(PROFILES_PATH, 'w') as f:
    json.dump(profiles_data, f, indent=2)

# Build digest data
digest = {
    'date': TODAY,
    'time': datetime.now(timezone.utc).strftime('%H:%M'),
    'checked': len(profiles),
    'profiles': profile_stats,
    'new_entries': {p: len(e) for p, e in new_entries_by_page.items()},
    'total_new': total_new,
}
with open(TEMP_DIR / 'digest_data.json', 'w') as f:
    json.dump(digest, f, indent=2)

print(f"\n=== DONE ===")
print(f"Checked: {len(profiles)} profiles, Total new: {total_new}")
for profile_name, stats in profile_stats.items():
    if stats['new'] > 0:
        print(f"  {profile_name}: {stats['new']} new")
