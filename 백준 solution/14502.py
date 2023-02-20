from collections import deque
import copy
# 수가 작기때문에 모든 경우의 수를 해보는 것도 좋을 듯하다.
def bfs():
    arr = copy.deepcopy(graph)
    q = deque()
    # 바이러스 시작 찾아주기
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i, j))

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0 :
                arr[nx][ny] = 2
                q.append((nx,ny))

    global answer
    result = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                result+=1

    answer = max(answer,result)

# 재귀사용하는 백트래킹 => 개인적으로 많이 부족한 부분
def wall(cnt):
    if cnt == 3: # 3개가 전부 꽉차면 계산 하지만 아니면 다른 백트래킹도있음
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1  #하나 만들고
                wall(cnt+1)
                graph[i][j] = 0  # 3개짜리 관련 모두 검사후 지우기      

n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

answer = 0
wall(0)
print(answer)
            
                
        





