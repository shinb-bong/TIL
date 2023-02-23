tc = int(input())
dp = [[0,0] for _ in range(41)]
for x in range(41):
    if x == 0:
        dp[0] = [1,0]
        continue
    if x == 1:
        dp[1] = [0,1]
        continue

    zero = dp[x-1][0]+dp[x-2][0]
    one = dp[x-1][1]+dp[x-2][1]
    dp[x] = [zero,one]

for _ in range(tc):
    n = int(input())
    print(" ".join(map(str,dp[n])))