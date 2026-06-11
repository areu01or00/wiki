import json, hashlib
from datetime import datetime, timezone

batch2 = {
    'type-systems': [
        {'title': 'Gradual typing - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Gradual_typing', 'description': 'Gradual typing is a type system that lies in between static typing and dynamic typing.'},
        {'title': 'Type Systems: From Generics to Dependent Types', 'url': 'https://federicocarrone.com/articles/type-systems/', 'description': 'Appendix: Type System Taxonomy.'},
        {'title': '30 Best general-purpose programming languages as of 2026 - Slant', 'url': 'https://www.slant.co/topics/15491/~general-purpose-programming-languages', 'description': 'Type system: gradual.'},
        {'title': 'Gradual typing in Python - GeeksforGeeks', 'url': 'https://www.geeksforgeeks.org/python/gradual-typing-in-python/', 'description': 'Gradual typing is a type system developed by Jeremy Siek and Walid Taha in 2006.'},
        {'title': 'Understanding Type Systems: Dynamic, Static... - DEV Community', 'url': 'https://dev.to/akshatjme/understanding-type-systems-dynamic-static-strong-and-weak-typing-34a2', 'description': 'Static Typing. In statically typed languages, types are known before execution.'},
        {'title': 'type-inference · GitHub Topics · GitHub', 'url': 'https://github.com/topics/type-inference?l=ocaml', 'description': 'functional-programming ocaml type-system.'},
        {'title': 'Gradual Typing Includes Both Fully Static and Fully Dynamic', 'url': 'https://jsiek.github.io/home/refined-criteria-gradual.pdf', 'description': 'Gradual typing touches both the static type system and the dynamic semantics.'},
        {'title': 'Consistent Subtyping for All | Springer Nature Link', 'url': 'https://link.springer.com/chapter/10.1007/978-3-319-89884-1_1', 'description': 'A Type Inference System Based on Saturation of Subtyping Constraints.'},
        {'title': 'Extending Dylan type system for better type inference and error...', 'url': 'https://pure.itu.dk/en/publications/extending-dylans-type-system-for-better-type-inference-and-error-/', 'description': 'We implemented the type system and a unification-based type inference algorithm.'},
        {'title': 'ReasonML vs TypeScript: comparing their type systems | Medium', 'url': 'https://medium.com/free-code-camp/reasonml-typescript-comparing-their-type-systems-620e4343221c', 'description': 'Static typing: Reason.'}
    ],
    'compilers': [
        {'title': '1. Building a JIT: Starting out with KaleidoscopeJIT - LLVM', 'url': 'https://llvm.org/docs/tutorial/BuildingAJIT1.html', 'description': 'The goal of this tutorial is to introduce you to LLVM ORC JIT APIs.'},
        {'title': 'Compilers and Modern Language Runtimes — LLVM, JIT, GC, V8 ...', 'url': 'https://www.youngju.dev/blog/culture/2026-04-15-compiler-runtime-llvm-jit-gc-v8-turbofan-maglev-inline-caching-escape-analysis-rust-monomorphization-deep-dive-guide-2025.en', 'description': 'Apr 15, 2026 · LLVM dominance, V8 4-tier JIT.'},
        {'title': 'Implementing JIT (Just In Time) Compilation - OpenGenus IQ', 'url': 'https://iq.opengenus.org/implement-jit-compilation/', 'description': 'JIT compilation involves transforming bytecode into machine instructions.'},
        {'title': 'JIT Design and Implementation · The Julia Language', 'url': 'https://docs.julialang.org/en/v1/devdocs/jit/', 'description': 'The optimization pipeline is based off LLVM new pass manager.'},
        {'title': 'PEP 744 – JIT Compilation | peps.python.org', 'url': 'https://peps.python.org/pep-0744/', 'description': 'Apr 11, 2024 · This new interpreter delivers significant performance improvements.'},
        {'title': '2026 EuroLLVM Developers Meeting - LLVM.org', 'url': 'https://llvm.org/devmtg/2026-04/', 'description': 'Apr 15, 2026 · IR2Vec is a widely adopted framework for generating vector embeddings from LLVM IR.'},
        {'title': 'Deegen: A JIT-Capable VM Generator for Dynamic Languages', 'url': 'https://fredrikbk.com/publications/deegen.pdf', 'description': 'optimized bytecode interpreter and a baseline JIT compiler.'},
        {'title': 'Clang bytecode interpreter update - Red Hat Developer', 'url': 'https://developers.redhat.com/articles/2025/10/15/clang-bytecode-interpreter-update', 'description': 'Oct 15, 2025 · Learn about recent improvements made to the Clang bytecode interpreter.'},
        {'title': '2026 EuroLLVM Developers Meeting - Agenda - Announcements', 'url': 'https://discourse.llvm.org/t/2026-eurollvm-developers-meeting-agenda/89725', 'description': 'Feb 6, 2026 · IR2Vec is a widely adopted framework.'},
        {'title': 'Understanding and Finding JIT Compiler Performance Bugs - arXiv', 'url': 'https://arxiv.org/pdf/2603.06551', 'description': 'Mar 6, 2026 · JIT compilers perform optimizations and generate native code at runtime.'}
    ],
    'system-design': [
        {'title': 'System Design in 2026: The Complete Guide (18500 words)', 'url': 'https://dev.to/yakhilesh/system-design-in-2026-the-complete-guide-18500-words-3nn6', 'description': 'Jan 7, 2026 · caching patterns that saved my apps from crashing.'},
        {'title': 'System Design Building Blocks: Design Scalable Systems in 2026', 'url': 'https://www.systemdesignhandbook.com/blog/system-design-building-blocks/', 'description': 'Master distributed systems & architecture patterns.'},
        {'title': 'Load Balancing and Caching: Improving Performance in Large ...', 'url': 'https://medium.com/@kalanamalshan98/load-balancing-and-caching-improving-performance-in-large-systems-8dba10c35d68', 'description': 'Jun 2, 2026 · Together they create a highly efficient system.'},
        {'title': '50 System Design Patterns Every Engineer Should Know in 90 ...', 'url': 'https://designgurus.substack.com/p/50-system-design-patterns-every-engineer', 'description': 'May 11, 2026 · Daily deep dives into system design & modern architecture.'},
        {'title': '8 Must-Used Distributed System Patterns | Sina Riyahi - LinkedIn', 'url': 'https://www.linkedin.com/posts/sina-riyahi_8-must-used-distributed-system-patterns-activity-7398669926544191488-If5F', 'description': 'Nov 24, 2025 · 8 Must-Used Distributed System Patterns.'},
        {'title': 'Scalability Patterns for Modern Distributed Systems', 'url': 'https://blog.bytebytego.com/p/scalability-patterns-for-modern-distributed', 'description': 'Nov 13, 2025 · Stateless Services, Horizontal Scaling, Load Balancing.'},
        {'title': 'Distributed Cache Invalidation Patterns - Foojay.io', 'url': 'https://foojay.io/today/distributed-cache-invalidation-patterns/', 'description': 'Apr 21, 2026 · Caching systems can significantly reduce latency.'},
        {'title': 'The Complete Guide to System Design in 2026 | InfraSketch Blog', 'url': 'https://infrasketch.net/blog/complete-guide-system-design', 'description': 'Jan 5, 2026 · caching, databases, and architecture patterns.'},
        {'title': 'Making software scale better with modern design patterns - Upsun', 'url': 'https://upsun.com/blog/software-design-patterns/', 'description': 'Apr 27, 2026 · Load balancing: Share traffic across servers.'},
        {'title': 'How Do I Properly Learn System Design? Need Guidance ... - Reddit', 'url': 'https://www.reddit.com/r/softwarearchitecture/comments/1owsg6p/how_do_i_properly_learn_system_design_need/', 'description': 'Nov 14, 2025 · scalability, load balancing, databases, caching.'}
    ]
}

now = datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M')
data = {'timestamp': now, 'batch': 2, 'results': {}}

for profile, results in batch2.items():
    data['results'][profile] = []
    for r in results:
        h = hashlib.md5(f"{r['title']}{r['url']}".encode('utf-8', errors='replace')).hexdigest()
        data['results'][profile].append({
            'title': r['title'],
            'url': r['url'],
            'description': r.get('description', ''),
            'hash': h
        })

with open(f'/home/hermes/wiki/temp/watch_run_{now}_batch2.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f'Saved batch2 to watch_run_{now}_batch2.json')
for profile, results in data['results'].items():
    print(f'  {profile}: {len(results)} results')
