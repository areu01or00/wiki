import json, hashlib, datetime, subprocess, os

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json') as f:
    profiles_data = json.load(f)

# All search results (from web searches)
all_results = {
    "system-design": [
        {"title": "System Design: The Complete Guide 2026", "url": "https://www.systemdesignhandbook.com/guides/system-design/", "desc": "Complete guide covering scalability, reliability, data flow, fault tolerance"},
        {"title": "Distributed Systems Roadmap (2026) | The Design Round", "url": "https://thedesignround.com/distributed-systems-roadmap", "desc": "Structured roadmap for distributed systems: CAP theorem, data replication, real-world architectures"},
        {"title": "System Design Building Blocks: Design Scalable Systems in 2026", "url": "https://www.systemdesignhandbook.com/blog/system-design-building-blocks", "desc": "Cloud-native, AI-assisted building blocks for distributed systems"},
        {"title": "System Design Series Part 3: Load Balancing & Caching - Wasil Zafar", "url": "https://www.wasilzafar.com/pages/series/system-design/system-design-load-balancing-caching.html", "desc": "Load balancing algorithms, caching strategies, Redis, Memcached, CDN patterns"},
        {"title": "System Design Guide 2026: Load Balancing, Caching, CDN, Databases, Message Queues, Scaling", "url": "https://onlinetools4free.com/research/system-design-guide-2026", "desc": "Comprehensive system design guide covering load balancing, caching, CDN, databases, scaling"},
        {"title": "Microservices Architecture Patterns in 2026: Mastering Distributed Systems Design", "url": "https://www.andrewhansen.au/microservices-architecture-patterns-in-2026-mastering-distributed-systems-design", "desc": "Microservices architecture patterns and best practices for distributed systems"},
        {"title": "Distributed Systems | Architecture Patterns · GitScrum Docs", "url": "https://docs.gitscrum.com/en/best-practices/distributed-systems-architecture-patterns", "desc": "Scalability patterns, consensus algorithms, Paxos, Raft, circuit breaker"},
        {"title": "12 Essential Distributed System Design Patterns Every Architect Should Know", "url": "https://antondevtips.com/blog/12-essential-distributed-system-design-patterns-every-architect-should-know", "desc": "API Gateway, CQRS, Saga, Sidecar, Strangler Fig, Anti-Corruption Layer patterns"},
        {"title": "Distributed System Design: the complete guide", "url": "https://grokkingthesystemdesign.com/guides/distributed-system-design", "desc": "Principles, architectures, scalability, fault tolerance, consistency"},
        {"title": "System Design Guide 2026 - Scalable Architecture Patterns", "url": "https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf", "desc": "API Gateway, Rate Limiter, Load Balancer, Caching, CQRS patterns"},
    ],
    "compilers": [
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 ...", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en", "desc": "LLVM dominance, V8 4-tier JIT, Inline Caching, Escape Analysis, Rust Monomorphization"},
        {"title": "Just-In-Time (JIT) Compiler with LLVM - Create Your Own Programming Language", "url": "https://createlang.rs/01_calculator/jit_intro.html", "desc": "Building JIT compiler with LLVM using inkwell Rust wrapper"},
        {"title": "JIT Compilation | microsoft/llvm | DeepWiki", "url": "https://deepwiki.com/microsoft/llvm/4-jit-compilation", "desc": "Microsoft LLVM JIT compilation deep dive"},
        {"title": "BuildingAJIT1.rst - chekalexey/compiler-course-2026", "url": "https://github.com/chekalexey/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst", "desc": "ORC-based JIT in LLVM tutorial, KaleidoscopeJIT, lazy compilation"},
        {"title": "BuildingAJIT1.rst - RomanPikhotskiy/compiler-course-2026", "url": "https://github.com/RomanPikhotskiy/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst", "desc": "Forked compiler course 2026 LLVM JIT tutorial"},
        {"title": "2026 European LLVM Developers' Meeting", "url": "https://llvm.swoogo.com/2026eurollvm/session/3943710/quick-talks", "desc": "LLVM JIT challenges, BOLT data prefetching, coroutine compilation, CFI binary rewriting"},
        {"title": "LLVM - Wikipedia", "url": "https://en.wikipedia.org/wiki/LLVM", "desc": "LLVM compiler infrastructure overview"},
        {"title": "The Case For Compilers: A Look at SPEC CPU 2026 on LLVM 22", "url": "https://www.servethehome.com/the-case-for-compilers-a-look-at-spec-cpu-2026-on-llvm-22", "desc": "SPEC CPU 2026 benchmark performance on LLVM 20 vs LLVM 22"},
        {"title": "BuildingAJIT3.rst - 4elodoy-Molovek/compiler-course-2026", "url": "https://github.com/4elodoy-Molovek/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT3.rst", "desc": "Lazy JIT compilation with ORC CompileOnDemand layer"},
        {"title": "JIT-Optimization-Engine - cloudsealed", "url": "https://github.com/cloudsealed/JIT-Optimization-Engine", "desc": "High-performance LLVM-based JIT engine for financial transactions using Numba"},
    ],
    "type-systems": [
        {"title": "Navigating the 2026 Language Landscape: A Typing and Paradigm Matrix", "url": "https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix", "desc": "Gradual typing ascendance, smarter type inference, TypeScript evolution"},
        {"title": "Type system concepts — typing documentation", "url": "https://typing.python.org/en/latest/spec/concepts.html", "desc": "Python type system specification: static, dynamic, gradual typing"},
        {"title": "Gradual Typing in Type Theory - numberanalytics.com", "url": "https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory", "desc": "Gradual typing in type theory and type inference"},
        {"title": "Gradual Typing as if Types Mattered - wgt20.irif.fr", "url": "https://wgt20.irif.fr/wgt20-final28-acmpaginated.pdf", "desc": "Gradual typing inheriting from static typing research"},
        {"title": "Type Theory and Gradual Typing - numberanalytics.com", "url": "https://www.numberanalytics.com/blog/type-theory-gradual-typing", "desc": "Soundness and completeness challenges in gradual type systems"},
        {"title": "The Rise of Static Typing - Why It Has Been Back Since the Mid-2010s 2026 - BrainDetox", "url": "https://braindetox.kr/en/posts/static_typing_rise_2026.html", "desc": "Type inference and gradual typing removing friction, AI coding pressure toward types"},
        {"title": "Efficient Selection of Type Annotations for Performance Improvement in Gradual Typing", "url": "https://programming-journal.org/2026/11/3/", "desc": "New technique for selecting type annotations to improve gradually typed program performance"},
        {"title": "arXiv: Efficient Selection of Type Annotations for Performance", "url": "https://arxiv.org/abs/2603.05649", "desc": "Amortized approach for selecting type annotations on Reticulated Python"},
        {"title": "Gradual Typing with Inference - Jeremy Siek", "url": "https://www.cs.cmu.edu/~aldrich/FOOL/fool08/siek-slides.pdf", "desc": "Combining gradual typing with unification-based type inference"},
        {"title": "Gradual Typing with Unification-based Inference - Jeremy Siek", "url": "https://jsiek.github.io/home/dls08igtlc.pdf", "desc": "How dynamic type interacts with type variables of inference"},
    ],
    "functional-programming": [
        {"title": "Functional Programming in 2026: Haskell vs. Gleam vs. Rust", "url": "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust", "desc": "Haskell expressive types, Gleam pragmatic BEAM, Rust systems prowess"},
        {"title": "The Future of Haskell and Functional Programming", "url": "https://softwarepatternslexicon.com/haskell/conclusion/the-future-of-haskell-and-functional-programming", "desc": "Future trends and applications of Haskell and FP"},
        {"title": "Monads are Omnipresent in Rust - bertiqwerty", "url": "https://www.bertiqwerty.com/en/posts/monad", "desc": "State monads in Rust, Builder pattern via monads"},
        {"title": "How I Learned Monads: Not Through Haskell But Through Rust", "url": "https://medium.com/@saehwanpark/how-i-learned-monads-not-through-haskell-but-through-rust-f4233f7779c7", "desc": "Learning monads through Rust Result/Option types"},
        {"title": "Does Rust Support Functional Programming Idioms? - codegenes.net", "url": "https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms", "desc": "Filter/Map/Reduce, Monads, and Syntactic Sugar in Rust"},
        {"title": "What's Coming for Haskell in 2026 - slicker.me", "url": "https://slicker.me/haskell/haskell-2026.html", "desc": "GHC 9.14 compiler advances, enhanced tooling, community growth"},
        {"title": "Monads and Monad-Like Patterns in Rust - softwarepatternslexicon.com", "url": "https://softwarepatternslexicon.com/rust/functional-programming-patterns-in-rust/monads-and-monad-like-patterns-in-rust", "desc": "Handling computations with context in Rust via monads"},
        {"title": "Functional Programming at Its Finest: Why Haskell Developers Bring Unmatched Code Reliability", "url": "https://pctechmag.com/2026/05/functional-programming-at-its-finest-why-haskell-developers-bring-unmatched-code-reliability", "desc": "Haskell type class system, functors, monads, applicatives"},
        {"title": "Monads in Functional Programming: A Comprehensive Guide", "url": "https://thetechgenie.in/monads-in-functional-programming-a-comprehensive-guide", "desc": "Comprehensive monad guide with Haskell examples"},
        {"title": "Monad (functional programming) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Monad_%28functional_programming%29", "desc": "Wikipedia reference for monads in FP"},
    ],
    "algorithms": [
        {"title": "Data Structure I - LeetCode", "url": "https://leetcode.com/problem-list/m1b6ucdi/", "desc": "LeetCode curated DSA study plan with 240+ problems"},
        {"title": "Best DSA Sheet 2026 | To Crack Interviews - namastedev.com", "url": "https://namastedev.com/namaste-dsa-sheet", "desc": "165 handpicked DSA questions with structured explanations"},
        {"title": "Top 100 DSA Interview Questions - LeetCode Discuss", "url": "https://leetcode.com/discuss/post/4258631/Top-100-DSA-Interview-Questions", "desc": "Top 100 DSA questions with links covering Arrays, Trees, DP, Graphs"},
        {"title": "Top 20 LeetCode Questions You Must Know in 2026 | Interview AiBox", "url": "https://interviewaibox.co/en/blog/top-20-leetcode-questions-you-must-know-2026", "desc": "20 most frequently asked LeetCode problems covering 10 core patterns"},
        {"title": "NeetCode | Coding Interview Prep, Courses, Versus Mode", "url": "https://neetcode.io/", "desc": "Structured prep with Blind 75, NeetCode 150, NeetCode 250"},
        {"title": "Data Structures & Algorithms Interview Guide 2026 | TechPrep", "url": "https://www.techprep.app/data-structures-and-algorithms/guide", "desc": "Blind 75 + TechPrep 100 framework for interview prep"},
        {"title": "Data Structures & Algorithms Roadmap 2026 - The Tutor Bridge", "url": "https://www.thetutorbridge.com/roadmap/dsa", "desc": "Complete DSA learning path with salary impact data"},
        {"title": "Data structures and algorithms study cheatsheets - Tech Interview Handbook", "url": "https://www.techinterviewhandbook.org/algorithms/study-cheatsheet", "desc": "Study cheatsheets for coding interviews covering all core topics"},
        {"title": "LeetCode Questions for TCS 2026: 50 Problems [Solved]", "url": "https://papersadda.com/article/leetcode-questions-tcs-2026", "desc": "50 LeetCode questions for TCS NQT/Ninja/Digital drives with trend data"},
        {"title": "Algorithms and Data Structures (LeetCode Preparation) | ArchMan", "url": "https://archman.dev/docs/algorithms-and-data-structures", "desc": "Beginner-friendly guide from fundamentals to advanced techniques"},
    ],
    "python-internals": [
        {"title": "How Python Works Under the Hood: Memory, GIL, and Bytecode", "url": "https://www.pythoncompiler.io/python/python-internals", "desc": "Memory, GIL, and Bytecode internals explained"},
        {"title": "Under the Hood of Python: Internals, Optimization, and Modern Features", "url": "https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features", "desc": "Cyclic GC, __slots__, Pattern Matching, Python 3.14 Free-Threading"},
        {"title": "Python Internals: Memory Management and the Global Interpreter Lock (GIL)", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil", "desc": "Reference counting, garbage collection, PyMalloc, GIL explained"},
        {"title": "Python 3.14 Free-Threading and Experimental JIT", "url": "https://blog.imseankim.com/python-3-14-free-threading-jit-compiler-gil-removal-2026", "desc": "Free-threading (no GIL), experimental JIT compiler, t-strings"},
        {"title": "State of Python 2026 | The Dev Newsletter", "url": "https://devnewsletter.com/p/state-of-python-2026", "desc": "PEP 703 GIL removal, PEP 779 criteria, uv overtaking pip, template strings, deferred annotations"},
        {"title": "Memory Management and GIL: Python Guide (2026) | Edugators", "url": "https://www.edugators.com/python/advanced/python-memory-gil", "desc": "Python memory management and GIL guide"},
        {"title": "The Secret Life of Python: Understanding the GIL", "url": "https://www.tech-reader.blog/2026/04/the-secret-life-of-python-understanding.html", "desc": "GIL explained via analogy, multiprocessing as solution"},
        {"title": "The Future of Python Internals: Exploring GIL Removal and Optimizations", "url": "https://developers-heaven.net/blog/the-future-of-python-internals-exploring-gil-removal-and-other-optimizations/", "desc": "Current state of GIL removal and future optimization plans"},
        {"title": "Python Complete Guide | CPython Internals and GIL", "url": "https://pkglog.com/en/blog/python-complete-guide", "desc": "CPython internals and GIL reference"},
        {"title": "Memory Management in Python - Real Python", "url": "https://realpython.com/python-memory-management", "desc": "Deep dive into Python memory management internals"},
    ],
}

