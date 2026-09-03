# AGOT Unified Compatibility Patch v1.0.0

A single local layer holding every compatibility fix for this playset. Targets CK3 1.19.0.6 /
AGOT 0.5.1 against the 66-mod AGOT playset.

Consolidated on 2026-08-30 from six separate local mods. **No game file was changed by the
consolidation** — all 91 files were copied byte-identical and verified by hash (the layer has since grown to 92). Only the packaging
changed: one folder, one `descriptor.mod`, one launcher pointer, one manifest.

> **Current dragon status:** the investigation is closed for the general invisible-body failure.
> Read [`DRAGON_INVESTIGATION.md`](DRAGON_INVESTIGATION.md) for the authoritative test record,
> confirmed signatures, production exclusions, false leads, and remaining thumbnail/UI follow-up.
> Earlier dragon sections below are retained as chronological evidence and may contain conclusions
> that were explicitly superseded by later controlled runs.

## Rejected mods — do not re-enable without addressing the cause

Recorded from bisection, so these are not re-tried blindly.

| Mod | Workshop ID | Why |
|---|---|---|
| Blood of Valyria | `3469933841` | **Crashes game start.** Hooks `on_game_start_after_lobby` with two `every_living_character` sweeps (`on_sdv_gives_vi_trait_every_living_character`, `on_sdv_beauty_fertility_base_after_lobby`), the second dispatching a per-character event. Does not scale to this playset. Also calls its own `sdv_heir_disinherit_removal_effect` with arguments it does not declare, at ~48 sites ("Scripted effect should have no arguments"). Isolated by bisection 2026-09-03: identical config crashed with it on, loaded with it off, twice each. |
| AGOT Iron and Salt | `3781577713` | One of two confirmed invisible-dragon causes. |
| The Unnecessary Dragons | `3287624076` | The other invisible-dragon cause. |
| Gamerule Gadget | `2826829936` | Overrides 68 game rules defined by AGOT and MIV, and hooks `on_game_start_after_lobby`. Incumbent-priority violation. Not the crash cause, but not wanted. |
| [KET] Court Position | `3742562925` | Overrides 42 court-position keys belonging to Court Positions Expanded. Incumbent-priority violation. |
| Dynamic Family Portrait (AGOT) | `3609763696` | Not standalone. Requires DFP base and AGOT More Dragon Eggs; without them its `hud.gui` references `portrait_hud_heir`, `portrait_hud_spouse` and `mde_dragon_portrait_*_size`, which no loaded mod defines. Merging it crashed the HUD build. Re-merge ONLY with both dependencies. |

## Where to look

| I want to… | Read |
|---|---|
| see every module, by upstream mod, in playset order | [`MODULES.md`](MODULES.md) — generated, do not hand-edit |
| check a module's source gate or built hash | `manifest/source_hashes.sha256` |
| see per-file provenance, transformation ids and rationale | `manifest/build_manifest.json` (schema v2) |
| know why a fix was *not* attempted | the `rationale` field of that file's manifest entry |
| add a mod without breaking key resolution | run `tools/check_duplicate_keys.py` before committing |
| regenerate the module index after a change | `python3 tools/gen_module_index.py` |
| read the dragon investigation record | [`DRAGON_INVESTIGATION.md`](DRAGON_INVESTIGATION.md) |
| read the six pre-consolidation patch docs | `manifest/legacy/` |

Everything below this table is the working history: chronological, including superseded
conclusions and approaches that were tried and failed. It is kept deliberately — several
sections record things that must **never** be retried. Current state lives in `MODULES.md`
and the manifest; narrative lives here.

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

> Status 2026-08-31: Iron and Salt was briefly suspected of the invisible-dragon bug, removed, then
> **cleared and re-enabled** — the bug persists without it. Everything in this section is live and
> current again, except P58, which stays deleted (wrong theory, verified inert).

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

#### P49 follow-up — the HUD reposition regression (2026-08-31)

After P49 was verified, the guard buttons were moved from upstream's `position = { -631 0 }` to
`{ -930 0 }` at the owner's request to sit nearer find character / find artifact. **The buttons then
disappeared entirely.** They were not hidden by logic — the save confirmed `has_winged_knights` on
the player as a genuine character flag and `agot_guards_roster_button_enabled` in the game rules, so
all three `is_shown` blocks passed, and there was no parse error for the file anywhere in a
35,792-line error log.

The X offset is measured **from the right edge, so more negative moves LEFT**. Moving −631 → −930
pushed the 114px strip 299px further *away* from the buttons it was meant to sit beside, landing it
around x 990–1104 on a 1920-wide screen — directly behind the centre bottom HUD panel, which shares
`hud_layer`. Rendered, occluded, invisible.

Restored to the known-good −631, with the direction recorded on the line itself. To nudge toward
find character / find artifact the value must go **less** negative (≈ −520), never more.

Lesson: a widget that renders but cannot be seen is not distinguishable from one that fails to
render, if you only read logs. Check geometry against screen dimensions before assuming logic.

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
## Portrait pipeline wave (2026-08-31) — P54, P55, ~~P58~~

> **P58 was deleted on 2026-08-31.** Its theory was wrong, it was inert, and the mod it patched
> (AGOT Iron and Salt) is out of the playset. The section below is kept only as a record of a
> wrong turn — see *RESOLVED — AGOT Iron and Salt was the cause*.

Three shipped fixes, one reverted attempt and one diagnostic. This wave is worth reading in full
because the reverted attempt is more instructive than two of the successes.

