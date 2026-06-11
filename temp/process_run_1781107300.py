#!/usr/bin/env python3
"""Wiki Watch Agent - process batch results and update wiki."""
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

PROFILES_PATH = "/home/hermes/programming-wisdom/watch_profiles.json"
ENTITIES_DIR = Path("/home/hermes/programming-wisdom/wiki/entities")
TEMP_DIR = Path("/home/hermes/wiki/temp")
WIKI_REPO = Path("/home/hermes/programming-wisdom")
TIMESTAMP = 1781107300
NOW_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
NOW_HUMAN_UTC = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def md5_of(title, url):
    return hashlib.md5(f"{title}{url}".encode("utf-8", errors="replace")).hexdigest()


def normalize_hashes(raw_hashes):
    out = []
    for h in raw_hashes:
        if isinstance(h, str):
            out.append(h)
        elif isinstance(h, dict):
            out.append(h.get("hash", ""))
    return out


def load_profiles():
    with open(PROFILES_PATH) as f:
        return json.load(f)


def load_batches():
    merged = {}
    for p in sorted(TEMP_DIR.glob(f"watch_run_{TIMESTAMP}_batch*.json")):
        with open(p) as f:
            data = json.load(f)
        for prof, payload in data["results"].items():
            merged[prof] = payload
    return merged


def collect_wiki_existing_hashes(entities_dir):
    """Safety layer: scan all entity files for any link already mentioned."""
    seen = set()
    url_to_page = {}
    for md_path in entities_dir.glob("*.md"):
        with open(md_path) as f:
            content = f.read()
        for m in re.finditer(r"\[([^\]]+)\]\((https?://[^\)]+)\)", content):
            t, u = m.group(1), m.group(2)
            h = md5_of(t, u)
            seen.add(h)
            url_to_page[u] = md_path.name
    return seen, url_to_page


def update_frontmatter(wiki_page_path, today_iso):
    """Update frontmatter 'updated' and 'last_watched' fields."""
    with open(wiki_page_path) as f:
        content = f.read()
    # Update 'updated: YYYY-MM-DD'
    content = re.sub(
        r"^updated:\s*\d{4}-\d{2}-\d{2}\s*$",
        f"updated: {today_iso}",
        content,
        count=1,
        flags=re.MULTILINE,
    )
    # Update 'last_watched: "..."'
    content = re.sub(
        r"^last_watched:\s*\"[^\"]*\"\s*$",
        f'last_watched: "{NOW_ISO}"',
        content,
        count=1,
        flags=re.MULTILINE,
    )
    with open(wiki_page_path, "w") as f:
        f.write(content)


