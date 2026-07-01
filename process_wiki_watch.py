#!/usr/bin/env python3
"""Wiki Watch pipeline - full processor."""

import json
import hashlib
import os
import re
from datetime import datetime, timezone
from typing import Dict, List, Any

# ============ CONFIGURATION ============
PROFILES_FILE = '/home/hermes/wiki/watch_profiles.json'
ENTITIES_DIR = '/home/hermes/wiki/entities'
TEMP_DIR = '/home/hermes/wiki/temp'
DISCORD_WEBHOOK_ID = '1491398499521003622'

# ============ PROFILES TO PROCESS ============
# Batch 1 results (already fetched)
BATCH1_RESULTS = {
    'system-design': [
        {"title": "Three Bold Predictions for Distributed Systems in 2026 - Axoniq", "url": "https://www.axoniq.io/blog/three-bold-predictions-for-distributed-systems-in-2026"},
        {"title": "The Complete Guide to System Design in 2026 - DEV Community", "url": "https://dev.to/fahimulhaq/complete-guide-to-system-design-oc7"},
        {"title": "Modern Software Architecture Patterns That Scale In 2026 - UpCloud", "url": "https://upcloud.com/blog/modern-software-architecture-patterns-2026-scales-production/"},
        {"title": "A Guide to Large-Scale Distributed Systems (2026)", "url": "https://www.systemdesignhandbook.com/blog/large-scale-distributed-systems/"},
        {"title": "50 System Design Patterns Every Engineer Should Know in 90 ...", "url": "https://designgurus.substack.com/p/50-system-design-patterns-every-engineer"},
        {"title": "Master System Design Roadmap 2026 | Rocky Bhatia posted on the ...", "url": "https://www.linkedin.com/posts/rocky-bhatia-a4801010_master-system-design-in-2026-one-visual-activity-7418616191402942464--RPc"},
        {"title": "10 System Design Patterns You Must Know in 2026 - MockExperts", "url": "https://www.mockexperts.com/blog/10-system-design-patterns-you-must-know-2026"},
        {"title": "9 Essential Software Architecture Patterns for Scalable Distributed ...", "url": "https://www.reddit.com/r/softwarearchitecture/comments/1tl6qsr/9_essential_software_architecture_patterns_for/"},
        {"title": "Complete Distributed Systems Guide 2026 - College Nirnay", "url": "https://www.collegenirnay.com/articles/complete-guide-distributed-systems-beginners"},
        {"title": "This Is What Actually Scales in 2026 | by Kavya's Programming Path", "url": "https://medium.com/javarevisited/forget-microservices-these-3-architecture-patterns-scale-better-in-2026-0194729ae6e3"},
    ],
    'compilers': [
        {"title": "Just-in-time compilation - Wikipedia", "url": "https://en.wikipedia.org/wiki/Just-in-time_compilation"},
        {"title": "The LLVM Compiler Infrastructure Project", "url": "https://llvm.org/"},
        {"title": "OrcJIT at Scale with the llvm-autojit Plugin - FOSDEM 2026", "url": "https://fosdem.org/2026/schedule/event/FTCATX-llvm-autojit/"},
        {"title": "LLVM Compiler Infrastructure - Google Summer of Code", "url": "https://summerofcode.withgoogle.com/programs/2026/organizations/llvm-compiler-infrastructure"},
        {"title": "2026 EuroLLVM Developers' Meeting - LLVM.org", "url": "https://llvm.org/devmtg/2026-04/"},
        {"title": "Retrofitting JIT Compilers into C Interpreters - tratt.net", "url": "https://tratt.net/laurie/blog/2026/retrofitting_jit_compilers_into_c_interpreters.html"},
        {"title": "JIT Design and Implementation - Julia Documentation", "url": "https://docs.julialang.org/en/v1/devdocs/jit/"},
        {"title": "Easy::jit: A just-in-time compiler for C++ - GitHub", "url": "https://github.com/jmmartinez/easy-just-in-time"},
        {"title": "Unmasking the World of LLVM IR Based JIT Execution", "url": "https://whiteknightlabs.com/2025/12/23/just-in-time-for-runtime-interpretation-unmasking-the-world-of-llvm-ir-based-jit-execution/"},
        {"title": "The LLVM Compiler Infrastructure Project", "url": "https://llvm.org/OpenProjects.html"},
    ],
    'type-systems': [
        {"title": "Elixir v1.20 released: now a gradually typed language", "url": "https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/"},
        {"title": "Navigating the Language Labyrinth: A 2026 Matrix Analysis of ...", "url": "https://pookietech.site/blog/navigating-the-language-labyrinth-a-2026-matrix-analysis-of-typing-and-paradigms"},
        {"title": "Efficient Selection of Type Annotations for Performance ... - arXiv", "url": "https://arxiv.org/pdf/2603.05649"},
        {"title": "PyCon US 2026 Typing Summit Recap - Bernát Gábor", "url": "https://bernat.tech/posts/pycon-us-2026-typing-summit-recap/"},
        {"title": "Type Inference for Functional and Imperative Dynamic Languages", "url": "https://mlaurent.ovh/publications/type_inference_imp.pdf"},
        {"title": "Type inference of all constructs and the next 15 months", "url": "https://elixir-lang.org/blog/2026/01/09/type-inference-of-all-and-next-15/"},
        {"title": "What type systems do you find interesting / useful / underrated?", "url": "https://www.reddit.com/r/ProgrammingLanguages/comments/1oj58xg/what_type_systems_do_you_find_interesting_useful/"},
        {"title": "Local Contextual Type Inference | Proceedings of the ACM on ...", "url": "https://dl.acm.org/doi/10.1145/3776653"},
        {"title": "What Is Gradual Typing? - ITU Online IT Training", "url": "https://www.ituonline.com/tech-definitions/what-is-gradual-typing/"},
        {"title": "Statically Typed vs Dynamically Typed Languages - Medium", "url": "https://medium.com/towardsdev/statically-typed-vs-dynamically-typed-languages-a-comprehensive-deep-dive-e30c09ec4439"},
    ],
}

