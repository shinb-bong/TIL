N = int(input())

arr = [0]
for _ in range(N):
    arr.append(int(input()))
answer = set()

def dfs(first,second,num):
    first.add(num)
    second.add(arr[num])
    if arr[num] in first:
        if first == second: # 들어있는 걸로 돌아갔는데 같다면 부분집합
            answer.update(first)
            return True
        return False # 아니라면 이미 실패
    return dfs(first,second,arr[num])

for i in range(1,N+1):
    if i not in answer:
        dfs(set(), set(), i)

print(len(answer))
answer= list(answer)
answer.sort()

for i in answer:
    print(i)