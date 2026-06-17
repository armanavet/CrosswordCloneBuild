import random, time, json
from wordfreq import top_n_list
from english_words import get_english_words_set
WALL=time.time()
DICT={w.upper() for w in get_english_words_set(['web2'],lower=True) if w.isalpha()}
common=[w.upper() for w in top_n_list('en',80000) if w.isalpha() and len(w)>=3]
rank={w:i for i,w in enumerate(common)}
STOP=set(['ISIS','OLEG','BEULAH','GOI','NOY','YOY','ELT','TOA','YEO','NEO','ARA','ENS','SEPTA','TAY','NOY'])
GOOD3={'OAR', 'WAY', 'ORB', 'YEW', 'SOW', 'MOM', 'FOE', 'WON', 'FIN', 'DUO', 'ACE', 'ALL', 'PRY', 'NIL', 'HEM', 'GAS', 'FOX', 'CAT', 'BIN', 'FAT', 'SAG', 'BID', 'RAG', 'RAP', 'FLU', 'POD', 'HEN', 'SUP', 'IMP', 'PIG', 'WIT', 'BIG', 'HUT', 'PAD', 'BOO', 'BED', 'NUT', 'ATE', 'ASK', 'NEW', 'VOW', 'BUN', 'ANT', 'EGG', 'TAX', 'COY', 'HEY', 'NET', 'YAP', 'FOR', 'HIS', 'RAW', 'INK', 'IVY', 'BUS', 'BOX', 'JOB', 'LED', 'OUR', 'MOP', 'PIE', 'HOP', 'NAG', 'RUB', 'USE', 'LOT', 'WAD', 'RIG', 'OFF', 'HAT', 'ELK', 'COP', 'FED', 'ELF', 'WAX', 'YEN', 'FAR', 'FUN', 'COB', 'BAY', 'NOR', 'WOE', 'RIB', 'CRY', 'MAD', 'PEG', 'TIE', 'LAY', 'MAN', 'PUN', 'FRY', 'WEB', 'DUE', 'EAR', 'OWE', 'PEP', 'EAT', 'CUE', 'SIP', 'LOG', 'OAT', 'WOW', 'JOT', 'THE', 'AWE', 'SON', 'RID', 'BUG', 'GEL', 'WAR', 'FIT', 'DIG', 'BOA', 'GAP', 'SEE', 'CAB', 'OFT', 'ASH', 'RYE', 'PAN', 'SIR', 'BOB', 'SAY', 'WED', 'RUM', 'HEW', 'AND', 'DIP', 'ROE', 'MAT', 'SLY', 'SPY', 'ARC', 'NUN', 'RAT', 'SUB', 'GNU', 'WEE', 'FIG', 'TEA', 'HUG', 'NOD', 'OIL', 'SAD', 'COO', 'PEN', 'ART', 'SIT', 'PUG', 'HAS', 'OUT', 'VIA', 'BAG', 'EVE', 'THY', 'YEA', 'TOE', 'FIX', 'CAR', 'PAR', 'KIT', 'JAM', 'DAB', 'SAT', 'BUY', 'CAD', 'MUG', 'JAB', 'INN', 'ICE', 'WRY', 'AXE', 'ION', 'MAP', 'BYE', 'EWE', 'DUB', 'PUT', 'BRA', 'SPA', 'ZOO', 'NIP', 'ELM', 'TOP', 'ADD', 'LID', 'SHE', 'COW', 'WET', 'WHO', 'FAD', 'AID', 'RED', 'TIN', 'CON', 'DAM', 'DID', 'NOT', 'WHY', 'BAD', 'KIN', 'HOW', 'DUG', 'BUD', 'JAY', 'YET', 'BIT', 'AIR', 'FEW', 'ORE', 'LAG', 'GOD', 'KEG', 'ROW', 'AIM', 'SKI', 'RAN', 'OPT', 'MEN', 'BUT', 'BOG', 'DEN', 'HUE', 'POT', 'HUB', 'HIM', 'TAB', 'MAY', 'GUM', 'NAP', 'OWL', 'HOT', 'ROT', 'PUP', 'ICY', 'TON', 'VAT', 'EGO', 'PEA', 'ARK', 'BOW', 'PRO', 'HAM', 'ANY', 'SEA', 'EBB', 'BAT', 'MOB', 'YAM', 'HOE', 'RAM', 'RIP', 'RUG', 'HAG', 'TIC', 'APT', 'BAR', 'BEG', 'ODE', 'MAR', 'EEL', 'PAL', 'PER', 'VAN', 'BIB', 'SOY', 'RUT', 'CUP', 'TAG', 'EYE', 'YES', 'VET', 'GYM', 'GET', 'SUE', 'MIX', 'KID', 'SKY', 'JIG', 'ROD', 'TOO', 'STY', 'SUN', 'CAN', 'COG', 'TRY', 'DIE', 'DRY', 'LET', 'TUG', 'ZAP', 'MUM', 'TAP', 'MOD', 'ARE', 'JAW', 'SIX', 'FAN', 'EON', 'ARM', 'RUN', 'FOG', 'SIN', 'HAY', 'HIT', 'YAK', 'DIN', 'TUB', 'YAW', 'LIE', 'PIT', 'FAX', 'DOT', 'END', 'SAP', 'SHY', 'MET', 'ONE', 'BOY', 'PET', 'SOD', 'SAW', 'ILK', 'IRK', 'SEW', 'JOG', 'DOE', 'AGE', 'RAY', 'SET', 'ERA', 'ODD', 'TAD', 'BAN', 'NOW', 'CUB', 'COT', 'PAY', 'LAP', 'CUT', 'CUR', 'PUB', 'HAD', 'NAB', 'TIP', 'KEY', 'SUM', 'GUN', 'VIE', 'IRE', 'HUM', 'JET', 'TUX', 'PAW', 'GIN', 'WIG', 'AGO', 'LOB', 'ROB', 'HER', 'YOU', 'RIM', 'DAY', 'TAR', 'DIM', 'FUR', 'WAG', 'FEE', 'TOT', 'COD', 'DON', 'WOK', 'WIN', 'GEM', 'WAS', 'TWO', 'GIG', 'ILL', 'OAK', 'LIT', 'URN', 'PIN', 'HID', 'DYE', 'LAB', 'TOY', 'LAW', 'DAD', 'JUG', 'LAD', 'PAT', 'FIR', 'WOO', 'POP', 'BET', 'PEW', 'JAR', 'PLY', 'DOG', 'CAP', 'LOW', 'TOW', 'SOB', 'OWN', 'GUY', 'OLD', 'EMU', 'JOY', 'APE', 'MUD', 'BEE', 'FIB', 'LEG', 'TAN', 'HOG', 'ACT', 'LIP', 'ZIP', 'GUT', 'DEW', 'HIP', 'FLY', 'GOT', 'ALE', 'TEN'}
pool=[w for w in common if w in DICT and w not in STOP and rank[w]<26000 and (len(w)!=3 or w in GOOD3)]
pool+=[w for w in GOOD3 if w not in set(pool)]
rank.update({w:rank.get(w,15000) for w in GOOD3})
N=13
# index: idx[L] = list; pos_idx[(L,pos,ch)] = set(indices into bylen[L])
bylen={}
for w in pool: bylen.setdefault(len(w),[]).append(w)
posidx={}
for L,ws in bylen.items():
    for i,w in enumerate(ws):
        for p,ch in enumerate(w):
            posidx.setdefault((L,p,ch),set()).add(i)
