import hashlib, json, os, datetime

# Load profiles
with open('/home/hermes/wiki/watch_profiles.json') as f:
    profiles_data = json.load(f)
profiles = profiles_data['profiles']

# All new results by profile
new_results = {
    "system-design": [
        ("Modern Distributed Systems: Patterns and Anti-patterns", "https://anshadameenza.com/blog/technology/distributed-systems-patterns", "7ada9c496017a8b9bf8183716cd7e6fd"),
        ("9 Software Architecture Patterns for Distributed Systems", "https://dev.to/somadevtoo/9-software-architecture-patterns-for-distributed-systems-2o86", "4ab0a2ddf18264d4a022c029d9ec2e59"),
        ("SRDS 2026 – 45th International Symposium on Reliable Distributed Systems", "https://srds-conference.org/", "6b1aabebc8c2034b820a06d7e470ab13"),
        ("Fundamentals of Distributed Systems", "https://www.pluralsight.com/courses/distributed-systems-fundamentals", "8d0648d865c805207a5c573a1c8709a6"),
        ("Distributed System Design Patterns: A Practitioner's Reference", "https://distributedsystemauthority.com/distributed-system-design-patterns", "e61061e4c00189833ef99234e250341f"),
        ("Four Distributed Systems Architectural Patterns by Tim Berglund", "https://www.youtube.com/watch?v=BO761Fj6HH8", "437d3e48eaea63b6ea4dee10f17fbfc3"),
        ("Distributed System Design: the complete guide to building scalable infrastructure", "https://grokkingthesystemdesign.com/guides/distributed-system-design", "aaaf9550e5e27d5469ea0edd84372b77"),
        ("Patterns of Distributed Systems: Complete Roadmap", "https://chanhle.dev/en/blog/patterns-of-distributed-systems-roadmap", "4493db04174fb52c7b4a8bed0a3bc5ca"),
    ],
    "compilers": [
        ("Resume - Sanjoy Das (LLVM JIT contributor)", "http://playingwithpointers.com/resume.html", "210e04572b39090ee9cd7ec538860be2"),
        ("Perry - The Native TypeScript Compiler That Lowers TS Straight to LLVM Machine Code 2026", "https://braindetox.kr/en/posts/perry_typescript_llvm_compiler_2026.html", "0470167cda0b8ace44506e8158e0fc2c"),
        ("Sanjoy Das - NVIDIA Deep Learning Compilers", "http://sanjoy.link/", "3bdfe3d91fcb7381420d85421812bd65"),
        ("LLVM 22 Compiler Enters Development With LLVM 21 Now Branched", "https://www.phoronix.com/news/LLVM-22-Starts-Development", "aa7bbcec21e7a14bcdbbe8e8454cbed1"),
        ("Compiler Engineer, Backend GPU - New College Grad 2026 | NVIDIA", "http://jobs.nvidia.com/careers/job/893393842967", "7cf6b4162957e52aaa6e5666f79c0a22"),
        ("The state of GPU codegen with Nim (bonus: LLVM JIT)", "https://forum.nim-lang.org/t/9794", "54d4017e54664c29e143a57591a6e2ca"),
    ],
    "type-systems": [
        ("Gradual Typing with Inference (PDF)", "https://www.cs.cmu.edu/~aldrich/FOOL/fool08/siek-slides.pdf", "178661c54e89a13212b83a5ca61f9073"),
        ("How to Evaluate the Performance of Gradual Type Systems (PDF)", "https://janvitek.org/pubs/jfp18.pdf", "a494deea1062222538215619ac30a801"),
        ("A Strategic Guide to Gradual Typing in Python", "https://medium.com/@tihomir.manushev/a-strategic-guide-to-gradual-typing-in-python-49ac85f6dbdd", "4a1bf7bf0062edce6ba48dc2be42137f"),
        ("Position Paper: Performance Evaluation for Gradual Typing (PDF)", "http://www.ccs.neu.edu/home/asumu/papers/stop15-tfgnvf.pdf", "feeb79b76a27479ce10ee5c00b60481d"),
        ("Gradual Typing for Functional Languages (PDF)", "http://scheme2006.cs.uchicago.edu/13-siek.pdf", "4f039ed76813cc5c53ff90a4e98560ad"),
        ("Design and Evaluation of Gradual Typing for Python (PDF)", "https://jsiek.github.io/home/dls28-vitousekA.pdf", "80a66ecc2e4dc5b4bce8bf6fa86545f0"),
    ],
    "functional-programming": [
        ("The Practical Value of Functional Programming — Monad...", "https://www.youngju.dev/blog/culture/2026-04-15-functional-programming-monad-haskell-elixir-erlang-gleam-effect-ts-practical-value-deep-dive-guide-2025.en", "79a6740af6699726b2d5c3d3cc1ef1ea"),
        ("A gentle introduction to monads", "https://kristofsl.medium.com/a-gentle-introduction-to-monads-bc583d41d95", "93c0707eb0933e258fc88852df8ddb50"),
        ("Monad (functional programming) - Wikipedia", "https://en.wikipedia.org/wiki/Monad_%28functional_programming%29", "6ac17140976f4e3a7be22d2ec701d1ce"),
        ("Functional Programming in 2026: Haskell vs. Gleam vs. Rust", "https://www.penchef.com/software-engineering/functional-programming-2026-haskell-gleam-rust", "6ac17140976f4e3a7be22d2ec701d1ce"),
        ("Does Rust Support Functional Programming Idioms?", "https://www.codegenes.net/blog/does-will-rust-support-functional-programming-idioms/", "8b392f40f2d9484600edbc6565709ca7"),
        ("How I Learned Monads: Not Through Haskell But Through Rust", "https://medium.com/@saehwanpark/how-i-learned-monads-not-through-haskell-but-through-rust-f4233f7779c7", "449f1936d11b3408b5111b8fbfc6e205"),
        ("What the Heck Are Monads?! - YouTube", "https://www.youtube.com/watch?v=Q0aVbqim5pE", "9d0a225bfde129bbfa085aba60185f02"),
        ("All About Monads - HaskellWiki", "https://wiki.haskell.org/All_About_Monads", "9d0a225bfde129bbfa085aba60185f02"),
        ("Haskell Guide [2026]: Functional Programming That Changes How You Think", "https://precisionaiacademy.com/blog/haskell-guide-2026", "449f1936d11b3408b5111b8fbfc6e205"),
        ("Monads are Omnipresent in Rust", "https://www.bertiqwerty.com/en/posts/monad/", "9d0a225bfde129bbfa085aba60185f02"),
    ],
    "algorithms": [
        ("NeetCode | Coding Interview Prep", "https://neetcode.io/", "b2ebff509c2065c89ae295b2fabe3868"),
        ("Data structures and algorithms study cheatsheets for coding interviews", "https://www.techinterviewhandbook.org/algorithms/study-cheatsheet", "357f94c12f741d708689d53f78f9d42b"),
        ("Data Structures & Algorithms Interview Guide 2026", "https://www.techprep.app/data-structures-and-algorithms/guide", "a939def8c0cd3e980d5350d2d5117e8b"),
        ("Best DSA Sheet 2026 | To Crack Interviews", "https://namastedev.com/namaste-dsa-sheet", "09ba1908ae63111d1e15e6d4bafc047c"),
        ("Data Structures & Algorithms in Java + 150 Leetcode Problems", "https://www.udemy.com/course/mastering-leetcode-in-java-top-100-most-asked-problems", "2ce4cd52cf753ee765017e7ac9e6e950"),
        ("Top 100 DSA Interview Questions", "https://leetcode.com/discuss/post/4258631/Top-100-DSA-Interview-Questions", "29ea82bbcf096f644d06a5b4f99cee53"),
        ("Cracking Advanced Interview Problems with Binary Search", "https://codesignal.com/learn/courses/sorting-and-searching-algorithms-in-python/lessons/cracking-advanced-interview-problems-with-binary-search", "9a3679b8acc4e611ff2922f27c031f35"),
    ],
    "python-internals": [
        ("Top 5 Ways to Overcome Python's GIL Limitations", "https://sqlpey.com/python/top-5-ways-to-overcome-python-gil-limitations", "79903d9d29eca6e42254b646a84cf548"),
        ("Python 3.14 Free-Threading and Experimental JIT", "https://blog.imseankim.com/python-3-14-free-threading-jit-compiler-gil-removal-2026", "3ffbda41664600606f9e3139cda64291"),
        ("Python's GIL Is Gone — What That Actually Means for Your Code", "https://python.plainenglish.io/pythons-gil-is-gone-what-that-actually-means-for-your-code-8ac535b5d879", "087455b373dbe987da5078283f97a4cb"),
        ("Python 3.14: Free-Threading, JIT Compilation, and What It Means for You", "https://www.devwharf.com/2026/03/10/python-3-14-free-threading-jit-compilation-and-what-it-means-for-you", "738e2a4c7e0523c64b71c940fceed74c"),
        ("Memory Management in Python - Honeybadger", "https://www.honeybadger.io/blog/memory-management-in-python", "f7f6243b9d9a4a96b54a33522ed861e0"),
    ],
}

