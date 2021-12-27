상세페이지 제작 
--------
물건별로 각자의 상세 페이지가 필요함

query string을 사용한다. 
----
URL의 query string 자료이름 = 값 & 자료이름2 = 값2 

값은 유니크한 값을 사용한다. 
id = ${doc.id}

상세페이지에서 해당 id를 받아오려면 url의 id 부분을 받아오면 되는데

`var query = new URLSearchParmas(window.location.search);
db.collection('product').doc(쿼리스트링.get('id')).get().then((result)=>{}) 문법 사용`

로그인 기능

firebase.auth().onAuthStateChanged()사용 로그인 상태가 변경되면 실행됨 (새로고침 포함)

하지만 서버에서 불러오는 느린작업이며 방지를 하기 위해 편법으로 localstorage에 저장

저장하는법
---
localstorage.setItem('정보이름','값');

무조건 값형태로 넣어줘야함으로 우리가 넣어줄땐 
JSON.stringfy(user);
로 Json변환후 넣어줘야한다.

가져올때
---
var jitem = localstorage.getItem('정보이름');
후 
JSON.parse(jitem).항목

로그아웃 할땐 삭제를 해주는게 효율적이므로
localstorage.removeItem('정보이름');    

