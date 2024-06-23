n,m = map(int,input().split())

books = list(map(int,input().split()))

left = []
right = []

for item in books:
    if item < 0:
        left.append(item)
    elif item > 0:
        right.append(item)

distance = []

# 음수쪽 계산
left.sort()
for i in range(len(left)//m):
    distance.append(abs(left[m*i]))

# 하나만 챙기면 그 이후껀 m이하라 다 챙김
if len(left) % m > 0:
    distance.append(abs(left[(len(left)//m) * m]))

right.sort(reverse=True)
for i in range(len(right)//m):
    distance.append(right[m*i]) 
if len(right) % m > 0:
    distance.append(right[(len(right)//m)*m])   

distance.sort()
result = distance.pop()
result += 2*sum(distance)
print(result)