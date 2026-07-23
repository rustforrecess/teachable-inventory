# Review worklist — consequence-ordered

983 unreviewed entries across the inventory, ordered by what a wrong
entry actually *breaks* in the engine, so the high-stakes review fits in one
sitting and the long tail can wait. Every entry below is `method: assistant,
reviewed: false` — drafted, never verified.

**How to sign off:** check the claim, then flip the entry with
`python tools/mark_reviewed.py <file> <form> [<form>…]` (sets
`reviewed: true`). Fix wrong entries in the JSON first, then mark. Re-run
`python tools/gen_review.py` any time to regenerate this list — it only
shows what is still unreviewed.

---

## Tier 1 — collective flags (wrong = wrong entailment verdicts)

`collective: true` makes `DistributionCheck` answer NOT-entailed and blocks
`distribute()`. A wrong flag here produces a wrong verdict, not a missed one.
Also confirm no verb *below* this tier secretly needs the flag.

- [ ] **assemble** — transitive/intransitive, collective
- [ ] **collide** — intransitive, collective
- [ ] **combine** — transitive/intransitive, collective
- [ ] **converge** — intransitive, collective
- [ ] **correspond** — intransitive, collective
- [ ] **huddle** — intransitive, collective
- [ ] **intersect** — intransitive/transitive, collective
- [ ] **meet** — transitive/intransitive, collective
- [ ] **merge** — intransitive/transitive, collective
- [ ] **overlap** — transitive/intransitive, collective
- [ ] **unite** — transitive/intransitive, collective

## Tier 2 — valency suppressors (wrong = objects silently destroyed)

These claim the verb licenses NO object, so the engine demotes trailing text
to modifiers. If one of these is actually transitive, its objects vanish —
the only tier where a wrong entry *suppresses* structure.

- [ ] **agree** — intransitive/clausal
- [ ] **apologize** — intransitive
- [ ] **appear** — intransitive/linking
- [ ] **argue** — intransitive/clausal
- [ ] **arrive** — intransitive
- [ ] **be** — intransitive/linking
- [ ] **become** — linking
- [ ] **come** — intransitive
- [ ] **complain** — intransitive/clausal
- [ ] **comply** — intransitive
- [ ] **consist** — intransitive
- [ ] **crawl** — intransitive
- [ ] **creep** — intransitive
- [ ] **cry** — intransitive
- [ ] **dance** — intransitive
- [ ] **default** — intransitive
- [ ] **depart** — intransitive
- [ ] **depend** — intransitive
- [ ] **die** — intransitive
- [ ] **differ** — intransitive
- [ ] **drift** — intransitive
- [ ] **drizzle** — avalent
- [ ] **emerge** — intransitive
- [ ] **exist** — intransitive
- [ ] **experiment** — intransitive
- [ ] **fail** — intransitive/verb_complement
- [ ] **fall** — intransitive
- [ ] **flow** — intransitive
- [ ] **fluctuate** — intransitive
- [ ] **glide** — intransitive
- [ ] **go** — intransitive
- [ ] **hail** — avalent
- [ ] **happen** — intransitive
- [ ] **hope** — intransitive/clausal/verb_complement
- [ ] **hurry** — intransitive
- [ ] **insist** — intransitive/clausal
- [ ] **jump** — intransitive
- [ ] **laugh** — intransitive
- [ ] **lie** — intransitive
- [ ] **listen** — intransitive
- [ ] **live** — intransitive
- [ ] **look** — intransitive/linking
- [ ] **occur** — intransitive
- [ ] **persist** — intransitive
- [ ] **pour** — avalent
- [ ] **rain** — avalent
- [ ] **remain** — intransitive/linking
- [ ] **reply** — intransitive/clausal
- [ ] **respond** — intransitive/clausal
- [ ] **rise** — intransitive
- [ ] **seem** — linking/verb_complement
- [ ] **sit** — intransitive
- [ ] **sleep** — intransitive
- [ ] **sleet** — avalent
- [ ] **slip** — intransitive
- [ ] **smile** — intransitive
- [ ] **snow** — avalent
- [ ] **sound** — linking
- [ ] **spring** — intransitive
- [ ] **stand** — intransitive
- [ ] **stay** — intransitive/linking
- [ ] **swear** — intransitive/clausal
- [ ] **swim** — intransitive
- [ ] **talk** — intransitive
- [ ] **tend** — verb_complement/intransitive
- [ ] **think** — intransitive/clausal
- [ ] **thunder** — avalent
- [ ] **travel** — intransitive
- [ ] **vary** — intransitive
- [ ] **wait** — intransitive/verb_complement
- [ ] **wander** — intransitive
- [ ] **weep** — intransitive
- [ ] **wonder** — clausal/intransitive

