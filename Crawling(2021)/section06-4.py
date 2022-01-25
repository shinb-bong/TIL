# Selenium
# Selenium 사용 실습(4) - 실습 프로젝트 (3)

# selenium 임포트

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


# 엑셀처리 임포트
import xlsxwriter
# 이미지 바이트 처리
from io import BytesIO
import urllib.request as req

# chrome 홈페이지 안띄우고 실행 
chrome_options = Options()
chrome_options.add_argument("--headless")


# 엑셀 처리 선언
workbook = xlsxwriter.Workbook("C:/crawling_result.xlsx")

# 워크 시트
worksheet = workbook.add_worksheet()

# webdriver 설정(Chrome ,FireFox 등) - Headless 모드
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options= chrome_options)

# webdriver 설정(Chrome ,FireFox 등) - 일반 모드
# browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920,1280) # maximize_window(), minimize_window()

# 페이지 이동 
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Content : {}'.format(browser.page_source))

# 제조사별 더 보기 클릭 1
# Explicitly wait -> 명시적으로 기다려달라

WebDriverWait(browser,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 제조사별 더보기 클릭 2
# IMplicitly wait -> 진짜 기다렸다가 그 이후에 함
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 클릭 
WebDriverWait(browser,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[13]/label'))).click()

# 2차 페이지 내용
# print('After Page Content : {}'.format(browser.page_source))

# 2초간 대기 
time.sleep(2)

# 현제 페이지 
cur_page = 1

# 크롤링 페이지 수
target_crawl_num = 6

# 엑셀 행 수
ins_cnt = 1

while cur_page <= target_crawl_num :


    # bs4 초기화
    soup = BeautifulSoup(browser.page_source,'html.parser')

    # 소스코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 상품 리스트 확인
    # print(pro_list)

    # 페이지 번호 출력
    print('******Current Page : {}'.format(cur_page),'********')
    print()

    

    # 필요 정보 추출
    for v in pro_list[0:5] :
        # 임시 출력
        # print(v)
        
        if not v.find('div', class_ = "ad_header") :
            # 상품명, 이미지, 가격
            
            prod_name = v.select('p.prod_name > a')[0].text.strip()
            prod_price = (v.select('p.price_sect > a')[0].text.strip())
            # print(v.select('p.prod_name > a')[0].text.strip())
            base = 'http:'
            add = v.select('a.thumb_link > img')[0]['src']
            quote = base + add
            # print(quote)
        

            # 이미지 요청 후 바이트 변환
            img_data = BytesIO(req.urlopen(quote).read())

            # 엑셀 저장(텍스트)
            worksheet.write('A%s'%ins_cnt,prod_name)
            worksheet.write('B%s'%ins_cnt,prod_price)
            
            # print(v.select('p.price_sect > a')[0].text.strip())
            
            #엑셀 저장(이미지)
            worksheet.insert_image('C%s'%ins_cnt,prod_name,{'image_data': img_data})


            ins_cnt += 1
        print()

    print()
    #페이지 별 스크린 샷 저장
    browser.save_screenshot('C:/target_page{}.png'.format(cur_page))
    
    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num :
        print("Crawaling Succed")
        break

    # 페이지 이동 클릭
    WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()
    # BeautifulSoup 인스턴스 삭제

    del soup

    # 3초간 대기
    time.sleep(3)

# 브라우저 종료
browser.close()

# 엑셀 파일 닫기 (이래야 작성됨)
workbook.close()

