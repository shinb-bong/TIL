adr = list(input().split(':'))

if adr.count(''):
    while len(adr) > 8:
        del adr[adr.index('')] # ::로 넘어갔을 경우 제거
    while len(adr) < 8:
        adr.insert(adr.index(''), '0000') # 삽입해서 밀어내기

for i in range(8):
    if len(adr[i]) < 4:
        adr[i] = '0'*(4-len(adr[i])) + adr[i]

print(*adr, sep=':') # 출력