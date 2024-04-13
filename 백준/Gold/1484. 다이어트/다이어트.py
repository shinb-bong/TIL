import sys
input = sys.stdin.readline

# G = 현재^2 - 기억^2
G = int(input())

n = [x for x in range(1,100001)]
t = [x for x in range(1,100001)]

N,M = 100000 , 100000

left, right = 0,0

answer = []

while left <N and right < M:
    temp = (n[left] + t[right]) * (n[left] - t[right])

    if temp == G:
        answer.append(n[left])
    if temp < G:
        left +=1
        continue
    right +=1

if not answer:
    print(-1)

else:
    for y in answer:
        print(y)

