"""Converts Outline's ::: type ... ::: notice containers into MkDocs
(Material + admonition extension) "!!! type" admonition blocks.

Outline (the wiki this site mirrors) exports callouts as containers like:

    :::info
    Some content here.

    :::

mkdocs.yml already enables the `admonition` extension, whose native syntax is:

    !!! info
        Some content here.

Can be imported (`convert_admonitions`) from the scraper's post-processing
step, or run directly to rewrite already-downloaded markdown files in place,
e.g. when the source site is unreachable and re-scraping isn't an option:

    python3 admonitions.py docs
"""

import os
import re

ADMONITION_RE = re.compile(
    r'^[ \t]*:::[ \t]*([A-Za-z][\w-]*)[ \t]*\n'
    r'(.*?)'
    r'\n[ \t]*:::[ \t]*$',
    re.MULTILINE | re.DOTALL,
)


def _indent_body(body: str) -> str:
    lines = body.strip('\n').split('\n')
    return '\n'.join('    ' + line if line.strip() else '' for line in lines)


def _replace(match: 're.Match[str]') -> str:
    admonition_type = match.group(1).lower()
    return f'!!! {admonition_type}\n\n{_indent_body(match.group(2))}'


def convert_admonitions(content: str) -> str:
    normalized = content.replace('\r\n', '\n').replace('\r', '\n')
    return ADMONITION_RE.sub(_replace, normalized)


if __name__ == "__main__":
    import sys

    root = sys.argv[1] if len(sys.argv) > 1 else "docs"
    changed_files = 0
    converted_blocks = 0
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            path = os.path.join(dirpath, filename)
            with open(path, "r", encoding="utf-8") as f:
                original = f.read()

            updated = convert_admonitions(original)
            if updated != original:
                block_count = len(ADMONITION_RE.findall(
                    original.replace('\r\n', '\n').replace('\r', '\n')
                ))
                with open(path, "w", encoding="utf-8") as f:
                    f.write(updated)
                changed_files += 1
                converted_blocks += block_count
                print(f"Converted {block_count} block(s) in {path}")

    print(f"\nDone: {converted_blocks} admonition block(s) across {changed_files} file(s).")
