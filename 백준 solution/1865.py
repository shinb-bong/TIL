# 플로이드 워셜 실패
# import sys
# input = sys.stdin.readline
# tc = int(input())
# for _ in range(tc):
#     n,m,w = map(int,input().split())

#     INF = int(1e9)
#     graph = [[INF] * (n+1) for _ in range(n+1)]
#     for _ in range(m):
#         x,y, cost = map(int,input().split())
#         graph[x][y] = cost

#     for _ in range(w):
#         x,y, cost = map(int,input().split())
#         graph[x][y] = -cost

#     for k in range(1,n+1):
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 if i == j:
#                     graph[i][j] = 0
#                 if graph[i][j] > graph[i][k] + graph[k][j] :
#                     graph[i][j] = graph[i][k] + graph[k][j]
#     print(graph)
#     answer = True
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if graph[i][j] <= INF:
#                 answer = False

#     if answer == False:
#         print("No")
#     else:
#         print("YES")

# ------


# 음수 간선이 있으면 벨만 포드
# 없으면 다익스트라
# 수가 적으면 플로워셜
def bf(start):
    dist[start] = 0
    for i in range(1, n+1):
        for s in range(1, n+1):
            for next, time in graph[s]:
                if dist[next] > dist[s] + time:
                    dist[next] = dist[s] + time
                    if i == n: #n번 이후에도 값이 갱신되면 음수 사이클 존재.
                        return True
    return False

INF = int(1e9)
tc = int(input())
for _ in range(tc):
    n,m,w = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)
    for _ in range(m):
        x,y, cost = map(int,input().split())
        graph[x].append((y,cost))
        graph[y].append((x,cost))

    for _ in range(w):
        x,y, cost = map(int,input().split())
        graph[x].append((y,-cost))

    result=bf(1)
    if result == False:
        print("NO")
    else:
        print("YES")