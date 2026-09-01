# Invisible dragons investigation — final record

Date: 2026-08-31  
Game: CK3 1.19.0.6  
AGOT: 0.5.1 (`2962333032`)

This is the authoritative record of the invisible-dragon investigation. The main README preserves
earlier hypotheses and reversals because they are useful history; when those passages disagree with
this document, this document and the final production section of the README take precedence.

## Final production state

The working production target is the `AGOT Testing` Workshop order with these two mods disabled:

- The Unnecessary Dragons (`3287624076`);
- AGOT Iron and Salt (`3781577713`).

The remaining 79 Workshop mods, including Revive Dead House and CK3 Naval Combat, are enabled. The
rebased `AGOT Unified Compatibility Patch` loads last. The most recent launcher state was exactly
79 Workshop entries plus that local patch (80 enabled entries total), with TUD and Iron absent.

In the latest production run the user could see almost every dragon. Two dragons lacked small
portrait thumbnails but displayed their complete 3D models when opened; that residual issue is
tracked separately below.

## What actually happened

Several independent faults produced the same visible symptom. Treating “shadow but no body” as one
bug caused most of the wasted test launches.

### 1. TUD deterministically breaks the AGOT dragon database path

The Unnecessary Dragons alone, added to the clean common baseline, reproduced the failure. Unbound
alone was clean; TUD plus Unbound failed; TUD alone then failed. The initiating log chain was:

```text
Unexpected token: dragon, near line: 14
invalid accessory group [dragon] for gene gene_dragon
could not find template [dragon]
```

AGOT's `dragon` body group therefore never registers, while `gene_dragon_shadow` remains separate
and valid. This explains the animated dragon-shaped shadow with no body.

TUD targets CK3 1.12 and implements an older artifact-based dragon system. It contains no
`common/genes`, ethnicity, dragon-entity or portrait-accessory override, which is why a search
limited to portrait files did not find it. It does define an artifact slot/database key named
`dragon`. A namespace/key collision is the leading explanation for the parser failure, but the
engine-internal collision mechanism was not directly instrumented; what is proven is TUD's
sufficiency and the exact downstream parser chain.

Resolution: remove TUD. The compatibility patch does not attempt to modernize it.

### 2. The attachment shader independently hides dragon bodies

With TUD and Iron removed, the complete remaining Workshop stack had a clean dragon database path
but dragons were still visually absent when the unified patch was disabled. That run had:

```text
X3013 shader errors                              1526
Failed getting shader for PS_attachment          1526
Unexpected token: dragon                            0
invalid accessory group [dragon]                    0
could not find template [dragon]                     0
```

Battle Graphics' winning `gfx/FX/court_scene.shader` called `ApplyVariationPatterns` with six
arguments while the enabled AGOT Color Picker for Clothes include defines seven. The compile failure
disabled portrait attachments broadly, including dragon bodies; it was not limited to clothes.

A temporary local diagnostic containing only the validated P54 `court_scene.shader` was loaded last
after the same 78 Workshop entries. Dragons rendered, and both X3013 and `PS_attachment` failures
fell to zero. The diagnostic shader was byte-identical to P54 in this compatibility patch:

```text
SHA-256 5A2AB027D2B7F85078E5164BE021D0495BA076B7AFD64A8901D8B06761C9AD9E
```

Resolution: keep P54 in the production patch and load the patch last. P54 requires AGOT Color Picker
for Clothes, Battle Graphics, and Battle Graphics AGOT Compatibility Patch. Those three were **added
to `descriptor.mod` on 2026-08-31** (18 -> 21 dependencies); before that the patch shipped P54
without declaring what it depends on.

Exact arities, verified at the call sites:

```text
Battle Graphics            ApplyVariationPatterns( ... NormalUVChannel )                 6 args
Battle Graphics AGOT Patch ApplyVariationPatterns( ... NormalUVChannel )                 6 args   <- wins without our patch
AGOT Color Picker Clothes  ApplyVariationPatterns( ... NormalUVChannel, PortraitEffect)  7 args
P54 (this patch)           ApplyVariationPatterns( ... NormalUVChannel, PortraitEffect)  7 args   <- wins, matches the include
``` The temporary shader-only diagnostic is not part of production.

