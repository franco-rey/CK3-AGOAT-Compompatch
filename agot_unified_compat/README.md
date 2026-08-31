# AGOT Unified Compatibility Patch v1.0.0

A single local layer holding every compatibility fix for this playset. Targets CK3 1.19.0.6 /
AGOT 0.5.1 against the 66-mod AGOT playset.

Consolidated on 2026-08-30 from six separate local mods. **No game file was changed by the
consolidation** — all 91 files were copied byte-identical and verified by hash. Only the packaging
changed: one folder, one `descriptor.mod`, one launcher pointer, one manifest.

## Load position — read this first

**This mod must be the last entry in the playset, after every Workshop mod.**

That is inherited, not arbitrary. The OPB layer inside it ships
`common/on_action/xx_gptc_on_action_replace.txt` at the same virtual path as Royal Court Event
Pack, and only wins by loading later. Placing this mod anywhere before Royal Court Event Pack
silently reverts that patch.

Verified at consolidation time: no mod loading after any of the six original patches claimed a
path any of them owned, so moving them all to the end flips no winner.

## What it contains

| Origin patch | Version | Files | Covers |
|---|---|---|---|
| AGOT Observer Stack Compatibility | 1.1.0 | 70 | The bulk: AGOT, AGOT+, Royal Guards, Grand Remembrance, Oathbound, ACS, House Founders, Expanded Domiciles, DireWolves, Duel Overlay, Active Courtiers |
| AGOT Seasons + Personality Compatibility | 1.0.0 | 7 | More Personality Depth, Seasons of Ice and Fire, and their displacement of House Founders / DireWolves / AGOT |
| MIV - AGOT CB Compatibility | 1.0.1 | 5 | More Interactive Vassals casus belli and FP3 struggle |
| AGOT - Mega Wars Revolt Succession Fix | 1.1.0 | 4 | AGOT Mega Wars revolt and rebellion succession |
| AGOT OPB Addon Compatibility | 1.0.1 | 3 | Immersive Personalities animal archetypes, Royal Court Event Pack hold-court selector |
| AGOT - Claimant Faction War Fix | 1.0.0 | 2 | AGOT claimant faction wars and the creation interaction |

91 game files. Full per-file provenance, transformation IDs and hash gates are in
`manifest/build_manifest.json`; every original document is preserved verbatim under
`manifest/legacy/`.

## Confirmed NOT working — do not assume these are fixed

**P24** (Grand Remembrance chronicle window) and **P36** (guard academy HUD binding). Both try to
gate a scripted-GUI call inside `And(...)`, which in CK3 GUI **evaluates every argument** rather
than short-circuiting. Three approaches are already known to fail:

1. A script-side `exists = this` in `is_shown` — the scope is rejected before the trigger body runs.
2. Reordering the `And()` arguments so `GetPlayer.IsValid` comes first — logically identical.
3. Patching further call sites of a guard that does not work.

The untried approach is a parent-container gate: an outer widget whose `visible` is
`[GetPlayer.IsValid]` alone, with the `IsShown` call on a child. Vanilla uses that idiom in
`hud.gui`, but never alongside a scripted-GUI call, so there is **no static proof** CK3 suppresses
a child's `visible` evaluation under an invisible parent. Settle it with an in-game observer-mode
test, not more file reading.

## Do NOT "fix" these — they are correct as they stand

- **Seasons of Ice and Fire winter tiers.** Seasons deliberately splits AGOT's
  `winter_normal_modifier` into `winter_north/normal_1/cold/light/southern`, all defined in its own
  `common/modifiers/seasons_modifiers.txt`. Lines that look "lost" in `00_weather_triggers.txt`,
  `00_map_related_custom_loc.txt`, `07_ep3_custom_loc.txt`, `01_event_backgrounds.txt` and
  `00_hunt_triggers.txt` are old-tier checks being superseded. Restoring AGOT's versions breaks the
  seasons system.
