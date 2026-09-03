#!/usr/bin/env python3
"""Regenerate MODULES.md from manifest/build_manifest.json.

MODULES.md is the human-readable map of what this layer patches and why. It is
derived, never hand-edited. Run after adding or changing any module:
    python3 tools/gen_module_index.py
"""
import json, os, collections, datetime, sys

UP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARADOX = os.path.abspath(os.path.join(UP, "..", ".."))

m = json.load(open(os.path.join(UP, "manifest/build_manifest.json"), encoding="utf-8"))
files = m["files"]

pos = {}
dlc = os.path.join(PARADOX, "dlc_load.json")
if os.path.exists(dlc):
    for i, e in enumerate(json.load(open(dlc))["enabled_mods"]):
        b = os.path.basename(e)
        if b.startswith("ugc_"):
            pos[b[4:-4]] = i + 1

byprov = collections.defaultdict(list)
for f in files:
    byprov[f.get("provider_name") or "(authored here)"].append(f)

def order_key(p):
    w = byprov[p][0].get("provider_workshop_id")
    return (pos.get(str(w), 9999), p)

L = ["# Module index", "",
     "Generated from `manifest/build_manifest.json` on %s." % datetime.date.today(),
     "Derived file - do not hand-edit. Regenerate with `python3 tools/gen_module_index.py`.", "",
     "%d files across %d upstream mods. **override** replaces an upstream virtual path;" % (
         len(files), len([k for k in byprov if k != "(authored here)"])),
     "**authored** is a new file this layer introduces.", "",
     "This layer must load **last**; every override below only wins because of that.", "",
     "| Playset # | Upstream mod | Files | Modules |", "|---:|---|---:|---|"]
for p in sorted(byprov, key=order_key):
    fs = byprov[p]
    w = fs[0].get("provider_workshop_id")
    mods = sorted({f["module"] for f in fs if f.get("module")})
    L.append("| %s | %s | %d | %s |" % (pos.get(str(w), "—"), p, len(fs), ", ".join(mods) or "—"))

L += ["", "## Files by upstream mod", ""]
for p in sorted(byprov, key=order_key):
    fs = byprov[p]
    w = fs[0].get("provider_workshop_id")
    ppos = pos.get(str(w))
    hdr = "### %s" % p
    if w:
        hdr += "  (`%s`, %s)" % (w, "playset #%d" % ppos if ppos else "**not in playset**")
    L += [hdr, ""]
    for f in sorted(fs, key=lambda x: x["virtual_path"]):
        mod = f.get("module") or ", ".join(f.get("transformations") or []) or "—"
        L.append("- `%s` — **%s** (%s)" % (f["virtual_path"], mod, f["kind"]))
        for r in (f.get("rationale") or [])[:1]:
            L.append("  - %s" % (r[:220] + ("…" if len(r) > 220 else "")))
    L.append("")

dormant = [f for f in files
           if f.get("provider_workshop_id") and str(f["provider_workshop_id"]) not in pos]
if dormant:
    L += ["## Dormant — upstream not currently in the playset", "",
          "Inert until their target mod is enabled. Each was verified harmless while absent.", ""]
    for f in sorted(dormant, key=lambda x: x["virtual_path"]):
        L.append("- `%s` — **%s**, targets `%s` (%s)" % (
            f["virtual_path"], f.get("module") or "—", f["provider_workshop_id"],
            f.get("provider_name") or "unknown"))
    L.append("")

open(os.path.join(UP, "MODULES.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("MODULES.md: %d lines, %d files, %d dormant" % (len(L), len(files), len(dormant)))
