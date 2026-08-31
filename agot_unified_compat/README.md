# AGOT Unified Compatibility Patch v1.0.0

A single local layer holding every compatibility fix for this playset. Targets CK3 1.19.0.6 /
AGOT 0.5.1 against the 66-mod AGOT playset.

Consolidated on 2026-08-30 from six separate local mods. **No game file was changed by the
consolidation** — all 91 files were copied byte-identical and verified by hash (the layer has since grown to 92). Only the packaging
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

92 game files. Full per-file provenance, transformation IDs and hash gates are in
`manifest/build_manifest.json`; every original document is preserved verbatim under
`manifest/legacy/`.

## Iron and Salt wave (2026-08-30)

Five mods were added at positions 60-64, ahead of this layer. Three needed nothing:
**Custom Name Lists**, **Raised Army CoA** and **Extended Family Actions** each collide with
nothing in the playset (their only shared keys are `on_action` entries, which merge rather than
override).

**CK3 Naval Combat (60) must never be enabled without AGOT Iron and Salt (61) after it.** Naval
Combat contains zero references to AGOT and its `gui/hud.gui` preserves **0 of 11** of AGOT's
additions -- it would strip `agot_hud_dragon_army_composition`, the Night's Watch adventurer
guard and the pirate/landless handling from the HUD. Iron and Salt declares Naval Combat as a
dependency, carries 6,444 internal `naval_combat` references, and its `hud.gui` preserves
**11 of 11** of AGOT's additions while adding the naval tab. Iron and Salt loading after Naval
Combat is what makes the pair safe.

Two files then needed merging into this layer, because it loads last:

| Module | Base | Merged in |
|---|---|---|
| P08 | this layer's existing three-way | `gui/window_character.gui` -- Iron and Salt's `agot_kraken_character_view` registered beside the dragon and fake-death views, and the `main_content` guard rewritten to exclude **both** direwolves and krakens, since all three special views share that container. MPD's view-hook, DireWolves' two bindings and AGOT's portrait/multiplayer clauses are all retained. |
| P09 | AGOT Iron and Salt | `gui/shared/cooltip.gui` -- new to this layer. Iron and Salt (12-line delta, kraken tooltip type) beat More Personality Depth (1-line delta), dropping MPD's `Not( Trait.IsPersonality )` guard so level-track bars reappeared on personality traits. Iron and Salt is the base; MPD's binding is re-applied on top. |

## Observer mode null-scope defect — SOLVED, pattern proven

In observer mode `GetPlayer` is invalid, so any GUI binding handing `GetPlayer.MakeScope` to a
scripted GUI passes a dangling character and the engine rejects the scope **before any trigger
runs**. The 7959 observer run exhausted a 100,000-entry error budget in 16 minutes on this alone.

**Two approaches that do NOT work — never retry them:**

1. `exists = this` inside the scripted GUI's `is_shown`. The scope is rejected before the trigger
   body is entered. Grand Remembrance already shipped this; it does nothing.
2. `And(GetPlayer.IsValid, IsShown(...))`. CK3 GUI `And()` **evaluates every argument** — it does
   not short-circuit — so this is identical to the unguarded binding. This was P24 and P36, and
   both demonstrably failed across multiple runs.

**The approach that DOES work — parent-container gate:**

```
container = {                       # or widget
    visible = "[GetPlayer.IsValid]"   # gate: player validity ALONE, no scripted-GUI call
    <original element> = {
        visible = "[... GetScriptedGui('x').IsShown( GetPlayer.MakeScope ) ...]"
        ...content unchanged...
    }
}
```

CK3 **does** suppress a hidden parent's child bindings. Proven empirically:

| Patch | File | Before | After |
|---|---|---|---|
| **P49** | `guard_academy_button_widget.gui` | 19,978 | **0** |
| **P50** | `gr_chronicle_window.gui` | 19,977 → 2,582 | pending confirmation |

P49 is **VERIFIED** against the 20:21 observer run. P50 applies the identical pattern; the outer
container carries the registered widget name and the window itself is untouched — layer, movable,
allow_outside, both state blocks and all content unchanged.

