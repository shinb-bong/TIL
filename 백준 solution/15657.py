# from itertools import combinations_with_replacement

# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# arr = combinations_with_replacement(arr,m)
# result = []
# for i in arr:
#     for j in i:
#         result.append(j)

# result.sort()

# for i in result:
#     for j in i:
#         print(j,end=" ")
#     print()

#----- 정렬이 안되어서 오답 판정 -------------
# 라이브러리 없이 해야할듯
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result = []

def dfs(k):
    # 높이가 같다면 탈출
    if k == m:
        print(' '.join(map(str,result)))
        return
    
    # 높이를 충족못했으면
    for i in range(n):
        # 첫번째 이거나 만약 2번째부터면 같거나 큰수부터
        if k == 0 or result[k-1] <= arr[i]:
            result.append(arr[i])
            dfs(k+1)
            result.pop()

dfs(0)


