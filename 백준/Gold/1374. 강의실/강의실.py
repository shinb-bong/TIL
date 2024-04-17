import sys
import heapq
input = sys.stdin.readline

n = int(input())

# 강의 번호, 시작 , 끝나는 시간
# 적은 강의실 사용
# 시간 정렬 과 힙 필요
arr = []
for i in range(n):
    arr.append(list(map(int,input().split()))[1:])

arr.sort()

rooms = []
heapq.heappush(rooms, arr[0][1])

for i in range(1,n): # 첫 강의를 이미 넣었기 떄문에
    if arr[i][0] < rooms[0]: # 새로운 방
        heapq.heappush(rooms,arr[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms,arr[i][1]) 

print(len(rooms))

