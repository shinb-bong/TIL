최빈값(mode)를 구하기 위해서 collections 모듈의 Counter 클래스를 알고 있어야 한다. 


```
from collections import Counter

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
cnt = Counter(colors)
cnt

>>> Counter({'blue': 3, 'red': 2, 'green': 1})

```

.most_common() 메소드를 등장한 횟수를 내림차순으로 정리해준다.
```
>>> numbers = [1, 2, 3, 3, 4, 4, 4, 5, 5] 
>>> from collections import Counter 
>>> cnt = Counter(numbers) 
>>> cnt.most_common() [(4, 3), (3, 2), (5, 2), (1, 1), (2, 1)]

```

이제 여기서 list에서 인덱싱을 해서 원하는 정보를 꺼내오면 된다.