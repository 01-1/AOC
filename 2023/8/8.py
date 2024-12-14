from math import gcd
xx = input()
input()

lc = {}
rc = {}

cnodes = []
for _ in range(718):
    x, y, z, w = input().split()
    z = z[1:4]
    w = w[:3]
    lc[x] = z
    rc[x] = w
    if x[-1] == 'A':
        cnodes.append(x)
    ##jprint(x,y,z,w)
    #print(lc[x], rc[x])


#steps = 0
#c = 'AAA'

#for c in cnodes:
    #cyc = 
#bignum = 139301
#print(len(xx*bignum))

gcder=[]

for c in cnodes:
    #origc = lc[c]
    nodes = {}


    steps = 0
    while 1:
        bb = False
        for ind, lr in enumerate(xx):
            if (c, ind) in nodes:
                print('cycle steps:', steps)
                print('cycle len:', steps - nodes[(c,ind)])
                gcder.append(steps - nodes[(c, ind)])
                bb = True
                break
            nodes[(c, ind)] = steps
            if lr == 'L':
                    c=(lc[c])
            else:
                    c=(rc[c])
            steps+=1
            fl = True
            if c[-1] == 'Z':
                print('z steps:', steps)

        if bb:
            break
    print(c, steps)


gg = 1
for x in gcder:
    ggg = gcd(gg,x)
    gg *= x // ggg

print(gg)
#print(steps)
#while c != 'ZZZ':

    


