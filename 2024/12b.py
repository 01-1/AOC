from collections import defaultdict
import sys

with open(0) as f:
    lines = ['.' * 9999] + ['.' + line.strip() + '.' for line in f.readlines()] + ['.' * 9999]


def adj(i, j): 
    return [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]

def adj5(i, j): 
    return [(i+1, j), (i, j+1), (i-1, j), (i, j-1), (i+1,j)]
vis = set()
su=0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c=='.':
            continue
        if (i, j) in vis:
            continue
        vis.add((i, j))
        d = []
        d.append((i, j))
        perim = 0
        it = []
        while d:
            (x, y) = d.pop()
            it.append((x, y))
            for (z, w) in adj(x, y):
                if lines[z][w] != lines[x][y]:
                    perim += 1
                    continue
                if (z, w) in vis:
                    continue
                vis.add((z,w))
                d.append((z,w))
        assert len(set(it)) == len(it)
        sides = 0
        its = set(it)
        for (x,y) in it:
            l = adj5(x,y)
            for p1, p2 in zip(l[:-1], l[1:]):
                if p1 not in its and p2 not in its:
                    sides += 1
                if p1 in its and p2 in its:
                    (i1, j1), (i2, j2) = p1, p2
                    if (i1 + i2 - x, j1 + j2 - y) not in its:
                        sides += 1

        su += sides * len(it)

print(su)


        

