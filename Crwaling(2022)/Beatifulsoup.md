BeautifulSoup
---

처음 시작할때
```
import requests

from bs4 import BeautifulSoup
```

웹사이트 접속

```
data = requests.get('URL')
```

페이지 넣고 눈에 편하게 html 보기

```
soup = BeautifulSoup(data.content,'html.parser')

print(soup)
```

필요한 정보만 뽑기(모두 찾기)
```
soup.find_all('태그명',속성명)[0].text
```
속성명은 생략가능
ex) (strong,id="id명")

필요한 정보만 뽑기(하나만)
```
soup.select('css selector')
```

이미지에 저장 하는법
```
import urllib.request #import 모여있는 맨위에다가 작성

urllib.request.urlretrieve(이미지URL, '파일명')
```

f스트링 문법
```
 f'문자 {변수} 문자'
```

\ 제거방법
```
soup = BeautifulSoup(data.content.replace('\',''), 'html.parser')
```