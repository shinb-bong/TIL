import sys
input = sys.stdin.readline

n = int(input())
rooms = list(map(int,input().split()))
m = int(input())

dp = [-1e9] * (m+1)
for i in range(n-1,-1,-1):
    x = rooms[i]
    for j in range(x, m+1):
        dp[j] = max(dp[j-x]*10 + i, i, dp[j]) # 십의 자리로 올리고 붙이기, 그냥 붙이기, 이미 붙여있는거 사용하기
print(dp[m])

