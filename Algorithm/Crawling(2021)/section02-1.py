#Section 02 -1
#파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req 

# 파일 URL 
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDEyMTVfMTg1%2FMDAxNjA4MDQyMzY0ODAz.VUGUtxbS1hF1ftRzL7mIcRYQQHO6mHBv9MOPa0xNrLwg.9qpCypOByFFr0hwkVKVzyOh4EWDx2N6PiHzFBCJa_ZIg.JPEG.0hoyaho0%2FIMG_3406.jpg&type=a340'
html_url = 'https://www.google.co.kr/'

#다운 받을 경로 
save_path1 = 'C:/test11.jpg'
save_path2 = 'C:/index1.html'

#예외처리

try : 
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e :
    print('Download failed')
    print(e)
else: 
    #Header 정보 출력  (정상적으로 정보가 잘 전달 되었는지)
    print(header1)
    print(header2)

    #다운로드 파일정보

    print('Filename1 : {}'.format(file1))
    print('Filename2 : {}'.format(file2))

    print()

    #성공 
    print('Download Succed')

