# Validation Results — AGOT OPB Addon Compatibility v1.0.1

Build date: 2026-08-28

## Scope of validation (important)

- **Static validation** (sections 1–3): performed and passing.
- **ck3-tiger syntax/schema validation** (section 4): performed against the AGOT + Immersive Personalities + Royal Court Event Pack + this mod stack.
- **Runtime in-game testing**: **NOT performed** — left to the user (section 5). Do not infer runtime compatibility from the checks below.

---

## 1. Source hash gate (pre-build)

| File | Expected | Actual | Result |
|------|----------|--------|--------|
| `3596393244/common/on_action/zz_gptev_on_actions.txt` | 409a3fc7…8a68a9 | 409a3fc7…8a68a9 | PASS |
| `3596393244/events/zz_gptev_events.txt` | 81400470…c496d | 81400470…c496d | PASS |
| `3596393244/common/defines/zz_gptev_defines.txt` | 0255ba87…1aac | 0255ba87…1aac | PASS |

The defines file is hash-checked only (Module B excluded; not copied).

Current selector-source hashes recorded during independent validation on 2026-08-29:

| File | Recorded SHA-256 | Purpose |
|------|-----------------|---------|
| `3360676953/common/on_action/xx_gptc_on_action_replace.txt` | `d45d56ff2f7ad5979e3638785783de3407986dd20f4f700c5daa560ae2fe8219` | RC source baseline for future rebuilds |
| `2962333032/common/on_action/activities/hold_court_on_actions.txt` | `80ef7c072d8104f857103e0a42e02965e3b489f9ead802329a58e215f7ed95c7` | AGOT selector baseline for future audits |

These two hashes establish the sources inspected on that date. Unlike the three pinned IP hashes above, no pre-build RC/AGOT pins were supplied, so they do not prove historical non-modification before 2026-08-29.

## 2. Module A — Immersive Personalities guards (A1–A4)

Semantic diffs vs. the pinned Workshop sources show **exactly** the four intended changes and nothing else:

| ID | Change | Replacement count | Result |
|----|--------|-------------------|--------|
| A1 | `gpt_on_birthday_animal_archetypes` → `trigger = { age = 16 is_human = yes }` | 1 | PASS |
| A2 (corrected) | `gpt_on_join_court_animal_archetypes` → **root-level** `is_human = yes` inside `trigger`; `scope:new_employer` keeps only `is_ai = no` | 1 | PASS |
| A3 | `gptev_coming_of_age_check` → `trigger = { age = 12 is_human = yes }` | 1 | PASS |
| A4 | `gpt_olympia_animal_archetype.1000` → `is_human = yes` added inside `every_living_character` `limit`, before `age >= 16` | 1 | PASS |

### A2 scope assertions
- Exactly one root-level `is_human = yes` in the A2 trigger (before `scope:new_employer`): **PASS**
- `scope:new_employer` still contains `is_ai = no`: **PASS**
- `scope:new_employer` does **not** contain `is_human = yes`: **PASS**
- Event remains `gpt_olympia_animal_archetype.1001`: **PASS**
- A non-human joiner fails the trigger even when the employer is human; a human joiner still passes when the employer is a human player: **PASS** (by construction)

### `is_human = yes` counts
- Built `common/on_action/zz_gptev_on_actions.txt` = **3** (A1, A2, A3): **PASS**
- Built `events/zz_gptev_events.txt` = **1** (A4): **PASS**
- Built `common/on_action/xx_gptc_on_action_replace.txt` = **0**: **PASS**

## 3. Royal Court court-event selector — same-path VFS override

**File:** `common/on_action/xx_gptc_on_action_replace.txt` — the *exact* virtual path of Royal Court Event Pack's own file (3360676953). It defines `hold_court_event_selection` with **only** the 103 `gptc_hold_court.*` entries (weights, grouping comments, order, and any conditions preserved verbatim). It contains **no** AGOT entries, **no** RC vanilla/hold_court entries, and none of the five disabled IDs.

