#!/usr/bin/env python3
"""Enable/disable mods in the active playset across all three stores.

    python3 tools/toggle_mods.py off 3469933841 3541596590
    python3 tools/toggle_mods.py on  3469933841
    python3 tools/toggle_mods.py list

Updates launcher-v2.sqlite, dlc_load.json and mod/AGOAT.json together so the
launcher, the game and the exported playset never disagree. Used for bisecting.
"""
import sqlite3, json, os, sys, datetime

D = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DB = os.path.join(D, "launcher-v2.sqlite")

def active_playset(cur):
    r = cur.execute("select id,name from playsets where isActive=1").fetchone()
    if not r: sys.exit("no active playset")
    return r

def sync(cur, ps):
    rows = cur.execute("""select pm.position,pm.enabled,m.steamId,m.displayName
                          from playsets_mods pm join mods m on m.id=pm.modId
                          where pm.playsetId=? order by pm.position""", (ps,)).fetchall()
    p = os.path.join(D, "dlc_load.json"); d = json.load(open(p))
    d["enabled_mods"] = ["mod/ugc_%s.mod" % r[2] if r[2] else "mod/agot_unified_compat.mod"
                         for r in rows if r[1]]
    json.dump(d, open(p, "w"), indent=2)
    p = os.path.join(D, "mod", "AGOAT.json")
    if os.path.exists(p):
        a = json.load(open(p))
        byid = {m.get("steamId"): m for m in a["mods"] if m.get("steamId")}
        loc = [m for m in a["mods"] if not m.get("steamId")]
        out = []
        for r in rows:
            if r[2] and byid.get(r[2]): e = dict(byid[r[2]])
            elif not r[2] and loc:      e = dict(loc[0])
            else:                        e = {"displayName": r[3], "steamId": r[2]}
            e["enabled"] = bool(r[1]); e["position"] = r[0]; out.append(e)
        a["mods"] = out; json.dump(a, open(p, "w"), indent=1)
    missing = [m for m in d["enabled_mods"] if not os.path.exists(os.path.join(D, m))]
    return len(d["enabled_mods"]), missing, rows

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    action = sys.argv[1]
    con = sqlite3.connect(DB); cur = con.cursor()
    ps, name = active_playset(cur)
    if action == "list":
        _, _, rows = sync(cur, ps)
        for r in rows:
            print("  %-4d %-3s %-12s %s" % (r[0]+1, "ON" if r[1] else "off", r[2] or "LOCAL", r[3]))
        return
    val = 1 if action == "on" else 0
    for sid in sys.argv[2:]:
        row = cur.execute("select id,displayName from mods where steamId=?", (sid,)).fetchone()
        if not row: print("  ?? unknown steamId", sid); continue
        cur.execute("update playsets_mods set enabled=? where playsetId=? and modId=?", (val, ps, row[0]))
        print("  %-3s %-12s %s" % (action, sid, row[1]))
    cur.execute("update playsets set updatedOn=? where id=?",
                (datetime.datetime.utcnow().isoformat()+"Z", ps))
    con.commit()
    n, missing, _ = sync(cur, ps)
    print("playset '%s': %d enabled | missing pointers: %s" % (name, n, missing or "none"))
    con.close()

main()
