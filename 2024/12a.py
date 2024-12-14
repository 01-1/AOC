from collections import defaultdict
import sys

with open(0) as f:
    lines = ['.' * 9999] + ['.' + line.strip() + '.' for line in f.readlines()] + ['.' * 9999]


def adj(i, j): 
    return [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]

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
        su += perim * len(it)

print(su)


        

