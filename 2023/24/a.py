import sys
inp = sys.stdin.read().splitlines()
en=enumerate


things = []

for l in inp:
    abc, d3f = l.split(' @ ')
    x,y,z = map(int,abc.split(', '))
    dx,dy,dz = map(int,d3f.split(', '))
    things.append(((x,y,z),(dx,dy,dz)))

things2 = things[2:]

RG = 200
rg = range(-RG, RG)

lines = []

epsilon = 1e-4

def into(a, da, c, dc):
    a1,a2,a3 = a
    da1,da2,da3 = da
    b1,b2,b3 = da1 + a1, da2 + a2, da3 + a3
    c1,c2,c3 = c
    dc1, dc2, dc3 = dc
    d1,d2,d3 = dc1 + c1, dc2 + c2, dc3 + c3
    #input a1,a2,a3 and all the other components here. 

    #define all constants required for solving t and s
    A=b1-a1
    B=c1-d1
    C=c1-a1
    D=b2-a2
    E=c2-d2
    F=c2-a2

    #find t and s using formula

    tn=(C*E-F*B)
    td=(E*A-B*D)
    sn=(D*C-A*F)
    sd=(D*B-A*E)
    if td == 0 or sd == 0:
        return False

    #try:
        #t=(C*E-F*B)/(E*A-B*D)
        #s=(D*C-A*F)/(D*B-A*E)
    #except ZeroDivisionError:
        #return False
    t = tn / td
    s = sn / sd

    print(a1 + t * da1, a2 + t * da2, a3 + t * da3)
    print(sum((a1 + t * da1, a2 + t * da2, a3 + t * da3)))
    print(c1 + s * dc1, c2 + s * dc2, c3 + s * dc3)
    print(sum((c1 + s * dc1, c2 + s * dc2, c3 + s * dc3)))

    if ((tn*sd*(b3-a3)+sn*td*(c3-d3)) == sd*td*(c3-a3)):
        return (0<=tn/td and 0<=sn/sd)
    return False
        

bx,by,bz = -153,-150,296

p0, (vx, vy, vz) = things2[0]
rel0 = (vx-bx,vy-by,vz-bz)
p1, (vx, vy, vz) = things2[1]
rel1 = (vx-bx,vy-by,vz-bz)
into(p0, rel0, p1, rel1)


sys.exit(0)
for bx in rg:
    for by in rg:
        for bz in rg:
            p0, (vx, vy, vz) = things2[0]
            rel0 = (vx-bx,vy-by,vz-bz)
            p1, (vx, vy, vz) = things2[1]
            rel1 = (vx-bx,vy-by,vz-bz)
            if doesint(p0, rel0, p1, rel1):
                print(bx,by,bz)
                

                
            #if doesint(p, (p1+vx,p2+vy,p3+vz), 
    print(bx)



                
            
#print(ct//2)
#print(s)
#print(len(s))


# not 29536


