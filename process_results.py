import hashlib
import json
import os
from datetime import datetime, timezone

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    profiles = json.load(f)['profiles']

# Define search results (filtered for relevant ones)
search_results = {
    "system-design": [
        {"title": ".NET Microservices Design Patterns in 2026: A Production-Grade Guide", "url": "https://dev.to/vikrant_bagal_afae3e25ca7/net-microservices-design-patterns-in-2026-a-production-grade-guide-pid"},
        {"title": "The Complete System Design Roadmap for 2026", "url": "https://designgurus.substack.com/p/the-complete-system-design-roadmap"},
        {"title": "Modern Architecture Patterns (2026 Edition)", "url": "https://medium.com/@uchit86/modern-architecture-patterns-2026-edition-e526aeaf85d7"},
    ],
    "compilers": [
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 TurboFan", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "The LLVM Compiler Infrastructure Project", "url": "https://llvm.org/devmtg/2026-04/"},
        {"title": "Use of JIT compiler infrastructure at Apple and CERN", "url": "https://indico.cern.ch/event/1675931/"},
        {"title": "Perry - The Native TypeScript Compiler That Lowers TS Straight to LLVM", "url": "https://braindetox.kr/en/posts/perry_typescript_llvm_compiler_2026.html"},
        {"title": "Python JIT compiler may be removed", "url": "https://www.theregister.com/devops/2026/06/08/python-jit-compiler-may-be-removed/5252079"},
    ],
    "type-systems": [
        {"title": "Elixir v1.20 released: now a gradually typed language", "url": "https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/"},
        {"title": "Efficient Selection of Type Annotations for Performance Improvement in Gradual Typing", "url": "https://arxiv.org/abs/2603.05649"},
        {"title": "Type inference of all constructs and the next 15 months", "url": "https://elixir-lang.org/blog/2026/01/09/type-inference-of-all-and-next-15/"},
        {"title": "Efficient Selection of Type Annotations for Performance (Programming Conference)", "url": "https://programming-journal.org/2026/11/3/"},
    ],
    "functional-programming": [
        {"title": "Rust: Functional Programming & Monads", "url": "https://medium.com/coderhack-com/functional-programming-with-monads-90230ccccb48"},
        {"title": "Master Monads: Unlock Functional Programming's Secret Weapon", "url": "https://notes.suhaib.in/docs/tech/latest/monads-demystified-the-math-driven-superpower-behind-functional-programming/"},
    ],
    "algorithms": [
        {"title": "Top 50 Microsoft Array LeetCode Questions (2026)", "url": "https://www.hackmnc.com/blogs/microsoft-array-leetcode-questions"},
        {"title": "Top 30 Most Common Coupang LeetCode Interview Questions", "url": "https://www.vervecopilot.com/hot-blogs/coupang-leetcode-interview-questions"},
        {"title": "Bloomberg LP Software Engineer Interview Guide 2026", "url": "https://www.interviewquery.com/guides/bloomberg-lp-software-engineer"},
    ],
    "python-internals": [
        {"title": "How Python Works Under the Hood: Memory, GIL, and Bytecode", "url": "https://pythoncompiler.io/python/python-internals/"},
        {"title": "Advanced Python Internals: GIL, Multithreading", "url": "https://dev.to/aman_kumar_6d5d23b9b1ed02/advanced-python-internals-gil-multithreading-20mk"},
        {"title": "Disabling GIL in Python, How to use Python without GIL, NoGIL", "url": "https://hemachandra.hashnode.dev/disabling-gil-nogil-in-python"},
    ],
}

# Compute hashes and find new results
new_results = {}
all_hashes_used = {}

for profile_name, results in search_results.items():
    existing_hashes = set(profiles[profile_name]['last_result_hashes'])
    new_results[profile_name] = []
    for r in results:
        h = hashlib.md5(f"{r['title']}{r['url']}".encode('utf-8', errors='replace')).hexdigest()
        if h not in existing_hashes:
            new_results[profile_name].append({**r, 'hash': h})
            if profile_name not in all_hashes_used:
                all_hashes_used[profile_name] = []
            all_hashes_used[profile_name].append(h)

# Print summary
for p, results in new_results.items():
    print(f"{p}: {len(results)} new results")
    for r in results:
        print(f"  - {r['title'][:60]}... | {r['url'][:70]}")

# Save temp file
os.makedirs('/home/hermes/wiki/temp', exist_ok=True)
ts = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
with open(f'/home/hermes/wiki/temp/watch_run_{ts}.json', 'w') as f:
    json.dump({'results': {k: v for k, v in new_results.items()}, 'all_hashes_used': all_hashes_used}, f, indent=2)
print(f"\nSaved to temp/watch_run_{ts}.json")
