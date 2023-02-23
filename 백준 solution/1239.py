import heapq
import sys
input = sys.stdin.readline
# 학생, 도로, 마을
n, m, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

def dij(start,end):
    q = []
    heapq.heappush(q,(0,start))
    visited = [-1] * (n+1)
    visited[start] = 0
    while q:
        cost,node = heapq.heappop(q)
        if node == end:
            return cost
        for a, b in graph[node]:
            if visited[a] == -1 or visited[a] > b+ cost:
                visited[a] = b+ cost
                heapq.heappush(q,(b+ cost, a))
    
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    if i != x:
        dp[i] += dij(i,x)
    
    dp[i] += dij(x,i)

print(max(dp))



# def bfs(start,end):
#     q = deque([])
#     q.append(start)
#     visited = [-1] * (n+1)
#     while q:
#         a = q.popleft()
#         for node, cost in graph[a]:
#             if visited[node] == -1 and visited[node] > visited[a]+ cost :
#                 visited[node] = visited[a]+ cost +1
#                 q.append(node)

#     return visited[end]

# dp = [0 for _ in range(n+1)]
# for i in range(1,n+1):
#     if i != x:
#         dp[i] += bfs(i,x)
    
#     dp[i] += bfs(x,i)
# print(dp)
# print(max(dp))


# 처음에는 BFS로 접근했다가
# 단방향성, 주어진 수가 크므로 플로이드워셜인
#  시간 복잡도 O(N^3)으로 검사를 하면 시간 초가가 날것 같다.
#  1,000,000,000
# 쨋든 다익스트라 알고리즘으로 접근했다. 
# 시간도 합격이고 통과
