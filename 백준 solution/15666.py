from itertools import product
n, m = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))

result = []
def dfs(k):
    if k ==m :
        print(" ".join(map(str,result)))
        return

    for i in range(len(arr)):
        if k == 0 or result[-1] <= arr[i]:
            result.append(arr[i]) # 넣고 깊이 탐색을 한다.
            dfs(k+1)    # 깊이 탐색 진행 (만약 원하는 단계까지 갈경우 멈춤)
            result.pop() # 그럼 다시 방금 넣었던 요소를 빼고 새로운 수에 for문 계속 도전

dfs(0)

