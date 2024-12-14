def f(pat):
    #print(pat)
    for i,r in enumerate(pat):
        sct = 0
        ri=i
        if i == 0:
            continue

        j = i-1
        while 1:
            if j < 0 or i>=len(pat):
                if sct == 1:
                    return ri
                break
            if pat[i] != pat[j]:
                if sct == 1:
                    break
                for a,b in zip(pat[i],pat[j]):
                    if a!=b:
                        sct+=1
                if sct != 1:
                    break
            i+=1
            j-=1
    return 0
        



#1349 
pats = list(('\n'.join(input() for _ in range(1349))).split('\n\n'))

sp=0
for pat in pats:
    pat = list(pat.split('\n'))
    tpat = [''.join(r[i] for r in pat) for i in range(len(pat[0]))]
    print(sp)
    sp += 100*f(pat)
    print(sp)
    sp += f(tpat)
    print(sp)
    print()
print(sp)
