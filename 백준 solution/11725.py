from collections import deque
def bfs(n,tree):
    q = deque([1])
    parent = [0] * (n+1) # 부모 기록
    while q:
        now = q.popleft()
        for i in tree[now]:
            # 방문 x면서 1이 아니면 (작은 수부터 진행했기 때문)
            if parent[i] == 0 and i !=1:
                parent[i] = now
                q.append(i)

    for i in range(2,n+1):
        print(parent[i])


n = int(input())
tree = [[] for _ in range(n+1)]

# 방향성 없음
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

bfs(n,tree)





        