| Module | Provider | Fix |
|---|---|---|
| P54 | AGOT Color Picker for Clothes | `gfx/FX/court_scene.shader` — every character in the game rendered **nude with distorted limbs**. Battle Graphics AGOT Patch (pos 78) wins this file with a version built against AGOT alone, calling `ApplyVariationPatterns` with **6** arguments and `AddDragonDecals` with **7**. But Color Picker for Clothes (pos 17) wins `agot_portrait_decals_shared.fxh` and `portrait_decals.fxh`, which define them with **7** and **8**. Result: `error X3013: no matching 6 parameter function`, then `Failed getting shader for PS_attachment`, then `Failed to create material with shader portrait_attachment_pattern` for every garment mesh. Fix is Color Picker's `court_scene.shader` verbatim (correct arity) plus Battle Graphics' ACG Addition block, which is its only unique contribution here. |
| P55 | AGOT+ | `asoiaf_agot_overwrite_effects.txt` — AGOT+ spawns the named dragons with `culture = culture:dragon`, and **no enabled mod nor vanilla defines a culture called `dragon`**. AGOT uses `culture:dragon_culture` (defined in `00_agot_cul_ancient_races.txt`) at 72 sites. Fixed at 7 sites: Vermax, Drogon ×2, Rhaegal ×2, Viserion ×2. Found by ck3-tiger, not by hand. |
| P58 | AGOT Iron and Salt | `zzz_kraken_no_human_accessories.txt` — dragons rendered at the wrong camera zoom. See below. |

### P54 has a hard dependency — read before disabling anything

P54 is **only correct while AGOT Color Picker for Clothes is enabled.** With Color Picker disabled,
AGOT's own chain is internally consistent at 6/7 arguments and this file reintroduces the exact
arity error it exists to fix. This was verified empirically in both directions: removed when Color
Picker was disabled, restored when it came back. The same caveat is recorded in the file header and
its manifest entry.

### P58 root cause

`zzz_kraken_no_human_accessories.txt` defines two portrait-modifier groups at **priority 100 and
110**. AGOT's `camera_zoom` group is **priority 12**, and AGOT also sets the dragon camera in
`00_agot_dragon_genes.txt:228` and `agot_dragon_trait_modifiers.txt:172` — all outranked.

Every one of the seven `kraken_visual_size` entries carries:

```
weight = { base = 0  modifier = { add = 1000  portrait_has_trait_trigger = { TRAIT = kraken } } }
```

Zero base weight, scoring only for krakens — but `selection_behavior = weighted_random` must still
resolve to an entry. A dragon matches none of them, an entry is selected anyway, and it applies
`gene_camera_zoom = linear_camera_zoom` at `value = 0.03`: a zoom meant for a kraken tentacle,
forced onto a dragon at nine times AGOT's priority.

The fix adds one no-op fallback entry per group, `base = 1` and factored to 0 for krakens.
Non-krakens select the fallback and receive no `dna_modifiers`. **Kraken behaviour is unchanged** —
the real size entries still score 1000, and all seven `gene_camera_zoom` lines are preserved.

### P56 — attempted, wrong, reverted. Keep this record.

The dragon symptom was: perfect dragon-shaped shadow, no body. Tracing the pipeline gave a clean
split — `dragon_shadow_mesh` uses shader `portrait_dragon_shadow` and rendered; `dragon_mesh` uses
`portrait_dragon_decals` and did not. **Both use the same `dragon.mesh` file.**

That pointed at colour. Color Picker for Clothes injects ten `AGOT_SetScriptedClothingColors()`
calls into `AddDragonDecals` in `portrait_decals.fxh`, overwriting DragonPrimary/Secondary/Tertiary/
Eye/Horn colour — the only functional difference in the entire dragon body path. P56 shipped that
file with those ten calls removed, keeping the 8-parameter signature so every caller still matched.

**It changed nothing, and it was reverted.** The reasoning was sound and the merge was verified
correct; the premise was wrong. Two lessons worth keeping:

- "This is the only functional difference in the path" is not evidence that it is *the* difference
  that matters. Everything else in the chain was verified correct and uncontested, which made this
  look like the answer by elimination. Elimination is not proof.
- The real cause was never in the shader at all. It was a portrait-modifier priority conflict two
  layers up, in a file that touches no shader code.

### How the dragon bug was actually found

Static analysis failed completely on this one and burned hours. What worked was bisection from a
known-good minimal playset, **built up rather than torn down**:

1. **AGOT alone** — dragons render correctly. Establishes a working baseline.
2. **AGOT + Submod Core + the 9 appearance mods** — still correct. Clears the entire appearance
   cluster in one launch.
3. Scan all 69 remaining mods: only **16** touch the portrait pipeline at all, and only **6**
   override a file AGOT ships. None override a dragon-critical file.
4. Owner's recollection narrowed it further — dragons were fine through roughly the first 40 mods.
5. **AGOT + CK3 Naval Combat + Iron and Salt** reproduced it in three mods. Naval Combat is present
   only because Iron and Salt's descriptor declares it a dependency; it is innocent (zero files
   under `gfx/portraits`, `gfx/models/portraits`, `common/genes`, `common/ethnicities`, `gfx/FX` or
   `common/traits`).

The reduced case also showed the bug more clearly than the full stack did: with three mods the
dragon rendered *small and distant* rather than absent, which is what identified it as a camera
problem rather than a rendering failure.

### Diagnostic techniques worth reusing

- **AGOT ships dragon shader debug views.** `portrait_decals.fxh` documents fourteen of them.
  Toggle from the console with `shader_debug AGOT_DEBUG_DRAGON_VIEW_9`, or uncomment the `#define`
  and purge the shadercache — the second route needs no console and therefore no `-debug_mode`.
  `_9` outputs a constant colour and so tests geometry independent of all colour data; `_1` shows
  the raw DiffuseMap sample. Note that a null result is ambiguous: these live in `PS_dragon`, so if
  fragments are discarded earlier the debug line never executes.
