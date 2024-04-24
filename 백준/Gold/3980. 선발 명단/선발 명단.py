C = int(input())

def dfs(p,s):
    global max_score
    if p == 11:
        max_score = max(max_score,s)
        return 
    
    for i in range(11):
        if visited[i]:
            continue
        if arr[p][i] == 0:
            continue
        
        visited[i] = 1
        dfs(p+1,s+arr[p][i])
        visited[i] = 0

for _ in range(C):
    arr = [list(map(int,input().split())) for _ in range(11)]
    max_score = 0
    visited = [0] * 11
    dfs(0,0)
    print(max_score)