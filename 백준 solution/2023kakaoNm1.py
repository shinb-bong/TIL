
def solution(today, terms, privacies):
    answer = []
    dic = dict()
    for i in terms:
        a,b = i.split()
        dic[a] = int(b)
    arr = list(map(int,today.split(".")))
    
    for idx, i in enumerate(privacies):
        a,b = i.split()
        y , m , d = map(int,str(a).split("."))
        m += dic[b]
        d -= 1
        if d == 0:
            m -=1
            d == 28
        while m > 12:
            y+=1 
            m -=12
        
        if arr[0] > y or (arr[0] ==y and arr[1] >m) or (arr[0] ==y and arr[1] ==m and arr[2] > d):
            answer.append(idx+1)
    
    
    return answer