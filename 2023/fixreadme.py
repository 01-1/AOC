with open('README.md') as f:
    inp = f.readlines()

replace = '    |         |      |     |          |     |       '
newlines = []

for i, line in enumerate(inp):
    if i < 5:
        newlines.append(line)
    else:
        newline = ''
        for j, k in zip(line, replace):
            if k == '|':
                newline += k
            else:
                newline += j
        newlines.append(newline)

with open('README.md', 'w') as f:
    f.writelines(newlines)

