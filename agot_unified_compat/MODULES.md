# Module index

Generated from `manifest/build_manifest.json` on 2026-09-03.
Derived file - do not hand-edit. Regenerate with `python3 tools/gen_module_index.py`.

102 files across 27 upstream mods. **override** replaces an upstream virtual path;
**authored** is a new file this layer introduces.

This layer must load **last**; every override below only wins because of that.

| Playset # | Upstream mod | Files | Modules |
|---:|---|---:|---|
| 6 | More Interactive Vassals | 5 | P08_MIV_DISABLED_CB_CONDITIONS, P08_MIV_SUPPORT_INTERACTION_ALIGNMENT, P34_FP3_STRUGGLE_CONCESSION_EMPTIED |
| 7 | A Game of Thrones | 22 | P04_PROVINCE_SCOPE_LIMIT, P09, P10, P16, P17, P18, P29_SCION_STORY_SELF_TERMINATE, P30A_DRAGON_TERROR_TOP_LIEGE, P30B_COA_DYNASTY_FOUNDER_SOFT, P43_KINGSGUARD_6_SOFT_SCOPE, P44_BLOOD_TRIGGER_SCOPE_RENAME, P52_GRAND_WEDDING_CLEANUP_GUARD, P53_KINGSGUARD_CANDIDATE_SOFT_SCOPE, P59_DRAGON_TRANSFER_VARS, P63_COUNCILLOR_TRIGGERS_3WAY, P67_HUD_FOURWAY_MERGE, P68_RALLY_POINTS_MAP_ICONS, P69_RALLY_POINTS_MILITARY_WINDOW |
| 9 | Legacy Of The Dragon | 1 | P12 |
| 13 | COW-AGOT: 3D Models & Bigger Castles | 1 | — |
| 17 | AGOT Color Picker for Clothes | 1 | P54_SHADER_APPLYVARIATIONPATTERNS_ARITY |
| 23 | Patch AGOT - MBS | 1 | P07_SCROLLAREA_IGNOREINVISIBLE |
| 24 | Active Courtiers | 1 | P48_ACTIVE_COURTIERS_FP3_STRUGGLE_NEUTRALISED |
| 26 | Search & Trade Artifacts | 2 | P70_SEARCH_TRADE_AGOT_PRICING, P71_SEARCH_TRADE_AGOT_ARTIFACT_PROTECTION |
| 33 | AGOT - Crowns of Westeros | 4 | P03_CULTURE_MIGRATION, P03_VALEMAN_OPINION |
| 38 | AGOT+ | 14 | P02_CROWN_CREATOR_CONTRACT, P02_KRAKENFALL_HOUSE_SCOPE, P02_WESTERMAN_OPINION, P15, P31A_MANCE_GIANT_REGIMENT, P31C_YOUNG_GRIFF_NICKNAME_AND_TRAIT, P31D_DUMMY_CHARACTER_LOCATION, P32A_DRAGON_FAITH_VALYRIAN_PAN_DRAGON, P33_TARGARYEN_95_MODIFIER_REMOVED, P51_NONEXISTENT_DYNASTY_BRANCH_NEUTRALISED |
| 41 | AGOT: House Founders | 3 | P01_HF_BIRTH_HOOKS_X_SEASONS_NICKNAME, P02_HF_ADVENTURER_NAMING_X_SEASONS_WINTER_TIERS, P19 |
| 42 | Advanced Character Search | 2 | P22, P26_RELIGION_FAMILY_SINGLE_BUCKET |
| 43 | Oathbound | 6 | — |
| 44 | Grand Remembrance | 6 | P24_GR_CHRONICLE_NULL_SCOPE, P25_RICE_SECTION_REMOVED, P50_CHRONICLE_PARENT_GATE, P62_GRAND_REMEMBRANCE_UNSET_VARS |
| 45 | Grand Remembrance - AGOT Compatibility Submod | 2 | — |
| 51 | DireWolves | 2 | P06_DIREWOLVES_MALFORMED_LOC, P45_DIREWOLF_PACK_SIZE_GUARD |
| 52 | Duel Overlay | 1 | P34_DUEL_OVERLAY_RESTORE_AGOT_NAME_FORMATTING |
| 54 | Expanded Domiciles for AGOT | 6 | P38_DOMICILE_FILE_SCOPED_CONSTANTS_RESTORED |
| 55 | AGOT: Royal Guards | 1 | P40_QUEENSGUARD_TARGARYEN63_SOFT_SCOPE |
| 58 | AGOT - More Personality Depth | 3 | P03_MPD_X_DIREWOLVES_X_AGOT_CHARACTER_WINDOW, P04_MPD_COURT_OWNER_SOFT_SCOPE, P07_PARANOID_UNSATISFIABLE_XP_CALLS_REMOVED |
| 59 | AGOT : Seasons of Ice and Fire | 1 | P05_SEASONS_DEAD_TITLE_CHECKS |
| 60 | Immersive Personalities | 2 | A4 |
| 61 | Royal Court Event Pack | 1 | — |
| 62 | CK3 Naval Combat | 1 | P60_NAVAL_COMBAT_DEAD_CULTURES |
| 71 | A Landed Knights Mod | 1 | P61_LANDED_KNIGHTS_HARD_FATHER_SCOPE |
| 83 | Court Positions Expanded 1.19 | 1 | P66_GRAND_VIZIER_DEAD_RELIGION |
| 84 | AGOT Great Councils | 1 | P64_IS_HUMAN_DIREWOLF |
| — | (authored here) | 10 | P03_VALEMAN_DEF_FORMAT, P33_CANON_CHILD_BIRTH_EFFECTS_98_104, P33_CANON_CHILD_TRIGGERS_98_104, P33_GREYJOY_13_ALT_MODIFIER_DEFINED, P37_SWORDS_OF_BRAAVOS_JOIN_NO_LINK_MARKUP |

