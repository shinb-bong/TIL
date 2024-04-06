def slope(x1,y1,x2,y2):
    return (y2-y1) / (x2-x1)

n = int(input())

buildings= list(map(int,input().split()))

result = 0

for idx,y1 in enumerate(buildings):
    x1 = idx +1

    # 오른쪽 보는 빌딩부터
    cur_slope_right = None
    count1 = 0

    for idx2 in range(idx+1,n):
        x2 = idx2 + 1
        y2 = buildings[idx2]

        slope_right = slope(x1,y1,x2,y2)

        if cur_slope_right is None or cur_slope_right < slope_right:
            cur_slope_right = slope_right
            count1 += 1
        
    cur_slope_left = None
    count2 = 0
    for idx2 in range(idx-1,-1,-1):
        x2 = idx2 +1
        y2 = buildings[idx2]
        slope_left = slope(x1,y1,x2,y2)
        if cur_slope_left is None or cur_slope_left > slope_left:
            cur_slope_left = slope_left
            count2 +=1 
        
    result = max(result,(count1 + count2))

print(result)


