from itertools import combinations

L, C = map(int,input().split())

arr = input().split()
# 서로 다른 L 개의 알파벳, 최소 한개의 모음 , 최소 두개의 자음
# 암호는 알파벳이 증가하는 순서

# C 문자가 주어졌을때 맞추기

com_arr = combinations(sorted(arr),L)

for com in com_arr:
    cnt1 = 0 # 자음
    cnt2 = 0 # 모음

    for a in com:
        if a in "aeiou":
            cnt2 += 1
        else:
            cnt1 += 1

    if cnt1 >= 2 and cnt2 >= 1:
        print("".join(com))