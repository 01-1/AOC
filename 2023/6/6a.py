
time='        59     70     78     78'.split()
distance='   430   1218   1213   1276'.split()
time=map(int,time)
distance=map(int,distance)
#time,distance=map(list,(time,distance))
a = 1
for t,d in zip(time, distance):
    recs = 0
    for xt in range(t+1):
        dtrav = (t-xt) * xt
        if (dtrav > d):
            recs += 1
    a *= recs

print(a)






