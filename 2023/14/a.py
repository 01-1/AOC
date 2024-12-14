g = [list(input()) for _ in range(100)]#[::-1]
s=0

memo = {}

cleft=0

for n in range(10**9):
    memo[str(g)] = n

    for _ in range(4):
        for _ in range(105):
            for j in range(100):
                for i in range(99):
                    if g[i+1][j] == 'O' and g[i][j] == '.':
                        g[i+1][j] = '.'
                        g[i][j] = 'O'
        g = list(list(x)[::-1] for x in zip(*g))

    print(n)
    if str(g) in memo:
        l = memo[str(g)]
        cleft = (10**9-n-1) % (n + 1 - l)
        break

print(cleft)
for _ in range(cleft):
    for _ in range(4):
        for _ in range(105):
            for j in range(100):
                for i in range(99):
                    if g[i+1][j] == 'O' and g[i][j] == '.':
                        g[i+1][j] = '.'
                        g[i][j] = 'O'
        g = list(list(x)[::-1] for x in zip(*g))


for i,r in enumerate(g[::-1]):
    for c in r:
        if c == 'O':
            s += i + 1


print(s)

