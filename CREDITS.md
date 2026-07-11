# Credits & Research Lineage

The Vocabulary Measurement System is built on decades of published research into
English orthography and structured-literacy instruction. This file credits the
researchers and traditions whose **findings** the engine and its data inventory
rest on.

**How to read this file.** We credit *findings* by scholarly citation. We do
**not** reproduce any author's copyrighted text, curated lists, or specific
scope-and-sequence arrangement. The facts of English orthography (grapheme–
phoneme correspondences, positional rules, base morphemes) are not owned by
anyone; our inventory (`data/`, CC BY 4.0) is an **independent compilation from
these facts**, attributed here out of academic and professional respect.

---

## Orthographic regularity — the quantitative backbone

- **Hanna, P. R., Hanna, J. S., Hodges, R. E., & Rudorf, E. H. (1966).**
  *Phoneme–Grapheme Correspondences as Cues to Spelling Improvement.*
  U.S. Office of Education. (ERIC ED128835.) — The foundational computer
  analysis of 17,310 words establishing that English is far more regular than
  its reputation: ~50% spellable from sound alone, ~84% with position and
  morphology. The engine's honest predictive ceiling comes from this work.

- **Venezky, R. L. (1970).** *The Structure of English Orthography.* Mouton.
  **(1999).** *The American Way of Spelling.* Guilford. — English orthography is
  patterned and **morphophonemic** (it preserves meaning units), not chaotic.

- **Kessler, B., & Treiman, R. (2001; 2003).** "Is English Spelling Chaotic?
  Misconceptions Concerning Its Irregularity." *Reading Psychology* 24(3–4),
  267–289. — Spelling–sound consistency rises sharply once the **position** of a
  phoneme and the **identity of neighboring graphemes** (especially the rime)
  are taken into account. The theoretical basis for our rime-first and
  origin-marker rules.

- **Treiman, R., & Kessler, B. (2002).** "Context sensitivity in the spelling of
  English vowels." *Journal of Memory and Language.* — Vowel spellings become
  more predictable when the surrounding consonants are considered.

- **Siegelman, N., Kearns, D. M., & Rueckl, J. G. (2020).** *Behavior Research
  Methods* 52(3), 1292–1312. — The consonant **following** a vowel predicts its
  pronunciation better than the one preceding it (coda-conditioned entropy 0.25
  vs onset 0.37 vs unconditional 0.69 bits). Directly motivates rime-first
  vowel decisions.

- **Berndt, R. S., Reggia, J. A., & Mitchum, C. C. (1987).** *Behavior Research
  Methods, Instruments & Computers* 19, 1–9. — Empirical grapheme→phoneme
  probabilities from a 17,310-word corpus.

- **Gontijo, P. F. D., Gontijo, I., & Shillcock, R. (2003).** *Behavior Research
  Methods* 35, 136–157. — Large-corpus grapheme–phoneme association analysis
  (~461 associations, ~2.4 phonemes per grapheme).

## Structured literacy — the pedagogy of a finite, teachable rule set

- **Orton–Gillingham tradition** (Samuel T. Orton; Anna Gillingham). — The
  multisensory, explicit, cumulative approach and the phonogram concept from
  which the finite GPC-plus-rules architecture descends.

- **Spalding, R. B. (1957).** *The Writing Road to Reading.* — Operationalized
  the Orton phonograms into a finite teaching set.

- **Riggs Institute** (Myrna McCulloch). — Extension of the phonogram tradition.

- **Moats, L. C.** *Speech to Print: Language Essentials for Teachers.* — The
  modern articulation of orthography-informed instruction; popularized the
  "only ~4% truly irregular" reading of Hanna et al.

- **Ehri, L. C.** — Orthographic-mapping theory, underpinning the "heart word"
  approach: decode the regular part, memorize only the deviant grapheme(s).

- **Eide, D. (2011; 3rd ed. 2018).** *Uncovering the Logic of English.* Logic of
  English. — The argument that English is highly regular once a full phonogram-
  and-rule system is taught, and the multi-sound-phonogram framing (e.g. "ch"
  as Greek /k/, French /ʃ/, English /tʃ/). We report her claims and use the
  shared underlying facts; we do not reproduce her curated lists or text.

- **UFLI Foundations** (University of Florida Literacy Institute) and the
  **Wilson Reading System.** — Consulted as published examples of finite,
  ordered scope-and-sequences and of positional rules (FLOSS, -ck, closed-
  syllable exceptions) taught as generalizations rather than word lists.

---

*A fuller synthesis with inline source URLs, verification notes, and the
predict-vs-explain analysis is in [`docs/g2p-research.md`](docs/g2p-research.md).*
