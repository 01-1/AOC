import sys
inp = sys.stdin.readlines()

ruld='RULD'
dir=((0,1),(1,0),(0,-1),(-1,0))


i,j = 0,0
cl = [(0,0)]
perim = 0

for abc in inp:
    a,b,c = abc.split()
    a=dir[ruld.index(a)]
    b=int(b)
    a = dir[int(c[-2])]
    b = int(c[2:-2], 16)
    di, dj = a
    di *= b
    dj *= b
    perim += b
    for _ in range(1):
        i+=di
        j+=dj
        cl.append((i,j))

print(perim)
ans = perim + 2
for (x1,y1),(x2,y2) in zip(cl,cl[1:]):
    ans += - x1 * y2 + x2 * y1
print(ans)
print(ans//2)



# perim = 8
# 4 + 8/2 + 1

# perim = 4
# 1 + 4/2 + 1

# I + B/2 + 1
sys.exit(0)

print(cl)
mini = 0
maxi = 0
minj = 0
maxj = 0
for i,j in cl:
    mini=min(i,mini)
    minj = min(j,minj)
    maxi = max(i,maxi)
    maxj = max(j,maxj)


gr = [[0]*(maxj-minj + 10) for _ in range(maxi-mini)]
for i,j in cl:
    gr[i][j] = 1

g=gr
num = len(cl)
#guess
q = [(-1,1)]
g[-1][1] =1

while q:
    i,j = q.pop()
    num += 1
    for di, dj in dir:
        di += i
        dj += j
        if g[di][dj] == 0:
            g[di][dj] = 1
            q.append((di,dj))



print(num)


