import json, hashlib, os, glob
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
now_str = now.strftime('%Y-%m-%d_%H-%M')
today = now.strftime('%Y-%m-%d')

# Load processing state
with open('/home/hermes/wiki/temp/processing_state.json', 'r') as f:
    state = json.load(f)

profiles_data = state['profiles_data']['profiles']

# Find latest batch files by modification time
all_batch_files = glob.glob('/home/hermes/wiki/temp/watch_run_*_batch*.json')
# Sort by mtime descending
all_batch_files.sort(key=lambda f: os.path.getmtime(f), reverse=True)

latest_batch1 = None
latest_batch2 = None
for f in all_batch_files:
    basename = os.path.basename(f)
    if 'batch1' in basename and latest_batch1 is None:
        latest_batch1 = f
    elif 'batch2' in basename and latest_batch2 is None:
        latest_batch2 = f
    if latest_batch1 and latest_batch2:
        break

print(f"Using batch1: {latest_batch1}")
print(f"Using batch2: {latest_batch2}")

batch_files_to_load = [f for f in [latest_batch1, latest_batch2] if f]

# Collect all results
all_results = {}  # profile -> list of {title, url, hash}
for bf in batch_files_to_load:
    with open(bf, 'r') as f:
        batch = json.load(f)
    for profile, results in batch['results'].items():
        if profile not in all_results:
            all_results[profile] = []
        all_results[profile].extend(results)

print(f"Loaded results for {len(all_results)} profiles")

# Deduplicate: compare against last_result_hashes
new_results = {}  # profile -> list of new results
total_new = 0
total_checked = 0

for profile, results in all_results.items():
    if profile not in profiles_data:
        print(f"  WARNING: Profile '{profile}' not found in profiles_data, skipping")
        continue
    
    existing_hashes = set(profiles_data[profile].get('last_result_hashes', []))
    new_results[profile] = []
    
    for r in results:
        total_checked += 1
        if r['hash'] not in existing_hashes:
            new_results[profile].append(r)
            total_new += 1
    
    print(f"  {profile}: {len(results)} checked, {len(new_results[profile])} new")

print(f"\nTotal: {total_checked} checked, {total_new} new")

# Group by wiki page
wiki_page_entries = {}  # wiki_page -> list of entry strings
new_hashes_by_profile = {}  # profile -> list of new hashes

for profile, results in new_results.items():
    if not results:
        continue
    
    wiki_page = profiles_data[profile]['wiki_page']
    if wiki_page not in wiki_page_entries:
        wiki_page_entries[wiki_page] = []
    
    if profile not in new_hashes_by_profile:
        new_hashes_by_profile[profile] = []
    
    for r in results:
        # Extract keywords from title
        title_words = r['title'].lower().replace('|', '').replace('[', '').replace(']', '').split()
        keywords = [w for w in title_words if len(w) > 3][:3]
        kw_str = ', '.join(keywords) if keywords else profile
        
        entry = f"- **{today}** | [{r['title']}]({r['url']}) | kw: {kw_str}"
        wiki_page_entries[wiki_page].append(entry)
        new_hashes_by_profile[profile].append(r['hash'])

print(f"\nWiki pages to update: {len(wiki_page_entries)}")
for page, entries in wiki_page_entries.items():
    print(f"  {page}: {len(entries)} entries")

# Update wiki pages using Python I/O
for wiki_page, entries in wiki_page_entries.items():
    filepath = f'/home/hermes/wiki/{wiki_page}'
    if not os.path.exists(filepath):
        print(f"  WARNING: {filepath} does not exist, creating it")
        with open(filepath, 'w') as f:
            f.write(f"# {wiki_page.split('/')[-1].replace('.md', '').replace('-', ' ').title()}\n\n## Updates\n")
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find first ## Updates line
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is None:
        # Add ## Updates section at the end
        lines.append('')
        lines.append('## Updates')
        insert_after = len(lines)
    
    # Insert new entries
    new_lines = lines[:insert_after] + entries + [''] + lines[insert_after:]
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(new_lines))
    
    print(f"  Updated {wiki_page} with {len(entries)} entries")

# Update processing_state.json
for profile, hashes in new_hashes_by_profile.items():
    if profile not in profiles_data:
        continue
    existing = profiles_data[profile].get('last_result_hashes', [])
    existing.extend(hashes)
    # Keep only last 20
    profiles_data[profile]['last_result_hashes'] = existing[-20:]
    profiles_data[profile]['last_run'] = now.isoformat()

state['profiles_data']['profiles'] = profiles_data
state['profiles_data']['last_run'] = now.isoformat()
state['profiles_data']['last_updated'] = now.isoformat()

with open('/home/hermes/wiki/temp/processing_state.json', 'w') as f:
    json.dump(state, f, indent=2)

print("\nUpdated processing_state.json")

# Save digest data
digest_data = {
    'new_entries_by_wiki_page': wiki_page_entries,
    'new_hashes_by_profile': new_hashes_by_profile,
    'total_checked': total_checked,
    'total_new': total_new,
    'profiles_checked': list(all_results.keys()),
    'timestamp': now_str
}

with open('/home/hermes/wiki/temp/digest_data.json', 'w') as f:
    json.dump(digest_data, f, indent=2)

print(f"Saved digest_data.json")
print(f"\n=== SUMMARY ===")
print(f"Profiles checked: {len(all_results)}")
print(f"Total results checked: {total_checked}")
print(f"New results found: {total_new}")
for profile, entries in new_results.items():
    if entries:
        print(f"  {profile}: {len(entries)} new")
