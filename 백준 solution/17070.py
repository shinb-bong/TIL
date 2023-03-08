n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dp = [[0]*n for _ in range(n)]
blank = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            blank.append((i,j))
            dp[i][j] = 0

dp[0][0] = 1
dp[0][1] = 1
for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = dp[i-1][j]