## Files by upstream mod

### More Interactive Vassals  (`2712590542`, playset #6)

- `common/character_interactions/interactive_call_ally.txt` — **P08_MIV_DISABLED_CB_CONDITIONS** (override)
- `common/character_interactions/interactive_request_vassal_support.txt` — **P08_MIV_SUPPORT_INTERACTION_ALIGNMENT** (override)
- `common/decisions/interactive_decisions.txt` — **P08_MIV_DISABLED_CB_CONDITIONS** (override)
- `common/on_action/interactive_on_actions.txt` — **P08_MIV_DISABLED_CB_CONDITIONS, P08_RANDOM_RULER_PLACEMENT_REMOVED** (override)
- `common/scripted_effects/interactive_scripted_effects.txt` — **P34_FP3_STRUGGLE_CONCESSION_EMPTIED** (override)

### A Game of Thrones  (`2962333032`, playset #7)

- `common/character_interactions/00_vassal_interactions.txt` — **—** (override)
  - CFWF_CLAIMANT_FACTION_INTERACTION_GUARDS
- `common/character_interactions/06_ep3_interactions.txt` — **P05_LORATH_EXCLUSION, P11, P27_APPOINTMENT_TITLE_LAW** (override)
- `common/council_positions/00_agot_council_kingsguard.txt` — **P43_KINGSGUARD_6_SOFT_SCOPE** (override)
- `common/factions/00_factions.txt` — **P18** (override)
- `common/scripted_effects/00_interaction_effects.txt` — **P10, P28_RECRUIT_SCOPE_GUARD** (override)
- `common/scripted_effects/04_dlc_ep2_wedding_effects.txt` — **P52_GRAND_WEDDING_CLEANUP_GUARD** (override)
- `common/scripted_effects/20_health_effects.txt` — **P16** (override)
- `common/scripted_effects/zzz_agot_dragon_transfer_vars_fix.txt` — **P59_DRAGON_TRANSFER_VARS** (override)
  - base = AGOT 00_agot_dragon_effects.txt lines 2302-2675 VERBATIM (374 lines, 57 $PARAM$ tokens, single top-level key, brace balance 0)
