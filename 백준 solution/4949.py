
while True:
    n = input()
    if n == ".":
        break
    arr = []
    cond = True
    for i in n:
        if i== "(" or i== "[":
            arr.append(i)
        if i== ")":
            if not arr or arr[-1] == '[':
                cond = False
                break
            elif arr[-1] == '(':
                arr.pop()
        if i== "]":
            if not arr or arr[-1] == '(':
                cond = False
                break
            elif arr[-1] == '[':
                arr.pop()

    if cond == True and len(arr) == 0 :
        print("yes")
    else:
        print("no")