### 3. Iron and Salt remains excluded

The minimal AGOT + CK3 Naval Combat control rendered dragons. Adding Iron and Salt produced the
no-dragon visual result. That minimal session's decisive log was later overwritten, so its exact
internal mechanism must not be reconstructed from memory or conflated with TUD's proven parser
signature.

Iron was also the donor for two compatibility-patch GUI merges. Once Iron was removed, those stale
references produced a separate character-window failure. Iron remains outside the production list.
**The rebase is complete**: the patch now holds 92 files and contains zero live Iron-only widgets
(verified: no non-comment `kraken` reference remains in any shipped file).

## Character-window double-panel defect

The first production run after removing TUD and Iron showed two family/relationship layouts drawn
over one another on a dragon character. The log made the cause explicit:

```text
gui/window_character.gui:4121  'agot_kraken_character_view' is not a valid widget/type/property
gui/shared/cooltip.gui:886     'kraken_cooltip_type_living' is not a valid widget/type/property
gui/shared/cooltip.gui:472     'container_kraken_character_tooltip' is not a valid widget/type/property
```

The unified patch still referenced widgets supplied only by Iron. Failure while building the dragon
character window left the ordinary family panel visible beneath the AGOT dragon relationship panel.

The corrective rebase removes `agot_kraken_character_view` and the `kraken_character_window` guard
from `gui/window_character.gui`, while preserving the AGOT, DireWolves and More Personality Depth
merge. The Iron-derived `gui/shared/cooltip.gui` override is removed entirely so More Personality
Depth can win naturally. This correction was made after the pictured run and needs a fresh launch
for runtime confirmation.

## Test sequence and what each run established

| Configuration | Visual result | Useful conclusion |
|---|---|---|
| AGOT + Naval Combat | Dragons visible | Clean minimal control; Naval alone did not cause this dragon symptom. |
| AGOT + Naval Combat + Iron | No dragon body | Iron is sufficient for a separate minimal visual failure; exact overwritten log remains unknown. |
| Broad/full stacks with TUD | No dragon body | Too many simultaneous variables; useful only as reproduction. |
| Bisect A | Dragons visible | Culprit lived in the complementary half. |
| Bisect B / B1 subdivisions | No dragon body until narrowed | Located TUD's candidate branch. |
| TUD + Unbound | No dragon body | Reduced failure to TUD, Unbound, or their interaction. |
| Unbound alone | Dragons visible; parser clean | Cleared Unbound. |
| TUD alone | No dragon body; exact parser chain present | Proved TUD sufficient. |
| Full remaining 78 Workshop mods, no patch | No visible body; dragon parser clean; 1,526 shader failures | Proved the residual image was a different attachment-shader failure, not a third gene culprit. |
| Same 78 plus shader-only P54 diagnostic last | Dragons visible; decisive errors all zero | Proved P54 fixes the residual visual failure without unrelated compatch content. |
| Production 79 Workshop mods plus unified patch | Almost all dragons visible; decisive errors zero | Restored Revive and the rest of the production list; exposed stale Iron GUI references and two unresolved thumbnails. |

## Reliable oracles

Do not rely on screenshots alone. Count these independently after each launch:

```text
Unexpected token: dragon
invalid accessory group [dragon]
could not find template [dragon]
X3013
Failed getting shader for PS_attachment
```

Interpretation:

- the first three indicate the dragon gene/accessory registration path;
- the last two indicate the attachment shader;
- zeroes in all five plus a visible model establish both paths as healthy;
- a visible full model with a missing small thumbnail is a separate portrait-camera/UI problem.

Also verify the actual `dlc_load.json`. Desktop JSON files are import definitions, not proof of what
the launcher really enabled.

## Process lessons

- Start from a known-good minimal configuration and add bounded groups. Removing arbitrary groups
  from a broken full stack gave weaker evidence and consumed seven-minute launches.
- Never call a mod “cleared” from static file absence alone. TUD touched no obvious portrait path
  but was still sufficient to poison registration.
- Keep database, shader, and GUI failures as separate hypotheses even when screenshots look alike.
- Preserve each run's logs before the next launch overwrites them. The lost Iron minimal log is the
  main unresolved evidentiary gap.
