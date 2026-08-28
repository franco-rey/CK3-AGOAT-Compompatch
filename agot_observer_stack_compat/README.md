# AGOT Observer Stack Compatibility

Last-loaded local compatibility mod (load position 43) for the 43-mod AGOT playset
recorded in `observer test.ck3`. Built per `CK3_observer_test_patch_implementation_manual.md`
(§1–§13), CK3 1.19.0.6 / AGOT 0.5.1.

## Contents (P01–P07 complete-file overrides, hash-gated)

| Module | Repair |
|---|---|
| P01 | AGOT+ canon-child repair (202 dual `location`+`employer` removals, newborn court attach, 8 parse repairs) |
| P02 | AGOT+ setup/artifact/crown API migration (5 files) |
| P03 | Crowns of Westeros culture migration (20 references) + additive `valeman_main_opinion` definition |
| P04 | EP3 local-settlement province-scope limit fix (1 call site) |
| P05 | Lorath candidacy exclusion (2 guards in `support_candidacy_interaction`) |
| P06 | COW-AGOT special-building syntax repair (2 opinion tokens + 1 holding limit) |
| P07 | County-view scrollarea `ignoreinvisible` removal (1 line) |

P08 is **not** part of this mod: it updates the existing local `miv_agot_cb_patch` (v1.0.0 → v1.0.1).

## Source identity (SHA-256 gate, all verified at build time)

| Provider | Virtual path | Hash (prefix) |
|---|---|---|
| 2962333032 | `events/dlc/ep3/ep3_laamp_decision_events.txt` | `412bd22f2b85bc7e…` |
| 2962333032 | `common/character_interactions/06_ep3_interactions.txt` | `7cb2344b17b8b7eb…` |
| 2950245430 | `common/scripted_effects/asoiaf_canon_children_effects.txt` | `080981232f070867…` |
| 2950245430 | `common/artifacts/templates/asoiaf_artifacts_templates.txt` | `7819e8e963bc5929…` |
| 2950245430 | `common/scripted_effects/asoiaf_setup_effects.txt` | `60daa8eaa60ab1bf…` |
| 2950245430 | `common/scripted_character_templates/asoiaf_invader_templates.txt` | `67ed5a01e2b1226a…` |
| 2950245430 | `common/modifiers/asoiaf_artifact_modifiers.txt` | `b781c7358e4a93e7…` |
| 2950245430 | `common/on_action/agot_on_actions/test_title_on_actions.txt` | `c5d8c4ed2a7e7d74…` |
| 2950245430 | `common/scripted_effects/asoiaf_scripted_effects_artifacts.txt` | `42c5da841ddb3601…` |
| 2995674648 | `common/artifacts/templates/ntc_artifacts_templates.txt` | `4a6a2270954c0250…` |
| 2995674648 | `common/scripted_triggers/00_ntc_crown_commission_triggers.txt` | `a32c297dc92b8947…` |
| 2995674648 | `common/scripted_character_templates/ntc_scripted_character_template.txt` | `2d5333009be4138a…` |
| 2995674648 | `common/modifiers/ntc_artifact_modifiers.txt` | `bef9756f993e2376…` |
| 2971198450 | `common/buildings/yy_agotcities_special_buildings_westeros.txt` | `d0517274f260152d…` |
| 3316173814 | `gui/window_county_view.gui` | `b3958c445ac4ba1a…` |
| local | `common/on_action/interactive_on_actions.txt` | `e03f3400ec01f0f8…` |

## Load order

This mod must load **last** (position 43). Enabling it in the launcher appends it at the end of
the mod list; keep it there. Dependencies are declared in `descriptor.mod` using the exact
`name=` values of the six enabled descriptors on the build machine.

## Rebase warning

Every override is hash-gated. After any AGOT / AGOT+ / Crowns / COW-AGOT / Patch AGOT–MBS
update, the source hashes in `manifest/source_hashes.sha256` will no longer match: stop and
rebase against the new sources rather than applying blind replacements.

## Runtime validation (manual §14) — performed in-game, not at build time

1. **Startup smoke test** (§14.1): archive `logs`, start the same bookmark/rules, stay unpaused
   through setup, exit; every error family in the §14.1 table must be 0.
2. **Targeted functional test** (§14.2): canon birth per mother state, one crown commission,
   one historical crown, Krakenfall, one case per migrated culture, Visit Local Settlement,
   valid administrative candidacy, Lorath succession, COW building completion, county GUI.
3. **25-year observer regression** (§14.3) and **100-year observer regression** (§14.4):
   `error.log` must not reach 100,000 entries; compare years 25/50/75/100 with the original run.

See `manifest/validation_results.md` for the static build results and the runtime checklist.
