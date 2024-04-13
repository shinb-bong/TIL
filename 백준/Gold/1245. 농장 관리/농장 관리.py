from collections import deque
dx = [1,0,-1,0,1,1,-1,-1]  # X,Y 모두 1이하이니 8방향
dy = [0,1,0,-1,1,-1,1,-1]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

def bfs(r,c):
    now_height = graph[r][c]
    q = deque()
    q.append((r,c))
    flag = True
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]
            
            if  0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == now_height:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] > now_height:
                    flag = False
    if flag:
        return True
    
    return False

cnt = 0

for r in range(N):
    for c in range(M):
        if not visited[r][c] and bfs(r, c):
            cnt += 1

print(cnt)
