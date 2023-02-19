# # 오답

# from collections import deque

# r,c,t = map(int,input().split())

# # 위치 받아오기
# arr = []
# for _ in range(r):
#     arr.append(list(map(int,input().split())))

# # 무조건 첫번째 줄이면서 체크
# air = []
# for j in range(r):
#     if arr[j][0] == -1:
#         air.append(j)
# visited = [[False]*c for _ in range(r)]        

# # 의사코드 
# # 초만큼 반복
# # 1차적으로 미세먼지를 퍼트린다 
# # 2차적으로 옮겨준다.

# def bfs(x,y,visited):
#     q = deque()
#     q.append((x,y))
#     dx = [-1,1,0,0]
#     dy = [0,0,1,-1]
#     visited[x][y] = True
#     while q :
#         a,b =q.popleft()
#         cnt = 0
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             # 범위안, 방문 안했고,공기청정기가 아닌데
#             if 0<= nx < r and 0<=ny <c and visited[nx][ny] == False and arr[nx][ny]!= -1:
#                 cnt +=1 
#                 visited[nx][ny] = True
#                 arr[nx][ny] += arr[a][b]//5
#                 q.append((nx,ny))
        
#         arr[a][b] = arr[a][b] - (arr[a][b]//5)*cnt

# def clean_up():
#     for i in range(air[0]):
#         for j in range(c):
#             if arr[air[0]][0]:
#                 continue
#             if j == 0:
#                 arr[i][j] = arr[i-1][j]
#             elif i == 0:
#                 arr[i][j] = arr[i][j+1]
#             elif i == air[0]-1:
#                 arr[i][j] = arr[i][j-1]
#             elif j == c-1:
#                 arr[i][j] = arr[i-1][j+1]
#     arr[air[0]][0] = -1
#     arr[air[0]][1] = 0

# def clean_down():
#     for i in range(air[1],r):
#         for j in range(c):
#             if arr[air[1]][0]:
#                 continue
#             if j ==0:
#                 arr[i][j] = arr[i+1][j]
#             elif i == air[1]:
#                 arr[i][j] = arr[i][j-11]
#             elif i == r-1:
#                 arr[i][j] = arr[i][j+1]
#             elif j == c-1:
#                 arr[i][j] = arr[i][j-1]
#     arr[air[1]][0] = -1
#     arr[air[1]][1] = 0

# # 의사코드 구현
# # 원하는 시간초 만큼 진행
# for _ in range(t):
#     # 우선 먼지 확산
#     for i in range(r):
#         for j in range(c):
#             if arr[i][j] != -1:
#                 bfs(i,j,visited)

#     clean_up()
#     clean_down()
#     visited = [[False]*c for _ in range(r)]   

# answer = 0
# for i in range(r):
#     for j in range(c):
#         if arr[i][j] > 0:
#             answer += arr[i][j]

# print(answer)



# #-------------------------------
# # 정답
# # 1.방향성을 잘못잡았음
# # 2. 추가적으로 한개의 리스트에 작업을 해서 중복 작업이 되었음
# # 3. 구현, 시뮬레이션은 문제를 이해하고 차근차근 코드가 길어져도 풀어내는 연습을 해야할듯함.

import sys
input = sys.stdin.readline

r,c,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(r)]

up = -1
down = -1

#공기 청정기 위치
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

def spread():
    dx = [-1,0,0,1]
    dy=  [0,-1,1,0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            # 아무것도 없거나 공기청정기가 아니라면
            if arr[i][j] != 0 and arr[i][j] != -1:
                tmp = 0 # 확산장소 빼줄 값
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                # 위치 안이면서 공기청정기가 아니라면
                    if 0<= nx <r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] //5
                        tmp += arr[i][j] //5
                arr[i][j] -= tmp
    # 이렇게해주는 이유는 
    # 미리 그래프에 반영해버리면 다른 것들이 반영된거에 추가업데이트 될수 있음
    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j] 

# 위로 돌기
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    # 공기청정기 기준으로 시작
    direct = 0
    before = 0 
    x,y = up,1 # 공기 청정기 위치 옆부터 시작
    while True:
        nx = x + dx[direct] # 우로 이동 시작
        ny = y + dy[direct]
        # 공기청정기로 돌아오면 끝/ 탈출문
        if x == up and y == 0: 
            break
        # 만약 가던 방향에서 범위를 벗어났다면 
        # 방향 비틀기
        if nx<0 or nx >= r or ny <0 or ny >= c:
            direct += 1
            continue
        # 전값 넣어주고 이어서 계속(처음에는 청정된 공기가 들어오니깐 0)
        arr[x][y] , before = before, arr[x][y]
        # 계속 진행
        x= nx
        y= ny
        

def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    #무조건 돌아서 온다는게 보장
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny   

# 시간만큼 돌리고
for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            answer += arr[i][j]

print(answer)