import sys
inp = sys.stdin.read().splitlines()
en=enumerate

minxy = 200000000000000
maxxy = 400000000000000
#minxy = 7
#maxxy = 27


ct=0
s=set()

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return None

lins = []

for l in inp:
    abc, d3f = l.split(' @ ')
    x,y,z = map(int,abc.split(', '))
    dx,dy,dz = map(int,d3f.split(', '))
    lins.append((x,y,dx,dy))

for i,(px,py,vx,vy) in en(lins):
    vx += px
    vy += py
    for j,(qx,qy,ux,uy) in list(en(lins))[i+1:]:
        #if i == j:
            #continue
        ux += qx
        uy += qy
        #if (px,py,vx,vy) == (qx,qy,ux,uy):
            #continue

        # x = (px + a*vx) = (qx + b*ux),
        # y =  py + a*vy  =  qy + b*uy
        l1 = line((px, py), (vx, vy))
        l2 = line((qx, qy), (ux, uy))
        inte = intersection(l1, l2)
        print(inte)
        if inte is not None:
            x, y = inte
            if minxy <= x <= maxxy and minxy <= y <= maxxy:
                if (vx-px) * (x - px) >= 0 and (vy - py) * (y - py) >= 0 and (ux - qx) * (x - qx) >= 0 and (uy - qy) * (y - qy) >= 0:
                    print(px, vx, x)
                    print(py, vy, y)
                    print(qx, ux, x)
                    print(qy, uy, y)
                    ct += 1

            
#print(ct//2)
print(ct)
#print(s)
#print(len(s))


# not 29536


