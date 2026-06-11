import json, hashlib, os
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
now_str = now.strftime('%Y-%m-%d_%H-%M')
today = now.strftime('%Y-%m-%d')

# Load profiles
with open('/home/hermes/wiki/temp/processing_state.json', 'r') as f:
    state = json.load(f)
profiles_data = state['profiles_data']['profiles']

# All search results (from both batches)
search_results = {
    "python-internals": [
        {"title": "Global interpreter lock - Wikipedia", "url": "https://en.wikipedia.org/wiki/Global_interpreter_lock"},
        {"title": "Understanding the Python Global Interpreter Lock (GIL)", "url": "https://thecodinggopher.substack.com/p/understanding-the-python-global-interpreter"},
        {"title": "Python's GIL Is Gone — What That Actually Means for Your Code", "url": "https://python.plainenglish.io/pythons-gil-is-gone-what-that-actually-means-for-your-code-8ac535b5d879"},
        {"title": "Inside Python: How your code runs, from source to execution | Medium", "url": "https://medium.com/codetodeploy/inside-python-how-your-code-runs-from-source-to-execution-3511f97a9a95"},
        {"title": "GlobalInterpreterLock", "url": "https://wiki.python.org/moin/GlobalInterpreterLock"},
    ],
    "algorithms": [
        {"title": "Is it still worth doing LeetCode in 2026? | by Fahim ul Haq - Medium", "url": "https://medium.com/@fahimulhaq/is-it-still-worth-doing-leetcode-a5ec9944970d"},
        {"title": "Optimization techniques for improving time complexity in algorithms", "url": "https://leetcode.com/discuss/study-guide/3221866/Optimization-techniques-for-improving-time-complexity-in-algorithms/"},
        {"title": "Data Structures & Algorithms in Java + 150 Leetcode Problems", "url": "https://www.coursera.org/specializations/packt-data-structures-and-algorithms-in-java-150-leetcode-problems"},
        {"title": "Rethinking DSA for 2026 Interview Success - LinkedIn", "url": "https://www.linkedin.com/posts/prince-singh-314a65187_traditional-dsa-is-no-longer-enough-in-2026-activity-7407985653629730816-fZoT"},
        {"title": "ATU Scholars Symposium: Data Structures & Algorithms Prep Hub", "url": "https://orc.library.atu.edu/atu_rs/2026/2026/51/"},
        {"title": "Essential Starter Techniques to Conquer Coding Challenges - Discuss", "url": "https://leetcode.com/discuss/study-guide/5450007/LeetCode-Level-Up:-Essential-Starter-Techniques-to-Conquer-Coding-Challenges/"},
        {"title": "Top 10 Data Structures Courses (2026 Edition) - MentorCruise", "url": "https://mentorcruise.com/courses/datastructures/"},
        {"title": "How to Pass Leetcode Interviews: The Ritual That Works", "url": "https://proandroiddev.com/how-to-pass-leetcode-interviews-the-ritual-that-works-a788ff2f4f27"},
        {"title": "DSA Roadmap 2026: Master Data Structures & Algo - CoderFile.io", "url": "https://coderfile.io/blog/dsa-roadmap-2026"},
        {"title": "LeetCode Alternatives 2026: Which Platform Fills the Gap?", "url": "https://www.codeintuition.io/blogs/leetcode-alternatives-2026"},
    ],
    "functional-programming": [
        {"title": "Monads as a Programming Pattern", "url": "https://samgrayson.me/essays/monads-as-a-programming-pattern/"},
        {"title": "Boilerplate Busting in Functional Languages | Lambda Land", "url": "https://lambdaland.org/posts/2024-05-01_definitely_not_about_monads/"},
        {"title": "Haskell Tutorial - YouTube", "url": "https://www.youtube.com/watch?v=02_H3LjqMr8"},
        {"title": "Monads in Functional Programming: From Theory to Practice | Medium", "url": "https://medium.com/@mo.mirjavadi/monads-in-functional-programming-from-theory-to-practice-9f9f93c0bf51"},
        {"title": "Null Object Pattern with Maybe Monad in Haskell", "url": "https://softwarepatternslexicon.com/patterns-haskell/6/12/"},
    ],
    "type-systems": [
        {"title": "Type system - Wikipedia", "url": "https://en.wikipedia.org/wiki/Type_system"},
        {"title": "Elixir v1.20 released: now a gradually typed language", "url": "https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/"},
        {"title": "Type inference of all constructs and the next 15 months", "url": "https://elixir-lang.org/blog/2026/01/09/type-inference-of-all-and-next-15/"},
        {"title": "From Duck Typing to Strict Types: Python's Evolving Type System", "url": "https://leapcell.medium.com/from-duck-typing-to-strict-types-pythons-evolving-type-system-09df4f5205f0"},
        {"title": "Type-Based Gradual Typing Performance Optimization", "url": "https://dl.acm.org/doi/full/10.1145/3632931"},
        {"title": "What type systems do you find interesting / useful / underrated?", "url": "https://www.reddit.com/r/ProgrammingLanguages/comments/1oj58xg/what_type_systems_do_you_find_interesting_useful/"},
        {"title": "What is a type system, really? - Lambda Land", "url": "https://lambdaland.org/posts/2023-01-17_what_is_a_type_system_really/"},
        {"title": "TYPE SYSTEMS - The Consensus", "url": "https://theconsensus.dev/t/type-systems.html"},
        {"title": "Efficient Selection of Type Annotations for Performance - arXiv", "url": "https://arxiv.org/pdf/2603.05649"},
    ],
    "compilers": [
        {"title": "Python JIT Tutorial: How to Enable and Optimize the CPython JIT", "url": "https://www.linkedin.com/pulse/python-jit-tutorial-how-enable-optimize-xslsc"},
        {"title": "Adventures in JIT compilation: Part 1 - an interpreter - Eli", "url": "https://eli.thegreenplace.net/2017/adventures-in-jit-compilation-part-1-an-interpreter"},
        {"title": "JIT compiler and bytecode optimization - High Performance Java", "url": "https://noobtomaster.com/high-performance-java/jit-compiler-and-bytecode-optimization/"},
        {"title": "2007-03-12-BossaLLVMIntroRevised.key", "url": "https://llvm.org/pubs/2007-03-12-BossaLLVMIntro.pdf"},
    ],
    "system-design": [
        {"title": "Memcached Python Client: Distributed Caching Patterns 2026", "url": "https://johal.in/memcached-python-client-distributed-caching-patterns-2026/"},
        {"title": "Caching Patterns: Cache-Aside, Write-Through | knowledgelib.io", "url": "https://knowledgelib.io/software/patterns/caching-patterns/2026"},
        {"title": "Distributed Systems 6.2: Raft - YouTube", "url": "https://www.youtube.com/watch?v=uXEYuDwm7e4"},
        {"title": "Design Issues of Distributed System (1).pptx", "url": "https://www.slideshare.net/slideshow/design-issues-of-distributed-system-1-pptx/272027019"},
        {"title": "Caching Patterns for Directories: Freshness vs Cost", "url": "https://content.directory/advanced-caching-patterns-2026"},
        {"title": "Zonal Gateway Load Balancing in Centralized E/E Architectures", "url": "https://eureka.patsnap.com/blog/scout-report/zonal-gateway-load-balancing-in-centralized-e-e-architectures-latency-redundancy-and-fault-containment/"},
        {"title": "Distributed System Design Trade-offs: Consistency | LinkedIn", "url": "https://www.linkedin.com/posts/javalgo_systemdesign-distributedsystems-architecture-activity-7457754792992624640-rxy3"},
    ],
}

