def flag(arr,equ):
    if arr[0][0]==arr[0][1]==arr[0][2]==equ:
        return True
    if arr[1][0]==arr[1][1]==arr[1][2]==equ:
        return True
    if arr[2][0]==arr[2][1]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][0]==arr[2][0]==equ:
        return True
    if arr[0][1]==arr[1][1]==arr[2][1]==equ:
        return True
    if arr[0][2]==arr[1][2]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][1]==arr[2][2]==equ:
        return True
    if arr[2][0]==arr[1][1]==arr[0][2]==equ:
        return True
    return False

while True:
    a = input()
    if a == "end":
        break

    else:
        xcnt = 0
        ocnt = 0
        index = 0
        arr=[[0]*3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                arr[i][j] = a[index]
                if a[index] == "X":
                    xcnt +=1
                if a[index] == "O":
                    ocnt += 1
                index += 1

        # 안되는 조건들 제외
        if xcnt > ocnt +1 :
            print("invalid")
            continue
        if ocnt > xcnt :
            print("invalid")
            continue

        if ocnt == xcnt:
            if flag(arr,"O") and not flag(arr,"X"):
                print("valid")
                continue

        if ocnt + 1 == xcnt:
            if flag(arr,"X") and not flag(arr,"O"):
                print("valid")
                continue

        ## 9칸이 다되었을때만 예외 (이부분 주의)
        if xcnt == 5 and ocnt ==4:
            if not flag(arr,"O"):
                print("valid")
                continue
            
        print("invalid")