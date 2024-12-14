import sys
inp = sys.stdin.readlines()

wfs={}
wah=[]
ctr=0
ac=0

n = False
for l in inp:
    l=l.rstrip()

    if l == '':
        n = True
        break
        #continue

    if n:#l[0] == '{':
        break
        x='x'
        m='m'
        a='a'
        s='s'
        xmas=eval(l.replace('=',':'))
        x=xmas[x]
        m=xmas[m]
        a=xmas[a]
        s=xmas[s]

        wf = 'in'
        while 1:
            for instr in wfs[wf]:
                if ':' in instr:
                    l,r = instr.split(':')
                    if eval(l):
                        wf = r
                        break
                else:
                    wf = instr
                    break

            if wf == 'R' or wf == 'A':
                break

        print(wf)
        if wf=='A':
            for v in xmas.values():
                ac+=v


    else:
        a,b = l.split('{')
        b=b[:-1].split(',')
        wfs[a]=b



def run(inp, lt, gt):
    if inp == 'A':
        ans = 1
        for c in 'xmas':
            if lt[c] - 1 <= gt[c]:
                return 0
            ans *= lt[c] - gt[c] - 1
        wah.append((lt.copy(),gt.copy()))
        return ans
    elif inp == 'R':
        return 0
    ans = 0
    for instr in wfs[inp]:
        if ':' in instr:
            l,r = instr.split(':')
            xmasy, cmp, val = l[0],l[1],int(l[2:])
            if cmp == '<':
                slt = lt[xmasy]
                lt[xmasy] = min(slt,val)
                ans += run(r, lt, gt)
                lt[xmasy] = slt
            else:
                sgt = gt[xmasy]
                gt[xmasy] = max(sgt,val)
                ans += run(r, lt, gt)
                gt[xmasy] = sgt
        else:
            ans += run(instr, lt, gt)
    return ans

    





#print(ac)
zeros,fourkays={},{}
for c in 'xmas':
    zeros[c] =0
    fourkays[c] =4001
ans = (run('in', fourkays, zeros))
print(ans)
print('len=',len(wah))

#2*
#6*
#...n!*

newah = []
for lt,gt in wah:
    nlt,ngt=[],[]
    for c in 'xmas':
        nlt.append(lt[c])
        ngt.append(gt[c])
    newah.append((nlt,ngt))

ewah = list(enumerate(newah))
pie=ewah
n = 1
mul = 1
while pie:
    np = []
    n += 1
    mul *= n
    ans *= n

    for pi,(plt,pgt) in pie:
        for i,(wlt,wgt) in ewah[pi+1:]:
            lt,gt=[],[]
            cans=1
            for (pli,pgi),(wli,wgi) in zip(zip(plt,pgt),zip(wlt,wgt)):
                lt.append(min(pli,wli))
                gt.append(min(pgi,wgi))


            #for c in 'xmas':
                #lt[c] = min(wlt[c],plt[c])
                #gt[c] = max(wgt[c],pgt[c])

            f=True
            #for c in 'xmas':
            for lti, gti in zip(lt,gt):
                if lti + 1<= gti:
                    f=False
                    break
                cans *= lti - gti - 1

            if cans != 0 and f:
                ans += cans
                np.append((pi+1+i,(lt,gt)))
        while (len(np) > ctr):
            print(len(np))
            ctr += 10**6

    print(n)
    print(len(np))
    pie=np



    
        
print(ans)
print(mul)
ans //= mul
print(ans)