**Why a same-path VFS override is required (engine behavior, verified):** Two distinct CK3 rules combine here (CK3 Modding wiki, "Override rules" and "On_actions"):

1. **Full-file override:** "If a mod has the same file as the game, it replaces all the contents of the file. (By the same file we mean same path, same filename)… When two mods have the same file, the file of the mod that is lower in the playset is loaded." So this mod's `xx_gptc_on_action_replace.txt` **replaces** RC's file at the same path because this mod loads last.
2. **On_action merge:** "`events`, `random_events` and `on_actions` are appended" across definitions of the same on_action key. So AGOT's separate file `common/on_action/activities/hold_court_on_actions.txt` (75 active entries, incl. `agot_hold_court.1001`/`.1011`, five IDs commented out) **appends** with this gptc-only file.

RC's original file re-listed the full 78-entry vanilla base *in addition to* its gptc entries; that base **re-activated** the five events AGOT deliberately disabled. Because RC's original is now fully overridden (never loaded), that vanilla base is gone. **Effective pool = AGOT's 75 active entries + 103 gptc entries = 178**, with the five disabled IDs absent. This is a genuine VFS file override — **not** a "final same-key definition", and **not** an unresolved runtime limitation.

Programmatic validation (order + weight + id):

| Check | Result |
|-------|--------|
| Override has exactly 103 active `random_events` entries | PASS |
| Every entry is `gptc_hold_court.*` | PASS |
| gptc multiset (id + weight) == RC's `gptc_hold_court.*` exactly (103/103) | PASS |
| Zero `hold_court.*` / `ep3_emperor_yearly.*` / `agot_hold_court.*` / `legend_events.*` entries | PASS |
| All 103 gptc entries weight 50 | PASS |
| 5 group comments + blank-line grouping preserved | PASS |
| Relative path == RC's original `common/on_action/xx_gptc_on_action_replace.txt` | PASS |
| AGOT baseline still 75 active; `agot_hold_court.1001`/`.1011` present; 5 IDs still disabled | PASS |
| Effective pool = 178 (75 AGOT + 103 gptc), no duplicate IDs | PASS |
| Five disabled IDs absent from the effective pool | PASS |

