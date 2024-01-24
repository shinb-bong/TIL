create tabel nodejs.comments(
    id, int not null primary key auto_increment,
    commenter int not null,
    comment varchar(100) not null, -- 댓글
    created_at datetime not null default now(),

    index commenter_idx(commenter ASC),
    constraint commenter foreign key(commenter) references nodejs.users(id) on delete cascade on update cas\
)
    comment = "댓글" -- 테이블 설명
    default charset = utf8mb4 -- 이모티콘 처리를 위한 인코딩
    engine = InnoDB;


-- with 사용 x

select job, sum(sal)
from emp
group by job
having sum(sal) > (select avg(sum(sal)) from emp group by job);


-- with 사용 ㅇ view 와 다른점은 메모리를 할당 받는다/ 테이블임

with eee as 
(
    select job,sum(sal) as total
    from emp
    group by job
)

select job, total
from eee
where total (select avg(total) from eee);

-- commit하면 사라지는 임시테이블 emp_temp 를 만드시오

create global temporary table emp_temp
on commit delete rows
as 
(
    select * 
    from emp
    where 1=2; -- table의 틀만 가져가고 싶음
)

-- h 컬럼이 초기값 1부터 제어문에 합당하는 5까지의 데이터를 갖는 가상의 테이블 생성

with recursive rc as (
    select 1 as h -- 재귀 초깃값
    union all
    select h+1 -- 재귀
    from rc
    where h < 5 -- 재귀 정지조건
)

select * from rc

with recursive rc as (
    select 0 as hour
    union all
    select hour+1 from rc where hour<23
)

select 
    rc.hour, 
    count(hour(A.datetime)) as count
from rc
left join animal_ins as A
on rc.hour = hour(A.datetime) -- 재귀숫자와 datetime시간숫자가 같은것 만
group by rc.hour -- 집계함수를 썼으니 그룹핑, 안그러면 다 더해서 레코드 하나만 반환


-- 트랜잭션 사용 (DDL은 transaction의 롤백의 대상이 아니다.)
START TRANSACTION; -- 트랜잭션 시작

select * from members; -- 초기 상태 보여줌
insert into members values(1, '쿠', '크다스', '크라운제과' '?', '대한민국'); -- 데이터 수정
select * from members; -- 수정 상태 보여줌

COMMIT -- 트랜잭션을 DB에 적용

select * from members; -- 적용된 결과 조회


-- root 권한으로 mysql 콘솔 실행
$ mysql -u root -p

-- 유저 추가
create user userid@localhost identified by 'password';

-- 모든 권한 부여
GRANT ALL PRIVILEGES ON *.* TO '계정 아이디'@'localhost' WITH GRANT OPTION;

-- 테이블 구조 확인
explain 테이블명;


-- 서브쿼리는 괄호를 통해 사용
select name, height 
from userTbl
where height > (select height from userTbl where name in ('김경호'));

-- left 조인의 주의점 
-- 행의 갯수가 달라질 수 있으므로 N을 잡는다. 또한, LEFT JOIN으로 시작을 했다면
-- 나머지 조인도 LEFT JOIN을 이어간다.

-- UNION은 DISTICT 자동 포함 => 지우고 싶으면 UNION ALL 사용

-- 서브쿼리는 복잡한 SQL 쿼리문에 많이 사용된다.
-- 최근 MySQL은 서브쿼리문을 조인문으로 변환해주지만 남용은 금물

-- 조인으로 서브쿼리 대체 불가
-- Group by 사용한 서브 쿼리가 FROM 에 있을때, ALL, 함수 안에 사용되고 있을때
SELECT city, sum_price
FROM
( 
  SELECT city, SUM(price) AS sum_price 
  FROM sale
  GROUP BY city -- group by 를 쓴 스칼라 서브쿼리
) AS s
WHERE sum_price < 2100;

-- EXISTS 는 조건이 맞는지 TRUE, FALSE 만 판단하기 때문에 만족하는 결과가 하나가 나오면 TRUE판단 

-- EXISTS는 메인쿼리 -> EXISTS 쿼리 /IN은 IN쿼리 -> 메인쿼리
select dept_id, dept_name
from 부서
where exists ( select 1 from 사원 where 사원.dept_id = 부서.dept_id )
-- 부서의 dept_id가 사원의 dept_id에 1개라도 존재하면 true
-- 따라서 dept_id가 동일한 사원 레코드를 만나면 더이상 탐색할 필요가 없어진다. (지연 평가)

-- MYSQL 은 세이프 모드가 자동
-- 환경 변수를 통해 해제 가능 

set SQL_SAFE_UPDATES = 0;  -- disable safe mode

delete from table where num > 1;

set SQL_SAFE_UPDATES = 1;  -- enable safe mode

-- 클러스터 인덱스 생성 
ALTER TABLE mixedtbl
ADD CONSTRAINT PK_mixedtbl_userID PRIMARY KEY (userID);

-- 클러스터 보조 인덱스 생성
ALTER TABLE mixedtbl
ADD CONSTRAINT UK_mixedtbl_name UNIQUE (name);

-- INDEX 손익 분기점 
-- 테이블이 가지고 있는 전체 데이터양의 10%~15%이내의 데이터가 출력 될때만
-- INDEX 가 이득이다. 그 이상은 풀스캔이 빠르다
CREATE TABLE books (
  -- 같이 지정
  id varchar(5) primary key, -- 기본키 지정 (클러스터 인덱스)
  name varchar(20) unique, -- 인덱스 생성 (보조 인덱스) (중복 비허용)
  writer varchar(20) NOT NULL,
  
  INDEX idx_test (writer asc) -- 인덱스 생성 (보조 인덱스)
);

