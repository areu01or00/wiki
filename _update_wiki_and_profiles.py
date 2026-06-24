import json
import hashlib
from datetime import datetime, timezone

# Load processed results
with open('/home/hermes/wiki/temp/processed_results.json') as f:
    processed = json.load(f)

with open('/home/hermes/wiki/watch_profiles.json') as f:
    profiles_data = json.load(f)

today = datetime.now(timezone.utc).strftime('%Y-%m-%d')

# === Update wiki pages ===
# Group by wiki page
by_page = {}
for profile, entries in processed.items():
    page = profiles_data['profiles'][profile]['wiki_page']
    by_page.setdefault(page, []).extend(entries)

WIKI_DIR = '/home/hermes/wiki/entities'

for page, entries in by_page.items():
    path = f'{WIKI_DIR}/{page}'
    with open(path) as f:
        content = f.read()
    lines = content.split('\n')
    
    # Build new entries (markdown list items)
    new_entries_md = []
    for e in entries:
        kw = e['keyword'].replace('|', '\\|')
        line = f"- **{today}** | [{e['title']}]({e['url']}) | kw: {kw}"
        new_entries_md.append(line)
    
    # Find FIRST ## Updates and insert after it
    inserted = False
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            # Skip existing blank lines at the top of updates
            while insert_after < len(lines) and lines[insert_after].strip() == '':
                insert_after += 1
            # If there are existing entries right after, just prepend; we'll insert before them
            # Actually: insert AFTER the heading itself (i+1) with a blank line separator
            lines = lines[:i+1] + new_entries_md + [''] + lines[i+1:]
            inserted = True
            break
    
    if not inserted:
        print(f"WARN: {page} has no '## Updates' header - appending at top after title")
        # Find the first heading and insert after
        for i, line in enumerate(lines):
            if line.startswith('# '):
                lines = lines[:i+1] + ['', '## Updates', ''] + new_entries_md + [''] + lines[i+1:]
                break
    
    new_content = '\n'.join(lines)
    with open(path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {page}: added {len(entries)} entries")

# === Update watch_profiles.json ===
new_hashes_by_profile = {}
for profile, entries in processed.items():
    new_hashes_by_profile[profile] = [e['hash'] for e in entries]

now_iso = datetime.now(timezone.utc).isoformat()
for profile, entries in processed.items():
    prof = profiles_data['profiles'][profile]
    existing = list(prof.get('last_result_hashes', []))
    new_hashes = new_hashes_by_profile[profile]
    combined = (existing + new_hashes)[-20:]  # keep last 20
    prof['last_result_hashes'] = combined
    prof['last_run'] = now_iso
    prof['last_new_count'] = len(new_hashes)
    prof['_new_total_for_digest'] = len(new_hashes)
    
    # Sub-topic discovery: extract new keywords from titles
    new_subs = set(prof.get('new_sub_topics_this_run', []))
    for e in entries:
        for token in e['title'].lower().split():
            token_clean = token.strip('.,()[]"\'/:-')
            if len(token_clean) > 3 and not token_clean[0].isdigit():
                new_subs.add(token_clean)
    prof['new_sub_topics_this_run'] = list(new_subs)[-20:]

# Update top-level last_run
profiles_data['last_run'] = now_iso

with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)

print("\nUpdated watch_profiles.json")
print(f"Total new entries: {sum(len(v) for v in processed.values())}")
