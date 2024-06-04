import heapq
INF = int(1e9) 
n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, cost = map(int,input().split())  
    graph[a].append((b,cost))
    graph[b].append((a,cost))

stop1, stop2 = map(int,input().split())

def dijkstra(start,end):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        cost, node= heapq.heappop(q)
        if cost > distance[node]:
            continue
        for w,v in graph[node]:
            if distance[w] > distance[node] + v:
                distance[w] = distance[node] + v
                heapq.heappush(q,[distance[w],w])

    return distance[end]
# 두가지 방법 비교
path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, n)
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, n)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))

