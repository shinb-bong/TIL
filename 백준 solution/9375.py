for _ in range(int(input())):
    n = int(input())
    dic = dict()
    for i in range(n):
        a , b = input().split()
        if b in dic:
            dic[b] +=1
        else:
            dic[b] =1
    answer = 1
    for x,y in dic.items():
        answer *= (y+1)
    
    print(answer-1)