import json

entries_data = json.load(open('/tmp/wiki_entries.json'))

for wiki_page, entries in entries_data.items():
    filepath = f'/home/hermes/wiki/entities/{wiki_page}'
    with open(filepath, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find FIRST ## Updates line
    insert_after = None
    for i, line in enumerate(lines):
        if line.strip() == '## Updates':
            insert_after = i + 1
            break
    
    if insert_after is None:
        print(f"WARNING: {wiki_page} has no ## Updates line!")
        continue
    
    # Extract just the entry lines (skip profile name)
    new_lines = [entry for _, entry in entries]
    
    # Insert after ## Updates
    result_lines = lines[:insert_after] + new_lines + [''] + lines[insert_after:]
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(result_lines))
    
    print(f"Updated {wiki_page}: added {len(new_lines)} entries")
