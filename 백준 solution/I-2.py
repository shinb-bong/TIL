from turtle import st


n = int(input())

count  = 0

# 총 개수가 작기 때문에 N^3 시간복잡도가 가능함.
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+ str(j)+ str(k):
                count += 1


print(count)