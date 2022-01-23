React-Router
---
특징: 각각 페이지마다 다른 HTML 파일을 보여주는게 아니다.
HTML 내부의 내용을 갈아치워서 다른 페이지처럼 흉내내는 것일 뿐이다.

예제 상세 페이지 만들기
---
    <Route path=”/detail/:id> 
    </Route>

여기서 만약 detail 페이지에서 id 값을 사용하고싶다? 

그럼 useParams() 을 사용하면 사용할 수있다.

React-router-dom 라이브러리에 존재하며 let {id} = useParams(); 이제 id는 :id에 있는 자리의 숫자를 의미한다.

또한 순서가 바뀔걸 염려해 	

    let 찾은 상품 = Axios.get(‘GET요청할URL’);

    .then((request)=>{ request.id == id  })
    .catch(()=>{ 요청실패시실행할코드 })
 이런느낌으로 해도될것 같긴하다.


Redux
---
순서:

1. Index.js 에있는 reducer라는 함수를 통해 수정방법을 미리 정의
2.      prpos.dispath()
    로 onClick 함수에 정의하면된다. 

        export default connect(state를props화)(Detail) 

    잊지않기로 한다.

쓰는 이유?

대규모 사이트들에서 데이터를 한눈에 한곳에 관리할 수 있어서 사용한다

한눈에 보게되어 만약 잘못된 경우는 reducer만 보게 됨

서버 개발처럼 서버의 데이터 입출력API 만드는 과정이랑 유사함

서버는 미리 API를 짜두는 데 이것도 reducer부터 짜놓는거임.

무조건 redux 먼저 하고 dispatch 짜고 데이터보내기!

***만약 reducer가 여러개 필요하다면?***

다른 이름의 reducer2 + reducer2의 초기값을 하나 더 만들고 

combineReducers()라는 함수안에 집어넣은 후에 createStore()안에 넣으시면 됩니다.

    let store = createStore( combineReducers({reducer, reducer2}) )

사용할 때는 

    [해당 불러와진거].reduce함수명

Redux 중요 사안 
---

내가 이 state 데이터를 다른 컴포넌트에 쓸 일이 없다면 useState()로 해당 컴포넌트 안에 간단하게 만드는게 나음

Redux에 데이터를 보내고 싶으면?
---

    props.dispatch({ type : 어쩌구, payload : '안녕' })
 이렇게 쓰면 안녕이라는 데이터를 redux store까지 데이터를 실어보낼 수 있고

reducer 안에서 요청을 처리할 땐 ***액션.payload*** 라고 쓰면 보냈던 '안녕' 데이터를 사용할 수 있다..

    reducer(state, 액션) {} 

이렇게 적은 부분에서의 액션이라는 파라미터는
그냥 dispatch() 소괄호 안에 들어있던 모든게 들어있다.


혹은 

useSelector 사용하는 방법이 있긴하다.

    import { useSelector } from 'react-redux';

    function Cart(props) {
    let state = useSelector((state) => state )
    console.log(state.reducer)
    
    (생략)
    }

저기에 state는 다 합쳐진 reduce 가 남아있으므로 명시해야함.

    let dispatch = useDispatch() 

하면 props.dispatch() 하던것을 dispatch()로 다 고쳐서 사용이 가능


findindex() 

    [1,2,3,4].findindex((a)=>{return a===1 });

하게 되면 1이 있는 자리의 인덱스를 뱉는다