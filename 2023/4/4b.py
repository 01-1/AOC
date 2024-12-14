n=196
a=0
times = [1] * n
for j in range(n):
    _,x=input().split(':')
    win,our=x.split('|')
    win = win.split()
    our = our.split()
    wins = 0
    for x in our:
        if x in win:
            wins += 1
    for i in range(1,wins+1):
        times[j+i] += times[j]



#print(times)

print(sum(times))
