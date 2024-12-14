x=input().split(',')
cv=0
s = 0
for w in x:
    cv=0
    for c in w:
        cv += ord(c)
        cv *= 17
        cv %= 256
    print(cv)
    s += cv
print(s)

