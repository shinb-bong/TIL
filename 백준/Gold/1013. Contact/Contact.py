import re
import sys

T = int(sys.stdin.readline())
results = []

for _ in range(T):
    sign = sys.stdin.readline().replace('\n', '')
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)
    if m: results.append("YES")
    else: results.append("NO")

for result in results:
    sys.stdout.write(str(result)+'\n')