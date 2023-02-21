# sql

```
-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서 대여 기록 별로 대여 금액(컬럼명: FEE)을 구하여 대여 기록 ID와 대여 금액 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬해주세요.SELECT HISTORY_ID,
ROUND(CASE
      WHEN HIS.DURATION < 7 THEN REN.DAILY_FEE * HIS.DURATION

      WHEN HIS.DURATION < 30 THEN REN.DAILY_FEE * HIS.DURATION *
                            (SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '7일 이상')

      WHEN HIS.DURATION < 90 THEN REN.DAILY_FEE * HIS.DURATION *
                            (SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '30일 이상')

      ELSE REN.DAILY_FEE * HIS.DURATION *
                            (SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '90일 이상') END) FEE

FROM (SELECT HISTORY_ID,CAR_ID,(DATEDIFF(END_DATE,START_DATE)+1) DURATION
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) HIS
JOIN CAR_RENTAL_COMPANY_CAR REN
ON HIS.CAR_ID = REN.CAR_ID
WHERE REN.CAR_TYPE = '트럭'
ORDER BY FEE DESC,HISTORY_ID DESC;
```

이렇게 새로운 테이블을 만들어서 join 하여 구할 수있고

```
SELECT T1.ID, T1.NAME, T1.HOST_ID
FROM PLACES T1 JOIN (SELECT ID,HOST_ID,COUNT(*) AS 'COUNT' FROM PLACES GROUP BY HOST_ID) T2 ON T1.HOST_ID = T2.HOST_ID
WHERE T2.COUNT > 1
ORDER BY T1.ID
```

나처럼

`SELECT ID,NAME,HOST_ID
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID
FROM PLACES
GROUP BY HOST_ID
HAVING COUNT(HOST_ID) >= 2)`

이렇게 서브쿼리를 사용하여 in절로 구할수도 있다.

조건을 한번 명시하고 필터링을 해서 1차적으로 주어진 조건을 구한뒤

다시 한번 추가 조건들을 필터링한다.

----
<노션 정리 재업로드> 

여기서는 1차적으로 5번 이상 빌린 차량들에 대해 조사를 하고 

그 이후 조건인 해당 기간에 빌린 내용에 대한 이라는 문장을 새롭게 날짜 조건절을 넣어 처리했다. 

그리고 자연스럽게 GROUP BY 에 MONTH가 들어가면서 빌린 달 이없으면 조회가 되지 않는다.

여기서 헷갈린 요인은 GROUP BY 에서는 두 개의 항목이 들어가도 상관이 없다. 

그리고 select에서 사용한 aslias 를 사용해도 상관없다.