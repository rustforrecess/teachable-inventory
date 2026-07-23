#!/usr/bin/env python3
"""Regenerate REVIEW.md — the consequence-ordered review worklist.

Run from anywhere: python tools/gen_review.py
Only unreviewed entries appear; marking entries reviewed shrinks the list.
"""
import json, io, collections

import os
R = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "")
def load(p): return json.load(io.open(R + p, encoding="utf-8"))

bv = load("en/base-verbs.json")["verbs"]
iv = load("en/irregular-verbs.json")["verbs"]
dv = load("en/definitional-verbs.json")["definitional_verbs"]
cj = load("en/conjunctions.json")["conjunctions"]
cf = load("shared/combining-forms.json")["forms"]
bm = load("en/base-morphemes.json")["bases"]["list"]

unrev = lambda es: [e for e in es if not e.get("reviewed")]
listed = set()

def fr(v): return "/".join(v["frames"])

# Tier 1: collective flags
t1 = [v for v in unrev(bv) if v.get("collective")]
listed |= {v["form"] for v in t1}
# Tier 2: valency suppressors — avalent, or no transitive/ditransitive frame
t2 = [v for v in unrev(bv) if v["form"] not in listed
      and not ({"transitive", "ditransitive"} & set(v["frames"]))]
listed |= {v["form"] for v in t2}
# Tier 4 pools (behavior-shaping frames), highest-tier-wins
t4d = [v for v in unrev(bv) if v["form"] not in listed and "ditransitive" in v["frames"]]
listed |= {v["form"] for v in t4d}
t4c = [v for v in unrev(bv) if v["form"] not in listed and "clausal" in v["frames"]]
listed |= {v["form"] for v in t4c}
t4v = [v for v in unrev(bv) if v["form"] not in listed and "verb_complement" in v["frames"]]
listed |= {v["form"] for v in t4v}
t4l = [v for v in unrev(bv) if v["form"] not in listed and "linking" in v["frames"]]
listed |= {v["form"] for v in t4l}
# Tier 6: the plain-transitive long tail
t6 = [v for v in unrev(bv) if v["form"] not in listed]

total = len(unrev(bv)) + len(unrev(iv)) + len(unrev(dv)) + len(unrev(cj)) + len(unrev(cf)) + len(unrev(bm))

out = []
w = out.append
w("# Review worklist — consequence-ordered")
w("")
w(f"{total} unreviewed entries across the inventory, ordered by what a wrong")
w("entry actually *breaks* in the engine, so the high-stakes review fits in one")
w("sitting and the long tail can wait. Every entry below is `method: assistant,")
w("reviewed: false` — drafted, never verified.")
w("")
w("**How to sign off:** check the claim, then flip the entry with")
w("`python tools/mark_reviewed.py <file> <form> [<form>…]` (sets")
w("`reviewed: true`). Fix wrong entries in the JSON first, then mark. Re-run")
w("`python tools/gen_review.py` any time to regenerate this list — it only")
w("shows what is still unreviewed.")
w("")
w("---")
w("")
w("## Tier 1 — collective flags (wrong = wrong entailment verdicts)")
w("")
w("`collective: true` makes `DistributionCheck` answer NOT-entailed and blocks")
w("`distribute()`. A wrong flag here produces a wrong verdict, not a missed one.")
w("Also confirm no verb *below* this tier secretly needs the flag.")
w("")
for v in t1:
    w(f"- [ ] **{v['form']}** — {fr(v)}, collective")
w("")
w("## Tier 2 — valency suppressors (wrong = objects silently destroyed)")
w("")
w("These claim the verb licenses NO object, so the engine demotes trailing text")
w("to modifiers. If one of these is actually transitive, its objects vanish —")
w("the only tier where a wrong entry *suppresses* structure.")
w("")
for v in t2:
    w(f"- [ ] **{v['form']}** — {fr(v)}")
w("")
w("## Tier 3 — irregular conjugations (wrong = the verb becomes invisible)")
w("")
w("`base_candidates` reduces surfaces through this table; a wrong past or")
w("participle breaks recognition AND licensing for that verb. Objective facts —")
w("fast to scan.")
w("")
for v in unrev(iv):
    w(f"- [ ] **{v['base']}** — {v['past']} / {v['participle']} ({v.get('pattern','')})")
w("")
w("## Tier 4 — behavior-shaping frames (ditransitive / clausal / verb-complement / linking)")
w("")
w("These frames will gate indirect objects, that-complements and catenative")
w("chains as those land; the demo's valence shell already draws from them.")
w("")
w("### ditransitive claims")
for v in t4d:
    w(f"- [ ] **{v['form']}** — {fr(v)}")
w("")
w("### clausal claims")
for v in t4c:
    w(f"- [ ] **{v['form']}** — {fr(v)}")
w("")
w("### verb-complement claims")
for v in t4v:
    w(f"- [ ] **{v['form']}** — {fr(v)}")
w("")
w("### linking claims (not already above)")
for v in t4l:
    w(f"- [ ] **{v['form']}** — {fr(v)}")
w("")
w("## Tier 5 — definitional verbs (wrong = false coreference matches)")
w("")
w("These become regex alternations in the coref extractor; a bad pattern")
w("rewrites text it shouldn't. Check the pattern shape, not just the word.")
w("")
for e in unrev(dv):
    pat = e.get("pattern", "")
    w(f"- [ ] **{e['form']}** ({e.get('subtype','?')}) — `{pat}`")
w("")
w(f"## Tier 6 — the transitive long tail ({len(t6)} verbs, scan for outliers)")
w("")
w("A wrong `transitive` only over-permits (never suppresses), so these are the")
w("lowest-stakes frames. Scan the list; pull anything suspicious up for a real")
w("check; mark in bulk when a run of them reads right.")
w("")
forms = [v["form"] for v in t6]
for i in range(0, len(forms), 10):
    w("  " + ", ".join(forms[i:i+10]))
w("")
w(f"## Tier 7 — conjunctions ({len(unrev(cj))}, VMS-facing)")
w("")
w("Loom's clause-boundary policy is a hard-coded subset in code (drift-guarded),")
w("so these entries currently gate VMS features, not Loom parsing.")
w("")
by_type = collections.defaultdict(list)
for c in unrev(cj):
    by_type[c.get("type", "?")].append(c["form"])
for t, fs in by_type.items():
    w(f"- **{t}**: " + ", ".join(fs))
w("")
w(f"## Tier 8 — combining forms ({len(unrev(cf))}, glosses + examples)")
w("")
w("Each gates a possible segmentation; individually low-probability, checkable")
w("in bulk. Verify origin + gloss + that the examples really contain the form.")
w("")
forms = [f["form"] for f in unrev(cf)]
for i in range(0, len(forms), 12):
    w("  " + ", ".join(forms[i:i+12]))
w("")
w(f"## Tier 9 — mined bases ({len(unrev(bm))})")
w("")
w("Free-standing-word claims recovered from git history; they authorize short-stem")
w("derivational splits. Confirm each is a real free base.")
w("")
forms = [b["form"] for b in unrev(bm)]
for i in range(0, len(forms), 12):
    w("  " + ", ".join(forms[i:i+12]))
w("")

io.open(R + "REVIEW.md", "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(f"REVIEW.md written: {total} entries, tiers: "
      f"1={len(t1)} 2={len(t2)} 3={len(unrev(iv))} "
      f"4={len(t4d)+len(t4c)+len(t4v)+len(t4l)} 5={len(unrev(dv))} 6={len(t6)} "
      f"7={len(unrev(cj))} 8={len(unrev(cf))} 9={len(unrev(bm))}")
