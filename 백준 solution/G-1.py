n, m, k = map(int,input().split())
# 리스트 입력
data = list(map(int,input().split()))

data.sort() # 큰수 정렬하기
first =  data[n-1] # 큰 수
second = data[n-2] # 두번째로 큰수

result = 0

while True:
    # 6+6+6 
    for i in range(k):
        if m == 0:
            break
        result += first
        m -=1
    
    if m == 0:
        break

    # + 5
    result += second 
    m -= 1

print(result)