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


#cnodes  = ['AAA']
steps = 0
#c = 'AAA'

#for c in cnodes:
    #cyc = 
#print(len(xx*bignum))

#xl = len(xx)
while 1:
    bb = False
    for lr in xx:
        nnodes = []
        if lr == 'L':
            for c in cnodes:
                nnodes.append(lc[c])
        else:
            for c in cnodes:
                nnodes.append(rc[c])
        steps+=1
        fl = True
        for n in nnodes:
            if n[-1] != 'Z':# and n != 'ZZZ':
                fl=False
        if fl:
            bb = True
            break
        cnodes=  nnodes

    if steps%1000 == 0:
        print(steps)

    if bb:
        break

print(steps)
#while c != 'ZZZ':

    


