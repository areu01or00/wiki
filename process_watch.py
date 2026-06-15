import json, hashlib, os
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
timestamp = now.strftime('%Y-%m-%d %H:%M UTC')

with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

def md5_hash(title, url):
    return hashlib.md5((title + url).encode('utf-8', errors='replace')).hexdigest()

# Search results
all_results = {
    'system-design': [
        ('Mastering Distributed Systems \u2014 Patterns & Principles (2026) | tutorialQ', 'https://tutorialq.com/dev/microservices/mastering-distributed-systems'),
        ('The Coming Paradigm Shift in Distributed Systems Architecture', 'https://gabogil.com/2026/01/20/the-coming-paradigm-shift-in-distributed-systems-architecture'),
        ('System Design: The Complete Guide 2026', 'https://www.systemdesignhandbook.com/guides/system-design/'),
        ('System Design Guide 2026 - Scalable Architecture Patterns', 'https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf'),
        ('Distributed Systems Best Practices | 2026 - docs.gitscrum.com', 'https://docs.gitscrum.com/en/best-practices/distributed-systems-architecture-patterns'),
        ('System Design Series Part 3: Load Balancing & Caching - Wasil Zafar', 'https://www.wasilzafar.com/pages/series/system-design/system-design-load-balancing-caching.html'),
        ('Patterns of Distributed Systems: Complete Roadmap | Chanh Le', 'https://chanhle.dev/en/blog/patterns-of-distributed-systems-roadmap'),
        ('System Design Guide 2026: Load Balancing, Caching, CDN, Databases, Message Queues, Scaling', 'https://onlinetools4free.com/research/system-design-guide-2026'),
        ('10 Essential Distributed System Design Patterns for Scalable Apps', 'https://netalith.com/blogs/system-design/distributed-system-design-patterns-scalable-applications'),
        ('Three Bold Predictions for Distributed Systems in 2026', 'https://www.axoniq.io/blog/three-bold-predictions-for-distributed-systems-in-2026'),
    ],
    'compilers': [
        ('FOSDEM 2026 - OrcJIT at Scale with the llvm-autojit Plugin', 'https://fosdem.org/2026/schedule/event/FTCATX-llvm-autojit/'),
        ('Compilers and Modern Language Runtimes \u2014 LLVM, JIT, GC, V8', 'https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en'),
        ('Just-In-Time (JIT) Compiler with LLVM - Create Your Own Language', 'https://createlang.rs/01_calculator/jit_intro.html'),
        ('compiler-course-2026 BuildingAJIT1.rst chekalexey', 'https://github.com/chekalexey/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst'),
        ('compiler-course-2026 BuildingAJIT1.rst RomanPikhotskiy', 'https://github.com/RomanPikhotskiy/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst'),
        ('compiler-course-2026 BuildingAJIT1.rst VALancaster', 'https://github.com/VALancaster/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst'),
        ('The Case For Compilers: A Look at SPEC CPU 2026 on LLVM 22', 'https://www.servethehome.com/the-case-for-compilers-a-look-at-spec-cpu-2026-on-llvm-22'),
        ('compiler-course-2026 BuildingAJIT3.rst 4elodoy-Molovek', 'https://github.com/4elodoy-Molovek/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT3.rst'),
        ('AI-Compiler Prompt Engineering: 2026 Cheat Sheet [Deep Dive]', 'https://techbytes.app/posts/ai-compiler-prompt-engineering-2026-cheat-sheet'),
        ('compiler-course-2026 BuildingAJIT1.rst Georghinho', 'https://github.com/Georghinho/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst'),
    ],
    'type-systems': [
        ('Efficient Selection of Type Annotations for Performance Improvement in Gradual Typing (Programming 2026)', 'https://2026.programming-conference.org/details/programming-2026-papers/7/Efficient-Selection-of-Type-Annotations-for-Performance-Improvement-in-Gradual-Typing'),
        ('Gradual Typing in Type Theory - numberanalytics.com', 'https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory'),
        ('Navigating the 2026 Language Landscape: A Typing and Paradigm Matrix - PookieTech', 'https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix'),
        ('The Rise of Static Typing - Why It Has Been Back Since the Mid-2010s 2026 - BrainDetox', 'https://braindetox.kr/en/posts/static_typing_rise_2026.html'),
        ('Gradual Typing - Language Design and Implementation', 'https://comp.anu.edu.au/study/projects/gradual-typing-language-design-and-implementation'),
        ('Foundations for Gradual Typing - Khoury College of Computer Science', 'https://www.khoury.northeastern.edu/research_projects/foundations-for-gradual-typing'),
        ('Gradual Typing Performance, Micro Configurations and Macro Perspectives | NSF', 'https://par.nsf.gov/biblio/10569815-gradual-typing-performance-micro-configurations-macro-perspectives'),
        ('Gradual Typing Across the Spectrum - GitHub Pages', 'https://nuprl.github.io/gtp'),
        ('Gradual typing - Wikipedia', 'https://en.wikipedia.org/wiki/Gradual_typing'),
        ('Gradual Typing Performance Springer', 'https://link.springer.com/chapter/10.1007/978-3-031-64626-3_15'),
    ],
    'functional-programming': [
        ('Functional Programming in 2026: Haskell vs. Gleam vs. Rust', 'https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust'),
        ('Monads are Omnipresent in Rust - bertiqwerty', 'https://www.bertiqwerty.com/en/posts/monad'),
        ('The Practical Value of Functional Programming \u2014 Monad ...', 'https://www.youngju.dev/blog/culture/2026-04-15-functional-programming-monad-haskell-elixir-erlang-gleam-effect-ts-practical-value-deep-dive-guide-2025.en'),
        ('Rust \u2014 Monday Morning Haskell | Monads Tutorial', 'https://cqjo.erkaid.de/rust-monday-morning-haskell-monads-tutorial-monday-morning-haskell'),
        ('Functional Programming at Its Finest: Why Haskell Developers Bring Unmatched Code Reliability', 'https://pctechmag.com/2026/05/functional-programming-at-its-finest-why-haskell-developers-bring-unmatched-code-reliability'),
        ('Haskell Guide [2026]: Functional Programming That Changes How You Think', 'https://precisionaiacademy.com/blog/haskell-guide-2026'),
        ('Does Rust Support Functional Programming Idioms? Exploring ...', 'https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms'),
        ('Monad (functional programming) - Wikipedia', 'https://en.wikipedia.org/wiki/Monad_%28functional_programming%29'),
        ('All About Monads - HaskellWiki', 'https://wiki.haskell.org/All_About_Monads'),
        ('Monad - HaskellWiki', 'https://wiki.haskell.org/Monad'),
    ],
    'algorithms': [
        ('Best DSA Sheet 2026 | To Crack Interviews - namastedev.com', 'https://namastedev.com/namaste-dsa-sheet'),
        ('How to Prepare for a Coding Interview: The Complete LeetCode Study Plan', 'https://careerlift.ai/blog/how-to-prepare-coding-interview-leetcode-study-plan'),
        ('Data Structures & Algorithms Interview Guide 2026 | TechPrep', 'https://www.techprep.app/data-structures-and-algorithms/guide'),
        ('Data Structures & Algorithms Roadmap 2026: Free Study Plan | Free Class AI', 'https://www.freeclass.ai/roadmaps/dsa-roadmap-2026'),
        ('The Ultimate Leetcode Roadmap: Data Structures & Algorithms Simplified', 'https://medium.com/@katravallicoding/the-ultimate-leetcode-roadmap-data-structures-algorithms-simplified-7564f84af829'),
        ('NeetCode | Coding Interview Prep, Courses, Versus Mode', 'https://neetcode.io/'),
        ('Ultimate Java + DSA + LEETCODE and Interviews Preparation', 'https://www.udemy.com/course/ultimate-java-dsa-leetcode-and-interviews-preparation'),
        ('Algorithms & Data Structures (LeetCode Preparation) | ArchMan', 'https://archman.dev/docs/algorithms-and-data-structures'),
        ('LeetCode Cheat Sheet \u2014 PIRATE KING', 'https://www.piratekingdom.com/leetcode/cheat-sheet'),
        ('How to prepare for Data Structures & Algorithms interview in 2026', 'https://www.youtube.com/watch?v=jKGApDjRT6Y'),
    ],
    'python-internals': [
        ('How Python Works Under the Hood: Memory, GIL, and Bytecode', 'https://www.pythoncompiler.io/python/python-internals'),
        ('The Python GIL Controversy: Why Multi-Core Parallelism Remains Broken', 'https://www.javacodegeeks.com/2026/01/the-python-gil-controversy-why-multi-core-parallelism-remains-broken-and-why-it-might-not-matter.html'),
        ('Memory Management & GIL: Python Guide (2026) | Edugators', 'https://www.edugators.com/python/advanced/python-memory-gil'),
        ('Python - Python Internals: Memory Management & the Global Interpreter Lock', 'https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil'),
        ('Under the Hood of Python: Internals, Optimization, and Modern Features', 'https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features'),
        ('Pythons GIL Is Gone \u2014 What That Actually Means for Your Code', 'https://python.plainenglish.io/pythons-gil-is-gone-what-that-actually-means-for-your-code-8ac535b5d879'),
        ('Impact of GIL-less Cpython on Performance and Compatibility', 'https://hps.vi4io.org/_media/teaching/autumn_term_2024/stud/scap/frederik_hennecke.pdf'),
        ('Python GIL: The Key to Backend Performance - odysse.io', 'https://odysse.io/en/gil-in-python-the-key-to-backend-performance-and-multithreading'),
        ('The Future of Python Internals: Exploring GIL Removal and Optimizations', 'https://developers-heaven.net/blog/the-future-of-python-internals-exploring-gil-removal-and-other-optimizations/'),
        ('State of Python 2026 | The Dev Newsletter', 'https://devnewsletter.com/p/state-of-python-2026'),
    ],
}

