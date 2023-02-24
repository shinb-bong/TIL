n = int(input())

result = 0
row = [0] * n
def is_okay(x):
    for i in range(x):
        #같은 열 or 대각선 있는지 판별
        # 그리고 N * N을 놓는것 자체가 한줄에 무조건 한개씩
        # 놓는거임
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False

    return True


def n_queen(x):
    global result
    # 판에 놓은 말의 수가 명시된 수와 같다면
    if x == n:
        result  +=1

    else:
        for i in range(n):
            row[x] = i
            # 지금 놓은 판의 퀸이 괜찮은지
            if is_okay(x):
                n_queen(x+1)

n_queen(0)
print(result)

