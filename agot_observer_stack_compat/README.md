# AGOT Observer Stack Compatibility v1.1.0

This aggregate compatibility layer targets CK3 1.19.0.6 / AGOT 0.5.1 and the current 52-mod successor playset. P09–P22 are grounded in runtime evidence from the earlier 49-mod Tybert run; this implementation itself is statically verified only.

## Patch contents

P01–P07 remain intact: AGOT+ canon-child creation and parser repair, AGOT+/artifact/crown API migration, Crowns culture migration, AGOT local-settlement scope repair, Lorath candidacy exclusion, COW-AGOT building repair, and the county-view GUI fix. P08 remains external in `miv_agot_cb_patch`; v1.1 only corrects its portable descriptor to 1.0.1 while preserving its gameplay hash.

| Module | Provider | v1.1 behavior |
|---|---|---|
| P09 | AGOT | Guards dead/weak title-flavor characters and requires a living character for realm traversal. |
| P10 | AGOT | Rejects missing rulers/actors before courtier-claim and kick-from-court evaluation. |
| P11 | LOCAL-1.0.0 / AGOT | Excludes head-of-faith titles from administrative candidacy scoring while retaining Lorath and legitimate appointment behavior. |
| P12 | LOCAL-1.0.0 / Legacy Of The Dragon | Supplies `CREATOR` at all eight legacy crown call sites. |
| P13 | LOCAL-1.0.0 / COW-AGOT | Removes three orphan `agot_cities.5000` completion hooks without altering the buildings. |
| P14 | LOCAL-1.0.0 / AGOT+ | Adds conservative missing Targaryen shims, fixes Tyrion's nickname key, and removes 34 redundant fixed-dragon scheme starts while retaining forced bonds/toasts. |
| P15 | AGOT+ | Guards the unlanded holy-order portrait branch against a missing liege. |
| P16 | AGOT | Soft-scopes the disease memory used during tooltip evaluation. |
| P17 | AGOT | Hides BP1 option A when the council-seat variable was not produced. |
| P18 | AGOT | Guards claimant legitimate-house state and rejects a claimant faction without a special title. |
| P19 | AGOT: House Founders | Defers forced house-head logic until the new ruler and house head have complete landed/title state. |
| P20 | Oathbound | Guards oathholder/heir variables, types custom localization, removes Persia-only sway/ransom branches, and scopes task cleanup to the surviving oathbound variable owner. |
| P21 | Grand Remembrance + AGOT submod | Uses the proven fabricate root, migrates 12 memory-count checks, and removes unsupported vanilla/RICE classifications. |
| P22 | Advanced Character Search | Keeps UI IDs stable while neutralizing unsupported AGOT database filters and removing invalid mixed keys. |

Intentional neutralizations are limited to missing Targaryen branches, redundant dragon scheme starts, orphan city event hooks, non-AGOT Grand Remembrance classifications, Persia-only Oathbound branches, and unsupported ACS filters.

## Load order (user-managed)

The user must load Observer Stack after House Founders, Advanced Character Search, Oathbound, Grand Remembrance, its AGOT submod, Mass Vassal Directives, the claimant patch, and every other source it overrides. Then keep Immersive Personalities and Royal Court Event Pack after the AGOT/local-patch portion as configured, with **AGOT OPB Addon Compatibility final**. Observer Stack is not the final mod.

This implementation did not edit or verify the launcher playset, `dlc_load.json`, launcher databases/caches, or machine-specific pointer `.mod` files.

## Protected OPB post-layer

`agot_opb_addon_compat` v1.0.1 is a separate unchanged final layer. It owns only:

- `common/on_action/zz_gptev_on_actions.txt` — `94548f0f048fe90cf568535edaaa9f15e13b5a2f6b7f2b3cbe02853be9a8ca63`
- `events/zz_gptev_events.txt` — `451f7aa31f248521fc4630ca365d2f16e6eb4fc24747a0231410b4f67a1c78d2`
- `common/on_action/xx_gptc_on_action_replace.txt` — `fd6274c02e1b053147a657ed935acaa2fa08b136844e0e99814ddbd5b7d50e6d`
- portable `descriptor.mod` — `9b95165c8c2d00db46767811cdfb50b14c8e38c2977e6760d2ae4024b281464f`

The gameplay overlaps are intentional: the first two override Immersive Personalities, and the third overrides Royal Court Event Pack. Neither those mods nor OPB contains an Observer P01–P22 gameplay virtual path.

## Rebase warning

Every complete-file override is hash-gated. If a source mod updates and a recorded source hash changes, stop and rebase the transformation against the new file rather than copying blindly. See `manifest/source_hashes.sha256`, `manifest/build_manifest.json`, and `manifest/validation_results.md` for the complete ledger and static results.
