# AGOT OPB Addon Compatibility

A small compatibility patch that makes **Immersive Personalities** (Workshop 3596393244) safe to run alongside **A Game of Thrones** (AGOT), and that fixes a court-event collision between **Royal Court Event Pack** (3360676953) and AGOT. It is load-order dependent: it must be the **last** mod in the playset.

## What it does

### 1. Dragon / non-human guards (Immersive Personalities)

Immersive Personalities assigns animal "archetype" traits (`gpt_badger`, `gpt_dragon`, etc.) to living characters via four entry points. AGOT dragons are living characters that take birthdays, so those entry points can reach non-humans. This mod adds `is_human = yes` guards to exactly those four points:

| ID | Location | Guard |
|----|----------|-------|
| A1 | `gpt_on_birthday_animal_archetypes` trigger | `age = 16 is_human = yes` |
| A2 | `gpt_on_join_court_animal_archetypes` trigger (ROOT scope) | `is_human = yes` added at root; `scope:new_employer` keeps only `is_ai = no` |
| A3 | `gptev_coming_of_age_check` trigger | `age = 12 is_human = yes` |
| A4 | `gpt_olympia_animal_archetype.1000` → `every_living_character` limit | `is_human = yes` added before `age >= 16` |

**A2 scope note:** in `on_join_court`, ROOT is the character *joining* the court and `scope:new_employer` is its employer. The guard must be on ROOT (the joiner), so that a non-human joining a human-controlled court is excluded while a human joining the same court still qualifies.

The 508-event personality dispatch chain (player-pulse scope) is **untouched**.

### 2. Royal Court court-event selector — same-path VFS override

Both AGOT and Royal Court Event Pack (RC) define the on_action key `hold_court_event_selection`. Two CK3 rules combine (CK3 Modding wiki, "Override rules" and "On_actions"): (a) a file at the **same virtual path** fully overrides an earlier mod's file with that path when it loads later, and (b) `random_events` lists are **appended** across separate definitions of the same on_action key.

RC's own file `common/on_action/xx_gptc_on_action_replace.txt` re-listed the full 78-entry vanilla base *in addition to* its gptc entries; that base re-activated five events AGOT deliberately disabled. To stop that, this mod ships a file at the **exact same path** — `common/on_action/xx_gptc_on_action_replace.txt` — containing **only** the 103 `gptc_hold_court.*` entries (weights, group comments, order, and conditions preserved verbatim). Because this mod loads **last**, it fully replaces RC's file (RC's vanilla base is never loaded). AGOT's separate `common/on_action/activities/hold_court_on_actions.txt` still loads and appends.

- **AGOT's** `hold_court_event_selection` is left untouched (75 active entries, weights, `#AGOT Disabled` comments, and `agot_hold_court.1001` / `.1011` preserved);
- the five AGOT-disabled events (`hold_court.6051`, `hold_court.8200`, `ep3_emperor_yearly.2060/2070/2090`) stay **inactive** — they appear only as commented-out lines, not active entries, in AGOT's file, and RC's active re-listing is no longer loaded;
- the **103** `gptc_hold_court.*` entries (all weight 50) come from the same-path override;
- **effective pool = 75 AGOT + 103 gptc = 178 entries.**

File: `common/on_action/xx_gptc_on_action_replace.txt` (103 gptc entries; 0 AGOT/vanilla entries).

## What it deliberately does NOT change

- AGOT content (no AGOT file is overwritten or modified in place).
- The 508-event personality dispatch chain.
- The `gpt_dragon` personality archetype (a label, not an AGOT dragon).
- The `paranoid` trait redefinition (accepted as additive).
- The flat-5 `RANDOM_CHARACTER_*` skill generation (Module B excluded by user decision).
- Any **other** Royal Court Event Pack file. The only RC file this mod overrides is `common/on_action/xx_gptc_on_action_replace.txt`, and that override is load-order dependent (this mod must load after RC).
- Any existing local compatibility patch.

## Required dependencies

- A Game of Thrones (2962333032)
- Immersive Personalities (3596393244)
- Royal Court Event Pack (3360676953)

## Required relative load order

1. AGOT and all AGOT submods / local patches load first.
2. **Immersive Personalities** loads after AGOT.
3. **Royal Court Event Pack** loads after AGOT.
4. **AGOT OPB Addon Compatibility** loads after both Workshop mods — **last** in the playset.

The last-position requirement is **mandatory**, not a suggestion: it is what (a) makes this mod's `is_human` guards the final on_action definitions, and (b) guarantees that this mod's `common/on_action/xx_gptc_on_action_replace.txt` loads after Royal Court Event Pack's file at the same path (so RC's re-listed vanilla base is not loaded). If this mod loads **before RC**, RC's original selector wins and re-activates the five AGOT-disabled events. Keeping the compatibility mod last also prevents a later mod from replacing the same virtual path. Set the load order in the CK3 launcher; do not edit `dlc_load.json` manually.

## Validation performed vs. remaining runtime tests

- **Static validation (done):** semantic diffs vs. pinned Workshop sources, brace/string/UTF-8/NUL/line-ending checks, programmatic validation of the same-path gptc override (103 entries, gptc-only, weights/grouping preserved; AGOT baseline intact; effective pool 75+103=178; five disabled IDs absent), and a fresh-source hash gate. See `manifest/validation_results.md`.
- **ck3-tiger syntax/schema validation (done):** run against the complete AGOT + Immersive Personalities + Royal Court Event Pack + this mod stack. See the report in `manifest/validation_results.md`.
- **Runtime tests (NOT done — for you):** dragon vs. human archetype assignment, coming-of-age on a dragon, personality pulse regression, court-event cadence, and error-log inspection must be done in a **new or disposable save** only. Never test on a live save. See the runtime checklist in `manifest/validation_results.md`.
