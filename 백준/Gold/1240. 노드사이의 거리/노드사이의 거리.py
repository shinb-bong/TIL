import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,find):
    q = deque()
    q.append((start,0))

    visited = [False] * (N+1)
    visited[start] = True

    while q:
        a,b = q.popleft()

        if a == find:
            return b

        for n, d in graph[a]:
            if not visited[n]:
                visited[n] = True
                q.append((n,b+d))

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

for _ in range(M):
    a,b = map(int,input().split())
    print(bfs(a,b))
    