- `common/scripted_modifiers/00_faction_modifiers.txt` — **P18** (override)
- `common/scripted_triggers/00_agot_blood_triggers.txt` — **P44_BLOOD_TRIGGER_SCOPE_RENAME** (override)
- `common/scripted_triggers/00_agot_coa_triggers.txt` — **P30B_COA_DYNASTY_FOUNDER_SOFT** (override)
- `common/scripted_triggers/00_agot_triggers.txt` — **P09** (override)
- `common/scripted_triggers/00_courtier_guest_management_triggers.txt` — **P10** (override)
- `common/scripted_triggers/zzzzzz_agot_councillor_triggers_merge.txt` — **P63_COUNCILLOR_TRIGGERS_3WAY** (override)
  - base = AGOT 00_councillor_triggers.txt blocks for can_be_chancellor_trigger / can_be_steward_trigger / can_be_marshal_trigger, VERBATIM
- `common/story_cycles/agot_story_cycle_naming_and_title_gui.txt` — **P29_SCION_STORY_SELF_TERMINATE** (override)
- `events/agot_events/agot_dragon_events.txt` — **P30A_DRAGON_TERROR_TOP_LIEGE** (override)
- `events/agot_events/agot_kingsguard_events.txt` — **P53_KINGSGUARD_CANDIDATE_SOFT_SCOPE** (override)
- `events/dlc/bp1/bp1_yearly.txt` — **P17** (override)
- `events/dlc/ep3/ep3_laamp_decision_events.txt` — **P04_PROVINCE_SCOPE_LIMIT** (override)
- `gui/hud.gui` — **P67_HUD_FOURWAY_MERGE** (override)
  - AGOT + CK3 Naval Combat + Battlefield Duel + + DFP(AGOT), three-way merged on vanilla 1.19.0.6. Repairs the regression where Naval Combat kept 0/3 AGOT identifiers after Iron and Salt was removed.
- `gui/map_icon_layer.gui` — **P68_RALLY_POINTS_MAP_ICONS** (override)
  - CoA Rally Points kept only 1/2 AGOT identifiers; merged against vanilla, AGOT ids 2/2 and all 80 Rally lines retained.
- `gui/window_military.gui` — **P69_RALLY_POINTS_MILITARY_WINDOW** (override)
  - CoA Rally Points kept 0/2 AGOT identifiers; merged against vanilla, AGOT's 205-line superset block taken over Rally's 13-line subset. All 409 Rally lines retained.

### Legacy Of The Dragon  (`3101422928`, playset #9)

- `events/decisions_events/rediscover_events.txt` — **P12** (override)

### COW-AGOT: 3D Models & Bigger Castles  (`2971198450`, playset #13)

- `common/buildings/yy_agotcities_special_buildings_westeros.txt` — **P06_RHOYNISH_OPINION, P06_HOLDING_CONTEXT, P13** (override)

### AGOT Color Picker for Clothes  (`3381385128`, playset #17)

- `gfx/FX/court_scene.shader` — **P54_SHADER_APPLYVARIATIONPATTERNS_ARITY** (override)
  - base = AGOT Color Picker for Clothes court_scene.shader verbatim (7-param ApplyVariationPatterns matching its agot_portrait_decals_shared.fxh)

### Patch AGOT - MBS  (`3316173814`, playset #23)

- `gui/window_county_view.gui` — **P07_SCROLLAREA_IGNOREINVISIBLE** (override)

### Active Courtiers  (`3157170996`, playset #24)

- `common/script_values/accou_marriage_values.txt` — **P48_ACTIVE_COURTIERS_FP3_STRUGGLE_NEUTRALISED** (override)

### Search & Trade Artifacts  (`2962238514`, playset #26)

- `common/script_values/at_basic_values.txt` — **P70_SEARCH_TRADE_AGOT_PRICING** (override)
  - S&T wins this path over AGOT and ships the two custom-price values as empty extension points, so dragon eggs and Valyrian steel priced at 0. AGOT's bodies restored on S&T's base.
- `common/scripted_triggers/at_artifact_triggers.txt` — **P71_SEARCH_TRADE_AGOT_ARTIFACT_PROTECTION** (override)
  - S&T wins this path and ships can_be_sold / can_be_destroyed as `always = yes`, letting the Iron Throne, historical uniques, Valyrian steel, dragon eggs and skulls be sold and destroyed. AGOT's rules restored; buy trigger…

