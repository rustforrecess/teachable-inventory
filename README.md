# Teachable Decoding Inventory (`data/`)

Open, fact-based data that the engine uses to resolve cases the pure-grapheme
rules leave underdetermined — the small, *teachable* inventories that structured
literacy relies on (base morphemes, origin markers, core GPCs).

**License:** [CC BY 4.0](LICENSE) — any school, curriculum, or product may use,
adapt, and redistribute this, with attribution. **Credits:** see
[`../CREDITS.md`](../CREDITS.md).

## Principles for anything added here

1. **Facts only.** Every entry is a fact about English orthography (a base
   morpheme, a grapheme's sound, an origin marker), not a word-by-word answer
   key and not a copy of any curriculum's curated list.
2. **Finite and teachable.** These are the bounded inventories a child is
   actually taught (a few dozen affixes, a handful of origin markers, ~100 base
   morphemes to start) — the one principled way past the from-letters residue
   (e.g. `farm` is a base, so `farmer` = farm+er, but `corn` here is not treated
   as a productive base of `corner`).
3. **Attributed at the row level.** Each file carries a `_meta` block and, where
   a specific finding backs an entry, a `source_notes` field citing it.
4. **Not sound-from-word.** These inventories condition sound/structure on
   *letters and finite teachable sets*, never on word frequency or a whole-word
   pronunciation lookup. (See `docs/g2p-research.md` §0.)

## Files

| File | Purpose | Status |
|------|---------|--------|
| `gpc-table.json` | Core grapheme→phoneme correspondences, ordered by frequency, with positional context | seed |
| `origin-markers.json` | Greek/French orthographic markers that disambiguate origin-sensitive graphemes (e.g. `ch`) | seed |
| `base-morphemes.json` | Finite list of base words/roots + affixes, to resolve morpheme boundaries | seed |
| `articulation.json` | Place/manner/voicing + "how a child FEELS each sound" — the multisensory teaching layer | seed |

All three are **seeds** — deliberately small, correct starting points meant to
be expanded. Growing them is the "Option B" inventory work discussed in the
project notes.
