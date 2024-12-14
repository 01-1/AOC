def count_arrangements(row, groups):
    ans = 0
    qs = row.count('?')
    for i in range(2**qs):
        #g = ''

        cts = []
        cct = 0
        for c in row:
            if c == '?':
                if i&1:
                    c = '#'
                else:
                    c = '.'
                i>>=1
            if c == '.':
                if cct != 0:
                    cts.append(cct)
                    cct = 0
            else:
                cct += 1
            #print(c,end='')
        #print()
        if cct != 0:
            cts.append(cct)
        #cts.sort()
        #print(cts)
        if cts == groups:
            ans+=1
    #print(ans)
    return ans

n=1000
def main():
    input_data = [
            input() for _ in range(n)
    ]

    total_arrangements = 0
    for line in input_data:
        parts = line.split(' ')
        row = parts[0]
        groups = list(map(int, parts[1].split(',')))
        
        total_arrangements += count_arrangements(row, (groups))

    print("Total arrangements:", total_arrangements)

if __name__ == "__main__":
    main()
