# Provenance & Clean-Lineage Guarantee

## The guarantee (what a downstream user can rely on)

**This inventory contains no ShareAlike (CC BY-SA) or NonCommercial (CC BY-NC)
data.** Every entry originates from exactly one of:

- **authored** — compiled from uncopyrightable facts by a person;
- **assistant** — drafted by an AI assistant from general knowledge (each such
  entry carries `reviewed: false` until a human verifies it); or
- **mined** — aggregate statistics computed by code from a *permissive* corpus:
  **CMUdict** (BSD-2-clause) and the **Moby** hyphenation list (public domain).

The per-file `_provenance` blocks record which, per batch, and the only three
`method` values that appear are `authored`, `assistant`, and `mined`.

**Explicitly excluded, and verified absent:**

| source | license | why excluded |
| --- | --- | --- |
| WikiMorph | CC BY-**SA** | ShareAlike would propagate to every downstream user |
| MorphoLex-en / the `morphemes` library | CC BY-**NC** | NonCommercial forbids commercial use and model training |
| CELEX | proprietary (LDC) | not redistributable |

**Therefore:** you may build on this data — commercially, in model training, in
app stores, in a CC BY-SA project — **without inheriting any copyleft or
non-commercial obligation.** Attribution (CC BY 4.0) is the only requirement.

## Verify it yourself

The claim is checkable, not just asserted. From the repository root:

```sh
# 1. No excluded source appears anywhere in the data or its provenance:
grep -rin "wikimorph\|morpholex\|by-sa\|sharealike\|non-commercial" en/ shared/   | grep -vi "excluded\|free\|WikiMorph-free"      # only exclusion notes should remain

# 2. Every provenance method is permissive:
grep -roh '"method": *"[a-z]*"' en/ shared/ | sort -u
#   => only "authored", "assistant", "mined"
```

Anything the first command surfaces beyond an *exclusion note* is a lineage bug
and should be treated as release-blocking.

## A note on this project's own history

An earlier, separate experiment (`shared-morpheme-db`, never published) did
ingest WikiMorph under CC BY-SA. **No file, entry, or statistic from it was ever
merged into this inventory** — this repository was extracted from the
WikiMorph-free `vocabulary-measurement-system` data, whose only external corpora
are CMUdict and Moby. The two lineages are physically separate and must stay so;
see CONTRIBUTING for the directional ShareAlike rule (you may give this data *to*
a BY-SA project, never take BY-SA data *in*).

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

## Safe vs. unsafe data sources

| Source | License | Use it? | Notes |
|--------|---------|---------|-------|
| **Moby Project** (Grady Ward) | **Public domain** | ✅ best | Explicitly dedicated to the public domain (1996). ~187k hyphenated words + pronunciations. No rights = no one can charge. |
| **CMU Pronouncing Dictionary** | Permissive (BSD-2-style) | ✅ yes | Free for any use incl. commercial + redistribution; just retain the notice. Has **stress marks** (syllable counts for free). |
| **Wiktionary** | CC BY-**SA** | ⚠️ eval / with care | Not a charge risk (share-alike keeps it free), but SA is "viral": redistributed derivatives must also be BY-SA — incompatible with our CC-BY data. Great for etymology reference; avoid mixing into redistributed corpora. |
| **CELEX2** | LDC, restricted | ❌ eval-only, never bundle | Redistribution prohibited; also may carry EU *sui generis database rights*. Fine to measure against **locally**, never checked in or shipped. |
| Any **CC BY-NC** source | Non-commercial | ❌ avoid | "NC" blocks a district's paid software vendor from using it → not truly free for schools in practice. |
| Any proprietary dictionary | © | ❌ avoid | Obvious. |

### Two traps worth naming
- **EU database rights.** The EU grants a *sui generis* right in databases
  separate from copyright. U.S.-origin sources (Moby, CMUdict) sidestep it.
  Prefer them; that's another reason to avoid CELEX for anything redistributed.
- **Non-commercial (NC) licenses look free but aren't** for schools that buy
  software — the vendor can't legally use NC data, so the school effectively
  can't either. Treat NC as unusable here.

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
