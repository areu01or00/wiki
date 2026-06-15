import json, os
from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc).strftime('%Y-%m-%d')

with open('temp/watch_run_1781484417.json') as f:
    batch = json.load(f)

new_results = batch['new_results']
new_hashes = batch['new_hashes']

# Profile to wiki page mapping
profile_to_page = {
    'system-design': 'entities/system-design.md',
    'compilers': 'entities/compilers.md',
    'type-systems': 'entities/type-systems.md',
    'functional-programming': 'entities/functional-programming.md',
    'algorithms': 'entities/algorithms.md',
    'python-internals': 'entities/python-internals.md',
}

# Keyword extraction helper
def extract_keyword(title):
    # Extract a meaningful keyword from the title
    words = title.split()
    # Return first meaningful word
    for w in words:
        w_clean = w.strip('[]()')
        if len(w_clean) > 3 and w_clean[0].isupper():
            return w_clean
    return words[0] if words else 'update'

# Update each wiki page
for profile_name, results in new_results.items():
    if not results:
        continue
    
    page_path = profile_to_page[profile_name]
    with open(page_path, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find the ## Updates line and insert after it
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is None:
        print(f"WARNING: No ## Updates section found in {page_path}")
        continue
    
    # Build new entries
    new_entries = []
    for r in results:
        kw = extract_keyword(r['title'])
        entry = f"- **{utc_now}** | [{r['title']}]({r['url']}) | kw: {kw}"
        new_entries.append(entry)
    
    # Insert entries
    lines = lines[:insert_after] + new_entries + [''] + lines[insert_after:]
    
    with open(page_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Updated {page_path} with {len(new_entries)} entries")

# Update watch_profiles.json
with open('watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)

for profile_name, hashes in new_hashes.items():
    existing = profiles_data['profiles'][profile_name]['last_result_hashes']
    existing.extend(hashes)
    # Keep only last 20
    profiles_data['profiles'][profile_name]['last_result_hashes'] = existing[-20:]
    profiles_data['profiles'][profile_name]['last_run'] = f"{batch['timestamp']}"

profiles_data['last_run'] = f"{batch['timestamp']}"

with open('watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)

print(f"Updated watch_profiles.json - all {len(new_hashes)} profiles updated")
