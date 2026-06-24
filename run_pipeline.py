#!/usr/bin/env python3
"""Wiki Watch pipeline: dedup, update wiki pages, update profiles, git push, build digest."""
import hashlib
import json
import os
import subprocess
import re
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
timestamp = now.strftime('%Y-%m-%d %H:%M UTC')
date_str = now.strftime('%Y-%m-%d')

os.chdir('/home/hermes/wiki')

# Load batch results
all_results = {}
for batch_file in ['temp/watch_run_20260624_1817_batch1.json', 'temp/watch_run_20260624_1817_batch2.json']:
    with open(batch_file, 'r') as f:
        batch = json.load(f)
    for profile, results in batch['results'].items():
        if profile not in all_results:
            all_results[profile] = []
        all_results[profile].extend(results)

# Load profiles
with open('watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# Hash function
def compute_hash(title, url):
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

# Skip irrelevant results (Wikipedia generic pages, dictionary entries, generic language tutorials)
skip_domains = [
    "en.m.wikipedia.org/wiki/",
    "simple.m.wikipedia.org/wiki/",
    "merriam-webster.com",
    "dictionary.com",
    "definitions.net",
    "thewindowsclub.com",
    "scienceinsights.org",
    "imdb.com",
    "codecademy.com",
    "online-python.com",
    "w3schools.com",
    "python.org/",  # python.org homepage is generic
    "wikipedia.org/wiki/",  # generic Wikipedia entries
    "algs4.cs.princeton.edu",
    "ocw.mit.edu",
    "geeksforgeeks.org/dsa/introduction-to-algorithms",
    "reddit.com/r/ProgrammingLanguages/comments/1oj58xg",  # generic reddit discussion
    "lobste.rs",
    "hacker-news",  # HN generic
]

def is_relevant(result, profile):
    """Skip truly irrelevant results."""
    url = result['url']
    title = result['title']

    # Skip if URL domain is in skip list
    for skip in skip_domains:
        if skip in url:
            return False

    # For python-internals, skip python.org generic homepage
    if profile == 'python-internals':
        if url == 'https://www.python.org/' or url == 'https://en.wikipedia.org/wiki/Python_(programming_language)':
            return False

    # For algorithms, skip the Wikipedia algorithm pages (too generic)
    if profile == 'algorithms':
        if 'wikipedia.org' in url and 'algorithm' in url.lower():
            return False
        if 'sedgewick' in url.lower() or 'mit.edu' in url:
            return False  # classic textbook, not news

    # For compilers, skip generic Wikipedia JIT page
    if profile == 'compilers':
        if 'wikipedia.org/wiki/Just-in-time' in url:
            return False
        if 'llvm.org/' == url or 'llvm.org/OpenProjects' in url:
            return False  # generic LLVM homepage, not new content
        if 'summerofcode' in url:
            return False  # GSoC listing page

    # For type-systems, skip generic Reddit thread
    if profile == 'type-systems':
        if 'reddit.com/r/ProgrammingLanguages' in url:
            return False

    # For functional-programming, skip lobsters and HN
    if profile == 'functional-programming':
        if 'lobste.rs' in url or 'ycombinator' in url:
            return False

    # For system-design, skip generic System Wikipedia entries
    if profile == 'system-design':
        if 'wikipedia.org' in url and 'system' in url.lower():
            return False
        if 'merriam-webster' in url or 'thewindowsclub' in url:
            return False
        if 'scienceinsights.org' in url:
            return False

    return True

# Hash dedup
results_by_profile = {}
new_hashes_by_profile = {}
sub_topics_discovered = {}

for profile_name, results in all_results.items():
    existing_hashes = set(profiles[profile_name]['last_result_hashes'])
    existing_sub_topics = set(profiles[profile_name].get('sub_topics', []))
    new_results = []
    new_hashes = []
    new_subtopics = set()

    for r in results:
        title = r['title']
        url = r['url']

        if not is_relevant(r, profile_name):
            continue

        h = compute_hash(title, url)
        if h in existing_hashes:
            continue
        if h in new_hashes:  # Avoid same-hash duplicates within this run
            continue

        new_results.append({"title": title, "url": url, "hash": h})
        new_hashes.append(h)

        # Sub-topic discovery: extract capitalized multi-word phrases and notable words
        # Skip very common words
        stop_words = {'the', 'and', 'for', 'with', 'how', 'what', 'why', 'who', 'when', 'where',
                      'this', 'that', 'these', 'those', 'from', 'into', 'than', 'then', 'are',
                      'was', 'were', 'been', 'being', 'have', 'has', 'had', 'will', 'would',
                      'can', 'could', 'should', 'may', 'might', 'must', 'shall', 'not', 'but',
                      'its', 'you', 'your', 'our', 'their', 'his', 'her', 'its', 'all', 'any',
                      'some', 'most', 'more', 'less', 'much', 'very', 'just', 'also', 'still',
                      'now', 'here', 'there', 'one', 'two', 'three', 'new', 'use', 'using',
                      'via', 'per', 'top', 'best', 'guide', 'overview', 'introduction',
                      'release', 'released', 'update', 'updated'}

        words = title.split()
        for word in words:
            clean = word.strip('.,:;!?()[]{}\"\'-–—')
            if len(clean) > 3 and clean.lower() not in stop_words:
                if clean not in existing_sub_topics and clean not in new_subtopics:
                    new_subtopics.add(clean)

    results_by_profile[profile_name] = new_results
    new_hashes_by_profile[profile_name] = new_hashes
    sub_topics_discovered[profile_name] = sorted(list(new_subtopics))[:15]

total_new = sum(len(r) for r in results_by_profile.values())
print(f"Total new results: {total_new}")
for p, r in results_by_profile.items():
    print(f"  {p}: {len(r)} new")

# Step 4 & 5: Group by wiki page, update wiki pages
new_entries_by_page = {}
for pname, results in results_by_profile.items():
    page = profiles[pname]['wiki_page']
    if page not in new_entries_by_page:
        new_entries_by_page[page] = []
    for r in results:
        # Keyword = first 3 meaningful words from title
        words = r['title'].replace('-', ' ').replace(':', ' ').replace('|', ' ').split()
        kw_words = []
        for w in words:
            clean = w.strip('.,:;!?()[]{}"\'-–—')
            if clean and not clean.lower() in {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'of', 'is', 'are', 'for', 'with', 'and'}:
                kw_words.append(clean)
            if len(kw_words) >= 3:
                break
        keyword = ' '.join(kw_words[:3]) if kw_words else 'wiki'
        entry = f"- **{date_str}** | [{r['title']}]({r['url']}) | kw: {keyword}"
        new_entries_by_page[page].append(entry)

updated_pages = []
for page, entries in new_entries_by_page.items():
    if not entries:
        continue
    filepath = f'entities/{page}'
    if not os.path.exists(filepath):
        print(f"WARNING: {filepath} does not exist, skipping")
        continue

    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break

    if insert_after is not None:
        # Insert after the first ## Updates header, before any existing content
        lines = lines[:insert_after] + entries + [''] + lines[insert_after:]
    else:
        lines.append('')
        lines.append('## Updates')
        lines.append('')
        lines.extend(entries)

    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))

    updated_pages.append(page)
    print(f"Updated {page} with {len(entries)} entries")

