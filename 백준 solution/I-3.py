input_data = input()

# 행
row = int(input_data[1])
#열 ord 함수 사용
column = int(ord(input_data[0])) - int(ord('a')) +1
count = 0

# 갈 수 있는 모든 방향 명시
steps = [(-2,-1),(-2,1),(-1,2),(-1,-2),(1,-2),(1,2),(2,-1),(2,1)]

for i in range(len(steps)):
    nx = column + steps[i][0]
    ny = row + steps[i][1]

    if nx < 1 or ny < 1 or nx > 8 or ny >8 :
        continue

    count +=1

print(count) 