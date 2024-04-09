# 투포인터
import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int,input().split())))

ans = 0

for i in range(N):
    target = arr[i]
    temp = arr[:i] + arr[i+1:]

    left, right = 0 , N-2
    while left < right:
        sum_value = temp[left] + temp[right]
        if sum_value > target:
            right -=1
        elif sum_value < target:
            left += 1
        else:
            ans +=1
            break

print(ans)