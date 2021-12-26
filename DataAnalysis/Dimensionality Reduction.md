
Supervised -> 결과가 제공됨
Unsupervised -> 결과가 제공이 안됨

차원을 줄여주는것 -> 연관이 깊은것만 집중해서 불필요한 항목에 대해 줄여줌 (적은 변수)

목적: 더 적은 attributes에 집중한다. 

dimensionality가 클 경우 :거리를 크게 구분을 하여 나눠야하는데 모든 samples에 대하여 거리가 비슷해진다.

1.feature extraction / 2.feature selection 방식이 존재함

설명:
1.조합을 해서 새로운 특성 / 2. 필요없는건 제거

1번에는 과거의 특성을 조합해서 새로운 특성을 만들어간다 (PCA,LDA,t-SNE)
LDA는 레이블 정보를 줘야함 Supervised
2번에는 filter , wrapper , embedded 방식이 존재함.