CREATE INDEX 인덱스명 ON 테이블명 (컬럼명); -- 보조 인덱스 생성 (중복 허용)

-- 인덱스 제거시 보조 인덱스 부터 삭제하고 클러스터 인덱스를 삭제하도록한다.
ALTER TABLE 테이블이름
DROP PRIMARY KEY; -- 만일 외래키와 연결이 되어있을 경우 제약조건에 의해 삭제가 안될수 있음

-- 따라서 먼저 외래키를 삭제 후 클러스터 인덱스 (primary key)를 삭제 하면 됨

-- 먼저 외래키명을 얻어서 (constraint_name)
select table_name, constraint_name
from information_schema.referential_constraints
where constraint_shcema = 디비명

alter table 테이블2 drop foreign key 외래키명; -- 외래키 삭제
alter table 테이블 drop primary key; -- 클러스터 인덱스 삭제

-- 풀텍스트인덱스는 중간의 단어나 문장으로도 인덱스를 생성해줌(MYSQL)의 부가적인 기능
-- char, varchar, text타입만 가능함
CREATE TABLE 테이블이름(
  …,
  열이름 데이터형식,
  …,
  FULLTEXT 인덱스이름 (열이름)
);

-- 풀텍스트인덱스 사용시에는 특수한 메소드를 사용해야함.
SELECT * FROM newspaper WHERE MATCH(article) AGAINST('영화');

SELECT * FROM newspaper WHERE MATCH(article) AGAINST('영화' in natural language mode);

SELECT * FROM newspaper WHERE MATCH(article) AGAINST('영화 배우'); 
-- ‘영화’ 또는 ‘배우’ 두 단어 중 하나가 포함된 기사 검색.
-- 정확히 영화 인것만 검색

-- 이를 해결하기 위해 불린 모드 검색 사용
-- 불린 모드 검색은 필수인 +, 제외하기 위한 -, 부분 검색을 위한 * 연산자 등의 다양한 연산자를 지원한다
-- '영화' 가 앞에 들어간 모든 결과 검색 

-- ex) 영화가 영화는 영화를
select * from newspaper
where match(article) against ('영화*' in boolean mode);


-- 정확히 '영화 배우' 단어가 들어있는 기사 내용 검색
select * from newspaper
where match(article) against('영화 배우' in boolean mode);


-- '영화 배우' 단어가 들어 있는 기사 중에서 '공포' 내용이 들어간 결과
select * from newspaper
where match(article) against('영화 배우 +공포' in boolean mode);


-- '영화 배우' 단어가 들어 있는 기사 중에서 '남자' 내용은 검색에서 제외
select * from newspaper
where match(article) against('영화 배우 -남자' in boolean mode);

-- mysql은 기본값으로 검색 가능 단어가 3
-- 몇 글자 이상부터 검색 가능한지 확인
SHOW VARIABLES LIKE 'innodb_ft_min_token_size';

-- 하지만 전체 텍스트 인덱스는 양이 많다.
-- 굳이 검색이 필요없는 것은 중지 단어로 넣어서 적용 가능
--db와 테이블 이름은 소문자 써야된다.
set global innodb_ft_aux_table = '디비명/테이블명';


--테이블에서 만들어진 전체텍스트 인덱스 보기 (필요없는 검색 단어가 있음)
select word, doc_count, doc_id, position from information_schema.innodb_ft_index_table ;

-- 중지단어 만들기전에 만들어놓은 풀텍스트 인덱스는 삭제
drop index idx_all on FulltextTbl ;


-- 중지단어를 위한 테이블 만들기
-- 테이블의 데이터는 반드시 value , 타입은 varchar -> 약속
CREATE TABLE user_stopword (value VARCHAR(30));


--중지 단어 만들기
insert into user_stopword values ('그는'), ('그리고'), ('극에') ; 


-- 중지 단어 테이블에 지금 만들 테이블을 추가하는 작업
-- 그러면 이제 user_stopword 테이블에 들어있는 단어로는 풀텍스트 인덱스를 만들지 않게 된다
set global innodb_ft_server_stopword_table = '디비명/user_stopword'; -- 모두 소문자


-- 만든 테이블이 들어갔는지 확인
show global variables like 'innodb_ft_server_stopword_table' ;


-- 중지단어 테이블 만들었으니, 이제 다시 풀텍스트 인덱스 생성.
create Fulltext index idx_description on FulltextTbl ( description );


-- 그러면 중지단어에 등록한 단어를 제외한 인덱스 단어들이 생성됨 (갯수가 줄어들음)
select word, doc_count, doc_id, position 
from information_schema.innodb_ft_index_table ;


-- 상품 이미지 같은 경우는 역정규화를 통해 배열 저장
-- 이럴땐 json을 사용
const arr = ['Apple', 'Banana', 'Orange']; 

let data = JSON.stringify(arr); // '["Apple","Banana","Orange"]' // 배열 문자열

let data2 = JSON.parse(data); // ['Apple', 'Banana', 'Orange'] 배열 자료형

-- json을 자료형으로 쓰지 않는것은 쿼리 성능 자체는 그냥 스트링 타입을 쓰는것이 좋음
CREATE TABLE example (
  `id` int NOT NULL AUTO_INCREMENT,
  `docs` JSON, -- json 타입 필드
  PRIMARY KEY (`id`)
);

INSERT INTO example (docs) VALUES ('["hot", "cold"]'); -- 배열 문자열을 저장
-- 그러면 배열이 테이블에 들어가게 된다.