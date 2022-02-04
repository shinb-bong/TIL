Google 로그인 연동
---

GCP를 통한 로그인 구현 (Google-Oauth)

>> 아래 Firebase를 통한 구현도 실습해봤는데 그게 더 효과적이고 보기 편하다.

1. Google Cloud Platform 프로젝트를 만들기.

> https://console.cloud.google.com

2. 좌측 메뉴의 사용자 인증 정보 - OAuth 클라이언트 ID 만들기로 들어온다.

- URL에는 현재 로컬로 하기때문에 로컬 주소인 http://localhost:3000를 넣어준다.

3. Google-login 모듈 설치

>     npm i react-google-login

4. 구글 로그인 버튼 Component 생성

         import React from 'react';
        import GoogleLogin from 'react-google-login';

        const clientId = "위의 Google Cloud Platform에서 발급받은 Client ID";

        export default function GoogleLoginBtn({ onGoogleLogin }){
            const onSuccess = async(response) => {
                const { googleId, profileObj : { email, name } } = response;
                
                await onGoogleLogin (
                // 구글 로그인 성공시 서버에 전달할 데이터
                );
            }

            const onFailure = (error) => {
                console.log(error);
            }

            return(
                <div>
                    <GoogleLogin
                        clientId={clientId}
                        responseType={"id_token"}
                        onSuccess={onSuccess}
                        onFailure={onFailure}/>
                </div>
            )
        }


5. 주의사항 이 google-login 으로 웹페이지에서 사용하는 경우

> 구글에서 받은 토큰은 "너가 인증한 구글 계정이 맞아"라는 인증서일 뿐, 우리가 이용해야 할 서버에서는 따로 토큰을 발급해주어야 한다. 

- 이부분은 firebase로 구현을 해야하나 싶다.



------

추가로 돌려본 실습)

React-firebase-auth

App.js 코드

    //App.js

    import React, { useState } from 'react';
    import { authService,firebaseInstance } from './fBase';
    import { Button, Container } from 'react-bootstrap'

    const App = () => {


    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [newAccount, setNewAccount] = useState(true);	// 새로운 유저인지 확인(초기값: true)
    
    const onGoogleClick = async (event) => {
        const {target: {name}} = event;
        let provider;
        if (name === 'google') {
        provider = new firebaseInstance.auth.GoogleAuthProvider();
        }
        const data = await authService.signInWithPopup(provider);
        console.log(data);
    }

    const onChange = (event) => {
        const {target: {name, value}} = event;
        if (name==='email') {
        setEmail(value)
        } else if (name=== "password") {
        setPassword(value);
        }
    }
    
    const onSubmit = async (event) => {
        event.preventDefault();
        try {
        let data;
        if (newAccount) {
            // create account
            data = await authService.createUserWithEmailAndPassword(email, password);
        } else {
            // login
            data = await authService.signInWithEmailAndPassword(email, password);
        }
        console.log(data);
        } catch(error) {
        console.log(error)
        }
    }
    
    const toggleAccount = () => setNewAccount((prev) => !prev);

    return (
        <>
        <Container>
        
        <head>
        
        // bootstrap css cdn
            <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
        crossorigin="anonymous"
        />
        </head>
        <form onSubmit={onSubmit}>
            <input name="email" type="email" placeholder="Email" required value={email} onChange={onChange}/>
            <input name="password" type="password" placeholder="password" required value={password} onChange={onChange}/>
            <input type="submit" value={ newAccount ? "Create Account" : "Login" } />
            <hr/>
        </form>
        <Button variant="secondary" onClick={toggleAccount}>{newAccount ? "Login" : "Create Account"}</Button>
        <Button  variant="primary" name="google" onClick={onGoogleClick}>구글 계정으로 로그인</Button>
        </Container>
        </>
    )
    }

    export default App;


fbase.js 코드

    import firebase from 'firebase/compat/app';
    import 'firebase/compat/auth';
    import 'firebase/compat/firestore';

    const firebaseConfig = {
        ~~ firebase 에서 받아온 정보
    };

    firebase.initializeApp(firebaseConfig);
    export const firebaseInstance = firebase;
    export const authService = firebase.auth();


하면 구글 로그인도 성공적으로 가능하였고 
이메일 비밀번호를 통한 로그인도 가능하였다.

+ Firebase에 Authentication에 저장되는 것도 확인 하였다.

+ Google과 일반 로그인 회원가입 모두 정상적으로 작동하였다.

>> 참고자료: https://gingerkang.tistory.com/106

