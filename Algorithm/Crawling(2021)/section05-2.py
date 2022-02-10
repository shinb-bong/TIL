#BeautifulSoup 사용 스크래핑(2) - 이미지 다운로드

import os
import urllib.parse as rep
import urllib.request as req 
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()

#User-Agent 정보 
opener.addheaders = [('User-agent',UserAgent().ie)]
# Header 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL (크롬 개발자 도구)

base = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='

# 검색어 
quote = rep.quote_plus('아이유')

#URL 완성
url = base + quote

#요청 URL 확인
print('Request URL : {}'.format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로 

save_Path = "C:/2021_imagedown/" # C:\\imagedown\\ 같다

# 폴더 생성 예외처리(문제 발생시 프로그램 종료)
try :
    # 기본 폴더가 있는지 체크
    if not (os.path.isdir(save_Path)):
        # 없으면 폴더 생성
        os.makedirs(os.path.join(save_Path))
except OSError as e:
    # 에러내용
    print("Folder creation failed")
    print("Folder name : {}".format(e.filename))

    # 런타임 에러
    raise RuntimeError("System Exit!")
else :
    # 폴더 생성이 되었거나 , 존재할 경우 
    print("Folder is created!")

# bs4 초기화
soup = BeautifulSoup(res,"html.parser")

# print(soup.prettify())

# select 사용

img_list = soup.select('div.photo_bx.api_ani_send._photoBox > a > img')


# find_all 사용 할 경우
img_list2 = soup.find_all('img')
# print(img_list2)
for v in img_list2 :
    print()
    print()
    print(v["src"])
    

# # find_all 사용 할경우 (강의)
# img_list2 = soup.find_all('a',class_="link_thumb _imageBox _infoBox")
# # print(img_list2)
# for v in img_list2 :
#     img_t = v.find('img')
#     print(img_t.attrs['src'])
#     req.urlretrieve(img_t.attrs['src'],fullFileName)

# print(img_list)

for i, img in enumerate(img_list, 1) :
    print()
    print()
    #속성 확인
    # print(img['src'], i)

    # 저장 파일 명 및 경로 
    fullFileName = os.path.join(save_Path,save_Path+str(i)+'.png')
    
    #파일명
    # print(fullFileName)

    # 다운로드 요청(URL, 다운로드 경로)

    req.urlretrieve(img['src'],fullFileName)
#다운로드 완료시
print("dowload succeded")
    