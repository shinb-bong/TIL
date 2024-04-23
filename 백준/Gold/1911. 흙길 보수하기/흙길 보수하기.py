import sys
import math

input = sys.stdin.readline

N, L = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort()

cnt =0
for i in range(N):
    length = arr[i][1] -arr[i][0]
    if i == N-1:
        cnt += math.ceil(length/L)
        break
    if (length) %L :
        temp = L - (length)%L
        now_cover = arr[i][1] + temp

        if arr[i+1][0] <= now_cover:
            arr[i+1][0] = now_cover
        cnt += (length)//L +1

    else:
        cnt += length// L

print(cnt)


