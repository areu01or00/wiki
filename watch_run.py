#!/usr/bin/env python3
import hashlib
import json
import os
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
timestamp = now.strftime('%Y-%m-%d %H:%M UTC')
date_str = now.strftime('%Y-%m-%d')

# Load watch profiles
with open('watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)

# All search results organized by profile
search_results = {
    "system-design": [
        {"title": "Distributed Systems | Architecture Patterns \u00b7 GitScrum Docs", "url": "https://docs.gitscrum.com/en/best-practices/distributed-systems-architecture-patterns", "description": "Master distributed systems design with scalability patterns and consensus algorithms."},
        {"title": "The Complete System Design Roadmap for 2026", "url": "https://designgurus.substack.com/p/the-complete-system-design-roadmap", "description": "System design is one of the broadest subjects in software engineering."},
        {"title": "System Architecture Design: The Complete Guide 2026", "url": "https://www.systemdesignhandbook.com/guides/system-architecture-design/", "description": "This guide focuses on system architecture design as a practical skill."},
        {"title": "System Design Guide 2026 - Scalable Architecture Patterns", "url": "https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf", "description": "Master scalable architecture patterns: API Gateway, Rate Limiter, Load Balancer, Caching, CQRS."},
        {"title": "Three Bold Predictions for Distributed Systems in 2026", "url": "https://www.axoniq.io/blog/three-bold-predictions-for-distributed-systems-in-2026", "description": "A deeper shift is underway in distributed systems in 2026."},
        {"title": "Distributed Systems Patterns Every Backend Engineer Must Know 2026", "url": "https://devstarsj.github.io/2026/03/26/distributed-systems-patterns-guide-2026/", "description": "Every significant backend application runs as a distributed system in 2026."},
        {"title": "Architecture Styles in Distributed Systems - GeeksforGeeks", "url": "https://www.geeksforgeeks.org/computer-networks/architecture-styles-in-distributed-systems/", "description": "Service-Oriented Architecture (SOA) is a design paradigm in distributed systems."},
    ],
    "compilers": [
        {"title": "Compilers and Modern Language Runtimes - LLVM, JIT, GC, V8, Turbofan, Maglev", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en", "description": "LLVM's dominance, V8's 4-tier JIT, Hidden Classes and Inline Caching."},
        {"title": "Just-In-Time (JIT) Compiler with LLVM - Create Your Own Language", "url": "https://createlang.rs/01_calculator/jit_intro.html", "description": "JIT compilation is a combination of Ahead-Of-Time compilation and interpretation."},
        {"title": "JIT Compilation | microsoft/llvm | DeepWiki", "url": "https://deepwiki.com/microsoft/llvm/4-jit-compilation", "description": "This document explains LLVM's ORC JIT compilation framework."},
        {"title": "Perry - The Native TypeScript Compiler That Lowers TS Straight to LLVM Machine Code 2026", "url": "https://braindetox.kr/en/posts/perry_typescript_llvm_compiler_2026.html", "description": "Perry compiles TypeScript straight to native machine code through LLVM."},
        {"title": "LLVM Implementation for Java JIT Compilers: A Deep Dive", "url": "https://thamizhelango.medium.com/llvm-implementation-for-java-jit-compilers-a-deep-dive-2141f25f35ec", "description": "Exploring how LLVM can be integrated with Java's JIT compilation process."},
        {"title": "Session Details: 2026 European LLVM Developers' Meeting", "url": "https://llvm.swoogo.com/2026eurollvm/session/3943710/quick-talks", "description": "LLVM JIT - Upcoming Challenges and Opportunities by Lang Hames."},
        {"title": "Resume - Sanjoy Das", "url": "http://playingwithpointers.com/resume.html", "description": "Sanjoy Das - Software Engineer at Google, LLVM contributor."},
    ],
    "type-systems": [
        {"title": "Navigating the 2026 Language Landscape: A Typing and Paradigm Matrix", "url": "https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix", "description": "The lines between traditional language classifications are blurring in 2026."},
        {"title": "Type system concepts - typing documentation", "url": "https://typing.python.org/en/latest/spec/concepts.html", "description": "Python type system concepts: static, dynamic, and gradual typing."},
        {"title": "Gradual Typing in Type Theory", "url": "https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory", "description": "Type inference is the process of automatically inferring the types of expressions."},
        {"title": "Efficient Selection of Type Annotations for Performance Improvement", "url": "https://programming-journal.org/2026/11/3/", "description": "New technique to select a subset of type annotations for improving execution performance."},
        {"title": "The Rise of Static Typing - Why It Has Been Back Since the Mid-2010s 2026", "url": "https://braindetox.kr/en/posts/static_typing_rise_2026.html", "description": "Type inference and gradual typing removed almost all of the friction."},
        {"title": "Compiling Gradual Types with Evidence", "url": "https://scixplorer.org/abs/2025arXiv251222684R/abstract", "description": "Evidence-based compiler called GrEv for gradual typing."},
        {"title": "[2603.05649] Efficient Selection of Type Annotations for Performance", "url": "https://arxiv.org/abs/2603.05649", "description": "New technique to select a subset of type annotations for improving execution performance of gradually typed programs."},
    ],
    "functional-programming": [
        {"title": "Does Rust Support Functional Programming Idioms? Exploring", "url": "https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms/", "description": "Functional programming in Rust with immutability, pure functions, and declarative composition."},
        {"title": "How I Learned Monads: Not Through Haskell But Through Rust", "url": "https://johnwick.cc/index.php?title=How_I_Learned_Monads:_Not_Through_Haskell_But_Through_Rust", "description": "Learning monads through Rust's Option and Result types."},
        {"title": "Monads are Omnipresent in Rust", "url": "https://www.bertiqwerty.com/en/posts/monad", "description": "Monads are omnipresent in Rust."},
        {"title": "Functional Programming in 2026: Haskell vs. Gleam vs. Rust", "url": "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust", "description": "The era of Functional Programming as a monolithic discipline is over."},
        {"title": "Monads and Monad-Like Patterns in Rust: Exploring Functional", "url": "https://softwarepatternslexicon.com/rust/functional-programming-patterns-in-rust/monads-and-monad-like-patterns-in-rust/", "description": "Understanding monads can significantly improve your Rust programming skills."},
        {"title": "Haskell Guide [2026]: Functional Programming That Changes How", "url": "https://precisionaiacademy.com/blog/haskell-guide-2026", "description": "Haskell guide for 2026: why pure functional programming matters."},
        {"title": "Latest Monad News - (MON) Future Outlook, Trends and Market Insights", "url": "http://coinmarketcap.com/cmc-ai/monad/latest-updates", "description": "Latest Monad cryptocurrency news."},
    ],
    "algorithms": [
        {"title": "Top 100 LeetCode Coding Interview Questions (2025 Edition)", "url": "https://www.shadecoder.com/blogs/top-100-leetcode-coding-interview-questions-%282025-edition%29", "description": "A fully updated 2025 list of the Top 100 LeetCode coding interview questions."},
        {"title": "LeetCode Questions Asked in Google 2026", "url": "https://papersadda.com/article/leetcode-questions-google-2026", "description": "Knowing which LeetCode problems actually appear in Google interviews saves months."},
        {"title": "LeetCode Interview Questions: Top Patterns by Company (2026)", "url": "https://interviewpilot.dev/blog/leetcode-interview-questions", "description": "The most frequently asked LeetCode interview questions at Google, Amazon, Meta, and Microsoft."},
        {"title": "Coding Interview Prep 2026: LeetCode Strategy That Works", "url": "https://precisionaiacademy.com/blog/coding-interview-prep-guide-2026", "description": "How to ace coding interviews in 2026 - LeetCode strategy, data structures, algorithm patterns."},
        {"title": "Best DSA Sheet 2026 | To Crack Interviews - namastedev.com", "url": "https://namastedev.com/namaste-dsa-sheet", "description": "Master Data Structures and Algorithms with curated questions."},
        {"title": "Google Interview Questions | Interview Solver", "url": "https://interviewsolver.com/interview-questions/google", "description": "Google commonly asks 100 coding problems in technical interviews."},
        {"title": "Explore - LeetCode", "url": "https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms", "description": "Common patterns and tricks related to data structures and algorithms."},
        {"title": "NeetCode | Coding Interview Prep", "url": "https://neetcode.io/", "description": "Tech interview roadmaps trusted by engineers at Google, Meta, OpenAI."},
    ],
    "python-internals": [
        {"title": "The GIL Is Finally Dead: Free-Threaded Python Is Production-Ready in 2026", "url": "https://www.birjob.com/blog/python-free-threaded-gil-dead-production-ready", "description": "Python 3.14 free-threaded build is production-ready. 10x CPU speedups."},
        {"title": "How Python Works Under the Hood: Memory, GIL, and Bytecode", "url": "https://www.pythoncompiler.io/python/python-internals", "description": "Python creates an integer object in memory, assigns a reference to it."},
        {"title": "Under the Hood of Python: Internals, Optimization, and Modern Features", "url": "https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features", "description": "Understand Python internals: Cyclic Garbage Collection, __slots__ for memory savings."},
        {"title": "Python GIL: The Key to Backend Performance", "url": "https://odysse.io/en/gil-in-python-the-key-to-backend-performance-and-multithreading/", "description": "The nature of the Global Interpreter Lock and its impact on concurrency."},
        {"title": "Python Internals: Memory Management and the Global Interpreter Lock (GIL)", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil", "description": "How Python works behind the scenes to manage memory and execute code efficiently."},
        {"title": "Memory Management and GIL: Python Guide (2026) | Edugators", "url": "https://www.edugators.com/python/advanced/python-memory-gil", "description": "Learn Memory Management and GIL in our Python course."},
        {"title": "The Python GIL Controversy: Why Multi-Core Parallelism Remains Broken", "url": "https://www.javacodegeeks.com/2026/01/the-python-gil-controversy-why-multi-core-parallelism-remains-broken-and-why-it-might-not-matter.html", "description": "The GIL controversy and why multi-core parallelism remains broken."},
        {"title": "The Inner Workings of Python: Beyond the Surface", "url": "https://python.plainenglish.io/the-inner-workings-of-python-beyond-the-surface-de2b8110e732", "description": "A deep technical look at Python internals - bytecode, eval loop, memory management, the GIL."},
    ],
}

def compute_hash(title, url):
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

results_by_wiki_page = {}
new_hashes_by_profile = {}
digest_entries = {}

for profile_name, results in search_results.items():
    profile = profiles_data['profiles'][profile_name]
    wiki_page = profile['wiki_page']
    existing_hashes = set(profile.get('last_result_hashes', []))
    
    new_results = []
    new_hashes = []
    
    for r in results:
        h = compute_hash(r['title'], r['url'])
        if h not in existing_hashes:
            new_results.append(r)
            new_hashes.append(h)
    
    if wiki_page not in results_by_wiki_page:
        results_by_wiki_page[wiki_page] = []
    
    for r in new_results:
        h = compute_hash(r['title'], r['url'])
        entry = f'- **{date_str}** | [{r["title"]}]({r["url"]}) | kw: {r["description"][:60]}'
        results_by_wiki_page[wiki_page].append({
            'entry': entry,
            'hash': h,
            'title': r['title'],
            'url': r['url'],
        })
    
    new_hashes_by_profile[profile_name] = new_hashes
    digest_entries[profile_name] = new_results

# Save temp results
temp_path = f'/home/hermes/wiki/temp/watch_run_{now.strftime("%Y%m%d_%H%M%S")}.json'
os.makedirs(os.path.dirname(temp_path), exist_ok=True)
with open(temp_path, 'w') as f:
    json.dump({
        'timestamp': timestamp,
        'results_by_wiki_page': {k: [r['entry'] for r in v] for k, v in results_by_wiki_page.items()},
        'new_hashes_by_profile': new_hashes_by_profile,
    }, f, indent=2)

print(f"Temp saved: {temp_path}")
print(f"New results per profile:")
for pname, entries in digest_entries.items():
    print(f"  {pname}: {len(entries)} new")
print(f"Wiki pages to update: {list(results_by_wiki_page.keys())}")
for wp, items in results_by_wiki_page.items():
    print(f"  {wp}: {len(items)} entries")

# Now update wiki pages using Python I/O
for wiki_page, items in results_by_wiki_page.items():
    if not items:
        continue
    wiki_path = f'/home/hermes/wiki/entities/{wiki_page}'
    if not os.path.exists(wiki_path):
        print(f"  WARNING: {wiki_path} does not exist, skipping")
        continue
    
    with open(wiki_path, 'r') as f:
        content = f.read()
    lines = content.split('\n')
    
    # Find FIRST ## Updates and insert after it
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is None:
        print(f"  WARNING: No '## Updates' found in {wiki_page}")
        continue
    
    new_entries = [item['entry'] for item in items]
    lines = lines[:insert_after] + new_entries + [''] + lines[insert_after:]
    
    with open(wiki_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"  Updated {wiki_page}: {len(new_entries)} entries")

# Update watch_profiles.json
for profile_name, hashes in new_hashes_by_profile.items():
    profile = profiles_data['profiles'][profile_name]
    existing = profile.get('last_result_hashes', [])
    updated = existing + hashes
    profile['last_result_hashes'] = updated[-20:]  # Keep max 20
    profile['last_run'] = timestamp

profiles_data['last_run'] = timestamp

with open('watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)
print("Updated watch_profiles.json")

# Generate digest
total_new = sum(len(v) for v in digest_entries.values())
digest_lines = [f"## \U0001f504 Wiki Watch Digest \u2014 {timestamp}", f"Checked: {len(search_results)} profiles", ""]

topic_names = {
    "system-design": "\U0001f3d7\ufe0f System Design & Distributed Systems",
    "compilers": "\U0001f4bb Compilers, LLVM & JIT",
    "type-systems": "\U0001f522 Type Systems & Gradual Typing",
    "functional-programming": "\U0001f9db Functional Programming & Monads",
    "algorithms": "\U0001f9ee Algorithms & Interview Prep",
    "python-internals": "\U0001f40d Python Internals, GIL & Memory",
}

for pname, entries in digest_entries.items():
    if not entries:
        continue
    digest_lines.append(f"### {topic_names.get(pname, pname)}")
    digest_lines.append(f"New: {len(entries)} results")
    for e in entries:
        digest_lines.append(f"- [{e['title']}]({e['url']})")
    # Discover sub-topics
    new_topics = set()
    for e in entries:
        desc = e['description'].lower()
        if 'perry' in desc or 'perry' in e['title'].lower():
            new_topics.add('Perry TypeScript Compiler')
        if 'graceful degradation' in desc or 'graceful' in desc:
            new_topics.add('Graceful Degradation')
        if 'monad' in e['title'].lower():
            new_topics.add('Monads')
        if 'gleam' in e['title'].lower():
            new_topics.add('Gleam Language')
        if 'neetcode' in e['title'].lower():
            new_topics.add('NeetCode')
        if 'gil' in e['title'].lower() and 'free-thread' in desc.lower():
            new_topics.add('Free-Threaded Python')
        if 'rust' in e['title'].lower() and 'monad' in e['title'].lower():
            new_topics.add('Rust Monads')
    if new_topics:
        digest_lines.append(f"Sub-topics: {', '.join(sorted(new_topics))}")
    digest_lines.append("---")
    digest_lines.append("")

digest = '\n'.join(digest_lines)
print("\n=== DIGEST ===")
print(digest)
print("=== END DIGEST ===")

# Save digest for delivery
with open('/home/hermes/wiki/temp/latest_digest.txt', 'w') as f:
    f.write(digest)
