# # 숫자가 별로 크지 않아서 플로이드 워셜
# INF = int(1e9)

# n, m = map(int,input().split())
# dist  = [[INF] * (n+1) for _ in range(n+1)]
# arr = [['-'] * (n + 1) for _ in range(n + 1)]
# for _ in range(m):
#     a, b, w = map(int, input().split())
#     dist[a][b] = dist[b][a] = w
#     arr[a][b] = str(b)
#     arr[b][a] = str(a)

# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if i == j:
#                 continue
#             if dist[i][j] > dist[i][k] + dist[k][j]:
#                 dist[i][j] = dist[i][k] + dist[k][j]
#                 arr[i][j] = arr[i][k]

# for i in arr[1:]:
#     for k in i[1:]:
#         print(k,end=" ")
#     print()

# 다익스트라 연습 
import heapq
INF = int(1e9)
def dijkstra(start):
    heap = []
    heapq.heappush(heap,[0,start])
    dp = [INF] *(n+1)
    dp[start] = 0
    # 전체 검색
    while heap:
        w, nu = heapq.heappop(heap)
        for ne, nw in s[nu]:
            wei = nw + w
            if dp[ne] > wei:
                dp[ne] = wei
                heapq.heappush(heap, [wei, ne])
                d[ne - 1][start - 1] = nu

n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
d = [[0] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])

for i in range(1, n + 1):
    dijkstra(i)

for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end=" ")
        else:
            print(d[i][j], end=" ")
    print()

