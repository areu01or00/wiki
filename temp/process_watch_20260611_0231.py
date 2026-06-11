#!/usr/bin/env python3
"""Process wiki watch batch results: dedup, update wiki pages, update watch_profiles."""
import hashlib
import json
import re
import os
from datetime import datetime, timezone
from pathlib import Path

WIKI_DIR = Path('/home/hermes/programming-wisdom/wiki')
ENTITIES_DIR = WIKI_DIR / 'entities'
PROFILES_PATH = Path('/home/hermes/programming-wisdom/watch_profiles.json')
BATCH_FILE = Path('/home/hermes/wiki/temp/watch_run_20260611_023138.json')
TEMP_DIR = Path('/home/hermes/wiki/temp')

NOW = datetime.now(timezone.utc)
TODAY = NOW.strftime('%Y-%m-%d')
NOW_ISO = NOW.isoformat()

def compute_hash(title, url):
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

def load_profiles():
    with open(PROFILES_PATH, 'r') as f:
        return json.load(f)

def load_existing_urls_from_page(page_path):
    """Safety layer: extract URLs that already exist in a wiki page."""
    urls = set()
    if not page_path.exists():
        return urls
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find all markdown links [text](url)
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        urls.add(match.group(2))
    return urls

def find_existing_hashes_in_page(page_path):
    """Try to extract existing entry titles for additional dedup safety."""
    titles = set()
    if not page_path.exists():
        return titles
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        titles.add(match.group(1).strip().lower())
    return titles

def insert_entries_in_wiki(page_path, new_entries):
    """Insert new entries after the first '## Updates' heading."""
    if not new_entries:
        return False
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    if insert_after is None:
        print(f"  WARNING: No '## Updates' heading in {page_path}")
        return False
    # Find the first non-blank line after the heading (i.e., first existing entry)
    first_existing = insert_after
    while first_existing < len(lines) and lines[first_existing].strip() == '':
        first_existing += 1
    # Insert new entries before the first existing entry, separated by a blank line
    new_block = new_entries + ['']
    lines = lines[:first_existing] + new_block + lines[first_existing:]
    new_content = '\n'.join(lines)
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

def main():
    # Load batch results
    with open(BATCH_FILE, 'r') as f:
        batch = json.load(f)

    profiles_data = load_profiles()
    profiles = profiles_data['profiles']

    # Flatten all results: (profile_name, wiki_page, result)
    all_results = []
    for batch_name, batch_data in batch['batches'].items():
        for profile_name, results in batch_data.items():
            for r in results:
                all_results.append((profile_name, results))

    # Process each profile
    new_hash_updates = {}  # profile_name -> list of new hashes
    wiki_page_updates = {}  # wiki_page -> list of new entries (with profile marker)

    for profile_name, results in all_results:
        profile = profiles[profile_name]
        wiki_page_path = ENTITIES_DIR / Path(profile['wiki_page']).name
        existing_hashes = set(profile.get('last_result_hashes', []))
        existing_urls = load_existing_urls_from_page(wiki_page_path)
        existing_titles = find_existing_hashes_in_page(wiki_page_path)

        new_hashes_for_profile = []
        new_entries_for_page = []

        for r in results:
            title = r['title']
            url = r['url']
            h = compute_hash(title, url)
            # Dedup checks: hash list, URL already in page, title already in page
            if h in existing_hashes:
                continue
            if url in existing_urls:
                continue
            if title.strip().lower() in existing_titles:
                continue
            new_hashes_for_profile.append(h)
            entry = f"- **{TODAY}** | [{title}]({url}) | kw: {profile_name}"
            new_entries_for_page.append((entry, h))
            existing_hashes.add(h)
            existing_urls.add(url)
            existing_titles.add(title.strip().lower())

        new_hash_updates[profile_name] = new_hashes_for_profile
        if profile['wiki_page'] not in wiki_page_updates:
            wiki_page_updates[profile['wiki_page']] = []
        wiki_page_updates[profile['wiki_page']].extend(new_entries_for_page)
        print(f"[{profile_name}] {len(new_entries_for_page)} new entries (from {len(results)} results)")

    # Aggregate: wiki page path -> list of entry strings (deduped by hash)
    aggregated = {}
    for page, entries_with_hash in wiki_page_updates.items():
        seen_hashes = set()
        unique_entries = []
        for entry, h in entries_with_hash:
            if h not in seen_hashes:
                unique_entries.append(entry)
                seen_hashes.add(h)
        aggregated[page] = unique_entries

    # Write to wiki pages
    for page_rel, entries in aggregated.items():
        page_path = ENTITIES_DIR / Path(page_rel).name
        if not page_path.exists():
            print(f"  ERROR: Page not found: {page_path}")
            continue
        if insert_entries_in_wiki(page_path, entries):
            print(f"  Wrote {len(entries)} entries to {page_path.name}")

    # Update watch_profiles.json
    for profile_name, new_hashes in new_hash_updates.items():
        profile = profiles[profile_name]
        old_hashes = profile.get('last_result_hashes', [])
        combined = old_hashes + new_hashes
        # Keep most recent 20
        profile['last_result_hashes'] = combined[-20:]
        profile['last_run'] = NOW_ISO
    profiles_data['last_run'] = NOW_ISO
    profiles_data['last_updated'] = NOW_ISO

    with open(PROFILES_PATH, 'w') as f:
        json.dump(profiles_data, f, indent=2)
    print(f"Updated watch_profiles.json")

    # Write digest data
    total_new = sum(len(v) for v in aggregated.values())
    digest_data = {
        'timestamp': NOW_ISO,
        'profiles_checked': len(profiles),
        'total_new': total_new,
        'by_topic': {}
    }
    for profile_name, new_hashes in new_hash_updates.items():
        # Get the actual entries for this profile
        profile = profiles[profile_name]
        page = profile['wiki_page']
        entries = aggregated.get(page, [])
        # Filter to entries with this profile's kw
        profile_entries = [e for e in entries if f"kw: {profile_name}" in e]
        digest_data['by_topic'][profile_name] = {
            'new_count': len(new_hashes),
            'entries': profile_entries,
            'wiki_page': page
        }

    digest_file = TEMP_DIR / f"digest_data_{NOW.strftime('%Y-%m-%d_%H-%M')}.json"
    with open(digest_file, 'w') as f:
        json.dump(digest_data, f, indent=2)
    print(f"Wrote digest: {digest_file}")
    print(f"Total new entries: {total_new}")
    return digest_data

if __name__ == '__main__':
    main()