- **`ck3-tiger` with the full load order.** Generate a `.conf` with one `load_mod` per enabled mod
  in load order, or every AGOT identifier reads as undefined and the run is 99,000 lines of noise.
  Tiger rejects a `load_mod` target that emits a packaging warning, and 31 of this playset's `.mod`
  files carry `picture=`, so point it at sanitised copies rather than the real pointers. Configured
  this way the full run takes ~51 seconds. P55 came directly out of it.
- **Shader changes need a shadercache purge.** Script and portrait-modifier changes do not.

## Invisible dragons — the P59 investigation (2026-08-31)

> **This section's "SOLVED" claim was wrong.** P59 fixed a real bug (a stale 44-parameter copy of
> the dragon transfer effect) but it was NOT the invisible-dragon cause, and the full playset had
> zero transfer-effect failures even before it. The actual cause was AGOT Iron and Salt — see
> *RESOLVED — AGOT Iron and Salt was the cause*. Kept because the method is reusable.

The symptom: every dragon rendered as an animated **shadow with no body**. Confirmed in the
character window, the portrait list, and a full family tree of alive-and-dead dragons — shadow
everywhere, body nowhere. It survived disabling both Color Picker mods, lowering portrait
multisampling, and restarting, so it was never a graphics-settings problem.

### The error signature

`error.log`, 72 occurrences — exactly one per call site in AGOT's
`00_agot_scenario_dragons_effects.txt`:

```
Compiling source for agot_historical_dragon_transfer_vars_to_story_cycle_effect
failed for unknown arguments: gene_dragon_primary_color_saturation,
gene_dragon_fire_color_template, gene_dragon_fire_color_value,
gene_dragon_fire_smoke_template, gene_dragon_fire_smoke_value,
gene_dragon_secondary_saturation, gene_dragon_tertiary_saturation,
gene_dragon_horn_color_saturation, gene_dragon_eye_color_saturation,
gene_dragon_body_pattern_template, gene_dragon_body_pattern_value,
gene_dragon_scale_shadows, gene_dragon_scale_highlights.
```

Thirteen names. Note which ones: every *saturation*, *template*, *smoke*, *pattern* and
*scale shadow/highlight*. Every *hue* and every *value* compiles fine. That asymmetry is the clue —
it is not random corruption, it is a definition that is a specific number of parameters behind.

### Root cause

**AGOT More Dragon Eggs (3388366564)** ships a full-file copy of AGOT's
`common/scripted_effects/00_agot_dragon_effects.txt` — 3,376 lines against AGOT's 3,359 — built
against an older AGOT. Its copy of this one effect is 322 lines using 44 `$PARAM$` tokens. AGOT's
current one is 374 lines using 57.

Diffing the two parameter sets returns 13 names. They match the 13 in the error **exactly, one for
one, with nothing left over on either side.** That is what identified the mod.

Scripted effects are *database keys*, so the last mod loaded wins the key. More Dragon Eggs loads
after AGOT, so its stale 44-parameter definition wins — while AGOT's 72 call sites still pass all
57 arguments. The compiler rejects the 13 it does not recognise and the effect never compiles.

### Why a dead scripted effect makes a dragon invisible rather than wrong-coloured

This effect is what populates the `gl_dragon_variable_storage` story cycles. All 44 dragon
appearance script values in `00_agot_dragon_gene_values.txt` read that storage. AGOT's own comment
in that file states the failure mode outright:

> Without this, portraits rendered before the storage populates get 0 and the DNA baseline shows
> instead of the scripted appearance.

With the transfer effect dead the storage is *never* populated, so all 44 values resolve to 0 and
the body renders at zero scale. The shadow keeps drawing because `dragon_shadow_entity` uses the raw
`dragon.mesh` and never consults the scripted appearance. Animated shadow, no body — precisely the
observed symptom.

### The fix

`common/scripted_effects/zzz_agot_dragon_transfer_vars_fix.txt` — AGOT's current 57-parameter
definition, verbatim from `00_agot_dragon_effects.txt` lines 2302–2675. Verified on build: 374 code
lines, 57 distinct `$PARAM$` tokens, one top-level key, brace balance 0, body byte-identical to
source. This patch loads last, so it wins the key back from any stale copy.

**Safe if irrelevant.** If More Dragon Eggs is disabled, this file is byte-for-byte the definition
AGOT already provides and changes nothing. There is no downside to leaving it in.

### Same risk class — check these if dragons regress

Legacy of Valyria (3403938445) and its two AGOT compatches (3787584130, 3788296332) also ship copies
of AGOT's dragon files — including a `zzzz_lv_agot_scripted_effect_runtime_overrides_v0_2_2.txt`
with 74 references to this same effect and their own copy of
`00_agot_scenario_dragons_effects.txt`. AGOT: The Long Night & Azor Ahai (3780269495) touches it
too. Any of these can re-take the key. The check is one command: diff the `$PARAM$` set of whichever
definition wins against AGOT's 57.

### What this supersedes

P58 (kraken camera zoom) was built on the theory that Iron and Salt's `kraken_visual_size` group was
stealing `gene_camera_zoom` from dragons via `weighted_random`. **That theory was wrong.** The patch
loaded, was inert, and changed nothing. It is retained only because it is harmless and its no-op
fallbacks are arguably correct hygiene for that group regardless. Do not credit it with fixing
anything.

The bisect that pointed at Iron and Salt (AGOT alone = 0 errors; AGOT + Naval Combat + Iron and Salt
= 72 errors) is still unexplained on its face, because More Dragon Eggs was not in that playset's
`.json`. Either it was enabled in the launcher at the time — the Desktop `.json` files are import
files, not proof of what was active — or a second stale copy was in play. **Verify by looking at a
dragon, not by trusting the bisect attribution.**