## Tier 3 — irregular conjugations (wrong = the verb becomes invisible)

`base_candidates` reduces surfaces through this table; a wrong past or
participle breaks recognition AND licensing for that verb. Objective facts —
fast to scan.

- [ ] **bear** — bore / borne (ear-ore-orn)
- [ ] **become** — became / become (come-came-come)
- [ ] **begin** — began / begun (i-a-u)
- [ ] **bend** — bent / bent (d-to-t)
- [ ] **bind** — bound / bound (ind-ound)
- [ ] **bite** — bit / bitten (ide-ode-idden)
- [ ] **blow** — blew / blown (ow-ew-own)
- [ ] **break** — broke / broken (eak-oke-oken)
- [ ] **bring** — brought / brought (augh-ough)
- [ ] **build** — built / built (d-to-t)
- [ ] **burst** — burst / burst (no-change)
- [ ] **buy** — bought / bought (augh-ough)
- [ ] **cast** — cast / cast (no-change)
- [ ] **catch** — caught / caught (augh-ough)
- [ ] **choose** — chose / chosen (eak-oke-oken)
- [ ] **come** — came / come (come-came-come)
- [ ] **cost** — cost / cost (no-change)
- [ ] **creep** — crept / crept (vowel-shorten-t)
- [ ] **cut** — cut / cut (no-change)
- [ ] **deal** — dealt / dealt (vowel-shorten-t)
- [ ] **dig** — dug / dug (vowel-change-same)
- [ ] **draw** — drew / drawn (ow-ew-own)
- [ ] **drink** — drank / drunk (i-a-u)
- [ ] **drive** — drove / driven (ide-ode-idden)
- [ ] **eat** — ate / eaten (distinct-participle)
- [ ] **fall** — fell / fallen (distinct-participle)
- [ ] **feed** — fed / fed (spelling-same-sound-change)
- [ ] **feel** — felt / felt (vowel-shorten-t)
- [ ] **fight** — fought / fought (augh-ough)
- [ ] **find** — found / found (ind-ound)
- [ ] **fly** — flew / flown (ow-ew-own)
- [ ] **forget** — forgot / forgotten (distinct-participle)
- [ ] **forgive** — forgave / forgiven (ive-ave-iven)
- [ ] **freeze** — froze / frozen (eak-oke-oken)
- [ ] **get** — got / gotten (distinct-participle)
- [ ] **give** — gave / given (ive-ave-iven)
- [ ] **go** — went / gone (suppletive)
- [ ] **grow** — grew / grown (ow-ew-own)
- [ ] **hang** — hung / hung (vowel-change-same)
- [ ] **hear** — heard / heard (vowel-change-same)
- [ ] **hide** — hid / hidden (ide-ode-idden)
- [ ] **hit** — hit / hit (no-change)
- [ ] **hold** — held / held (vowel-change-same)
- [ ] **hurt** — hurt / hurt (no-change)
- [ ] **keep** — kept / kept (vowel-shorten-t)
- [ ] **know** — knew / known (ow-ew-own)
- [ ] **lay** — laid / laid (vowel-change-same)
- [ ] **lead** — led / led (spelling-same-sound-change)
- [ ] **leave** — left / left (vowel-shorten-t)
- [ ] **lend** — lent / lent (d-to-t)
- [ ] **let** — let / let (no-change)
- [ ] **lie** — lay / lain (suppletive)
- [ ] **light** — lit / lit (spelling-same-sound-change)
- [ ] **lose** — lost / lost (vowel-shorten-t)
- [ ] **make** — made / made (vowel-change-same)
- [ ] **mean** — meant / meant (vowel-shorten-t)
- [ ] **meet** — met / met (spelling-same-sound-change)
- [ ] **mistake** — mistook / mistaken (ake-ook-aken)
- [ ] **pay** — paid / paid (vowel-change-same)
- [ ] **put** — put / put (no-change)
- [ ] **quit** — quit / quit (no-change)
- [ ] **read** — read / read (spelling-same-sound-change)
- [ ] **ride** — rode / ridden (ide-ode-idden)
- [ ] **ring** — rang / rung (i-a-u)
- [ ] **rise** — rose / risen (ide-ode-idden)
- [ ] **run** — ran / run (come-came-come)
- [ ] **say** — said / said (vowel-change-same)
- [ ] **see** — saw / seen (distinct-participle)
- [ ] **seek** — sought / sought (augh-ough)
- [ ] **sell** — sold / sold (vowel-change-same)
- [ ] **send** — sent / sent (d-to-t)
- [ ] **set** — set / set (no-change)
- [ ] **sew** — sewed / sewn (regular-past-irregular-participle)
- [ ] **shake** — shook / shaken (ake-ook-aken)
- [ ] **shoot** — shot / shot (spelling-same-sound-change)
- [ ] **show** — showed / shown (regular-past-irregular-participle)
- [ ] **shrink** — shrank / shrunk (i-a-u)
- [ ] **shut** — shut / shut (no-change)
- [ ] **sing** — sang / sung (i-a-u)
- [ ] **sink** — sank / sunk (i-a-u)
- [ ] **sit** — sat / sat (vowel-change-same)
- [ ] **sleep** — slept / slept (vowel-shorten-t)
- [ ] **speak** — spoke / spoken (eak-oke-oken)
- [ ] **spend** — spent / spent (d-to-t)
- [ ] **split** — split / split (no-change)
- [ ] **spread** — spread / spread (no-change)
- [ ] **spring** — sprang / sprung (i-a-u)
- [ ] **stand** — stood / stood (vowel-change-same)
- [ ] **steal** — stole / stolen (eak-oke-oken)
- [ ] **stick** — stuck / stuck (vowel-change-same)
- [ ] **strike** — struck / struck (vowel-change-same)
- [ ] **swear** — swore / sworn (ear-ore-orn)
- [ ] **sweep** — swept / swept (vowel-shorten-t)
- [ ] **swim** — swam / swum (i-a-u)
- [ ] **take** — took / taken (ake-ook-aken)
- [ ] **teach** — taught / taught (augh-ough)
- [ ] **tear** — tore / torn (ear-ore-orn)
- [ ] **tell** — told / told (vowel-change-same)
- [ ] **think** — thought / thought (augh-ough)
- [ ] **throw** — threw / thrown (ow-ew-own)
- [ ] **understand** — understood / understood (vowel-change-same)
- [ ] **wake** — woke / woken (eak-oke-oken)
- [ ] **wear** — wore / worn (ear-ore-orn)
- [ ] **weep** — wept / wept (vowel-shorten-t)
- [ ] **win** — won / won (vowel-change-same)
- [ ] **wind** — wound / wound (ind-ound)
- [ ] **write** — wrote / written (ide-ode-idden)

