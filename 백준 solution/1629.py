# 수가 커서 시간복잡도 초과나옴
# 분할 정복으로 풀어야함
import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())

def DC(a,b):
    if b == 1:
        return a % c
    
    temp = DC(a,b//2)

    if b% 2 == 0: 
        return temp * temp % c
    else:
        return temp * temp * a % c

print(DC(a,b))