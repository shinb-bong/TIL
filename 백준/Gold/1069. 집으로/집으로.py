import math
x,y,d,t= map(int,input().split())

# 출발은 X,Y 점프는 D, T
dist = (x**2 + y**2) ** 0.5

if dist >= d:
    ans = min(t*(dist//d) + dist%d, t * (dist//d) + t, dist ) # 이등변 삼각형으로 가는법을 몰랐다

else:
    ans = min(t+ (d-dist), 2 * t, dist)

print(ans)
