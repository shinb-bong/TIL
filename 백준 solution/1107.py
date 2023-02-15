# n = input()
# length = len(n)
# n = int(n)
# m = int(input())
# error = list(map(int,input().split())) if not m == 0 else []
# right = [i for i in range(10) if not i in error]
# number = n

# cnt = 0
# tmp = 0
# for i in range(length-1, -1,-1):
#     k = number // 10**i
#     if (n-tmp) // (10**(i+1))>0:
#         tmp += max(right)*(10**i)
#     else:
#         if k in right:
#             tmp += k * (10**i)
#         else:
#             target = 10
#             small =0
#             for s in range(len(right)):
#                 if target >= abs(k-right[s]):
#                     small = s
#                     target = abs(k-right[s])
#             tmp += right[small] * (10**i)
        
#     number = number % (10**i)

# if 98<=n <=102:
#     print(abs(100-n))
# else:
#     print(length+abs(n-tmp))
import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
errors = list(map(int,input().split()))

# +,- 로 이동할 경우를 디폴트
min_cnt = abs(100-target)

for nums in range(1000000):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인
        if int(nums[j]) in errors:
            break
        # 고장난게없으면
        elif j == len(nums) -1:
            min_cnt = min(min_cnt,abs(int(nums)-target)+ len(nums))
    
print(min_cnt)