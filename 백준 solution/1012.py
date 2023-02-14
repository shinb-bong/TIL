import sys
sys.setrecursionlimit(10**9)
def dfs(x,y):
  for i in range(4):
    dx =[-1,1,0,0]
    dy =[0,0,-1,1]
    nx = x + dx[i]
    ny = y + dy[i]
    if (0<=nx<n) and (0<= ny <m):
      if graph[nx][ny] == 1:
        graph[nx][ny] = -1
        dfs(nx,ny)
    
tc = int(input())
for _ in range(tc):
    m, n, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int,input().split())
        graph[b][a] = 1

    answer = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                answer += 1
    print(answer)