n  = int(input())

dp = [0,1]

for i in range(2,n+1):
    tmp = int(1e9)
    for j in range(1,int(i**(1/2))+1):
        tmp = min(tmp,dp[i- j**2 ])
    dp.append(tmp+1)

print(dp[n])
