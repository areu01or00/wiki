import hashlib, json, time, datetime, os, re

timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
today = datetime.datetime.utcnow().strftime('%Y-%m-%d')

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json') as f:
    profiles = json.load(f)['profiles']

# All search results organized by profile
all_results = {
    "system-design": [
        {"title": "The Coming Paradigm Shift in Distributed Systems Architecture", "url": "https://gabogil.com/2026/01/20/the-coming-paradigm-shift-in-distributed-systems-architecture"},
        {"title": "The Complete Guide to System Design in 2026 AI-Native and Serverless", "url": "https://dev.to/devin-rosario/the-complete-guide-to-system-design-in-2026-ai-native-and-serverless-1kpb"},
        {"title": "Mastering Distributed Systems — Patterns & Principles (2026)", "url": "https://tutorialq.com/dev/microservices/mastering-distributed-systems"},
        {"title": "The 7 Architecture Patterns Every IT Head Should Revisit in 2026", "url": "https://www.linkedin.com/pulse/7-architecture-patterns-every-head-should-revisit-2026-b5y3f"},
        {"title": "Distributed Systems Architecture in Java: A Complete Hands-On Reference", "url": "https://medium.com/@devarshivyas/distributed-systems-architecture-in-java-a-complete-hands-on-reference-bca66da1e41a"},
    ],
    "compilers": [
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 Turbofan Maglev", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "Best Free Open-Source Compilers in 2026", "url": "https://www.analyticsinsight.net/programming/best-free-and-open-source-compilers-for-developers-in-2026"},
        {"title": "The Future of Programming: Compiler Writing in 2026", "url": "https://artikls.com/article/future-programming-compiler-writing-2026"},
        {"title": "Sanjoy Das - Deep Learning Compilers at NVIDIA", "url": "http://sanjoy.link/"},
        {"title": "The Case For Compilers: A Look at SPEC CPU 2026 on LLVM 22", "url": "https://www.servethehome.com/the-case-for-compilers-a-look-at-spec-cpu-2026-on-llvm-22/"},
    ],
    "type-systems": [
        {"title": "Gradual type inference research papers", "url": "https://scholar.google.com/scholar?as_sdt=0&as_vis=1&hl=en&oi=scholart&q=gradual+type+inference+research+papers"},
        {"title": "Type system concepts — typing documentation", "url": "https://typing.python.org/en/latest/spec/concepts.html"},
        {"title": "Efficient Selection of Type Annotations for Performance Improvement in Gradual Typing", "url": "https://2026.programming-conference.org/details/programming-2026-papers/7/Efficient-Selection-of-Type-Annotations-for-Performance-Improvement-in-Gradual-Typing"},
        {"title": "Gradual Typing with Inference", "url": "https://www.cs.cmu.edu/~aldrich/FOOL/fool08/siek-slides.pdf"},
        {"title": "Gradual Liquid Type Inference", "url": "https://nikivazou.github.io/static/oopsla18main-p124-p.pdf"},
    ],
    "functional-programming": [
        {"title": "Understanding Monads — From types to categories to analogy", "url": "https://nickx.hu/Monads.pdf"},
        {"title": "Making Sense of Monads - Monday Morning Haskell", "url": "https://academy.mondaymorninghaskell.com/p/making-sense-of-monads"},
        {"title": "Monad (functional programming) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Monad_%28functional_programming%29"},
        {"title": "A Gentle Introduction to Haskell: About Monads", "url": "https://www.haskell.org/tutorial/monads.html"},
        {"title": "All About Monads - HaskellWiki", "url": "https://wiki.haskell.org/All_About_Monads"},
    ],
    "algorithms": [
        {"title": "Top 100 LeetCode Coding Interview Questions (2025 Edition)", "url": "https://www.shadecoder.com/blogs/top-100-leetcode-coding-interview-questions-%282025-edition%29"},
        {"title": "Data Structure I - LeetCode", "url": "https://leetcode.com/problem-list/m1b6ucdi/"},
        {"title": "NeetCode | Coding Interview Prep, Courses, Versus Mode", "url": "https://neetcode.io/"},
        {"title": "Top Interview 150 - Study Plan - LeetCode", "url": "https://leetcode.com/studyplan/top-interview-150/"},
        {"title": "60 LeetCode problems to solve for coding interview", "url": "https://medium.com/%40koheiarai94/60-leetcode-questions-to-prepare-for-coding-interview-8abbb6af589e"},
    ],
    "python-internals": [
        {"title": "Python Internals: Memory Management & the Global Interpreter Lock (GIL)", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil"},
        {"title": "Memory Management & GIL: Python Guide (2026)", "url": "https://www.edugators.com/python/advanced/python-memory-gil"},
        {"title": "What is the GIL in Python and Why Should You Care?", "url": "https://dev.to/imsushant12/what-is-the-gil-in-python-and-why-should-you-care-1cai"},
        {"title": "The Future of Python Internals: Exploring GIL Removal and Other Optimizations", "url": "https://developers-heaven.net/blog/the-future-of-python-internals-exploring-gil-removal-and-other-optimizations"},
        {"title": "The Evolution of Python's Memory Management", "url": "https://www.linkedin.com/pulse/evolution-pythons-memory-management-from-reference-counting-gupta-a95me"},
    ],
}

def md5(text):
    return hashlib.md5(text.encode('utf-8', errors='replace')).hexdigest()

# Compute hashes and deduplicate per profile
new_results = {}
new_hashes = {}

for profile_name, results in all_results.items():
    existing = set(profiles[profile_name]['last_result_hashes'])
    new_items = []
    all_new = []
    for r in results:
        h = md5(f"{r['title']}{r['url']}")
        if h not in existing:
            new_items.append({**r, 'hash': h})
            all_new.append(h)
    new_results[profile_name] = new_items
    new_hashes[profile_name] = all_new

# Group by wiki_page
wiki_updates = {}
for profile_name, items in new_results.items():
    if not items:
        continue
    wp = profiles[profile_name]['wiki_page']
    if wp not in wiki_updates:
        wiki_updates[wp] = []
    for item in items:
        entry = f"- **{today}** | [{item['title']}]({item['url']}) | {profile_name}"
        wiki_updates[wp].append(entry)

print("=== NEW RESULTS BY PROFILE ===")
for p, items in new_results.items():
    print(f"  {p}: {len(items)} new")
    for i in items:
        print(f"    - {i['title'][:70]}")
        print(f"      hash: {i['hash']}")

print("\n=== WIKI PAGES TO UPDATE ===")
for wp, entries in wiki_updates.items():
    print(f"  {wp}: {len(entries)} entries")

# Save data for next steps
with open('/tmp/wiki_watch_data.json', 'w') as f:
    json.dump({
        'new_results': new_results,
        'new_hashes': new_hashes,
        'wiki_updates': wiki_updates,
        'profiles': profiles,
    }, f)

print("\nData saved to /tmp/wiki_watch_data.json")
