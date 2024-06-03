# import heapq
# n,m,l = map(int,input().split())
# buildings = list(map(int,input().split()))

# buildings.sort()
# arr = []
# if n == 0 :
#     heapq.heappush(arr,-l)
# else:
#     heapq.heappush(arr,-buildings[0])
#     if n > 1:
#         for i in range(1,n):
#             heapq.heappush(arr,-(buildings[i]-buildings[i-1]))
#     heapq.heappush(arr,-(l-buildings[-1]))

# for i in range(m):
#     k = heapq.heappop(arr)
#     heapq.heappush(arr, k//2)
#     heapq.heappush(arr, k-k//2)

# print(-heapq.heappop(arr))

N, M, L = map(int, input().split())
arr = [0]+list(map(int, input().split()))+[L]
arr.sort()

start, end = 1, L-1
result = 0
while start <= end:
    count = 0
    mid = (start+end) // 2
    for i in range(1, len(arr)):
        if arr[i]-arr[i-1] > mid:
            count += (arr[i]-arr[i-1]-1)//mid # 설치되어있는곳은 설치 못해서 뺀거에 -1 한번더
    if count > M:
        start = mid+1
    else:
        end = mid-1
        result = mid
print(result)