### AGOT - Crowns of Westeros  (`2995674648`, playset #33)

- `common/artifacts/templates/ntc_artifacts_templates.txt` — **P03_CULTURE_MIGRATION** (override)
- `common/modifiers/ntc_artifact_modifiers.txt` — **P03_VALEMAN_OPINION** (override)
- `common/scripted_character_templates/ntc_scripted_character_template.txt` — **P03_CULTURE_MIGRATION** (override)
- `common/scripted_triggers/00_ntc_crown_commission_triggers.txt` — **P03_CULTURE_MIGRATION** (override)

### AGOT+  (`2950245430`, playset #38)

- `common/artifacts/templates/asoiaf_artifacts_templates.txt` — **P02_KRAKENFALL_HOUSE_SCOPE** (override)
- `common/modifiers/asoiaf_artifact_modifiers.txt` — **P02_WESTERMAN_OPINION** (override)
- `common/on_action/agot_on_actions/test_title_on_actions.txt` — **P02_CROWN_CREATOR_CALLS, P12** (override)
- `common/on_action/asoiaf_yearly_on_actions.txt` — **P31A_MANCE_GIANT_REGIMENT** (override)
  - P14.3
- `common/scripted_character_templates/asoiaf_invader_templates.txt` — **P02_INVADER_IS_DEAD, P31B_YOUNG_GRIFF_NICKNAME** (override)
- `common/scripted_effects/asoiaf_agot_overwrite_effects.txt` — **P32A_DRAGON_FAITH_VALYRIAN_PAN_DRAGON** (override)
  - P55: culture:dragon -> culture:dragon_culture at 7 dragon create_character sites (AGOT+ upstream references an undefined culture; AGOT defines dragon_culture in 00_agot_cul_ancient_races.txt)
- `common/scripted_effects/asoiaf_assign_inactive_traits_effects.txt` — **P33_TARGARYEN_95_MODIFIER_REMOVED** (override)
- `common/scripted_effects/asoiaf_canon_children_effects.txt` — **P01_REMOVE_DUAL_PLACEMENT, P01_ATTACH_NEWBORN_TO_COURT, P01_CANON_PARSE_REPAIRS** (override)
  - P14.2
- `common/scripted_effects/asoiaf_scripted_effects_artifacts.txt` — **P02_CROWN_CREATOR_CONTRACT** (override)
- `common/scripted_effects/asoiaf_scripted_effects_strong_seed.txt` — **P51_NONEXISTENT_DYNASTY_BRANCH_NEUTRALISED** (override)
- `common/scripted_effects/asoiaf_setup_effects.txt` — **P02_UNDERAGED_SCOPE_PREFIX, P02_HAS_CLAIM_ON, P02_IS_DEAD_TRIGGER, P02_REMOVE_NOOP_EXISTS, P32B_MORE_BOOKMARKS_RHLLOR_REMOVED** (override)
- `common/scripted_effects/asoiaf_targaryen_invasion_claimants_effects.txt` — **P31C_YOUNG_GRIFF_NICKNAME_AND_TRAIT** (override)
- `common/scripted_triggers/asoiaf_clothing_triggers.txt` — **P15** (override)
- `events/asoiaf_young_griff_landing_events.txt` — **P31D_DUMMY_CHARACTER_LOCATION** (override)

### AGOT: House Founders  (`2967263410`, playset #41)

- `common/on_action/child_birth_on_actions.txt` — **P01_HF_BIRTH_HOOKS_X_SEASONS_NICKNAME** (override)
- `common/scripted_effects/00_agot_hf_effects.txt` — **P19** (override)
- `common/scripted_effects/07_dlc_ep3_scripted_effects.txt` — **P02_HF_ADVENTURER_NAMING_X_SEASONS_WINTER_TIERS** (override)

### Advanced Character Search  (`3084203091`, playset #42)

- `common/scripted_effects/acs_se_religion.txt` — **P26_RELIGION_FAMILY_SINGLE_BUCKET** (override)
- `common/scripted_triggers/gen_acs_st_big_switch.txt` — **P22** (override)

### Oathbound  (`3457401824`, playset #43)

- `common/casus_belli_types/oathbound_conquests.txt` — **—** (override)
  - P20.1
