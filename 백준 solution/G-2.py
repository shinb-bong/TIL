n, m ,k = map(int,input().split())

# 리스트 입력 받기
data= list(map(int,input().split()))
data.sort()

first = data[n-1]
second = data[n-2]
#예시 6+6+6+5 6+6+6+5  => (K+1)

count = int(m / (k+1)) * k  # 큰수가 나오는 만큼
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)