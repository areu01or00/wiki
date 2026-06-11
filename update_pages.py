import json
import os
from datetime import datetime, timezone

# Load the temp results
with open('/home/hermes/wiki/temp/watch_run_20260611_084726.json', 'r') as f:
    temp_data = json.load(f)

results = temp_data['results']

# Date string for entries
today = datetime.now(timezone.utc).strftime('%Y-%m-%d')

# Keywords extraction based on title keywords
def extract_keywords(title, sub_topics):
    """Extract relevant keywords from title."""
    keywords = []
    title_lower = title.lower()
    for st in sub_topics:
        if any(w in title_lower for w in st.lower().split()):
            keywords.append(st)
    if not keywords:
        # Fallback: pick first sub-topic
        keywords = [sub_topics[0]] if sub_topics else ['general']
    return keywords

# Update each wiki page
wiki_dir = '/home/hermes/wiki/entities'
os.makedirs(wiki_dir, exist_ok=True)

# Profile config for keywords
profile_config = {
    "system-design": {"wiki_page": "system-design.md", "sub_topics": ["load balancing", "caching patterns", "distributed systems", "scalability"]},
    "compilers": {"wiki_page": "compilers.md", "sub_topics": ["JIT compilation", "LLVM", "bytecode", "optimization"]},
    "type-systems": {"wiki_page": "type-systems.md", "sub_topics": ["gradual typing", "type inference", "dependent types"]},
    "functional-programming": {"wiki_page": "functional-programming.md", "sub_topics": ["monads", "Haskell", "Rust patterns", "functional idioms"]},
    "algorithms": {"wiki_page": "algorithms.md", "sub_topics": ["dynamic programming", "DSA roadmap", "coding interviews"]},
    "python-internals": {"wiki_page": "python-internals.md", "sub_topics": ["GIL", "free-threaded Python", "CPython internals", "memory management"]},
}

# Group by wiki_page
wiki_page_entries = {}
for profile_name, entries in results.items():
    if not entries:
        continue
    config = profile_config[profile_name]
    page = config['wiki_page']
    sub_topics = config['sub_topics']
    
    if page not in wiki_page_entries:
        wiki_page_entries[page] = []
    
    for entry in entries:
        kw = extract_keywords(entry['title'], sub_topics)
        line = f"- **{today}** | [{entry['title']}]({entry['url']}) | kw: {', '.join(kw)}"
        wiki_page_entries[page].append(line)

# Update each wiki page
for page, new_entries in wiki_page_entries.items():
    page_path = os.path.join(wiki_dir, page)
    
    # Read existing file
    if os.path.exists(page_path):
        with open(page_path, 'r') as f:
            content = f.read()
        lines = content.split('\n')
    else:
        lines = [f'# {page.replace(".md", "").replace("-", " ").title()}']
    
    # Find ## Updates section and insert after it
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_idx = i + 1
            break
    
    if insert_idx is None:
        # Add ## Updates section at the end
        lines.append('')
        lines.append('## Updates')
        insert_idx = len(lines)
    
    # Insert new entries
    lines = lines[:insert_idx] + new_entries + [''] + lines[insert_idx:]
    
    # Write back
    with open(page_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Updated {page}: {len(new_entries)} entries added")

print("\nDone updating wiki pages!")
