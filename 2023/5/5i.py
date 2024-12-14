
xx =list(map(int, input().split()))
print(len(xx))
print(*xx)

input()
input()
mappas=[]

while 1:
    n = input()
    if n == '':
        input()
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
