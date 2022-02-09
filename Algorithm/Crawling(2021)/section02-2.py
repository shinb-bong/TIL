#파이썬 크롤링 기초
#urlopen 함수 기초 사용법

import urllib.request as req 
# from을 쓰면 모듈에서 한개의 함수만 불러올수있음
from urllib.error import URLError,HTTPError

#다운로드 경로 및 파일명

path_list = ["C:/test1.jpg", "C:/index.html"]
# 다운로드 리소스 url

target_url=["https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150112_32%2Fguswndld12_14210569751738iM2A_JPEG%2FIMG_6972.JPG&type=a340","https://www.google.co.kr/"]


#enmuerate : 문자열을 split 한후 리스트 문자열로 바꾼뒤 반복문을 돌릴때 리스트의 각 인덱스의 문자열과 인덱스 자체를 접근하는 방식일때 사용합니다.
for i, url in enumerate(target_url) :
    #예외처리
    try : 
        #웹 수신 정보 읽기
        response = req.urlopen(url)
        #수신내용
        contents = response.read()

        print("-------------------------")
        #상태정보 중간 출력

        print('Header Info-{} : {}'. format(i,response.info()))
        print("HTTP Status code : {}".format(response.getcode()))

        print()
        print("-------------------------")

        with open(path_list[i],'wb') as c:
            c.write(contents)






    except HTTPError as e :
        print("Download failed")
        print("HTTpError Code : ", e.code)
    except URLError as e :
        print("Download failed")
        print("URL  ERROR Resaon:", e.reason)

    #성공
    else:
        print()
        print("Download Succed.")

