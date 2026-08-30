# AGOT Observer Stack Compatibility v1.1.0

This aggregate compatibility layer targets CK3 1.19.0.6 / AGOT 0.5.1 and the current 61-mod successor playset. P09–P22 are grounded in runtime evidence from the earlier 49-mod Tybert run. P24–P33, added in the 2026-08-29 revision wave without a version bump, are grounded in the independent 405-year observer run 7899–8304. P35-P44, added in the 2026-08-30 revision wave, are grounded in the 8183 Gar Sagon run, which confirmed the P35/P37 title-name repair (landed_titles 663 MB -> 5.7 MB, guard-book prose 7,918,803 -> 49 lines) and exposed the pending-event flood that P39/P41 address.

P45 comes from the 8296 Lucerys of Driftmark run (22 minutes at 5x, no clock freeze), which is the first run to verify the previous wave against live gameplay rather than statically. Eight of the ten patches checked hold at exactly zero: P37, P38, P39/P41, P40, P42, P43, P44. P35 is down from 7,907,555 to 37, all legitimate chronicle writes. `landed_titles` is 6.4 MB and the pending-event queue is healthy. **P24 and P36 are confirmed NOT working** — see the P24/P36 GUI note below before touching either.

Everything else in this layer remains statically verified only.

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
| P24 | Grand Remembrance | **NOT EFFECTIVE — do not treat as fixed.** Intended to require a real character scope before the chronicle window's `is_shown` reads `is_alive`. Same structural flaw as P36, plus three un-overridden call sites (see the P24/P36 GUI note below). The earlier 82,917 → 2,514 drop came from the window being open less, not from the guard working. |
| P25 | Grand Remembrance | Removes the RICE trait-detection section; the RICE mod is not installed, so its 26 trait identifiers never resolved. Non-RICE obituary classification is unchanged. |
| P26 | Advanced Character Search | Collapses religion-family bucketing to the single AGOT-safe `other` list. The vanilla `rf_abrahamic` / `rf_eastern` / `rf_pagan` families do not exist in AGOT. |
| P27 | LOCAL-1.1.0 / AGOT | Scores appointment candidates only for titles that actually use appointment succession, replacing a holder-level realm-law check that admitted ordinary titles such as `c_the_lower_city`. |
| P28 | LOCAL-1.1.0 / AGOT | Requires the optional `recruit` scope to exist before it is compared. |
| P29 | AGOT | Gives the `scion_title_data` story cycle a 30-day self-termination group. AGOT creates one story per title and never ends it, leaving records pointing at dead royals and destroyed titles. |
| P30 | AGOT | Compares the dragon-terror rider's top liege instead of calling `top_liege` on a province scope, and soft-compares dynamic dynasty founders in the Rhllor personal-CoA trigger. |
| P31 | LOCAL-1.1.0 / AGOT+ | Repairs Mance Rayder's `giant` men-at-arms key, both Young Griff nickname keys, the undefined `is_targaryen_11` inactive trait, and the two locationless dummy characters in the landing event. |
| P32 | LOCAL-1.1.0 / AGOT+ | Points the seven dragon spawns at `faith:valyrian_pan_dragon` and removes the two obsolete More Bookmarks `faith:rhllor` migrations. Neither faith id exists in this playset. |
| P33 | LOCAL-1.1.0 / AGOT+ | Implements the seven canon children of Aegon IV (Targaryen 98–104), re-keying AGOT+'s duplicate-trigger typo, and supplies the undefined `asoiaf_Greyjoy_13_alt_modifier` while dropping the undefined `asoiaf_Targaryen_95_modifier` call. |
| P34 | Duel Overlay | Restores AGOT's two name-formatting lines (`agot_text_label_center`, `AGOTGetShortUINameNoTooltip`) on top of Duel Overlay's duel window. Duel Overlay is built on vanilla and otherwise reverts them; all of its own overlay content is preserved. |
| P35 | AGOT: Royal Guards | Makes the Lord Commander guard-book entry once per service page. Ten call sites reach `agot_guard_positions_record_lord_commander_effect` and only one honoured the author's own `agot_guard_positions_command_recorded` flag, so the same appointment was rewritten without bound. |
| P36 | AGOT: Royal Guards | **NOT EFFECTIVE — do not treat as fixed.** Intended to gate the guard-academy HUD widget's `visible` binding on `GetPlayer.IsValid` before it calls `IsShown`. The binding was rewritten as `And(GetPlayer.IsValid, And(...))`, which is logically identical to the original: `And()` in CK3 GUI evaluates every argument, so reordering cannot prevent the `IsShown` call. Confirmed still firing at 2,514 entries in the 8296 Lucerys run. See the P24/P36 GUI note below before attempting again. |
| P37 | AGOT: Royal Guards | Renders the Swords of Braavos join entry with `GetNameNoTooltip` instead of `GetFullName`, matching its six sibling join keys. `GetFullName` emitted `ONCLICK`/`TOOLTIP` link markup into a stored title name, which cannot round-trip through the localization system. |
| P38 | Expanded Domiciles for AGOT | Restores 40 file-scoped `@constants` across six domicile building files. CK3 `@constants` do not cross file boundaries; the mod copied AGOT's and vanilla's building definitions into new `_UE`/`_UY`/`_UC` files but left the definitions behind, so every gold, prestige and construction-time reference silently fell back to engine defaults. |
| P39 | AGOT: Royal Guards | De-duplicates the guard inheritance review. The on_action is registered on three title-gain hooks and each firing fanned out to seven queued events with no guard, flooding the pending-event queue. Sets and honours the author's existing `agot_guard_positions_inheritance_review_pending` flag. |
| P40 | AGOT: Royal Guards | Soft-scopes the four `character:Targaryen_63` switches in the Queensguard on_actions. One runs from `on_death`, i.e. for every death in the world, and hard-switching into a character absent from the era logged a failed context switch each time. |
| P44 | AGOT | Renames the temporary scope `actor` to `agot_blood_actor` in both hairymen culture-conversion triggers. Any caller with a permanent `actor` scope — every character interaction — made the engine refuse the temporary and log a name collision on each evaluation. |
| P42 | AGOT: Royal Guards | Makes the training-rank comparisons tooltip-safe. `agot_guard_positions_update_training_rank_effect` initialises its two numeric variables at the top, but `set_variable` is a no-op while CK3 builds a tooltip, so the comparisons below still dereferenced an unset variable. Reached from the academy admission option, that produced 50,679 entries — 73% of the run's error log — re-fired every frame the window was open. Each read is now guarded with `has_variable`. |
| P43 | AGOT | Soft-scopes `cp:kingsguard_6` in the Kingsguard `can_reassign` block. A vacant sixth slot made the hard switch fail, and because `can_reassign` is re-evaluated by the council UI it fired continuously — 626 entries in four seconds. |
| P41 | AGOT: Royal Guards | Caps the departure-cleanup event queue. `agot_guard_positions.1007` has five trigger sites; four sit in cleanup effects guarded by `agot_guard_positions_departure_cleanup_complete`, which the rejoin paths clear, so guard-membership churn re-armed the cycle indefinitely. Adds duration flags the rejoin path does not clear: `.1007` at most once per character per 11 days, `.1004` once per liege per 2 days. Bookmark setup and single-appointment call sites are left alone. |