# Batch 2 results (already fetched)
BATCH2_RESULTS = {
    'functional-programming': [
        {"title": "Monad (functional programming) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Monad_(functional_programming)"},
        {"title": "Monads and Effects | Bartosz Milewski's Programming Cafe", "url": "https://bartoszmilewski.com/2016/11/30/monads-and-effects/"},
        {"title": "functional programming - Why are side-effects modeled as monads...", "url": "https://stackoverflow.com/questions/2488646/why-are-side-effects-modeled-as-monads-in-haskell"},
        {"title": "Monads in Haskell, explained without the jargon (2026)", "url": "https://coldwa.st/e/blog/2026-06-14-haskell-monads.html"},
        {"title": "What Is a Monad in Functional Programming? | Built In", "url": "https://builtin.com/software-engineering-perspectives/monads"},
        {"title": "Monads and Monad-Like Patterns in Rust: Exploring Functional...", "url": "https://softwarepatternslexicon.com/rust/functional-programming-patterns-in-rust/monads-and-monad-like-patterns-in-rust/"},
        {"title": "Rust: Functional Programming & Monads", "url": "https://readmedium.com/functional-programming-with-monads-90230ccccb48"},
        {"title": "Monads: A Powerful Concept in Functional Programming | Algor Cards", "url": "https://cards.algoreducation.com/en/content/9SCjzneK/monads-functional-programming"},
        {"title": "Just how much can you do with functions? | Haskell, Functional...", "url": "https://www.youtube.com/watch?v=rEgOP6MVGAM"},
        {"title": "monad-transformers · GitHub Topics · GitHub", "url": "https://github.com/topics/monad-transformers"},
    ],
    'algorithms': [
        {"title": "Coding Interview Prep 2026: LeetCode Strategy That Works", "url": "https://precisionaiacademy.com/blog/coding-interview-prep-guide-2026"},
        {"title": "The Ultimate Leetcode Roadmap: Data Structures & Algorithms ... - Medium", "url": "https://medium.com/@katravallicoding/the-ultimate-leetcode-roadmap-data-structures-algorithms-simplified-7564f84af829"},
        {"title": "Data Structure I - LeetCode", "url": "https://leetcode.com/problem-list/m1b6ucdi/"},
        {"title": "GitHub - heydi424/DSA-Handbook-for-Coding-Interviews_2026", "url": "https://github.com/heydi424/DSA-Handbook-for-Coding-Interviews_2026"},
        {"title": "ashishps1/awesome-leetcode-resources - GitHub", "url": "https://github.com/ashishps1/awesome-leetcode-resources"},
        {"title": "Namaste DSA Sheet | To Crack FAANG & PBC's Interviews", "url": "https://namastedev.com/namaste-dsa-sheet"},
        {"title": "NeetCode | Coding Interview Prep, Courses, Versus Mode", "url": "https://neetcode.io/"},
        {"title": "I Tried 20+ Java DSA Courses with LeetCode Exercises on Udemy ... - Medium", "url": "https://medium.com/javarevisited/i-tried-20-java-dsa-courses-with-leetcode-exercises-on-udemy-here-are-my-top-5-recommendations-86085dfbcd84"},
        {"title": "LeetCode - The World's Leading Online Programming Learning Platform", "url": "https://leetcode.com/problemset/algorithms/"},
        {"title": "", "url": "/clev?event=StartpageResultClick"},
    ],
    'python-internals': [
        {"title": "Python in 2026: Free-Threading and UV Change Everything - Medium", "url": "https://medium.com/@kenancan.dev/python-in-2026-free-threading-and-uv-change-everything-548c19b170aa"},
        {"title": "Memory Management — Python 3.14.6 documentation", "url": "https://docs.python.org/3/c-api/memory.html"},
        {"title": "How Python's GIL actually works (and when it bites you)", "url": "https://dev.to/lovestaco/how-pythons-gil-actually-works-and-when-it-bites-you-3f2"},
        {"title": "How Python's GIL Works - Codefinity", "url": "https://codefinity.com/blog/How-Python's-GIL-Works"},
        {"title": "Using `malloc_trim` to help with memory management", "url": "https://discuss.python.org/t/using-malloc-trim-to-help-with-memory-management/107682"},
        {"title": "Goodbye GIL: Exploring free-threaded mode in Python 3.14 - LinkedIn", "url": "https://www.linkedin.com/pulse/goodbye-gil-exploring-free-threaded-mode-python-314-adarsh-divakaran-a93ac"},
        {"title": "Memory Management | Python - AlgoMaster.io", "url": "https://algomaster.io/learn/python/memory-management"},
        {"title": "What is the Python Global Interpreter Lock (GIL) - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/python/what-is-the-python-global-interpreter-lock-gil/"},
        {"title": "Python 3.14 and the End of the GIL - Towards Data Science", "url": "https://towardsdatascience.com/python-3-14-and-the-end-of-the-gil/"},
        {"title": "Tearing Off the GIL Veil: A Deep Dive into Python Multithreading's ...", "url": "https://medium.com/codex/tearing-off-the-gil-veil-a-deep-dive-into-python-multithreadings-inner-mechanics-a94c92546e79"},
    ],
}

