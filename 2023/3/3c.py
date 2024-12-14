# all except numbers and .
# flood fill and then delet

n = 140
#n = 10
inp = [input() for _ in range(n)]
b = [list(x) for x in inp]
e = [list(x) for x in inp]

s=set()
for i,r in enumerate(inp):
    for j,c in enumerate(r):
        if c not in '1234567890.':
            s.add(c)

print(s)
