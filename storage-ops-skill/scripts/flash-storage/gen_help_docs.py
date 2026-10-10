#!/usr/bin/env python3
"""Parse the flash-storage command reference into topic/command help files.

Reads:    ../reference/flash-storage/command-reference.md
Writes:   docs/_topics.md
          docs/<topic-slug>/_index.md
          docs/<topic-slug>/<command-slug>.md

All code comments, docstrings and console output are in English.
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

import json

REF_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "reference", "flash-storage", "command-reference.md",
)
DOCS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "docs",
)
# Command group descriptions (LLM-generated summaries), keyed by group slug.
# Used when generating _topics.md and <group>/_index.md.
_DESC_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "config", "command-group-description.json",
)
with open(_DESC_PATH, encoding="utf-8") as _f:
    GROUP_DESCRIPTIONS: Dict[str, str] = json.load(_f)

# Topics excluded from the topic list (intro/guide chapters, not command topics)
EXCLUDED_TOPICS = {
    "About This Document",
    "CLI Use Guidance",
    "High-Risk Command List",
    "How to Obtain Help",
    "Glossary",
    "Acronyms and Abbreviations",
}

# Redundant prefix removed from command function descriptions,
# e.g. 'The **create lun** command is used to create LUNs.' -> 'create LUNs.'
# The word 'command' is optional (some entries omit it), and a few source
# entries contain typos like 'command to used to' instead of 'command is used to'.
_FUNCTION_PREFIX_RE = re.compile(
    r"^The\s+\*{0,2}[^*]+\*{0,2}\s+(?:command\s+)?(?:is|to)?\s*used\s+to\s+",
    re.IGNORECASE,
)

_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def slugify(name: str) -> str:
    """Lowercase, strip non-alphanumeric chars, join whitespace runs with '-'."""
    s = name.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s-]+", "-", s)
    return s.strip("-")


def link_text(line: str) -> str:
    """Extract the display text of a markdown link, e.g. '[base](#base)' -> 'base'."""
    m = _LINK_RE.search(line)
    return m.group(1) if m else line.strip()


# ---------------------------------------------------------------------------
# Reference document model
# ---------------------------------------------------------------------------

class Command:
    def __init__(self, name: str, body: List[str], function: str = ""):
        self.name = name
        self.body = body
        self.function = function


class CommandGroup:
    def __init__(self, name: str, commands: List[Command]):
        self.name = name
        self.commands = commands


class Topic:
    def __init__(self, name: str, intro: List[str], groups: List[CommandGroup]):
        self.name = name
        self.intro = intro
        self.groups = groups


def parse_reference(lines: List[str]) -> List[Topic]:
    """Parse the markdown reference into a list of Topic objects.

    Heading levels in the reference:
        ##  topic            (h2)
        ### command group    (h3)
        #### command         (h4)
        ##### section        (h5, e.g. Function / Format / Parameters)
    """
    # Locate heading lines
    headings: List[Tuple[int, int, str]] = []  # (line_no, level, text)
    for i, line in enumerate(lines):
        m = _HEADING_RE.match(line)
        if m:
            headings.append((i, len(m.group(1)), m.group(2).strip()))

    topics: List[Topic] = []
    for idx, (h2_no, h2_level, h2_text) in enumerate(headings):
        if h2_level != 2 or h2_text in EXCLUDED_TOPICS:
            continue
        # Range of this topic: until the next h2 or h1
        end = next(
            (ln for ln, lv, _ in headings[idx + 1:] if lv <= 2),
            len(lines),
        )
        topic_lines = lines[h2_no + 1:end]

        # Topic intro: lines before the first link line
        intro: List[str] = []
        for line in topic_lines:
            if _LINK_RE.search(line) or _HEADING_RE.match(line):
                break
            if line.strip():
                intro.append(line.strip())

        # Command groups inside this topic
        groups: List[CommandGroup] = []
        inner_headings = [(ln, lv, tx) for ln, lv, tx in headings if h2_no < ln < end]
        for gidx, (h3_no, h3_level, h3_text) in enumerate(inner_headings):
            if h3_level != 3:
                continue
            g_end = next(
                (ln for ln, lv, _ in inner_headings[gidx + 1:] if lv <= 3),
                end,
            )
            group_lines = lines[h3_no + 1:g_end]
            # Commands: h4 headings inside this group range
            commands: List[Command] = []
            cmd_headings = [
                (ln, lv, tx) for ln, lv, tx in inner_headings
                if h3_no < ln < g_end and lv == 4
            ]
            for cidx, (h4_no, _lv, h4_text) in enumerate(cmd_headings):
                c_end = next(
                    (ln for ln, lv, _ in cmd_headings[cidx + 1:] if lv <= 4),
                    g_end,
                )
                body = lines[h4_no + 1:c_end]
                function = extract_function(body)
                commands.append(Command(h4_text, body, function))
            groups.append(CommandGroup(h3_text, commands))

        topics.append(Topic(h2_text, intro, groups))

    return topics


def extract_function(body: List[str]) -> str:
    """Extract the first paragraph of the '##### Function' section."""
    lines = body
    for i, line in enumerate(lines):
        if line.strip() == "##### Function":
            for para in lines[i + 1:]:
                if not para.strip():
                    continue
                text = para.strip()
                text = _FUNCTION_PREFIX_RE.sub("", text)
                return text
            break
    return ""


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------

def write_docs(topics: List[Topic]) -> None:
    """Generate all docs/ files from the parsed topics."""
    os.makedirs(DOCS_DIR, exist_ok=True)

    # _topics.md
    topic_lines = ["# Flash Storage Topics", ""]
    for t in topics:
        topic_lines.append(f"## {t.name}")
        topic_lines.append("")
        if t.intro:
            topic_lines.extend(t.intro)
            topic_lines.append("")
        topic_lines.append("| command group | function |")
        topic_lines.append("|---|---|")
        for g in t.groups:
            name = g.name.replace("|", "\\|")
            desc = GROUP_DESCRIPTIONS.get(slugify(g.name), "")
            topic_lines.append(f"| {name} | {desc} |")
        topic_lines.append("")
    with open(os.path.join(DOCS_DIR, "_topics.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(topic_lines))

    slug_used: Dict[str, int] = defaultdict(int)
    conflict_log: List[str] = []

    for t in topics:
        for g in t.groups:
            group_dir = os.path.join(DOCS_DIR, slugify(g.name))
            os.makedirs(group_dir, exist_ok=True)

            # Command group index: _index.md (description + markdown table)
            index_lines = [f"# {g.name}", ""]
            desc = GROUP_DESCRIPTIONS.get(slugify(g.name), "")
            if desc:
                index_lines += [desc, ""]
            index_lines += ["| command | function |", "|---|---|"]
            for cmd in g.commands:
                name = cmd.name.replace("|", "\\|")
                function = (cmd.function or "").replace("|", "\\|")
                index_lines.append(f"| {name} | {function} |")
            with open(os.path.join(group_dir, "_index.md"), "w", encoding="utf-8") as f:
                f.write("\n".join(index_lines))

            # Command help files
            for cmd in g.commands:
                base = slugify(cmd.name)
                slug_used[base] += 1
                n = slug_used[base]
                if n > 1:
                    # Keep only the first variant of a duplicated command slug
                    conflict_log.append(f"{cmd.name} skipped (duplicate slug '{base}')")
                    continue
                content = [f"# {cmd.name}", ""] + cmd.body
                with open(os.path.join(group_dir, f"{base}.md"), "w", encoding="utf-8") as f:
                    f.write("\n".join(content))

    # stats
    total_cmds = sum(len(g.commands) for t in topics for g in t.groups)
    total_files = sum(
        len([f for f in os.listdir(os.path.join(DOCS_DIR, slugify(g.name)))
             if f.endswith(".md") and f != "_index.md"])
        for t in topics for g in t.groups
    )
    print(f"Topics: {len(topics)}")
    print(f"Command groups: {sum(len(t.groups) for t in topics)}")
    print(f"Commands: {total_cmds}")
    print(f"Command files: {total_files}")
    if conflict_log:
        print("Slug conflicts:")
        for c in conflict_log:
            print(f"  {c}")


def main() -> None:
    if not os.path.exists(REF_PATH):
        sys.exit(f"Reference not found: {REF_PATH}")
    with open(REF_PATH, encoding="utf-8") as f:
        lines = f.read().split("\n")
    topics = parse_reference(lines)
    write_docs(topics)


if __name__ == "__main__":
    main()
