su = 0
for _ in range(200):
    ns = list(map(int,input().split()))
    while len(ns) != 1:
        su += ns[-1]
        ds = []
        for i in range(len(ns)-1):
            ds.append(ns[i+1]-ns[i])
        ns=ds
    su += ns[-1]
print(su)
