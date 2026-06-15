import hashlib, json, os, time
from datetime import datetime, timezone

# Current timestamp
now = datetime.now(timezone.utc)
ts = now.strftime('%Y-%m-%d %H:%M UTC')
ts_file = now.strftime('%Y%m%d_%H%M%S')

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json', 'r') as f:
    data = json.load(f)

profiles = data['profiles']

# All search results
search_results = {
    "system-design": [
        {"title": "The Coming Paradigm Shift in Distributed Systems Architecture", "url": "https://gabogil.com/2026/01/20/the-coming-paradigm-shift-in-distributed-systems-architecture"},
        {"title": "Distributed Systems Roadmap (2026) | The Design Round", "url": "https://thedesignround.com/distributed-systems-roadmap"},
        {"title": "Patterns of Distributed Systems: Complete Roadmap | Chanh Le", "url": "https://chanhle.dev/en/blog/patterns-of-distributed-systems-roadmap"},
        {"title": "System Design Guide 2026 - Scalable Architecture Patterns", "url": "https://tktips.org/wp-content/uploads/2026/01/System-Design-Guide-2026.pdf"},
        {"title": "Mastering Distributed Systems — Patterns & Principles (2026) | tutorialQ", "url": "https://tutorialq.com/dev/microservices/mastering-distributed-systems"},
        {"title": "System Design Guide 2026: Load Balancing, Caching, CDN, Databases, Message Queues, Scaling", "url": "https://onlinetools4free.com/research/system-design-guide-2026"},
        {"title": "System Design Series Part 3: Load Balancing & Caching - Wasil Zafar", "url": "https://www.wasilzafar.com/pages/series/system-design/system-design-load-balancing-caching.html"},
        {"title": "Edge Computing Trends 2026: The Rise of Distributed ...", "url": "https://www.thetechtrep.com/edge-computing-trends-2026"},
        {"title": "System Architecture Design: The Complete Guide 2026", "url": "https://www.systemdesignhandbook.com/guides/system-architecture-design/"},
        {"title": "Distributed Systems Best Practices | 2026 - docs.gitscrum.com", "url": "https://docs.gitscrum.com/en/best-practices/distributed-systems-architecture-patterns"},
    ],
    "compilers": [
        {"title": "Just-In-Time (JIT) Compiler with LLVM - Create Your Own ...", "url": "https://createlang.rs/01_calculator/jit_intro.html"},
        {"title": "Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 ...", "url": "https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en"},
        {"title": "ML Compiler Optimization Revolution [Deep Dive] [2026]", "url": "https://techbytes.app/posts/ml-compiler-optimization-revolution-2026"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at ...", "url": "https://github.com/RomanPikhotskiy/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "LLVM - Wikipedia", "url": "https://en.wikipedia.org/wiki/LLVM"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT1.rst at course-spring-2026", "url": "https://github.com/chekalexey/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT1.rst"},
        {"title": "compiler-course-2026/llvm/docs/tutorial/BuildingAJIT3.rst at ...", "url": "https://github.com/4elodoy-Molovek/compiler-course-2026/blob/course-spring-2026/llvm/docs/tutorial/BuildingAJIT3.rst"},
        {"title": "LLVM Weekly - a weekly newsletter covering developments in ...", "url": "https://llvmweekly.org/"},
        {"title": "AI-Compiler Prompt Engineering: 2026 Cheat Sheet [Deep Dive]", "url": "https://techbytes.app/posts/ai-compiler-prompt-engineering-2026-cheat-sheet"},
        {"title": "LLVM Integration and JIT Compilation | AcademySoftwareFoundation/OpenShadingLanguage | DeepWiki", "url": "https://deepwiki.com/AcademySoftwareFoundation/OpenShadingLanguage/3.1-llvm-integration-and-jit-compilation"},
    ],
    "type-systems": [
        {"title": "Efficient Selection of Type Annotations for Performance ...", "url": "https://programming-journal.org/2026/11/3"},
        {"title": "Gradual Typing in Type Theory - numberanalytics.com", "url": "https://www.numberanalytics.com/blog/ultimate-guide-gradual-typing-type-theory"},
        {"title": "Type system concepts — typing documentation", "url": "https://typing.python.org/en/latest/spec/concepts.html"},
        {"title": "Gradual Typing as if Types Mattered - wgt20.irif.fr", "url": "https://wgt20.irif.fr/wgt20-final28-acmpaginated.pdf"},
        {"title": "Navigating the Language Labyrinth: A 2026 Matrix Analysis of Typing and Paradigms - PookieTech Blog", "url": "https://pookietech.com.ng/blog/navigating-the-language-labyrinth-a-2026-matrix-analysis-of-typing-and-paradigms"},
        {"title": "The Rise of Static Typing - Why It Has Been Back Since the ...", "url": "https://braindetox.kr/en/posts/static_typing_rise_2026.html"},
        {"title": "Navigating the 2026 Language Landscape: A Typing and Paradigm ...", "url": "https://pookietech.com.ng/blog/navigating-the-2026-language-landscape-a-typing-and-paradigm-matrix"},
        {"title": "TypeScript Type System | microsoft/TypeScript-Handbook | DeepWiki", "url": "https://deepwiki.com/microsoft/TypeScript-Handbook/2-typescript-type-system"},
        {"title": "Efficient Selection of Type Annotations for Performance Improvement in Gradual Typing", "url": "https://2026.programming-conference.org/details/programming-2026-papers/7/Efficient-Selection-of-Type-Annotations-for-Performance-Improvement-in-Gradual-Typing"},
        {"title": "A Deep Dive into Type Systems — What Static Typing Really ...", "url": "https://yoichiozaki.github.io/en/blog/type-systems"},
    ],
    "functional-programming": [
        {"title": "Practical uses of monads in Haskell - vuink.com", "url": "https://vuink.com/post/anhguf-d-dse/en/2026/05/28/practical-use-of-monads-d-dhtml"},
        {"title": "Monads Tutorial — Monday Morning Haskell", "url": "https://mmhaskell.com/monads/tutorial"},
        {"title": "Nauths · Practical uses of monads in Haskell", "url": "https://nauths.fr/en/2026/05/28/practical-use-of-monads.html"},
        {"title": "Demystifying monads in Rust through property-based testing", "url": "https://vuink.com/post/fhafubjref-d-dvb/posts/monads-through-pbt"},
        {"title": "Making Sense of Monads - Monday Morning Haskell", "url": "https://academy.mondaymorninghaskell.com/p/making-sense-of-monads"},
        {"title": "Demystifying monads in Rust through property-based testing", "url": "https://sunshowers.io/posts/monads-through-pbt"},
        {"title": "Functional Programming in 2026: Haskell vs. Gleam vs. Rust | PenChef", "url": "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust"},
        {"title": "Functional Programming at Its Finest: Why Haskell Developers ...", "url": "https://pctechmag.com/2026/05/functional-programming-at-its-finest-why-haskell-developers-bring-unmatched-code-reliability"},
        {"title": "The Best Monad Tutorial Ever Written — Andrew Lilley Brinker", "url": "https://www.alilleybrinker.com/mini/the-best-monad-tutorial"},
        {"title": "Rust — Monday Morning Haskell | Monads Tutorial", "url": "https://cqjo.erkaid.de/rust-monday-morning-haskell-monads-tutorial-monday-morning-haskell"},
    ],
    "algorithms": [
        {"title": "Best DSA Sheet 2026 | To Crack Interviews - namastedev.com", "url": "https://namastedev.com/namaste-dsa-sheet"},
        {"title": "LeetCode Interview Questions: Top Patterns by Company (2026) | InterviewPilot", "url": "https://interviewpilot.dev/blog/leetcode-interview-questions"},
        {"title": "LeetCode Questions Asked in Google 2026 - PA", "url": "https://papersadda.com/article/leetcode-questions-google-2026"},
        {"title": "Top 100+ Data Structure Interview Questions [2026]", "url": "https://www.testmuai.com/learning-hub/data-structures-interview-questions"},
        {"title": "Data Structures Interview Questions: The Complete 2026 Guide | PhantomCodeAI", "url": "https://www.phantomcodeai.com/blogs/data-structures-interview-questions-complete-guide"},
        {"title": "Top 20 LeetCode Questions You Must Know in 2026 | Interview AiBox", "url": "https://interviewaibox.co/en/blog/top-20-leetcode-questions-you-must-know-2026"},
        {"title": "Algorithms & Data Structures (LeetCode Preparation) | ArchMan", "url": "https://archman.dev/docs/algorithms-and-data-structures"},
        {"title": "NeetCode | Coding Interview Prep, Courses, Versus Mode", "url": "https://neetcode.io/"},
        {"title": "Ultimate Java + DSA + LEETCODE and Interviews Preparation", "url": "https://www.udemy.com/course/ultimate-java-dsa-leetcode-and-interviews-preparation"},
        {"title": "Top LeetCode questions asked in NETFLIX Interviews for SDE role", "url": "https://medium.com/%40ridhisingla001/top-leetcode-questions-asked-in-netflix-interviews-for-sde-role-1611f353fee5"},
    ],
    "python-internals": [
        {"title": "The Python GIL Controversy: Why Multi-Core Parallelism ...", "url": "https://www.javacodegeeks.com/2026/01/the-python-gil-controversy-why-multi-core-parallelism-remains-broken-and-why-it-might-not-matter.html"},
        {"title": "Python - Python Internals: Memory Management & the Global ...", "url": "https://evidhya.com/subjects/python/python-internals-memory-management-the-global-interpreter-lock-gil"},
        {"title": "Under the Hood of Python: Internals, Optimization, and Modern Features", "url": "https://blog.habibullah.dev/under-the-hood-of-python-internals-optimization-and-modern-features"},
        {"title": "Memory Management & GIL: Python Guide (2026) | Edugators", "url": "https://www.edugators.com/python/advanced/python-memory-gil"},
        {"title": "The Ultimate Python Learning Roadmap for 2026: Complete", "url": "https://course4all.com/blog/python-learning-roadmap-2026"},
        {"title": "How Python Works Under the Hood: Memory, GIL, and Bytecode", "url": "https://www.pythoncompiler.io/python/python-internals"},
        {"title": "Python Memory Profiling and Optimization Techniques", "url": "https://dasroot.net/posts/2026/04/python-memory-profiling-optimization-techniques"},
        {"title": "Python Global Interpreter Lock (GIL) - cosmiclearn.com", "url": "https://www.cosmiclearn.com/python/gil.php"},
        {"title": "Python's GIL Is Gone — What That Actually Means for Your Code", "url": "https://python.plainenglish.io/pythons-gil-is-gone-what-that-actually-means-for-your-code-8ac535b5d879"},
        {"title": "Global Interpreter Lock (GIL) in Python: Past, Present, and ...", "url": "https://igorpejic.com/posts/gil"},
    ],
}

def compute_hash(title, url):
    return hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

# Deduplicate and find new results per profile
all_new = {}
all_new_hashes = {}
all_subs = set()

for profile_name, results in search_results.items():
    last_hashes = set(profiles[profile_name]['last_result_hashes'])
    new_results = []
    new_hashes = []
    for r in results:
        h = compute_hash(r['title'], r['url'])
        if h not in last_hashes:
            new_results.append(r)
            new_hashes.append(h)
            words = r['title'].replace(':', '').replace(',', '').replace('.', '').replace("'", '').split()
            for w in words:
                if len(w) > 2 and w.lower() not in ('the', 'and', 'for', 'with', 'this', 'that', 'from', 'has', 'are', 'was', 'not', 'but', 'how', 'why', 'can', 'will', 'your', 'you', 'its', 'our', 'who', 'all', 'new', 'may', 'use', 'top', 'get', 'let', 'set', 'add', 'run', 'see', 'own', 'big', 'old', 'way', 'two', 'per', 'via', 'vs'):
                    all_subs.add(w)
    all_new[profile_name] = new_results
    all_new_hashes[profile_name] = new_hashes

# Save temp batch files
os.makedirs('/home/hermes/wiki/temp', exist_ok=True)
for pname, results in all_new.items():
    fname = f'/home/hermes/wiki/temp/watch_run_{ts_file}_{pname}.json'
    with open(fname, 'w') as f:
        json.dump(results, f, indent=2)

# Aggregate by wiki_page
page_entries = {}
for pname, results in all_new.items():
    if not results:
        continue
    wp = profiles[pname]['wiki_page']
    if wp not in page_entries:
        page_entries[wp] = []
    for r in results:
        page_entries[wp].append({'title': r['title'], 'url': r['url'], 'profile': pname})

# Update wiki pages
for wiki_page, entries in page_entries.items():
    fpath = f'/home/hermes/wiki/entities/{wiki_page}'
    if not os.path.exists(fpath):
        print(f"SKIP: {fpath} not found")
        continue

    with open(fpath, 'r') as f:
        content = f.read()
    lines = content.split('\n')

    new_lines = []
    for e in entries:
        new_lines.append(f"- **{now.strftime('%Y-%m-%d')}** | [{e['title']}]({e['url']}) | kw: {e['profile']}")

    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break

    if insert_after is not None:
        lines = lines[:insert_after] + new_lines + [''] + lines[insert_after:]
        with open(fpath, 'w') as f:
            f.write('\n'.join(lines))
        print(f"Updated {wiki_page} with {len(new_lines)} entries")
    else:
        print(f"WARNING: No '## Updates' section in {wiki_page}")

# Update profiles
for pname, new_h in all_new_hashes.items():
    old = profiles[pname]['last_result_hashes']
    old.extend(new_h)
    profiles[pname]['last_result_hashes'] = old[-20:]
    profiles[pname]['last_run'] = ts

# Add discovered sub-topics
for pname in all_new:
    existing = set(profiles[pname].get('sub_topics', []))
    for sub in all_subs:
        if sub not in existing:
            profiles[pname]['sub_topics'].append(sub)

data['profiles'] = profiles
data['last_run'] = ts

with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Updated watch_profiles.json")

# Print digest summary
total_new = sum(len(v) for v in all_new.values())
print(f"\n=== DIGEST: {ts} ===")
print(f"Checked: {len(profiles)} profiles, {total_new} new results")
for pname, results in all_new.items():
    print(f"  {pname}: {len(results)} new results")
    for r in results[:3]:
        print(f"    - {r['title']}")
    if len(results) > 3:
        print(f"    ... and {len(results)-3} more")
