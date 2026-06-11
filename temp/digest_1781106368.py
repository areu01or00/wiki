#!/usr/bin/env python3
"""Build correct Discord digest - only count entries from this run."""
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path("/home/hermes/programming-wisdom")
PROFILES_PATH = WIKI_ROOT / "watch_profiles.json"
TEMP_DIR = Path("/home/hermes/wiki/temp")
TS = 1781106368
NOW_UTC = datetime.fromtimestamp(TS, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
TODAY = datetime.fromtimestamp(TS, tz=timezone.utc).strftime("%Y-%m-%d")

# Load profiles
with open(PROFILES_PATH) as f:
    profiles_data = json.load(f)
profiles = profiles_data["profiles"]

# Load batch files for raw results (all profile queries)
all_results = {}
for batch_file in sorted(TEMP_DIR.glob(f"watch_run_{TS}_batch*.json")):
    with open(batch_file) as f:
        batch = json.load(f)
    for prof_name, prof_data in batch["results"].items():
        all_results[prof_name] = prof_data

# For each profile, parse its wiki page to get only the NEW entries
# (entries between ## Updates and the first blank line)
def get_new_entries_for_profile(prof_name):
    profile = profiles[prof_name]
    wiki_path = WIKI_ROOT / "wiki" / profile["wiki_page"]
    if not wiki_path.exists():
        return []
    with open(wiki_path) as f:
        content = f.read()
    lines = content.split("\n")
    # Find ## Updates line
    new_entries = []
    in_updates = False
    for line in lines:
        if line.strip() == "## Updates":
            in_updates = True
            continue
        if in_updates:
            if line.strip() == "":  # First blank line = end of new entries
                break
            if line.startswith("- **"):
                m = re.match(r"- \*\*\d{4}-\d{2}-\d{2}\*\* \| \[(.+?)\]\((.+?)\)", line.strip())
                if m:
                    new_entries.append({"title": m.group(1), "url": m.group(2)})
    return new_entries

new_by_profile = {}
for prof_name in all_results:
    new_by_profile[prof_name] = get_new_entries_for_profile(prof_name)

# Build the digest
print(f"## 🔄 Wiki Watch Digest — {NOW_UTC}")
print(f"Checked: {len(profiles)} profiles")
total_new = 0
for prof_name in all_results:
    n_new = len(new_by_profile[prof_name])
    if n_new == 0:
        continue
    total_new += n_new
    pretty = prof_name.replace("-", " ").title()
    print(f"### {pretty}")
    print(f"New: {n_new} results")
    for e in new_by_profile[prof_name]:
        url = e["url"]
        if "arxiv" in url:
            source = "arxiv"
        elif "wikipedia" in url or "wiki.python" in url:
            source = "wikipedia"
        elif "github" in url:
            source = "github"
        elif "medium" in url:
            source = "medium"
        elif "youtube" in url:
            source = "youtube"
        elif "reddit" in url:
            source = "reddit"
        elif "stackoverflow" in url:
            source = "stackoverflow"
        elif "linkedin" in url:
            source = "linkedin"
        elif ".edu" in url or "acm" in url or "dl.acm" in url:
            source = "academic"
        else:
            try:
                source = url.split("/")[2].replace("www.", "")
            except IndexError:
                source = "web"
        print(f"- [{e['title']}]({e['url']}) | {source}")
    subs = [e["title"][:50] for e in new_by_profile[prof_name][:3]]
    print(f"Added sub-topics: {', '.join(subs)}")
    print("---")
print(f"\nTotal: {total_new} new entries across {len([n for n in new_by_profile.values() if n])} profiles")
