# AGOT Seasons + Personality Compatibility v1.0.0

Targets CK3 1.19.0.6 / AGOT 0.5.1. This layer exists solely to repair three whole-file
overrides where **AGOT - More Personality Depth** (MPD) and **AGOT : Seasons of Ice and Fire**
(Seasons) silently displaced content from mods loaded before them. It adds no gameplay of its
own and neutralizes nothing.

Built and statically verified on 2026-08-30 against the 65-mod playset. Not yet runtime-tested.

## Why only three files

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

### Deliberately not reverted in P03

These are MPD's actual design decisions, not collateral losses. Do not "restore" them:

- `text_single "ai_personality"` keeps `visible = yes`. MPD shows AI personality for player
  characters too; AGOT had `visible = "[Not( Character.IsPlayer )]"`.
- `secondary_widget` keeps `position = { 310 0 }`. MPD shifted it from AGOT's `300` to make room
  for its own content.

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
