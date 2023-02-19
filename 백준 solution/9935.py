"""
stack을 문자열 대신 배열로 바꾸면 조금이라도 시간을 아낄 수 있습니다.

python의 문자열은 immutable로, 글자 하나를 뒤에 붙일지라도 새 문자열을 만들고 그대로 복사해넣는 과정을 거칩니다. 따라서 겉으로 보기엔 O(1) 같아도 실제로는 O(N)입니다.
"""

import sys

s = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()

while target in s:
    s = s.replace(target ,"")

if s:
    print(s)
else:
    print('FRULA')


#-----------
# 다른 사람풀이(하나씩 추가해주면서 마지막부터 target 길이만큼 빼서 같으면 다 빼버리기)
# 그다음 계속 이어붙이기
# for i in range(len(S)):
#     stack.append(S[i])
#     if ''.join(stack[-ex_len:]) == explosion_string:
#         for _ in range(ex_len):
#             stack.pop()
"""
    1. 입력문자열을 앞에서부터 차례차례 한 글자씩 스택에 push 합니다.
    2. 현재 글자가 폭발 문자열의 마지막 글자와 일치하면 
스택의 top부터 폭발문자열의 길이까지 확인하여 폭발문자열이 만들어지는지 확인합니다.
    3. 폭발문자열이 만들어진다면 만들어지는 폭발문자열을 스택에서 pop합니다.
    4. 1~3을 반복합니다.
    5. 문자열 순회를 마치고 스택이 비어있으면, FRULA를 출력, 비어있지 않다면 스택 속 문자열을 차례로 출력합니다.
"""

string = input()    # 전체 문자열
bomb = input()      # 폭발 문자열
 
lastChar = bomb[-1] # 폭발 문자열의 마지막 글자
stack = []
length = len(bomb)  # 폭발 문자열의 길이

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)
 