n = int(input())

def recursion(arr,m):
    if len(arr) == m:
        op.append(arr[:])
        return

    arr.append(' ')
    recursion(arr,m)
    arr.pop()

    arr.append('+')
    recursion(arr,m)
    arr.pop()

    arr.append('-')
    recursion(arr,m)
    arr.pop()

for _ in range(n):
    op = []
    m = int(input())
    recursion([],m-1)
    
    for o in op:
        st = ''
        for i in range(m-1):
            st += str(i+1)+o[i]
        st += str(m)

        if (eval(st.replace(' ',''))) == 0: # 공백제거
            print(st)
    print()