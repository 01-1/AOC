sd={'r':12,'g':13,'b':14}
h=0
for i in range(1,101):
    m=input().split(';')
    f=True
    for a in m:
        b = a.split(',')
        for k in b:
            ct=int(k[:-1])
            t=k[-1]
            if ct > sd[t]:
                f=False
    if f:
        h+=i
print(h)