### Still outstanding: CK3 Naval Combat — 60,396 entries

Now the dominant source, and the same defect. The calls live in **AGOT Iron and Salt's**
`gui/hud.gui` (11,716 lines — Iron and Salt wins that path over Naval Combat), clustered in the
topbar gold/treasury tooltip around lines 8929–9274: ten `naval_combat_finance_active_gui` calls
plus `GetPlayer.MakeScope.ScriptValue('naval_combat_monthly_maintenance_value')`.

The fix is the same parent gate and would be a handful of surgical edits — but it means this layer
takes on an **11,716-line whole-file override of an actively-developed mod**, re-derived on every
Iron and Salt update. That is a maintenance decision, not a technical one, and is deliberately left
to the owner. It only affects observer mode; normal play is unaffected because `GetPlayer` is valid.
## King Ronnel playthrough wave (2026-08-30) — P51, P52, P53

The 8003 normal-play run put total errors at 25,333 of the 100,000 budget, with only 2,508 during
actual gameplay. These three fixes target the largest remaining gameplay-phase sources. All follow
patterns already proven in this layer, and all are behaviour-preserving.

| Module | Provider | Fix |
|---|---|---|
| P51 | AGOT+ | `asoiaf_scripted_effects_strong_seed.txt` — `agot_assign_strong_seed_traits_effect` tested `dynasty ?= dynasty:dynn_Redbeard`. That dynasty is **not defined by any mod in this playset**, and `?=` only soft-scopes the left side — an unresolvable dynasty literal on the right still errors. **40 entries.** The branch could never be true, so its limit becomes `always = no`. The body is left in place so the intent survives if AGOT+ ever adds the dynasty. |
| P52 | AGOT | `04_dlc_ep2_wedding_effects.txt` — `clean_grand_wedding_betrothal_variables` dereferenced `var:promised_grand_wedding_marriage_countdown` without checking it exists, producing three errors per call (unset variable, then two invalid-scope `remove_variable` calls). **48 entries.** Now wrapped in `has_variable`, with both inner scopes soft. |
| P53 | AGOT | `agot_kingsguard_events.txt` — **112 entries**, `Undefined event target 'kingsguard_candidate'` across eight sites. See below. |

### P53 root cause

`agot_kingsguard.9002` picks its candidate with a `random_` block whose limit can match nobody, so
`scope:kingsguard_candidate` is never saved. Its option ran regardless: `add_courtier` errored, and
it still fired `agot_kingsguard.1008`, which dereferences the same missing scope at six further
sites. **One failed raise produced seven errors.**

Two changes:

1. The `.9002` option body is wrapped in `exists = scope:kingsguard_candidate`. With no candidate
   there is nothing to do, so nothing runs — and `.1008` is no longer fired into a scope it cannot
   use. This is the root-cause fix.
2. All 24 `scope:kingsguard_candidate` hard switches across the file become `?=`, which also covers
   `.1005`, `.1007`, `.1009`, `.3011`, `.9003` and `.9005`. Same idiom as P40 (`Targaryen_63`) and
   P43 (`cp:kingsguard_6`).

All 10 candidate save sites and all 6 numbered variants are untouched.

### Deliberately not patched from this run

- **Iron and Salt kraken tooltip chain** — 2,002 entries, 80% of gameplay-phase noise. Fires
  `while building tooltip/description`: the decision preview runs `kraken_create_at_saved_location_effect`,
  but `create_character` is a no-op in tooltip mode so everything downstream gets an invalid scope.
  Execution is unaffected. `00_kraken_effects.txt` is 1,384 lines in an actively-developed mod, so a
  patch would not survive updates for zero functional gain.
- **The Unnecessary Dragons missing decision art** — 128 entries, `No valid picture found for
  'hatch_dragon_decision'`. The decision works; the author simply ships no illustration.
- **`gene_kraken` / `gene_direwolf`** — 5,386 each, load-time only. Saves predating those mods have
  no stored value for the new portrait genes. Expected and harmless.
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
