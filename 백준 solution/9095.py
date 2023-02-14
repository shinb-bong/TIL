tc = int(input())

for _ in range(tc):
    n = int(input())
    dp = [0]* 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4,12):
        for j in range(1,4):
            dp[i] += dp[i-j]
    print(dp[n])
