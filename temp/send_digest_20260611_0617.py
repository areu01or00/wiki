#!/usr/bin/env python3
"""Send Discord digest for wiki watch update."""
import json
from datetime import datetime, timezone

# Load digest data
with open('/home/hermes/wiki/temp/digest_data_2026-06-11_06-17.json', 'r') as f:
    digest = json.load(f)

NOW = datetime.now(timezone.utc)
timestamp = NOW.strftime('%Y-%m-%d %H:%M UTC')

# Build digest message
lines = []
lines.append(f"## 🔄 Wiki Watch Digest — {timestamp}")
lines.append(f"Checked: {digest['profiles_checked']} profiles")
lines.append(f"Total new: {digest['total_new']}")
lines.append("")

for topic, data in digest['by_topic'].items():
    if data['new_count'] > 0:
        lines.append(f"### {topic.replace('-', ' ').title()}")
        lines.append(f"New: {data['new_count']} results")
        for entry in data['entries']:
            # Extract title and url from markdown format
            # Format: - **date** | [Title](url) | kw: profile
            parts = entry.split(' | ')
            if len(parts) >= 2:
                title_url = parts[1]
                lines.append(f"- {title_url}")
        lines.append("---")

# Write the digest
output = '\n'.join(lines)
print(output)

# Save for delivery
with open('/home/hermes/wiki/temp/discord_digest_2026-06-11_06-17.md', 'w') as f:
    f.write(output)
