#!/usr/bin/env python3
import hashlib
import json
import os
from datetime import datetime

# All search results from the 2 batches
all_results = {
    "system-design": [
        {"title": "Cloud-Native Architecture for 2026: Microservices, Serverless, and Beyond", "url": "https://www.elightwalk.com/blog/cloud-native-architecture"},
        {"title": "Cloud Native Architecture in 2026: 8 Trends, Tools, and Implementation Guide", "url": "https://www.decipherzone.com/blog-detail/cloud-native-architecture-trends"},
        {"title": "Cloud-Native Operating System Guide: The Future of Distributed Infrastructure", "url": "https://netalith.com/blogs/operating-systems/cloud-native-operating-systems-distributed-infrastructure-2026"},
        {"title": "Cloud Native Architecture | Kubernetes & Serverless 2026", "url": "https://gegosoft.com/cloud-native-architecture"},
        {"title": "The Coming Paradigm Shift in Distributed Systems Architecture", "url": "https://gabogil.com/2026/01/20/the-coming-paradigm-shift-in-distributed-systems-architecture"},
    ],
    "compilers": [
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 ...", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at course-spring-2026 · RomanPikhotskiy/compiler-course-2026 · GitHub", "url": "https://github.com/RomanPikhotskiy/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at ...", "url": "https://github.com/VALancaster/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "Perry - The Native TypeScript Compiler That Lowers TS Straight to LLVM Machine Code 2026 - BrainDetox", "url": "https://braindetox.kr/en/posts/perry_typescript_llvm_compiler_2026.html"},
        {"title": "The Case For Compilers: A Look at SPEC CPU 2026 on LLVM 22 - ServeTheHome", "url": "https://www.servethehome.com/the-case-for-compilers-a-look-at-spec-cpu-2026-on-llvm-22"},
    ],
    "type-systems": [
        {"title": "Navigating the 2026 Language Landscape: A Typing and Paradigm Matrix - PookieTech Blog", "url": "https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix"},
        {"title": "Efficient Selection of Type Annotations for Performance ...", "url": "https://programming-journal.org/2026/11/3/"},
        {"title": "Gradual Typing in Type Theory - numberanalytics.com", "url": "https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory"},
        {"title": "Type system concepts — typing documentation", "url": "https://typing.python.org/en/latest/spec/concepts.html"},
        {"title": "Typed and Confused: Studying the Unexpected Dangers of ...", "url": "https://www.staicu.org/publications/ase2024.pdf"},
    ],
    "functional-programming": [
        {"title": "A Gentle Introduction to Haskell: About Monads", "url": "https://www.haskell.org/tutorial/monads.html"},
        {"title": "Making Sense of Monads - Monday Morning Haskell", "url": "https://academy.mondaymorninghaskell.com/p/making-sense-of-monads"},
        {"title": "Nauths · Practical uses of monads in Haskell", "url": "https://nauths.fr/en/2026/05/28/practical-use-of-monads.html"},
        {"title": "Haskell - Monads - Online Tutorials Library", "url": "https://www.tutorialspoint.com/haskell/haskell_monads.htm"},
        {"title": "Monads Tutorial — Monday Morning Haskell", "url": "https://mmhaskell.com/monads/tutorial"},
    ],
    "algorithms": [
        {"title": "Data structures and algorithms study cheatsheets for coding interviews | Tech Interview Handbook", "url": "https://www.techinterviewhandbook.org/algorithms/study-cheatsheet"},
        {"title": "How to Prepare for a Coding Interview: The Complete LeetCode ...", "url": "https://careerlift.ai/blog/how-to-prepare-coding-interview-leetcode-study-plan"},
        {"title": "Data Structures & Algorithms Roadmap 2026 - Complete Learning ...", "url": "https://www.thetutorbridge.com/roadmap/dsa"},
        {"title": "NeetCode | Coding Interview Prep, Courses, Versus Mode", "url": "https://neetcode.io/"},
        {"title": "Top 100 DSA Interview Questions - Discuss - LeetCode", "url": "https://leetcode.com/discuss/post/4258631/Top-100-DSA-Interview-Questions"},
    ],
    "python-internals": [
        {"title": "Exploring Python: Internals and Optimization", "url": "https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features"},
        {"title": "Python - Python Internals: Memory Management & the Global Interpreter Lock (GIL) | eVidhya", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil"},
        {"title": "CPython Internals: How Python Really Works Under the Hood | Abhik Sarkar", "url": "https://www.abhik.ai/articles/cpython-internals"},
        {"title": "Python 3.14 Free-Threading and Experimental JIT: How Python ...", "url": "https://blog.imseankim.com/python-3-14-free-threading-jit-compiler-gil-removal-2026"},
        {"title": "The Python GIL Controversy: Why Multi-Core Parallelism ...", "url": "https://www.javacodegeeks.com/2026/01/the-python-gil-controversy-why-multi-core-parallelism-remains-broken-and-why-it-might-not-matter.html"},
    ],
}

# Load existing profiles
with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)

