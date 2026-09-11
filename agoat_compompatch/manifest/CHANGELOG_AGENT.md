# AGOAT Compompatch - agent changelog

Internal notes for whoever maintains this patch (moved out of the public README, which is not ours to edit).
The provenance ledger is `source_hashes.sha256` / `build_manifest.json`; run `python manifest/audit_drift.py`.

### 2026-09-11 — erasure sweep + NoW/LoV rebase (v1.1.2, second pass)

Because this patch loads last, every full-file copy it ships silently erases whatever later mods
changed in that file. A normalised erasure scan (trailing comments and whitespace stripped, every
compatch file set-compared against every enabled mod shipping the same path, each lost line checked
against current vanilla) found the real losses below; the rest were AGOT's own vanilla omissions,
our deliberate patch deltas, or comment noise.

**Engine fact that drove the biggest fix:** CK3 loads a directory's subfolders after its top-level
files, so `map_data/geographical_regions/replace/…` beats every `zz_` file. Our stale full copy of
Nobility of Westeros' region file (pre-09-10) therefore re-imposed AGOT's original
`graphical_mena`/`graphical_mediterranean` over the LoV compatch's versions — that was the
**1,648 `has no visual geographical region` errors** (all of LoV's Essos plus NoW's Neck). A region
resolver reproduces 1,648 with our old file loaded last and 14 (an upstream LoV gap at Asshai) with
NoW's current file.

| File(s) | What was wrong | Fix |
|---|---|---|
| `map_data/geographical_regions/replace/00_agot_geographical_region.txt` | stale pre-09-10 NoW full copy (see above) | NoW's current 73-key delta verbatim |
| `map_data/definition.csv`, `island_region.txt`, six `gfx/map/map_object_data/*_locators.txt` | built on NoW before its 09-05/09-10 updates; `special_building` header still `clamp_to_water_level=no` | rebuilt: LoV compatch base (all 10,451/11,295 ids) + NoW's changed ids by id + COW-NoW's COW-specific scales on the two files it ships; NoW's 163 barony renames applied |
| `history/titles/agot_e_the_{north,crownlands,riverlands,vale,westerlands}.txt` | NoW rewrote all five on 09-10; our copies carried its old layout | NoW current + AGOT-canon blocks NoW still drops (`b_kings_mountain`, `b_tristonkeep`, `b_goldengate`, `b_lanns_hall`, five Northern baronies, …) + Stark_155/156 (Benjen, Rodwell) holder entries in the six Winterfell titles |
| `history/characters/zz_agoat_agot_0521_characters_hidden_by_now.txt` | NoW's 09-10 update re-added 17 of the 20 characters we restored → duplicate definitions | trimmed to the three still missing (`Hardy_83`, `Cave_92`, `Cave_93`). NoW itself references an undefined `Blackwater_6` — upstream bug, left alone |
| `events/agot_events/agot_kingsguard_events.txt` | erased the LoV compatch's changes (religion-based checks, `cp:` slot guards, relation-trigger guards) | LoV compatch current + our 24 `scope:kingsguard_candidate ?=` guards + recruit-option `exists` wrapper |
| `common/scripted_effects/asoiaf_setup_effects.txt` (P02) | fork of pre-09-09 AGOT+ | AGOT+ current + the script errors its rewrite introduced, all confirmed by ck3-tiger against the live playset: `has_claim =` → `has_claim_on =` ×15, bare `asoiaf_underaged ?=` → `scope:asoiaf_underaged ?=` ×107, `is_dead = yes` → `is_alive = no` ×2, seven bare `exists = character:X` lines written in effect context wrapped into proper `if/limit` guards, `faith:rhllor` (no such faith in 0.5.2.1) → `faith:rhllor_fc` ×5. `asoiaf_destroy_crownlands_title_effect` (still called by `test_title_on_actions.txt`, definition dropped upstream) moved to additive `zzzzzz_agoat_p02_crownlands_effect.txt` |
| `common/scripted_effects/asoiaf_canon_children_effects.txt` (P01) | fork of pre-09-09 AGOT+ | AGOT+ current (dragon-bond schemes adopted) + its 09-09 errors repaired: `employer = scope:mother.employer` dropped from 202 `create_character` blocks that already set `location` (exactly one is allowed, and the scope is empty for ruler mothers) with our courtier placement restored instead; `start_scheme … target =` → `target_character =` ×24; `every_dynasty_member` inside triggers → `any_dynasty_member` ×6; `trait = beauty_good_3` outside `create_character` → `add_trait`; `any_spouse.house ?=` → `any_spouse = { house ?= }`; `nick_the_imp` → `nick_agot_historical_the_imp`; `exists` guards around parent-scope house/faith/culture sets |
| `gui/window_character.gui` | erased AGOT Dragon Wives (Valyrian multi-wife rows) and In My Humble Opinion's two hooks | Dragon Wives' four real hunks applied (its stale `agot_fake_death_character_view` hunk skipped); IMHO liege-opinion blockoverride + `IMHO_player_personality_enabled` (game rule, default on) on `ai_personality` |
| `gui/hud.gui` | erased More Dragon Eggs' HUD dragon portrait | `bottom_left_dragon_portrait` type + instance inserted |
| `gui/shared/portraits.gui` | IMHO's opinion-badge types are CK3 1.15 copies of AGOT's `portrait_opinion` types | IMHO's `block "IMHO_player_opinion"` added to both AGOT types (dragon-hidden) |
| `gui/map_icon_layer.gui` | missed the LoV compatch's one deliberate removal | `GetDecisionWithKey('find_elder_interaction')` datacontext removed (it is an interaction, not a decision) |
| `common/governments/replace/00_agot_government_types.txt` | full 16-key copy re-declaring AGOT's `first_ranger_government` and missing NoW's `valid_holdings` | deleted — NoW's current replace file is a one-key `command_government` delta and loads last on its own |
| **new** `common/character_interactions/zzzzzz_wlbol_baie_agot_education_merge.txt` | Ward Limit (loads later) overrode Better AI Education – AGoT's five education interactions, erasing its AI guardian scoring and AGOT's education changes | BAE-AGoT's file with Ward Limit's rule (`num_of_relation_ward < 2` → `< wlbol_ward_limit`, 21 spots); BAE-AGoT's own `has_focus != education_learning` (a simple-assign trigger, logged every AI pass) rewritten as `NOT = { has_focus = … }` |
| **new** `gui/00_player_opinion_portraits.gui` | CK3 keeps the *first* registered GUI type, and Show Player Opinion's `00_` file registers `portrait_opinion` before AGOT's `shared/portraits.gui`, so AGOT's dragon guards (and the IMHO block added to `shared/portraits.gui`, now inert) never applied: dragon portraits carried opinion boxes | SPO's file verbatim + AGOT's `Not(IsCharacterDragon)` guards on both types. SPO supersedes IMHO's opinion badge (same information); IMHO's PoV button, personality rule and liege hook stay live |
| **new** `common/traits/zzzzzz_petty_mayham_traits_merge.txt` | Petty Inheritable Traits overrode Mayham's harsher versions of seven congenital traits | Mayham's blocks + Petty's `opposites` (the only thing Petty changes) |

