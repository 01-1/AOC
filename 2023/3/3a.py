# all except numbers and .
# flood fill and then delet

n = 140
#n = 10
inp = [input() for _ in range(n)]
b = [list(x) for x in inp]
e = [list(x) for x in inp]

for i,r in enumerate(inp):
    for j,c in enumerate(r):
        if c not in '1234567890.':
            #ii=i
            #jj=j
            ind = 0
            cs = [(i, j)]
            while (cs):
                i, j = cs.pop()
                for di in range(-1,2):
                    for dj in range(-1,2):
                        ni = i+di
                        nj = j+dj
                        b[ni][nj] = 'o'
                        #if (b[ni][nj] != 0):
                            #b[ni][nj] = 0
                            #cs.append((ni, nj))
                        #else:
                            #break


for i,r in enumerate(inp):
    ok = False
    inn = False
    for j,c in enumerate(r):
        if c in '1234567890':
            if (not inn):
                ok = False
            inn = True
            if b[i][j] == 'o':
                ok = True
        else:
            if inn:
                if not ok:
                    #for jj, c in list(enumerate(r))[:j][::-1]:
                    for jj in range(j-1,-1,-1):
                        if e[i][jj] not in '1234567890':
                            break
                        e[i][jj] = '.'
                        b[i][jj] = '.'
            inn = False

        if inn:
            if not ok:
                for jj in range(len(r)-1,-1,-1):
                    if e[i][jj] not in '1234567890':
                        break
                    e[i][jj] = '.'
                    b[i][jj] = '.'
                #for jj, c in list(enumerate(r))[:][::-1]:
                if False:
                    if c not in '1234567890':
                        break
                    e[i][jj] = '.'

print ('\n'.join(map(lambda x: ''.join(x), e)))
for d in (e):
    for i, c in enumerate(d):
        if (c not in '1234567890'): d[i] = ' '

f = (''.join(map(lambda x: ''.join(x), e))).split()
print(f)
print ('\n'.join(map(lambda x: ''.join(x), e)))
print ('\n'.join(map(lambda x: ''.join(x), b)))
print(sum(map(int,f)))





            #i=ii
            #j=jj
            
            
