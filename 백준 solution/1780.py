n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

rm = 0
rz = 0
rp = 0

# 개인적으로 분할 정복은 
# 1.어느정도의 양을 자를지 정한다.
# 2. 검사할 기준을 잡는다.
# 3. 새로 잘라진 위치에 대해서 재귀적으로 다시 확인한다.
# 4. 원하는 최종 결과값 계산을 진행한다.

def dfs(x,y,n):
    global rm,rz,rp
    check = paper[x][y] # 처음 종이 숫자
    for i in range(x, x+n):
        for j in range(y,y+n):
            if paper[i][j] != check:
                for k in range(3):# 3x3 범위를 재귀적 탐색
                    for l in range(3):
                        dfs(x+k *n//3, y+l*n//3, n//3) # 3*3으로 나눈 위치
                return
    
    if check == -1:
        rm += 1
    elif check ==0:
        rz +=1
    else:
        rp +=1

dfs(0,0,n)
print(f'{rm}\n{rz}\n{rp}')