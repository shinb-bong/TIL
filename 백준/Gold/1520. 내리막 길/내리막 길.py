import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(m)]
dp = [[-1] * n for i in range(m)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx< m and 0<= ny <n and arr[x][y] > arr[nx][ny]:
                dp[x][y] += dfs(nx,ny)
                
    return dp[x][y]
print(dfs(0,0))