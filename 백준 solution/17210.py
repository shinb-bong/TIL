import sys
n, m = map(int,sys.stdin.readline().rstrip().split())

dic = dict()
for _ in range(n):
    site , pwd= input().split()
    dic[site] = pwd

for _ in range(m):
    k = sys.stdin.readline().rstrip()
    print(dic[k])