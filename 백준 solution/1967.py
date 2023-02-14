import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 재귀 한계를 정해준다.

n = int(input())
graph = [[] for _ in range(n+1)]

def dfs(a,b):
    for i in graph[a]:
        dx, dy = i
        if dist[dx] == -1:
            dist[dx] = b + dy
            dfs(dx,b+dy)

# 양방향 그래프
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])   

# 1번 노드에서 말단 노드를 찾는다.
dist = [-1] * (n + 1)         
dist[1] = 0
dfs(1,0)

# 한쪽 끝에서 다른 끝까지 가야하니깐 다시 dfs
start= dist.index(max(dist)) # 마지막 노드의 인덱스
dist = [-1] * (n + 1)         
dist[start] = 0
dfs(start,0)
print(max(dist))