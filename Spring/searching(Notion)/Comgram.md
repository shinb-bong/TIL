# BE

기술 스택:

postgresql

- 버전 14
    
    ```
    spring.datasource.url=jdbc:postgresql://localhost:5432/comgram
    spring.datasource.username=postgres
    spring.datasource.password=12345
    spring.datasource.show-sql=true
    spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
    ```
    

PostgreSQL 설치

[PostgreSQL 설치 한후 PostgreSQL 접속 까지 해보자! - 도라가이드](https://dora-guide.com/postgresql-install/)

연동 

[[Spring boot + JPA Hibernate ] Postgres 연동하기](https://velog.io/@_koiil/Spring-boot-JPA-Hibernate-Postgres-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0)

- psql comgram 으로 실행

---

KaKao JWT OAuth2 도움되었던 글

[스프링부트x리액트 '카카오 로그인 하기' (JWT+OAuth2) [2]](https://sudo-minz.tistory.com/78)

카카오톡 로그인까지 참고 문서

---

PostgreSQL 명령어

[PostgreSQL의 psql 사용법](https://www.bearpooh.com/138)

jwt 이론

[Spring Boot에서 JWT 사용하기](https://shinsunyoung.tistory.com/110)

jwt 프론트 백엔드 그림

[https://sudo-minz.tistory.com/7](https://sudo-minz.tistory.com/77)7

[단위 테스트에 Spring Securiy 인증 관련 어노테이션들 사용하기](https://shinsunyoung.tistory.com/94)

공식 연동 문서

[](https://www.baeldung.com/spring-security-5-oauth2-login)

**[Provider ID must be specified for client registration 'azure'?](https://stackoverflow.com/questions/71781499/provider-id-must-be-specified-for-client-registration-azure)**

⇒ 해결 방법: 우리나라의 네이버나 카카오톡은 아직 Provider가 제공이 되지않는다. 구글 같은 경우 제공

그래서 우리는 properties에 직접 provider를 지정해야한다.

카카오 로그인 API 공식 페이지

[애플리케이션 등록](https://docs.kakaoi.ai/kakao_i_agent/instance/application/)

스프링 마음에 드는 사이트

[Spring Boot에서 CORS 적용해보기](https://shinsunyoung.tistory.com/86)

bindingResult 에러 메시지 표시

[@Valid 를 이용해 @RequestBody 객체 검증하기](https://jyami.tistory.com/55)

메시지 error properties 만들기

[에러메세지 커스터마이징](https://programmingrecoding.tistory.com/32)

[Validation - 오류 코드와 메시지 처리 시리즈](https://velog.io/@seungju0000/Validation-%EC%98%A4%EB%A5%98-%EC%BD%94%EB%93%9C%EC%99%80-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%B2%98%EB%A6%AC-%EC%8B%9C%EB%A6%AC%EC%A6%88)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4aca9fd4-7f6d-4f4c-a2d6-9f331385b647/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a440049e-010e-4bda-b680-0e39d05a6ae3/Untitled.png)

[Been Validation - 에러 코드](https://velog.io/@seungju0000/Been-Validation-%EC%97%90%EB%9F%AC-%EC%BD%94%EB%93%9C)

 

Object Error 

[Been Validation - 오브젝트 오류](https://velog.io/@seungju0000/Been-Validation-%EC%98%A4%EB%B8%8C%EC%A0%9D%ED%8A%B8-%EC%98%A4%EB%A5%98)

2023 1.10

1. refresh 토큰 적용
2. follow 적용
3. [error.properties](http://error.properties) 적용

fetchResult deprecated

[QueryDsl) fetchResults()가 deprecated 된 이유](https://velog.io/@nestour95/QueryDsl-fetchResults%EA%B0%80-deprecated-%EB%90%9C-%EC%9D%B4%EC%9C%A0)

repository 획일화

[QueryDSL 공부 10 - Spring data JPA 에서 QueryDsl활용](https://ugo04.tistory.com/140)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/57624620-4615-4f8d-babe-d3e269ad0ae6/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0dc59eb7-d62c-4325-8a53-1a9011e41513/Untitled.png)

Optional

[[Java] Optional 사용법 및 예제](https://hbase.tistory.com/212)

Stream

[[Java] 스트림(Stream) 이란? 스트림과 컬렉션의 차이점 #내부반복 #외부반복](https://ksr930.tistory.com/237)

---

## 배포

백엔드 프론트 배포 

[Spring Security + JWT + React - 08. AWS EC2 Spring 백엔드 배포](https://velog.io/@juno0713/Spring-Security-JWT-React-08.-%EB%B0%B1%EC%97%94%EB%93%9C-%EB%B0%B0%ED%8F%AC)

postgresql 설치 완료 후 DB 커넥션 획득하여 백엔드 성공적으로 실행

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ba2bebe8-6695-48e2-97ad-a1ec56f578da/Untitled.png)

리눅스 재부팅 명령어

[냉정과 열정사이](https://psychoria.tistory.com/785)

Gradle 버전 확인 및 변경

[[IntelliJ] Gradle 버전 확인 및 변경](https://tychejin.tistory.com/388)

Postgresql AWS 설치

[](https://velog.io/@vnbm04/PostgreSQL)

배포때 —warning-mode all 

[빌드시 --warning-mode all 경고 없애기](https://aisi1004.tistory.com/842)

**Gradle 빌드 시 Execution failed for task ':test'. 에러 해결** 

[[Java] Spring Boot / Gradle 빌드 시 Execution failed for task ':test'. 에러 해결](https://a-half-human-half-developer.tistory.com/m/168)

postgresql 콘솔 명령어

[[PostgreSQL] 기본 명령어](https://rianshin.tistory.com/68)

---

오늘의 투두

1. 보안 관련 설정 새롭게 정립
2. 페이징
3. Repository 인스턴스화

---

jwt Bearer 꼭 써야하나? 라는 고찰과 실무 예시

[HTTP Authorization header에 Bearer와 jwt 중 무엇을 사용할까?](https://velog.io/@hyex/HTTP-Authorization-header%EC%97%90-Bearer%EC%99%80-jwt-%EC%A4%91-%EB%AC%B4%EC%97%87%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%A0%EA%B9%8C)

인텔리제이에서 ERD 생성

[[Intellij] Intellij에서 ERD 이쁘게 만드는 법](https://devlog-wjdrbs96.tistory.com/425)

Dto 범위에 대한 고찰

[DTO의 사용 범위에 대하여](https://tecoble.techcourse.co.kr/post/2021-04-25-dto-layer-scope/)

프로필과 게시물 사진 관련 고민

[SpringBoot 인스타그램 - 12 게시글 등록](https://velog.io/@jiandme/SpringBoot-%EC%9D%B8%EC%8A%A4%ED%83%80%EA%B7%B8%EB%9E%A8-12-%EA%B2%8C%EC%8B%9C%EA%B8%80-%EB%93%B1%EB%A1%9D)

좋은 참고 예시

[Spring Security + JWT + React - 05. 백엔드 - 게시판 제작: 게시판, 추천, 댓글](https://velog.io/@juno0713/Spring-Security-JWT-React-05.-%EB%B0%B1%EC%97%94%EB%93%9C-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EC%A0%9C%EC%9E%91-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EC%B6%94%EC%B2%9C-%EB%8C%93%EA%B8%80)

---

[에러 고찰 2023.1.16](https://www.notion.so/2023-1-16-ae7882d760b04d0cb7085979c66bc459)

---

fetch 조인 에러

[[QueryDSL] 에러 발생 - query specified join fetching, but the owner of the fetched association was not present in the select list](https://dazbee.tistory.com/84)

---

2022.01.17 Kakao를 제외한 Naver, Google 로그인 도입을 위한 Oauth2.0 리팩토링

참고사이트

[[Spring Boot] OAuth2 + JWT + React 적용해보리기](https://velog.io/@jkijki12/Spring-Boot-OAuth2-JWT-%EC%A0%81%EC%9A%A9%ED%95%B4%EB%B3%B4%EB%A6%AC%EA%B8%B0)

[](https://velog.io/@minjoon1324/SpringSecurity-Oauth2-with-JWTNaver-FaceBook-Kakao-Google)

네이버 API 공식 사이트 (파라미터 참고)

[네이버 로그인 개발가이드 - LOGIN](https://developers.naver.com/docs/login/devguide/devguide.md#3-3-1-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%ED%9A%8C%EC%9B%90%EC%9D%98-%ED%94%84%EB%A1%9C%ED%95%84-%EC%A0%95%EB%B3%B4)

구글 API 공식 사이트 등록

[Google Cloud Platform](https://console.cloud.google.com/apis/credentials/consent?project=evident-healer-375001)

프론트엔드 사용하지 않고 Oauth2.0 로그인 테스트 하는 법 

`[localhost:8080/login](http://localhost:8080/login)` 으로 직접 접속

![스크린샷 2023-01-17 오후 12.14.21.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/74ecd24e-194d-4e5a-be50-e7548ed9a916/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-01-17_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.14.21.png)

Redis를 써볼까 고민하는 문서

[[DB] Redis란 무엇일까? 간단하게 알아보기!](https://devlog-wjdrbs96.tistory.com/374)

인메모리 Nosql인 데이터베이스로 라고 생각하면 될듯한데,

사용할 곳은 리프레쉬 토큰 같이 빠르게 접근을 해야하는 항목에 적용하면 좋을 듯하다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6a7d87c3-686b-470d-836d-2380982b0853/Untitled.png)

경로 상황별 “/” 처리

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/904b2952-6e6a-4ce2-b2f1-2956384ff2ab/Untitled.png)

다음에 파일 저장을 하게된다면

외부 파일 저장소를 활용하느

[AWS S3](https://jforj.tistory.com/261) 를 활용하는 것이 좋을듯하다.

Mutipart + AWS

깃허브 토큰 인증 하는 법 (변경 사안)

[GitHub 토큰 인증 로그인 하기 - [오류 해결]: remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.](https://miracleground.tistory.com/entry/GitHub-%ED%86%A0%ED%81%B0-%EC%9D%B8%EC%A6%9D-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%ED%95%98%EA%B8%B0-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0-remote-Support-for-password-authentication-was-removed-on-August-13-2021-Please-use-a-personal-access-token-instead)

[error: failed to push some refs to 에러](https://sosoeasy.tistory.com/406)