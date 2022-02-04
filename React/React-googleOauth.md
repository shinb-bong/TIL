Google 로그인 연동
---

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