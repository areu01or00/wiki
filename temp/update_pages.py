import json, os
from datetime import datetime, timezone

with open('/home/hermes/wiki/temp/new_results.json', 'r') as f:
    new_results = json.load(f)

with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

today = datetime.now(timezone.utc).strftime('%Y-%m-%d')

# Group by wiki_page
wiki_updates = {}  # wiki_page -> list of entry lines
all_new_hashes = {}  # profile_name -> list of new hashes

for profile_name, results in new_results.items():
    wiki_page = profiles[profile_name]['wiki_page']
    page_path = f'/home/hermes/wiki/entities/{wiki_page}'
    
    if wiki_page not in wiki_updates:
        wiki_updates[wiki_page] = []
    all_new_hashes[profile_name] = []
    
    for r in results:
        title_escaped = r['title'].replace('[', '\\[').replace(']', '\\]')
        entry = f"- **{today}** | [{title_escaped}]({r['url']}) | kw: {profile_name}"
        wiki_updates[wiki_page].append(entry)
        all_new_hashes[profile_name].append(r['hash'])

# Update each wiki page
for wiki_page, entries in wiki_updates.items():
    page_path = f'/home/hermes/wiki/entities/{wiki_page}'
    
    if os.path.exists(page_path):
        with open(page_path, 'r') as f:
            content = f.read()
        lines = content.split('\n')
        
        # Find first ## Updates and insert after it
        insert_after = None
        for i, line in enumerate(lines):
            if line.strip() == '## Updates':
                insert_after = i + 1
                break
        
        if insert_after is not None:
            lines = lines[:insert_after] + entries + [''] + lines[insert_after:]
        else:
            # If no ## Updates section, append at end
            lines = lines + ['', '## Updates'] + entries + ['']
        
        with open(page_path, 'w') as f:
            f.write('\n'.join(lines))
        print(f"Updated {wiki_page}: {len(entries)} entries")
    else:
        print(f"WARNING: {page_path} not found, skipping")

# Update watch_profiles.json
for profile_name, hashes in all_new_hashes.items():
    existing = profiles[profile_name]['last_result_hashes']
    existing.extend(hashes)
    # Keep max 20
    profiles[profile_name]['last_result_hashes'] = existing[-20:]
    profiles[profile_name]['last_run'] = datetime.now(timezone.utc).isoformat()

profiles_data['profiles'] = profiles
with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)
print("Updated watch_profiles.json")

# Build digest
total_new = sum(len(v) for v in wiki_updates.values())
print(f"\nDIGEST_DATA:{total_new}")
for profile_name in profiles:
    new_count = len(all_new_hashes.get(profile_name, []))
    print(f"PROFILE:{profile_name}:{new_count}")
