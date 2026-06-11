#!/usr/bin/env python3
"""Full wiki watch pipeline: dedup, update pages, update profiles, generate digest."""
import json
import hashlib
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path('/home/hermes/wiki')
PROFILES_PATH = Path('/home/hermes/programming-wisdom/watch_profiles.json')
ENTITIES_DIR = WIKI_ROOT / 'entities'
TEMP_DIR = WIKI_ROOT / 'temp'

# All search results from this run
batch1 = {
    "python-internals": [
        {"title": "How Python's GIL actually works (and when it bites you)", "url": "https://dev.to/lovestaco/how-pythons-gil-actually-works-and-when-it-bites-you-3f2"},
        {"title": "Advanced Python 4— GIL in Python - by Abhishek Jain - Medium", "url": "https://medium.com/@abhishekjainindore24/advanced-python-4-gil-in-python-375321837f3c"},
        {"title": "Thread states and the global interpreter lock — Python 3.14.5 ...", "url": "https://docs.python.org/3/c-api/threads.html"},
        {"title": "What Is the Python Global Interpreter Lock (GIL)? - Real Python", "url": "https://realpython.com/python-gil/"},
        {"title": "Goodbye GIL: Exploring free-threaded mode in Python 3.14 - LinkedIn", "url": "https://www.linkedin.com/pulse/goodbye-gil-exploring-free-threaded-mode-python-314-adarsh-divakaran-a93ac"},
        {"title": "Understanding the Python Global Interpreter Lock (GIL)", "url": "https://thecodinggopher.substack.com/p/understanding-the-python-global-interpreter"},
        {"title": "\"Why Python Is Removing The GIL\" (13.5 minutes by Core Dumped)", "url": "https://www.reddit.com/r/Python/comments/1pxxket/why_python_is_removing_the_gil_135_minutes_by/"},
        {"title": "The Secret Life of Python: Understanding the GIL | by Aaron Rose", "url": "https://medium.com/@aaron.rose.tx/the-secret-life-of-python-understanding-the-gil-2efacc6e008d"},
        {"title": "5 Python Performance Killers Expert Fixes 2026 Guide - iCert Global", "url": "https://www.icertglobal.com/blog/5-python-performance-killers-expert-fixes-2026-guide"},
        {"title": "Python 3.14 and the End of the GIL - Towards Data Science", "url": "https://towardsdatascience.com/python-3-14-and-the-end-of-the-gil/"},
    ],
    "algorithms": [
        {"title": "ashishps1/awesome-leetcode-resources - GitHub", "url": "https://github.com/ashishps1/awesome-leetcode-resources"},
        {"title": "Best DSA Sheet 2026 | To Crack Interviews - namastedev.com", "url": "https://namastedev.com/namaste-dsa-sheet"},
        {"title": "Complete Data Structures and Algorithms / Unwired Learning", "url": "https://unwiredlearning.com/bundles/complete-data-structures-and-algorithms"},
        {"title": "abimanyunk/Data-Structures-and-Algorithms - GitHub", "url": "https://github.com/abimanyunk/Data-Structures-and-Algorithms"},
        {"title": "Data Structures & Algorithms Roadmap 2026 - Complete Learning Path", "url": "https://www.thetutorbridge.com/roadmap/dsa"},
        {"title": "Algorithm Challenges on LeetCode Guide - AlgoHay", "url": "https://www.algohay.com/blog/algorithm-challenges-on-leetcode-guide/"},
        {"title": "I Tried 30+ Data Structures and Algorithms Courses: Here are ... - Medium", "url": "https://medium.com/javarevisited/i-tried-30-data-structures-and-algorithms-courses-here-are-my-top-5-recommendations-for-2026-124e64b5cf4c"},
        {"title": "LeetCode Python Solutions: Dynamic Programming Optimization Techniques 2026", "url": "https://johal.in/leetcode-python-solutions-dynamic-programming-optimization-techniques-2026/"},
        {"title": "DSA Tutorial - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/"},
    ],
    "functional-programming": [
        {"title": "Functional Programming in 2026: Haskell vs. Gleam vs. Rust", "url": "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust"},
        {"title": "Haskell Guide [2026]: Functional Programming That Changes How You Think", "url": "https://precisionaiacademy.com/blog/haskell-guide-2026"},
        {"title": "Does Rust Support Functional Programming Idioms? Exploring Filter/Map ...", "url": "https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms/"},
        {"title": "The Practical Value of Functional Programming — Monad, Functor, Pure ...", "url": "https://www.youngju.dev/blog/culture/2026-04-15-functional-programming-monad-haskell-elixir-erlang-gleam-effect-ts-practical-value-deep-dive-guide-2025.en"},
        {"title": "Functional Programming - Rust Design Patterns", "url": "https://rust-unofficial.github.io/patterns/functional/"},
        {"title": "How I Learned Monads: Not Through Haskell But Through Rust", "url": "https://medium.com/@saehwanpark/how-i-learned-monads-not-through-haskell-but-through-rust-f4233f7779c7"},
        {"title": "Hello, Haskell: Getting Started in 2026 · lukastymo", "url": "https://lukastymo.com/posts/025-hello-haskell-a-hands-on-lab-for-2026/"},
        {"title": "Functional Programming in Rust: Idioms and Examples | PythonLib", "url": "https://pythonlib.ru/en/post92"},
        {"title": "GitHub - rljacobson/rust_patterns: A living collection of advanced and ...", "url": "https://github.com/rljacobson/rust_patterns"},
    ],
}

