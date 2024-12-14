
xx =list(map(int, input().split()))
print(len(xx))
print(*xx)

sz = max(xx)
sz=0
#print(sz)
x = [False] * sz
#print('memory!!')

#print(len(xx))
xx=[]
for a,b in zip(xx[::2],xx[1::2]):
    for i in range(a,a+b):
        #x.append(i)
        x[i] = True

#print('done with this part')

input()
input()




mappas = []
while 1:
    n = input()
    if n == '':
        input()
        # end, map
        y = [False] * sz
        for seed, b in enumerate(x):
            if not b:
                continue
            for a,b,c in mappas:
                if b <= seed < b + c:
                    #print(a, b, c, seed)
                    #y.append(a + seed - b)
                    y[a+seed-b] = True
                    break
            else:
                y[seed] = True
                #y.append(seed)

        x=y
        #print(x)
        print(len(mappas))
        for a,b,c in mappas:
            print(a,b,c)
        mappas=[]

        
    elif n == 'end':
        break
    else:
        mappas.append(list(map(int,n.split())))

#print(x)
#print(min(x))
