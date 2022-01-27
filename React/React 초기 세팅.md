React 초기 세팅
---

1. Node.js 최신 버전 설치
2. npx create-react-app <앱명>
3. npm start // 서버 미리보기

중요한 변수 설정 
----

중요한 변수나 변경이 있을 변수는 
useState문법을 사용

    let [글제목, 글제목변경] = useState('남자 코트 추천');

처럼 [변수명,변수변경메소드]로 선언해줍니다. 

Component
---

    function Modal(){
    return (
        <div className="modal">
        <h2>제목</h2>
        <p>날짜</p>
        <p>상세내용</p>
        </div>
    )
    }

+ return안에는 무조건 한개의 div 태그로 해야한다. 그래서 <> </>로 묶어주는것도 방법임

Map
---
    { 글제목.map(function(a){
        return (
        <div className="list">
          <h3  onClick={ ()=>{ 따봉변경(따봉+1) } }>{ a }</h3>
          <p>2월 18일 발행</p>
          <hr />
        </div>
      }) }

+ map 함수 앞에 있는 변수 만큼 반복을 수행하며 해당 차례에 있는 값은 a로 들어가게됨.

import, export
---
    // import 하고 싶은 js
    import { name1, name2 } from './data.js';

    // export 하고 싶은 js
    export default [
    {
        id : 0,
        title : "White and Black",
        content : "Born in France",
        price : 120000
    },

    {
        id : 1,
        title : "Red Knit",
        content : "Born in Seoul",
        price : 110000
    },

    {
        id : 2,
        title : "Grey Yordan",
        content : "Born in the States",
        price : 130000
    }
    ]     

+ 이렇게 다른 파일에 있는 변수를 쓰거나 값을 사용 가능

useEffect
---

function 과 return 사이에 위치하는 문법

    useEffect(()=>{
    //코드를 적습니다 여기
    });

를 적으면 되고 페이지가 랜더링 되기전 가장 먼저 수행을 하게 된다. 그래서 변수 더하기나 다양한 기능을 수행 할 수 있다.

+ 또한 여러개의 useEffect를 사용가능하며 수직적으로 실행된다.

Props
---

만약 컴포넌트들에게 나의 변수를 전달하고 싶으면 전역변수가 아닌데 어떻게 전달할까? 

그럴땐 Props를 사용하면 된다. 

    function Modal(props){
    return (
        <div className="modal">
        <h2>제목 { props.글제목[0] }</h2>
        <p>날짜</p>
        <p>상세내용</p>
        </div>
        )
    }

+ props 사용법은 다음과 같으며 props.으로 사용하면된다.

