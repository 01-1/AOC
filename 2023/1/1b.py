x = 0
dig = ['one','two','three','four','five','six','seven','eight','nine']
dig2 = ['1','2','3','4','5','6','7','8','9']
for _ in range(1000):
    n =input()
    bind = len(n)
    fc = 0
    for i, c in enumerate(dig):
        try:
            if n.index(c) < bind:
                bind = n.index(c)
                fc = i+1
        except ValueError:
            pass
    for i, c in enumerate(dig2):
        try:
            if n.index(c) < bind:
                bind = n.index(c)
                fc = i+1
        except ValueError:
            pass    
    bind=len(n)
    fc *= 10
    sc=0
    for i, c in enumerate(dig):
        try:
            if n[::-1].index(c[::-1]) < bind:
                bind = n[::-1].index(c[::-1])
                sc = i+1
        except ValueError:
            pass
    for i, c in enumerate(dig2):
        try:
            if n[::-1].index(c[::-1]) < bind:
                bind = n[::-1].index(c[::-1])
                sc = i+1
        except ValueError:
            pass
    print(n)
    print(fc+sc)
    x += fc+sc
print(x)
