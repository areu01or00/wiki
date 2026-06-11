#!/usr/bin/env python3
"""Full pipeline: merge batches, dedup, update wiki pages, update profiles, create digest."""
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

WIKI_DIR = Path('/home/hermes/programming-wisdom')
ENTITIES_DIR = WIKI_DIR / 'wiki' / 'entities'
PROFILES_PATH = WIKI_DIR / 'watch_profiles.json'
BATCH_FILES = [
    Path('/home/hermes/wiki/temp/watch_run_2026-06-11_06-30_batch1.json'),
    Path('/home/hermes/wiki/temp/watch_run_2026-06-11_06-30_batch2.json'),
]

NOW = datetime.now(timezone.utc)
TODAY = NOW.strftime('%Y-%m-%d')
NOW_ISO = NOW.isoformat()

def compute_hash(title, url):
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

def load_profiles():
    with open(PROFILES_PATH, 'r') as f:
        return json.load(f)

def load_existing_urls_from_page(page_path):
    urls = set()
    if not page_path.exists():
        return urls
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        urls.add(match.group(2))
    return urls

def find_existing_titles_in_page(page_path):
    titles = set()
    if not page_path.exists():
        return titles
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        titles.add(match.group(1).strip().lower())
    return titles

def insert_entries_in_wiki(page_path, new_entries):
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
    first_existing = insert_after
    while first_existing < len(lines) and lines[first_existing].strip() == '':
        first_existing += 1
    new_block = new_entries + ['']
    lines = lines[:first_existing] + new_block + lines[first_existing:]
    new_content = '\n'.join(lines)
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

def main():
    # Load and merge batch results
    all_results_by_profile = {}
    for batch_file in BATCH_FILES:
        with open(batch_file, 'r') as f:
            batch = json.load(f)
        for profile_name, results in batch['profiles'].items():
            if profile_name not in all_results_by_profile:
                all_results_by_profile[profile_name] = []
            all_results_by_profile[profile_name].extend(results)

    profiles_data = load_profiles()
    profiles = profiles_data['profiles']

    new_hash_updates = {}
    wiki_page_entries = {}  # wiki_page -> list of (entry_string, hash)

    for profile_name, results in all_results_by_profile.items():
        if profile_name not in profiles:
            print(f"  WARNING: Unknown profile {profile_name}, skipping")
            continue
        profile = profiles[profile_name]
        wiki_page_path = ENTITIES_DIR / Path(profile['wiki_page']).name
        existing_hashes = set(profile.get('last_result_hashes', []))
        existing_urls = load_existing_urls_from_page(wiki_page_path)
        existing_titles = find_existing_titles_in_page(wiki_page_path)

        new_hashes_for_profile = []
        new_entries_for_page = []

        for r in results:
            title = r['title']
            url = r['url']
            h = r.get('hash') or compute_hash(title, url)
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
        if profile['wiki_page'] not in wiki_page_entries:
            wiki_page_entries[profile['wiki_page']] = []
        wiki_page_entries[profile['wiki_page']].extend(new_entries_for_page)
        print(f"[{profile_name}] {len(new_entries_for_page)} new entries (from {len(results)} results)")

    # Aggregate by wiki page (dedup by hash)
    aggregated = {}
    for page, entries_with_hash in wiki_page_entries.items():
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
        profile['last_result_hashes'] = combined[-20:]
        profile['last_run'] = NOW_ISO
    profiles_data['last_run'] = NOW_ISO
    profiles_data['last_updated'] = NOW_ISO

    with open(PROFILES_PATH, 'w') as f:
        json.dump(profiles_data, f, indent=2)
    print(f"Updated watch_profiles.json")

    # Write summary
    total_new = sum(len(v) for v in aggregated.values())
    summary = {
        'timestamp': NOW_ISO,
        'profiles_checked': len(profiles),
        'total_new': total_new,
        'new_by_topic': {},
        'unchanged_topics': [],
        'wiki_pages_updated': list(aggregated.keys()),
    }
    for profile_name, new_hashes in new_hash_updates.items():
        if new_hashes:
            summary['new_by_topic'][profile_name] = len(new_hashes)
        else:
            summary['unchanged_topics'].append(profile_name)

    summary_path = Path('/home/hermes/wiki/temp/watch_run_2026-06-11_06-30_summary.json')
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Summary: {json.dumps(summary, indent=2)}")
    return summary

if __name__ == '__main__':
    main()
