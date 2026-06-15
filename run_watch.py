import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
timestamp = now.strftime('%Y-%m-%d %H:%M UTC')
date_str = now.strftime('%Y-%m-%d')

# All search results organized by profile
search_data = {
    "system-design": [
        {"title": "Emerging Backend Architectures for 2026: Microservices, Serverless & Edge Computing", "url": "https://tensorblue.com/blog/emerging-backend-architectures-for-2026-microservices-serverless-and-beyond"},
        {"title": "System Design Guide 2026 - Scalable Architecture Patterns", "url": "https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf"},
        {"title": "System Design Series Part 3: Load Balancing & Caching - Wasil Zafar", "url": "https://www.wasilzafar.com/pages/series/system-design/system-design-load-balancing-caching.html"},
        {"title": "Distributed Systems | Architecture Patterns - GitScrum Docs", "url": "https://docs.gitscrum.com/en/best-practices/distributed-systems-architecture-patterns"},
        {"title": "System Design Guide 2026: Load Balancing, Caching, CDN, Databases, Message Queues, Scaling - OnlineTools4Free Research", "url": "https://onlinetools4free.com/research/system-design-guide-2026"},
        {"title": "Patterns of Distributed Systems: Complete Roadmap | Chanh Le", "url": "https://chanhle.dev/en/blog/patterns-of-distributed-systems-roadmap"},
        {"title": "Distributed System Design: the complete guide to building", "url": "https://grokkingthesystemdesign.com/guides/distributed-system-design"},
        {"title": "Microservices Architecture Patterns in 2026: Mastering", "url": "https://www.andrewhansen.au/microservices-architecture-patterns-in-2026-mastering-distributed-systems-design"},
        {"title": "State of the Art in Parallel and Distributed Systems: Emerging Trends and Challenges", "url": "https://www.mdpi.com/2079-9292/14/4/677"},
        {"title": "Microservices Design Patterns: The Comprehensive Architectural Guide", "url": "https://netalith.com/blogs/microservices-architecture/microservices-design-patterns-guide-2026"},
    ],
    "compilers": [
        {"title": "Unlocking Performance: The Overlooked Power of Low-Cost", "url": "https://thecodersblog.com/low-compilation-cost-register-allocation-in-llvm-based-binary-translation-2026"},
        {"title": "Just-In-Time (JIT) Compiler with LLVM - Create Your Own", "url": "https://createlang.rs/01_calculator/jit_intro.html"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at course-spring-2026 - RomanPikhotskiy/compiler-course-2026", "url": "https://github.com/RomanPikhotskiy/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst", "url": "https://github.com/VALancaster/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "Compilers and Modern Language Runtimes - LLVM, JIT, GC, V8", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at course-spring-2026 - chekalexey/compiler-course-2026", "url": "https://github.com/chekalexey/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "PEP 744 - JIT Compilation", "url": "https://peps.python.org/pep-0744/"},
        {"title": "Jeandle: How Ant Group LLVM-Based JVM JIT Aims to Supercharge Java", "url": "https://www.besthub.dev/articles/jeandle-how-ant-group-s-llvm-based-jvm-jit-aims-to-supercharge-java-991748738e77"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT3.rst", "url": "https://github.com/4elodoy-Molovek/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT3.rst"},
        {"title": "AI-Compiler Prompt Engineering: 2026 Cheat Sheet Deep Dive", "url": "https://techbytes.app/posts/ai-compiler-prompt-engineering-2026-cheat-sheet"},
    ],
    "type-systems": [
        {"title": "Gradual Typing in Type Theory - numberanalytics.com", "url": "https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory"},
        {"title": "Navigating the Language Labyrinth: A 2026 Matrix Analysis of Typing and Paradigms - PookieTech Blog", "url": "https://pookietech.com.ng/blog/navigating-the-language-labyrinth-a-2026-matrix-analysis-of-typing-and-paradigms"},
        {"title": "Gradual Typing as if Types Mattered", "url": "https://wgt20.irif.fr/wgt20-final28-acmpaginated.pdf"},
        {"title": "Efficient Selection of Type Annotations for Performance", "url": "https://programming-journal.org/2026/11/3/"},
        {"title": "Navigating the 2026 Language Landscape: A Typing and Paradigm Matrix - PookieTech Blog", "url": "https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix"},
        {"title": "The Rise of Static Typing - Why It Has Been Back Since the Mid-2010s 2026 - BrainDetox", "url": "https://braindetox.kr/en/posts/static_typing_rise_2026.html"},
        {"title": "Gradual typing - Wikipedia", "url": "https://en.wikipedia.org/wiki/Gradual_typing"},
        {"title": "PEAK-System Forum - Index page", "url": "https://forum.peak-system.com/"},
        {"title": "The Ins and Outs of Gradual Type Inference", "url": "https://www.microsoft.com/en-us/research/wp-content/uploads/2017/08/grad_ti1.pdf"},
        {"title": "301 Moved Permanently", "url": "https://www.peak-system.com/de"},
    ],
    "functional-programming": [
        {"title": "Functional Programming at Its Finest: Why Haskell Developers", "url": "https://pctechmag.com/2026/05/functional-programming-at-its-finest-why-haskell-developers-bring-unmatched-code-reliability"},
        {"title": "Functional Programming in 2026: Haskell vs. Gleam vs. Rust", "url": "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust"},
        {"title": "How I Learned Monads: Not Through Haskell But Through Rust", "url": "https://medium.com/@saehwanpark/how-i-learned-monads-not-through-haskell-but-through-rust-f4233f7779c7"},
        {"title": "The Practical Value of Functional Programming - Monad, Functor, Pure Functions, Haskell, Erlang/Elixir, Gleam, Effect-TS", "url": "https://www.youngju.dev/blog/culture/2026-04-15-functional-programming-monad-haskell-elixir-erlang-gleam-effect-ts-practical-value-deep-dive-guide-2025.en"},
        {"title": "Monads are Omnipresent in Rust - bertiqwerty", "url": "https://www.bertiqwerty.com/en/posts/monad/"},
        {"title": "A Rust Design Pattern for Linear Types", "url": "https://users.rust-lang.org/t/a-rust-design-pattern-for-linear-types/140567"},
        {"title": "Monad (functional programming) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Monad_%28functional_programming%29"},
        {"title": "Haskell Guide 2026: Functional Programming That Changes How You Think", "url": "https://precisionaiacademy.com/blog/haskell-guide-2026"},
        {"title": "Does Rust Support Functional Programming Idioms? Exploring", "url": "https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms"},
        {"title": "What is a monad? And who needs Haskell anyway?", "url": "https://users.rust-lang.org/t/what-is-a-monad-and-who-needs-haskell-anyway/45710"},
    ],
    "algorithms": [
        {"title": "Best DSA Sheet 2026 | To Crack Interviews - namastedev.com", "url": "https://namastedev.com/namaste-dsa-sheet"},
        {"title": "Algorithms and Data Structures (LeetCode Preparation) | ArchMan", "url": "https://archman.dev/docs/algorithms-and-data-structures"},
        {"title": "Coding Interview Prep 2026: LeetCode Strategy That Works", "url": "https://precisionaiacademy.com/blog/coding-interview-prep-guide-2026"},
        {"title": "Data Structures and Algorithms Interview Guide 2026 | TechPrep", "url": "https://www.techprep.app/data-structures-and-algorithms/guide"},
        {"title": "NeetCode | Coding Interview Prep, Courses, Versus Mode", "url": "https://neetcode.io/"},
        {"title": "How to prepare for Data Structures and Algorithms interview in 2026", "url": "https://www.youtube.com/watch?v=jKGApDjRT6Y"},
        {"title": "Ultimate Java + DSA + LEETCODE and Interviews Preparation", "url": "https://www.udemy.com/course/ultimate-java-dsa-leetcode-and-interviews-preparation"},
        {"title": "Data Structures and Algorithms Roadmap 2026: Free Study Plan for Coding Interviews", "url": "https://www.freeclass.ai/roadmaps/dsa-roadmap-2026"},
        {"title": "How to Prepare for a Coding Interview: The Complete LeetCode", "url": "https://careerlift.ai/blog/how-to-prepare-coding-interview-leetcode-study-plan"},
        {"title": "The Ultimate Leetcode Roadmap: Data Structures and Algorithms", "url": "https://medium.com/@katravallicoding/the-ultimate-leetcode-roadmap-data-structures-algorithms-simplified-7564f84af829"},
    ],
    "python-internals": [
        {"title": "Python - Python Internals: Memory Management and the Global Interpreter Lock (GIL)", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil"},
        {"title": "How Python Works Under the Hood: Memory, GIL, and Bytecode", "url": "https://www.pythoncompiler.io/python/python-internals"},
        {"title": "Memory Management and GIL: Python Guide (2026) | Edugators", "url": "https://www.edugators.com/python/advanced/python-memory-gil"},
        {"title": "Python Memory Leaks: 7 Fixes for Long-Running Apps in 2026", "url": "https://appsconcerebro.com/en/blog/python-2026-diagnostico-y-solucion-de-fugas-de-memoria-en-ap"},
        {"title": "Exploring Python: Internals and Optimization", "url": "https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features"},
        {"title": "The Future of Python Internals: Exploring GIL Removal and", "url": "https://developers-heaven.net/blog/the-future-of-python-internals-exploring-gil-removal-and-other-optimizations/"},
        {"title": "Pythons GIL Is Gone - What That Actually Means for Your Code", "url": "https://python.plainenglish.io/pythons-gil-is-gone-what-that-actually-means-for-your-code-8ac535b5d879"},
        {"title": "Modern Python in 2026 - Python 3.13 / 3.14 / free-threaded / uv / Ruff / Polars 1.0 / FastAPI / Litestar / Robyn deep-dive", "url": "https://www.youngju.dev/blog/culture/2026-05-16-modern-python-2026-python-3-13-3-14-free-threaded-uv-ruff-polars-fastapi-litestar-robyn-deep-dive.en"},
        {"title": "Python Memory Profiling and Optimization Techniques", "url": "https://dasroot.net/posts/2026/04/python-memory-profiling-optimization-techniques"},
        {"title": "Python In-Depth - Memory Management in Python (GIL and Profiling)", "url": "https://medium.com/@arjundahal/python-in-depth-memory-management-in-python-gil-and-profiling-7b5c74e186e3"},
    ],
}

# Load existing profiles
with open('watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)

profiles = profiles_data['profiles']

# Step 3: Hash deduplication
def compute_hash(title, url):
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

# Filter out irrelevant results
skip_urls = [
    "forum.peak-system.com",
    "peak-system.com/de",
    "youtube.com",
    "udemy.com",
    "neetcode.io",
    "en.wikipedia.org/wiki/Monad",
    "en.wikipedia.org/wiki/Gradual_typing",
    "users.rust-lang.org",
    "microsoft.com/en-us/research/wp-content",
    "grokkingthesystemdesign.com",
]

results_by_profile = {}
new_hashes_by_profile = {}
sub_topics_discovered = {}

for profile_name, results in search_data.items():
    existing_hashes = set(profiles[profile_name]['last_result_hashes'])
    new_results = []
    new_hashes = []
    new_subtopics = set()
    
    for r in results:
        title = r['title']
        url = r['url']
        
        if any(skip in url for skip in skip_urls):
            continue
        
        h = compute_hash(title, url)
        if h not in existing_hashes:
            new_results.append({"title": title, "url": url, "hash": h})
            new_hashes.append(h)
            
            words = title.split()
            for word in words:
                clean = word.strip('.,:;!?()[]{}"\'-')
                if len(clean) > 3 and clean not in profiles[profile_name].get('sub_topics', []):
                    new_subtopics.add(clean)
    
    results_by_profile[profile_name] = new_results
    new_hashes_by_profile[profile_name] = new_hashes
    sub_topics_discovered[profile_name] = list(new_subtopics)[:10]

total_new = 0
for pname, results in results_by_profile.items():
    print(f"{pname}: {len(results)} new results")
    total_new += len(results)
print(f"\nTotal new results: {total_new}")

# Save temp file
temp_data = {
    "timestamp": timestamp,
    "results_by_profile": results_by_profile,
    "new_hashes_by_profile": new_hashes_by_profile,
}
os.makedirs('temp', exist_ok=True)
with open(f'temp/watch_run_{now.strftime("%Y%m%d_%H%M%S")}.json', 'w') as f:
    json.dump(temp_data, f, indent=2)

# Step 4 & 5: Update wiki pages
new_entries_by_page = {}
for pname, results in results_by_profile.items():
    page = profiles[pname]['wiki_page']
    if page not in new_entries_by_page:
        new_entries_by_page[page] = []
    for r in results:
        kw_words = r['title'].replace('-', ' ').replace(':', '').split()[:3]
        keyword = ' '.join(kw_words)
        entry = f"- **{date_str}** | [{r['title']}]({r['url']}) | kw: {keyword}"
        new_entries_by_page[page].append(entry)

updated_pages = []
for page, entries in new_entries_by_page.items():
    if not entries:
        continue
    filepath = f'entities/{page}'
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
    
    if insert_after is not None:
        lines = lines[:insert_after] + entries + [''] + lines[insert_after:]
    else:
        lines.append('')
        lines.append('## Updates')
        lines.append('')
        lines.extend(entries)
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))
    
    updated_pages.append(page)
    print(f"Updated {page} with {len(entries)} entries")

# Step 6: Update watch_profiles.json
for pname in search_data.keys():
    existing = profiles[pname]['last_result_hashes']
    new_h = new_hashes_by_profile[pname]
    updated = existing + new_h
    profiles[pname]['last_result_hashes'] = updated[-20:]
    profiles[pname]['last_run'] = timestamp
    
    for st in sub_topics_discovered.get(pname, []):
        if st not in profiles[pname]['sub_topics']:
            profiles[pname]['sub_topics'].append(st)

profiles_data['last_run'] = timestamp
profiles_data['profiles'] = profiles

with open('watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2, ensure_ascii=False)

print("Updated watch_profiles.json")

# Step 7: Git push
result = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True)
print(f"git add: {result.stdout} {result.stderr}")
result = subprocess.run(['git', 'commit', '-m', f'{date_str} Wiki watch update'], capture_output=True, text=True)
print(f"git commit: {result.stdout} {result.stderr}")
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print(f"git push: {result.stdout} {result.stderr}")

# Step 8: Build digest
digest_lines = []
digest_lines.append(f"## Wiki Watch Digest -- {timestamp}")
digest_lines.append(f"Checked: {len(search_data)} profiles")
digest_lines.append(f"New results: {total_new}")
digest_lines.append("")

profile_display = {
    "system-design": "System Design",
    "compilers": "Compilers & LLVM",
    "type-systems": "Type Systems",
    "functional-programming": "Functional Programming",
    "algorithms": "Algorithms & DSA",
    "python-internals": "Python Internals",
}

for pname, results in results_by_profile.items():
    display = profile_display.get(pname, pname)
    digest_lines.append(f"### {display}")
    digest_lines.append(f"New: {len(results)} results")
    if results:
        for r in results[:5]:
            digest_lines.append(f"- [{r['title'][:80]}]({r['url']})")
        if len(results) > 5:
            digest_lines.append(f"- ...and {len(results)-5} more")
    else:
        digest_lines.append("No new results this cycle")
    new_st = sub_topics_discovered.get(pname, [])
    if new_st:
        digest_lines.append(f"New sub-topics: {', '.join(new_st[:5])}")
    digest_lines.append("---")

print("\n=== DISCORD DIGEST ===")
print('\n'.join(digest_lines))
