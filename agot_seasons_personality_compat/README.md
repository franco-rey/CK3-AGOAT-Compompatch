# AGOT Seasons + Personality Compatibility v1.0.0

Targets CK3 1.19.0.6 / AGOT 0.5.1. This layer repairs conflicts and defects introduced by
**AGOT - More Personality Depth** (MPD) and **AGOT : Seasons of Ice and Fire** (Seasons) in the
66-mod playset. P01-P03 restore content those two silently displaced from mods loaded before them;
P04-P07 fix defects in the mods themselves. It adds no gameplay of its own and neutralizes nothing.

**Runtime-verified.** The 8251 Ormund run (38 minutes) confirmed P01-P06 at exactly zero, with the
error log falling from 60,178 entries in 18 minutes to 46,025 in 38 minutes. P07 was added from that
run's evidence and is not yet runtime-tested.

## Why only three files were needed for the displacement fixes (P01-P03)

MPD and Seasons contest 17 virtual paths between them. Fourteen need no patch, and it matters
that a future agent does **not** "fix" them:

- **Seasons deliberately replaces AGOT's winter tiers.** It splits `winter_normal_modifier`
  into `winter_north_modifier`, `winter_normal_modifier_1`, `winter_cold_modifier`,
  `winter_light_modifier` and `winter_southern_modifier`, all defined in its own
  `common/modifiers/seasons_modifiers.txt`. Every apparently "lost" line in
  `00_weather_triggers.txt`, `00_map_related_custom_loc.txt`, `07_ep3_custom_loc.txt`,
  `01_event_backgrounds.txt` and `00_hunt_triggers.txt` is an old-tier check being superseded.
  Restoring AGOT's lines there would break the seasons system. `00_weather_triggers.txt` shows a
  301-line diff but defines the same 25 keys — only the bodies changed.
- **Both mods are genuinely AGOT-aware.** MPD's rewrite of `ai_has_warlike_personality` and
  `ai_has_cautious_personality` carries AGOT's own `# AGOT Disabled:` clauses forward and layers
  its trait-XP system on top. Seasons' `03_fp2_interactions.txt` keeps the struggle branch and
  adds `has_title = title:h_the_iron_throne` plus its own situation parameter.
- `00_war.txt`, `99_casus_belli_values.txt`, `mapmodes.gui`, `agot_mapmodes.gui`,
  `00_board_game_effects.txt`, `00_wet_nurse_tasks.txt` and `bp2_character_interaction_events.txt`
  are strict supersets of what they override — nothing is lost.
- `cooltip.gui`: MPD's one changed line adds `Not( Trait.IsPersonality )`, which is its feature.

`on_action` **entries with the same name merge across files** rather than overriding, so the
many shared `on_game_start` / `on_birthday` definitions in this playset are not conflicts. Only
same-*path* overrides displace content — which is what the three files below are.

## Patch contents