batch2 = {
    "type-systems": [
        {"title": "Gradual typing - Wikipedia", "url": "https://en.wikipedia.org/wiki/Gradual_typing"},
        {"title": "Gradual typing: a new perspective | Proceedings of the ACM on...", "url": "https://dl.acm.org/doi/10.1145/3290329?cookieSet=1"},
        {"title": "Principal Type Schemes for Gradual Programs", "url": "https://www.cs.ubc.ca/~rxg/ptsgp.pdf"},
        {"title": "A semantic foundation for gradual set-theoretic types", "url": "https://theses.hal.science/tel-03853222/document"},
        {"title": "Dynamic Type Inference for Gradual Hindley–Milner Typing", "url": "https://arxiv.org/pdf/1810.12619"},
        {"title": "Higher-rank Polymorphism: Type Inference", "url": "https://xnning.github.io/papers/Thesis.pdf"},
        {"title": "GitHub - kevle6/Gradual_Typing", "url": "https://github.com/kevle6/Gradual_Typing"},
        {"title": "Static vs Dynamic Typing: Choosing the Right System for Your Code", "url": "https://jsschools.com/programming/static-vs-dynamic-typing-choosing-the-right-syste/"},
        {"title": "Gradual Typing and The Gradually Typed Lambda Calculus", "url": "https://stace.dev/static/e034014d3c4358b7745a06490939788f/gradual-typing.pdf"},
        {"title": "Languages: Types", "url": "https://ggbaker.selfip.net/prog-langs/content/lang-types.html"},
    ],
    "compilers": [
        {"title": "1. Building a JIT: Starting out with KaleidoscopeJIT - LLVM", "url": "https://llvm.org/docs/tutorial/BuildingAJIT1.html"},
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 ...", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "Implementing JIT (Just In Time) Compilation - OpenGenus IQ", "url": "https://iq.opengenus.org/implement-jit-compilation/"},
        {"title": "JIT Design and Implementation · The Julia Language", "url": "https://docs.julialang.org/en/v1/devdocs/jit/"},
        {"title": "PEP 744 – JIT Compilation | peps.python.org", "url": "https://peps.python.org/pep-0744/"},
        {"title": "2026 EuroLLVM Developers' Meeting - LLVM.org", "url": "https://llvm.org/devmtg/2026-04/"},
        {"title": "Understanding and Finding JIT Compiler Performance Bugs - arXiv", "url": "https://arxiv.org/pdf/2603.06551"},
        {"title": "Deegen: A JIT-Capable VM Generator for Dynamic Languages", "url": "https://fredrikbk.com/publications/deegen.pdf"},
        {"title": "Clang bytecode interpreter update - Red Hat Developer", "url": "https://developers.redhat.com/articles/2025/10/15/clang-bytecode-interpreter-update"},
        {"title": "2026 EuroLLVM Developers' Meeting - Agenda - Announcements", "url": "https://discourse.llvm.org/t/2026-eurollvm-developers-meeting-agenda/89725"},
    ],
    "system-design": [
        {"title": "System Design Series Part 3: Load Balancing & Caching", "url": "https://www.wasilzafar.com/pages/series/system-design/system-design-load-balancing-caching.html"},
        {"title": "System Design Guide 2026: Load Balancing, Caching, CDN, Databases ...", "url": "https://onlinetools4free.com/research/system-design-guide-2026"},
        {"title": "How I Build a Distributed System in 2026: Principles, Patterns, and ...", "url": "https://thelinuxcode.com/how-i-build-a-distributed-system-in-2026-principles-patterns-and-pitfalls/"},
        {"title": "Designing Resilient Distributed Systems: Advanced Caching Strategies ...", "url": "https://martinuke0.github.io/posts/2026-03-21-designing-resilient-distributed-systems-advanced-caching-strategies-for-performance/"},
        {"title": "Distributed Systems | Architecture Patterns · GitScrum Docs", "url": "https://docs.gitscrum.com/en/best-practices/distributed-systems-architecture-patterns"},
        {"title": "Complete Guide to System Design: Scaling, Load Balancing ... - Medium", "url": "https://medium.com/the-product-lens-looking-at-the-world-through-a/complete-guide-to-system-design-scaling-load-balancing-microservices-and-distributed-systems-cc4242c6ca1f"},
        {"title": "Load Balancing Strategies for Distributed Systems", "url": "https://andrewodendaal.com/articles/distributed-systems-load-balancing/"},
        {"title": "Load Balancing Algorithms - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/system-design/load-balancing-algorithms/"},
        {"title": "Mastering Scalability Pattern Implementation | Nerd Level Tech", "url": "https://nerdleveltech.com/mastering-scalability-pattern-implementation"},
    ],
}

