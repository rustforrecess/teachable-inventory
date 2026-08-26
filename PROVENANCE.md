# Provenance & Inclusion Policy

## Inclusion policy (what a downstream user can rely on)

Every entry in this inventory comes from a **permissive source** — one of:

- **authored** — compiled from uncopyrightable facts by a person;
- **assistant** — drafted by an AI assistant from general knowledge (each such
  entry carries `reviewed: false` until a human verifies it); or
- **mined** — aggregate statistics computed by code from a permissive corpus:
  **CMUdict** (BSD-2-clause), the **Moby** word lists — hyphenation and
  part-of-speech — and **Webster's Unabridged Dictionary 1913**, both Moby and
  Webster's being public domain.

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
#   => CMUdict (BSD-2) / Moby (public domain) / Webster's 1913 (public domain) only
```

If either command surfaces anything outside those sets, it is a lineage bug and
should be treated as release-blocking.

## Lineage

This inventory was extracted from the `vocabulary-measurement-system` data,
whose only external corpora are CMUdict (BSD-2), Moby (public domain) and
Webster's Unabridged 1913 (public domain);
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

Everything redistributed here rests on three permissive sources, all
U.S.-origin (which also sidesteps EU database rights):

| Source | License | Notes |
|--------|---------|-------|
| **Moby Project** (Grady Ward) | **Public domain** | Dedicated to the public domain (1996). ~187k hyphenated words + pronunciations. No rights = no one can charge. |
| **CMU Pronouncing Dictionary** | Permissive (BSD-2-style) | Free for any use incl. commercial + redistribution; retain the notice. Carries stress marks (syllable counts for free). |
| **Webster's Unabridged Dictionary 1913** | **Public domain** | Published 1913, copyright long expired; distributed by Project Gutenberg (#29765). Backs `semantic-dimensions.json`. |

Which licenses are admissible, and the reasoning behind the line, is contributor
policy — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

### Etymology in particular

Etymological claims are **facts**, and facts are what `authored` and
`assistant` entries are made of. A compiled DATABASE of them is a different
thing, and the usable ones are all closed to us:

| Reference | Status |
|-----------|--------|
| **etymonline** (Online Etymology Dictionary) | **Proprietary** — Harper Family LLC. Not public domain, despite being free to read. |
| **Wiktionary** and everything derived from it | CC BY-SA — ShareAlike |
| Etymological WordNet, EtymDB, MorphyNet | CC BY-SA, inherited from Wiktionary |

So an etymon here is checked against a **public-domain** reference and says
which one, with the lemma, the URL and the date consulted:

- **Lewis & Short, A Latin Dictionary (1879)** — for Latin, public domain by age
- **Liddell & Scott, A Greek-English Lexicon** — for Greek, public domain by age
- **Webster's Unabridged 1913** — already a source elsewhere in this inventory

**A public-domain work read through an encumbered interface is still public
domain — but cite the work, not the interface.** Perseus is the obvious place
to look these up and its own licence is CC BY-NC-SA 3.0 for texts and CC BY-SA
4.0 for `PerseusDL/lexica`: NonCommercial *and* ShareAlike, inadmissible here
twice over. That licence covers Perseus's encoding, markup and editorial
matter, not the centuries-old dictionary underneath and not the facts it
states. So a lookup may go through Perseus; a citation may not. Entries point
at a public-domain scan instead, and record the route taken so the distinction
is auditable rather than assumed.

The claim is restated rather than quoted. L&S is out of copyright and could be
quoted freely, but not lifting phrasing is a habit worth keeping uniform,
since the next source may not be.

Two things an etymon must not do. It must not cite a source nobody opened —
`source` means consulted, and a reference merely thought likely belongs
nowhere. And it must not reproduce a particular work's selection of cognates
or its transliterations: a cognate SET is standard scholarship, but which
members are cited and how they are spelled is editorial.

The rule in one line: *the reconstruction is a fact and may be recorded; the
sentence someone wrote about it is theirs.*

### Where this stands, honestly

Sourcing began on 2026-08-26 and covers **6 of 305 combining
forms**. It is not a claim about the rest.

| | count |
|---|---|
| cite a consulted public-domain source | 6 |
| carry an etymon saying explicitly that they are NOT sourced | 2 |
| have no etymon block at all | 297 |
| make an etymological claim in a free-text `note` | 48 |

Those 48 notes are the backlog that matters — "cess is the same root",
"Greek hydro is its counterpart", "septic is NOT this" are all etymological
claims, all assistant-drafted, none checked. They are not wrong so far as
anyone knows; nobody has looked. `reviewed: false` has always said so, and
this table says how much of it there is.

Two things follow. An entry WITHOUT a `source` field makes no sourcing claim —
absence is not an implicit citation. And an entry may say plainly that it is
unsourced, as `auto` and `taxo` do: recording that a lookup was attempted and
failed is worth more than silence, because the next person knows where the
edge is.


## Repository rules that keep the chain clean

1. **Never commit a full third-party corpus.** Downloaded corpora live in
   `data/corpora/` which is **git-ignored**. They are fetched locally for
   evaluation, never redistributed by us.
2. **Only Moby (PD), CMUdict (permissive) and Webster's 1913 (PD) may back
   anything we redistribute.**
3. **Record every source** here with its license, canonical URL, and retrieval
   date before relying on it.
4. **Derived inventories in `data/` ship under CC-BY** (see `LICENSE`) and cite
   the finding they rest on.

## Source log

| Date pulled | Source | Canonical URL | License captured |
|-------------|--------|---------------|------------------|
| 2026-07 | CMUdict | github.com/cmusphinx/cmudict `cmudict.dict` | BSD-2-style (permissive) |
| 2026-07 | Moby Hyphenation List (#3204) | github.com/GITenberg/Moby-Hyphenation-List_3204 `files/mhyph.txt` | Public domain (Grady Ward / PG) |
| 2026-07 | Moby Part-of-Speech List (#3203) | Project Gutenberg #3203 | Public domain (Grady Ward / PG) |
| 2026-07 | Webster's Unabridged Dictionary 1913 | Project Gutenberg #29765 | Public domain (copyright expired) |

Both are eval-only, git-ignored under `data/corpora/`, never redistributed. Moby is used by
`src/tests/SplitEvalTester.js` for split-position agreement (dictionary hyphenation — a relative
signal, NOT an OG reading-syllable gold; see that file's header).
