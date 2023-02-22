# n = input()

# arr =[]
# tmp = []
# cond = False
# for i in n:
#     if i == "(":
#         continue
#     if i == ")":
#         cond= True
#         continue
#     if cond:
#         arr.append(i)
#         for _ in range(len(tmp)):
#             arr.append(tmp.pop())
#         cond = False
#         continue
#     if i.isalpha():
#         arr.append(i)
#         continue
#     if i == "+" or i =="-":
#         tmp.append(i)
#         continue
#     tmp.append(i)
#     cond=True

# if tmp:
#     for _ in range(len(tmp)):
#             arr.append(tmp.pop())    
    
# print("".join(arr))

# ----- 그림 그려서 새로운 조건문 생각하기 ----- 
# 머리속으로는 복잡해서 불가
n = list(input())
arr = []
answer = ''

for i in n:
    if i.isalpha():
        answer += i
    else:
        if i == '(':
            arr.append(i)
        elif i == "*" or i == '/':
            while arr and (arr[-1] == "*" or arr[-1] == "/"):
                answer += arr.pop()
            arr.append(i)

        elif i == "+" or i  == "-":
            while arr and arr[-1] != '(':
                answer += arr.pop()
            arr.append(i)
        
        elif i == ")":
            while arr and arr[-1] != '(':
                answer += arr.pop()
            arr.pop()

while arr:
    answer += arr.pop()

print(answer)
        
     