# Step 6: Update watch_profiles.json
for pname in all_results.keys():
    existing = profiles[pname]['last_result_hashes']
    new_h = new_hashes_by_profile[pname]
    updated = existing + new_h
    profiles[pname]['last_result_hashes'] = updated[-20:]
    profiles[pname]['last_run'] = timestamp
    profiles[pname]['new_sub_topics_this_run'] = sub_topics_discovered.get(pname, [])
    profiles[pname]['last_new_count'] = len(new_h)
    profiles[pname]['_new_total_for_digest'] = profiles[pname].get('_new_total_for_digest', 0) + len(new_h)

    for st in sub_topics_discovered.get(pname, []):
        if st not in profiles[pname]['sub_topics']:
            profiles[pname]['sub_topics'].append(st)

profiles_data['last_run'] = timestamp
profiles_data['profiles'] = profiles

with open('watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2, ensure_ascii=False)

print("Updated watch_profiles.json")

# Save final temp file for record
final_temp = {
    "timestamp": timestamp,
    "results_by_profile": {p: [{"title": r['title'], "url": r['url']} for r in r2] for p, r2 in results_by_profile.items()},
    "new_hashes_by_profile": new_hashes_by_profile,
    "sub_topics_by_profile": sub_topics_discovered,
    "updated_pages": updated_pages,
    "total_new": total_new,
}
with open(f'temp/watch_run_{now.strftime("%Y%m%d_%H%M%S")}_final.json', 'w') as f:
    json.dump(final_temp, f, indent=2)

# Step 7: Git push
try:
    result = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True, cwd='/home/hermes/wiki')
    print(f"git add: rc={result.returncode}")
    result = subprocess.run(['git', 'commit', '-m', f'{timestamp} Wiki watch update'], capture_output=True, text=True, cwd='/home/hermes/wiki')
    print(f"git commit: rc={result.returncode}")
    print(result.stdout)
    if result.stderr:
        print(f"  stderr: {result.stderr.strip()}")
    result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True, cwd='/home/hermes/wiki', timeout=60)
    print(f"git push: rc={result.returncode}")
    print(result.stdout)
    if result.stderr:
        print(f"  stderr: {result.stderr.strip()}")
except Exception as e:
    print(f"Git error: {e}")

# Step 8: Build digest
profile_display = {
    "system-design": "System Design",
    "compilers": "Compilers & LLVM",
    "type-systems": "Type Systems",
    "functional-programming": "Functional Programming",
    "algorithms": "Algorithms & DSA",
    "python-internals": "Python Internals",
}

digest_lines = []
digest_lines.append(f"## \ud83d\udd04 Wiki Watch Digest \u2014 {timestamp}")
digest_lines.append(f"Checked: {len(all_results)} profiles")
digest_lines.append(f"New results: {total_new}")
digest_lines.append("")

for pname in all_results.keys():
    display = profile_display.get(pname, pname)
    results = results_by_profile[pname]
    digest_lines.append(f"### {display}")
    digest_lines.append(f"New: {len(results)} results")
    if results:
        for r in results[:5]:
            t = r['title'][:90] + ('...' if len(r['title']) > 90 else '')
            digest_lines.append(f"- [{t}]({r['url']}) | source: web_search")
        if len(results) > 5:
            digest_lines.append(f"- ...and {len(results) - 5} more")
    else:
        digest_lines.append("No new results this cycle")
    new_st = sub_topics_discovered.get(pname, [])
    if new_st:
        digest_lines.append(f"Added sub-topics: {', '.join(new_st[:8])}")
    digest_lines.append("---")

digest_text = '\n'.join(digest_lines)
print("\n=== DISCORD DIGEST ===")
print(digest_text)

# Save digest for delivery
with open(f'temp/watch_run_{now.strftime("%Y%m%d_%H%M%S")}_digest.json', 'w') as f:
    json.dump({"digest": digest_text, "timestamp": timestamp, "total_new": total_new,
               "per_profile": {p: len(r) for p, r in results_by_profile.items()}}, f, indent=2)