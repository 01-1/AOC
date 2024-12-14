t = []
n = 1000
for _ in range(n):
    a, b = input().split()
    b = int(b)
    kinds = {}

    for x in a:
        kinds[x] = kinds.get(x,0) + 1

    sk = sorted(kinds.values())[::-1] + [0,0]

    f,s = sk[:2]
    print(sk)

    if f == 5:
        d = 0
    elif f == 4:
        d = 1
    elif f == 3 and s == 2:
        d = 2
    elif f == 3:
        d = 3
    elif f == 2 and s==2:
        d = 4
    elif f ==2:
        d=  5
    else: 
        d = 6

    #g = "23456789TJQKA"
    g = 'AKQJT98765432'
    t.append((d, list(map(lambda c: g.index(c), a)), b))
    print(t[:-1])
    t.sort()
    print(t)


t.sort()
t.reverse()
print(t)

x =0
ct = 1
for a,d,b in t:
    x +=b * ct
    ct +=1
print(x)
