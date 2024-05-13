import sys
input = sys.stdin.readline

def dfs(node,dist):
    global maxdist
    visited[node] = True # 가장 큰수
    maxdist = max(dist,maxdist)
    if dist >= 4:
        return
    for next_node in graph[node]:
        if visited[next_node] == False:
            dfs(next_node,dist+1) # 이안에서 next_node는 True 가 되니깐
            # 다음 노드 계산할때 문제가 생김 그래서 다시 원복
            visited[next_node] = False # 원복 과정

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

maxdist = -1
check = False
for i in range(n):
    visited = [False for _ in range(n)]
    dfs(i,0)
    if maxdist >= 4: # 최소화
        print(1)
        check=True
        break

if check == False:
    print(0)