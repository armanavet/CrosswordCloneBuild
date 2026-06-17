import re
s=open('fill2.py').read()
# rank by frequency
s=s.replace(
"pool=[w for w in common if w in DICT]",
"rank={w:i for i,w in enumerate(common)}\n"
"STOP=set(['ISIS','OLEG','BEULAH','GOI','NOY','YOY','ELT','TOA','YEO','NEO','ARA','ENS','SEPTA','TAY','NOY'])\n"
"pool=[w for w in common if w in DICT and w not in STOP and rank[w]<30000]")
# candidate returns sorted by rank
s=s.replace(
"        if cur is None: cur=ALL[l]\n        return [bylen[l][i] for i in cur if bylen[l][i] not in used]",
"        if cur is None: cur=ALL[l]\n        res=[bylen[l][i] for i in cur if bylen[l][i] not in used]\n        res.sort(key=lambda w: rank.get(w,999999))\n        return res")
# in solve, try most-common-first with mild randomness instead of full shuffle
s=s.replace(
"        random.shuffle(bc)\n        s=slots[best]",
"        head=bc[:12]; random.shuffle(head); bc=head+bc[12:]\n        s=slots[best]")
open('fill2.py','w').write(s)
print("patched")
