x = 0
for _ in range(1000):
    n =input()
    fc = '0'
    lc = '0'
    flag=1
    for c in n:
        if c in '1234567890':
            if flag:
                fc = c
                flag=0
            lc = c
    x += int(fc+lc)
print(x)
