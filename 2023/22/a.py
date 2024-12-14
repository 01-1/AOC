import sys
inp = sys.stdin.read().splitlines()


brix=[]

for brick in inp:
    a, b = brick.split('~')
    ax,ay,az = map(int,a.split(','))
    bx,by,bz = map(int,b.split(','))
    #ax+=1
    #ay+=1
    #az+=1
    bx+=1
    by+=1
    bz+=1
    #ax-=1
    #ay-=1
    #az-=1
    brix.append((az,ax,ay,bz,bx,by))

brix.sort()

down = []

child={}
wah = set()

for i in range(len(inp)):
    child[i] = []
for az,ax,ay,bz,bx,by in brix:
    zoff = 0

    z = None
    for i, (cz,cx,cy,dz,dx,dy) in enumerate(down):
        if not (bx <= cx or ax >= dx or by <= cy or ay >= dy): # https://stackoverflow.com/questions/40795709/checking-whether-two-rectangles-overlap-in-python-using-two-bottom-left-corner
            lzoff = zoff
            zoff = max(zoff, dz)
            if lzoff != zoff:
                z = i
            elif zoff == dz:
                z = None

    if z is not None:
        wah.add(z)
        child[z].append(len(down))

    #if z not in child:
        #child[z] = []

            
    bz+=zoff-az
    az=zoff
    down.append((az,ax,ay,bz,bx,by))

ans = -len(inp)
ans = 0

vis = 0
for i in range(len(inp)):
    if i in child:
        q = [i]
        ans -= 1
        while q:
            x=q.pop()
            ans += 1
            for y in child[x]:
                q.append(y)
            #q += child[x]
print(ans)


#print(wah)
#for x in wah:
    #print(down[x])
    
#print(len(inp)-len(wah))