# Step 3: Hash deduplication
today = datetime.datetime.utcnow().strftime('%Y-%m-%d')
now_str = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

profile_new_entries = {}
profile_new_hashes = {}

for profile_name, results in all_results.items():
    existing_hashes = set(profiles_data["profiles"][profile_name]["last_result_hashes"])
    new_entries = []
    new_hashes = []
    
    for r in results:
        h = hashlib.md5(f"{r['title']}{r['url']}".encode('utf-8', errors='replace')).hexdigest()
        if h not in existing_hashes:
            keyword = r['desc'].split(',')[0].split(':')[0].strip()[:40]
            entry = f"- **{today}** | [{r['title']}]({r['url']}) | kw: {keyword}"
            new_entries.append(entry)
            new_hashes.append(h)
            existing_hashes.add(h)
    
    profile_new_entries[profile_name] = new_entries
    profile_new_hashes[profile_name] = new_hashes

# Step 5: Update wiki pages using Python I/O
for profile_name, entries in profile_new_entries.items():
    if not entries:
        continue
    wiki_page = profiles_data["profiles"][profile_name]["wiki_page"]
    wiki_path = f"/home/hermes/wiki/entities/{wiki_page}"
    
    if not os.path.exists(wiki_path):
        print(f"WARNING: {wiki_path} does not exist, skipping")
        continue
    
    with open(wiki_path, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is None:
        lines.append('')
        lines.append('## Updates')
        lines.append('')
        insert_after = len(lines)
    
    lines = lines[:insert_after] + entries + [''] + lines[insert_after:]
    
    with open(wiki_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Updated {wiki_page} with {len(entries)} new entries")

# Step 6: Update watch_profiles.json
for profile_name, new_h in profile_new_hashes.items():
    hashes = profiles_data["profiles"][profile_name]["last_result_hashes"]
    hashes.extend(new_h)
    profiles_data["profiles"][profile_name]["last_result_hashes"] = hashes[-20:]
    profiles_data["profiles"][profile_name]["last_run"] = now_str

profiles_data["last_run"] = now_str

with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)

print("Updated watch_profiles.json")

# Step 7: Git push
os.chdir('/home/hermes/wiki')
result = subprocess.run(['git', 'add', '-A'], capture_output=True, text=True)
print("git add:", result.stdout.strip(), result.stderr.strip())
result = subprocess.run(['git', 'commit', '-m', f'{now_str} Wiki watch update'], capture_output=True, text=True)
print("git commit:", result.stdout.strip(), result.stderr.strip())
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print("git push:", result.stdout.strip(), result.stderr.strip())

# Step 8: Generate Discord digest
total_new = sum(len(v) for v in profile_new_entries.values())
total_profiles = len(all_results)

digest_lines = [
    f"## Wiki Watch Digest -- {now_str}",
    f"Checked: {total_profiles} profiles | New: {total_new} results",
    ""
]

profile_display_names = {
    "system-design": "System Design",
    "compilers": "Compilers and LLVM",
    "type-systems": "Type Systems",
    "functional-programming": "Functional Programming",
    "algorithms": "Algorithms and DSA",
    "python-internals": "Python Internals",
}

for profile_name, entries in profile_new_entries.items():
    display = profile_display_names.get(profile_name, profile_name)
    count = len(entries)
    if count == 0:
        continue
    
    new_subtopics = []
    existing_topics = set(profiles_data["profiles"][profile_name]["sub_topics"])
    for r in all_results[profile_name]:
        for word in r['title'].split():
            clean = word.strip(':,.!?()[]{}"\'-')
            if clean and len(clean) > 2 and clean not in existing_topics:
                new_subtopics.append(clean)
                existing_topics.add(clean)
    profiles_data["profiles"][profile_name]["sub_topics"] = list(existing_topics)
    
    digest_lines.append(f"### {display}")
    digest_lines.append(f"New: {count} results")
    for e in entries:
        digest_lines.append(e)
    if new_subtopics[:5]:
        digest_lines.append(f"Added sub-topics: {', '.join(new_subtopics[:5])}")
    digest_lines.append("---")

with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)

digest = '\n'.join(digest_lines)
print("\n=== DISCORD DIGEST ===")
print(digest)

with open('/home/hermes/wiki/temp/digest_latest.txt', 'w') as f:
    f.write(digest)
