# # 당연히 시간 초과  100,000* 1024 * 1024
# import sys
# input = sys.stdin.readline
# n, m = map(int,input().split())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int,input().split())))

# for _ in range(m):
#     answer = 0
#     start_x, start_y , end_x, end_y = map(int,input().split())

#     for i in range(start_x-1,end_x):
#         for j in range(start_y-1,end_y):
#             answer += arr[i][j]

#     print(answer)


#--------------------
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp = [[0] for _ in range((n*n)+1)]
dp[0] = arr[0]

for i in range(1,n*n):
    dp[i] = arr[i//n][i%n] + dp[i-1]

for _ in range(m):
    answer = 0
    start_x, start_y , end_x, end_y = map(int,input().split())
    if start_x== end_x and start_y == end_y:
        print(arr[start_x-1][start_y-1])
        continue

    for i in range(start_x-1,end_x):
        answer += dp[end_y-1] - dp[start_y-2]
    
    print(answer)

# --- 힌트를 보고 그림으로 그려본 마지막 방법
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + data[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])