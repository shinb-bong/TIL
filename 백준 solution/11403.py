n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] + arr[k][j] == 2:
                arr[i][j] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()

