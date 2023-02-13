from itertools import combinations

n, m = map(int,input().split())
dp = []
for i in range(1,n+1):
    dp.append(i)
arr = list(combinations(dp,m ))
arr.sort()
for i in arr:
    for a in i:
        print(a,end=" ")
    print()