## Tier 4 — behavior-shaping frames (ditransitive / clausal / verb-complement / linking)

These frames will gate indirect objects, that-complements and catenative
chains as those land; the demo's valence shell already draws from them.

### ditransitive claims
- [ ] **ask** — ditransitive/clausal/transitive
- [ ] **bring** — ditransitive/transitive
- [ ] **buy** — ditransitive/transitive
- [ ] **cost** — transitive/ditransitive
- [ ] **feed** — transitive/ditransitive
- [ ] **forgive** — transitive/ditransitive
- [ ] **give** — ditransitive/transitive
- [ ] **lend** — ditransitive/transitive
- [ ] **offer** — ditransitive/transitive
- [ ] **owe** — transitive/ditransitive
- [ ] **pass** — transitive/intransitive/ditransitive
- [ ] **pay** — ditransitive/intransitive/transitive
- [ ] **promise** — ditransitive/clausal/verb_complement
- [ ] **save** — transitive/ditransitive
- [ ] **sell** — ditransitive/intransitive/transitive
- [ ] **send** — ditransitive/transitive
- [ ] **show** — ditransitive/clausal/transitive
- [ ] **teach** — ditransitive/transitive
- [ ] **tell** — ditransitive/clausal/transitive
- [ ] **throw** — transitive/ditransitive