- **More Personality Depth's own design choices.** In `gui/window_character.gui`, the
  `ai_personality` text keeps `visible = yes` (MPD shows it for players too) and `secondary_widget`
  keeps `position = { 310 0 }` (shifted from AGOT's 300 for MPD's own content).
- **`paranoid` removed from MPD's XP roll.** `add_trait_xp` without a track name fails outright on
  a multi-track trait, so paranoid was already receiving no XP. The calls were no-ops that logged
  23,209 entries in one run. Do not "restore" them, and do not guess a track name — the merged
  track identifiers cannot be determined statically.
- **`on_action` entries with the same name merge across mods** rather than overriding. Shared
  `on_game_start` / `on_birthday` / `on_join_court` definitions are not conflicts. Sixteen mods in
  this playset define `on_game_start`.

## Known and deliberately unpatched

- **`on_action_namespace.192 has been queued twice`** — up to 37,987 entries in one run.
  `on_action_namespace` is a synthetic namespace the engine assigns to delayed on_action events at
  load; the ordinal cannot be mapped back to source script, so the responsible mod is not
  identifiable statically. Not harmful: the engine rejects the duplicate rather than queueing it.
- **Seasons `middle_of_year_season_trigger`** — written as an AND of spring, summer and autumn
  (never true), and `current_season_autumn = autumn` is not valid comparison syntax. The
  `location`-scope error at `00_weather_triggers.txt:441` is downstream of that. Repairing it means
  turning the AND into an OR, which changes when seasonal travel events fire — a design change.
- **Seasons `remove_doctrine`** — ~80 unguarded calls across a 5,000-line file for 83 log lines on
  an effect that is already a no-op. Poor rebase tradeoff.
- **Vanilla tournament / feast weak-character comparisons** — large vanilla event files, errors
  resolve as a false trigger rather than a broken outcome.
- **EP3 `add_random_external_estate_building`** — "Cannot begin new construction when already
  constructing", ~1,000 entries under administrative government. Estates end up under-built. The
  fix needs EP3's intended fill flow, which is not established.
- **DireWolves `make_unprunable` on living characters** — engine no-op warning.

## Runtime verification

| Run | Character | Length | Outcome |
|---|---|---|---|
| 8183 | Gar Sagon | — | Confirmed the title-name repair: `landed_titles` 663 MB to 5.7 MB, guard-book prose 7,918,803 to 49 lines |
| 8296 | Lucerys of Driftmark | 22 min at 5x | No clock freeze; eight of ten checked patches at exactly zero |
| 8212 | Ser Duncan (camp) | 18 min | First run to reach the guard academy final trials |
| 8251 | Lord Paramount Ormund | 38 min | Clean exit; gamestate 200 MB, `landed_titles` 23 KB, pending-event queue empty |

Two clock freezes that motivated this work have not recurred in any run since. The error log fell
from 60,178 entries in 18 minutes to 46,025 in 38 minutes, and the last wave of fixes projects
roughly 22,000 — about a fifth of the engine's 100,000-entry cap.

## Rebase warning

Most files here are whole-file overrides of Workshop content and are hash-gated in
`manifest/source_hashes.sha256`. If a source mod updates and its recorded SOURCE hash changes,
**re-derive that patch against the new file** rather than carrying this build forward. Check first
whether the upstream author fixed the defect themselves — several of these patches become
unnecessary the moment they do.

11 of the 91 files are new content with no upstream parent (`zz_`-prefixed key overrides, the Mega
Wars event and localization files, and the `localization/replace/` fixes). Those carry a BUILT hash
only.

## Maintenance notes

- The launcher pointer `agot_unified_compat.mod` is git-ignored (`/*.mod`) and machine-specific. It
  must be created by hand on each machine with a correct absolute `path=` line.
- Version numbers are deliberately not incremented per fix, because the pointer files are
  hand-maintained across two machines.
- `manifest/legacy/` holds the six original READMEs, manifests and validation records verbatim.
  Nothing was summarised away; consult them for the full historical audit trail.
