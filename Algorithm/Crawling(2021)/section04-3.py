# Requsets
# request 사용 스크랩핑(3) - Rest API

# Rest API : GET, POST, DELETE, PUT:UPDATE, REPLACE(FETCH : UPDATE, MODIFY)
# 중요 : URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET : /movies : 영화를 전부 조회
# /movies/:id : 아이디인 영화를 조회
# Post : /movies : 영화를 생성
# PUT : /movies : 영화를 수정
# DELETE : /movies : 영화를 삭제

#세션 활성화

import requests
s = requests.Session()

# 예제 1
r = s.get('https://api.github.com/events')

# 수신 상태 체크 
r.raise_for_status()

#출력
print(r.text)

# 예제 2
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()

# 쿠키 삽입
jar.set('name','sbk',domain ="httpbin.org", path='/cookies')

#요청 
r = s.get('http://httpbin.org/cookies', cookies = jar)

print(r.text)

# 예제 3

r = s.get("http://github.com", timeout = 5)

# 출력
print(r.text)


# 예제 4
r = s.post('http://httpbin.org/post', data = {'id':'test77','pw':'1111'}, cookies = jar)

# 출력 
print(r.text)
print(r.headers)

# 예제 5
# 요청

payload1 ={'id':'test77','pw':'1111' }
payload2 = (('id','test77'),('pw','1111'))

r = s.post('http://httpbin.org/post' , data = payload1)

#출력

print(r.text)

# 예제 6(PUT)

r = s.put('http://httpbin.org/put', data = payload1)
# 출력
print(r.text)

# 예제 7 (DELETE)

r = s.delete('http://httpbin.org/delete' ,data = {'id': 1})

#출력

print(r.text)

# 예제 7 (DELETE)

r = s.delete('https://jsonplaceholder.typicode.com/posts/1' )
print(r.ok)
print(r.text)
print(r.headers)
s.close()