### clausal claims
- [ ] **add** — clausal/transitive
- [ ] **admit** — transitive/clausal
- [ ] **advise** — transitive/clausal/verb_complement
- [ ] **announce** — transitive/clausal
- [ ] **assume** — transitive/clausal
- [ ] **believe** — clausal/transitive
- [ ] **certify** — transitive/clausal
- [ ] **claim** — clausal/transitive
- [ ] **conclude** — clausal/transitive
- [ ] **consider** — transitive/clausal
- [ ] **convince** — transitive/clausal/verb_complement
- [ ] **decide** — clausal/transitive/verb_complement
- [ ] **demand** — transitive/clausal
- [ ] **demonstrate** — clausal/transitive
- [ ] **deny** — transitive/clausal
- [ ] **determine** — clausal/transitive
- [ ] **discover** — transitive/clausal
- [ ] **doubt** — transitive/clausal
- [ ] **estimate** — clausal/transitive
- [ ] **expect** — clausal/transitive/verb_complement
- [ ] **explain** — clausal/transitive
- [ ] **find** — clausal/transitive
- [ ] **forget** — transitive/clausal/verb_complement
- [ ] **guess** — clausal/transitive
- [ ] **hear** — transitive/clausal
- [ ] **imagine** — transitive/clausal
- [ ] **infer** — transitive/clausal
- [ ] **judge** — transitive/clausal
- [ ] **know** — clausal/transitive
- [ ] **learn** — intransitive/clausal/transitive
- [ ] **mean** — clausal/transitive
- [ ] **mention** — transitive/clausal
- [ ] **note** — clausal/transitive
- [ ] **notice** — transitive/clausal
- [ ] **observe** — clausal/transitive
- [ ] **perceive** — transitive/clausal
- [ ] **predict** — clausal/transitive
- [ ] **prove** — clausal/transitive
- [ ] **realize** — transitive/clausal
- [ ] **recall** — transitive/clausal
- [ ] **recognize** — transitive/clausal
- [ ] **remember** — transitive/clausal/verb_complement
- [ ] **remind** — transitive/clausal/verb_complement
- [ ] **report** — clausal/transitive
- [ ] **request** — transitive/clausal
- [ ] **say** — clausal/transitive
- [ ] **see** — transitive/clausal
- [ ] **state** — clausal/transitive
- [ ] **suggest** — clausal/transitive
- [ ] **understand** — clausal/transitive
- [ ] **warn** — transitive/clausal

### verb-complement claims
- [ ] **allow** — transitive/verb_complement
- [ ] **attempt** — transitive/verb_complement
- [ ] **avoid** — transitive/verb_complement
- [ ] **begin** — intransitive/transitive/verb_complement
- [ ] **cause** — transitive/verb_complement
- [ ] **choose** — transitive/verb_complement
- [ ] **continue** — intransitive/transitive/verb_complement
- [ ] **enable** — transitive/verb_complement
- [ ] **encourage** — transitive/verb_complement
- [ ] **enjoy** — transitive/verb_complement
- [ ] **finish** — transitive/intransitive/verb_complement
- [ ] **hate** — transitive/verb_complement
- [ ] **have** — transitive/verb_complement
- [ ] **help** — transitive/verb_complement
- [ ] **instruct** — transitive/verb_complement
- [ ] **intend** — transitive/verb_complement
- [ ] **invite** — transitive/verb_complement
- [ ] **like** — transitive/verb_complement
- [ ] **love** — transitive/verb_complement
- [ ] **manage** — transitive/verb_complement
- [ ] **need** — transitive/verb_complement
- [ ] **persuade** — transitive/verb_complement
- [ ] **plan** — transitive/verb_complement
- [ ] **prefer** — transitive/verb_complement
- [ ] **prepare** — transitive/intransitive/verb_complement
- [ ] **quit** — transitive/intransitive/verb_complement
- [ ] **refuse** — transitive/verb_complement
- [ ] **require** — transitive/verb_complement
- [ ] **start** — intransitive/transitive/verb_complement
- [ ] **try** — transitive/verb_complement
- [ ] **want** — transitive/verb_complement

### linking claims (not already above)
- [ ] **feel** — intransitive/linking/transitive
- [ ] **smell** — linking/transitive/intransitive
- [ ] **taste** — linking/transitive
- [ ] **turn** — transitive/intransitive/linking

## Tier 5 — definitional verbs (wrong = false coreference matches)

