import random, sys, time, json
WALL=time.time()
from wordfreq import top_n_list
from english_words import get_english_words_set

DICT = {w.upper() for w in get_english_words_set(['web2'], lower=True) if w.isalpha()}
common = [w.upper() for w in top_n_list('en', 60000) if w.isalpha() and len(w)>=3]
pool = [w for w in common if w in DICT]
N=13

def runs_ok(black):
    # all across/down runs length>=3
    for r in range(N):
        c=0
        while c<N:
            if (r,c) in black: c+=1; continue
            s=c
            while c<N and (r,c) not in black: c+=1
            if c-s<3: return False
    for c in range(N):
        r=0
        while r<N:
            if (r,c) in black: r+=1; continue
            s=r
            while r<N and (r,c) not in black: r+=1
            if r-s<3: return False
    return True

def gen_pattern(seed):
    rng=random.Random(seed)
    black=set()
    cells=[(r,c) for r in range(N) for c in range(N) if (r,c)<=(N-1-r,N-1-c)]
    rng.shuffle(cells)
    target=rng.randint(30,38)
    for (r,c) in cells:
        if len(black)>=target: break
        if (r,c)==(N//2,N//2): continue
        pair={(r,c),(N-1-r,N-1-c)}
        nb=black|pair
        if runs_ok(nb):
            black=nb
    if runs_ok(black) and len(black)>=28:
        return black
    return None

def make_slots(black):
    slots=[]
    for r in range(N):
        c=0
        while c<N:
            if (r,c) in black: c+=1; continue
            s=c
            while c<N and (r,c) not in black: c+=1
            slots.append([(r,cc) for cc in range(s,c)])
    for c in range(N):
        r=0
        while r<N:
            if (r,c) in black: r+=1; continue
            s=r
            while r<N and (r,c) not in black: r+=1
            slots.append([(rr,c) for rr in range(s,r)])
    return slots

bylen={}
for w in pool: bylen.setdefault(len(w),[]).append(w)

def try_fill(black, tlimit):
    slots=make_slots(black)
    cell_slots={}
    for i,s in enumerate(slots):
        for cell in s: cell_slots.setdefault(cell,[]).append(i)
    assign={}; slot_words=[None]*len(slots); used=set()
    start=time.time()
    def candidates(si):
        s=slots[si];L=len(s);res=[]
        for w in bylen.get(L,[]):
            if w in used: continue
            ok=True
            for k,cell in enumerate(s):
                a=assign.get(cell)
                if a is not None and a!=w[k]: ok=False;break
            if ok: res.append(w)
        return res
    def solve():
        if time.time()-start>tlimit: return False
        unf=[i for i in range(len(slots)) if slot_words[i] is None]
        if not unf: return True
        best=None;bestc=None
        for si in unf:
            c=candidates(si)
            if best is None or len(c)<len(bestc):
                best=si;bestc=c
                if not c: break
        if not bestc: return False
        cands=bestc[:]; random.shuffle(cands)
        s=slots[best]
        for w in cands:
            changed=[]
            for k,cell in enumerate(s):
                if cell not in assign: assign[cell]=w[k]; changed.append(cell)
            slot_words[best]=w; used.add(w)
            ok=True
            for cell in s:
                for j in cell_slots[cell]:
                    if slot_words[j] is None and not candidates(j): ok=False;break
                if not ok: break
            if ok and solve(): return True
            slot_words[best]=None; used.discard(w)
            for cell in changed: del assign[cell]
        return False
    if solve():
        return assign, slots
    return None,None

random.seed(123)
done=False
for seed in range(0,5000):
    if time.time()-WALL>38: print("timeout no full solve"); break
    b=gen_pattern(seed)
    if not b: continue
    nslots=len(make_slots(b))
    res,slots=try_fill(b, 2.5)
    if res:
        out=[[('#' if (r,c) in b else res[(r,c)]) for c in range(N)] for r in range(N)]
        print("SOLVED seed",seed,"blacks",len(b),"slots",len(slots))
        for row in out: print(''.join(row))
        json.dump({"N":N,"black":sorted(map(list,b)),"grid":[''.join(r) for r in out]}, open('grid.json','w'))
        done=True; break
if not done: print("none")
