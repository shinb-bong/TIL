# Requests
# requsets 사용 스크래핑(2) - Json

import json
import requests

s = requests.Session()

# 100개  Json 데이터 요청

r = s.get('https://httpbin.org/stream/100',stream = True)

# 수신 확인
print(r.text)

# Encoding 확인
print('Encoding  : {} '.format(r.encoding))

# if r.encoding is None :
#     r.encoding = 'utf-8'


# print('After : {}'.format(r.encoding))


for line in r.iter_lines(decode_unicode=True):
    #라인 출력후 타입 확인
    # print(line)
    # print(type(line))

    #Json(Dict) 변환 후 타입 확인
    b = json.loads(line) # str -> dict
    # print(b)
    # print(type(b))

    # 정보 출력
    for k , v in b.items() :
        print("KEY : {} ,  VALUE : {}".format(k,v))

    print()
    print()


s.close()


#복습

r = s.get('https://jsonplaceholder.typicode.com/todos/1', stream = True)

# Header 정보
print(r.headers)

# 본문 정보
print(r.text)

#json 변환
print(r.json())

# key 반환
print (r.json().keys())
print (r.json().values())

# 인코딩 반환
print(r.encoding)

# 바이너리 정보
print(r.content)

s.close()


print()
print('*'*100)


# #내가한 복습

# r = s.get('https://jsonplaceholder.typicode.com/posts')
# # print(r.headers)
# # print(r.text)
# print(r.json())

# print('Encoding  : {} '.format(r.encoding))

# for line in r.iter_lines(decode_unicode=True):
#     #라인 출력후 타입 확인
#     print(line)
#     print(type(line))

#     p = json.loads(line) # str->dict
    
