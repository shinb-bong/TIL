from collections import deque
import sys
input = sys.stdin.readline
tc = int(input())

# 모든 경우의 수 기록을 하며 찾기 하지만 앞부터 차근차근
for _ in range(tc):
    a ,b = map(int,input().split())
    q = deque()
    q.append((a,""))
    visited = [False] *10000

    while q:
        n , path =q.popleft()
        visited[n] = True
        # 탈출문
        if n == b:
            print(path)
            break
        
        # 각 역할마다 모두 반복
        # D
        tmp = (2*n)%10000
        if not visited[tmp]:
            q.append((tmp,path+"D"))
            visited[tmp] = True
        # 2
        tmp = (n-1)%10000
        if not visited[tmp]:
            q.append((tmp,path+"S"))
            visited[tmp] = True
        # 3
        tmp = (10*n+(n//1000))%10000
        if not visited[tmp]:
            q.append((tmp,path+"L"))
            visited[tmp] = True
            
        # 4
        tmp = (n//10+(n%10)*1000)%10000
        if not visited[tmp]:
            q.append((tmp,path+"R"))
            visited[tmp] = True