ALL_RESULTS = {**BATCH1_RESULTS, **BATCH2_RESULTS}


def compute_hash(title: str, url: str) -> str:
    """Compute MD5(title+url) with NO separator."""
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()


def load_profiles() -> Dict:
    with open(PROFILES_FILE, 'r') as f:
        data = json.load(f)
    return data['profiles']


def save_temp_results(results: Dict, batch_num: int):
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    path = f'{TEMP_DIR}/watch_run_{timestamp}_batch{batch_num}.json'
    os.makedirs(TEMP_DIR, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"[TEMP] Saved batch {batch_num} to {path}")
    return path


def get_wiki_entry_for_result(result: Dict, keyword: str = '') -> str:
    """Build a wiki entry line for a result."""
    title = result['title']
    url = result['url']
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    return f"- **{today}** | [{title}]({url}) | kw: {keyword}"


def find_updates_section(content: str) -> int:
    """Find the ## Updates section and return the line index to insert after."""
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            return i + 1
    return -1


def update_wiki_page(wiki_page: str, new_entries: List[str]) -> bool:
    """Update wiki page with new entries using Python I/O."""
    if not new_entries:
        print(f"  [WIKI] No new entries for {wiki_page}")
        return False
    
    path = f'{ENTITIES_DIR}/{wiki_page}'
    if not os.path.exists(path):
        print(f"  [WIKI] Wiki page not found: {path}")
        return False
    
    with open(path, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    insert_idx = find_updates_section(content)
    
    if insert_idx == -1:
        print(f"  [WIKI] No ## Updates section found in {wiki_page}")
        return False
    
    # Insert entries after the ## Updates line
    lines = lines[:insert_idx] + new_entries + [''] + lines[insert_idx:]
    
    with open(path, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"  [WIKI] Updated {wiki_page} with {len(new_entries)} entries")
    return True


def update_profiles_json(profiles: Dict, new_hashes: Dict[str, List[str]]):
    """Update profiles with new result hashes and last_run time."""
    now = datetime.now(timezone.utc).isoformat()
    
    for profile_name, new_hash_list in new_hashes.items():
        if profile_name not in profiles:
            continue
        profile = profiles[profile_name]
        if not isinstance(profile, dict):
            continue
        
        # Append new hashes (max 20)
        existing_hashes = profile.get('last_result_hashes', [])
        updated_hashes = new_hash_list + existing_hashes
        profile['last_result_hashes'] = updated_hashes[:20]
        
        # Update last_run
        profile['last_run'] = now
    
    # Write back
    with open(PROFILES_FILE, 'r') as f:
        data = json.load(f)
    
    for profile_name, new_hash_list in new_hashes.items():
        if profile_name not in data['profiles']:
            continue
        profile = data['profiles'][profile_name]
        if not isinstance(profile, dict):
            continue
        
        existing_hashes = profile.get('last_result_hashes', [])
        updated_hashes = new_hash_list + existing_hashes
        profile['last_result_hashes'] = updated_hashes[:20]
        profile['last_run'] = now
    
    with open(PROFILES_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"[PROFILES] Updated watch_profiles.json")


def build_discord_digest(all_new_by_profile: Dict[str, List], total_new: int) -> str:
    """Build Discord digest message."""
    now_utc = datetime.now(timezone.utc)
    date_str = now_utc.strftime('%Y-%m-%d %H:%M UTC')
    
    lines = [
        f"## 🔄 Wiki Watch Digest — {date_str}",
        f"Checked: {len(all_new_by_profile)} profiles",
        ""
    ]
    
    for profile_name, results in all_new_by_profile.items():
        if not results:
            continue
        lines.append(f"### {profile_name.replace('-', ' ').title()}")
        lines.append(f"New: {len(results)} results")
        for r in results[:5]:  # Show max 5 in digest
            lines.append(f"- [{r['title'][:80]}]({r['url']})")
        if len(results) > 5:
            lines.append(f"  ... and {len(results) - 5} more")
        lines.append("---")
    
    return '\n'.join(lines)


def main():
    print("=" * 60)
    print("WIKI WATCH PIPELINE")
    print("=" * 60)
    
    # Save temp batch files
    save_temp_results(BATCH1_RESULTS, 1)
    save_temp_results(BATCH2_RESULTS, 2)
    
    # Load profiles
    profiles = load_profiles()
    print(f"\n[PROFILES] Loaded {len(profiles)} profiles")
    
    # Process each profile
    new_by_wiki_page: Dict[str, Dict[str, List]] = {}  # wiki_page -> {profile_name: [entries]}
    all_new_hashes: Dict[str, List[str]] = {}
    all_new_by_profile: Dict[str, List] = {}
    
    for profile_name, search_results in ALL_RESULTS.items():
        print(f"\n[PROCESSING] {profile_name}")
        
        if profile_name not in profiles:
            print(f"  [SKIP] Profile not found in watch_profiles.json")
            continue
        
        profile = profiles[profile_name]
        if not isinstance(profile, dict):
            print(f"  [SKIP] Profile is not a dict")
            continue
        
        wiki_page = profile.get('wiki_page', '')
        if not wiki_page:
            print(f"  [SKIP] No wiki_page configured")
            continue
        
        existing_hashes = set(profile.get('last_result_hashes', []))
        
        # Deduplicate
        new_results = []
        new_hashes = []
        for result in search_results:
            title = result['title']
            url = result['url']
            if not title or not url:
                continue
            h = compute_hash(title, url)
            if h not in existing_hashes and h not in new_hashes:
                new_results.append(result)
                new_hashes.append(h)
        
        print(f"  Search results: {len(search_results)}, New (deduplicated): {len(new_results)}")
        
        if not new_results:
            all_new_by_profile[profile_name] = []
            continue
        
        all_new_by_profile[profile_name] = new_results
        all_new_hashes[profile_name] = new_hashes
        
        # Group by wiki page
        if wiki_page not in new_by_wiki_page:
            new_by_wiki_page[wiki_page] = {}
        new_by_wiki_page[wiki_page][profile_name] = new_results
    
    # Update wiki pages (grouped by wiki_page)
    print("\n" + "=" * 60)
    print("UPDATING WIKI PAGES")
    print("=" * 60)
    
    for wiki_page, profile_results in new_by_wiki_page.items():
        # Aggregate all new results for this wiki page from all profiles
        all_entries_for_page = []
        for profile_name, results in profile_results.items():
            for result in results:
                title = result['title']
                url = result['url']
                keyword = profile_name
                today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
                entry = f"- **{today}** | [{title}]({url}) | kw: {keyword}"
                all_entries_for_page.append(entry)
        
        if all_entries_for_page:
            update_wiki_page(wiki_page, all_entries_for_page)
    
    # Update profiles JSON
    print("\n" + "=" * 60)
    print("UPDATING PROFILES")
    print("=" * 60)
    update_profiles_json(profiles, all_new_hashes)
    
    # Git push
    print("\n" + "=" * 60)
    print("GIT PUSH")
    print("=" * 60)
    os.chdir('/home/hermes/wiki')
    commit_msg = f"$(date '+%Y-%m-%d %H:%M IST') Wiki watch update"
    result = os.system(f"git add -A && git commit -m '{commit_msg}' && git push origin main 2>&1")
    if result == 0:
        print("[GIT] Push successful")
    else:
        print(f"[GIT] Push failed with code {result}")
    
    # Discord digest
    print("\n" + "=" * 60)
    print("DISCORD DIGEST")
    print("=" * 60)
    total_new = sum(len(v) for v in all_new_by_profile.values())
    digest = build_discord_digest(all_new_by_profile, total_new)
    print(digest)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Profiles checked: {len(ALL_RESULTS)}")
    print(f"Total new results: {total_new}")
    for profile_name, results in all_new_by_profile.items():
        if results:
            print(f"  {profile_name}: {len(results)} new")
    
    return all_new_by_profile


if __name__ == '__main__':
    main()
