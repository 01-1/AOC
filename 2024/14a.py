from collections import defaultdict

with open(0) as f:
    lines = [line.strip() for line in f.readlines()]

t = 100
s=[0]*4

for line in lines:
    p, v = line.split()
    exec(p)
    exec(v)
    pi, pj = p
    vi, vj = v
    x, y = (pi + vi*t) % 101, (pj + vj*t) % 103
    if x == 50 or y == 51:
        continue
    s[(x<50) + (y<51)*2]+=1

a,b,c,d=s
print(s)
print(a*b*c*d)
