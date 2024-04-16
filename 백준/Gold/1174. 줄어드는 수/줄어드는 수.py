import sys
from itertools import combinations

n = int(sys.stdin.readline())

ans = []

for i in range(1,11):
    for comb in combinations(range(10), i):
        comb = list(comb)
        comb.sort(reverse =True)
        ans.append(int("".join(map(str,comb))))
    if n < len(ans):
        break

ans.sort()

try: 
    print(ans[n-1])
except:
    print(-1)

