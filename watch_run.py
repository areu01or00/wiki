import hashlib, json, os, datetime

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json') as f:
    profiles = json.load(f)['profiles']

# All search results by profile
results = {
    "system-design": [
        ("Modern Distributed Systems: Patterns and Anti-patterns", "https://anshadameenza.com/blog/technology/distributed-systems-patterns"),
        ("9 Software Architecture Patterns for Distributed Systems", "https://dev.to/somadevtoo/9-software-architecture-patterns-for-distributed-systems-2o86"),
        ("SRDS 2026 – 45th International Symposium on Reliable Distributed Systems", "https://srds-conference.org/"),
        ("Distributed Systems Architecture in Java: A Complete Hands-On Reference", "https://medium.com/@devarshivyas/distributed-systems-architecture-in-java-a-complete-hands-on-reference-bca66da1e41a"),
        ("Fundamentals of Distributed Systems", "https://www.pluralsight.com/courses/distributed-systems-fundamentals"),
        ("Distributed System Design Patterns: A Practitioner's Reference", "https://distributedsystemauthority.com/distributed-system-design-patterns"),
        ("System Design Guide 2026 - Scalable Architecture Patterns", "https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf"),
        ("Four Distributed Systems Architectural Patterns by Tim Berglund", "https://www.youtube.com/watch?v=BO761Fj6HH8"),
        ("Distributed System Design: the complete guide to building scalable infrastructure", "https://grokkingthesystemdesign.com/guides/distributed-system-design"),
        ("Patterns of Distributed Systems: Complete Roadmap", "https://chanhle.dev/en/blog/patterns-of-distributed-systems-roadmap"),
    ],
    "compilers": [
        ("Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8", "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"),
        ("compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst", "https://github.com/RomanPikhotskiy/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"),
        ("Resume - Sanjoy Das (LLVM JIT contributor)", "http://playingwithpointers.com/resume.html"),
        ("Perry - The Native TypeScript Compiler That Lowers TS Straight to LLVM Machine Code 2026", "https://braindetox.kr/en/posts/perry_typescript_llvm_compiler_2026.html"),
        ("PostgreSQL Tutorial: Just-in-Time Compilation (JIT)", "https://www.rockdata.net/tutorial/tune-jit-compilation"),
        ("Just-In-Time (JIT) Compiler with LLVM - Create Your Own Programming Language with Rust", "https://createlang.rs/01_calculator/jit_intro.html"),
        ("Sanjoy Das - NVIDIA Deep Learning Compilers", "http://sanjoy.link/"),
        ("LLVM 22 Compiler Enters Development With LLVM 21 Now Branched", "https://www.phoronix.com/news/LLVM-22-Starts-Development"),
        ("Compiler Engineer, Backend GPU - New College Grad 2026 | NVIDIA", "http://jobs.nvidia.com/careers/job/893393842967"),
        ("The state of GPU codegen with Nim (bonus: LLVM JIT)", "https://forum.nim-lang.org/t/9794"),
    ],
    "type-systems": [
        ("Gradual Typing with Inference (PDF)", "https://www.cs.cmu.edu/~aldrich/FOOL/fool08/siek-slides.pdf"),
        ("Type system concepts — typing documentation", "https://typing.python.org/en/latest/spec/concepts.html"),
        ("Scholarly articles for gradual type inference research papers", "https://scholar.google.com/scholar?as_sdt=0&as_vis=1&hl=en&oi=scholart&q=gradual+type+inference+research+papers"),
        ("How to Evaluate the Performance of Gradual Type Systems (PDF)", "https://janvitek.org/pubs/jfp18.pdf"),
        ("Gradual typing - Wikipedia", "https://en.wikipedia.org/wiki/Gradual_typing"),
        ("Gradual Typing — Glossary — Textbook of Python", "https://www.textbookofpython.com/glossary/gradual-typing.html"),
        ("A Strategic Guide to Gradual Typing in Python", "https://medium.com/@tihomir.manushev/a-strategic-guide-to-gradual-typing-in-python-49ac85f6dbdd"),
        ("Position Paper: Performance Evaluation for Gradual Typing (PDF)", "http://www.ccs.neu.edu/home/asumu/papers/stop15-tfgnvf.pdf"),
        ("Gradual Typing for Functional Languages (PDF)", "http://scheme2006.cs.uchicago.edu/13-siek.pdf"),
        ("Design and Evaluation of Gradual Typing for Python (PDF)", "https://jsiek.github.io/home/dls28-vitousekA.pdf"),
    ],
    "functional-programming": [
        ("The Practical Value of Functional Programming — Monad...", "https://www.youngju.dev/blog/culture/2026-04-15-functional-programming-monad-haskell-elixir-erlang-gleam-effect-ts-practical-value-deep-dive-guide-2025.en"),
        ("A gentle introduction to monads", "https://kristofsl.medium.com/a-gentle-introduction-to-monads-bc583d41d95"),
        ("Monad (functional programming) - Wikipedia", "https://en.wikipedia.org/wiki/Monad_%28functional_programming%29"),
        ("Functional Programming in 2026: Haskell vs. Gleam vs. Rust", "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust"),
        ("Does Rust Support Functional Programming Idioms?", "https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms/"),
        ("How I Learned Monads: Not Through Haskell But Through Rust", "https://medium.com/@saehwanpark/how-i-learned-monads-not-through-haskell-but-through-rust-f4233f7779c7"),
        ("What the Heck Are Monads?! - YouTube", "https://www.youtube.com/watch?v=Q0aVbqim5pE"),
        ("All About Monads - HaskellWiki", "https://wiki.haskell.org/All_About_Monads"),
        ("Haskell Guide [2026]: Functional Programming That Changes How You Think", "https://precisionaiacademy.com/blog/haskell-guide-2026"),
        ("Monads are Omnipresent in Rust", "https://www.bertiqwerty.com/en/posts/monad/"),
    ],
    "algorithms": [
        ("Data Structure I - LeetCode", "https://leetcode.com/problem-list/m1b6ucdi/"),
        ("How to prepare for Data Structures & Algorithms interview in 2026", "https://www.youtube.com/watch?v=jKGApDjRT6Y"),
        ("NeetCode | Coding Interview Prep", "https://neetcode.io/"),
        ("Data structures and algorithms study cheatsheets for coding interviews", "https://www.techinterviewhandbook.org/algorithms/study-cheatsheet"),
        ("Data Structures & Algorithms Interview Guide 2026", "https://www.techprep.app/data-structures-and-algorithms/guide"),
        ("Best DSA Sheet 2026 | To Crack Interviews", "https://namastedev.com/namaste-dsa-sheet"),
        ("Data Structures & Algorithms in Java + 150 Leetcode Problems", "https://www.udemy.com/course/mastering-leetcode-in-java-top-100-most-asked-problems"),
        ("Top 100 DSA Interview Questions", "https://leetcode.com/discuss/post/4258631/Top-100-DSA-Interview-Questions"),
        ("GitHub - JimengShi/Leetcode-Data-Structures-Algorithms", "https://github.com/JimengShi/Leetcode-Data-Structures-Algorithms"),
        ("Cracking Advanced Interview Problems with Binary Search", "https://codesignal.com/learn/courses/sorting-and-searching-algorithms-in-python/lessons/cracking-advanced-interview-problems-with-binary-search"),
    ],
    "python-internals": [
        ("Python Internals: Memory Management & the Global Interpreter Lock (GIL)", "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil"),
        ("Memory Management & GIL: Python Guide (2026)", "https://www.edugators.com/python/advanced/python-memory-gil"),
        ("Top 5 Ways to Overcome Python's GIL Limitations", "https://sqlpey.com/python/top-5-ways-to-overcome-python-gil-limitations"),
        ("The Future of Python Internals: Exploring GIL Removal and Other Optimizations", "https://developers-heaven.net/blog/the-future-of-python-internals-exploring-gil-removal-and-other-optimizations"),
        ("Python 3.14 Free-Threading and Experimental JIT", "https://blog.imseankim.com/python-3-14-free-threading-jit-compiler-gil-removal-2026"),
        ("Python 3.14 Free-Threading - True Parallelism Without the GIL", "https://www.edgarmontano.com/posts/python/python-3-14-free-threading-true-parallelism"),
        ("Python's GIL Is Gone — What That Actually Means for Your Code", "https://python.plainenglish.io/pythons-gil-is-gone-what-that-actually-means-for-your-code-8ac535b5d879"),
        ("Python 3.14: Free-Threading, JIT Compilation, and What It Means for You", "https://www.devwharf.com/2026/03/10/python-3-14-free-threading-jit-compilation-and-what-it-means-for-you"),
        ("Memory Management in Python - Honeybadger", "https://www.honeybadger.io/blog/memory-management-in-python"),
    ],
}

# Compute hashes and find new results per profile
new_results = {}
all_hashes = {}
for profile_name, items in results.items():
    last_hashes = set(profiles[profile_name]['last_result_hashes'])
    new_results[profile_name] = []
    for title, url in items:
        h = hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()
        all_hashes.setdefault(profile_name, []).append(h)
        if h not in last_hashes:
            new_results[profile_name].append((title, url, h))

# Summary
for p, items in new_results.items():
    print(f"{p}: {len(items)} new results")
    for t, u, h in items:
        print(f"  [{h}] {t} -> {u}")

# Save batch file
ts = datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')
os.makedirs('/home/hermes/wiki/temp', exist_ok=True)
with open(f'/home/hermes/wiki/temp/watch_run_{ts}.json', 'w') as f:
    json.dump({k: [(t, u, h) for t, u, h in v] for k, v in new_results.items()}, f, indent=2)

print(f"\nSaved to temp/watch_run_{ts}.json")
