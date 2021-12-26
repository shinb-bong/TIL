Principle Components Analysis
---
Unsupervised형태

적은 Compoents면 충분히 기존의 데이터를 설명할 수 있다.

ex) 축 분리

W값엔 벡터의 축이 어떻게 나타나는지 맵핑됨
1. Covariance Matrix 계산
2. eigenvectors , eigenvalues 를 고른다
3. 투영시켜서 볼 수 있다.
4. eigenvalues를 보고 중요도를 판단 가능

Covariance: 두 변수 사이에 관계정도 계산

사용법: 
from sklearn.decomposition import PCA 