**Counts:** 75 AGOT active entries preserved (in AGOT's own file, unchanged), 103 `gptc_hold_court.*` entries in the override, 178 total effective entries.

## 4. ck3-tiger validation

Tool: `ck3-tiger` v1.19.0 (built from source, `amtep/tiger`). Vanilla game auto-detected (CK3 1.19.0.6 "Scribe").

**Stack** (secondary mods loaded via `load_mod` in a temporary config, then the primary compat mod):
AGOT → Immersive Personalities → Royal Court Event Pack → **AGOT OPB Addon Compatibility**.

Exact command used for the independent live-artifact re-run:
```
/tmp/tiger-src/target/release/ck3-tiger --no-color --config /Users/franco/.lmstudio/scratchpads/rw/tiger_stack/ck3-tiger.conf /Users/franco/.lmstudio/scratchpads/rw/tiger_stack/live_compat.mod
```
`live_compat.mod` points to the installed `agot_opb_addon_compat` folder, and `ck3-tiger.conf` contains `load_mod` entries for the three dependency `.mod` pointers.

**Result with compat mod (full stack):**
```
fatal: 0, error: 0, warning: 0, untidy: 0, tips: 0
No problems found.
```
All four mods loaded and validated with **zero** diagnostics. The independent evaluation ran the same full-stack command four times; all four runs produced the same clean summary. A previously reported intermittent IP `strict-scopes` diagnostic did not reproduce in these runs.

**Baseline runs (for context, same tool/config):**
- AGOT + Immersive Personalities only: `fatal: 0, error: 0, warning: 0, untidy: 0, tips: 0` — clean.
- AGOT + Immersive Personalities + Royal Court Event Pack (no compat): `fatal: 0, error: 0, warning: 0, untidy: 0, tips: 0` — clean.

**Conclusion:** the complete AGOT → Immersive Personalities → Royal Court Event Pack → **AGOT OPB Addon Compatibility** stack reports **no new errors, warnings, or untidy/tips attributable to this patch**. (Note: earlier handoff figures — a single pre-existing AGOT `strict-scopes` note, and 5 RC `missing-item` errors — came from a different Tiger configuration and did **not** reproduce in this re-run; they are therefore not carried into this report. This Tiger run confirms the package is syntactically and schema-clean on the full stack; it does **not** prove runtime behavior, which remains for in-game testing.)

## 5. Runtime checklist (NOT done — for the user)

Test from a **new/disposable save** only. Never test on a live save.

- [ ] A human reaching age 16 receives an Immersive Personalities archetype.
- [ ] An AGOT dragon reaching age 16 receives no `gpt_*` archetype.
- [ ] A dragon at ages 12 and 16 receives no coming-of-age event.
- [ ] A non-human joining a human player's court receives no archetype (corrected A2 root-scope check).
- [ ] A normal human continues receiving the 5-year personality pulse events.
- [ ] As a Royal-Court-owning player ruler: RC court events appear at a sane cadence.
- [ ] The five AGOT-disabled events (6051, 8200, ep3 2060/2070/2090) do **not** fire (confirm the same-path override took effect: with this mod loaded last, RC's re-listed vanilla base is gone).
- [ ] AGOT court behavior (courtier management, court language, `agot_hold_court.1001`/`.1011`) remains intact.
- [ ] `error.log` shows no new `gpt_*`, `gptc_*`, `is_human`, `NRoyalCourt`, or `hold_court` error family from these files.

## 6. Encoding and line endings

| File | BOM | CR count | NUL | Braces (final/min) | Quotes | UTF-8 | Result |
|------|-----|----------|-----|--------------------|--------|-------|--------|
| `common/on_action/zz_gptev_on_actions.txt` | efbbbf | 0 | 0 | 0 / 0 | EVEN | OK | PASS |
| `events/zz_gptev_events.txt` | efbbbf | 0 | 0 | 0 / 0 | EVEN | OK | PASS |
| `common/on_action/xx_gptc_on_action_replace.txt` | efbbbf | 0 | 0 | 0 / 0 | EVEN | OK | PASS |

All gameplay files: UTF-8 with BOM, LF, no NUL, balanced braces, closed quotes. JSON/Markdown/`.mod` metadata: UTF-8, LF, no BOM required.

## 7. Git / install integrity

- Top-level `agot_opb_addon_compat.mod` is Git-ignored (matches `.gitignore:/*.mod`): **PASS**
- Nested `agot_opb_addon_compat/descriptor.mod` is trackable (not ignored): **PASS**
- Current repository state contains no tracked modification outside this mod: **PASS** (`git status --porcelain` showed only `?? agot_opb_addon_compat/`; the top-level pointer is ignored)
- The three pinned IP source hashes match their expected values: **PASS**
- Current RC and AGOT selector hashes are recorded above for future comparison. Because no pre-build RC/AGOT hashes were supplied, historical non-modification before 2026-08-29 is **not claimed**.

## 8. Module B decision

**KEEP Immersive Personalities' flat-5 generated-character skill behavior.** No `defines` override is created; `zz_gptev_defines.txt` is hash-verified only, not copied.

## 9. Rebase warning

If **Immersive Personalities (3596393244)** updates, re-hash `zz_gptev_on_actions.txt` and `zz_gptev_events.txt` against `source_hashes.sha256` and re-apply A1–A4. If **Royal Court Event Pack** changes its `common/on_action/xx_gptc_on_action_replace.txt`, the same-path override must be regenerated (re-extract only the `gptc_hold_court.*` entries from the new RC file). If **AGOT** changes its `common/on_action/activities/hold_court_on_actions.txt`, re-verify the 75-entry baseline and that the five IDs stay disabled. Compare both selector files with the baselines now recorded in `source_hashes.sha256`; treat any changed source hash as a fresh audit trigger.
