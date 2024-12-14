def count_arrangements(row, groups):
    #row = '?'.join(row*5)
    row = '?'.join([row]*5)
    print(row)
    groups = groups * 5
    #print(groups)
    dp = [[0] * (len(groups)+1) for _ in range(len(row)+1)]
    dp[0][0] = 1

    #dp.append([1] * (len(groups)+1))
    #dp.append([1] * (len(groups)+1))

    cct = 0
    for i,c in enumerate(row):
        if c == '.':
            if cct != 0:
                cct = 0
        else:
            cct += 1
        i+=1

        #dp[i][0] += dp[i-1][0]
        if c != '#':
            dp[i][0] += dp[i-1][0]

        for j, n in ((enumerate(groups))):
            #print(n)
            j+=1
            if c != '#':
                dp[i][j] += dp[i-1][j]
            if cct>=n:
                if i-n-1 < 0:
                    if j==1 and i-n >= 0:
                        dp[i][j] += dp[i-n][j-1]

                elif row[i-n-1] != '#':
                    dp[i][j] += dp[i-n-1][j-1]


    print(dp)
    return dp[-1][-1]

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