now_str = datetime.datetime.utcnow().strftime('%Y-%m-%d')
wiki_dir = '/home/hermes/wiki/entities'

# Keywords for each profile
keywords = {
    "system-design": "distributed systems",
    "compilers": "compilers",
    "type-systems": "type systems",
    "functional-programming": "functional programming",
    "algorithms": "algorithms",
    "python-internals": "python internals",
}

# Update each wiki page
for profile_name, items in new_results.items():
    wiki_file = os.path.join(wiki_dir, profiles[profile_name]['wiki_page'])
    if not os.path.exists(wiki_file):
        print(f"SKIP: {wiki_file} not found")
        continue
    
    with open(wiki_file, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Build new entries
    new_entries = []
    for title, url, h in items:
        # Find matching keywords from sub_topics
        entry_kw = keywords.get(profile_name, profile_name)
        new_entries.append(f"- **{now_str}** | [{title}]({url}) | kw: {entry_kw}")
    
    # Find ## Updates and insert after it
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is not None:
        lines = lines[:insert_after] + new_entries + [''] + lines[insert_after:]
    else:
        # If no ## Updates section, append at end
        lines.extend(['\n## Updates\n'] + new_entries + [''])
    
    with open(wiki_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Updated {wiki_file}: +{len(items)} entries")

# Update watch_profiles.json
now_iso = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
for profile_name, items in new_results.items():
    new_hashes = [h for _, _, h in items]
    existing = profiles[profile_name]['last_result_hashes']
    updated = new_hashes + existing
    profiles[profile_name]['last_result_hashes'] = updated[:20]
    profiles[profile_name]['last_run'] = now_iso

profiles_data['profiles'] = profiles
with open('/home/hermes/wiki/watch_profiles.json', 'w') as f:
    json.dump(profiles_data, f, indent=2)

print("\nwatch_profiles.json updated")
print(f"Timestamp: {now_iso}")
