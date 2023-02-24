n = int(input())

dp = [0] * (n+1)
arr = [0] + list(map(int,input().split()))
dp[1] = arr[1]

# 전체를 본다.
for i in range(2,n+1):
    # 1부터 나까지 모두 비교한다.
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j] + arr[j])

print(dp[n])