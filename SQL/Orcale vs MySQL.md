MySQL의 장점
---

1. 용량 & 처리 
- 처리 속도가 빠르고 대용량 처리에 용이함

2. 접근성
- 구조가 간단하여 사용하기 좋음

3. 가격
- 오픈소스는 무료, 상업용은 유료

MySQL의 단점
---
1. 복잡한 쿼리는 성능저하
2. 트랜잭션 지원이 완벽하지 않음
3. 사용자 정의 함수의 사용이 쉽지 않고 유연하지 않다.


Orcale 장점
---

1. 관리 시스템
- 다수의 사용자가 동시에 접근 가능

2. 변화관리
변경 plan 을 작성하고 실제 구현하기 전에 변경 사항 효과를 볼 수 있음

3. 경고
- 오류 발생시 메일 및 계정에 알림

4. 분산처리

5. 용량 & 처리
- 고성능 트랜잭션 처리

Orcale의 단점
---

1. 비용적 부담이 크다
2. 초보자에게 어렵다
3. 높은 지원 하드웨어 사양이 필요


문법 차이(편의성을 위해 O, M으로 표현)
---

1. 시퀀스 사용함수

- O: 시퀀스명.NEXTVAL
- M: 시퀀스명.CURRVAL

2. 형 변환 방법
- O: TO_CHAR, TO_NUMBER
- M: CAST

3. 날짜 포맷 변환
- O: To_CHAR(writedate,'YYYYMMDD HH24MISS')
- M: DATE_FORMAT(writedate, '%Y%m%d%H%i%s')

4. 현재 날짜
- O: SYSDATE
- M: NOW()

5. 요일변환 숫자가 다름

    일 월 화 수 목 금 토

O: 1,2,3,4,5,6,7

M: 0,1,2,3,4,5,6

6. 문자열 합치기
- O: ||
- M: CONCAT()

7. 컬럼이 NULL일때 다른 문자로 표현해주는 방법이 다름
- O: NVL
- ML IFNULL

8. 페이징 방식이 다름
- O:
```
SELECT * FROM (SELECT ROWNUM, A * FROM (SELECT * FROM DEPT) A) WHERE ROWNUM BETWEEN 0 AND 10;
```

- M:
```
SELECT * FROM DEPT LIMIT 0,10;
``` 


