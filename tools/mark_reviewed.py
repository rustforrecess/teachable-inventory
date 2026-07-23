#!/usr/bin/env python3
"""Mark inventory entries reviewed: python tools/mark_reviewed.py <file> <form>...

<file> is repo-relative (e.g. en/base-verbs.json). Finds each <form> by its
"form" (or "base") key and sets "reviewed": true. Refuses silently-missing
forms — every argument must match exactly one entry.
"""
import io, json, os, sys, collections
NL = chr(10)

if len(sys.argv) < 3:
    sys.exit(__doc__)
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(root, sys.argv[1])
forms = set(sys.argv[2:])
d = json.load(io.open(path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)

def entry_lists(node):
    if isinstance(node, list) and node and isinstance(node[0], dict) and (
        "form" in node[0] or "base" in node[0]
    ):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from entry_lists(v)

hit = collections.Counter()
for lst in entry_lists(d):
    for e in lst:
        key = e.get("form", e.get("base"))
        if key in forms:
            e["reviewed"] = True
            hit[key] += 1

missing = forms - set(hit)
dupes = [f for f, n in hit.items() if n > 1]
if missing:
    sys.exit(f"not found: {sorted(missing)} — nothing written")
if dupes:
    sys.exit(f"ambiguous (multiple entries): {dupes} — nothing written")
io.open(path, "w", encoding="utf-8", newline=NL).write(
    json.dumps(d, indent=2, ensure_ascii=False) + NL
)
print(f"marked reviewed in {sys.argv[1]}: {' '.join(sorted(hit))}")
