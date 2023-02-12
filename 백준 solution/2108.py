# 수의 개수 
from collections import Counter

n = int(input())
# 수의 입력
arr = []
for _ in range(n):
  arr.append( int(input()) )

# 산술 평균
print(round(sum(arr)/n))

# 중앙 값
arr.sort()
print(arr[n//2])

# 최빈값
nums = Counter(arr).most_common()
if len(nums)> 1:
  if nums[0][1] == nums[1][1]:
    print(nums[1][0])
  else:
    print(nums[0][0])
else:
  print(nums[0][0])

print(arr[-1]-arr[0])