**Checked and left alone:** Naval Combat / CoA Rally Points / War Panel Allies Fix / Duel Overlay /
Better Barbershop / Show Player Opinion "losses" are vanilla lines AGOT itself omits or adaptations
already made (`AGOTGetNameNoTooltip`); Local Artisan's two AI-weight tweaks are already applied;
Hiraeth's dropped lines reference vanilla heritages/struggles that do not exist in AGOT; Legacy of
the Dragon's `vs_*_template` references are defined nowhere (Valyrian Steel ships no templates), so
the `valyrian_steel_template` substitution stands; MPD's `paranoid` XP lines stay removed (P07 —
multi-track trait); Knights & Banners (AoW) is icons only; Armies of Westeros vs REMASTERED differ by
one icon line. Grand Remembrance, ACS, Expanded Court Position, Oathbound, Crowns and the other
AGOT+ files keep their long-standing deliberate deltas (verified identical to the original
`agot_unified_compat` versions, comments stripped).

Ledger rebuilt: 159 files, 130 hash-gated (the new merge files are gated to the files they were
built from), 29 additive; `python manifest/audit_drift.py` → 130 same, 0 changed. The Workshop copy
(3795793975, built Sep 6) does not contain any of this and needs re-upload.

**Verified in-game (2026-09-11, observer run with the local build loaded):** X3013 shader errors
1,561 → 0, `has no visual geographical region` 1,648 → 0, dragon-transfer compile failures 72 → 0,
government-modifier errors → 0, `find_elder` decision errors → 0, canon-children `create_character`
failures 202 → 0 (the four left are vanilla Temujin spawns and Revive Dead House). Non-noise error
lines vs the Sep 8 session: 43,293 → 28,889. No error names any rebuilt history, map or GUI file.
The ~70K `Character - 4294967295` lines are Naval Combat / Royal Guards script values evaluated with
no player in observer mode, unchanged in kind from before.

