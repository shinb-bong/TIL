import sys
input = sys.stdin.readline

# 각 집중국 수신 가능 영역 길이의 합 최소

N = int(input())
K = int(input())

arr = list(map(int,input().split()))
arr.sort()

ans = []
for i in range(N-1):
    ans.append(arr[i+1] - arr[i])

ans.sort() # 최소 길이

print(sum(ans[:N-K]))
