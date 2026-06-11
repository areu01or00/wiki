import hashlib
import json
import os
from datetime import datetime

# All search results organized by profile
results = {
    "system-design": [
        {"title": "Top 7 Most-Used Distributed System Patterns", "url": "https://www.youtube.com/watch?v=nH4qjmP2KEE"},
        {"title": "Distributed Systems Architecture Patterns for Edge Computing in 2026", "url": "https://tianpan.co/forum/t/distributed-systems-architecture-patterns-for-edge-computing-in-2026/1225"},
        {"title": "Building Distributed Systems Architecture: From Single Server Dreams to Multi-Node Reality", "url": "https://hemaks.org/posts/building-distributed-systems-architecture-from-single-server-dreams-to-multi-node-reality/"},
        {"title": "Event-Driven Architecture: The Architectural Shift That Changed Distributed Systems", "url": "https://javascript.plainenglish.io/event-driven-architecture-the-architectural-shift-that-changed-distributed-systems-66f4e9ee14f0"},
        {"title": "System Design Roadmap", "url": "https://roadmap.sh/system-design"},
        {"title": "Centralized vs. Decentralized vs. Distributed Systems", "url": "https://www.geeksforgeeks.org/system-design/comparison-centralized-decentralized-and-distributed-systems/"},
        {"title": "Distributed System Design Patterns", "url": "https://medium.com/@nishantparmar/distributed-system-design-patterns-2d20908fecfc"},
        {"title": "Design patterns in distributed system", "url": "https://www.slideshare.net/slideshow/design-patterns-in-distributed-system/66719846"},
    ],
    "compilers": [
        {"title": "Just-in-time compilation - Wikipedia", "url": "https://en.wikipedia.org/wiki/Just-in-time_compilation"},
        {"title": "The LLVM Compiler Infrastructure Project - Open Projects", "url": "https://llvm.org/OpenProjects.html"},
        {"title": "OrcJIT at Scale with the llvm-autojit Plugin - FOSDEM 2026", "url": "https://fosdem.org/2026/schedule/event/FTCATX-llvm-autojit/"},
        {"title": "LLVM Compiler Infrastructure - Google Summer of Code 2026", "url": "https://summerofcode.withgoogle.com/programs/2026/organizations/llvm-compiler-infrastructure"},
        {"title": "Retrofitting JIT Compilers into C Interpreters", "url": "https://tratt.net/laurie/blog/2026/retrofitting_jit_compilers_into_c_interpreters.html"},
        {"title": "jank is off to a great start in 2026", "url": "https://jank-lang.org/blog/2026-03-06-great-start/"},
        {"title": "2026 EuroLLVM Developers Meeting", "url": "https://llvm.org/devmtg/2026-04/"},
    ],
    "type-systems": [
        {"title": "Luau (programming language) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Luau_(programming_language)"},
        {"title": "Type inference of all constructs and the next 15 months", "url": "https://elixir-lang.org/blog/2026/01/09/type-inference-of-all-and-next-15/"},
        {"title": "Static vs. Dynamic Typing: The Ultimate Guide to Type Systems in 2026", "url": "https://toolshelf.tech/blog/static-vs-dynamic-typing-guide-2026/"},
        {"title": "TypeScript Overtakes JavaScript: What JVM Developers Need to Know", "url": "https://www.javacodegeeks.com/2026/03/typescript-overtakes-javascript-what-jvm-developers-need-to-know.html"},
        {"title": "Understanding Type Systems: Dynamic, Static, Strong and Weak Typing", "url": "https://dev.to/akshatjme/understanding-type-systems-dynamic-static-strong-and-weak-typing-34a2"},
        {"title": "Pyre Migrate Django: Gradual Typing Adoption 2025", "url": "https://johal.in/pyre-migrate-django-gradual-typing-adoption-2025/"},
    ],
    "functional-programming": [
        {"title": "Monad (functional programming) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Monad_(functional_programming)"},
        {"title": "monads - GitHub Topics", "url": "https://github.com/topics/monads"},
        {"title": "Rust: Functional Programming & Monads", "url": "https://readmedium.com/functional-programming-with-monads-90230ccccb48"},
        {"title": "All About Monads - HaskellWiki", "url": "https://wiki.haskell.org/All_About_Monads"},
        {"title": "Monads (and Functors and Applicatives) explained in Rust", "url": "https://users.rust-lang.org/t/monads-and-functors-and-applicatives-explained-badly-in-rust/15187"},
        {"title": "monad in Functional programming - DEV Community", "url": "https://dev.to/anusornc/monad-in-functional-programming-2e5e"},
    ],
    "algorithms": [
        {"title": "Are Big Tech interviews still DSA, LeetCode-heavy in 2026?", "url": "https://www.reddit.com/r/careeradvice/comments/1tzzhde/are_big_tech_interviews_still_dsa_leetcodeheavy/"},
        {"title": "How to prepare for Data Structures & Algorithms interview in 2026", "url": "https://www.youtube.com/watch?v=jKGApDjRT6Y"},
        {"title": "I Tried 20+ Python DSA Courses with LeetCode Exercises", "url": "https://medium.com/javarevisited/i-tried-20-python-dsa-courses-with-leetcode-exercises-on-udemy-here-are-my-top-5-recommendations-ae743aaa931b"},
        {"title": "Most Asked LeetCode Problems in 2026 (40 Companies, Real Data)", "url": "https://www.dsaprep.dev/blog/most-asked-leetcode-problems-2026"},
        {"title": "Leetcode Interviews Fail to Measure Real Engineering Skills", "url": "https://www.linkedin.com/posts/sajjaad-khader_dear-tech-companies-its-2026-leetcode-activity-7452355472281460736-JLik"},
        {"title": "LeetCode vs NeetCode vs PracHub (2026 Interview Guide)", "url": "https://prachub.com/resources/leetcode-vs-neetcode-vs-prachub-2026-interview-guide"},
        {"title": "Google 2026 Interview Preparation - Complete Weekly Roadmap", "url": "https://gist.github.com/carefree-ladka/6d1722421f9e1e46bd2dbdb5ea1b4684"},
    ],
    "python-internals": [
        {"title": "Python 3.14.2 Release and the Rise of Free-Threaded CPython", "url": "https://blog.cubed.run/python-3-14-2-release-and-the-rise-of-free-threaded-cpython-what-developers-must-know-in-2026-61102e66e2e5"},
        {"title": "Python support for free threading - Python 3.14.6 documentation", "url": "https://docs.python.org/3/howto/free-threading-python.html"},
        {"title": "Python Free-Threading Guide", "url": "https://py-free-threading.github.io/"},
        {"title": "Python 3.15: The GIL is Dead. Now What for AI Performance?", "url": "https://shahvatsal.com/blog/python-3-15-gil-free-ai-performance"},
        {"title": "Python in 2026: From Glue Code to the Universal AI Operating System", "url": "https://medium.com/@ajay.singh_91430/python-in-2026-from-glue-code-to-the-universal-ai-operating-system-e10a51a6524a"},
        {"title": "Python 3.13 GIL: Unlock True Parallelism with the Free-Threaded Build", "url": "https://www.stork.ai/blog/youre-using-python-313-wrong"},
        {"title": "Get started with the free-threaded build of Python 3.13", "url": "https://www.infoworld.com/article/3552750/get-started-with-the-free-threaded-build-of-python-3-13.html"},
        {"title": "Python Complete Guide | CPython Internals GIL", "url": "https://pkglog.com/en/blog/python-complete-guide/"},
    ],
}

