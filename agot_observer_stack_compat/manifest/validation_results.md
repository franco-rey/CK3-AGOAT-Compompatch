# Validation results — AGOT Observer Stack Compatibility v1.1.0

Implementation state: **implemented and statically verified**

Date: 2026-08-29

Runtime status: **PENDING USER PLAYTEST / SAVE-LOG REVIEW**

## Repository and source preflight

- Audit-start Git state: `main` tracking `origin/main` with the intended uncommitted v1.1 implementation delta already present (34 files total); no unrelated changes were identified.
- Source roles resolved from the user-supplied mod repository and Workshop root; all Workshop inputs are outside the writable repository.
- Retained v1 source gates: 15/15 available Workshop inputs rechecked PASS; the historical pre-P08 local hash remains in the manifest, while the installed P08 gameplay is verified at `d402a25411f7d691ae682f8e99fc88aca1c4fc09ac089c3a47fdade14dd1ab8e`.
- v1.1 Workshop source gates: 22/22 PASS before staging and PASS after implementation.
- current-local v1.0.0 gates: 4/4 PASS before transformation.
- protected OPB gates: 4/4 PASS before and after; no OPB file changed.
- No `REBASE REQUIRED` or `UNRELATED LOCAL PATCH CHANGED` condition occurred.

## Applied transformation counts

- P09: one dead-holder branch replacement, two soft scopes, and one living guard.
- P10: two ruler-guarded triggers and two actor-guarded effects.
- P11: four `is_head_of_faith = no` guards; two Lorath guards and all three score calls retained.
- P12: eight `CREATOR = this` additions (3 local on-action + 5 Legacy Of The Dragon).
- P13: three orphan `on_complete` blocks removed; `planky_town_special`, `agot_castamere_03`, and `agot_castamere_ruins_02` remain.
- P14: 4 trigger shims + 7 effect shims created, 1 nickname key fixed, 24 canon-child and 10 yearly fixed-dragon scheme blocks removed; 24 + 10 forced bond branches retained.
- P15: one `exists = liege` guard inserted.
- P16: one memory scope softened.
- P17: one option trigger inserted.
- P18: four modifier prerequisite lines inserted and one hard special-title block replaced.
- P19: one six-prerequisite new-ruler block inserted; no effect block removed.
- P20: 3 CB guards, 5 localization type declarations, 2 heir soft scopes, 2 permanent-transfer prerequisite sets, 3 cleanup variable guards, 2 task-target scope corrections to the surviving oathbound variable owner, 2 event-variable requirements, 3 event soft scopes, 1 Persia sway replacement, and 1 Persia ransom block removal.
- P21: 1 fabricate definition replaced, 12 memory-count calls migrated, 1 RICE revalidation neutralized, 4 missing-trait checks + 3 physician-chain lines + 1 Papacy block + the RICE/crossing/elective sections + 1 purple-trait check removed.
- P22: 24 missing-trait cases, 14 Confucian cases, 8 religion-family cases, 10 council cases, 18 minister cases, and 2 gunpowder cases replaced; 28 invalid mixed-OR lines removed.
- P23: one portable MIV descriptor version changed from 1.0.0 to 1.0.1; gameplay unchanged.

The machine-readable exact operation counters are retained in `manifest/build_manifest.json` under `implementation_counts`.

## Static validation

- PASS: all 28 changed/added gameplay files are UTF-8 with LF, have no NUL bytes, balanced braces with no negative dip, and closed quoted strings.
- PASS: portable descriptors and documentation use LF; JSON parses.
- PASS: no temporary/staging path leaked into production files and no `replace_path` was added.
- PASS: all exact forbidden-token checks in the implementation specification.
- PASS: Oathbound sway/murder cleanup guards and comparisons use the surviving oathbound (`scope:target`), where those task variables are assigned, rather than the dead oathholder (`root`). This corrects an ambiguity/error in P20.3 of the specification.
- PASS: exactly 4 canon trigger shims, 7 canon effect shims, 5 Oathbound `type = character` declarations, and 3 inserted CB availability guards.
- PASS: zero owner-only calls to the eight affected crown effects in the final overriding files.
- PASS: 34 fixed-dragon scheme calls removed while 34 forced relationship branches/toasts remain.
- PASS: zero unsupported P22 database keys and no empty `OR`/`NOR` introduced by the named removals.
- PASS: MIV gameplay hash remains `d402a25411f7d691ae682f8e99fc88aca1c4fc09ac089c3a47fdade14dd1ab8e`.
- PASS: Observer portable descriptor is 1.1.0, retains `supported_version="1.19.0.6"`, and declares the seven required added dependencies.

