#BeautifulSoup 사용 스크래핑(1) - 기본 사용법
#BeautifulSoup

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title> The Dormouse's story</title>
    </head>
    <body>
        <h1> this is h1 area </h1>
        <h2> this is h2 area </h2>
        <p class = "title"><b>The Dormouse's story</b></p>
        <p class = "story">Once upon a time there were three little sistes.
            <a  href= "http://example.com/elsie" class ="sister" id ="link1">Elsie</a>
            <a  href= "http://example.com/lacie" class ="sister" id ="link1">Lacie</a>
            <a data-io = "link3" href= "http://example.com/little" class ="sister" id ="link1">Title</a>
        </p>
        <p  class ="story">
            story....
        </p>
    </body>
<html>
"""

#예제 1 (BeautifulSoup 기초)
#bs4 초기화 (연 내용 넣어주기)

soup = BeautifulSoup(html,'html.parser')

#타입 확인
print('soup', type(soup))
print('prettify', soup.prettify) #내용 출력

#h1 태그 접근

h1 = soup.html.body.h1
print('h1', h1)

# p 태그 접근
p1 = soup.html.body.p 
print('p1',p1)

# 다음 태그 
p2 = p1.next_sibling.next_sibling  # /p도 포함 해서 두개씩 써야함
print('p2',p2)

# 텍스트 출력1
print('h1>>',h1.string)  #string 메소트 -> 텍스트만 출력

# 텍스트 출력2
print('p1>>',p1.string)

# 함수 확인 
print(dir(p2))

# 다음 엘리먼트 확인
# print(list(p2.next_element)) # 잘사용안함

# 반복 출력 확인
for v in p2.next_element:
    print(v)

# 예제 2(Find, Find_all)

# bs4 초기화 
soup2 = BeautifulSoup(html,'html.parser')

# a 태그 모두 선택

link1 = soup.find_all('a',limit = 2) #limit 옵션
#리스트 요소 확인
print('links', link1)

# 중요
link2 = soup.find_all("a", class_ ='sister') #class_ 자리에 id = "link2", string = "title", string = ["Elsie"] 가능
print(link2)

for t in link2 :
    print(t)

#처음 발견한 a 태그 선택
link3 = soup.find("a")
print()
print(link3)
print(link3.string)
print(link3.text)

# 다중 조건(중요)
link4 = soup.find("a",{"class" : "sister", "data-io":"link3"})

print(link4.text)
print(link4.string)

# css 선택자 : select, select_one
# 태그로 접근 : find, find_all


# 예제 3(select,select_one)
# 태그 + 클래스 + 자식 선택자

link5 = soup.select_one('p.title > b') #.은 클래스
print()
print(link5)
print(link5.string)

link6 = soup.select_one("a#link1")# #은 id

print(link6)
print(link6.string)

link7 = soup.select_one("a[data-io= 'link3']") #[]속성(그 외) 값에 접근 # text 보단 string 선호
print(link7.string)

#선택자에 맞는 전체 선택
link8 = soup.select('p.story > a')
print(link8)

link9 = soup.select('p.story > a:nth-of-type(2)')
print(link9)


link10 = soup.select("p.story")
print(link10)

for t in soup.select("p.story") :
    temp = t.find_all("a")
    

    if temp:
        for v in temp:
            print(' >>>>>>>',v)
            print(' >>>>>>>',v.string)

    else :
        print('----',t)
        print('----',t.string)