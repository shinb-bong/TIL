from collections import deque

n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

# 이동할 방향 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    # 큐 구현
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        # 현재 위치에서 네 방향으로 모두 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 넘치는 것 제외
            if nx < 0 or ny >0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단 기록 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[nx][ny] +1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
