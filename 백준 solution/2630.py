n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

blue, white = 0 ,0

def check(row,col,n):
    global blue, white
    pos = arr[row][col]
    for i in range(row, row+n):
        for j in range(col,col+n):

            if pos != arr[i][j]:
            # 길이를 절반으로
                next_n = n // 2

                # 새롭게 잘라서 만드는 과정
                check(row,col,next_n) # 1사분면
                check(row,col + next_n,next_n) #2
                check(row+ next_n,col,next_n) # 3
                check(row+ next_n,col+ next_n,next_n) #4
                return 
    # 더이상 안잘라도될 때 
    if pos == 0:
        white += 1
    else:
        blue += 1
    return 

check(0,0,n)
print(white)
print(blue)
        
