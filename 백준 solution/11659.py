# # 시간 초과 예상 코드 100,000 * 100,000
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# for _ in range(m):
#     a,b = map(int,input().split())
#     print(sum(arr[a-1:b]))
# 구간합 
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
dp =  [0 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i] = dp[i-1]+ arr[i-1]

for _ in range(m):
    a,b = map(int,input().split())
    print(dp[b]-dp[a-1])
