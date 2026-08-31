# Validation results — AGOT Unified Compatibility Patch v1.0.0

Consolidation date: 2026-08-30

This document records the **consolidation** of six local patch mods into one. It does not restate
the per-patch validation histories, which are preserved verbatim in `legacy/` and remain the
authoritative record for anything predating this date.

## What consolidation did and did not change

- **Game files: unchanged.** All 91 were copied byte-identical and verified by SHA-256 on both
  sides. Zero content edits.
- **Packaging: changed.** Six folders, six `descriptor.mod` files and six launcher pointers became
  one of each.
- **Load position: changed.** The six mods occupied positions 58–65 with Immersive Personalities
  (63) and Royal Court Event Pack (64) interleaved. The unified mod sits after all of them.

## Pre-consolidation safety checks

| Check | Result |
|---|---|
| Game-file path collisions across the six mods | **0** — 91 files to 91 unique paths |
| Executable references to a mod folder name in any game file | **0** |
| `replace_path` declarations to reconcile | **0** — none of the six declared any |
| Load-order winner flips from moving to the end | **0** |
| Database-key collisions with Immersive Personalities / Royal Court Event Pack | 5, all `on_action` |

The five `on_action` hits are not override conflicts. CK3 merges same-named `on_action` entries
across files rather than replacing them — sixteen mods in this playset define `on_game_start`. Four
of the five carry no `trigger` on either side. The fifth, `quarterly_playable_pulse`, has a trigger
on the Observer Stack side only, gating that definition's own events.

The only collisions found were nine documentation files (three `SOURCE_MANIFEST.txt` at mod root
and the `README.md` / `manifest/*` sets). None are loaded by CK3. All nine originals are preserved
under `legacy/` rather than being overwritten.

## Post-consolidation verification

| Check | Result |
|---|---|
| Files copied | 91 of 91 |
| Copies hash-identical to source | **91 / 91** |
| `build_manifest.json` entries | 91 |
| Entries whose `built_sha256` matches disk | **91 / 91** |
| Upstream SOURCE gates re-checked against the Workshop | **79 checked, 0 stale** |
| Entries with no SOURCE gate | 11, all genuinely new files with no upstream parent |
| Original doc/manifest files preserved verbatim | 15 |
| Declared dependencies after removing self-references | 18 |

The 11 gate-less entries are the `zz_`-prefixed database-key overrides, the Mega Wars event and
localization files, and the two `localization/replace/` fixes. None derive from a Workshop file, so
a SOURCE hash would be meaningless for them.

## Manifest schema unification

Three incompatible formats were merged programmatically, not by hand:

- `build_manifest.json` from Observer Stack (70 entries) and Seasons + Personality (7), which use
  `provider_workshop_id` / `source_sha256` and `merge_base_workshop_id` / `base_sha256`
  respectively.
- OPB's nested schema (3 entries) using `expected_source_sha256` / `actual_source_sha256`.
- Flat `KEY=VALUE` text in `SOURCE_MANIFEST.txt` for MIV (5 files), Mega Wars (4) and Claimant
  Faction (2). These had no JSON representation; entries were generated from the file provenance
  map, with upstream providers resolved by path lookup against the enabled playset and hashes
  computed from disk.

Every entry now carries `virtual_path`, `origin_patch`, `provider_workshop_id`, `provider_name`,
`transformations`, `source_sha256` (where one exists) and `built_sha256` in one schema.

## Carried forward unresolved

- **P24 and P36 remain confirmed NOT working.** See the README before retrying either; three
  approaches are already known to fail and the remaining one needs an in-game test.
- The known-unpatched list in the README (`on_action_namespace.192`, Seasons
  `middle_of_year_season_trigger`, Seasons `remove_doctrine`, vanilla tournament/feast weak scopes,
  EP3 external estate construction, DireWolves `make_unprunable`) is unchanged by consolidation.

## Runtime status

**VERIFIED** across four playtests for the patch content, as recorded in the README and in
`legacy/observer_stack_validation_results.md`.

**The consolidation itself is statically verified only.** Game files are provably identical and the
load-order analysis is complete, but the unified mod has not yet been loaded in-game. First launch
should confirm: the launcher lists one local mod, the guard HUD buttons no longer overlap Search &
Trade / Advanced Character Search, and `error.log` shows no new load-time entries naming a path
this mod owns.
