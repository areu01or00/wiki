import json

with open('/tmp/wiki_watch_data.json') as f:
    data = json.load(f)

wiki_updates = data['wiki_updates']
new_hashes = data['new_hashes']
profiles = data['profiles']

# Step 5: Update wiki pages
wiki_dir = '/home/hermes/wiki/entities'

for wiki_page, entries in wiki_updates.items():
    filepath = f'{wiki_dir}/{wiki_page}'
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        lines = content.split('\n')
        
        # Find FIRST ## Updates and insert after it
        insert_after = None
        for i, line in enumerate(lines):
            if line.strip() == '## Updates':
                insert_after = i + 1
                break
        
        if insert_after is not None:
            new_block = entries + ['']
            lines = lines[:insert_after] + new_block + lines[insert_after:]
            with open(filepath, 'w') as f:
                f.write('\n'.join(lines))
            print(f"Updated {wiki_page}: {len(entries)} entries")
        else:
            print(f"WARNING: No '## Updates' found in {wiki_page}")
    except FileNotFoundError:
        print(f"WARNING: File not found: {filepath}")

# Step 6: Update watch_profiles.json
import datetime
timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

for profile_name, hashes in new_hashes.items():
    if not hashes:
        continue
    old = profiles[profile_name]['last_result_hashes']
    combined = old + hashes
    profiles[profile_name]['last_result_hashes'] = combined[-20:]  # max 20
    profiles[profile_name]['last_run'] = timestamp
    print(f"Updated profile {profile_name}: {len(hashes)} new hashes")

with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump({"profiles": profiles}, f, indent=2)

print("\nwatch_profiles.json updated")
