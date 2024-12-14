n=140
#zn=10
g = [input() for _ in range(n)]

ij = []
for i, r in enumerate(g):
    for j, c in enumerate(r):
        if c == '#':
            ij.append((i,j))

d = 0
for aij in ij:
    for bij in ij:
        ai, aj = aij
        bi, bj = bij
        d += abs(ai-bi) + abs(aj-bj)

d1=d

gprime = []
all = '.'*n
for r in g:
    if r == all:
        gprime.append(r)
    gprime.append(r)

print(gprime)
nn = len(gprime)
g = [''.join(x[i] for x in gprime) for i in range(n)]
    
gprime = []
all = '.'*nn
for r in g:
    if r == all:
        gprime.append(r)
    gprime.append(r)


print(gprime)
ij = []
for i, r in enumerate(gprime):
    for j, c in enumerate(r):
        if c == '#':
            ij.append((i,j))

d = 0
for aij in ij:
    for bij in ij:
        ai, aj = aij
        bi, bj = bij
        d += abs(ai-bi) + abs(aj-bj)

#print(((d - d1) * 1 + d1)//2)
#print(((d - d1) * 9 + d1)//2)
#print(((d - d1) * 100 + d1)//2)
#print(((d - d1) * 10**6 + d1))
print(((d - d1) * (10**6-1) + d1)//2)