**Local testing on the PC:** the game keys installed mods by *name*. While the Workshop copy is
subscribed, both `.mod` files are "AGOAT Compompatch" and the game keeps the Workshop entry (even
when disabled), so the local folder never loads. Unsubscribe from 3795793975 to test locally;
re-subscribe when you want the published build back. The launcher regenerates the top-level pointer
from `descriptor.mod` on every start, so the pointer cannot be edited around this.

### 2026-09-11 — upstream drift rebase (v1.1.2)

Audit of every override against current Workshop content, using the provenance ledger recovered from
git (`6fed5e2`, Sep 3 — the last commit before `manifest/` was deleted). 110 upstream gates checked:
93 unchanged, 16 changed, 1 moved. The Sep 4/6 rebase (v1.1.1) had already caught 12 of the 16;
upstream then moved **again** after Sep 6 in four files.

**Rebased now (all verified before writing):**

| File | Upstream | What changed | Verification |
|---|---|---|---|
| `gui/window_character.gui` (P03) | AGOT 0.5.2.1 + DireWolves 09-11 | Old copy was built on pre-0.5.2.1 AGOT and **dropped six 0.5.2.1 widgets** (`liege_portrait`, `char_view_house_area`, `character_relation_to_you`, `other_player_name`, `ai_personality`, `char_view_titles`) plus 3 MPD bindings — a visible character-window regression. Rebuilt as a three-way merge on the current AGOT base. | all 6 widgets + both DireWolves views + `IsCharacterDirewolf` guard + `mpd_view_hook` present; brace 0; no kraken refs. One MPD hunk deliberately dropped: it re-inserted `agot_fake_death_character_view`, a template AGOT 0.5.2.1 removed — re-adding a dangling reference is the exact bug that broke this window before. |
| `common/scripted_effects/asoiaf_scripted_effects_strong_seed.txt` (P51) | AGOT+ 09-10 | Never rebased; 15 upstream lines missing. Rebuilt as upstream verbatim + P51's soft-scope guards. Upstream now defines all but **one** of the dynasties P51 originally neutralised (`dynn_Aranys` remains missing). | keys 2=2, brace 0, 6 refs softened |
| `common/scripted_effects/zzz_agot_dragon_transfer_vars_fix.txt` (P59) | AGOT 0.5.2.1 | Comment-only drift (params 57=57, logic identical). Refreshed verbatim so the gate stays honest. | block byte-identical to AGOT, comments included |

**Deliberately NOT rebased — need their own pass:**

- `common/scripted_effects/asoiaf_setup_effects.txt` (P02) and `asoiaf_canon_children_effects.txt`
  (P01) — AGOT+ rewrote ~1,200 lines of each on 09-09, **and our own delta is 1,085 / 836 lines**.
  That is two divergent thousand-line edits to an 11,000-line file: a merge with judgment calls, not
  a rebase. Until done, our copies (loading last) revert AGOT+'s 09-09 changes to those files.

**Still correct, no action:** P64 `is_human` (DireWolves moved its trigger to an additive
`dw_direwolf_character_triggers.txt`; Great Councils still drops the direwolf line, so the merge is
still needed); all MIV overrides (their "missing" upstream lines are P08's intentional removals,
pickaxe-verified to Aug 30); House Founders and MIV decisions (1-2 lines).

**Provenance was lost and has been restored.** The v1.0.0/v1.1.1 rewrite stripped every patch header
(0 of 155 files carried one) and deleted `manifest/`. `manifest/source_hashes.sha256` and
`build_manifest.json` are rebuilt from current upstream: 156 files, 127 hash-gated, 29 additive.
Re-run the audit any time with `python manifest/audit_drift.py` — a changed SOURCE hash means
upstream moved and that override may be stale. This is how the Royal Guards supersession was caught;
without it, none of the above is detectable.

**Load order:** unchanged. Two duplicate pairs remain enabled by choice — both Knights & Banners
variants (187 shared files) and both Armies of Westeros.
