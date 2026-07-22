# Contributing

This repository is **data only** — no code, one licence, one question to answer
before anything is merged: *where did this come from?*

## The promise

**Free for schools, forever.** Not "free for now" — free in a way nobody can
revoke, including us.

- **Open licences are irrevocable.** CC BY 4.0 cannot be pulled back. Every
  school keeps its rights even if this project is sold or abandoned.
- **The content is facts.** Morphemes, verb forms and grapheme–phoneme
  correspondences are facts about English, and facts are not copyrightable
  (*Feist v. Rural Telephone*, 1991). These inventories are independent
  compilations from those facts. The licence is belt-and-braces, not the only
  defence.

Both are fragile in exactly one way: **a single entry with unclear provenance
poisons the whole chain**, and cleaning up afterwards is expensive or
impossible. That is why the rule below is not negotiable.

**Licence:** everything here is CC BY 4.0 — see [`LICENSE`](LICENSE). By
contributing you agree your work is released under it.

**Sign your commits** using the
[DCO](https://developercertificate.org/) — no CLA, no rights assignment:

```bash
git commit -s -m "your message"
```

## Where entries may come from

When a pull request adds or changes entries, **say in the PR where they came
from.** One of these must be true:

✅ **Your own compilation from facts.** You listed the morphemes or forms
yourself, from knowledge or from published *findings* you cite. This is how the
whole inventory was built — see [`CREDITS.md`](CREDITS.md), which credits
researchers by citation without reproducing anyone's lists.

✅ **A CC0, CC BY, MIT, BSD, Apache-2.0 or public-domain source**, recorded in
[`PROVENANCE.md`](PROVENANCE.md) with the retrieval date.

❌ **Anything with a non-commercial (NC) clause.** NC poisons distribution
through app stores, model training, and every downstream user. MorphoLex-en
(CC BY-NC-SA) and the `morphemes` Python library that wraps it are permanently
excluded — do not reintroduce them, not even as a dev-time convenience.

❌ **ShareAlike (CC BY-SA) coming IN.** It would relicense this inventory and
everything built on it.

✅ **ShareAlike going OUT is fine, and encouraged.** The restriction is
directional and people routinely read it as a blanket ban:

| direction | allowed? | why |
| --- | --- | --- |
| this data → into a CC BY-SA project | **yes** | CC BY is a compatible input; the combined work becomes BY-SA |
| CC BY-SA data → into this inventory | **no** | ShareAlike propagates to everything downstream |

Contributing this work **back to Wiktionary** is exactly what CC BY was chosen
to allow. Merging Wiktionary or WikiMorph content *in* is what breaks the chain.

❌ **Scraped or unattributable data**, or a curated list copied from a
curriculum, textbook or commercial programme. Copying someone's *selection and
arrangement* is not copying facts — that is the part they do own.

❓ **Unsure?** Open an issue before doing the work. Email the dataset author if
a licence is unclear. Asking is cheap; untangling a licence later is not.

## Record provenance for what you add

Every inventory carries a `_provenance` block with per-batch records. **Add one
for your batch.** Fields:

| field | meaning |
| --- | --- |
| `date` | when |
| `commit_subject` | the commit's subject line — deliberately not a hash, which means nothing to a human reader and breaks if history is ever rewritten |
| `method` | `authored` (compiled from facts by a person), `mined` (derived by code from a corpus named in PROVENANCE.md), or `assistant` (drafted by an AI assistant at a maintainer's direction and accepted by them) |
| `by` | who |
| `scope` | what the batch covers |
| `prompted_by` | *optional but valuable* — what made this necessary |

All three methods produce uncopyrightable facts, so none threatens the
free-forever promise. Recording which is which lets a downstream user filter —
a school may reasonably want teacher-verified entries only — and keeps the
chain auditable by someone who was not here.

An individual entry needing its own sourcing may carry a `prov` field directly.

## Keep the inventories honest

Each file has a `_meta` block with `title`, `description`, `license`,
`credits`, `source_notes` and `status`. Keep it accurate. **If your change makes
an inventory less of a seed, update `status`** — readers rely on knowing how
complete a list claims to be.

Prefer a fact that generalises over a special case. These are teachable
inventories: a list that grows without a principle stops being teachable.

## Consumers

This repository is canonical. Consumers vendor a copy rather than depending on
it at build time, so that each stays simple to run. If you change a schema,
say so clearly in the PR — someone else's sync will pick it up.
