n = input()
m = int(input())

arr = []
for _ in range(m):
    arr.append(str(input()))

cond = False
for i in range(26):
    tmp = ""
    for k in n:
        tmp += chr(((ord(k) -97 + i) % 26) + 97)

    for k in range(m):
        if arr[k] in tmp:
            print(tmp)
