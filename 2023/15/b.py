x=input().split(',')
y = {}
#q = [[] for _ in range(10)]
box = [{} for _ in range(256)]
ibox = [0]*256

cv=0
s = 0
for w in x:
    wn = w[-1]
    if wn == '-':
        sw = w[:-1]
    else:
        sw = w[:-2]

    cv=0
    for c in sw:
        cv += ord(c)
        cv *= 17
        cv %= 256
    
    
    if (wn == '-'):
        if sw in box[cv]:
            box[cv].pop(sw)
    else:
        if sw in box[cv]:
            box[cv][sw] = (box[cv][sw][0], wn[-1])
            ibox[cv]+=1
        else:
            #if box[cv] != {}:
                #cv += 1
                #cv %= 256
            box[cv][sw] = (ibox[cv], wn[-1])
            ibox[cv]+=1

for i,d in enumerate(box):
    i += 1
    l = list(d.values())
    l.sort()
    for j, (qi, n) in enumerate(l):
        j += 1
        s += i * j * int(n)
        print(i * j * int(n), i, j, n)



print(s)