# Load existing hashes from profiles
profiles_path = "/home/hermes/wiki/watch_profiles.json"
with open(profiles_path) as f:
    profiles_data = json.load(f)

# Step 3: Hash deduplication
all_hashes = {}
new_entries_by_page = {}
today = datetime.utcnow().strftime("%Y-%m-%d")

for profile_name, profile_results in results.items():
    profile = profiles_data["profiles"][profile_name]
    wiki_page = profile["wiki_page"]
    existing_hashes = set(profile.get("last_result_hashes", []))

    if wiki_page not in new_entries_by_page:
        new_entries_by_page[wiki_page] = []
    if wiki_page not in all_hashes:
        all_hashes[wiki_page] = set()

    new_count = 0
    for item in profile_results:
        title = item["title"]
        url = item["url"]
        h = hashlib.md5(f"{title}{url}".encode('utf-8', errors='replace')).hexdigest()

        all_hashes[wiki_page].add(h)

        if h not in existing_hashes:
            words = title.lower().split()
            kw = ", ".join(words[:3])
            entry = f"- **{today}** | [{title}]({url}) | kw: {kw}"
            new_entries_by_page[wiki_page].append((entry, h))
            new_count += 1
            profile["last_result_hashes"].append(h)

    profile["last_run"] = datetime.utcnow().isoformat() + "Z"
    if len(profile["last_result_hashes"]) > 20:
        profile["last_result_hashes"] = profile["last_result_hashes"][-20:]

    print(f"{profile_name}: {new_count} new results")

# Save updated profiles
with open(profiles_path, 'w') as f:
    json.dump(profiles_data, f, indent=2)
print("Profiles updated.")

# Step 5: Update wiki pages
entities_dir = "/home/hermes/wiki/entities"
for wiki_page, entries in new_entries_by_page.items():
    if not entries:
        continue
    filepath = os.path.join(entities_dir, wiki_page)
    if not os.path.exists(filepath):
        print(f"WARNING: {filepath} not found, skipping")
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
        print(f"WARNING: No '## Updates' found in {wiki_page}")
        continue

    new_lines = [e[0] for e in entries]
    lines = lines[:insert_after] + new_lines + [''] + lines[insert_after:]

    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))

    print(f"Updated {wiki_page}: {len(new_lines)} entries inserted")

# Save temp results
ts = int(datetime.utcnow().timestamp())
temp_path = f"/home/hermes/wiki/temp/watch_run_{ts}.json"
with open(temp_path, 'w') as f:
    json.dump({"profiles": list(results.keys()), "results": results, "new_entries": {k: [e[0] for e in v] for k, v in new_entries_by_page.items()}}, f, indent=2)
print(f"Saved to {temp_path}")

total_new = sum(len(v) for v in new_entries_by_page.values())
print(f"\nTotal new entries across all pages: {total_new}")
