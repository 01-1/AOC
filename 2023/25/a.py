import sys
inp = sys.stdin.read().splitlines()
en = enumerate

#adj = {}
rev = {}
adj = [[] for _ in range(1539)]

revi = 0

for l in inp:
    a, b = l.split(': ')
    b = b.split()

    if a not in rev:
        rev[a] = revi
        revi += 1

    x = rev[a]
    for bi in b:

        if bi not in rev:
            rev[bi] = revi
            revi += 1

        y = rev[bi]
        adj[x].append(x)
        adj[y].append(y)
        

print(adj)
print(len(adj))

#for a,c in adj.items():
    #pass
    #print(c)
