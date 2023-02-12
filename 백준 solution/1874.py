import sys
input = sys.stdin.readline
n = int(input())

stack = []
answer = []
cond = True
cnt = 1 # push 할때 기록
for i in range(n):
    k = int(input())
    while cnt <= k :
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    if stack[-1] == k:
        stack.pop()
        answer.append('-')
    else:
        cond = False
if cond == False:
    print("NO")
else:
    for a in answer:
        print(a)
            

            

