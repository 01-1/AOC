n=110
g=[input() for _ in range(n)]

dirs = (0,1), (1,0), (0,-1), (-1,0)

xs=[]
for fd,dd in enumerate(dirs):
    for ij in range(n):
        tupu = []
        for pos in dd:
            if pos == 0:
                tupu.append(ij)
            elif pos == 1:
                tupu.append(0)
            else:
                tupu.append(n-1)
        fi,fj=tupu
        cpos = [(fi,fj,fd)]

        h = [[[0] * 4 for _ in range(n)] for _ in range(n)]

        while cpos:
            npos = []
            for i, j, d in cpos:
                h[i][j][d] = 1
                nds = [d]
                c = g[i][j]
                if c == '.':
                    pass
                if c =='/':
                    nds = [d ^ 3]
                elif c == '\\':
                    nds = [d ^ 1]
                elif c == '|':
                    if d & 1:
                        pass
                    else:
                        nds = [1, 3]
                elif c == '-':
                    if d & 1:
                        nds = [0, 2]


                for nd in nds:
                    di, dj = dirs[nd]
                    ni = i + di
                    nj = j + dj
                    if not (0 <= ni < n and 0 <= nj < n):
                        continue
                    if h[ni][nj][nd]:
                        continue
                    h[ni][nj][nd] = 1
                    npos.append((ni,nj,nd))
            cpos=npos
                
        x=0
        for a in h:
            for b in a:
                t = 0
                for c in b:
                    if c:
                        t = 1
                x += t


        xs.append(x)
print(xs)
print(max(xs))