These become regex alternations in the coref extractor; a bad pattern
rewrites text it shouldn't. Check the pattern shape, not just the word.

- [ ] **be** (equative) — `X is Y`
- [ ] **equal** (equative) — `X equals Y`
- [ ] **constitute** (equative) — `X constitutes Y`
- [ ] **represent** (equative) — `X represents Y`
- [ ] **amount** (equative) — `X amounts to Y`
- [ ] **correspond** (equative) — `X corresponds to Y`
- [ ] **call** (naming) — `X is called Y / we call X Y`
- [ ] **name** (naming) — `X is named Y`
- [ ] **term** (naming) — `X is termed Y`
- [ ] **label** (naming) — `X is labeled Y`
- [ ] **designate** (naming) — `X is designated (as) Y`
- [ ] **refer** (naming) — `X, referred to (herein) as Y`
- [ ] **know** (naming) — `X, (also) known as Y / a.k.a.`
- [ ] **dub** (naming) — `X, dubbed Y`
- [ ] **style** (naming) — `X, styled Y`
- [ ] **entitle** (naming) — `X is entitled Y / titled Y`
- [ ] **hereinafter** (naming) — `X (hereinafter Y) / (hereinafter referred to as Y)`
- [ ] **mean** (defining) — `X means Y`
- [ ] **define** (defining) — `X is defined as Y / we define X as Y`
- [ ] **denote** (defining) — `X denotes Y`
- [ ] **signify** (defining) — `X signifies Y`
- [ ] **connote** (defining) — `X connotes Y`
- [ ] **describe** (defining) — `X describes Y`
- [ ] **specify** (defining) — `X specifies Y`
- [ ] **stand** (defining) — `X stands for Y`
- [ ] **classify** (classifying) — `X is classified as Y`
- [ ] **categorize** (classifying) — `X is categorized as Y`
- [ ] **belong** (classifying) — `X belongs to Y`
- [ ] **count** (classifying) — `X counts as Y`
- [ ] **qualify** (classifying) — `X qualifies as Y`
- [ ] **fall** (classifying) — `X falls under Y`
- [ ] **comprise** (meronymic) — `X comprises Y`
- [ ] **consist** (meronymic) — `X consists of Y`
- [ ] **include** (meronymic) — `X includes Y`
- [ ] **equivalent** (equivalence) — `X is equivalent to Y`
- [ ] **synonymous** (equivalence) — `X is synonymous with Y`
- [ ] **same** (equivalence) — `X is the same as Y`
- [ ] **tantamount** (equivalence) — `X is tantamount to Y`
- [ ] **identify** (naming) — `X is identified as Y`
- [ ] **collectively** (naming) — `X and Z, collectively the Y`

## Tier 6 — the transitive long tail (219 verbs, scan for outliers)

A wrong `transitive` only over-permits (never suppresses), so these are the
lowest-stakes frames. Scan the list; pull anything suspicious up for a real
check; mark in bulk when a run of them reads right.

  absorb, accrue, affect, align, analyze, answer, apply, approach, approve, arrange
  attract, audit, bear, beat, bend, bind, bite, blow, borrow, bounce
  break, build, burst, calculate, call, cancel, capitalize, carry, cast, catch
  change, cite, classify, clean, climb, close, collect, compare, conduct, construct
  consume, contain, contrast, convert, cook, count, cover, create, cross, cut
  deal, decline, decrease, define, deposit, describe, design, detect, develop, dig
  discuss, divide, do, draw, drink, drive, drop, eat, edit, emit
  end, enter, evaluate, exceed, exert, exit, fight, file, fill, float
  fly, follow, form, freeze, gather, generate, get, graph, greet, group
  grow, hang, hide, hit, hold, hurt, identify, improve, include, increase
  incur, investigate, involve, issue, join, keep, kick, label, lay, lead
  leave, lift, light, liquidate, list, lose, make, match, measure, mistake
  model, move, multiply, negotiate, obtain, open, paint, place, play, plot
  point, practice, process, produce, provide, pull, push, put, question, raise
  reach, read, receive, record, redeem, reduce, reflect, register, relate, release
  remit, renew, repel, represent, research, resist, restate, return, review, revise
  ride, ring, roll, run, rush, seek, serve, set, settle, sew
  share, shoot, shrink, shut, simplify, sing, sink, slide, solve, sort
  speak, spend, spin, split, spread, stage, steal, stick, stop, store
  strike, study, subtract, summarize, support, sweep, take, tear, test, thank
  touch, transfer, transform, translate, transmit, use, visit, wake, walk, wash
  watch, wear, welcome, win, wind, withdraw, withhold, work, write

