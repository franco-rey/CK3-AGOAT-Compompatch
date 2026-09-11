"""Drift audit for AGOAT Compompatch.

Re-hashes every SOURCE line in source_hashes.sha256 against the live Workshop directory.
  same     upstream file unchanged since this override was built
  CHANGED  upstream moved -> that override may now be stale; diff it before trusting it
  GONE     upstream no longer ships that path -> override may be orphaned

Run:  python manifest/audit_drift.py   (from the mod root; Workshop dir is auto-detected or set WS)
"""
import io, os, re, sys, hashlib, collections
WS = os.environ.get("CK3_WORKSHOP", r"E:\SteamLibrary\steamapps\workshop\content\1158310")
HERE = os.path.dirname(os.path.abspath(__file__))
ledger = os.path.join(HERE, "source_hashes.sha256")
rows = []
for ln in io.open(ledger, encoding="utf-8", errors="ignore"):
    m = re.match(r"^([0-9a-f]{64})\s+(\d{9,10})/(\S+)", ln)
    if not m: continue
    h, mod, rel = m.groups(); p = os.path.join(WS, mod, *rel.split("/"))
    if not os.path.exists(p): st = "GONE"
    else: st = "same" if hashlib.sha256(io.open(p, "rb").read()).hexdigest() == h else "CHANGED"
    rows.append((st, mod, rel))
def name(mod):
    d = os.path.join(WS, mod, "descriptor.mod")
    if not os.path.exists(d): return mod
    m = re.search(r'^name\s*=\s*"([^"]*)"', io.open(d, encoding="utf-8-sig", errors="ignore").read(), re.M)
    return m.group(1) if m else mod
c = collections.Counter(r[0] for r in rows)
print("gates: %d   same: %d   CHANGED: %d   GONE: %d" % (len(rows), c["same"], c["CHANGED"], c["GONE"]))
by = collections.defaultdict(list)
for st, mod, rel in rows:
    if st != "same": by[(mod, name(mod))].append((st, rel))
for (mod, nm), lst in sorted(by.items(), key=lambda x: -len(x[1])):
    print("\n### %s (%s) - %d moved" % (nm, mod, len(lst)))
    for st, rel in lst: print("   %-7s %s" % (st, rel))
sys.exit(1 if c["CHANGED"] or c["GONE"] else 0)