### P59 verified working — but it was NOT the invisible-dragon cause (2026-08-31)

Post-P59 launch of the full 80-mod playset:

```
agot_historical_dragon_transfer_vars_to_story_cycle_effect failures :  0   (was 72)
all "Compiling source for" failures                                 :  0
```

The save confirms the downstream effect too: 54 `story_dragon_variable_storage` cycles exist and
carry real values (`dragon_size` identity=130000000). So the transfer effect compiles and runs.
**Dragons are still shadow-only.** P59 fixed a real, separate bug. Keep it; do not credit it with
this symptom.

### The actual cause, narrowed to one line

```
[E][pdx_persistent_reader.cpp:216]: Error: "Unexpected token: dragon, near line: 14"
    in file: "common/genes/dragon_accessory_genes.txt" near line: 24
[E][ethnicity.cpp:64]: invalid accessory group [dragon] for gene gene_dragon.
    file: common/ethnicities/03_agot_dragon.txt line: 128 (dragon)
```

Line 14 of that file is `dragon = {`, the body group; line 24 is its closing brace. **The parser
rejects the dragon body group, so it never registers**, and the ethnicity that generates dragon DNA
then cannot find it. `gene_dragon` has only two groups — `human_body` (index 0, which is literally
`1 = empty`) and `dragon` (index 1). With `dragon` gone, every dragon's DNA can only resolve to the
empty human body. `gene_dragon_shadow` is a separate gene and stays valid, so the shadow keeps
rendering. That is the whole symptom, and it needs no portrait modifier to explain it.

Both errors are absent from a 1-mod AGOT launch, and Caraxes renders correctly at 11 mods.

**Every override mechanism has been eliminated.** Across all 80 enabled mods plus vanilla, AGOT is
the *sole* provider of every link in the chain, uncontested:

| Link | Providers |
|---|---|
| ethnicity `dragon` (`03_agot_dragon.txt`) | AGOT only |
| gene `gene_dragon` (`dragon_accessory_genes.txt`) | AGOT only |
| accessory `dragon` (`agot_dragon.txt`) | AGOT only |
| entity `dragon_entity` (`dragon.asset`) | AGOT only |
| portrait modifiers touching `gene_dragon` | AGOT ×2, Iron and Salt ×1 (trait-gated to `kraken`) |

Shader chains are complete: the `portrait.shader` winner (AGOT Color Picker for Clothes) has all of
`portrait_dragon_decals`, `portrait_dragon_wing_decals`, `portrait_dragon_shadow`; our P54
`court_scene.shader` has all 217 AGOT effects plus the 2 Battle Graphics ones, missing none.
There are only 40 accessory genes loaded in total, so no gene-count ceiling is involved.

Since no file or key override explains it, the parse failure depends on the **state of the gene /
accessory database at the time that file is read** — most likely the accessory token `dragon`
referenced on line 17 not being registered yet. Supporting evidence that accessory registration is
partly broken in this list: 42 × `portraitaccessories.cpp:159 has an invalid accessory` (all
`tgc_*` / blackfyre).

**Do not ship another speculative portrait patch for this.** P56 and P58 were both built on
plausible-sounding theories and both did nothing. Use the log line as the oracle instead — it is
deterministic and appears at load, so a candidate playset can be judged by one grep:

```
grep -c "Unexpected token: dragon" logs/error.log
```

Two mods add accessory genes late and both attach to AGOT's own `dragon_origin` node: DireWolves
(pos 51, declares a `human_body` group under `gene_direwolf`) and Iron and Salt (pos 62,
`gene_kraken`). They are the first thing to rule out.

## Iron and Salt investigated and CLEARED — I was wrong (2026-08-31)

**Iron and Salt is NOT the cause and is back in the playset.** It was disabled, the game was loaded,
and the parse error appeared unchanged:

```
07:30:13  Unexpected token: dragon, near line: 14   in common/genes/dragon_accessory_genes.txt
07:30:14  invalid accessory group [dragon] for gene gene_dragon
```

The reasoning that convicted it was a **correlation artifact**. `crashes/` holds 14 sessions with
their own `error.log` and `meta.yml`; every session up to Aug 25 was clean and every session from
Aug 31 was broken, and Iron and Salt tracked that split perfectly. But 42 mods were added at once in
that window, so all 42 track it equally well. Presence-correlation over a single bulk change carries
almost no discriminating power. Record it as a method failure, not just a wrong answer.

What the crash archive *did* establish, and still holds: DireWolves is cleared (three Aug 20–21
sessions ran it without the error), and the break window is bounded by those 42 mods.

### The causal chain, now confirmed end to end

Four lines from one launch, in order:

```
Unexpected token: dragon, near line: 14   common/genes/dragon_accessory_genes.txt   (line 14 = "dragon = {")
invalid accessory group [dragon] for gene gene_dragon      common/ethnicities/03_agot_dragon.txt:128
could not find template [dragon]    gfx/portraits/portrait_modifiers/00_agot_dragon_genes.txt:105  (dragonrider)
could not find template [dragon]    gfx/portraits/trait_portrait_modifiers/agot_dragon_trait_modifiers.txt:11  (dragon)
```

The body group fails to parse, so it never registers; the ethnicity that generates dragon DNA cannot
find it; and **both** of AGOT's dragon portrait modifiers then fail to apply the body template.
`gene_dragon` has only `human_body` (index 0, literally `1 = empty`) and `dragon` (index 1), so the
body resolves to nothing. `gene_dragon_shadow` is a separate gene and is untouched — hence an
animated shadow with no body. This part is no longer a hypothesis.

### The oracle — use this, do not hunt for a dragon

Deterministic, appears at game load, one command:

```
grep -c "Unexpected token: dragon, near line: 14" logs/error.log
```

### Current suspects

