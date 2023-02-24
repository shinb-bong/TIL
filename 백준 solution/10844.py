n= int(input())

dp = [[0]*10 for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1 # 무조건 1개

for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] # 0->1일때
        elif j == 9:
            dp[i][j] = dp[i-1][8] # 9 ->8일때
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] # 앞뒤

print(sum(dp[n]) % 1000000000)