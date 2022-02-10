#파이썬 크롤링 기초
#lxml 사용 기초 스크래핑(1)
#pip install lxml, requsets, cssselect

import requests
import lxml.html
def main() :

    """
    네이버 메인 스탠드 스크랩핑 메인함수
    """

    #스크랩핑 대상 URL

    response = requests.get("https://www.naver.com")

    # 신문사 링크 리스트 획득(우리가 만들어줄 함수)
    urls = scrape_news_list_page(response)

    #결과 출력 
    for url in urls :
        #url 출력
        print(url)
        #파일쓰기 
        #생략

def scrape_news_list_page(response):
    #URL 리스트 선언
    urls = []

    #태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content)
     #끌어오기
    for a in root.cssselect('a.btn_popup'): #"""css 선택자 클래스 넣어주기 """

        #링크 
        url = a.get('href') #"""속성"""
        urls.append(url)
    
    return urls


#copy selector 가 만능은 아니다






# 스크랩핑 시작
if __name__ == "__main__" :
    main()