from collections import deque

def bfs():
    q =  deque()
    q.append((hx,hy))
    while q:
        x,y = q.popleft()
        if abs(x-ex) + abs(y-ey) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = con[i]
                if abs(x-nx) + abs(y-ny) <= 1000: # 다음 편의점까지 갈수 있다면
                    visited[i] = 1
                    q.append((nx,ny))
    print('sad')
    return

tc = int(input())
for _ in range(tc):
    n = int(input())
    hx,hy = map(int,input().split())
    con = []
    for _ in range(n):
        con.append(list(map(int,input().split())))

    ex,ey = map(int,input().split())

    visited = [0 for _ in range(n)]

    bfs()