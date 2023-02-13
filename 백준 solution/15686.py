import sys
from itertools import combinations
input = sys.stdin.readline

n , m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

house = []
chicken=[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i,j))
        if arr[i][j] == 2:
            chicken.append([i,j])

com = list(combinations(chicken,m))

answer = []
for i in com:
    total = 0
    for x,y in house:
        dist = int(1e9)
        for k in range(m):
            dist = min(abs(i[k][0] - x) + abs(i[k][1] -y),dist) 
        total += dist
    answer.append(total)

print(min(answer))

# for k in perm:
#     dist = int(1e9)
#     for x,y in house:
#         total = 0
#         for i in range(m):
#             dist = min(abs(k[i][0] - x) + abs(k[i][1] -y),dist)
#         answer += dist


