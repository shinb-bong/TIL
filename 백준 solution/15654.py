from itertools import permutations

n , m = map(int,input().split())
arr = list(map(int,input().split()))
k = list(permutations(arr,m))
k.sort()
for i in k :
    for j in i:
        print(j, end=" ")
    print()
# print(len(list(permutations(n,m))))