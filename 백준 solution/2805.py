n ,k = map(int,input().split())

arr = list(map(int,input().split()))
answer = 0

start = 0
end = max(arr)
while(start <= end):
    total= 0
    mid = (start + end) //2
    for i in arr:
        if i > mid:
            total += (i-mid)
            
    if total < k :
        end = mid -1
    else:
        answer = mid
        start = mid+1
print(answer)
     
