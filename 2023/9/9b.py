su = 0
for _ in range(200):
    ns = list(map(int,input().split()))
    hist = []
    while len(ns) != 1:
        #su += ns[-1]
        ds = []
        for i in range(len(ns)-1):
            ds.append(ns[i+1]-ns[i])
        hist.append(ns)
        ns=ds
    hist.append(ns)
    print(hist)
    cv = 0
    for l in hist[::-1]:
        cv = l[0] - cv
    su += cv

print(su)