# Deduplicate
new_results = {}
total_new = 0
total_checked = 0

for profile, results in search_results.items():
    existing_hashes = set(profiles_data[profile].get('last_result_hashes', []))
    new_results[profile] = []
    
    for r in results:
        total_checked += 1
        h = hashlib.md5((r['title'] + r['url']).encode('utf-8', errors='replace')).hexdigest()
        r['hash'] = h
        if h not in existing_hashes:
            new_results[profile].append(r)
            total_new += 1
    
    print(f"{profile}: {len(results)} checked, {len(new_results[profile])} new")

print(f"\nTotal: {total_checked} checked, {total_new} new")

# Group by wiki page
wiki_page_entries = {}
new_hashes_by_profile = {}

for profile, results in new_results.items():
    if not results:
        continue
    
    wiki_page = profiles_data[profile]['wiki_page']
    if wiki_page not in wiki_page_entries:
        wiki_page_entries[wiki_page] = []
    
    if profile not in new_hashes_by_profile:
        new_hashes_by_profile[profile] = []
    
    for r in results:
        title_words = r['title'].lower().replace('|', '').replace('[', '').replace(']', '').split()
        keywords = [w for w in title_words if len(w) > 3][:3]
        kw_str = ', '.join(keywords) if keywords else profile
        
        entry = f"- **{today}** | [{r['title']}]({r['url']}) | kw: {kw_str}"
        wiki_page_entries[wiki_page].append(entry)
        new_hashes_by_profile[profile].append(r['hash'])

print(f"\nWiki pages to update: {len(wiki_page_entries)}")
for page, entries in wiki_page_entries.items():
    print(f"  {page}: {len(entries)} entries")

# Update wiki pages
for wiki_page, entries in wiki_page_entries.items():
    filepath = f'/home/hermes/wiki/{wiki_page}'
    with open(filepath, 'r') as f:
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
        insert_after = len(lines)
    
    new_lines = lines[:insert_after] + entries + [''] + lines[insert_after:]
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(new_lines))
    
    print(f"  Updated {wiki_page} with {len(entries)} entries")

# Update processing_state.json
for profile, hashes in new_hashes_by_profile.items():
    if profile not in profiles_data:
        continue
    existing = profiles_data[profile].get('last_result_hashes', [])
    existing.extend(hashes)
    profiles_data[profile]['last_result_hashes'] = existing[-20:]
    profiles_data[profile]['last_run'] = now.isoformat()

state['profiles_data']['profiles'] = profiles_data
state['profiles_data']['last_run'] = now.isoformat()
state['profiles_data']['last_updated'] = now.isoformat()

with open('/home/hermes/wiki/temp/processing_state.json', 'w') as f:
    json.dump(state, f, indent=2)

# Save batch files
batch1 = {"results": {k: v for k, v in search_results.items() if k in ["python-internals", "algorithms", "functional-programming"]}}
batch2 = {"results": {k: v for k, v in search_results.items() if k in ["type-systems", "compilers", "system-design"]}}

with open(f'/home/hermes/wiki/temp/watch_run_{now_str}_batch1.json', 'w') as f:
    json.dump(batch1, f, indent=2)
with open(f'/home/hermes/wiki/temp/watch_run_{now_str}_batch2.json', 'w') as f:
    json.dump(batch2, f, indent=2)

# Save digest data
digest_data = {
    'new_entries_by_wiki_page': wiki_page_entries,
    'new_hashes_by_profile': new_hashes_by_profile,
    'total_checked': total_checked,
    'total_new': total_new,
    'profiles_checked': list(search_results.keys()),
    'timestamp': now_str
}
with open('/home/hermes/wiki/temp/digest_data.json', 'w') as f:
    json.dump(digest_data, f, indent=2)

print(f"\nSaved all files.")