# Save batch files
now_ts = datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M')
with open(TEMP_DIR / f'watch_run_{now_ts}_batch1.json', 'w') as f:
    json.dump(batch1, f, indent=2)
with open(TEMP_DIR / f'watch_run_{now_ts}_batch2.json', 'w') as f:
    json.dump(batch2, f, indent=2)

# Merge all results
all_results = {}
for batch in [batch1, batch2]:
    for profile_name, results in batch.items():
        all_results.setdefault(profile_name, []).extend(results)

print(f"Total results: {sum(len(v) for v in all_results.values())} across {len(all_results)} profiles")

# Load profiles
with open(PROFILES_PATH, 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# Load existing wiki URLs for cross-checking
existing_urls = {}
for name, prof in profiles.items():
    wiki_page = prof['wiki_page']
    page_file = ENTITIES_DIR / wiki_page.split('/')[-1]
    if page_file.exists():
        content = page_file.read_text()
        urls = set(re.findall(r'https?://[^\s\)]+', content))
        existing_urls[name] = urls
    else:
        existing_urls[name] = set()

TODAY = datetime.now(timezone.utc).strftime('%Y-%m-%d')
now_iso = datetime.now(timezone.utc).isoformat()

new_entries_by_page = defaultdict(list)
new_hashes_by_profile = defaultdict(list)
profile_stats = {}
seen_hashes_global = set()

for profile_name, prof in profiles.items():
    seen_hashes = set(prof['last_result_hashes'])
    wiki_page = prof['wiki_page']
    page_basename = wiki_page.split('/')[-1].replace('.md', '')

    new_count = 0
    sub_topics = []
    profile_hashes_to_add = []

    for result in all_results.get(profile_name, []):
        title = result['title']
        url = result['url']
        if not title or not url:
            continue
        kw = page_basename
        h = hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

        # Skip if already in this profile's hashes
        if h in seen_hashes:
            continue
        # Skip if hash already seen in this run globally
        if h in seen_hashes_global:
            continue
        # Safety layer: check actual wiki page for URL
        if url in existing_urls.get(page_basename, set()):
            seen_hashes.add(h)
            profile_hashes_to_add.append(h)
            continue

        seen_hashes.add(h)
        seen_hashes_global.add(h)
        profile_hashes_to_add.append(h)
        new_count += 1

        entry = (profile_name, title, url, h, kw)
        new_entries_by_page[wiki_page].append(entry)
        sub_topics.append(kw)

    new_hashes_by_profile[profile_name] = profile_hashes_to_add
    profile_stats[profile_name] = {
        'new': new_count,
        'sub_topics': sorted(set(sub_topics)) if sub_topics else []
    }

print("\nProfile stats:")
for p, s in profile_stats.items():
    print(f"  {p}: new={s['new']}, sub_topics={s['sub_topics']}")

print(f"\nPages to update:")
for page, entries in new_entries_by_page.items():
    print(f"  {page}: {len(entries)} entries")

# Update wiki pages
def update_wiki_page(wiki_page_path, entries):
    if not wiki_page_path.exists():
        print(f"  WARNING: {wiki_page_path} does not exist")
        return False

    content = wiki_page_path.read_text()
    lines = content.split('\n')

    insert_after_idx = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after_idx = i + 1
            break

    if insert_after_idx is None:
        print(f"  WARNING: No '## Updates' found in {wiki_page_path}")
        return False

    new_lines = []
    for profile_name, title, url, h, kw in entries:
        new_lines.append(f"- **{TODAY}** | [{title}]({url}) | kw: {kw}")
    new_lines.append('')

    new_content = lines[:insert_after_idx] + new_lines + lines[insert_after_idx:]
    wiki_page_path.write_text('\n'.join(new_content))
    return True

print("\nUpdating wiki pages:")
total_new = 0
for wiki_page, entries in new_entries_by_page.items():
    fname = wiki_page.split('/')[-1]
    target = ENTITIES_DIR / fname
    if not target.exists():
        print(f"  WARNING: {target} does not exist")
        continue
    ok = update_wiki_page(target, entries)
    print(f"  {target.name}: {'OK' if ok else 'FAILED'} ({len(entries)} entries)")
    total_new += len(entries)

# Update watch_profiles.json
print("\nUpdating watch_profiles.json:")
for profile_name, prof in profiles.items():
    new_hashes = new_hashes_by_profile.get(profile_name, [])
    combined = list(prof['last_result_hashes']) + new_hashes
    prof['last_result_hashes'] = combined[-20:]
    prof['last_run'] = now_iso
    print(f"  {profile_name}: added {len(new_hashes)} hashes (total now: {len(prof['last_result_hashes'])})")

profiles_data['last_run'] = now_iso
profiles_data['last_updated'] = now_iso

with open(PROFILES_PATH, 'w') as f:
    json.dump(profiles_data, f, indent=2)

# Build digest data
digest = {
    'date': TODAY,
    'time': datetime.now(timezone.utc).strftime('%H:%M'),
    'checked': len(profiles),
    'profiles': profile_stats,
    'new_entries': {p: len(e) for p, e in new_entries_by_page.items()},
    'total_new': total_new,
}
with open(TEMP_DIR / 'digest_data.json', 'w') as f:
    json.dump(digest, f, indent=2)

# Generate Discord digest
time_str = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')
lines = []
lines.append(f"## 🔄 Wiki Watch Digest — {time_str} UTC")
lines.append(f"Checked: {len(profiles)} profiles")
lines.append("")

for profile_name, prof in profiles.items():
    stats = profile_stats[profile_name]
    if stats['new'] > 0:
        entries = new_entries_by_page.get(prof['wiki_page'], [])
        # Only show entries for this profile
        profile_entries = [e for e in entries if e[0] == profile_name]
        lines.append(f"### {profile_name.replace('-', ' ').title()}")
        lines.append(f"New: {len(profile_entries)} results")
        for pname, title, url, h, kw in profile_entries:
            lines.append(f"- [{title}]({url}) | web search")
        lines.append("---")
    else:
        lines.append(f"### {profile_name.replace('-', ' ').title()}")
        lines.append("New: 0 results (no new content)")
        lines.append("---")

if total_new == 0:
    lines.insert(3, "No new content found across any profiles.")

digest_text = '\n'.join(lines)
with open(TEMP_DIR / f'discord_digest_{now_ts}.md', 'w') as f:
    f.write(digest_text)

print(f"\n=== DONE ===")
print(f"Checked: {len(profiles)} profiles, Total new: {total_new}")
print(f"\nDigest preview:")
print(digest_text)
