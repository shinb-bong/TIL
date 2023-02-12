import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    arr = list(input().split())
    command= arr[0]
    if command == "push":
        result.append(arr[1])

    if command == "pop":
        print(result.pop() if len(result) != 0 else "-1")

    if command == "size" :
        print(len(result))

    if command == "empty":
        print("1" if len(result) == 0 else "0")

    if command == "top":
        print(result[-1] if len(result) != 0 else "-1")
        # if len(result) == 0:
        #     print("-1")
        # else:
        #     print(result[-1])