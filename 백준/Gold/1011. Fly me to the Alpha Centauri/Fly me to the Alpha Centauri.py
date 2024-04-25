T = int(input())

for _ in range(T):
    start, end = map(int,input().split())
    distance = end - start
    count = 0
    move = 1 # 현재 이동 가능 거리
    total = 0
    while total < distance:
        count += 1
        total += move
        if count % 2 == 0:
            move += 1

    print(count)