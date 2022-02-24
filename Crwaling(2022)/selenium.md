selenium
---

사용이유:

테스트를 직접 하기 싫어서 자동화 시키려고 나온 라이브러리

하지만 데이터 수집에 사용

- ajax가 많이 들어간 사이트
- request+bs4 로 수집하기 어려웠던 사이트
- 로그인이 필요한 사이트 할 때 유용

사용법

1. chromedriver 구글에 검색해 os에 맞는 파일을 다운 받습니다.

2. 셀레니움을 설치합니다.

```
pip install selenium==3.141.0
```

3. 코드 입력

```
from selenium import webdriver

from selenium.webdriver.common.keys import Keys 

import time

driver = webdriver.Chrome('chromedriver.exe')
```
---
원하는 URL 접속 & 이동

```
driver.get('https://instagram.com')
```
원하는 요소 찾기
```
driver.find_element_by_css_selector('.class명')

driver.find_element_by_css_selector('#id명')

driver.find_element_by_css_selector('태그명[속성이름="속성명"]')
```

다른 방법의 원하는 요소 찾기
```
driver.find_element_by_class_name('class명')[X]
```

원하는 요소의 글자 가져오기
```
driver.find_element_by_css_selector('.class명').text
```

찾는법: 윗요소의 클래스명 + 띄어쓰기 + 밑요소의 태그명

class명이 없는 태그 가져오기
```
driver.find_element_by_css_selector('input[name="password"]')
```

원하는 요소를 클릭/키입력
```
driver.find_element_by_css_selector('.class명').click()

driver.find_element_by_css_selector('.class명').send_keys('codingapple_test')

driver.find_element_by_css_selector('.class명').send_keys(Keys.ENTER)  #엔터키입력
```

가끔 click()이 안되면 강제로 클릭하는 법
```
e = driver.find_element_by_css_selector('클릭하고싶은요소')
driver.execute_script('arguments[0].click();', e)
```

***주의! html요소는 중복으로 출현 가능 class명 확인 or css selector 사용***

원하는 속성가져오기
```
이미지 = driver.find_element_by_css_selector('').get_attribute('src')
// 이렇게 하면 이미지 url가져와짐
```

이미지 파일 저장
```
import urllib.request #이건 import 모여있는 맨위에다가 작성

urllib.request.urlretrieve(이미지URL, '파일명')
```