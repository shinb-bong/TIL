n = int(input())

cnt = 1
for i in range(n,0,-1):
    cnt *= i
arr = list(str(cnt))

answer = 0
while arr[-1] == '0':
    arr.pop()
    answer += 1

print(answer)

# 다른 방법
import sys

N = int(sys.stdin.readline())

print(N//5 + N//25 + N//125)

# 추가로 내가 생각한 방법
#  5를 나눠서 5의 배수를 구하고 다시 5를 나눠서 25의 배수 다시 5를 나누면 125의 배수
n = int(input())

count = 0

for num in range(1, n + 1):
    while num % 5 == 0:
        count += 1
        num = num // 5 

print(count)