- A full compatibility patch is valid only for the dependency set it was built against. For subset
  tests, use a deliberately minimal diagnostic such as the one-file P54 shader patch.
- Graphics-quality, supersampling, and render-scale changes were non-diagnostic here; the failures
  were deterministic content/compiler errors.
- Static collision scans and ck3-tiger are valuable for narrowing and finding stale definitions, but
  they do not replace controlled runtime tests. **ck3-tiger could never have found this one**: the
  cwtools CK3 config ships `config/common/gene/genes.cwt` as a five-line stub with
  `skip_root_key = any` and defines no accessory-gene grammar anywhere in its 98 files. A full
  81-mod Tiger run with `show_loaded_mods = yes` (481,633 lines) reported zero problems in
  `dragon_accessory_genes.txt`. Its silence on gene internals is structural, not a clean bill of
  health.
- When an upstream mod updates, re-run source-hash gates before carrying full-file overrides forward.

## Verification pass (reviewed against both handoffs and the working session, 2026-08-31)

Everything above checks out against the evidence, with these amendments.

### One claim I cannot corroborate

The table's first row — **AGOT + CK3 Naval Combat -> dragons visible** — is not recorded anywhere in
the working session's own history. What is recorded there is AGOT alone (1 mod) and the known-good
11-mod set, both rendering dragons. If that 2-mod control was never actually launched, then the
minimal `AGOT + Naval + Iron` failure implicates **Naval Combat, Iron and Salt, or their interaction**,
and Naval Combat is not excluded. This matters only for the unresolved Iron minimal case; it does not
affect the TUD or shader conclusions.

### Findings from the compatch work not recorded above

- **P59 / stale scripted-effect copies.** The 72-failure signature
  (`agot_historical_dragon_transfer_vars_to_story_cycle_effect failed for unknown arguments`) is
  produced by a *stale full-file copy* of AGOT's `00_agot_dragon_effects.txt` shipped by **AGOT More
  Dragon Eggs** (`3388366564`, not in the playset). Its copy uses 44 `$PARAM$` tokens where AGOT's
  uses 57; the 13 it omits match the 13 named in the error exactly. P59 restores AGOT's definition and
  is byte-identical to it when nothing overrides it. **P59 did not fix the invisible dragons** — the
  full playset had zero such failures even before it existed.
- **Upstream can retire our patches.** AGOT: Royal Guards updated on 2026-08-31 at ~16:12 and the
  author independently implemented all five of our guard fixes (P35, P39, P41, P42, P46), two of them
  more thoroughly than we had. Because this patch loads last, our older merges would have **reverted**
  the author's fixes — including one whose own comment says it prevents locking the persistent reader.
  Those four files were deleted rather than rebuilt. The `source_hashes.sha256` gate is what caught it.
- **The crash archive is the highest-value evidence source on this install.** `crashes/ck3_<ts>/`
  preserves 14 sessions, each with its own `error.log` **and** a `meta.yml` listing every loaded mod.
  That bounded the break window to 42 mods without a single test launch. Caveat: it is not a bisect —
  every broken session was the same large playset.
- **Correlation across a bulk change proves nothing.** Iron and Salt was wrongly convicted on a 14/14
  presence correlation. 42 mods entered the playset in one batch, so all 42 correlated identically.
  This is a distinct failure mode from the "cleared by file absence" error already listed above, and
  it cost more launches than any other single mistake.
- **BOM and CRLF defeat naive greps.** Several AGOT files begin with a UTF-8 BOM, which breaks
  `^pattern` anchors and produced at least one false "this identifier is not defined anywhere"
  conclusion. Read with `utf-8-sig`.

### Compatch state at time of review

```text
files                        92
built_sha256 mismatches       0
upstream sources current     80
upstream drift                0
manifest <-> disk            consistent both directions
descriptor dependencies      21 (P54's three added)
```

## Remaining work

- Confirm the de-krakened character window and restored More Personality Depth cooltip on one fresh
  production launch. No further dragon bisect is required.
- Investigate the two missing small dragon thumbnails separately. Their full models render and all
  decisive gene/shader signatures are zero, so they must not be folded back into the solved invisible-
  dragon incident without new evidence.
- Revalidate Naval Combat's AGOT HUD integration in the final no-Iron stack as part of the broader
  compatch audit.

