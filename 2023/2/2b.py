h=0
for i in range(1,101):
    m=input().split(';')
    f=True
    sd={'r':0,'g':0,'b':0}
    for a in m:
        b = a.split(',')
        for k in b:
            ct=int(k[:-1])
            t=k[-1]
            sd[t] = max(sd[t], ct)
    x=1
    for a, b in sd.items():
        x*=b
    h+=x    

print(h)
