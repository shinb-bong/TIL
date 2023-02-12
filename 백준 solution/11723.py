import sys
input = sys.stdin.readline
n = int(input())
s = set()

for _ in range(n):
    arr = list(input().split())
    if len(arr) == 1:
        if arr[0] == "all":
            s = set([i for i in range(1,21)])
        else:
            s = set()
    else:
        cond, x = arr[0],int(arr[1])
        if cond == "add":
            s.add(x)
        if cond == "remove":
            s.discard(x)
        if cond == "check":
            print(1 if x in s else 0)
        if cond == "toggle":
            if x in s:
                s.discard(int(arr[1]))
            else:
                s.add(x)
    