def main():
    profiles_data = load_profiles()
    profiles = profiles_data["profiles"]
    batch_results = load_batches()
    existing_hashes, url_to_page = collect_wiki_existing_hashes(ENTITIES_DIR)

    print(f"Loaded {len(profiles)} profiles")
    print(f"Batch results for {len(batch_results)} profiles")
    print(f"Wiki has {len(existing_hashes)} existing hash entries")

    new_by_page = defaultdict(list)
    profile_new_hashes = defaultdict(list)
    profile_new_topics = defaultdict(set)

    for prof_name, prof_cfg in profiles.items():
        query = prof_cfg.get("query", "")
        wiki_page = prof_cfg.get("wiki_page", f"entities/{prof_name}.md")
        known_hashes = set(normalize_hashes(prof_cfg.get("last_result_hashes", [])))
        results = batch_results.get(prof_name, {}).get("web", [])
        if not results:
            print(f"  {prof_name}: no batch results")
            continue

        new_results = []
        for r in results:
            t, u = r["title"], r["url"]
            if not t or not u:
                continue
            h = md5_of(t, u)
            if h in known_hashes:
                continue
            if h in existing_hashes:
                continue
            new_results.append((t, u, h))

        if not new_results:
            print(f"  {prof_name}: 0 new (out of {len(results)} results)")
            continue

        print(f"  {prof_name}: {len(new_results)} new (out of {len(results)} results)")
        kw = prof_name
        for t, u, h in new_results:
            new_by_page[wiki_page].append((prof_name, t, u, kw))
            profile_new_hashes[prof_name].append(h)
            existing_hashes.add(h)
            first_words = " ".join(t.lower().split()[:4])
            profile_new_topics[prof_name].add(first_words)

    total_new = sum(len(v) for v in new_by_page.values())
    print(f"\nTotal new entries: {total_new}")
    for page, entries in new_by_page.items():
        print(f"  {page}: {len(entries)} new entries")
    for prof in profile_new_hashes:
        print(
            f"  profile {prof}: {len(profile_new_hashes[prof])} new hashes, "
            f"{len(profile_new_topics.get(prof, set()))} sub-topics"
        )

    if total_new == 0:
        # Still update last_run
        for prof_name in profiles:
            profiles[prof_name]["last_run"] = NOW_ISO
        profiles_data["last_run"] = NOW_ISO
        with open(PROFILES_PATH, "w") as f:
            json.dump(profiles_data, f, indent=2)
        print("\nNo new entries; just bumped last_run.")
        return 0

    # Update wiki pages
    for wiki_page_rel, entries in new_by_page.items():
        full_path = ENTITIES_DIR / Path(wiki_page_rel).name
        if not full_path.exists():
            print(f"  WARNING: {full_path} does not exist; skipping")
            continue
        with open(full_path) as f:
            content = f.read()
        lines = content.split("\n")
        insert_after = None
        for i, line in enumerate(lines):
            if line.strip() == "## Updates":
                insert_after = i + 1
                break
        if insert_after is None:
            print(f"  WARNING: no '## Updates' in {full_path}; appending at end")
            insert_after = len(lines)

        new_entry_lines = []
        for prof, title, url, kw in entries:
            new_entry_lines.append(f"- **{TODAY}** | [{title}]({url}) | kw: {kw}")
        insertion = [""] + new_entry_lines + [""]

        lines = lines[:insert_after] + insertion + lines[insert_after:]
        with open(full_path, "w") as f:
            f.write("\n".join(lines))
        # update frontmatter
        update_frontmatter(full_path, TODAY)
        print(f"  Updated {full_path} with {len(entries)} new entries")

    # Update watch_profiles.json
    for prof_name, new_hashes in profile_new_hashes.items():
        prof = profiles[prof_name]
        old_hashes = normalize_hashes(prof.get("last_result_hashes", []))
        combined = old_hashes + new_hashes
        prof["last_result_hashes"] = combined[-20:]
        prof["last_run"] = NOW_ISO
    for prof_name in profiles:
        if prof_name not in profile_new_hashes:
            profiles[prof_name]["last_run"] = NOW_ISO
    profiles_data["last_run"] = NOW_ISO

    with open(PROFILES_PATH, "w") as f:
        json.dump(profiles_data, f, indent=2)
    print(f"\nUpdated {PROFILES_PATH}")

    # Write digest
    digest = {
        "timestamp": TIMESTAMP,
        "date_utc": NOW_HUMAN_UTC,
        "checked": len(profiles),
        "new_count": total_new,
        "by_profile": {p: len(v) for p, v in profile_new_hashes.items()},
        "by_page": {p: len(v) for p, v in new_by_page.items()},
        "sub_topics": {p: sorted(list(t)) for p, t in profile_new_topics.items()},
        "new_entries": [
            {"profile": prof, "title": t, "url": u, "wiki_page": wp}
            for wp, entries in new_by_page.items()
            for prof, t, u, kw in entries
        ],
    }
    digest_path = TEMP_DIR / f"digest_{TIMESTAMP}.json"
    with open(digest_path, "w") as f:
        json.dump(digest, f, indent=2)
    print(f"Wrote digest to {digest_path}")

    # Markdown digest for Discord
    md_lines = [f"## 🔄 Wiki Watch Digest — {NOW_HUMAN_UTC}", ""]
    md_lines.append(f"Checked: {len(profiles)} profiles")
    md_lines.append("")
    for prof_name, prof_cfg in profiles.items():
        page = prof_cfg.get("wiki_page", f"entities/{prof_name}.md")
        if prof_name not in profile_new_hashes:
            continue
        # find all new entries for this profile across all pages
        prof_entries = []
        for wp, entries in new_by_page.items():
            for p, t, u, kw in entries:
                if p == prof_name:
                    prof_entries.append((t, u, wp))
        if not prof_entries:
            continue
        # topic name
        md_lines.append(f"### {prof_name}")
        md_lines.append(f"New: {len(prof_entries)} results")
        for t, u, wp in prof_entries:
            md_lines.append(f"- [{t}]({u}) | source: web search")
        topics = profile_new_topics.get(prof_name, set())
        if topics:
            md_lines.append(f"Added sub-topics: {', '.join(sorted(topics))}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    md_digest_path = TEMP_DIR / f"digest_{TIMESTAMP}.md"
    with open(md_digest_path, "w") as f:
        f.write("\n".join(md_lines))
    print(f"Wrote markdown digest to {md_digest_path}")
    print("\n=== Digest Preview ===")
    print("\n".join(md_lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
