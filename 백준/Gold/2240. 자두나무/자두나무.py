import sys

input = sys.stdin.readline

T, W = map(int, input().split())
jadu = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]

# bottom_up dp
dp[1][0], dp[1][1] = jadu[1] % 2, jadu[1] // 2 # 초기항
for t in range(2, T + 1):
    for w in range(W + 1):
        j = jadu[t] % 2 if w % 2 == 0 else jadu[t] // 2 # 1,2, 번 구분
        dp[t][w] = max(dp[t - 1][0:w + 1]) + j
        #  t초 전까지 w 만큼 움직인것의 합 
print(max(dp[-1]))