# corpora/ — fetched, never committed

Reference works downloaded to verify entries. **Everything in this directory is
git-ignored**, deliberately.

`PROVENANCE.md` requires every etymological claim to name a source that was
actually opened. Opening one means having it locally, and having it locally
should not mean redistributing it — so it lands here and stops here.

This applies to public-domain works too. Webster's 1913 could legally be
committed; it still should not be. The inventory ships small derived facts
under CC BY, and bundling a 20 MB dictionary beside them invites exactly the
confusion about what is licensed how that `PROVENANCE.md` exists to prevent.

## What tends to live here

| Work | Licence | Fetch |
|------|---------|-------|
| **Skeat, *A Concise Etymological Dictionary of the English Language*** (1884) | Public domain by age | `curl -L https://archive.org/download/conciseetymologi00skea_0/conciseetymologi00skea_0_djvu.txt -o corpora/skeat-1884.txt` |
| **Liddell & Scott, *Intermediate Greek-English Lexicon*** (1889) | Public domain by age | `curl -L https://archive.org/download/intermediategree00lidd/intermediategree00lidd_djvu.txt -o corpora/lsj-intermediate-1889.txt` |
| Webster's Unabridged Dictionary (1913) | Public domain by age | `curl -L https://www.gutenberg.org/cache/epub/29765/pg29765.txt -o corpora/websters-1913.txt` |
| Lewis & Short, *A Latin Dictionary* (1879, printed as *Harpers' Latin Dictionary* 1891) | Public domain by age | `curl -L https://archive.org/download/harperslatindict01lewi/harperslatindict01lewi_djvu.txt -o corpora/lewis-short-1891.txt` |

### Which to reach for

**Skeat first, for anything English.** It is the only one of the four written
to answer the question this inventory asks — where a word comes from — and it
gives the whole chain in one line: `Prolific. (F. — L.) F. prolifique,
fruitful. — L. proli-, crude form of proles, offspring; -ficus, from facere, to
make.` Headwords are `Capitalised.` at line start, followed by a parenthesised
language chain, so `grep -A3 "^Prolific"` works. Being CONCISE, it carries base
words rather than every derivative: look up `Terror`, not `Terrific`;
`Species`, not `Specific`.

**Intermediate LSJ for Greek roots.** Its OCR preserves real Greek with English
glosses — `ά-δεσιτοτος, ov, {δεσπότης) without master` — which the full Lewis &
Short scan does not manage.

### What these are actually like

**Skeat** — good OCR, purpose-built, best coverage-per-effort. Greek quotations
are garbled (`olKovo/jLia` for οἰκονομία) but the English gloss beside them
survives, and the gloss is what a claim rests on.

**Webster's 1913** is a clean transcription — headwords uppercase on their own
line, so `grep -n "^ECONOMY$"` finds an entry directly. Greek characters were
dropped in transcription, so an etymology can read `fr. Gr. ... + Vicinity,
Nomad` with the Greek word simply missing.

**Lewis & Short** is OCR of a scan and reads like it: `bencdico, bcnefacio`.
Headwords are not recoverable by pattern, abbreviations are dense, Greek is
largely mangled. Good for confirming a claim appears under a lemma; not for
reading an entry end to end.

Where the OCR is unreadable, record the claim as unsourced rather than guessing
at it — naming a source is a promise that someone could check it, and an
unreadable page checks nothing.

## What must never live here

Anything ShareAlike, NonCommercial, or proprietary — Wiktionary and its
derivatives, MorphyNet, MorphoLex, Perseus's own encodings, etymonline. Not
because downloading them is wrong, but because a file sitting in the working
tree is one `git add -A` from becoming a lineage problem, and this repository's
whole value is that its lineage is checkable.
