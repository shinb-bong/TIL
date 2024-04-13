import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

arr = [[[0,[True,True]] for _ in range(m+1)] for _ in range(n+1)]

arr [0][0][0] = 1

for _ in range(k):
    a,b,c,d = map(int,input().split())
    if a > c: 
        a,c = c,a
    if b > d:
        b,d = d,b
    # 이제 위로나 옆으로 못가는 경우밖에 없음
    if c-a > d-b:
        d = 0
    else: 
        d = 1
    # arr[a][b] 는 좌표
    # 0은 횟수 
    # 1은 못가는 갈수 있는 방향
    arr[a][b][1][d] = False
    # 어차피 위로아니면 오른쪽 밖에 없음

moves = [(1,0),(0,1)]
for x in range(n+1):
    for y in range(m+1):
        for i in range(2):
            nx, ny = x + moves[i][0], y + moves[i][1]
            if nx <= n and ny <= m and arr[x][y][1][i]:
                arr[nx][ny][0] += arr[x][y][0]

print(arr[n][m][0])
