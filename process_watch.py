import hashlib, json, os, time
from datetime import datetime, timezone

timestamp = int(time.time())
utc_now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

with open('watch_profiles.json') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

search_results = {
    'system-design': [
        {'title': 'Top 10 Software Architecture Patterns to Follow in 2026', 'url': 'https://www.moontechnolabs.com/blog/software-architecture-patterns'},
        {'title': '10 Software Architecture Patterns Engineers Need in 2026', 'url': 'https://blog.patoliyainfotech.com/software-architecture-patterns-guide'},
        {'title': 'System Design Guide 2026: Load Balancing, Caching, CDN, Databases, Message Queues, Scaling', 'url': 'https://onlinetools4free.com/research/system-design-guide-2026'},
        {'title': 'System Design Guide 2026 - Scalable Architecture Patterns', 'url': 'https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf'},
        {'title': 'System Design Series Part 3: Load Balancing & Caching - Wasil Zafar', 'url': 'https://www.wasilzafar.com/pages/series/system-design/system-design-load-balancing-caching.html'},
    ],
    'compilers': [
        {'title': 'Compilers and Modern Language Runtimes', 'url': 'https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en'},
        {'title': 'JIT Compilation | microsoft/llvm | DeepWiki', 'url': 'https://deepwiki.com/microsoft/llvm/4-jit-compilation'},
        {'title': 'Just-In-Time (JIT) Compiler with LLVM - Create Your Own Programming Language with Rust', 'url': 'https://createlang.rs/01_calculator/jit_intro.html'},
        {'title': 'ML Compiler Optimization Revolution [Deep Dive] [2026]', 'url': 'https://techbytes.app/posts/ml-compiler-optimization-revolution-2026/'},
    ],
    'type-systems': [
        {'title': 'Efficient Selection of Type Annotations for Performance', 'url': 'https://programming-journal.org/2026/11/3'},
        {'title': 'The Rise of Static Typing - Why It Has Been Back Since the Mid-2010s 2026', 'url': 'https://braindetox.kr/en/posts/static_typing_rise_2026.html'},
        {'title': 'Type system concepts - typing documentation', 'url': 'https://typing.python.org/en/latest/spec/concepts.html'},
        {'title': 'Navigating the 2026 Language Landscape: A Typing and Paradigm Matrix', 'url': 'https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix'},
        {'title': 'Gradual Typing in Type Theory', 'url': 'https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory'},
    ],
    'functional-programming': [
        {'title': 'Haskell Guide [2026]: Functional Programming That Changes How You Think', 'url': 'https://precisionaiacademy.com/blog/haskell-guide-2026'},
        {'title': 'Functional Programming in 2026: Haskell vs. Gleam vs. Rust', 'url': 'https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust'},
        {'title': 'Does Rust Support Functional Programming Idioms? Exploring Filter/Map/Reduce, Monads, and Syntactic Sugar', 'url': 'https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms'},
        {'title': 'Monads are Omnipresent in Rust', 'url': 'https://www.bertiqwerty.com/en/posts/monad'},
        {'title': 'How I Learned Monads: Not Through Haskell But Through Rust', 'url': 'https://medium.com/@saehwanpark/how-i-learned-monads-not-through-haskell-but-through-rust-f4233f7779c7'},
    ],
    'algorithms': [
        {'title': 'DSA Practice - Interview Questions - workat.tech', 'url': 'https://workat.tech/problem-solving/practice/topics'},
        {'title': 'Best DSA Sheet 2026 | To Crack Interviews - namastedev.com', 'url': 'https://namastedev.com/namaste-dsa-sheet'},
        {'title': 'Data structures and algorithms study cheatsheets for coding interviews', 'url': 'https://www.techinterviewhandbook.org/algorithms/study-cheatsheet'},
        {'title': 'How to Prepare for a Coding Interview: The Complete LeetCode Study Plan', 'url': 'https://careerlift.ai/blog/how-to-prepare-coding-interview-leetcode-study-plan'},
        {'title': 'NeetCode | Coding Interview Prep, Courses, Versus Mode', 'url': 'https://neetcode.io/'},
    ],
    'python-internals': [
        {'title': 'The Python GIL Controversy: Why Multi-Core Parallelism Remains Broken', 'url': 'https://www.javacodegeeks.com/2026/01/the-python-gil-controversy-why-multi-core-parallelism-remains-broken-and-why-it-might-not-matter.html'},
        {'title': 'How Python Works Under the Hood: Memory, GIL, and Bytecode', 'url': 'https://www.pythoncompiler.io/python/python-internals'},
        {'title': 'Under the Hood of Python: Internals, Optimization, and Modern Features', 'url': 'https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features'},
        {'title': 'Python - Python Internals: Memory Management & the Global Interpreter Lock (GIL)', 'url': 'https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil'},
        {'title': 'Memory Management & GIL: Python Guide (2026) | Edugators', 'url': 'https://www.edugators.com/python/advanced/python-memory-gil'},
    ],
}

def compute_hash(title, url):
    return hashlib.md5(f'{title}{url}'.encode('utf-8', errors='replace')).hexdigest()

new_results_by_profile = {}
all_new_hashes = {}
total_new = 0

for profile_name, results in search_results.items():
    existing_hashes = set(profiles[profile_name]['last_result_hashes'])
    new_results = []
    new_hashes = []
    for r in results:
        h = compute_hash(r['title'], r['url'])
        if h not in existing_hashes:
            new_results.append(r)
            new_hashes.append(h)
            existing_hashes.add(h)
    new_results_by_profile[profile_name] = new_results
    all_new_hashes[profile_name] = new_hashes
    total_new += len(new_results)
    print(f'Profile {profile_name}: {len(new_results)} new out of {len(results)}')

print(f'Total new: {total_new}')

# Save batch file
batch_data = {'timestamp': utc_now, 'new_results': new_results_by_profile, 'new_hashes': all_new_hashes}
with open(f'temp/watch_run_{timestamp}.json', 'w') as f:
    json.dump(batch_data, f, indent=2)
print(f'Saved to temp/watch_run_{timestamp}.json')
