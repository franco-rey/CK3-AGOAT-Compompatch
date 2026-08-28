# Validation results — AGOT Observer Stack Compatibility build (2026-08-28)

## §4 hash gate (pre-build)

| Source | Expected | Actual | Result |
|---|---|---|---|
| AGOT ep3 decision events (P04) | `412bd22f2b85bc7e…` | `412bd22f2b85bc7e…` | PASS |
| AGOT EP3 interactions (P05) | `7cb2344b17b8b7eb…` | `7cb2344b17b8b7eb…` | PASS |
| AGOT+ canon children (P01) | `080981232f070867…` | `080981232f070867…` | PASS |
| AGOT+ artifact templates (P02.3) | `7819e8e963bc5929…` | `7819e8e963bc5929…` | PASS |
| AGOT+ setup effects (P02.1) | `60daa8eaa60ab1bf…` | `60daa8eaa60ab1bf…` | PASS |
| AGOT+ invader templates (P02.2) | `67ed5a01e2b1226a…` | `67ed5a01e2b1226a…` | PASS |
| AGOT+ artifact modifiers (P02.4) | `b781c7358e4a93e7…` | `b781c7358e4a93e7…` | PASS |
| AGOT+ test title on-actions (P02.5) | `c5d8c4ed2a7e7d74…` | `c5d8c4ed2a7e7d74…` | PASS |
| AGOT+ scripted artifact effects (P02.5) | `42c5da841ddb3601…` | `42c5da841ddb3601…` | PASS |
| Crowns artifact templates (P03) | `4a6a2270954c0250…` | `4a6a2270954c0250…` | PASS |
| Crowns crown-commission triggers (P03) | `a32c297dc92b8947…` | `a32c297dc92b8947…` | PASS |
| Crowns character template (P03) | `2d5333009be4138a…` | `2d5333009be4138a…` | PASS |
| Crowns artifact modifiers (P03) | `bef9756f993e2376…` | `bef9756f993e2376…` | PASS |
| COW-AGOT special buildings (P06) | `d0517274f260152d…` | `d0517274f260152d…` | PASS |
| Patch AGOT-MBS county GUI (P07) | `b3958c445ac4ba1a…` | `b3958c445ac4ba1a…` | PASS |
| Local MIV patch on-actions (P08) | `e03f3400ec01f0f8…` | `e03f3400ec01f0f8…` | PASS |

All 16/16 sources match the manual.

## Transform counts (required vs applied)

- `common/scripted_effects/asoiaf_canon_children_effects.txt`: {'P01_REMOVE_DUAL_PLACEMENT': 202, 'P01_ATTACH_NEWBORN_TO_COURT': 1, 'P01_TRAIT_ADD': 1, 'P01_DYNASTY_TRIGGER_ANY': 6, 'P01_SPOUSE_NOT_BLOCK': 1, 'P01_TOTAL_ADJACENT_PARSE_REPAIRS': 8}
- `common/scripted_effects/asoiaf_setup_effects.txt`: {'P02_UNDERAGED_SCOPE_PREFIX': 107, 'P02_HAS_CLAIM_ON': 15, 'P02_IS_DEAD_TRIGGER': 2, 'P02_REMOVE_NOOP_EXISTS': 9}
- `common/scripted_character_templates/asoiaf_invader_templates.txt`: {'P02_INVADER_IS_DEAD': 1}
- `common/artifacts/templates/asoiaf_artifacts_templates.txt`: {'P02_KRAKENFALL_HOUSE_SCOPE': 1}
- `common/modifiers/asoiaf_artifact_modifiers.txt`: {'P02_WESTERMAN_OPINION': 1}
- `common/on_action/agot_on_actions/test_title_on_actions.txt`: {'P02_CROWN_CREATOR_CALLS': 7, 'P02_CROWN_CREATOR_CALLS_REQUIRED_BY_MANUAL': 8}
- `common/scripted_effects/asoiaf_scripted_effects_artifacts.txt`: {'P02_CROWN_CREATOR_DECLARATIONS': 3, 'P02_CROWN_CREATOR_FIELDS': 6}
- `common/artifacts/templates/ntc_artifacts_templates.txt`: {'culture:stormlander': 10, 'culture:riverlander': 3, 'culture:valeman': 3, 'culture:westerman': 1}
- `common/scripted_triggers/00_ntc_crown_commission_triggers.txt`: {'culture:stormlander': 2}
- `common/scripted_character_templates/ntc_scripted_character_template.txt`: {'culture:mountain_clansman': 1}
- `common/modifiers/ntc_artifact_modifiers.txt`: {'valeman_opinion': 3}
- `events/dlc/ep3/ep3_laamp_decision_events.txt`: {'P04_PROVINCE_SCOPE_LIMIT': 1}
- `common/character_interactions/06_ep3_interactions.txt`: {'P05_LORATH_EXCLUSION': 2}
- `common/buildings/yy_agotcities_special_buildings_westeros.txt`: {'P06_RHOYNISH_OPINION': 2, 'P06_HOLDING_CONTEXT': 1}
- `gui/window_county_view.gui`: {'P07_SCROLLAREA_IGNOREINVISIBLE': 1}

## Deviations from manual (count-gate hits)

