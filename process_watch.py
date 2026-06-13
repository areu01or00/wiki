import json, hashlib, time, os

os.chdir('/home/hermes/wiki')

# Load profiles
with open('watch_profiles.json') as f:
    data = json.load(f)
profiles = data['profiles']

# All search results from both batches
all_results = {
    "system-design": [
        {"title": "System Design Guide 2026 - Scalable Architecture Patterns", "url": "https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf"},
        {"title": "Distributed Systems | Architecture Patterns · GitScrum Docs", "url": "https://docs.gitscrum.com/en/best-practices/distributed-systems-architecture-patterns"},
        {"title": "Microservices Architecture Patterns in 2026: Mastering Distributed Systems Design", "url": "https://www.andrewhansen.au/microservices-architecture-patterns-in-2026-mastering-distributed-systems-design"},
        {"title": "Distributed Systems Roadmap (2026) | The Design Round", "url": "https://thedesignround.com/distributed-systems-roadmap"},
        {"title": "System Design Patterns: The Complete Guide 2026", "url": "https://www.systemdesignhandbook.com/guides/system-design-patterns"},
    ],
    "compilers": [
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 Turbofan, Maglev", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "Just-In-Time (JIT) Compiler with LLVM - Create Your Own Programming Language", "url": "https://createlang.rs/01_calculator/jit_intro.html"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst", "url": "https://github.com/VALancaster/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "JIT Compilation | microsoft/llvm | DeepWiki", "url": "https://deepwiki.com/microsoft/llvm/4-jit-compilation"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at course-spring-2026", "url": "https://github.com/chekalexey/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
    ],
    "type-systems": [
        {"title": "Type system concepts — typing documentation", "url": "https://typing.python.org/en/latest/spec/concepts.html"},
        {"title": "Efficient Selection of Type Annotations for Performance Improvement of Gradual Typing", "url": "https://programming-journal.org/2026/11/3"},
        {"title": "Navigating the 2026 Language Landscape: A Typing and Paradigm Matrix", "url": "https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix"},
        {"title": "Gradual Typing in Type Theory", "url": "https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory"},
        {"title": "The Rise of Static Typing - Why It Has Been Back Since the Mid-2010s 2026", "url": "https://braindetox.kr/en/posts/static_typing_rise_2026.html"},
    ],
    "functional-programming": [
        {"title": "Functional Programming in 2026: Haskell vs. Gleam vs. Rust", "url": "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust"},
        {"title": "Bean Exchange", "url": "http://spot.bean.exchange/"},
        {"title": "The Practical Value of Functional Programming — Monad ...", "url": "https://www.youngju.dev/blog/culture/2026-04-15-functional-programming-monad-haskell-elixir-erlang-gleam-effect-ts-practical-value-deep-dive-guide-2025.en"},
        {"title": "How I Learned Monads: Not Through Haskell But Through Rust | by Sae-Hwan Park | Medium", "url": "https://medium.com/@saehwanpark/how-i-learned-monads-not-through-haskell-but-through-rust-f4233f7779c7"},
        {"title": "Monads are Omnipresent in Rust - bertiqwerty", "url": "https://www.bertiqwerty.com/en/posts/monad"},
    ],
    "algorithms": [
        {"title": "Best DSA Sheet 2026 | To Crack Interviews - namastedev.com", "url": "https://namastedev.com/namaste-dsa-sheet"},
        {"title": "Data Structures & Algorithms Roadmap 2026 - Complete Learning Path | The Tutor Bridge", "url": "https://www.thetutorbridge.com/roadmap/dsa"},
        {"title": "NeetCode | Coding Interview Prep, Courses, Versus Mode", "url": "https://neetcode.io/"},
        {"title": "Algorithms & Data Structures (LeetCode Preparation) | ArchMan", "url": "https://archman.dev/docs/algorithms-and-data-structures"},
        {"title": "Data structures and algorithms study cheatsheets for coding interviews | Tech Interview Handbook", "url": "https://www.techinterviewhandbook.org/algorithms/study-cheatsheet"},
    ],
    "python-internals": [
        {"title": "How Python Works Under the Hood: Memory, GIL, and Bytecode", "url": "https://www.pythoncompiler.io/python/python-internals"},
        {"title": "Memory Management & GIL: Python Guide (2026) | Edugators", "url": "https://www.edugators.com/python/advanced/python-memory-gil"},
        {"title": "Python - Python Internals: Memory Management & the Global Interpreter Lock (GIL) | eVidhya", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil"},
        {"title": "Exploring Python: Internals and Optimization", "url": "https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features"},
        {"title": "Python's GIL Is Gone — What That Actually Means for Your Code", "url": "https://python.plainenglish.io/pythons-gil-is-gone-what-that-actually-means-for-your-code-8ac535b5d879"},
    ],
}

def compute_hash(title, url):
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

# Process each profile
new_entries_by_page = {}
new_hashes_by_profile = {}
digest = {}

for profile_name, results in all_results.items():
    profile = profiles[profile_name]
    existing_hashes = set(profile.get("last_result_hashes", []))
    new_hashes = []
    new_results = []
    
    for r in results:
        h = compute_hash(r["title"], r["url"])
        if h not in existing_hashes:
            new_hashes.append(h)
            new_results.append(r)
            existing_hashes.add(h)
    
    new_hashes_by_profile[profile_name] = new_hashes
    digest[profile_name] = new_results
    
    wiki_page = profile["wiki_page"]
    if wiki_page not in new_entries_by_page:
        new_entries_by_page[wiki_page] = []
    
    today = time.strftime("%Y-%m-%d")
    for r in new_results:
        entry = f"- **{today}** | [{r['title']}]({r['url']}) | {profile_name}"
        new_entries_by_page[wiki_page].append(entry)

# Print summary
print("=== Deduplication Summary ===")
for profile_name, hashes in new_hashes_by_profile.items():
    print(f"{profile_name}: {len(hashes)} new results")
print()
print("=== Wiki Page Updates ===")
for page, entries in new_entries_by_page.items():
    print(f"{page}: {len(entries)} entries")
    for e in entries:
        print(f"  {e}")
print()

# Update wiki pages using Python I/O
for wiki_page, entries in new_entries_by_page.items():
    if not entries:
        continue
    filepath = f"entities/{wiki_page}"
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
    
    if insert_after is None:
        print(f"WARNING: No '## Updates' found in {filepath}")
        continue
    
    new_block = entries + ['']
    lines = lines[:insert_after] + new_block + lines[insert_after:]
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))
    print(f"Updated {filepath} with {len(entries)} entries")

# Update watch_profiles.json
now_str = time.strftime("%Y-%m-%d %H:%M UTC")
for profile_name, new_hashes in new_hashes_by_profile.items():
    if not new_hashes:
        profiles[profile_name]["last_run"] = now_str
        continue
    
    existing = profiles[profile_name].get("last_result_hashes", [])
    existing.extend(new_hashes)
    profiles[profile_name]["last_result_hashes"] = existing[-20:]
    profiles[profile_name]["last_run"] = now_str

with open('watch_profiles.json', 'w') as f:
    json.dump(data, f, indent=2)
print("\nUpdated watch_profiles.json")

# Save digest
with open('temp/last_digest.json', 'w') as f:
    json.dump(digest, f, indent=2)
print("Saved digest data")
