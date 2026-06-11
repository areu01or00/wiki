import hashlib, json, os
from datetime import datetime, timezone

profiles = json.load(open('/home/hermes/wiki/watch_profiles.json'))

# Collect all search results grouped by profile
all_results = {
    "system-design": [
        {"title": "Modern Distributed Systems: Patterns and Anti-patterns", "url": "https://anshadameenza.com/blog/technology/distributed-systems-patterns"},
        {"title": "Microservices Architecture Patterns in 2026: Mastering Distributed Systems Design", "url": "https://www.andrewhansen.au/microservices-architecture-patterns-in-2026-mastering-distributed-systems-design/"},
        {"title": "9 Software Architecture Patterns for Distributed Systems", "url": "https://dev.to/somadevtoo/9-software-architecture-patterns-for-distributed-systems-2o86"},
        {"title": "Evolving Software Architecture for the Cloud Era", "url": "https://medium.com/@bubu.tripathy/evolving-software-architecture-for-the-cloud-era-331dc2051c14"},
        {"title": "Patterns of Distributed Systems: Complete Roadmap", "url": "https://chanhle.dev/en/blog/patterns-of-distributed-systems-roadmap"},
        {"title": "System Design Guide 2026 - Scalable Architecture Patterns", "url": "https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf"},
        {"title": "Microservices Design Patterns for Cloud Architecture", "url": "https://ieeechicago.org/microservices-design-patterns-for-cloud-architecture"},
        {"title": "Mastering Distributed Systems — Patterns & Principles (2026)", "url": "https://tutorialq.com/dev/microservices/mastering-distributed-systems"},
    ],
    "compilers": [
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8, Turbofan, Maglev", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "Building a JIT: Starting out with KaleidoscopeJIT", "url": "https://github.com/RomanPikhotskiy/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "The Case For Compilers: A Look at SPEC CPU 2026 on LLVM 22", "url": "https://www.servethehome.com/the-case-for-compilers-a-look-at-spec-cpu-2026-on-llvm-22/"},
        {"title": "The state of GPU codegen with Nim (bonus: LLVM JIT)", "url": "https://forum.nim-lang.org/t/9794"},
        {"title": "JIT Compiler with LLVM - Create Your Own Programming Language with Rust", "url": "https://createlang.rs/01_calculator/jit_intro.html"},
        {"title": "Perry - The Native TypeScript Compiler That Lowers TS Straight to LLVM Machine Code 2026", "url": "https://braindetox.kr/en/posts/perry_typescript_llvm_compiler_2026.html"},
    ],
    "type-systems": [
        {"title": "Efficient Selection of Type Annotations for Performance", "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260305649L/abstract"},
        {"title": "Elixir 1.20 adds type inference, boosts compilation speed, and debuts new compiler options", "url": "https://alternativeto.net/news/2026/6/elixir-1-20-adds-type-inference-boosts-compilation-speed-and-debuts-new-compiler-options/"},
        {"title": "How to Evaluate the Performance of Gradual Type Systems", "url": "https://janvitek.org/pubs/jfp18.pdf"},
        {"title": "A Strategic Guide to Gradual Typing in Python", "url": "https://medium.com/@tihomir.manushev/a-strategic-guide-to-gradual-typing-in-python-49ac85f6dbdd"},
        {"title": "Design and Evaluation of Gradual Typing for Python", "url": "https://jsiek.github.io/home/dls28-vitousekA.pdf"},
    ],
    "functional-programming": [
        {"title": "All About Monads - HaskellWiki", "url": "https://wiki.haskell.org/All_About_Monads"},
        {"title": "A Gentle Introduction to Haskell: About Monads", "url": "https://www.haskell.org/tutorial/monads.html"},
        {"title": "Monads Tutorial — Monday Morning Haskell", "url": "https://mmhaskell.com/monads/tutorial"},
        {"title": "Making Sense of Monads - Monday Morning Haskell", "url": "https://academy.mondaymorninghaskell.com/p/making-sense-of-monads"},
        {"title": "Understanding Monads", "url": "https://nickx.hu/Monads.pdf"},
        {"title": "Monad tutorials timeline - Haskell", "url": "https://wiki.haskell.org/Monad_tutorials_timeline"},
        {"title": "Monad (functional programming) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Monad_(functional_programming)"},
    ],
    "algorithms": [
        {"title": "Data Structure I - LeetCode", "url": "https://leetcode.com/problem-list/m1b6ucdi/"},
        {"title": "Leetcode-Style Interviews | InterviewGuide.dev", "url": "https://interviewguide.dev/leetcode"},
        {"title": "NeetCode | Coding Interview Prep, Courses, Versus Mode", "url": "https://neetcode.io/"},
        {"title": "How to prepare for Data Structures & Algorithms interview in 2026", "url": "https://www.youtube.com/watch?v=jKGApDjRT6Y"},
        {"title": "59 Essential Searching Algorithms Interview Questions in 2026", "url": "https://github.com/Devinterview-io/searching-algorithms-interview-questions"},
        {"title": "DSA Syllabus: Full Course Curriculum 2026", "url": "https://www.wscubetech.com/blog/dsa-syllabus"},
        {"title": "The Ultimate Leetcode Roadmap: Data Structures & Algorithms Simplified", "url": "https://medium.com/@katravallicoding/the-ultimate-leetcode-roadmap-data-structures-algorithms-simplified-7564f84af829"},
    ],
    "python-internals": [
        {"title": "Python Internals: Memory Management & the Global Interpreter Lock (GIL)", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil"},
        {"title": "Memory Management in Python", "url": "https://www.honeybadger.io/blog/memory-management-in-python"},
        {"title": "Memory Management & GIL: Python Guide (2026)", "url": "https://www.edugators.com/python/advanced/python-memory-gil"},
        {"title": "Under the Hood of Python: Internals, Optimization, and Modern Features", "url": "https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features"},
        {"title": "Python Memory Management Internals", "url": "https://medium.com/@majidbasharat21/python-memory-management-internals-91d6077d6737"},
        {"title": "The Future of Python Internals: Exploring GIL Removal and Other Optimizations", "url": "https://developers-heaven.net/blog/the-future-of-python-internals-exploring-gil-removal-and-other-optimizations"},
        {"title": "The Evolution of Python's Memory Management", "url": "https://www.linkedin.com/pulse/evolution-pythons-memory-management-from-reference-counting-gupta-a95me"},
        {"title": "Memory Management in Python – Real Python", "url": "https://realpython.com/python-memory-management"},
    ],
}

def md5_hash(title, url):
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

# Group by wiki_page
wiki_page_entries = {}

for profile_name, results in all_results.items():
    profile = profiles['profiles'][profile_name]
    wiki_page = profile['wiki_page']
    existing_hashes = set(profile['last_result_hashes'])
    new_hashes = []
    
    for r in results:
        h = md5_hash(r['title'], r['url'])
        if h not in existing_hashes:
            existing_hashes.add(h)
            new_hashes.append(h)
            if wiki_page not in wiki_page_entries:
                wiki_page_entries[wiki_page] = []
            keywords = []
            title_lower = r['title'].lower()
            for st in profile['sub_topics']:
                if st.lower() in title_lower:
                    keywords.append(st)
            if not keywords:
                keywords = profile['sub_topics'][:2]
            kw_str = ', '.join(keywords[:3])
            entry = f"- **2026-06-11** | [{r['title']}]({r['url']}) | kw: {kw_str}"
            wiki_page_entries[wiki_page].append((profile_name, entry))
    
    updated = profile['last_result_hashes'] + new_hashes
    profiles['profiles'][profile_name]['last_result_hashes'] = updated[-20:]
    profiles['profiles'][profile_name]['last_run'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')

json.dump(profiles, open('/home/hermes/wiki/watch_profiles.json', 'w'), indent=2)

print("=== DEDUP RESULTS ===")
for wiki_page, entries in wiki_page_entries.items():
    print(f"\n{wiki_page}: {len(entries)} new entries")
    for pname, e in entries:
        print(f"  [{pname}] {e}")

json.dump({k: v for k, v in wiki_page_entries.items()}, open('/tmp/wiki_entries.json', 'w'))
