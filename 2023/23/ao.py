import heapq

import sys
inp = sys.stdin.read().splitlines()
en=enumerate


sys.setrecursionlimit(100000)

#d='<^>v' # complement
dch = '>v<^'
dir=[(0,1),(1,0),(0,-1),(-1,0)]

adj = {}

pq = []
heapq.heappush(pq, (0,0,1,-1,1))
#adj[(0,1)] = 0
step = set()


#for i,l in en(inp):
    #for j,c in en(l):


#vis = set()

def dfs(dist, i, j, li, lj):
    if adj[(i,j,li,lj)] > dist + 1000:
        return

    if i == 140 and j == 139:
        print(dist)
        return

    step.add((i, j))
    dist += 1

    while 1:
        if 1 or inp[i][j] == '.':
            for di, dj in dir:
                di += i
                dj += j
                if (di, dj) in step:
                    continue
                if inp[di][dj] == '#':
                    continue
                ma = max(adj.get((di,dj,i,j), 0), dist)
                adj[(di,dj,i,j)] = ma
                if ma <= dist + 1000:
                    dfs(dist, di, dj,i,j)

        else:
            di, dj = dir[dch.index(inp[i][j])]
            di += i
            dj += j
            if (di, dj) in step:
                continue
            if inp[di][dj] == '#':
                continue
            ma = max(adj.get((di,dj,i,j), 0), dist)
            adj[(di,dj,i,j)] = ma
            if ma <= dist + 1000:
                dfs(dist, di, dj,i,j)
        break


    step.remove((i,j))


    



#dfs(0, 0, 1)
#adj[(1,1,0,1)] = 1
adj[(1,1)] = 1
dfs(1, 1, 1,0,1)

while 0:
    dist, i, j, li, lj = heapq.heappop(pq)
    print(dist,i,j,li,lj)

    if i == 140 and j == 139:
        print(dist)
        break

    if adj[(i, j)] > dist:
        continue

    if (i,j) in step:
        print("bad")
    step.add((i,j))

    dist += 1
    if inp[i][j] == '.':
        for di, dj in dir:
            di += i
            dj += j
            if (di == li and dj == lj):
                continue
            if inp[di][dj] == '#':
                continue
            if dist > adj.get((di,dj), 0):
                adj[(di,dj)] = dist
                heapq.heappush(pq, (dist, di, dj, i, j))
    else:
        #print(inp[i][j])
        di, dj = dir[dch.index(inp[i][j])]
        di += i
        dj += j
        if (di == li and dj == lj):
            continue
        if inp[di][dj] == '#':
            continue
        if dist > adj.get((di,dj), 0):
            adj[(di,dj)] = dist
            heapq.heappush(pq, (dist, di, dj, i, j))
    


