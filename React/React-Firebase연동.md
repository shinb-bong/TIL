React-Firebase 연동
---

firebase 프로젝트 생성하고

index.js에 

    import firebase from "firebase/app";
    import "firebase/firestore";

    const firebaseConfig = {
    해당 프로젝트키~
    };


    firebase.initializeApp(firebaseConfig);
    export const db = firebase.firestore();

를 입력해 준다.

그 후 원하는 js에 가서

    import {db} from './index.js';
    import "firebase/firestore";

입력해준다. 그러면 이제 Firebase를 사용할 수 있다.

예제 코드로 한번 돌려봤는데 

    function App() {
    let [catagori,setCatagori] = useState([]);
    useEffect(() => {
        //sector 값만 바꿔서 돌리면 분류되서 쭈르륵 뜹니다. 테이블, 페이지먼트 안건드려도 됩니둥
        var users = db.collection("product").limit(100)
        users.get()
        .then(query => {
            // var array = query.map(a => a.data());
            // console.log(array);
            var array = []
            query.forEach(function (doc) {
            array.push(doc.data());
            });
            setCatagori(array);
        })
    }, []);

    
    return (
        <div className="App">
        <Container>
            {
            console.log(catagori)
            }
            {catagori[1]?.name}
        </Container>
        </div>
    );
    }

인데 여기서 재랜더링이 Firebase에서 가져오는 현상보다 빠르게 일어나서 오류가 자주 일어났다. 

해결 방안: 

    {catagori[1]?.name}

처럼 뒤에 ? 를 붙여주면 해당 리스트가 로드 되기전까지 출력하지 않는다.