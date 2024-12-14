from collections import defaultdict

with open(0) as f:
    lines = [line.strip() for line in f.readlines()]

for t in range(0,9999):
    e = [[' ']*103 for _ in range(101)]

    flag = True
    for line in lines:
        p, v = line.split()
        exec(p)
        exec(v)
        pi, pj = p
        vi, vj = v
        x, y = (pi + vi*t) % 101, (pj + vj*t) % 103
        if x == 50 or y == 51:
            continue
        e[x][y] = '#'
        if (x < 10 and y < 10):
            flag = False
        #s[(x<50) + (y<51)*2]+=1

    if flag:
        print('\n'.join([''.join(l) for l in e]))
        print(t)

