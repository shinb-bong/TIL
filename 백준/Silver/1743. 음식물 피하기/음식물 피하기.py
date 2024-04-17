import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
count = 0

def bfs(x,y):
    q = deque()
    q.append((x,y))
    size = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    size += 1
                    q.append((nx,ny))
    
    return size

for _ in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            size = bfs(i,j)
            count = max(count,size)

print(count)