Of the 42 mods added in the break window, only three have any footprint under `gfx/portraits` or
`common/genes`: **AGOT: Royal Guards** (8 portrait_modifier files), **AGOT - Unbound** (3), and
**Battleground Commanders** (1 portrait_animation).
AGOT - Unbound is independently suspicious: its `au_headgear_armor.txt` throws
`Failed to find accessory group for agot_most_headgears_` and `au_clothes_situational.txt` throws
four more accessory failures in the same load.

**Caveat on that filter.** "Touches `gfx/portraits` or `common/genes`" is the same class of
structural reasoning that wrongly convicted Iron and Salt. If disabling these three does not clear
the error, the filter is unsound and the honest fallback is binary search over the 42 — roughly six
loads.

## Playset state (2026-08-31) — ALL 80 mods enabled

The patch is built for the complete `AGOT Testing` playset with every Workshop mod enabled, and all
97 files are present. Iron and Salt, Royal Guards, Unbound and Battleground Commanders were each
disabled at various points during the invisible-dragon investigation; **all are enabled again** and
the corresponding patch files have been restored from git. P56 and P58 remain deleted (both were
wrong theories, both verified inert).

### Upstream caught up: AGOT: Royal Guards, 2026-08-31 — 4 patches RETIRED

AGOT: Royal Guards (3733779333) was updated upstream on 2026-08-31 at ~16:12 (40 files). The hash
ledger flagged four of our files as drifted, and a read-only comparison showed **the mod author has
independently implemented all five of our fixes** — in two cases better than we did:

| Patch | What we did | What upstream now does |
|---|---|---|
| P35 | guard flag against repeated Lord Commander writes | **Removed the self-referential name concatenation outright.** Its new comment: *"Never build a dynamic title from its own current name. That recursive title chain expands inside saves and can lock the persistent reader."* |
| P39 | set `agot_guard_positions_inheritance_review_pending`, which the author declared but never set | Sets it in 6 places, plus a new 30-day `agot_guard_positions_inherited_title_as_guard` flag gating the `.1006` fan-out |
| P41 | gate the five `agot_guard_positions.1007` trigger sites | Cut them structurally: 5 → 3 in the effects file, 3 → 1 in swords of braavos |
| P42 | initialise `training_merit` / `training_rank` before comparison | 8 initialisations — identical count to ours |
| P46 | guard the academy `add_trait_xp` reads | All 9 wrapped in `has_character_modifier` if/else_if limits |

**These four files were therefore DELETED, not rebuilt:**

```
common/on_action/00_agot_guard_positions_on_actions.txt        [P39]
common/scripted_effects/00_agot_guard_positions_effects.txt    [P41, P42, P46]
common/scripted_effects/06_agot_swords_of_braavos_effects.txt  [P41]
common/scripted_effects/08_agot_guard_order_book_effects.txt   [P35]
```

Keeping them would have been actively harmful. This patch loads last, so our older merges would have
**reverted the author's fixes** — including the one whose own comment says it prevents locking the
persistent reader. That is the same failure mode diagnosed for AGOT More Dragon Eggs: a stale
full-file copy silently winning a database key.

The hash gate in `manifest/source_hashes.sha256` is what caught this. It works; trust it.

#### Royal Guards patches RETAINED — verified still needed

| File | Patch | Why it stays |
|---|---|---|
| `common/on_action/05_agot_queensguard_on_actions.txt` | P40 | Source hash unchanged — upstream did not touch it |
| `gui/guard_academy_button_widget.gui` | P36, P47, P49 | Source hash unchanged |
| `localization/replace/english/zz_observer_stack_guard_book_l_english.yml` | P37 | Still needed: upstream still uses `GetFullName` on `agot_guard_order_book_page_join_swords_of_braavos` while using `GetNameNoTooltip` for the other six page-join keys — the exact inconsistency P37 fixes |

#### Full-ledger audit, same date

All 93 entries were checked against current Workshop content: **80 sources verified byte-current, 0
drifted.** The remaining 13 have no comparable upstream source — they are our own additive `zz_`/
`zzz_` files and the absorbed content of three retired local mods. No other mod in the playset needs
catching up.

### Load-order note for Iron and Salt

Its Workshop page specifies: AGOT → other → CK3 Naval Combat → AGOT Iron and Salt → **mods that
modify GUI**. The first three are satisfied (positions 7, 61, 62). The GUI clause is not: 27
GUI-modifying mods load *before* it and only 4 after. That is why it clobbered More Personality
Depth and DireWolves and why P03 and P09 have to exist at all — moving it ahead of the GUI mods
would make both unnecessary. It is *not* related to the dragon bug: Dragon Test 1 was three mods in
exactly the prescribed order, with no GUI mods present, and dragons were still invisible.

## DEFINITIVE PLAYSET (2026-08-31) — invisible dragons SOLVED

Dragons render. The cause was **two independent bugs producing an identical symptom**, which is why
single-culprit hunting failed repeatedly.

| # | Cause | Mechanism | Resolution |
|---|---|---|---|
| 1 | **The Unnecessary Dragons** (3287624076) | Declares `common/artifacts/slots/tud_slots.txt` with a slot whose database key is exactly `dragon`, colliding with AGOT's accessory-gene **group** `dragon` in `gene_dragon`. The group fails to parse (`Unexpected token: dragon, near line: 14`) and the body accessory never registers. `gene_dragon_shadow` is a separate gene, so the shadow still drew. | **Mod removed from the playset.** TUD ships zero gene/portrait files, so no structural filter could find it. |
| 2 | **Battle Graphics** (3225355262) | Stale `gfx/FX/court_scene.shader` calls `ApplyVariationPatterns` with 6 arguments where the winning Color Picker include defines 7 → 1,526 `X3013` errors, 1,526 `Failed getting shader for PS_attachment`. **All** portrait attachments fail, dragon bodies included. | **P54 in this patch.** A shader-only diagnostic mod containing just P54's `court_scene.shader` took X3013 from 1,526 to 0 and dragons rendered. |

