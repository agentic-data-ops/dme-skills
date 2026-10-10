#!/usr/bin/env python3
"""Update docs with generated command-group descriptions (provided by the LLM).

- docs/<group>/_index.md: insert a description paragraph under the group heading.
- docs/_topics.md: fill the function column of the command group table.

Run after parse-docs.py; regenerating docs via parse-docs.py will overwrite
these edits, so apply them last.
"""
from __future__ import annotations

import json
import os
import re

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
DESCRIPTIONS = json.load(open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "_group_descriptions.json"),
    encoding="utf-8",
))


def slugify(name: str) -> str:
    """Lowercase, strip non-alphanumeric chars, join whitespace runs with '-'."""
    s = name.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s-]+", "-", s)
    return s.strip("-")


def update_index(group: str, desc: str) -> None:
    path = os.path.join(BASE, group, "_index.md")
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    if len(lines) >= 2 and lines[0].startswith("# ") and not lines[1].strip():
        # Insert description after the heading + blank line
        lines = lines[:2] + [desc, ""] + lines[2:]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def update_topics() -> None:
    path = os.path.join(BASE, "_topics.md")
    with open(path, encoding="utf-8") as f:
        md = f.read()

    def repl(m: re.Match) -> str:
        raw = m.group(1)
        desc = DESCRIPTIONS.get(slugify(raw), "")
        return f"| {raw} | {desc} |"

    md = re.sub(r"^\| ([\w\-]+) \| {2}\|$", repl, md, flags=re.M)
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)


def main() -> None:
    updated = 0
    for group, desc in sorted(DESCRIPTIONS.items()):
        if not desc:
            continue
        update_index(group, desc)
        updated += 1
    update_topics()
    print(f"Updated {updated} group indexes and _topics.md")


if __name__ == "__main__":
    main()