## Final hashes — P09–P22 changed/added gameplay files

| Virtual path | Final SHA-256 |
|---|---|
| `common/buildings/yy_agotcities_special_buildings_westeros.txt` | `ce75dc485d29b771774316b0b9df58efd0fe1ff53a6fc4874c20a56fe0b2ffac` |
| `common/casus_belli_types/oathbound_conquests.txt` | `6144736e0646da6be6ae269932299d36566e8ad8ecf932f00e22859b33e7cb74` |
| `common/character_interactions/06_ep3_interactions.txt` | `27a6bc7f49ffb6d929a441ad206f34bc34331d10d6b964ed9d0441eeed25787e` |
| `common/character_interactions/oathbound_ransom_interaction.txt` | `e655372afb7a6154a5a71a4a829408b205491ab1870dae7c54a135e442775f01` |
| `common/customizable_localization/oathbound_custom_loc.txt` | `9e560d5f9b03e3a0ce5201575c8f898e565b4e75c81a8e69ac4113a2f89a30e0` |
| `common/factions/00_factions.txt` | `89afd7d76158f4ebb60801b7732f7586b9595bb86f5b5d61c8d42d89d90ab23c` |
| `common/on_action/agot_on_actions/test_title_on_actions.txt` | `1707def3f76fbf5bd743b0bec68efb68a6a7753cd18462fb14fb0213dc8dd890` |
| `common/on_action/asoiaf_yearly_on_actions.txt` | `0e5c15d8f0f3ff8aef61e1f9d432cf10f7d398ab749a9446ac0726601a3641d7` |
| `common/on_action/gr_on_actions.txt` | `756b2247d9bccdc38449290c9faee734b158507abd39d432069853b439a957d0` |
| `common/on_action/relations/oathbound_on_relation_deaths.txt` | `4383797b93e2f37c2976eff907ca6b943eda1d77dca68e9d402a5ea008180133` |
| `common/on_action/zz_gr_memory_tracking.txt` | `6f18d59272f3a70cdc9030e4d2bb482fd46b1120ca0e7b31d6824753d4e21c4c` |
| `common/scripted_effects/00_agot_hf_effects.txt` | `5c81c79b6dfc9b3d1227cc4b805e6a758fa94bbb3fb48d8332b6b9a81ec3638f` |
| `common/scripted_effects/00_interaction_effects.txt` | `6535e5853ec09ab2572819ff9af1238cac19f93c0072db502fd218fc92664811` |
| `common/scripted_effects/20_health_effects.txt` | `f1536a47e61fb622c8326a4742bf44ea1d134bd582705baba51da2c8987bbd09` |
| `common/scripted_effects/asoiaf_canon_children_effects.txt` | `ffcf1299dbf37c3ed21f1bddaadef492b3494b133adb7adc6805eaefb86c4775` |
| `common/scripted_effects/zz_observer_stack_canon_child_missing_effects.txt` | `656697f7804abcd76b361daedebee94ab42e21818144f2cbb1c26e47d7b29828` |
| `common/scripted_modifiers/00_faction_modifiers.txt` | `694f20806130a5b9c6d71c4701091c6148f6bac410cf7ebb088ba25643241866` |
| `common/scripted_triggers/00_agot_triggers.txt` | `94ac2c04ab9f1744e189e3ffa3491103449314f94b15efc0b206fdafb77d08e9` |
| `common/scripted_triggers/00_courtier_guest_management_triggers.txt` | `9b7af5257e72364b9267d9155fdad07025d71fbb420cd98383596f50e1286f44` |
| `common/scripted_triggers/asoiaf_clothing_triggers.txt` | `7c668bd2df1947c8b21be753ef3d032d6d95863854a505e2097e3ea9836fb144` |
| `common/scripted_triggers/gen_acs_st_big_switch.txt` | `a2324c3e415559ca882d8ba72d8d6bdb08c229c08ba59062a8e5a137ecdcdc5e` |
| `common/scripted_triggers/zz_observer_stack_canon_child_missing_triggers.txt` | `f4859d089d7fa0b9bfe3a24a08c21845c29f0f195e623db1ed7589698876b192` |
| `events/decisions_events/rediscover_events.txt` | `f38164d695316f2f61a3cc70c333e9f90166f35ba0b4ba9ca5845272490649c6` |
| `events/dlc/bp1/bp1_yearly.txt` | `35a6af5485b02b08ef6ac887e7517d2d7787c6dd7d2de95c96dd88b976bb93ee` |
| `events/gr_obituary_events.txt` | `3526f157cd9d57f8c9cbf3e9c47d772e4d5821d240c4f31b55676588e756e978` |
| `events/gr_obituary_replay_events.txt` | `8133b62971aa58c8ecf212ca0f8a77d28ad565dd4ce8cd6570810f0cc24d8e60` |
| `events/oathbound_heir_events.txt` | `565244825e173d1e0544403d5b38fd39810c3c851fd3e946718c5870449b08f3` |
| `events/scheme_events/oathbound_sway_vassals_events.txt` | `038abd4c2e77cf649714dfad9e95a20794be48fcf2e2f16f6f00383200f4d5d8` |

