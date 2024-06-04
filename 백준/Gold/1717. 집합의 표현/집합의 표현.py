import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline
n, m = map(int,input().split())
parent = [i for i in range(n+1)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def check(a,b):
    if find_parent( a) == find_parent(b):
        print("yes")
    else:
        print("no")

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    com, n1,n2 = map(int,input().split())
    if com == 0:
        union(n1,n2)
    else:
        check(n1,n2)

