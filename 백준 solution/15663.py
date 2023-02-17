# # 라이브러리 사용
# from itertools import permutations
# n, m = map(int,input().split())
# arr = list(map(int,input().split()))
# result = set()
# for i in permutations(arr,m):
#     result.add(i)

# result = list(result)
# result.sort()
# for i in result:
#     print(" ".join(map(str,i)))

# 백트래킹
n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False] * n
result = []

def dfs(k):
    if k ==m:
        print(' '.join(map(str,result)))
        return
    # 바로 전 숫자
    prev = 0
    # 다시 전체를 돌면서
    for i in range(n):
        if not visited[i] and prev!= arr[i]: # 오름차순이기 때문에 전이랑 같지만 않으면 성공
            visited[i] = True
            result.append(arr[i])
            prev = arr[i]
            dfs(k+1)
            visited[i] = False
            result.pop()


dfs(0)


