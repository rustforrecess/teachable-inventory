# Provenance & Inclusion Policy

## Inclusion policy (what a downstream user can rely on)

Every entry in this inventory comes from a **permissive source** — one of:

- **authored** — compiled from uncopyrightable facts by a person;
- **assistant** — drafted by an AI assistant from general knowledge (each such
  entry carries `reviewed: false` until a human verifies it); or
- **mined** — aggregate statistics computed by code from a permissive corpus:
  **CMUdict** (BSD-2-clause) and the **Moby** hyphenation list (public domain).

Those are the *only* admissible sources. New data is accepted from CC0, CC BY,
MIT, BSD, Apache-2.0, or public-domain origins, and from nothing else — see
[`CONTRIBUTING.md`](CONTRIBUTING.md) for the rule contributors follow.

The whole inventory is therefore **CC BY 4.0**, and attribution is the only
obligation it carries. You may build on it — commercially, in model training,
in app stores, or as an input to a copyleft project — with nothing else to
inherit.

## Verify it yourself

The policy is checkable, not just asserted. From the repository root:

```sh
# Every provenance method is one of the three permissive kinds:
grep -roh '"method": *"[a-z]*"' en/ shared/ | sort -u
#   => only "authored", "assistant", "mined"

# Every declared external source is permissive:
grep -rho '"source": *"[^"]*"' en/ shared/ | sort -u
#   => CMUdict (BSD-2) / Moby (public domain) only
```

If either command surfaces anything outside those sets, it is a lineage bug and
should be treated as release-blocking.

## Lineage

This inventory was extracted from the `vocabulary-measurement-system` data,
whose only external corpora are CMUdict (BSD-2) and Moby (public domain);
everything else is authored from facts or assistant-drafted. Every source is
permissive, so the inventory may be given freely to any project, including a
copyleft one. The one directional rule — permissive flows in, copyleft never
does — is stated for contributors in [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

# Data Provenance & "Free Forever" Policy

The goal: this engine and its inventory must be **permanently free for schools**,
with no path for anyone to later assert rights and charge for it. This file
records *why* that holds and *which* data sources are safe to use.

> This is engineering/policy documentation, not formal legal advice. Before a
> public release, a one-time review by IP counsel is cheap insurance. The
> analysis below is the standard open-data reasoning and is deliberately
> conservative.

## Why "free forever" actually holds

1. **Open licenses are irrevocable.** MIT, Apache-2.0, CC-BY, CC0 and a public-
   domain dedication cannot be retracted. Once a version is released under them,
   every downstream user — including every school — keeps those rights **even if
   the author later changes their mind or sells the project.** No one can claw it
   back and start charging existing users.

2. **The core content is facts, and facts aren't copyrightable.** In the U.S.,
   *Feist v. Rural Telephone* (1991) held that facts and mere "sweat-of-the-brow"
   compilations lack copyright — only original *selection/arrangement* gets thin
   protection. A word's pronunciation, syllable count, and morpheme structure are
   facts. Our derived corpora and inventories are largely **uncopyrightable
   facts**; the open license we add is belt-and-suspenders, not the only defense.

3. **We compile independently from facts** and never redistribute any
   copyrighted curriculum's text or curated lists (see `../CREDITS.md`).

## Sources used

Everything redistributed here rests on two permissive sources, both
U.S.-origin (which also sidesteps EU database rights):

| Source | License | Notes |
|--------|---------|-------|
| **Moby Project** (Grady Ward) | **Public domain** | Dedicated to the public domain (1996). ~187k hyphenated words + pronunciations. No rights = no one can charge. |
| **CMU Pronouncing Dictionary** | Permissive (BSD-2-style) | Free for any use incl. commercial + redistribution; retain the notice. Carries stress marks (syllable counts for free). |

Which licenses are admissible, and the reasoning behind the line, is contributor
policy — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Repository rules that keep the chain clean

1. **Never commit a full third-party corpus.** Downloaded corpora live in
   `data/corpora/` which is **git-ignored**. They are fetched locally for
   evaluation, never redistributed by us.
2. **Only Moby (PD) and CMUdict (permissive) may back anything we redistribute.**
3. **Record every source** here with its license, canonical URL, and retrieval
   date before relying on it.
4. **Derived inventories in `data/` ship under CC-BY** (see `LICENSE`) and cite
   the finding they rest on.

## Source log

| Date pulled | Source | Canonical URL | License captured |
|-------------|--------|---------------|------------------|
| 2026-07 | CMUdict | github.com/cmusphinx/cmudict `cmudict.dict` | BSD-2-style (permissive) |
| 2026-07 | Moby Hyphenation List (#3204) | github.com/GITenberg/Moby-Hyphenation-List_3204 `files/mhyph.txt` | Public domain (Grady Ward / PG) |

Both are eval-only, git-ignored under `data/corpora/`, never redistributed. Moby is used by
`src/tests/SplitEvalTester.js` for split-position agreement (dictionary hyphenation — a relative
signal, NOT an OG reading-syllable gold; see that file's header).