| P45 | DireWolves | Moves the feral-hunt pack-size save inside the author's own `scope:dw_hunt_pack_leader ?=` guard. `random_in_global_list` leaves the leader unset when no living flagged leader is in the chosen county, and the pack-size save was the one of three consecutive statements left outside the guard, so `dw_direwolf_feral_pack_size_value` dereferenced an unset scope three times per evaluation — 3,018 entries in the 8296 Lucerys run. Single-key database override; the rest of `dw_direwolf_decisions.txt` is untouched. |

P23 is unused. Intentional neutralizations are limited to missing Targaryen branches, redundant dragon scheme starts, orphan city event hooks, non-AGOT Grand Remembrance classifications, Persia-only Oathbound branches, unsupported ACS filters, non-installed RICE classifications, ACS religion families absent from AGOT, and the obsolete More Bookmarks faith migrations.

### P33 note on canon sources

AGOT+ references birth effects for Targaryen 98–104 from events `.0882` / `.0883` but never defines them, so each matching pregnancy was terminated and no child was created. Its trigger file also defines `asoiaf_canon_children_Targaryen_99_trigger` twice (Lily and Willow) and never defines `_101_trigger` (Rosey). The rebuilt shims re-key the author's own trigger bodies correctly and add the missing Summer Islander gates, made mutually exclusive with the Westerosi sequence on the mother's heritage.