- **P02_CROWN_CREATOR_CALLS** in `common/on_action/agot_on_actions/test_title_on_actions.txt`: required 8, applied 7. Manual §6.5 lists 8 crown-effect calls incl. agot_create_artifact_visenya_circlet_effect; the hash-gated source contains 7. Raw-byte search of the file and the entire AGOT+ mod (2950245430) finds zero occurrences of 'visenya'/'circlet'. No call to that effect exists in this stack, so no missing-CREATOR error family exists for it. Count NOT adjusted; 7/8 applied.

## §5.4 record — dragon-scheme references (no fix applied, per manual)

Manual reports 22 `start_scheme` calls with unreadable fixed dragon targets in
`asoiaf_canon_children_effects.txt`. Static scan of the hash-gated source finds **24**
`target = character:dragon_*` scheme targets (lines listed below). The disposition
depends on bookmark/game-rule branches per §5.4; correction is deferred until one is
reproduced in a bookmark where the dragon should exist. No substitution was made.

| Line (source) | Target |
|---|---|
| 4381 | `character:dragon_quicksilver` |
| 4476 | `character:dragon_balerion` |
| 4630 | `character:dragon_quicksilver` |
| 4792 | `character:dragon_vermithor` |
| 4883 | `character:dragon_silverwing` |
| 5183 | `character:dragon_balerion` |
| 5419 | `character:dragon_caraxes` |
| 5553 | `character:dragon_meleys` |
| 6333 | `character:dragon_meleys` |
| 6441 | `character:dragon_balerion` |
| 6544 | `character:dragon_caraxes` |
| 6731 | `character:dragon_syrax` |
| 6898 | `character:dragon_sunfyre` |
| 7022 | `character:dragon_dreamfyre` |
| 7133 | `character:dragon_vhagar` |
| 7284 | `character:dragon_tessarion` |
| 7427 | `character:dragon_moondancer` |
| 7515 | `character:dragon_morning` |
| 7842 | `character:dragon_vermax` |
| 7996 | `character:dragon_arrax` |
| 8143 | `character:dragon_tyraxes` |
| 8285 | `character:dragon_stormcloud` |
| 11746 | `character:dragon_vhagar` |
| 11831 | `character:dragon_seasmoke` |

## Static acceptance results

- P01: create_character=202, employer lines=0, location lines=202, parentage calls=202, travel calls=202, trait->add_trait +1 (15->16), any_dynasty_member=6, every_dynasty_member=15 (effect-context pair preserved)
- P02.1: unscoped asoiaf_underaged=0, scoped=107, has_claim_on=15, is_dead=0, 9 no-op exists removed, limit-context exists=character:Melisandre_1 preserved
- P02.2: invader is_dead=0 / is_alive=no=1; P02.3: house:house_BaratheonKL=1; P02.4: westerman_main_opinion=1
- P02.5: 7 crown calls now carry CREATOR=this; robertI/joffreyI/renly OWNER-only calls untouched (per manual); 3 defs gained $CREATOR$ + 6 creator fields
- P03: obsolete culture keys=0 (stormlander_main=10, riverman_main=3, valeman_main 1->4, westerman_main 6->7, moon_clan template=1); valeman_main_opinion=5 x3; additive def file created
- P04: province-scoped limit now `exists = county`; shared trigger definition untouched
- P05: 2 d_lorath guards added; no other title/succession changes
- P06: the_mother_religion_opinion x2; holding-limit collapsed to NOT={has_building=castle_05}; add_building preserved
- P07: 19->18 ignoreinvisible; only the buildings_grid_wrapper scrollarea line removed; size 320x120 intact
- All 16 gameplay files: UTF-8+BOM, LF, no NUL, brace depth 0 with no negative dips, strings closed

## Excluded from this build (diagnostic-only / not authorized)

- D01 (§15): Council Experience isolation — not built; AGOT–Council Experience (3319167091) files untouched.
- D02 (§16): war / Mega Wars scope telemetry — not built; no diagnostic mod created.
- §17: MAA observer nulls, epidemics, schemes, weddings, dead-character perks,
  portrait/DNA/vanity port, pruning — no production patch authorized; nothing shipped.

## Runtime matrix (manual §14) — to be completed in-game

### 14.1 Startup smoke (threshold 0 for every family)

- [ ] dual location+employer create-character validation: ____
- [ ] P01 canon parser errors: ____
- [ ] P02 obsolete setup trigger/effect syntax: ____
- [ ] crown missing/unknown CREATOR arguments: ____
- [ ] missing Crowns culture keys: ____
- [ ] obsolete culture/religion opinion tokens: ____
- [ ] COW unknown holding trigger: ____
- [ ] MIV removed random-ruler effect: ____
- [ ] county-view wrapper GUI errors after opening county view: ____

### 14.2 Targeted functional (setup / expected / actual / log excerpt)

- [ ] canon birth per mother state (ruler/courtier/traveling landless/etc.)
- [ ] one crown commission (owner+creator set, single artifact, visuals per game rule)
- [ ] one historical crown creation
- [ ] Krakenfall scoring/eligibility
- [ ] one Crowns culture case per migrated culture
- [ ] Visit Local Settlement (coastal/inland/island/landlocked)
- [ ] valid administrative candidacy (2+ titles)
- [ ] Lorath succession unchanged
- [ ] affected COW building completion (with/without castle_05)
- [ ] county GUI grid/scrollbar

### 14.3 25-year observer regression

- [ ] zero recurrence of P01–P08 target families; no new error family from compatibility files

### 14.4 100-year observer regression

- [ ] error.log does NOT reach 100,000 entries; checkpoints at 25/50/75/100 vs original run
- [ ] save → exit → CRC check → reload → advance 1 year → save
