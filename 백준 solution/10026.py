
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx= [-1,1,0,0]
    dy= [0,0,1,-1]
    visited[x][y] = 1
    while q:
        a, b =q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx<n and 0<= ny <n and arr[nx][ny] == arr[a][b] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))

n =int(input())
arr = []
for _ in range(n): 
    arr.append(input())

visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            bfs(i,j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt1 , cnt2)

