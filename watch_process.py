import json, hashlib, time, os

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)

profiles = profiles_data['profiles']

# All search results (manually aggregated from both batches)
all_results = {
    "system-design": [
        {"title": "The Coming Paradigm Shift in Distributed Systems Architecture", "url": "https://gabogil.com/2026/01/20/the-coming-paradigm-shift-in-distributed-systems-architecture"},
        {"title": "System Design Series Part 3: Load Balancing & Caching - Wasil Zafar", "url": "https://www.wasilzafar.com/pages/series/system-design/system-design-load-balancing-caching.html"},
        {"title": "System Design Building Blocks: Design Scalable Systems in 2026", "url": "https://www.systemdesignhandbook.com/blog/system-design-building-blocks"},
        {"title": "System Design Guide 2026: Load Balancing, Caching, CDN ...", "url": "https://onlinetools4free.com/research/system-design-guide-2026"},
        {"title": "Mastering Distributed Systems — Patterns & Principles (2026) | tutorialQ", "url": "https://tutorialq.com/dev/microservices/mastering-distributed-systems"},
        {"title": "System Architecture Design: The Complete Guide 2026", "url": "https://www.systemdesignhandbook.com/guides/system-architecture-design/"},
        {"title": "System Design Guide 2026 - Scalable Architecture Patterns", "url": "https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf"},
        {"title": "Distributed Systems Best Practices | 2026 - docs.gitscrum.com", "url": "https://docs.gitscrum.com/en/best-practices/distributed-systems-architecture-patterns"},
        {"title": "10 Essential Distributed System Design Patterns for Scalable Apps", "url": "https://netalith.com/blogs/system-design/distributed-system-design-patterns-scalable-applications"},
    ],
    "compilers": [
        {"title": "JIT Compilation | microsoft/llvm | DeepWiki", "url": "https://deepwiki.com/microsoft/llvm/4-jit-compilation"},
        {"title": "Just-In-Time (JIT) Compiler with LLVM - Create Your Own Programming Language with Rust", "url": "https://createlang.rs/01_calculator/jit_intro.html"},
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 ...", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at ...", "url": "https://github.com/VALancaster/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at ...", "url": "https://github.com/Georghinho/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "Resume - Sanjoy Das", "url": "http://playingwithpointers.com/resume.html"},
        {"title": "Announcing an Open Source LLVM toolchain for Snapdragon CPUs and MCUs", "url": "https://www.qualcomm.com/developer/blog/2026/04/announcing-an-open-source-llvm-toolchain-for-snapdragon-cpus-mcus"},
        {"title": "LLVM Weekly - #648, June 1st 2026", "url": "https://llvmweekly.org/issue/648"},
        {"title": "LLVM - Wikipedia", "url": "https://en.wikipedia.org/wiki/LLVM"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at ...", "url": "https://github.com/RomanPikhotskiy/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
    ],
    "type-systems": [
        {"title": "Efficient Selection of Type Annotations for Performance Improvement in Gradual Typing", "url": "https://2026.programming-conference.org/details/programming-2026-papers/7/Efficient-Selection-of-Type-Annotations-for-Performance-Improvement-in-Gradual-Typing"},
        {"title": "Navigating the 2026 Language Landscape: A Typing and Paradigm Matrix - PookieTech Blog", "url": "https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix"},
        {"title": "Gradual Typing as if Types Mattered - wgt20.irif.fr", "url": "https://wgt20.irif.fr/wgt20-final28-acmpaginated.pdf"},
        {"title": "Type system concepts — typing documentation", "url": "https://typing.python.org/en/latest/spec/concepts.html"},
        {"title": "Gradual Typing in Type Theory - numberanalytics.com", "url": "https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory"},
        {"title": "Design and Evaluation of Gradual Typing for Python", "url": "https://jsiek.github.io/home/dls28-vitousekA.pdf"},
        {"title": "The Rise of Static Typing - Why It Has Been Back Since the Mid-2010s 2026 - BrainDetox", "url": "https://braindetox.kr/en/posts/static_typing_rise_2026.html"},
        {"title": "On the cost of type-tag soundness - ACM Digital Library", "url": "http://dl.acm.org/doi/10.1145/3162066"},
        {"title": "Type-Based Gradual Typing Performance Optimization | Proceedings of the ACM on Programming Languages", "url": "https://dl.acm.org/doi/10.1145/3632931"},
        {"title": "Toward a Corpus Study of the Dynamic Gradual Type - arXiv.org", "url": "https://arxiv.org/html/2503.08928"},
    ],
    "functional-programming": [
        {"title": "Does Rust Support Functional Programming Idioms? Exploring ...", "url": "https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms/"},
        {"title": "Functional Programming in 2026: Haskell vs. Gleam vs. Rust", "url": "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust"},
        {"title": "The Practical Value of Functional Programming — Monad ...", "url": "https://www.youngju.dev/blog/culture/2026-04-15-functional-programming-monad-haskell-elixir-erlang-gleam-effect-ts-practical-value-deep-dive-guide-2025.en"},
        {"title": "How I Learned Monads: Not Through Haskell But Through Rust", "url": "https://medium.com/@saehwanpark/how-i-learned-monads-not-through-haskell-but-through-rust-f4233f7779c7"},
        {"title": "Rust vs Haskell. Two Languages That Both Want to ... - Medium", "url": "https://medium.com/rustaceans/rust-vs-haskell-22d581f2686d"},
        {"title": "Monads are Omnipresent in Rust - bertiqwerty", "url": "https://www.bertiqwerty.com/en/posts/monad"},
        {"title": "Haskell Guide [2026]: Functional Programming That Changes How ...", "url": "https://precisionaiacademy.com/blog/haskell-guide-2026"},
        {"title": "Monad (functional programming) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Monad_%28functional_programming%29"},
    ],
    "algorithms": [
        {"title": "Problem List - LeetCode", "url": "http://leetcode.com/company/amazon"},
        {"title": "Best DSA Sheet 2026 | To Crack Interviews - namastedev.com", "url": "https://namastedev.com/namaste-dsa-sheet"},
        {"title": "LeetCode - The World's Leading Online Programming ...", "url": "https://leetcode.com/problemset/javascript"},
        {"title": "Algorithms & Data Structures (LeetCode Preparation) | ArchMan", "url": "https://archman.dev/docs/algorithms-and-data-structures"},
        {"title": "Top Google Questions - LeetCode", "url": "https://leetcode.com/problem-list/7p55wqm"},
        {"title": "snehasishroy/leetcode-companywise-interview-questions", "url": "https://github.com/snehasishroy/leetcode-companywise-interview-questions"},
        {"title": "Data Structures & Algorithms Roadmap 2026 - Complete Learning ...", "url": "https://www.thetutorbridge.com/roadmap/dsa"},
        {"title": "ChunhThanhDe/Leetcode-Top-Interview", "url": "https://github.com/ChunhThanhDe/Leetcode-Top-Interview"},
    ],
    "python-internals": [
        {"title": "How Python Works Under the Hood: Memory, GIL, and Bytecode", "url": "https://www.pythoncompiler.io/python/python-internals"},
        {"title": "Under the Hood of Python: Internals, Optimization, and Modern Features", "url": "https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features"},
        {"title": "Python - Python Internals: Memory Management & the Global ...", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil"},
        {"title": "Memory Management & GIL: Python Guide (2026) | Edugators", "url": "https://www.edugators.com/python/advanced/python-memory-gil"},
        {"title": "Python Memory Profiling and Optimization Techniques", "url": "https://dasroot.net/posts/2026/04/python-memory-profiling-optimization-techniques"},
        {"title": "State of Python 2026 | The Dev Newsletter", "url": "https://devnewsletter.com/p/state-of-python-2026"},
        {"title": "Python's GIL Is Gone — What That Actually Means for Your Code", "url": "https://python.plainenglish.io/pythons-gil-is-gone-what-that-actually-means-for-your-code-8ac535b5d879"},
        {"title": "The Python GIL Controversy: Why Multi-Core Parallelism Remains Broken", "url": "https://www.javacodegeeks.com/2026/01/the-python-gil-controversy-why-multi-core-parallelism-remains-broken-and-why-it-might-not-matter.html"},
        {"title": "01_Advanced_Memory_GIL.md - GitHub", "url": "https://github.com/AmanDevNet/AI_ML_Interview_Prep/blob/main/Python_Revision_Handbook/Phase3/01_Advanced_Memory_GIL.md"},
        {"title": "CPython Internals Explained by Ethan Garrett on Apple Books", "url": "https://books.apple.com/us/book/cpython-internals-explained/id6776812050"},
    ],
}

# Compute hashes and find new results
new_by_profile = {}
all_hashes_by_profile = {}

for profile_name, results in all_results.items():
    existing_hashes = set(profiles[profile_name].get('last_result_hashes', []))
    new_results = []
    all_hashes = []
    
    for r in results:
        h = hashlib.md5(f"{r['title']}{r['url']}".encode('utf-8', errors='replace')).hexdigest()
        all_hashes.append(h)
        if h not in existing_hashes:
            r['hash'] = h
            new_results.append(r)
    
    new_by_profile[profile_name] = new_results
    all_hashes_by_profile[profile_name] = all_hashes

# Print summary
print("=== DEDUPLICATION RESULTS ===")
total_new = 0
for profile_name, new_results in new_by_profile.items():
    total_new += len(new_results)
    print(f"\n{profile_name}: {len(new_results)} new results")
    for r in new_results:
        print(f"  + {r['title'][:70]}")
        print(f"    {r['url'][:80]}")

print(f"\n=== TOTAL NEW: {total_new} ===")

# Group by wiki page
wiki_updates = {}
for profile_name, new_results in new_by_profile.items():
    if not new_results:
        continue
    wiki_page = profiles[profile_name]['wiki_page']
    if wiki_page not in wiki_updates:
        wiki_updates[wiki_page] = {'entries': [], 'profiles': []}
    for r in new_results:
        wiki_updates[wiki_page]['entries'].append(r)
    wiki_updates[wiki_page]['profiles'].append(profile_name)

print(f"\n=== WIKI PAGE UPDATES ===")
for page, info in wiki_updates.items():
    print(f"{page}: {len(info['entries'])} entries from {info['profiles']}")

# Step 5: Update wiki pages using Python I/O
now_str = time.strftime('%Y-%m-%d')
for wiki_page, info in wiki_updates.items():
    page_path = f'/home/hermes/wiki/entities/{wiki_page}'
    if not os.path.exists(page_path):
        # Create the file with basic structure
        with open(page_path, 'w') as f:
            f.write(f'# {wiki_page.replace(".md", "").replace("-", " ").title()}\n\n## Updates\n\n')
        print(f"Created new wiki page: {page_path}")
    
    with open(page_path, 'r') as f:
        content = f.read()
    lines = content.split('\n')
    
    # Build new entries
    new_entries = []
    for r in info['entries']:
        entry = f"- **{now_str}** | [{r['title']}]({r['url']}) | kw: {r['title'].split()[0].lower()}"
        new_entries.append(entry)
    
    # Find FIRST ## Updates and insert after it
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is not None:
        lines = lines[:insert_after] + new_entries + [''] + lines[insert_after:]
        with open(page_path, 'w') as f:
            f.write('\n'.join(lines))
        print(f"Updated {wiki_page}: inserted {len(new_entries)} entries")

# Step 6: Update watch_profiles.json
now_utc = time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())
for profile_name, new_results in new_by_profile.items():
    if not new_results:
        profiles[profile_name]['last_run'] = now_utc
        continue
    
    existing_hashes = profiles[profile_name].get('last_result_hashes', [])
    new_hashes = [r['hash'] for r in new_results]
    updated_hashes = new_hashes + existing_hashes
    # Keep max 20
    profiles[profile_name]['last_result_hashes'] = updated_hashes[:20]
    profiles[profile_name]['last_run'] = now_utc

# Add discovered sub-topics
for profile_name, new_results in new_by_profile.items():
    for r in new_results:
        title_words = r['title'].replace('-', ' ').replace(':', '').split()
        for word in title_words:
            if len(word) > 3 and word not in profiles[profile_name].get('sub_topics', []):
                profiles[profile_name]['sub_topics'].append(word)

profiles_data['last_run'] = now_utc
profiles_data['profiles'] = profiles

with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)
print(f"\nUpdated watch_profiles.json at {now_utc}")

# Save temp run file
timestamp = int(time.time())
with open(f'/home/hermes/wiki/temp/watch_run_{timestamp}.json', 'w') as f:
    json.dump({"timestamp": now_utc, "results": all_results, "new_by_profile": {k: [{'title': r['title'], 'url': r['url'], 'hash': r['hash']} for r in v] for k, v in new_by_profile.items()}}, f, indent=2)
print(f"Saved run to watch_run_{timestamp}.json")
