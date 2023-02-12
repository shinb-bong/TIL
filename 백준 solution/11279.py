import heapq
import sys
input = sys.stdin.readline
n = int(input())

q = []
for _ in range(n):
    k = int(input())
    if k == 0:
        print(-heapq.heappop(q) if len(q)>0 else "0")

    else:
        heapq.heappush(q,-k)