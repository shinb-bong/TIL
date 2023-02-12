n, k = map(int,input().split())

count = 0

# while n >= k :
#     while n%k != 0:
#         n -=1
#         count +=1
    
#     n //=k
#     count += 1

# while n > 1:
#     n-=1
#     count +=1
# print(count)

while True:
    target = (n//k) * k # 나눌수있는 최대수 
    count += (n-target) # 1로 뺸수

    #n 이 k보다 작을때 반복문 탈출
    if n < k:
        break

    count +=1
    n //=k

# 마지막으로 1씩 뺸거
count += (n-1)
print(count)


