# from collections import deque
# import sys
# input = sys.stdin.readline
# n, m = map(int,input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# ans = []

# dx = [-1,1,0,0]
# dy = [0,0,1,-1]

# def bfs(x,y):
#     if graph[x][y] == 2 or graph[x][y] == 0:
#         return 0
#     arr = [item[:] for item in graph]
#     q = deque()
#     q.append([x,y,0])
#     arr[x][y] = -1
#     while q:
#         a,b,cost = q.popleft()
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx < 0 or nx >= n or ny <0 or ny >= m:
#                 continue
#             if arr[nx][ny] == 2:
#                 return cost+1
#             if arr[nx][ny] == 0 or arr[nx][ny] == -1:
#                 continue
            
#             arr[nx][ny] = -1
#             q.append([nx,ny,cost+1])

# for i in range(n):
#     temp = []
#     for j in range(m):
#         temp.append(bfs(i,j))

#     ans.append(temp)

# for i in range(n):
#     print(" ".join(map(str,ans[i])))

# 실패 요인:
# 시간초과로 인한 실패를 경험했다.

# 왜 시간초과일까 고민을 해보니 n = 1000 m = 1000에 O(MN) 이니깐 1000,000 인데

# 모든 칸에 대해 수행할 경우 너무 많은 수행을 하게 되어 시간 초과로 이어진다.

# 그렇다면 어떻게 해야할까?

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

ans = []
visited = [[-1]* m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    while q:    
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            if visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[a][b] +1
                    q.append([nx,ny])
           
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i,j)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end = ' ')
    print()