# Map profile name to wiki_page
profile_to_wiki = {}
for name, prof in profiles_data['profiles'].items():
    profile_to_wiki[name] = prof['wiki_page']

# Compute hashes and deduplicate
new_results_by_profile = {}
all_hashes = {}  # profile -> list of new hashes
for profile_name, results in all_results.items():
    existing_hashes = set(profiles_data['profiles'][profile_name].get('last_result_hashes', []))
    wiki_page = profile_to_wiki[profile_name]
    all_hashes[profile_name] = []
    
    for r in results:
        title = r['title']
        url = r['url']
        h = hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()
        
        if h not in existing_hashes:
            if profile_name not in new_results_by_profile:
                new_results_by_profile[profile_name] = []
            new_results_by_profile[profile_name].append({
                'title': title,
                'url': url,
                'hash': h,
                'wiki_page': wiki_page,
            })
            all_hashes[profile_name].append(h)

# Extract keywords from title
def extract_keywords(title):
    stop = {'the','a','an','in','on','for','to','and','or','of','is','it','that','with','from','by','at','as','how','what','why','which','are','be','this','has','have'}
    words = []
    for w in title.replace(':','').replace(',','').replace('.','').replace('-',' ').replace('|',' ').replace('—',' ').split():
        if w.lower() not in stop and len(w) > 1 and not w.startswith('('):
            words.append(w)
    return words[:3]

# Generate date
today = datetime.utcnow().strftime('%Y-%m-%d')
now_utc = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

# Group by wiki_page
updates_by_wiki_page = {}
for profile_name, results in new_results_by_profile.items():
    for r in results:
        wp = r['wiki_page']
        if wp not in updates_by_wiki_page:
            updates_by_wiki_page[wp] = []
        updates_by_wiki_page[wp].append(r)

# === STEP 5: Update wiki pages ===
wiki_dir = '/home/hermes/wiki/entities'

for wiki_page, entries in updates_by_wiki_page.items():
    filepath = os.path.join(wiki_dir, wiki_page)
    if not os.path.exists(filepath):
        print(f"WARNING: Wiki page {filepath} does not exist, skipping")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find ## Updates section and insert after it
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is None:
        # If no ## Updates section, append at end
        insert_after = len(lines)
        lines.append('')
        lines.append('## Updates')
        lines.append('')
        insert_after = len(lines)
    
    # Build new entry lines
    new_lines = []
    seen_titles = set()
    for e in entries:
        if e['title'] in seen_titles:
            continue
        seen_titles.add(e['title'])
        kws = extract_keywords(e['title'])
        kw_str = ', '.join(kws) if kws else e['title'].split()[0]
        new_lines.append(f"- **{today}** | [{e['title']}]({e['url']}) | kw: {kw_str}")
    
    if new_lines:
        lines = lines[:insert_after] + new_lines + [''] + lines[insert_after:]
        
        with open(filepath, 'w') as f:
            f.write('\n'.join(lines))
        print(f"Updated {wiki_page} with {len(new_lines)} entries")

# === STEP 6: Update watch_profiles.json ===
for profile_name, hashes_list in all_hashes.items():
    if hashes_list:
        prof = profiles_data['profiles'][profile_name]
        existing = prof.get('last_result_hashes', [])
        existing.extend(hashes_list)
        prof['last_result_hashes'] = existing[-20:]  # Keep max 20
        prof['last_run'] = now_utc

profiles_data['last_run'] = now_utc

with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)

print(f"\nUpdated watch_profiles.json")

# === Print summary ===
print(f"\n--- SUMMARY ---")
print(f"Total profiles checked: {len(all_results)}")
total_new = 0
for profile_name, results in new_results_by_profile.items():
    count = len(results)
    total_new += count
    print(f"  {profile_name}: {count} new results -> {profile_to_wiki[profile_name]}")
    for r in results:
        print(f"    - {r['title'][:80]}")
print(f"Total new entries: {total_new}")
print(f"Date: {now_utc}")
