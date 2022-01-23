Django 외부라이브러리 Part

Django-crispy-forms
----

-	사용법은 책에
-	폼이 테이블 형태로 나타나지 않게 하는 것 
-	그래서 폼을 양쪽 너비에 맞춰서 화면에 꽉차게 만들어 줄 수 있음
마크다운 적용하기
-	django-markdownx
-	사용법은 책에...
-	포스트 상세페이지에 그대로 안가는 것은 마크다운 문법을 오버라이딩 함으로써 해결가능
-	def get_content_markdown(self):
return markdown(self.content)


-	그 후 html에서 필터로 safe를 씌워준다. 

로그인 기능 

-	Django-allauth:
사용하면 구글 로그인 카카오톡 로그인등 이런 기능을 회원가입할때 이용 할 수있음
사용법 대로 사용하면
Admin에 카데고리로 SITES 와 SOCIAL ACCOUNTS 가 생성되어있음.
이 기능을 리액트에서 사용하고싶은데 어떻게 해야하나 

또한 인스타그램 팝업 기능은 어케하는가  모달창으로 구현을 한다.


crsf, dispatch()
---
crsf란?? 보안에 중요

장고에서 form을 사용할때 보안을 위해 form 안에 무작위 토큰을 input 값으로 부여하고 
나중에 서버에 Post 값을 확인할때 그 토큰 값이 맞는지 확인하는 과정을 거친다. 그래서 특별한 경우가 아니라면 form 안에 {% csrf_token %}을 써야한다.

dispatch()보안에 중요

-	웹 사이트 방문자의 요청이 GET인지 POST 인지 판단하는 메소드
-	사용 예) 다른 사용자가 타 사용자의 댓글을 마음대로 수정을 할 수 있으므로 다른거에 앞서 그 글을 입력한 사용자가 지금 사용자와 맞는지 확인하는 과정에서 사용가능함.


DeleteView를 사용하지 않은 이유
---

DeleteView는 장고에서 제공해주는 뷰로써 댓글을 삭제하기전 진짜 삭제할 것인가? 에 대해 물어보는 페이지로갔다가 돌아옵니다. 하지만 보통 사이트는 모달창을 통해 그사이트 위에서 삭제 결정을 하기때문에 Modal 을 이용했습니다.


pagination
---

-	paginate_by 를 해당 List views.py안에 넣어준다.

query 조건에서는 title.contains 처럼 쓰는것이 아닌 title__contains 로 사용
그리고 distinct() 설정을 해줘야 중복 제거

bootstrap grid
---
부트스트랩 grid는 페이지를 12칸으로 나눈건데 만약 col-4 col-4 로 12개보다작을경우
4를 표현하고 공백 4 그다음 4를 추가해서 최대한 두개를 거리를 둔다.

css에는 alpha 값을 지정하여 투명도를 지정할 수 있다.



