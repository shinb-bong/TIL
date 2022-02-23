time,formatting
---

1970년 1월1일 부터 지금까지 몇초나 흘렀는지 알려준다.

epoch time
```
import time
print(time.time())
```

시간형식 변환
```
import time
시간 = time.ctime(1610175600)
print(시간)
```
보기좋은 time
```
import time

시간 = time.localtime()

print(시간)
print(시간.tm_year)
print(시간.tm_mon)
print(시간.tm_mday)
```

```
import time
시간 = time.localtime()
time.strftime('%Y년 %m월 %d일', 시간)
print(시간.tm_year)
print(시간.tm_mon)
print(시간.tm_mday)
```

datetime 라이브러리

```
import datetime
시간 = datetime.datetime(2022, 10, 20)
print(시간)

# 현재시각
datetime.datetime.now()
```