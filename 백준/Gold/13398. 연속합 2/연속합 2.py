import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

dp = [[0]*n for _ in range(2)]
# 누적합(덧셈 현재 제외)
dp[0][0] = arr[0]
dp[1][0] = -1000

for i in range(1,n):
    dp[0][i] = max(dp[0][i-1] +arr[i], arr[i]) # 이어넣기, 그냥 지금이 큼
    dp[1][i] = max(dp[0][i-1],dp[1][i-1] + arr[i]) # 현재수 뺀거, 빼진거에 현재수 넣기
print(max(max(dp[0]),max(dp[1])))