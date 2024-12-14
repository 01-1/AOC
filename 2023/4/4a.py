
a=0
times = [1] * 196
for _ in range(196):
    _,x=input().split(':')
    win,our=x.split('|')
    win = win.split()
    our = our.split()
    wins = 1
    for x in our:
        if x in win:
            wins += 1
    wins //= 2
    a += wins




print(a)
