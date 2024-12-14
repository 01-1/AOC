import sys
inp = sys.stdin.readlines()

label2type = {}
children = {}

flowand = {}
ict = {}

labels= []
for l in inp:
    l, r = l.rstrip().split(' -> ')
    typee, label = l[0], l[1:]
    labels.append(label)
    label2type[label]=typee
    children[label] = r.split(', ')
    for c in children[label]:
        if c not in label2type:
            children[c] = []
            label2type[c] = '.'
    flowand[label] = 0

for label in labels:
    for c in children[label]:
        if c not in ict:
            ict[c] = {}
        ict[c][label] = 0





#label2type



lows = 0
highs = 0

print(children)

for _ in range(1000):
    pulses = [('roadcaster', 0)]
    #lows += 1
    while pulses:
        label, hi = pulses.pop(0)
        print ( label, hi, children[label] )
        if hi == 1:
            highs += 1
        else:
            lows += 1
        if label2type[label] == '%':
            if hi != 0:
                continue

            flowand[label] = 1-flowand[label]

            if flowand[label]:
                highs += 0*len(children[label])
            else:
                lows += 0*len(children[label])

            for child in children[label]:
                pulses.append((child, flowand[label]))

                if label2type[child] == '&':
                    if ict[child][label] < flowand[label]: 
                        flowand[child] += 1
                    elif ict[child][label] > flowand[label]: 
                        flowand[child] -= 1
                    ict[child][label] = flowand[label]

        elif label2type[label] == '&':
            rf = 1 if flowand[label] == len(ict[label]) else 0

            if rf:
                lows += 0*len(children[label])
            else:
                highs +=0*len(children[label])
                flowand[label] = 0

            for child in children[label]:
                pulses.append((child, rf))
                if label2type[child] == '&':
                    if ict[child][label] < rf: 
                        flowand[child] += 1
                    elif ict[child][label] > rf: 
                        flowand[child] -= 1
                    ict[child][label] = rf
            flowand[label] = rf

        elif label2type[label] == 'b':
            lows += 0*len(children[label]) #no hi
            flowand[label] = hi 
            for child in children[label]:
                pulses.append((child, flowand[label]))
                if label2type[child] == '&':
                    if ict[child][label] < flowand[label]: 
                        flowand[child] += 1
                    elif ict[child][label] > flowand[label]: 
                        flowand[child] -= 1
                    ict[child][label] = flowand[label]



print(lows, highs)
    
print(lows*highs)