new_results = {}
sub_topic_discoveries = {}

for profile_name, results in all_results.items():
    existing_hashes = set(profiles[profile_name]['last_result_hashes'])
    new_results[profile_name] = []
    sub_topic_discoveries[profile_name] = set()
    for title, url in results:
        h = md5_hash(title, url)
        if h not in existing_hashes:
            new_results[profile_name].append({'title': title, 'url': url, 'hash': h})
            for word in title.replace('|', '').replace(':', '').replace(',', '').replace('\u2014', ' ').split():
                clean = word.strip('[]()\u2019"')
                if len(clean) > 3 and clean not in profiles[profile_name].get('sub_topics', []):
                    sub_topic_discoveries[profile_name].add(clean)

# Save temp
os.makedirs('/home/hermes/wiki/temp', exist_ok=True)
temp_file = f'/home/hermes/wiki/temp/watch_run_{now.strftime("%Y%m%d_%H%M%S")}.json'
with open(temp_file, 'w') as f:
    json.dump({'timestamp': timestamp, 'new_results': new_results}, f, indent=2)

# Print summary
print(f'Timestamp: {timestamp}')
total_new = 0
for pn, res in new_results.items():
    print(f'{pn}: {len(res)} new')
    total_new += len(res)
    for r in res:
        print(f'  - {r["title"][:70]}... [{r["hash"][:8]}]')
print(f'Total new: {total_new}')

# Save for wiki updates
with open('/tmp/wiki_watch_data.json', 'w') as f:
    json.dump({
        'timestamp': timestamp,
        'new_results': new_results,
        'sub_topic_discoveries': {k: list(v)[:10] for k, v in sub_topic_discoveries.items()},
    }, f)
print('Data saved to /tmp/wiki_watch_data.json')
