import heapq
import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    k = int(input())
    if k < 0:
        heapq.heappush(q,(abs(k),False))
        continue
    if k >0 :
        heapq.heappush(q,(k,True))
        continue

    try:
        a,b = heapq.heappop(q)
        if b == False:
            print(-a)
        else:
            print(a)
    except:
        print(0)
