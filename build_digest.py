#!/usr/bin/env python3
"""Build digest and send to Discord."""
import json
import os
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
timestamp = now.strftime('%Y-%m-%d %H:%M UTC')

# Load final temp file
import glob
final_files = sorted(glob.glob('temp/watch_run_*_final.json'))
if not final_files:
    print("ERROR: No final temp file found")
    exit(1)

with open(final_files[-1], 'r') as f:
    final = json.load(f)

profile_display = {
    "system-design": "System Design",
    "compilers": "Compilers & LLVM",
    "type-systems": "Type Systems",
    "functional-programming": "Functional Programming",
    "algorithms": "Algorithms & DSA",
    "python-internals": "Python Internals",
}

digest_lines = []
digest_lines.append(f"## \U0001f504 Wiki Watch Digest \u2014 {timestamp}")
digest_lines.append(f"Checked: {len(final['results_by_profile'])} profiles")
digest_lines.append(f"New results: {final['total_new']}")
digest_lines.append("")

for pname, results in final['results_by_profile'].items():
    display = profile_display.get(pname, pname)
    digest_lines.append(f"### {display}")
    digest_lines.append(f"New: {len(results)} results")
    if results:
        for r in results[:5]:
            t = r['title'][:90] + ('...' if len(r['title']) > 90 else '')
            digest_lines.append(f"- [{t}]({r['url']}) | source: web_search")
        if len(results) > 5:
            digest_lines.append(f"- ...and {len(results) - 5} more")
    else:
        digest_lines.append("No new results this cycle")
    new_st = final.get('sub_topics_by_profile', {}).get(pname, [])
    if new_st:
        digest_lines.append(f"Added sub-topics: {', '.join(new_st[:8])}")
    digest_lines.append("---")

digest_text = '\n'.join(digest_lines)

# Save digest
digest_file = f'temp/watch_digest_{now.strftime("%Y%m%d_%H%M%S")}.md'
with open(digest_file, 'w', encoding='utf-8') as f:
    f.write(digest_text)
print(f"Digest saved to {digest_file}")
print(f"Digest length: {len(digest_text)} chars")
print("---DIGEST START---")
print(digest_text)
print("---DIGEST END---")