# n = int(input())

# m = int(input())

# arr = list(input())
# target = []
# for i in range(n):
#     target.append("I")
#     target.append("O")

# target.append("I")

# answer = 0
# # IO 를 갯수만큼 검사를 하되 마지막 +1 이 I면 +?
# for i in range(m- len(target)):
#     if arr[i] == "I":
#         if target == arr[i:i+len(target)]:
#             answer +=1

# print(answer)
# 서브 태스크 1만 성공

n = int(input())

m = int(input())

arr = input()
answer , i ,cnt = 0,0,0

while i <(m-1):
    if arr[i:i+3] == 'IOI':
        i +=2
        cnt +=1
        if cnt == n:
            answer += 1
            cnt -= 1
    
    else:
        i += 1
        cnt = 0

print(answer)