import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

if n == 1:
    print('A')

elif n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print('A')

else:
    if arr[0] == arr[1]:
        a = 0
    else:
        a = (arr[2]-arr[1]) // (arr[1] - arr[0])

    b = arr[1] - arr[0] * a 

    flag = False
    for i in range(n-1):
        next_val = arr[i] * a + b
        if (arr[i+1] != next_val):
            flag = True
            break


    print(arr[-1]* a + b if flag == False else 'B')  