- `common/character_interactions/oathbound_ransom_interaction.txt` — **—** (override)
  - P20.6
- `common/customizable_localization/oathbound_custom_loc.txt` — **—** (override)
  - P20.2
- `common/on_action/relations/oathbound_on_relation_deaths.txt` — **—** (override)
  - P20.3
- `events/oathbound_heir_events.txt` — **—** (override)
  - P20.4
- `events/scheme_events/oathbound_sway_vassals_events.txt` — **—** (override)
  - P20.5

### Grand Remembrance  (`3678529052`, playset #44)

- `common/customizable_localization/gr_story_custom_loc.txt` — **P62_GRAND_REMEMBRANCE_UNSET_VARS** (override)
  - base = Grand Remembrance gr_story_custom_loc.txt VERBATIM plus guards
- `common/on_action/gr_on_actions.txt` — **—** (override)
  - P21.3
- `common/on_action/zz_gr_memory_tracking.txt` — **—** (override)
  - P21.1
- `common/scripted_effects/gr_npc_obituary_data_effect.txt` — **P25_RICE_SECTION_REMOVED** (override)
- `common/scripted_guis/gr_scripted_guis.txt` — **P24_GR_CHRONICLE_NULL_SCOPE** (override)
- `gui/gr_chronicle_window.gui` — **P50_CHRONICLE_PARENT_GATE** (override)

### Grand Remembrance - AGOT Compatibility Submod  (`3683507542`, playset #45)

- `events/gr_obituary_events.txt` — **—** (override)
  - P21.2
- `events/gr_obituary_replay_events.txt` — **—** (override)
  - P21.2

### DireWolves  (`3766320609`, playset #51)

- `common/decisions/zz_observer_stack_direwolf_hunt_fix.txt` — **P45_DIREWOLF_PACK_SIZE_GUARD** (override)
- `localization/replace/english/zz_compat_direwolf_fixes_l_english.yml` — **P06_DIREWOLVES_MALFORMED_LOC** (override)

### Duel Overlay  (`2636170225`, playset #52)

- `gui/event_windows/duel_event.gui` — **P34_DUEL_OVERLAY_RESTORE_AGOT_NAME_FORMATTING** (override)

### Expanded Domiciles for AGOT  (`3768775292`, playset #54)

- `common/domiciles/buildings/00_agot_pirate_ship_buildings_UE.txt` — **P38_DOMICILE_FILE_SCOPED_CONSTANTS_RESTORED** (override)
- `common/domiciles/buildings/00_agot_ranger_buildings_UE.txt` — **P38_DOMICILE_FILE_SCOPED_CONSTANTS_RESTORED** (override)
- `common/domiciles/buildings/00_camp_buildings_UC.txt` — **P38_DOMICILE_FILE_SCOPED_CONSTANTS_RESTORED** (override)
- `common/domiciles/buildings/00_chinese_estate_buildings_UE.txt` — **P38_DOMICILE_FILE_SCOPED_CONSTANTS_RESTORED** (override)
- `common/domiciles/buildings/00_yurt_buildings_UY.txt` — **P38_DOMICILE_FILE_SCOPED_CONSTANTS_RESTORED** (override)
- `common/domiciles/buildings/01_camp_level_one_internal_slots_UE.txt` — **P38_DOMICILE_FILE_SCOPED_CONSTANTS_RESTORED** (override)

### AGOT: Royal Guards  (`3733779333`, playset #55)

- `common/on_action/05_agot_queensguard_on_actions.txt` — **P40_QUEENSGUARD_TARGARYEN63_SOFT_SCOPE** (override)

### AGOT - More Personality Depth  (`3717990443`, playset #58)

- `common/scripted_effects/mpd_scripted_effects.txt` — **P07_PARANOID_UNSATISFIABLE_XP_CALLS_REMOVED** (override)
- `common/scripted_effects/mpd_xp_calculator.txt` — **P04_MPD_COURT_OWNER_SOFT_SCOPE** (override)
- `gui/window_character.gui` — **P03_MPD_X_DIREWOLVES_X_AGOT_CHARACTER_WINDOW** (override)
  - 2026-08-31: Iron and Salt merge REMOVED for good. AGOT Iron and Salt is permanently out of the playset (one of two confirmed invisible-dragon causes). Its widgets no longer exist, so agot_kraken_character_view and the kr…

