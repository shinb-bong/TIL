import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp=[[0] * 3 for _ in range(n)]
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]
for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][j+1], dp[i-1][j+2]) + arr[i][j]
        if j == 1:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j+1]) + arr[i][j]
        if j == 2:
            dp[i][j] = min(dp[i-1][j-2], dp[i-1][j-1]) + arr[i][j]

print(min(dp[n-1]))