All 40 final Observer gameplay files, including unchanged P01–P07 outputs, are recorded with full hashes in `build_manifest.json` and `source_hashes.sha256`.

## Intended definition ownership (static, load-order conditional)

| Definition(s) | Source provider | Observer final virtual path |
|---|---|---|
| `agot_flavour_is_in_westeros_trigger`, `agot_flavour_is_living_in_westerosi_realm_trigger` | AGOT 2962333032 | `common/scripted_triggers/00_agot_triggers.txt` |
| courtier/guest claim triggers | AGOT 2962333032 | `common/scripted_triggers/00_courtier_guest_management_triggers.txt` |
| kick-from-court effects | AGOT 2962333032 | `common/scripted_effects/00_interaction_effects.txt` |
| `support_candidacy_interaction` | AGOT 2962333032 | `common/character_interactions/06_ep3_interactions.txt` |
| `claimant_faction`, `claimant_faction_modifiers` | AGOT 2962333032 | `common/factions/00_factions.txt`; `common/scripted_modifiers/00_faction_modifiers.txt` |
| `agot_hf_force_house_head` | House Founders 2967263410 | `common/scripted_effects/00_agot_hf_effects.txt` |
| all three Oathbound CBs | Oathbound 3457401824 | `common/casus_belli_types/oathbound_conquests.txt` |
| `gr_internal_fabricate_tracking`, `gr_internal_obituary_processing` | Grand Remembrance 3678529052 | `common/on_action/zz_gr_memory_tracking.txt`; `common/on_action/gr_on_actions.txt` |
| `acs_switch_filter` | ACS 3084203091 | `common/scripted_triggers/gen_acs_st_big_switch.txt` |
| `portrait_wear_helmet_trigger` | AGOT + AGOT+ 2950245430 | `common/scripted_triggers/asoiaf_clothing_triggers.txt` |

Every listed definition exists at the intended Observer virtual path. The claimant patch's two scripted-effect definitions remain only in `agot_claimant_faction_war_fix/common/scripted_effects/zz_agot_claimant_faction_war_fix.txt`; Observer does not shadow that file.

This is a static ownership result only. It assumes the user loads Observer after all of its providers, keeps Immersive Personalities and Royal Court Event Pack after the AGOT/local-patch portion as configured, and loads AGOT OPB Addon Compatibility final.

## OPB/new-mod collision audit

- Observer has zero gameplay virtual-path collisions with Immersive Personalities 3596393244, Royal Court Event Pack 3360676953, or protected OPB.
- Intentional OPB overlaps only: `common/on_action/zz_gptev_on_actions.txt` and `events/zz_gptev_events.txt` override Immersive Personalities; `common/on_action/xx_gptc_on_action_replace.txt` overrides Royal Court Event Pack.
- Neither new Workshop mod nor OPB contains any intended-ownership definition listed above.

## Final Git diff/status summary

- Intended repository delta: 34 files total — 24 added and 10 modified.
- Gameplay: 24 complete/additive files added and 4 existing Observer gameplay files revised.
- Metadata/docs: Observer descriptor + README + 3 manifest files modified; MIV portable descriptor modified.
- No temporary staging output is inside the repository.
- No Workshop/source, launcher playset, launcher database/cache, `dlc_load.json`, machine-specific pointer `.mod`, OPB file, claimant scripted-effect file, branch, or Git history operation was changed.

## Runtime checklist — all pending

Every item below is **PENDING USER PLAYTEST / SAVE-LOG REVIEW**. CK3 was not launched.

### Startup smoke

- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — missing `CREATOR` for all eight crown effects.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — unknown Targaryen 98–104 effects / 101–104 triggers.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — unreadable fixed-dragon scheme targets and missing Tyrion nickname.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — missing `agot_cities.5000`.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — ACS and Grand Remembrance database/PostValidate families.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — removed memory-count trigger and Oathbound localization/Persia families.

