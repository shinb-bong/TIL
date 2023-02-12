n ,k = map(int,input().split())
dic_num = dict()
dic_name = dict()
for i in range(1,n+1):
    name = input()
    dic_num[i] = name
    dic_name[name] = i

for _ in range(k):
    cond = input()
    if cond.isalpha():
        print(dic_name[cond])
    else:
        print(dic_num[int(cond)])