Names, genders, cultures and house assignment follow AGOT's own canonical history entries for `Targaryen_98`–`Targaryen_104`: Alysanne, Lily, Willow and Rosey by Aegon IV's lowborn Westerosi lover, and Bellenora, Narha and Balerion by his Summer Islander lover. Appearance is copied from those same canon characters, which ship complete DNA in AGOT's `dna_data`, so `has_scripted_appearance` is truthful here.

### P24 / P36 GUI note — unresolved, read before retrying

Both patches target the same defect in two mods: a HUD binding of the form

```
visible = "[And( <cheap checks>, GetScriptedGui('X').IsShown(GuiScope.SetRoot(GetPlayer.MakeScope).End) )]"
```

When `GetPlayer` is invalid the engine hands the scripted GUI a dangling character
(`(no character) weak (Character - 4294967295)`) and rejects it *before* any trigger in
`is_shown` runs, logging `untyped trigger [ Scoped object of type 'character' is not valid ]`
once per frame the binding is evaluated.

Three approaches have been tried and are known **not** to work:

1. **Script-side `exists = this` in `is_shown`.** Grand Remembrance already ships this
   (commit `fdc9265`, predating the failing run) and it has no effect — the scope is
   rejected before the trigger body is entered. Two such guards were added and then
   reverted rather than shipped inert.
2. **Reordering the `And()` arguments so `GetPlayer.IsValid` comes first** (what P36
   currently does). `And()` in CK3 GUI evaluates all of its arguments; it does not
   short-circuit. This is logically identical to the unpatched binding.
3. **Patching more call sites of the same broken guard.** Pointless while the mechanism
   itself does not work.

The remaining untried approach is a **parent-container gate**: an outer widget whose
`visible` is `[GetPlayer.IsValid]` *alone*, with the `IsShown` call moved to a child.
Vanilla uses bare `visible = "[GetPlayer.IsValid]"` as a container gate in `hud.gui`
(lines 36, 42, 994, 1084) and `hud_outliner.gui`, so the idiom is sanctioned — but vanilla
never combines it with a scripted-GUI call (`gui/` has 21 `GetScriptedGui` references and
zero that pass `GetPlayer.MakeScope`), so **there is no static proof that CK3 suppresses
evaluation of a child's `visible` expression under an invisible parent.** That is the one
unknown, and it can only be settled by an in-game observer-mode test, not by reading files.
Do not ship this as a fix until that test has been run.

Note also that `agot_guard_positions_standalone_hud_layout.is_shown` is only
`has_game_rule = agot_guards_roster_button_enabled` — a global check that does not need the
character scope at all. That does not rescue the binding (the scope is rejected before
triggers run), but it means nothing is lost if a future fix passes a different root.

Affected bindings, none currently working:

- `3733779333/gui/guard_academy_button_widget.gui` — outer L14 (overridden by P36), and
  inner buttons at L22, L35, L49 which are un-overridden and carry the same pattern.
- `3678529052/gui/gr_chronicle_window.gui` L13, L19 — overridden by P24.
- `3678529052/gui/scripted_widgets/gr_chronicle_scripted_widgets.txt` L1 — **not overridden.**
- `3678529052/gui/gr_book_event_window.gui` L1020, L1074 — **not overridden.**

### Known-unfixable, deliberately not patched

- **`on_action_namespace.192 has been queued twice with the same data including delay`** —
  37,987 entries in the 8296 Lucerys run, 55% of the log, all in the final 2.5 minutes.
  `on_action_namespace` is a synthetic namespace the engine assigns to delayed on_action
  events at load time; the ordinal 192 is not mappable back to a source on_action from
  script, so the responsible mod cannot be identified statically. **Not currently harmful:**
  the engine *rejects* the duplicate rather than queueing it, which is why the save's pending
  queue stayed healthy (11,728 events across 159 types, top event spread over 2,800
  characters). Worth re-checking if the queue ever starts growing again.
- **Tournament / feast weak-character comparisons** — ~1,100 entries at
  `tournament_events.txt:8609 (tournament_events.1312:trigger)` via `ep2_tournament_on_actions.txt`
  405/470/522, `feast_default_events_joe.txt:70`, and `00_relation_triggers.txt:621`. These are
  vanilla/DLC activity paths comparing against dead participants. Patching would mean whole-file
  overrides of very large vanilla event files with a correspondingly large rebase surface every
  game patch, for errors that resolve as a false trigger rather than a broken outcome.
- Load-time setup-effect dead characters (715), province construction (184), and DNA template
  (164) entries remain assessed as not worth the edit surface.

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
