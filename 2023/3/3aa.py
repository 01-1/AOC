# all except numbers and .
# flood fill and then delet

n = 140
#n=10
inp = [input() for _ in range(n)]
e = [[' ']*len(x) for x in inp]

for i,r in enumerate(inp):
    for j,c in enumerate(r):
        if c not in '1234567890.':
            ri,rj = i,j
            ind = 0
            cs=[]
            for di in range(-1,2):
                for dj in range(-1,2):
                    ni = i+di
                    nj = j+dj

                    if (inp[ni][nj] in '1234567890'):
                        cs.append((ni,nj))

            #cs = [(i, j)]
            while (cs):
                ai, aj = cs.pop()
                e[ai][aj] = inp[ai][aj]
                for nj in (aj-1,aj+1):
                    if (nj == -1 or nj == len(r)):
                        continue
                    ni=ai
                    if (e[ni][nj] == ' ' and inp[ni][nj] in '1234567890'):
                        cs.append((ni,nj))

            e[ri][rj] = ' '
            i=ri
            j=rj

print ('\n'.join(map(lambda x: ''.join(x), e)))
f = (''.join(map(lambda x: ''.join(x), e))).split()
print(f)
#print ('\n'.join(map(lambda x: ''.join(x), e)))
print(sum(map(int,f)))





            #i=ii
            #j=jj
            
            