ALL={L:set(range(len(ws))) for L,ws in bylen.items()}

def runs_ok(black):
    for r in range(N):
        c=0
        while c<N:
            if (r,c) in black:c+=1;continue
            s=c
            while c<N and (r,c) not in black:c+=1
            if c-s<3:return False
    for c in range(N):
        r=0
        while r<N:
            if (r,c) in black:r+=1;continue
            s=r
            while r<N and (r,c) not in black:r+=1
            if r-s<3:return False
    return True

def gen_pattern(seed):
    rng=random.Random(seed)
    black=set()
    cells=[(r,c) for r in range(N) for c in range(N) if (r,c)<=(N-1-r,N-1-c)]
    rng.shuffle(cells)
    target=rng.randint(36,44)
    for (r,c) in cells:
        if len(black)>=target:break
        if (r,c)==(N//2,N//2):continue
        pair={(r,c),(N-1-r,N-1-c)}
        if runs_ok(black|pair): black|=pair
    return black if (runs_ok(black) and len(black)>=32) else None

def make_slots(black):
    slots=[]
    for r in range(N):
        c=0
        while c<N:
            if (r,c) in black:c+=1;continue
            s=c
            while c<N and (r,c) not in black:c+=1
            slots.append([(r,cc) for cc in range(s,c)])
    for c in range(N):
        r=0
        while r<N:
            if (r,c) in black:r+=1;continue
            s=r
            while r<N and (r,c) not in black:r+=1
            slots.append([(rr,c) for rr in range(s,r)])
    return slots

def try_fill(black,tlimit):
    slots=make_slots(black)
    L=[len(s) for s in slots]
    cellslots={}
    for i,s in enumerate(slots):
        for cell in s: cellslots.setdefault(cell,[]).append(i)
    assign={}
    sw=[None]*len(slots); used=set()
    start=time.time()
    def cand_idx(si):
        s=slots[si];l=L[si]
        cur=None
        for p,cell in enumerate(s):
            a=assign.get(cell)
            if a is not None:
                st=posidx.get((l,p,a),set())
                cur=st if cur is None else (cur & st)
                if not cur: return []
        if cur is None: cur=ALL[l]
        res=[bylen[l][i] for i in cur if bylen[l][i] not in used]
        res.sort(key=lambda w: rank.get(w,999999))
        return res
    def solve():
        if time.time()-start>tlimit:return False
        unf=[i for i in range(len(slots)) if sw[i] is None]
        if not unf:return True
        best=None;bc=None
        for si in unf:
            c=cand_idx(si)
            if best is None or len(c)<len(bc):
                best=si;bc=c
                if not c:break
        if not bc:return False
        head=bc[:12]; random.shuffle(head); bc=head+bc[12:]
        s=slots[best]
        for w in bc:
            ch=[]
            for k,cell in enumerate(s):
                if cell not in assign:assign[cell]=w[k];ch.append(cell)
            sw[best]=w;used.add(w)
            ok=True
            for cell in s:
                for j in cellslots[cell]:
                    if sw[j] is None and not cand_idx(j):ok=False;break
                if not ok:break
            if ok and solve():return True
            sw[best]=None;used.discard(w)
            for cell in ch:del assign[cell]
        return False
    return (assign,slots) if solve() else (None,None)

random.seed(2024)
for seed in range(0,20000):
    if time.time()-WALL>40: print("TIMEOUT");break
    b=gen_pattern(seed)
    if not b:continue
    res,slots=try_fill(b,3.0)
    if res:
        out=[[('#' if (r,c) in b else res[(r,c)]) for c in range(N)] for r in range(N)]
        print("SOLVED seed",seed,"blacks",len(b))
        for row in out:print(''.join(row))
        json.dump({"N":N,"black":sorted(map(list,b)),"grid":[''.join(r) for r in out]},open('grid.json','w'))
        break
