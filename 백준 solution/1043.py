import sys
input = sys.stdin.readline
n, m = map(int,input().split())

arr = set(map(int,input().split()[1:]))

party = []
for _ in range(m):
    party.append(list(map(int,input().split()))[1:])
answer = 0


# 거짓말쟁이 판별(증식)
for _ in range(m):
    for i in range(m):
        for j in list(arr):
            if j in party[i]:
                arr.update(party[i])

for i in range(m):
    cond = True
    for j in list(arr):
        if j in party[i]:
            cond = False

    if cond:
        answer +=1

print(answer)

# 끝나고 회고
# for _ in range(m):
#     for party in parties:
#         if party & knowList:
#             knowList = knowList.union(party)
# 이렇게 set 과 set의 합집합으로 풀어낸 좋은 방법도 있었다.
#결국은 파티를 다 돌고 한번 더 검사한 내 풀이도 맞지만