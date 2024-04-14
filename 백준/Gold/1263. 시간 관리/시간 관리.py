import sys
input = sys.stdin.readline

n = int(input())


arr = []
for i in range(n):
    t, s = map(int,input().split())
    arr.append((s,t)) # 끝나는 시간, 걸리는 시간

arr.sort(reverse= True)

answer = arr[0][0] - arr[0][1]

for i in range(1,n):
    if answer > arr[i][0]: # 크면 겹칠 일이 없으니 새로운 일끝나는 시간이 곧 끝나는 시간
        answer = arr[i][0] - arr[i][1]

    else:
        # 작으면 겹치니깐 우선된 일이 끝나자마자 이어서 한다고 생각
        answer -= arr[i][1]

print(answer if answer>= 0 else -1)