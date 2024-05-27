arr = list(map(int,input().split()))

N = arr[0]
arr = arr[1:]
visited = [[False]*(2*N+1) for _ in range(2*N+1)]
visited[N][N] = True
dx = [0,0,-1,1]
dy = [1,-1,0,0]
answer = 0 
def dfs(x,y,cnt,p,visited):
    global answer
    if cnt == N:
        answer += p
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 
        if 0<= nx < 2*N+1 and 0<= ny < 2*N+1 and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx,ny,cnt+1,p*arr[i]/100,visited)
            visited[nx][ny] = False
    # q = deque())
    # q.append((x,y,0,1))
    # visited[x][y] = True

    # while q:
    #     x,y,cnt,p = q.popleft()
    #     if cnt == N:
    #         answer += p
    #         continue
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #         if 0<= nx < 2*N+1 and 0<= ny < 2*N+1 and visited[nx][ny] == False:
    #             visited[nx][ny] = True
    #             q.append((nx,ny,cnt+1,p*arr[i]/100))
    #             print(p*arr[i]/100)
    # bfs로는 취소를 못함

dfs(N,N,0,1,visited)

print(answer)



