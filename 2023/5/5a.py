x =map(int, input().split())
input()
input()

mappas = []
while 1:
    n = input()
    if n == '':
        input()
        # end, map
        y = []
        for seed in x:
            for a,b,c in mappas:
                if b <= seed < b + c:
                    #print(a, b, c, seed)
                    y.append(a + seed - b)
                    break
            else:
                y.append(seed)

        x=y
        print(x)
        mappas=[]

        
    elif n == 'end':
        break
    else:
        mappas.append(list(map(int,n.split())))

print(x)
print(min(x))
