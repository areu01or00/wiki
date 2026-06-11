#!/usr/bin/env python3
"""Wiki Watch Agent - process batch results and update wiki. Run 1781112745."""
import hashlib
import json
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path("/home/hermes/programming-wisdom")
PROFILES_PATH = WIKI_ROOT / "watch_profiles.json"
ENTITIES_DIR = WIKI_ROOT / "wiki" / "entities"
TEMP_DIR = Path("/home/hermes/wiki/temp")
RUN_TS = 1781112745
NOW_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
NOW_PRETTY = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def md5_of(title, url):
    return hashlib.md5(f"{title}{url}".encode("utf-8", errors="replace")).hexdigest()


def normalize_hashes(raw):
    out = []
    for h in raw or []:
        if isinstance(h, str):
            out.append(h)
        elif isinstance(h, dict):
            out.append(h.get("hash", ""))
    return [h for h in out if h]


def is_junk(url, title=""):
    if not url or not url.startswith("http"):
        return True
    if "/clev?event=" in url:
        return True
    junk_hosts = [
        "typing.com", "typingclub.com", "monkeytype.com", "typingtest.com",
        "typeracer.com", "10fastfingers.com", "speedtypingonline.com",
    ]
    if any(s in url for s in junk_hosts):
        return True
    if title and title.strip() == "":
        return True
    return False


def collect_wiki_existing(entities_dir):
    seen = set()
    url_to_page = {}
    for md in entities_dir.glob("*.md"):
        with open(md) as f:
            content = f.read()
        for m in re.finditer(r"\[([^\]]+)\]\((https?://[^\)]+)\)", content):
            t, u = m.group(1), m.group(2)
            seen.add(md5_of(t, u))
            url_to_page[u] = md.name
    return seen, url_to_page


def main():
    with open(PROFILES_PATH) as f:
        profiles_data = json.load(f)
    profiles = profiles_data["profiles"]

    merged = {}
    for p in sorted(TEMP_DIR.glob(f"watch_run_{RUN_TS}_batch*.json")):
        with open(p) as f:
            data = json.load(f)
        for prof, payload in data["results"].items():
            merged[prof] = payload

    existing_hashes, url_to_page = collect_wiki_existing(ENTITIES_DIR)
    print(f"Loaded {len(profiles)} profiles")
    print(f"Batch results for {len(merged)} profiles")
    print(f"Existing hashes in wiki: {len(existing_hashes)}")

    new_by_page = defaultdict(list)
    profile_new_hashes = defaultdict(list)
    profile_new_topics = defaultdict(set)
    profile_skipped_junk = defaultdict(int)
    profile_skipped_dup = defaultdict(int)
    profile_skipped_empty = defaultdict(int)
    profile_skipped_in_wiki = defaultdict(int)

    for prof_name, prof_cfg in profiles.items():
        wiki_page = prof_cfg.get("wiki_page", f"entities/{prof_name}.md")
        known_hashes = set(normalize_hashes(prof_cfg.get("last_result_hashes", [])))
        results = merged.get(prof_name, {}).get("web", [])
        if not results:
            continue
        n_new = 0
        for r in results:
            t, u = r.get("title", ""), r.get("url", "")
            if not t.strip():
                profile_skipped_empty[prof_name] += 1
                continue
            if is_junk(u, t):
                profile_skipped_junk[prof_name] += 1
                continue
            h = md5_of(t, u)
            if h in known_hashes:
                profile_skipped_dup[prof_name] += 1
                continue
            if h in existing_hashes:
                profile_skipped_in_wiki[prof_name] += 1
                continue
            kw = prof_name
            new_by_page[wiki_page].append((prof_name, t, u, kw))
            profile_new_hashes[prof_name].append(h)
            existing_hashes.add(h)
            first_words = " ".join(t.lower().split()[:4])
            profile_new_topics[prof_name].add(first_words)
            n_new += 1
        print(
            f"  {prof_name}: {n_new} new (of {len(results)} results; "
            f"skipped {profile_skipped_junk[prof_name]} junk, "
            f"{profile_skipped_dup[prof_name]} dup-in-profile, "
            f"{profile_skipped_in_wiki[prof_name]} dup-in-wiki, "
            f"{profile_skipped_empty[prof_name]} empty)"
        )

    total_new = sum(len(v) for v in new_by_page.values())
    print()
    print("=== Summary ===")
    print(f"Total new entries: {total_new}")
    for page, entries in new_by_page.items():
        print(f"  {page}: {len(entries)} new entries")
    for prof in profile_new_hashes:
        print(
            f"  profile {prof}: {len(profile_new_hashes[prof])} new hashes, "
            f"{len(profile_new_topics.get(prof, []))} sub-topics"
        )

    if total_new > 0:
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
            print(f"  Updated {full_path} with {len(entries)} new entries")
    else:
        print("No updates needed.")

    for prof_name, new_hashes in profile_new_hashes.items():
        prof = profiles[prof_name]
        old_hashes = normalize_hashes(prof.get("last_result_hashes", []))
        combined = old_hashes + new_hashes
        prof["last_result_hashes"] = combined[-20:]
        prof["last_run"] = NOW_ISO
    profiles_data["last_run"] = NOW_ISO

    with open(PROFILES_PATH, "w") as f:
        json.dump(profiles_data, f, indent=2)
    print(f"\nUpdated {PROFILES_PATH}")

    digest_path = TEMP_DIR / f"digest_{RUN_TS}.json"
    digest = {
        "timestamp": RUN_TS,
        "date_utc": NOW_PRETTY,
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
    with open(digest_path, "w") as f:
        json.dump(digest, f, indent=2)
    print(f"Wrote digest to {digest_path}")


if __name__ == "__main__":
    main()
