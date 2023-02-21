from collections import deque
tc = int(input())
for _ in range(tc):
    cond = True
    command = input()
    k = int(input())
    if k == 0:
        input()
        if 'D' in command:
            print('error')
        else:
            print('[]')
        continue
    cnt = 0
    arr = deque(input()[1:-1].split(","))

    for i in command:
        if i == "R":
            if cnt == 0:
                cnt +=1
            else:
                cnt -=1
            continue
        try:
            if cnt == 0 :
                arr.popleft()
            else:
                arr.pop()
        except:
            print("error")
            cond = False
            break
    arr =list(arr)

    # 문자열 출력 **최적으로 수정**
    # 문자열은 바로 이어줄 문자열 ",".join(문자열) 가능
    if cond == True:
        result = []
        if cnt == 0:
            print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("["+",".join(arr)+"]")