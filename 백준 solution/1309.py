N = int(input())
dp = [[0,0,0] for _ in range(N)]
dp[0] = [1,1,1]
 
for i in range(1,N):4
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = sum(dp[i-1])%9901
 
print(sum(dp[-1])%9901)
