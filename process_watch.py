#!/usr/bin/env python3
"""Wiki watch processor: dedup, aggregate, update wiki, save profiles, push."""
import json
import hashlib
import os
import re
import subprocess
from datetime import datetime, timezone
from collections import defaultdict, OrderedDict

WIKI_DIR = '/home/hermes/wiki'
ENTITIES_DIR = os.path.join(WIKI_DIR, 'entities')
TEMP_DIR = os.path.join(WIKI_DIR, 'temp')
PROFILES_PATH = os.path.join(WIKI_DIR, 'watch_profiles.json')

# Load batch results
all_results = {}  # profile_name -> [results]
for batch_n in (1, 2):
    p = os.path.join(TEMP_DIR, f'watch_run_batch{batch_n}.json')
    with open(p) as f:
        data = json.load(f)
    for prof_name, results in data['profiles'].items():
        all_results.setdefault(prof_name, []).extend(results)

print(f"Loaded {sum(len(v) for v in all_results.values())} total results across {len(all_results)} profiles")

# Load profiles
with open(PROFILES_PATH) as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# Compute hashes & find new entries per profile
new_entries_by_profile = {}  # profile_name -> [result dicts]
seen_hashes_by_profile = {}  # profile_name -> set of all hashes known (last + new)

for name, prof in profiles.items():
    results = all_results.get(name, [])
    last_hashes = set(prof.get('last_result_hashes', []))
    new_results = []
    seen = set(last_hashes)
    for r in results:
        title = r.get('title', '')
        url = r.get('url', '')
        h = hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()
        if h not in seen:
            seen.add(h)
            new_results.append({'title': title, 'url': url, 'description': r.get('description', ''), 'hash': h})
    new_entries_by_profile[name] = new_results
    seen_hashes_by_profile[name] = seen

for name, prof in profiles.items():
    new_results = new_entries_by_profile[name]
    print(f"  {name}: {len(new_results)} new (of {len(all_results.get(name, []))} returned)")

# Aggregate by wiki_page
entries_by_page = defaultdict(list)  # wiki_page -> [(profile_name, [result])]
for name, prof in profiles.items():
    page = prof.get('wiki_page')
    if page and new_entries_by_profile.get(name):
        entries_by_page[page].append((name, new_entries_by_profile[name]))

# Save timestamp
now = datetime.now(timezone.utc)
date_str = now.strftime('%Y-%m-%d')
datetime_str = now.strftime('%Y-%m-%d %H:%M UTC')

# Update wiki pages
print("\n--- Updating wiki pages ---")
for page, profile_bundles in entries_by_page.items():
    # Flatten all new entries across profiles targeting same page, dedup by hash
    flat = []
    seen_h = set()
    for prof_name, results in profile_bundles:
        for r in results:
            if r['hash'] not in seen_h:
                seen_h.add(r['hash'])
                flat.append((prof_name, r))
    if not flat:
        continue
    fp = os.path.join(ENTITIES_DIR, page)
    with open(fp, 'r') as f:
        content = f.read()
    lines = content.split('\n')
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_idx = i + 1
            break
    if insert_idx is None:
        print(f"  WARNING: no ## Updates header in {page}, skipping")
        continue
    # Build new entries - extract a 1-2 word keyword from title
    new_lines = []
    for prof_name, r in flat:
        title = r['title']
        url = r['url']
        # Try to extract a keyword - use first meaningful 2-3 word phrase
        kw = title[:60].strip()
        new_lines.append(f"- **{date_str}** | [{title}]({url}) | kw: {kw}")
    # Insert after ## Updates
    lines = lines[:insert_idx] + new_lines + [''] + lines[insert_idx:]
    new_content = '\n'.join(lines)
    with open(fp, 'w') as f:
        f.write(new_content)
    print(f"  Updated {page}: +{len(new_lines)} entries")

# Update watch_profiles.json
print("\n--- Updating watch_profiles.json ---")
for name, prof in profiles.items():
    seen = list(seen_hashes_by_profile[name])
    # Keep last 20
    prof['last_result_hashes'] = seen[-20:]
    prof['last_run'] = now.isoformat()
    # Discover new sub-topics from new entries
    new_results = new_entries_by_profile.get(name, [])
    existing_sub_topics = set(prof.get('sub_topics', []))
    new_sub_topics = []
    for r in new_results:
        # Heuristic: extract first meaningful capitalized phrase as potential sub-topic
        title = r['title']
        # Use first 5 words as candidate
        words = re.findall(r"[A-Za-z][A-Za-z0-9'-]+", title)
        if not words:
            continue
        candidate = ' '.join(words[:5])
        # Compare case-insensitively to existing
        if not any(candidate.lower() == s.lower() for s in existing_sub_topics):
            new_sub_topics.append(candidate)
            existing_sub_topics.add(candidate)
    if new_sub_topics:
        prof.setdefault('new_sub_topics_this_run', [])
        prof['new_sub_topics_this_run'].extend(new_sub_topics)
        prof['last_new_count'] = len(new_sub_topics)
    # Add new result titles to sub_topics list
    for r in new_results:
        for w in re.findall(r"[A-Za-z][A-Za-z0-9'-]+", r['title']):
            if w.lower() not in {s.lower() for s in prof.get('sub_topics', [])}:
                prof.setdefault('sub_topics', []).append(w)

# Write profiles
with open(PROFILES_PATH, 'w') as f:
    json.dump(profiles_data, f, indent=2, ensure_ascii=False)
print("  profiles written")

# Write a final combined result file for traceability
combined = {
    'timestamp': now.isoformat(),
    'profiles': {
        name: {
            'wiki_page': profiles[name].get('wiki_page'),
            'returned': len(all_results.get(name, [])),
            'new': len(new_entries_by_profile.get(name, [])),
            'new_entries': [
                {'title': r['title'], 'url': r['url'], 'hash': r['hash']}
                for r in new_entries_by_profile.get(name, [])
            ],
            'new_sub_topics': profiles[name].get('new_sub_topics_this_run', []),
        }
        for name in profiles
    }
}
combined_path = os.path.join(TEMP_DIR, 'watch_run_final.json')
with open(combined_path, 'w') as f:
    json.dump(combined, f, indent=2, ensure_ascii=False)
print(f"  final result file: {combined_path}")

# Build digest
total_profiles = len(profiles)
total_new = sum(len(new_entries_by_profile.get(n, [])) for n in profiles)
total_subtopics = sum(len(profiles[n].get('new_sub_topics_this_run', [])) for n in profiles)
print(f"\nTotal: {total_profiles} profiles, {total_new} new entries, {total_subtopics} new sub-topics")

# Git push
print("\n--- Git push ---")
try:
    subprocess.run(['git', 'add', '-A'], cwd=WIKI_DIR, check=True)
    commit_msg = f"{datetime_str} Wiki watch update"
    subprocess.run(['git', 'commit', '-m', commit_msg], cwd=WIKI_DIR, check=True)
    subprocess.run(['git', 'push', 'origin', 'main'], cwd=WIKI_DIR, check=True)
    print("  git push OK")
except subprocess.CalledProcessError as e:
    print(f"  git error: {e}")
    # Try master
    try:
        subprocess.run(['git', 'push', 'origin', 'master'], cwd=WIKI_DIR, check=True)
        print("  git push master OK")
    except subprocess.CalledProcessError as e2:
        print(f"  git push master also failed: {e2}")
