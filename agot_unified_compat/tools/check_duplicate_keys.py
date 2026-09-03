#!/usr/bin/env python3
"""Detect duplicate database keys inside this patch.

Why this exists
---------------
This mod was consolidated from six separate local patches. While they were
separate mods, two files defining the same key were resolved by MOD load order,
which was deliberate and tested. Once merged into one mod the contest moved
inside a single directory, where CK3 resolves duplicates by FILENAME order --
an accident of alphabetisation that silently flipped four scripted effects
(see P65 in common/scripted_effects/interactive_scripted_effects.txt).

The consolidation check verified that no later mod claimed a shared virtual
PATH. It did not check for duplicate KEYS inside the merged mod. This does.

Run before every commit that adds or merges a file:
    python3 tools/check_duplicate_keys.py
Exit code 1 means a duplicate needs a deliberate decision.

Note on on_action: entries with the same key MERGE rather than override, so
common/on_action is reported separately as informational, never as a failure.
"""
import os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_.]*)\s*=\s*\{', re.M)

# Directories where a later definition REPLACES an earlier one.
OVERRIDE_DIRS = [
    "common/scripted_effects", "common/scripted_triggers", "common/decisions",
    "common/character_interactions", "common/modifiers", "common/script_values",
    "common/scripted_modifiers", "common/factions", "common/casus_belli_types",
    "common/buildings", "common/court_positions/types", "common/council_positions",
    "common/scripted_guis", "common/story_cycles", "common/scripted_character_templates",
    "common/customizable_localization", "common/artifacts/templates",
    "common/domiciles/buildings", "common/modifier_definition_formats",
    "common/traits", "common/genes", "common/game_rules", "common/on_action/relations",
]
# Directories where same-key entries MERGE. Informational only.
MERGE_DIRS = ["common/on_action"]


def scan(rel):
    d = os.path.join(ROOT, rel)
    if not os.path.isdir(d):
        return {}
    km = collections.defaultdict(list)
    for f in sorted(os.listdir(d)):
        if not f.endswith(".txt"):
            continue
        with open(os.path.join(d, f), encoding="utf-8-sig", errors="replace") as fh:
            for k in set(KEY.findall(fh.read())):
                km[k].append(f)
    return {k: v for k, v in km.items() if len(v) > 1}


def main():
    failures = 0
    for rel in OVERRIDE_DIRS:
        for k, files in sorted(scan(rel).items()):
            print("DUPLICATE  %s/%s" % (rel, k))
            print("           defined in: %s" % ", ".join(files))
            print("           CK3 keeps:  %s  (last filename alphabetically)" % sorted(files)[-1])
            failures += 1
    for rel in MERGE_DIRS:
        for k, files in sorted(scan(rel).items()):
            print("merge-ok   %s/%s  in %s" % (rel, k, ", ".join(files)))
    if failures:
        print("\n%d duplicate key(s) with override semantics." % failures)
        print("Resolve each deliberately -- delete the losing definition and say why.")
        print("Do NOT rely on filename ordering; overriding files must keep their")
        print("upstream names to override at all, so renaming is not an option.")
        return 1
    print("\nNo duplicate keys with override semantics.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