### AGOT : Seasons of Ice and Fire  (`3377641022`, playset #59)

- `events/season_flavor_events.txt` — **P05_SEASONS_DEAD_TITLE_CHECKS** (override)

### Immersive Personalities  (`3596393244`, playset #60)

- `common/on_action/zz_gptev_on_actions.txt` — **A1, A2, A3** (override)
  - A1: Age-16 birthday guard: added is_human = yes to gpt_on_birthday_animal_archetypes trigger (expected 1, applied 1)
- `events/zz_gptev_events.txt` — **A4** (override)
  - A4: Game-start living-character sweep guard: added is_human = yes inside every_living_character limit in gpt_olympia_animal_archetype.1000 (expected 1, applied 1)

### Royal Court Event Pack  (`3360676953`, playset #61)

- `common/on_action/xx_gptc_on_action_replace.txt` — **—** (override)

### CK3 Naval Combat  (`3772178688`, playset #62)

- `common/scripted_triggers/naval_combat_triggers.txt` — **P60_NAVAL_COMBAT_DEAD_CULTURES** (override)
  - base = CK3 Naval Combat naval_combat_triggers.txt VERBATIM apart from the changes below

### A Landed Knights Mod  (`3361162762`, playset #71)

- `common/on_action/on_add_vet_modifer.txt` — **P61_LANDED_KNIGHTS_HARD_FATHER_SCOPE** (override)
  - base = A Landed Knights Mod on_add_vet_modifer.txt VERBATIM apart from one operator

### Court Positions Expanded 1.19  (`2754449789`, playset #83)

- `common/court_positions/types/00_exp_grand_vizier_position.txt` — **P66_GRAND_VIZIER_DEAD_RELIGION** (override)
  - base = Court Positions Expanded 1.19 file VERBATIM apart from three lines

### AGOT Great Councils  (`3621472324`, playset #84)

- `common/scripted_triggers/zzzzzz_is_human_direwolf_merge.txt` — **P64_IS_HUMAN_DIREWOLF** (override)
  - base = AGOT Great Councils' is_human block VERBATIM

### (authored here)

- `common/casus_belli_types/zz_agot_mw_revolt_succession_fix.txt` — **—** (authored)
  - MWRSF_REVOLT_AND_REBELLION_CB_OVERRIDE
- `common/modifier_definition_formats/zz_observer_stack_culture_opinion_definitions.txt` — **P03_VALEMAN_DEF_FORMAT** (authored)
- `common/modifiers/zz_observer_stack_missing_canon_child_modifiers.txt` — **P33_GREYJOY_13_ALT_MODIFIER_DEFINED** (authored)
- `common/scripted_effects/zz_agot_claimant_faction_war_fix.txt` — **—** (authored)
  - CFWF_CLAIMANT_FACTION_WAR_EFFECTS
- `common/scripted_effects/zz_observer_stack_canon_child_missing_effects.txt` — **P33_CANON_CHILD_BIRTH_EFFECTS_98_104** (authored)
  - P14.1_MISSING_EFFECT_SHIMS
- `common/scripted_triggers/zz_observer_stack_canon_child_missing_triggers.txt` — **P33_CANON_CHILD_TRIGGERS_98_104** (authored)
  - P14.1_MISSING_TRIGGER_SHIMS
- `events/agot_mw_revolt_succession_fix_crown_events.txt` — **—** (authored)
  - MWRSF_SYNCHRONOUS_CROWN_CHOICE_CHAIN
- `events/agot_mw_revolt_succession_fix_events.txt` — **—** (authored)
  - MWRSF_DEFERRED_REVOLT_PUNISHMENT
- `localization/english/agot_mw_revolt_succession_fix_l_english.yml` — **—** (authored)
  - MWRSF_LOCALIZATION
- `localization/replace/english/zz_observer_stack_guard_book_l_english.yml` — **P37_SWORDS_OF_BRAAVOS_JOIN_NO_LINK_MARKUP** (authored)

