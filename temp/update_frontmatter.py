#!/usr/bin/env python3
"""Update frontmatter last_watched and updated fields in entity files."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ENTITIES_DIR = Path("/home/hermes/programming-wisdom/wiki/entities")
DIGEST_PATH = Path("/home/hermes/wiki/temp/digest_1781103681.json")
NOW_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

with open(DIGEST_PATH) as f:
    digest = json.load(f)

# Map wiki_page to updated count
page_updates = digest["by_page"]

for page_rel, count in page_updates.items():
    full_path = ENTITIES_DIR / Path(page_rel).name
    if not full_path.exists():
        print(f"  SKIP: {full_path} not found")
        continue
    with open(full_path) as f:
        content = f.read()

    # update updated: YYYY-MM-DD line
    new_content = re.sub(
        r"^updated: \d{4}-\d{2}-\d{2}$",
        f"updated: {TODAY}",
        content,
        count=1,
        flags=re.MULTILINE,
    )
    # update last_watched: "..." line
    new_content = re.sub(
        r'^last_watched: "[^"]+"$',
        f'last_watched: "{NOW_ISO}"',
        new_content,
        count=1,
        flags=re.MULTILINE,
    )

    with open(full_path, "w") as f:
        f.write(new_content)
    print(f"  Updated frontmatter in {full_path.name}")

print("Done.")
