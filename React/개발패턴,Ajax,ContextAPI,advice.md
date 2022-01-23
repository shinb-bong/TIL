개발 패턴
---
1. 서버 DB에 있는 게시물을 json형태로 보내줌
2. React로 html을 구성하고 접속시 ajax요청

시작하기전에 제일 먼저 실행되는 구문 여러개를 사용해도 되지만 위에서부터 차근차근 실행됨

Useeffect ( ()=>{a},[b]);  b에 있는게 변경될때만 구문이 실행됨.

Ajax
---
Ajax: 서버에 새로고침없이 요청 할 수 있게 도와줌
-	GET 서버에게 정보요청
-	POST 서버로 중요정보 전달

보통 axios 깔아서 사용함
Axios.get(‘GET요청할URL’);

    .then(()=>{ 요청성공시실행할코드 })
    .catch(()=>{ 요청실패시실행할코드 })

Context API 
---
하위 컴포넌트들이 상속받은 값을 props없이 사용가능함

Component 특징
---
1. Component 이름지으실 땐 영어대문자로 보통 시작함.
2. return () 안엔 태그들이 평행하게 여러개 들어갈 수 없다.
평행하게 여러개의 태그를 쓰고 싶으면 <div>로 묶어야함.아니면 의미없는 div를 쓰기 싫으시면 <> </> 이걸로 묶어도 된다.

map 함수 사용법 
---
Component 반복문

    {
    shoes.map((a,i)=>{ 
        return <Component shoes = {shoes[i]} I = {i} key = {i}/>
        });
    }

리스트 추가 
---

    […원래리스트,…새롭게 받아온 리스트] 

기능 개발 advice
---
1. 실행하자마자 정보를 받아오고 싶으면 당연히 useEffect에 넣어서 진행.

2. HTML 재랜더링이 필요한 변수들만 state로 만들고 나머지는 불필요한것들은 var 변수로 선언

3. 자주 쓰는 항목들은 컴퓨터가 재랜더링 할때 마다 메모리 재할당을 해줘야 하므로 변수로 저장

4. import 한게 정말 많다 그걸 바로 import해오면 사이트가 느려질수 있으므로 
얘네가 필요할때 사용해주세요~ 라는 명령어를 사용해주면 좋다.
<Suspense\>를 이용해서 로딩이 오래걸릴떄 띄워줄 안내문 같은걸 적어줄수도 있다.

5. PWA 기술까지 사용할려면 처음 프로젝트 생성할때 

    npx create-react-app <프로젝트명> –template cra-template-pwa    
라고 적어줘야 service-worker.js 까지 만들어줌

    5-1. 만약 안했더라면 새로운 프로젝트에 만들어서 파일 옮겨주고 index.js 차이점만 보안 나머진 라이브러리 설치도 다시해줘야함

    그후 serviceWorkerRegistration.register(); 로 바꾸면 끝

6.





