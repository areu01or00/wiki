#!/usr/bin/env python3
"""Build and send Discord digest for 2026-06-11 01:05 wiki watch run."""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

TEMP_DIR = Path('/home/hermes/wiki/temp')

with open(TEMP_DIR / 'digest_data.json') as f:
    d = json.load(f)

# Build per-profile top entries from the wiki pages we just wrote
WIKI = Path('/home/hermes/programming-wisdom/wiki/entities')
PROFILE_DISPLAY = {
    'python-internals': 'Python Internals',
    'algorithms': 'Algorithms',
    'functional-programming': 'Functional Programming',
    'type-systems': 'Type Systems',
    'compilers': 'Compilers & JIT',
    'system-design': 'System Design',
}

# Read the new entries from each wiki page
TODAY = d['date']
top_entries_by_profile = {}
for profile, fname in [
    ('python-internals', 'python-internals.md'),
    ('algorithms', 'algorithms.md'),
    ('functional-programming', 'functional-programming.md'),
    ('type-systems', 'type-systems.md'),
    ('compilers', 'compilers.md'),
    ('system-design', 'system-design.md'),
]:
    f = WIKI / fname
    if not f.exists():
        continue
    content = f.read_text()
    lines = content.split('\n')
    in_updates = False
    entries = []
    for line in lines:
        if line.strip() == '## Updates':
            in_updates = True
            continue
        if in_updates:
            if TODAY in line and line.startswith('- **'):
                entries.append(line)
            elif line.startswith('- **') and TODAY not in line:
                break
            elif line.startswith('# '):
                break
    top_entries_by_profile[profile] = entries

# Build digest
time_str = datetime.now(timezone.utc).strftime('%H:%M')
date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')

digest = f"## 🔄 Wiki Watch Digest — {date_str} {time_str} UTC\n"
digest += f"Checked: {d['checked']} profiles\n"

for profile, display in PROFILE_DISPLAY.items():
    stats = d['profiles'].get(profile, {})
    new = stats.get('new', 0)
    digest += f"### {display}\n"
    digest += f"New: {new} results\n"
    entries = top_entries_by_profile.get(profile, [])
    for e in entries[:6]:
        digest += f"- {e[2:]}\n"
    sub = stats.get('sub_topics', [])
    if sub and new > 0:
        digest += f"Added sub-topics: {', '.join(sub)}\n"
    digest += "---\n"

# Print to verify
print(digest)

# Save
out_path = TEMP_DIR / 'discord_digest.md'
with open(out_path, 'w') as f:
    f.write(digest)

# Send via hermes send
result = subprocess.run(
    ['hermes', 'send', '--to', 'discord:1491398499521003622', '--file', str(out_path)],
    capture_output=True, text=True
)
print("---STDOUT---")
print(result.stdout)
print("---STDERR---")
print(result.stderr)
print(f"---EXIT: {result.returncode}---")
