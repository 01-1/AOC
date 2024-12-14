import sys
inp = sys.stdin.readlines()

wfs={}
ac=0

n = False
for l in inp:
    l=l.rstrip()

    if l == '':
        n = True
        continue

    if n:#l[0] == '{':
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






print(ac)
