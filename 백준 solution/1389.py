# 유저 수가 적으므로 플로이드 워셜
INF = int(1e9)
n, m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
result=[]
for i in range(1,n+1):
    sum = 0
    for j in range(1,n+1):
        sum += graph[i][j]
    
    result.append((sum,i))

result.sort()
print(result[0][1])

