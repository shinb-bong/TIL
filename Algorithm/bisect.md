bisect 파이썬 이분탐색 라이브러리
---

bisect_left(literable, value) : 왼쪽 인덱스를 구하기

bisect_right(literable, value) : 오른쪽 인덱스를 구하기

+ bisect_right - bisect_left를 통해서 특정의 몇개의 숫자가 있는지 알아낼 수 있다.


+ 장점 : 원소들이 정렬된 리스트에서 특정 범위 내에 속하는 특정 값의 개수를 구할 때 효과적이며 

시간복잡도 : logN을 가진다.


LIS bisect 구현
----

```
import bisect

x = int(input())
arr = list(map(int, input().split()))

answer = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:

        answer.append(arr[i])
    else:
        idx = bisect.bisect_left(answer, arr[i])
        answer[idx] = arr[i]

print(len(answer))
```