| Module | Base | Restores |
|---|---|---|
| P01 | AGOT: House Founders | `common/on_action/child_birth_on_actions.txt` — Seasons displaced all three House Founders birth hooks: `agot_hf_child_birth_action_cadet_effect`, `agot_hf_child_birth_action_last_bastard_effect`, `agot_hf_lowbron_city_child_effect`. Cadet-branch creation, last-bastard tracking and lowborn city children stopped firing on birth. House Founders is the base (delta +5 vs Seasons' +1); Seasons' single `season_flavor_events.00015` nickname hook is re-inserted at the same point in the delayed-events list. |
| P02 | AGOT: House Founders | `common/scripted_effects/07_dlc_ep3_scripted_effects.txt` — Seasons displaced House Founders' adventurer-naming rework. HF comments out vanilla's `adventurer_name_*` entries in `create_landless_adventurer_title_effect`'s `random_list` and substitutes `380 = { agot_hf_laamp_naming_effect = yes }`; under Seasons that reverted to vanilla's naming list. House Founders is the base (delta 339 vs Seasons' 12); Seasons' winter-tier rewrite is applied at both sites in `random_rain_snow_chance_effect` (the Snow `OR` and the Rain `NOR`), with `winter_mild_modifier` and `winter_harsh_modifier` preserved and not duplicated. |
| P03 | AGOT - More Personality Depth | `gui/window_character.gui` — a three-way where MPD displaced both DireWolves and AGOT. Restores DireWolves' `dw_direwolf_character_view`, `dw_direwolf_relationship_row` and the `IsCharacterDirewolf` guard on the `main_content` vbox (without which the direwolf panel and relationship row vanish and the human view draws over direwolves), plus AGOT's `agot_pre_war_liege_portrait_vbox` and the `HasGameStartedForTheFirstTime` clause on two `visible` bindings. MPD is the base; its `mpd_view_hook` widget and trait-XP roller are untouched. |
| P04 | AGOT - More Personality Depth | `common/scripted_effects/mpd_xp_calculator.txt` — seven `court_owner = { ... }` hard scope switches in `mpd_calculate_trait_xp`, soft-scoped to `court_owner ?= { ... }`. The effect runs from `mpd_distribute_initial_xp` on `on_game_start` across every character, so every landless adventurer, camp follower and unlanded character failed the switch: **29,673 entries** in the 8212 Ser Duncan camp run, 49% of the whole error log, 4,239 per site. The author already guards the inner variable reads with `has_variable`, but the outer scope switch fails before any of that runs — the same ordering trap as Observer Stack P42/P43. A character with no court owner could never satisfy these wet-nurse modifiers anyway, so the XP weights are unchanged. |
| P05 | AGOT : Seasons of Ice and Fire | `events/season_flavor_events.txt` — removes 28 dead title checks (`h_dorne`, `h_the_north`, `h_the_vale`, `h_the_riverlands`, `h_the_stormlands`, `h_the_reach`, `h_the_westerlands`, each repeated across the `.00015` trigger and three `immediate` branches). None resolve in AGOT; `title_links.cpp:214` logged all 28 at load. `has_title` against an unresolvable id is always false, so removal cannot change any outcome. `h_the_iron_throne` and `k_dragonstone` resolve and are kept in all four blocks, plus all seven `e_*` regional titles in the trigger block, so no `OR` is left empty. |
| P06 | DireWolves | `localization/replace/english/zz_compat_direwolf_fixes_l_english.yml` — re-declares two keys DireWolves ships malformed: `trait_direwolf_young_wolf` (prose after the closing quote, `localization_reader.cpp:581`) and `dw_debug_show_wolf_blood_interaction_desc` (no opening quote, `localization_reader.cpp:535`). Files under `localization/replace/` take priority regardless of load order, so only these two keys are affected. |
| P07 | AGOT - More Personality Depth × Immersive Personalities | `common/scripted_effects/mpd_scripted_effects.txt` — removes the two `paranoid` trait-XP calls that cannot succeed: the roll in `mpd_roll_all_personality_xp` and the reset in `mpd_force_reroll_all_personality_xp`. `add_trait_xp` without a track name fails outright on a multi-track trait, so paranoid was **already** receiving no XP from MPD; every one of these **23,209 entries** (50% of the 8251 Ormund log) was a no-op that logged. Removal is therefore behaviour-identical. The other 38 of 39 rolled traits keep both roll and reset, verified by count. |

### Deliberately not reverted in P03

These are MPD's actual design decisions, not collateral losses. Do not "restore" them:

- `text_single "ai_personality"` keeps `visible = yes`. MPD shows AI personality for player
  characters too; AGOT had `visible = "[Not( Character.IsPlayer )]"`.
- `secondary_widget` keeps `position = { 310 0 }`. MPD shifted it from AGOT's `300` to make room
  for its own content.

## Known issues deliberately NOT patched

Recorded so a fresh agent does not burn time rediscovering them, or "fix" one by guessing.

### `paranoid` multi-track — RESOLVED by P07, but read this before "improving" it

P07 removes the calls rather than repairing them, and that is deliberate. `paranoid` is defined
four times in this playset — AGOT (6, no tracks), Mayham (38, no tracks), MPD (56, one anonymous
`track` block) and Immersive Personalities (63, flat, no tracks). The engine reports *multiple*
tracks although no single definition declares more than one, so trait definitions are being merged
rather than replaced, and the merged track identifiers cannot be determined statically — the error
message does not name them.

Do **not** "fix" this by supplying a track name; that is a guess that fails silently. Do not
redefine the trait from this mod either: it loads at 58 and IP at 63, so IP wins regardless.

What remains available is a **design choice**, not a repair: if MPD's tracked paranoid is wanted
instead of IP's flat one, move this layer after IP (position 64+) and redefine the trait there.
That placement is safe — nothing at 59–65 claims any path this mod owns. Until someone makes that
call, paranoid keeps IP's stats and simply has no MPD XP progression, which was already true.
### Seasons `current_season_spring` scope — 46 errors, blocked by a deeper bug

`location trigger [ Wrong scope for trigger: province, expected character, combat, army ]` at
`00_weather_triggers.txt:441`, reached via `is_nice_season_to_be_outside_trigger` →
`middle_of_year_season_trigger` → `current_season_spring`.

The scope error is downstream of a worse problem: `middle_of_year_season_trigger` (lines 98–106) is

```
middle_of_year_season_trigger = {
    current_season_spring = yes
    current_season_summer = yes
    current_season_autumn = autumn
}
```

which is an **AND** of spring, summer and autumn — never true — and `current_season_autumn = autumn`
is not valid comparison syntax. Silencing the scope error would leave a trigger that is
unconditionally false; making it work means turning the AND into an OR, which changes when seasonal
travel events fire. That is a gameplay design change, not a repair.

### Seasons `remove_doctrine` — 83 errors, poor rebase tradeoff

`set_AGOT_season_*` strips the previous season's doctrine from a hardcoded list of ~20 faiths
without checking `has_doctrine` first. Harmless at runtime (the effect is a no-op that logs), but a
correct fix means guarding ~80 call sites inside a 5,000-line file, creating a large whole-file
override that must be rebased on every Seasons update — for 0.14% of the error log.

### DireWolves `make_unprunable` on living characters — 45 warnings

Engine-level no-op warning from DireWolves marking direwolves unprunable while alive. No behavioural
effect and no clean fix short of restructuring the mod's pruning logic.

## Load order

Must load **after** both AGOT - More Personality Depth and AGOT : Seasons of Ice and Fire.
Anything later in the playset is safe: no mod mounted after Seasons claims any of these three
paths (verified against Observer Stack, Immersive Personalities, Royal Court Event Pack and the
OPB layer — the only shared entries are `descriptor.mod` and `thumbnail.png`, which are per-mod
and never merged). Placing it immediately after Seasons is the intended position.

This layer does not touch `dlc_load.json`, the launcher playset, or any other mod's descriptor.

## Rebase warning

All three files are whole-file merges and are hash-gated on **both** parents.
`manifest/source_hashes.sha256` records the base and donor hash for each. If either parent
updates and its hash changes, re-derive the merge against the new file rather than copying this
one forward — in particular, re-check whether the displaced content still exists upstream, since
these patches become unnecessary the moment either author fixes the conflict themselves.

See `manifest/build_manifest.json` for the per-file merge base, donor, and built hashes.
