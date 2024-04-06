import sys
input = sys.stdin.readline

C, N = map(int,input().split())
cost_list = [list(map(int,input().split())) for _ in range(N)]
arr = []

dp = [1e9 for _ in range(C+100)]
dp[0] = 0

for cost, m in cost_list:
    for i in range(C+100):
        dp[i] = min(dp[i-m] + cost, dp[i])

print(min(dp[C:]))