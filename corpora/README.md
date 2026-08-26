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
| Webster's Unabridged Dictionary (1913) | Public domain by age | `curl -L https://www.gutenberg.org/cache/epub/29765/pg29765.txt -o corpora/websters-1913.txt` |
| Lewis & Short, *A Latin Dictionary* (1879, printed as *Harpers' Latin Dictionary* 1891) | Public domain by age | `curl -L https://archive.org/download/harperslatindict01lewi/harperslatindict01lewi_djvu.txt -o corpora/lewis-short-1891.txt` |

### What these are actually like

**Webster's 1913** is a clean transcription — headwords are uppercase on their
own line, so `grep -n "^ECONOMY$"` finds an entry directly. Its one real
limitation is that Greek characters were dropped in transcription: an
etymology reads `fr. Gr. ... + Vicinity, Nomad`, with the Greek word missing
and only the cross-references left. The Latin glosses survive intact, so the
claim is usually still readable.

**Lewis & Short** is OCR of a scanned 1891 printing, and reads like it:
`bencdico, bcnefacio` for *benedico, benefacio*. Headwords are not reliably
recoverable by pattern, abbreviations are dense (`Curt. 9, 5, 16`), and Greek
is largely mangled. It is good for confirming that a claim appears under a
lemma; it is not good for reading an entry end to end. Where the OCR is
unreadable, say the claim is unsourced rather than guessing at it — the point
of naming a source is that someone could check it, and an unreadable page
checks nothing.

## What must never live here

Anything ShareAlike, NonCommercial, or proprietary — Wiktionary and its
derivatives, MorphyNet, MorphoLex, Perseus's own encodings, etymonline. Not
because downloading them is wrong, but because a file sitting in the working
tree is one `git add -A` from becoming a lineage problem, and this repository's
whole value is that its lineage is checkable.
