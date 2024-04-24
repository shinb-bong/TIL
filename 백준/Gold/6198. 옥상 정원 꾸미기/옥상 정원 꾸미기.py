n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
result = 0

# 내림차순 정렬됨
for i in arr:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    result += len(stack) -1 
    # stack.pop O(1)
    # 역으로 봐지는것을 계산한거임

print(result)
