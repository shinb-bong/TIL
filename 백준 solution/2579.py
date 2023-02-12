n = int(input())
arr= []
dp = [0] * n
for _ in range(n):
    arr.append(int(input()))
if n <=2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[1] + arr[0]
    dp[2] = max(arr[1]+arr[2], arr[0]+arr[2])
    for i in range(3,n):
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

    print(dp[n-1])