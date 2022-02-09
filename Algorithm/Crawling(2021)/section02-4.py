#파이썬 크롤링 기초
#lxml 사용 기초 스크래핑(1)
#pip install lxml, requsets, cssselect

import requests
from lxml.html import fromstring, tostring
def main() :

    """
    네이버 메인 스탠드 스크랩핑 메인함수
    """
    #세션 사용
    session = requests.Session()

    #스크랩핑 대상 URL

    response = session.get("https://www.naver.com")

    # 신문사 링크 딕셔너리  획득(우리가 만들어줄 함수)
    urls = scrape_news_list_page(response)

    #딕셔너리 확인
    print(urls)

    #결과 출력 
    for url in urls :
        #url 출력
        print(name, url)
        #파일쓰기 

        #생략

def scrape_news_list_page(response):
    #URL 딕셔너리 선언
    urls = {}

    #태그 정보 문자열 저장
    root = fromstring(response.content)
     #끌어오기
    for a in root.xpath('//*[@id="NM_NEWSSTAND_DEFAULT_THUMB"]/div[1]/div[4]/div/div[2]/div[1]'): 

        #a 구조 확인
        # print(a)

        #a 의 문자열 출력

        # print(tostring(a, pretty_print=True))

        name , url = extract_contents(a)

        #딕셔너리 삽입
        urls[name] = url

         
    return urls

def extract_contents(dom) :
    #링크 주소

    link = dom.xpath('./div/a[3]')[0].get("href")

    #신문사 명
    name = dom.xpath('./a/img')[0].get('alt') #xpath('./img')
    
    return name, link


#copy selector 가 만능은 아니다



# 스크랩핑 시작
if __name__ == "__main__" :
    main()