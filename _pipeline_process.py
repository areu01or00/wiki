import json
import hashlib
import os

# Load all batch results
all_results = {}
for fname in ['watch_run_20260624_011619_batch1.json', 'watch_run_20260624_011619_batch2.json']:
    path = f'/home/hermes/wiki/temp/{fname}'
    with open(path) as f:
        batch = json.load(f)
    for profile, results in batch['results'].items():
        all_results.setdefault(profile, []).extend(results)

# Load watch profiles
with open('/home/hermes/wiki/watch_profiles.json') as f:
    profiles_data = json.load(f)

# Compute hashes and dedup
processed = {}
for profile, results in all_results.items():
    prof = profiles_data['profiles'][profile]
    existing_hashes = set(prof.get('last_result_hashes', []))
    new_entries = []
    for r in results:
        if not r.get('url') or r['url'].startswith('/clev?'):
            continue  # skip malformed
        h = hashlib.md5(f"{r['title']}{r['url']}".encode('utf-8', errors='replace')).hexdigest()
        if h in existing_hashes:
            continue
        new_entries.append({
            'hash': h,
            'title': r['title'],
            'url': r['url'],
            'description': r.get('description', ''),
            'keyword': r['title'][:50] if r['title'] else 'unknown'
        })
    processed[profile] = new_entries

# Save processed
with open('/home/hermes/wiki/temp/processed_results.json', 'w') as f:
    json.dump(processed, f, indent=2)

# Print summary
for profile, entries in processed.items():
    print(f"\n=== {profile} ({len(entries)} new) ===")
    for e in entries[:5]:
        print(f"  - {e['title'][:60]}...")
    if len(entries) > 5:
        print(f"  ... +{len(entries)-5} more")

# Group by wiki page
by_page = {}
for profile, entries in processed.items():
    page = profiles_data['profiles'][profile]['wiki_page']
    by_page.setdefault(page, []).extend([(profile, e) for e in entries])

print("\n=== By Wiki Page ===")
for page, entries in by_page.items():
    print(f"\n{page}: {len(entries)} new entries")
    profiles_for_page = set(p for p, _ in entries)
    print(f"  from profiles: {profiles_for_page}")
