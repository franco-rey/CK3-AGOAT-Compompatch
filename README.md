# Crusader Kings 3 (v1.19) - AGOT
### A Greatest of All Time Compilation + Compatibility Patch

#### Installation Instructions
1. Subscribe to the mod collection [here](https://steamcommunity.com/sharedfiles/filedetails/?id=3795029485).
2. Ensure that you import the .json of the playset load order [here](https://github.com/franco-rey/CK3-AGOAT-Compompatch/blob/main/agoat_compompatch/AGOAT.json).

---
- Check out the full modlist and author credits [here](https://github.com/franco-rey/CK3-AGOAT-Compompatch/blob/main/agoat_compompatch/credits.md).
- All mods in the collection remain required dependencies, and explicit permission was obtained wherever an author's terms ask for it.

## Changelog

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
