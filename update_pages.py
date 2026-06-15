import json, hashlib, os, subprocess
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
timestamp = now.strftime('%Y-%m-%d %H:%M UTC')
date_str = now.strftime('%Y-%m-%d')

# Load intermediate data
with open('/tmp/wiki_watch_data.json', 'r') as f:
    data = json.load(f)

new_results = data['new_results']
sub_topic_discoveries = data['sub_topic_discoveries']

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

def md5_hash(title, url):
    return hashlib.md5((title + url).encode('utf-8', errors='replace')).hexdigest()

# Group results by wiki_page (multiple profiles can share same page)
page_entries = {}  # wiki_page -> list of (profile_name, entries)
for profile_name, results in new_results.items():
    if not results:
        continue
    wiki_page = profiles[profile_name]['wiki_page']
    if wiki_page not in page_entries:
        page_entries[wiki_page] = []
    entries = []
    for r in results:
        title = r['title']
        url = r['url']
        # Extract a keyword from title
        keyword = profile_name.replace('-', ' ')
        entry = f"- **{date_str}** | [{title}]({url}) | kw: {keyword}"
        entries.append(entry)
    page_entries[wiki_page].append((profile_name, entries))

# Update wiki pages using Python I/O
for wiki_page, profile_entries in page_entries.items():
    filepath = f'/home/hermes/wiki/entities/{wiki_page}'
    if not os.path.exists(filepath):
        # Create minimal file
        with open(filepath, 'w') as f:
            f.write(f'# {wiki_page.replace(".md", "").replace("-", " ").title()}\n\n## Updates\n\n')
    
    with open(filepath, 'r') as f:
        content = f.read()
    lines = content.split('\n')
    
    # Find FIRST ## Updates and insert after it
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is None:
        # Add ## Updates at the top after title
        insert_after = 2
        lines.insert(insert_after, '## Updates')
        insert_after += 1
    
    # Collect all new entries for this page
    new_entries = []
    for profile_name, entries in profile_entries:
        new_entries.extend(entries)
    
    # Insert after ## Updates line
    lines = lines[:insert_after] + new_entries + [''] + lines[insert_after:]
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f'Updated {wiki_page} with {len(new_entries)} entries')

# Update watch_profiles.json
for profile_name, results in new_results.items():
    if not results:
        continue
    # Append new hashes (max 20)
    new_hashes = [r['hash'] for r in results]
    existing = profiles[profile_name]['last_result_hashes']
    existing.extend(new_hashes)
    # Keep only last 20
    profiles[profile_name]['last_result_hashes'] = existing[-20:]
    
    # Add new sub-topics
    if profile_name in sub_topic_discoveries:
        for st in sub_topic_discoveries[profile_name]:
            if st not in profiles[profile_name].get('sub_topics', []):
                profiles[profile_name].setdefault('sub_topics', []).append(st)
    
    profiles[profile_name]['last_run'] = timestamp

profiles_data['profiles'] = profiles
profiles_data['last_run'] = timestamp

with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2, ensure_ascii=False)

print(f'Updated watch_profiles.json')

# Git push
os.chdir('/home/hermes/wiki')
result = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True)
print(f'git add: {result.stdout} {result.stderr}')

commit_msg = f'{timestamp} Wiki watch update'
result = subprocess.run(['git', 'commit', '-m', commit_msg], capture_output=True, text=True)
print(f'git commit: {result.stdout} {result.stderr}')

result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print(f'git push: {result.stdout} {result.stderr}')

# Prepare Discord digest
total_new = sum(len(r) for r in new_results.values())
discord_msg = f'## \U0001f504 Wiki Watch Digest \u2014 {timestamp}\n'
discord_msg += f'Checked: {len(new_results)} profiles\n'

for profile_name, results in new_results.items():
    if not results:
        continue
    topic_name = profile_name.replace('-', ' ').title()
    discord_msg += f'### {topic_name}\n'
    discord_msg += f'New: {len(results)} results\n'
    for r in results[:5]:  # Show max 5 per topic
        discord_msg += f'- [{r["title"][:60]}...]({r["url"]})\n'
    if len(results) > 5:
        discord_msg += f'- ...and {len(results) - 5} more\n'
    # Add discovered sub-topics
    if profile_name in sub_topic_discoveries and sub_topic_discoveries[profile_name]:
        topics_list = ', '.join(sub_topic_discoveries[profile_name][:5])
        discord_msg += f'Added sub-topics: {topics_list}\n'
    discord_msg += '---\n'

with open('/tmp/discord_digest.txt', 'w') as f:
    f.write(discord_msg)

print(f'\nDiscord digest saved to /tmp/discord_digest.txt')
print(f'Total new results: {total_new}')
