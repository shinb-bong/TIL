PageRank 
---
구글 검색의 기반이 되는 알고리즘 

- 웹페이지 사이의 연결 관계가 상당히 유용한 정보를 제공해 줄 수 있는 것에서 유래


다른 페이지에서 오는 링크를 같은 비중으로 보는 것 보다 차별화를 두어서 링크 숫자를 ***정규화*** 하는 방식을 사용한다.
(점수를 매긴다.)

    PR(A) = (1-d) + d (PR(T1)/C(T1) + … + PR(Tn)/C(Tn))

- PR은 PageRank
- 수식은 정규화시킨 페이지랭크의 합 
- 특징: 노드가 많으면 페이지 랭크가 우수해도 기여도가 낮아진다.

각 PageRank는 재귀적으로 구해지며 재귀적 알고리즘을 사용한다.

그럼 이때 d의 의미는 무엇인가?

- Damping Factor
- 논문에선 보통 0.85로 작성
- 어떤 사람이 마구잡이로 서핑을 하는데 이 페이지에 머무르지 않고 다른 페이지를 누를 확률을 말한다.
- 그래서 1일경우 무조건 다른 페이지를 누르는 것으로 판명

구글은 다른 요소를 가미해서 사용했겠지만 

***영향력 있는 사이트가 인용이 될수록 페이지 랭크 수치가 올라간다***

는  변함이 없다