The definitive playset is the `AGOT Testing` list with **AGOT Iron and Salt** and **The Unnecessary
Dragons** disabled, this patch last.

### P54's hard dependencies are now declared

`descriptor.mod` gained three entries it should always have carried, since P54's shader is Color
Picker for Clothes' file plus Battle Graphics' ACG block:

```
"AGOT Color Picker for Clothes"
"Battle Graphics"
"Battle Graphics AGOT Compatibility Patch"
```

### Iron and Salt content removed for good — and it was causing a visible UI bug

Iron and Salt is permanently out (its own separate minimal-case dragon failure is unrepaired and
distinct from TUD's). Two patch files were built on it and had become **actively harmful**:

```
gui/shared/cooltip.gui:886   'kraken_cooltip_type_living' is not a valid widget/type/property
gui/shared/cooltip.gui:472   'container_kraken_character_tooltip' is not a valid widget/type/property
gui/window_character.gui:4121 'agot_kraken_character_view' is not a valid widget/type/property
```

Line 4121 sits beside the dragon character view. That container failed to build, and the result was
**two relationship panels rendered superimposed** on dragon characters — duplicated, offset
Parents / Grandparents / Children / Siblings rows.

- `gui/shared/cooltip.gui` — **deleted.** It existed only to reconcile More Personality Depth with
  Iron and Salt. With Iron gone, MPD's version wins naturally and is correct.
- `gui/window_character.gui` — **de-krakened.** `agot_kraken_character_view` and the
  `kraken_character_window` guard removed; the `main_content` guard is back to DireWolves' form
  `[And( IsCharacterNormal, Not( IsCharacterDirewolf ) )]`. Verified after the edit: zero live kraken
  references, brace balance 0, and `dw_direwolf_character_view`, `dw_direwolf_relationship_row`,
  `IsCharacterDirewolf`, `mpd_view_hook`, `agot_pre_war_liege_portrait_vbox`,
  `agot_dragons_character_view`, `agot_hidden_character_view` and `agot_fake_death_character_view`
  all still present. **This file must stay** — its chain is AGOT → DireWolves → MPD → us, so
  deleting it would silently drop DireWolves' character view.

If Iron and Salt is ever reinstated, both are recoverable from git history — and its Workshop page's
load-order rule (GUI mods *after* it) should be honoured, which would have avoided needing P03/P09
at all.

### Still open

- **Two dragons show no portrait thumbnail but render correctly when clicked.** Not explained by the
  current log: all four decisive signatures are 0, and the only dragon-gene messages are
  `Unknown gene_dragon_main_horn_shape gene template dragon_horns_none` in AGOT's own
  `common/dna_data/test_dna_*` files — which describe *human* test characters and are longstanding
  AGOT data debt present in clean sessions too.
- **AGOT + CK3 Naval Combat + Iron and Salt** reproduces invisible dragons with a *different*
  signature (72 `agot_historical_dragon_transfer_vars_to_story_cycle_effect` compile failures, zero
  parse errors). A third mechanism, unexplained and sidestepped rather than fixed.

## Log-spam / script-error wave (2026-09-01) — P60, P61, P62

Mined from the crash session at `crashes/ck3_20260831_225832` — 413,840 error-log lines in 37
minutes of play. **59,467 of those were script errors**, and three mods accounted for the bulk.
All three fixes are behaviour-preserving: every condition patched here already evaluated false,
it just errored loudly while doing so.

| Patch | Mod | Errors/session | Fix |
|---|---|---|---|
| P60 | CK3 Naval Combat | **31,373** | dead vanilla culture/heritage lookups |
| P61 | A Landed Knights Mod | **7,564** | hard `father` scope switch |
| P62 | Grand Remembrance | **13,608** | 319 unguarded `var:` reads |

Combined: roughly **52,500 fewer runtime script errors per session**, and a large cut in the log
I/O that accompanies them (~186 lines/second sustained at 5× speed).

### P60 — CK3 Naval Combat gates ships on cultures AGOT deletes

`naval_combat_can_build_longship_trigger` and its two siblings test vanilla cultures and heritages:

```
norse  norwegian  swedish  danish  greek  han  goryeo
heritage_north_germanic  heritage_byzantine  heritage_chinese
```

**AGOT declares `replace_path` on BOTH `common/culture/cultures` and `common/culture/pillars`**, so
none of them exist. There is a subtlety worth recording: Battle Graphics (pos 76) *does* re-add
`swedish`, `norse`, `norwegian` and `danish` as real culture definitions after AGOT, so a naive file
scan says they exist — but each one declares `heritage = heritage_north_germanic` and
`language = language_norse`, both wiped by the pillars replace_path, so the cultures still fail to
register. That is why the log says "Failed to fetch a valid culture 'swedish'" while the definition
is plainly on disk.

`naval_combat_yearly_ai_management` evaluates this per character per year, so at 5× speed it fires
constantly. The three special-ship triggers are now `always = no` and the stray `culture:norse` test
in `naval_combat_can_use_sea_raid_trigger` is dropped. All 13 trigger definitions preserved.

**Deliberately not done:** mapping these ships onto real AGOT cultures (ironborn for longships, say).
That would *enable* content that has never worked in this playset — a gameplay decision, not a fix.

### P61 — A Landed Knights Mod hard-scopes `father`

`on_add_vet_modifer.txt` runs `every_side_knight` on both sides of every combat and tests
`father = { ... }`. `father` is a **hard** scope switch, so any knight with no recorded father throws
`father trigger [ Failed context switch ]`. Changed to `father ?=`.

**Deliberately not fixed:** the inner `is_army_owner` is not a valid CK3 trigger — the game logs
`Unknown trigger: is_army_owner` at load, so this condition never evaluated meaningfully upstream
either. Silencing 7,564 runtime errors is a fix; guessing what the author meant would be a rewrite.

### P62 — Grand Remembrance reads 319 variables with zero guards

`gr_story_custom_loc.txt` makes 319 `var:` reads and contains **no** `exists = var:` guard anywhere.
Evaluated against any character without a Grand Remembrance story, every read fails:

```
4,536  Event target link 'var' returned an unset scope
4,536  Invalid left side during comparison 'var'
3,528  Failed to fetch variable for 'gr_story_opinion'
1,008  Failed to fetch variable for 'gr_story_chronicler_type'
```

Each of the 65 trigger blocks that reads a variable now carries `exists = var:NAME` for every
variable it touches — 205 guards. All 6 top-level loc keys and all 143 `text` blocks preserved.

### Also observed in that session — NOT patched

- **The crash itself was memory, not script.** The last three lines before
  `EXCEPTION_ACCESS_VIOLATION` are `CreateTexture2D failed … Not enough memory resources`, retried at
  half size and failing again. Settings at the time: `render_scale 2.0` at 2560×1440 (4× the pixels),
  `portrait_multi_sampling x8`, `texture_quality ultra`, `shadowmap_resolution 4096×4096`,
  `upscale_quality off`. Clicking rapidly through many armies allocates portrait render targets, which
  is the trigger — but the ceiling is the settings. This is a settings change, not a patch.
- **11,624 `portraitcontext.cpp:326`** — longstanding AGOT `common/dna_data` debt, present in clean
  sessions too. Not ours to fix.
- **2,000 `add_domicile_building … already constructing`** from `07_dlc_ep3_scripted_effects.txt`.
  Five mods ship that path; identifying the right owner needs more evidence than one session.

## Batch 1-2 mod wave (2026-09-01) — 17 mods added, P63

Playset: `E:\Desktop\AGOAT + Batch 1-2.json` — the existing 81-entry order preserved verbatim,
18 appended at positions 81-98. 96 enabled.

Measured against the live stack (40,811 files, 76,143 db keys indexed, `on_action` excluded because
those entries merge). Results:

- **No `replace_path`** in any of the 18.
- **No intra-batch file conflicts** at all.
- **14 files override AGOT.** All were diffed line-by-line; only one group lost AGOT *keys*.
- **Two intra-batch key collisions**, one patched (P63) and one irreconcilable (below).

### P63 — councillor triggers, three-way merge

`can_be_chancellor_trigger`, `can_be_steward_trigger`, `can_be_marshal_trigger` are defined by
**three** mods: AGOT, Female Knight and Councillor (`zzzzzz_00_councillor_triggers.txt`) and
More Traditions v2 (`MTXXX_councillor_triggers.txt`). One wins, two vanish.

Worse: both submods were built by copying AGOT's block and editing it, and **both dropped AGOT's own
lore guards** —

```
NOT = { has_trait = kingsguard }     (chancellor, steward, marshal)
NOT = { has_trait = maester }        (marshal)
```

— so with either of them winning, a Kingsguard could be made Chancellor and a maester Marshal.

The patch takes AGOT's blocks verbatim (restoring all 4 guards) and widens the single gender-gate
line into an OR carrying both submods' relaxations, so nobody loses a feature:

```
OR = {
    can_be_councillor_gender_trigger = { COURT_OWNER = $COURT_OWNER$ }          # AGOT
    $COURT_OWNER$ = { is_ai = no }                                              # Female Knight
    MTXXX_liege_flouts_council_faith_tradition_trigger = { LIEGE = $COURT_OWNER$ }  # More Traditions
    is_ruler = yes                                                              # More Traditions
}
```

**Dependency:** requires Female Knight *and* More Traditions loaded. Delete the file if either is
removed — a dangling trigger reference is exactly the failure mode behind the kraken GUI bug.

### Better Executions Updated — DISABLED, not patchable

`Better Executions Updated` (2429466948) and `Bloodlines: Legacies of AGOT` (3522779004) **both fully
rewrite `execute_prisoner_interaction`** — 2,278 lines and 1,372 lines respectively, and Bloodlines'
entire file is that one key. This is an either/or, not a merge, and it does not belong in a
"straightforward patching" batch.

Resolved on the stated priority order (lore first): **Bloodlines kept, Better Executions disabled.**
Bloodlines adds dozens of house legacy tracks — arryn, baratheon, baelish, ashford, allyrion and
more — which is the larger lore gain. Better Executions is left in the playset as a disabled entry
so the decision is recorded rather than forgotten.

### Checked and found harmless — do not "fix" these

- **Bloodlines' dynasty legacy files.** They appear to delete 8 AGOT legacy tracks
  (`stark_legacy_track`, `bolton_legacy_track`, `umber_legacy_track`, `dayne_legacy_track`,
  `velaryon_legacy_track`, `borrell_legacy_track`, `forrester_legacy_track`, `dornish_legacy_track`).
  **They do not** — every one is redefined elsewhere in Bloodlines, alongside dozens of new house
  tracks. It is a wholesale expansion of AGOT's legacy system. No patch needed.
- **`blind_castrated_disfigured_recipient_support_effect`.** Better Executions ships a 33-line
  version that strips AGOT's `keep_imprisoned` handling and patron modifier. Our patch already
  carries AGOT's 51-line version plus a one-line `exists = scope:recruit` guard, and loads last — so
  the correct version already wins. Nothing to do.
- The other 13 AGOT file overrides lose only formatting lines; **no AGOT keys are dropped** by any of
  them.

### Version rot in this batch — watch these

`Ward Limit Based On Learning` (1.11.\*), `Petty Inheritable Traits` (1.18.\*),
`Immersive Concubinage` (1.18.\*.\*), `Show Player Opinion` (1.18.1.1). TUD declared 1.12.\* and its
entire decision system turned out non-functional, so an old `supported_version` here means "verify
the feature actually works", not merely "probably fine".

## Post-batch live-run findings (2026-09-01) — P64, P66

First live session with the Batch 1-2 playset (96 workshop + patch): a Rhaenyra playthrough and an
observer run. **All four earlier patches verified working in play** — every target signature 0:

```
P60 naval "Failed to fetch a valid culture"      0   (was 31,373)
P61 "father trigger [ Failed context switch ]"   0   (was  7,564)
P62 gr_story_custom_loc errors                   0   (was 13,608)
dragon parse error / X3013 shader errors         0 / 0
```

### P64 — is_human: Great Councils drops DireWolves' exclusion

DireWolves (pos 50) extends AGOT's `is_human` with `NOT = { has_trait = direwolf }`. **AGOT Great
Councils (pos 83) ships its own otherwise-identical copy that omits that line**, loads later, and
wins — so direwolves counted as human for councils, marriage pools, and everything else gated on
`is_human`.

This is the same failure class as the invisible-dragon and kraken bugs: a later mod copies an
earlier definition and silently drops one line the earlier mod depends on. Patched by taking Great
Councils' version verbatim with the direwolf exclusion restored.

### P66 — Court Positions Expanded gates Grand Vizier on a religion AGOT deletes

`has_religion = religion:islam_religion` in `is_shown`, `valid_position` and `valid_character`.
AGOT `replace_path`s the religion directories, so it does not exist: **2,919 errors per session**.
The three lookups become `always = no`. Behaviour unchanged — the position was already permanently
unavailable, just noisily so.

**To actually enable it** you would map those three lines to a real AGOT faith (something Essosi
suits a Grand Vizier). That ADDS content that has never worked here, so it is a gameplay decision
and deliberately not made in a bug-fix patch.

### Silent losses found and NOT yet patched

Measured across the whole playset — keys where a newly added mod overrides a **non-AGOT** mod:

| Winner | Loses to it | Keys |
|---|---|---|
| Ward Limit (pos 85) | **Better AI Education + AGoT Patch** (pos 35/36) | `educate_child_interaction`, `offer_ward_interaction`, `offer_guardianship_interaction`, `remove_guardian_interaction`, `make_child_learn_language_interaction` |
| Petty Inheritable Traits (pos 89) | **[AGOT] Mayham** (pos 39) | `bleeder`, `lisping`, `stuttering`, `wheezing` |
| Petty Inheritable Traits | **Better Barbershop + Mayham** | `clubfooted`, `hunchbacked`, `scaly` |
| No Duchy Limit (pos 81) | AGOT+, More Interactive Vassals | `NCharacterOpinion` |

Ward Limit is the significant one: you run Better AI Education *and* its AGOT patch specifically for
education behaviour, and all five of its education interactions are being replaced wholesale.

### Observer mode is inherently noisy with CK3 Naval Combat — not a bug

The observer run logged **74,624** null-scope errors (`Character - 4294967295`) from Naval Combat's
script values (`transport_ship_count_value`, `monthly_maintenance_value`,
`flagship_active_maintenance_value`). The same session pre-patch had 41.

That is **not** a regression from P60 — P60 only touched three `can_build_*_trigger` definitions and
none of these values. It is observer mode: with no player character those values evaluate against a
null character handle, and Naval Combat guards the *variable* (`exists = var:...`) but not the
*scope*, so the guard itself throws. In normal play there is a player character and it resolves.
Cosmetic, but it is where a 29 MB log comes from.

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

### Crashes on this install are memory, not mod conflicts (2026-08-31)

Established after a Hold Court crash. **Check this before investigating conflicts.**

Windows Event 2004 (Resource-Exhaustion-Detector) recorded `ck3.exe` at **42.0 GB** committed,
followed seven seconds later by
`CreateTexture2D failed: D24_UNORM_S8_UINT/5120x2880 — Not enough memory resources`. Steam and
Chrome were starved simultaneously and had to be force-closed.

Contributing factors: **34.8 GB** of enabled mod assets (AGOT+ 15.3 GB and AGOT 12.4 GB alone are
27.7 GB), `render_scale = 2.0` at 2560×1440 rendering everything at **5120×2880** — four times
native pixels and four times every render target — plus `portrait_multi_sampling = x8` and
`texture_quality = ultra`, on 32 GB RAM with a 25 GB pagefile.

It reproduced only under load (5× speed with Chrome and Steam open). A clean rerun at normal speed
rendered the same court scene fine on an identical modlist, so the ceiling is real but reached only
under churn — high speed fragments memory and a large contiguous allocation fails that would
otherwise succeed.

**Why this matters diagnostically:** crash signatures differ across dumps (13, 16 and 45 stack
frames observed) *because* it is memory — the access violation lands on whatever allocation fails
next, which is exactly why nothing ever correlates in the script logs. The owner's crash history
also predates any patching in this layer.

Cheapest lever if it recurs: `render_scale` 2.0 → 1.5 returns 44% of render-target memory while
keeping most of the supersampling benefit, since returns diminish sharply past 2.25× samples.

A separate, unresolved **load-time race** produces an access violation at a consistent address after
exactly 301 database nodes, roughly one launch in several. Two crash logs were byte-identical in
line count with the same errors in *different order* — direct evidence of concurrent
initialisation. Not memory, not GPU, no shader errors; no content difference exists between a
crashed and a successful load. Relaunching is the remedy; it cannot corrupt a save because it dies
before game state exists.

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
