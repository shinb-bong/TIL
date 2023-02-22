from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n):
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)-1,2):
        graph[arr[0]].append((arr[i],arr[i+1]))

# 지름 같은 경우 기준을 하나 잡고 가장 깊은거를 찾고 +
# 한번더해서 깊은거와 깊은걸 찾는다. 
def bfs(a):
    visited = [-1] * (n+1)
    visited[a] = 0
    q = deque([a])
    _max = [0, 0]

    while q:
        x = q.popleft()
        for node ,cost in graph[x]:
            # 방문하지 않았을때
            if visited[node] == -1:
                visited[node] = visited[x]+ cost
                q.append(node)
                if _max[0] < visited[node]:
                    _max = visited[node], node

    return _max
            
# 1번을 기준으로 제일 깊은 노드를 찾고
dis, node = bfs(1)
dis, node = bfs(node)

print(dis)

# def find_last_node(i,graph):
#     cnt = 0
#     if cnt == 5:
#         print(i)
#         return 
#     for x, cost in graph[i]:
#         find_last_node(x,graph)
#         cnt +=1
#         print(i)

# for i in range(1,n+1):
#     find_last_node(i,graph)


# # 내가 덱을 쓰는 BFS에 활용이 좋으므로 재귀(DFS)연습
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)-1,2):
        graph[arr[0]].append((arr[i],arr[i+1]))

# 여기가 차이점

def dfs(x,y):
    # 각 노드와 연결된 노드를 확인
    for a, b in graph[x]:
        # 아직 가지 않은 노드라면
        if visited[a] == -1:
            visited[a] = b + y # 거기까지의 거리로 만듬
            dfs(a,b+y) # 다시 이어진 걸로 이어서 탐색

visited = [-1] * (n + 1)
visited[1] = 0
 #1번부터 visited 업데이트해서 가장 먼 요소 찾기
dfs(1,0) # 시작은 코스트 0

start = visited.index(max(visited)) # 1번 노드에서 가장 먼 노드 찾기(값이 크면 됨) => 인덱스로 반환
visited = [-1] *(n+1) # 초기화
visited[start] = 0
dfs(start,0)

# 이제 가장 먼거에서 먼게되었음
print(max(visited))
# 가장 먼 노드는
print(f'가장 먼 노드는{start}에서 {visited.index(max(visited))}')