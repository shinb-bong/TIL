n = int(input())

arr = map(int,input().split())

m = int(input())
find = map(int,input().split())

result = dict()
for i in arr:
    if i in result:
        result[i] +=1
    else:
        result[i] = 1


for i in find:
    if i in result:
        print(result[i],end=" ")
    else:
        print(0,end= " ")