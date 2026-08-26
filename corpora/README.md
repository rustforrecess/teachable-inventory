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
| Lewis & Short, *A Latin Dictionary* (1879) | Public domain by age | archive.org: `harperslatindict01lewi` |

## What must never live here

Anything ShareAlike, NonCommercial, or proprietary — Wiktionary and its
derivatives, MorphyNet, MorphoLex, Perseus's own encodings, etymonline. Not
because downloading them is wrong, but because a file sitting in the working
tree is one `git add -A` from becoming a lineage problem, and this repository's
whole value is that its lineage is checkable.
