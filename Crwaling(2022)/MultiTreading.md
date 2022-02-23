멀티 쓰레딩
---

```
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)
pool.map(작업시킬함수, 작업시킬리스트)
pool.close()
pool.join()
```

이때 close() join()은 작업을 끝내고 가져와라 이다.

실전 tip

- 수집 필요한 모든 URL을 리스트[ ] 자료에 담아둔다. 

- URL을 입력하면 수집 결과를 주는 함수를 만든다.

- 그거 두개를 동시에 멀티쓰레딩 map 함수에 집어넣어서 멀티 쓰레딩을 진행한다.