### Targeted functional checks

- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — courtier/guest claim and kick-from-court tooltips.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — portrait cases including a liegeless order member.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — valid administrative title vs Faceless Men candidacy.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — commissioned and rediscovered crowns.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — affected COW building completion.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — disease tooltip and real epidemic memory.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — BP1 8180 without a standard council seat.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — claimant faction with/without legitimate-house state.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — House Founders landed and incomplete transitions.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — three Oathbound CBs with live/missing/dead oathholder.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — Oathbound death/heir cleanup and sway task.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — GR fabricate count and obituary 1/3/10 thresholds.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — ACS supported and neutralized filter pairs.

### Normal-play checkpoints

- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — 5-year log archive.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — 25-year save/exit/reload/month advance.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — 50-year checkpoint.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — 100-year checkpoint without the 100,000-record ceiling.

---

## Static validation — 2026-08-29 revision wave (P24–P33, no version bump)

Evidence baseline: independent 405-year observer run, 7899–8304.

### Preconditions

- 11/11 Workshop source hashes recomputed and matched before editing.
- 7/7 already-owned installed-patch hashes recomputed and matched before editing.
- 0 shared virtual paths among the five local patches after the build.
- Every new override has exactly one upstream provider; no later-loading enabled mod owns any of them.
- Only the three authorized patch directories were modified.

### Transformation counts (expected = actual)

| Module | Virtual path | Transformation | Count |
|---|---|---|---:|
| P24 | `common/scripted_guis/gr_scripted_guis.txt` | `P24_GR_CHRONICLE_NULL_SCOPE` | 1 |
| P25 | `common/scripted_effects/gr_npc_obituary_data_effect.txt` | `P25_RICE_SECTION_REMOVED` | 1 |
| P26 | `common/scripted_effects/acs_se_religion.txt` | `P26_RELIGION_FAMILY_SINGLE_BUCKET` | 2 |
| P27 | `common/character_interactions/06_ep3_interactions.txt` | `P27_APPOINTMENT_TITLE_LAW` | 2 |
| P28 | `common/scripted_effects/00_interaction_effects.txt` | `P28_RECRUIT_SCOPE_GUARD` | 1 |
| P29 | `common/story_cycles/agot_story_cycle_naming_and_title_gui.txt` | `P29_SCION_STORY_SELF_TERMINATE` | 1 |
| P30A | `events/agot_events/agot_dragon_events.txt` | `P30A_DRAGON_TERROR_TOP_LIEGE` | 2 |
| P30B | `common/scripted_triggers/00_agot_coa_triggers.txt` | `P30B_COA_DYNASTY_FOUNDER_SOFT` | 33 |
| P31A | `common/on_action/asoiaf_yearly_on_actions.txt` | `P31A_MANCE_GIANT_REGIMENT` | 1 |
| P31B | `common/scripted_character_templates/asoiaf_invader_templates.txt` | `P31B_YOUNG_GRIFF_NICKNAME` | 1 |
| P31C | `common/scripted_effects/asoiaf_targaryen_invasion_claimants_effects.txt` | `P31C_YOUNG_GRIFF_NICKNAME_AND_TRAIT` | 2 |
| P31D | `events/asoiaf_young_griff_landing_events.txt` | `P31D_DUMMY_CHARACTER_LOCATION` | 2 |
| P32A | `common/scripted_effects/asoiaf_agot_overwrite_effects.txt` | `P32A_DRAGON_FAITH_VALYRIAN_PAN_DRAGON` | 7 |
| P32B | `common/scripted_effects/asoiaf_setup_effects.txt` | `P32B_MORE_BOOKMARKS_RHLLOR_REMOVED` | 2 |
| P33a | `common/scripted_triggers/zz_observer_stack_canon_child_missing_triggers.txt` | `P33_CANON_CHILD_TRIGGERS_98_104` | 7 |
| P33b | `common/scripted_effects/zz_observer_stack_canon_child_missing_effects.txt` | `P33_CANON_CHILD_BIRTH_EFFECTS_98_104` | 7 |
| P33c | `common/scripted_effects/asoiaf_assign_inactive_traits_effects.txt` | `P33_TARGARYEN_95_MODIFIER_REMOVED` | 1 |
| P33d | `common/modifiers/zz_observer_stack_missing_canon_child_modifiers.txt` | `P33_GREYJOY_13_ALT_MODIFIER_DEFINED` | 1 |

### Structural checks

