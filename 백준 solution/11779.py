import heapq
INF = int(1e9)
n = int(input())
m = int(input())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int,input().split())
    graph[a].append((b,cost))
start, end =map(int,input().split())
dist = [INF] * (n+1)
prev = [0] * (n+1)

def dij(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        wei , node =heapq.heappop(q)
        if dist[node] < wei:
            continue
        for x,new_wei in graph[node]:
            cost = wei+ new_wei
            if cost < dist[x]:
                dist[x] = cost
                prev[x] = node
                heapq.heappush(q,(cost,x))

dij(start)
print(dist[end])

route = [end]
now = end
while now != start:
    now = prev[now]
    route.append(now)

route.reverse()
print(len(route))

for i in route:
    print(i,end=" ")
