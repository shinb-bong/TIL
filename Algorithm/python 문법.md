Python 문법 헷갈리는거 정리하기
---

1. 전역 변수를 사용하려면 

        global <변수>를 사용해야한다.

2. 람다 함수식
    
        def add(a,b):
            return a+b
        print(add(3,7))
        // 같다

        print((lambda a,b :a +b)(3,7))

3. 입출력 빠르게 받기

        import sys

        data = sys.stdin.readline().rstrip()
        // .rstrip() 안쓰면 enter가 줄바꿈 기호임

3. 자주 사용하는 라이브러리

    1. 내장함수 
    2. itertools: 반복되는 형태의 데이터를 처리하는 기능
    3. heapq: 우선순위큐
    4. bisect: 이진탐색을 제공
    5. collections: 덱 카운터 자료구조 포함