## Tier 7 — conjunctions (70, VMS-facing)

Loom's clause-boundary policy is a hard-coded subset in code (drift-guarded),
so these entries currently gate VMS features, not Loom parsing.

- **coordinating**: for, and, nor, but, or, yet, so
- **correlative**: both … and, either … or, neither … nor, not only … but also, whether … or, as … as, such … that, so … that, no sooner … than, rather … than
- **subordinating**: after, before, when, whenever, while, since, until, till, once, as, as soon as, by the time, now that, because, so that, in order that, if, unless, provided, providing, as long as, in case, even if, only if, whether, although, though, even though, whereas, than, as if, as though, just as, where, wherever, how, lest
- **conjunctive_adverb**: however, therefore, moreover, nevertheless, consequently, furthermore, otherwise, thus, hence, meanwhile, besides, instead, accordingly, subsequently, likewise, still

## Tier 8 — combining forms (270, glosses + examples)

Each gates a possible segmentation; individually low-probability, checkable
in bulk. Verify origin + gloss + that the examples really contain the form.

  an, ana, atmo, bi, cata, centi, circum, con, dec, deca, deci, di
  dia, dodeca, dys, ecto, endo, ennea, epi, equi, eu, exo, giga, hepta
  hetero, hexa, homo, in, infra, inter, intra, iso, kilo, macro, mega, meta
  micro, milli, mono, multi, nano, non, non, oct, omni, para, penta, per
  peri, poly, pro, proto, quadr, quint, semi, sept, sext, sub, super, syn
  tele, tetra, trans, tri, ultra, uni, act, aero, agr, angul, ann, anthrop
  aqu, arch, astro, av, baro, bio, calc, capit, carb, cardio, carn, ced
  cent, centr, cerebr, chem, chloro, chromo, chron, cip, circ, clin, cosm, cred
  cult, curv, cycl, cyto, dem, dent, dermo, dict, doc, duc, duct, dur
  dyna, electro, encephal, erg, fac, fenestr, ferr, fin, flect, flor, flu, form
  fract, gam, gastr, geo, germ, glaci, gluc, glyc, gnos, grad, gram, grav
  greg, helio, hemo, hepat, herb, hist, hydro, iatr, integ, ion, ject, kary
  kine, later, lev, lin, lip, litho, loc, log, luc, lun, magn, magnet
  mar, med, mer, meteor, metr, migr, min, mit, morph, mort, mot, nat
  nav, necr, neuro, nom, nom, nov, nucle, numer, ocean, od, odont, opt
  ord, oste, ov, ox, paed, path, ped, pend, petr, phag, phil, phob
  phono, phys, phyto, polis, popul, port, pos, potent, press, prote, psych, puls
  put, pyro, radi, radic, rect, rupt, sacchar, sal, scal, sci, scrib, script
  sect, seism, sens, sequ, sol, son, soph, spect, spir, spor, sta, stell
  struct, tech, temp, tend, terr, thermo, ton, top, tract, val, var, vect
  ven, ver, vert, vit, viv, vol, vulcan, zoo, zyg, cyte, gen, gon
  lysis, naut, oid, philic, phobic, phore, phyll, phyte, plankt, plasm, pod, some
  sphere, stasis, stat, thesis, troph, vore

## Tier 9 — mined bases (87)

Free-standing-word claims recovered from git history; they authorize short-stem
derivational splits. Confirm each is a real free base.

  active, adjust, aggressive, allow, arm, arrange, attractive, bear, believe, bend, blue, care
  charge, clear, close, comfort, competitive, complete, conscious, cool, count, crisp, dear, deliver
  develop, draft, dress, dry, elect, employ, enforce, export, fair, forgive, fresh, grace
  grate, hand, health, high, install, insure, issue, large, late, light, like, manage
  mark, mind, narrow, near, nice, occupy, organize, pass, pay, position, present, press
  print, question, rare, record, sale, sensitive, service, shake, sharp, size, slow, sound
  stock, support, talk, taste, terse, trace, trade, treat, true, tune, use, wear
  white, whole, work