- Brace balance verified on every changed file (comment- and string-aware scan): PASS.
- UTF-8 BOM, LF endings and trailing-newline convention preserved per source file: PASS.
- Residual-token scans (word-boundary where a corrected token is a superstring):

  - `RICE_` in the P25 file: 0
  - `rf_abrahamic` / `rf_eastern` / `rf_pagan` in the P26 file: 0
  - three-line holder-level appointment guard at the two P27 sites: 0 (the unrelated line-82 `is_valid` site is deliberately retained)
  - unguarded `scope:recruit` comparison in the P28 effect: 0
  - `house = dynasty:dynn_*.dynasty_founder.house` in P30B: 0; soft form: 33; static house comparisons: unchanged
  - `type = giant` as a whole token: 0 (`type = giant_regiment` present)
  - `nick_young_griff`, `is_targaryen_11`, `asoiaf_Targaryen_95_modifier`: 0
  - `faith:valyrian` / `faith:rhllor` as whole tokens: 0
  - non-empty body for `fp3_struggle_ending_concession_effects`: none
  - unguarded `joined_faction` dereference in the claimant interaction: 0

### Dependency existence checks

- `giant_regiment`, `nick_agot_young_griff`, `valyrian_pan_dragon`, `has_title_law_flag`,
  `acs_gvl_rf_other`, `acs_set_update_rf = { FAMILY = other }`, `heritage_summer`,
  `language_agot_westeros`, `birth.1001/1002/1003`, traits `asoiaf_Targaryen_98`–`104_trait`,
  `asoiaf_Targaryen_88_trait` and history/DNA for `Targaryen_98`–`Targaryen_104`: all present.

### Runtime status

- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — fresh observer start, error.log must not reach 100,000.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — `gr_chronicle_window:is_shown` signature must be 0.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — open/close the GR chronicle on a living character.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — open ACS, exercise and clear the religion filter.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — 25-year run, then 100-year run with save/reload and 31+ days.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — no stale `scion_title_data` story after reload; dragon storage and the ACS object pool still present.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — P27 residual at the sibling `scope:secondary_recipient` call; apply the specified third guard only if it persists.
- [ ] PENDING USER PLAYTEST / SAVE-LOG REVIEW — canon children 98–104 spawn once each and are not duplicated.

---

## Runtime test 1 — observer run 8283-8334 (51 years), 2026-08-29

Save: `observer test.ck3`. 17 of 18 acceptance signatures returned **zero**:
P25 RICE, P26 religion families, P27 appointment candidates, P28 recruit scope,
P30A/B dragon and CoA scopes, P31 nickname/trait/giant/location, P32 faiths,
P33 canon children and modifiers, MIV Persia/FP3, and the claimant cascade.

P29 confirmed working: 3 surviving `scion_title_data` stories, all with a
**living** `scoped_royal` and an existing `scoped_title`, each scheduled for the
next 30-day tick. The 405-year baseline had 164 of 175 pointing at dead royals.

**P24 FAILED and was re-fixed.** The script-side `exists = this` guard did not
reduce the storm (82,917 baseline -> 81,879). Root cause: the window's `visible`
binding in `gui/gr_chronicle_window.gui` passes `GetPlayer`, which in observer
mode is a dangling character reference. `exists = this` cannot catch that - the
scope is set and typed Character, it just points at nothing. Fixed at the binding
with `And(GetPlayer.IsValid, ...)`. The scripted-GUI guard is retained as
harmless defence in depth but is not the load-bearing fix.

Residual: 6 linter warnings for `acs_gvl_rf_abrahamic/eastern/pagan` "used but
never set" - expected consequence of the P26 single-bucket design, cosmetic.

- [ ] PENDING RE-TEST — `gr_chronicle_window` signature must be 0 in the next run.
- [ ] PENDING RE-TEST — error.log must not reach 100,000.

## P34 — Duel Overlay compatibility (2026-08-29)

Duel Overlay (@55 in the current order) loads before this patch (@60) and ships its
own `gui/event_windows/duel_event.gui` built on vanilla, reverting AGOT's custom
name widget. This patch takes ownership of the path and restores exactly two AGOT
lines on top of Duel Overlay's file. Diff vs the Duel Overlay source is those two
changes and nothing else. Brace balance PASS.

**DireWolves needs no patch.** Verified: its overrides of
`common/scripted_triggers/00_agot_character_triggers.txt` (+1/-0),
`gui/window_character.gui` and `gui/shared/portraits.gui` are all AGOT's content
plus its own additions, and no enabled mod loading after it provides those paths.

- [ ] PENDING RUNTIME — duel window shows AGOT-formatted participant names with the
      Duel Overlay bars visible.
