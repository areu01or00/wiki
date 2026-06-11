import json, hashlib, os, sys
from datetime import datetime, timezone

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# Load batch results
all_results = {}
for bf in ['/home/hermes/wiki/temp/watch_run_1781166652_batch1.json', '/home/hermes/wiki/temp/watch_run_1781166652_batch2.json']:
    with open(bf, 'r') as f:
        batch = json.load(f)
        for profile_name, results in batch['results'].items():
            all_results[profile_name] = results

# Compute hashes and find new ones
new_results = {}
sub_topics_found = set()
today = datetime.now(timezone.utc).strftime('%Y-%m-%d')

for profile_name, results in all_results.items():
    existing_hashes = set(profiles[profile_name]['last_result_hashes'])
    new_results[profile_name] = []
    
    for r in results:
        h = hashlib.md5(f"{r['title']}{r['url']}".encode('utf-8', errors='replace')).hexdigest()
        if h not in existing_hashes:
            new_results[profile_name].append({
                'title': r['title'],
                'url': r['url'],
                'description': r.get('description', ''),
                'hash': h
            })
            text = (r.get('title', '') + ' ' + r.get('description', '')).lower()
            for topic in profiles[profile_name]['sub_topics']:
                if topic.lower() in text:
                    sub_topics_found.add(topic)

# Print summary
for profile_name, new in new_results.items():
    print(f"\n=== {profile_name} ===")
    print(f"  New results: {len(new)}")
    for r in new:
        print(f"  - [{r['title']}]({r['url']})")
        print(f"    Hash: {r['hash']}")

print(f"\n=== Sub-topics found: {sub_topics_found}")

# Save
with open('/home/hermes/wiki/temp/new_results.json', 'w') as f:
    json.dump(new_results, f, indent=2)
