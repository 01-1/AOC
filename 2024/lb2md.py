with open(0) as f:
    inp = f.readlines()

replace = '    |         |      |     |          |     |       '
newlines = ['''|   |         |      |     |          |     ||
----|--------:|-----:|----:|----------|-----|-------
Day |     Time| Rank |Score|      Time| Rank| Score''']

for i, line in enumerate(inp):
    newline = ''
    for j, k in zip(line, replace):
        if k == '|':
            newline += k
        else:
            newline += j
    newlines.append(newline)

for line in newlines:
    print(line.rstrip())
