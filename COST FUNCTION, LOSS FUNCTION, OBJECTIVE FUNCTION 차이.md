COST FUNCTION, LOSS FUNCTION, OBJECTIVE FUNCTION 차이



COST FUNCTION : 한가지 데이터 샘플의 비용

- $\hat{y_1}$ , $y_1$  간 차이의 정도



LOSS FUNCTION : 데이터셋 전체의 평균 비용

- $\hat{Y}$ , $Y$  간 차이의 정도



OBJECTIVE FUNCTION  : 최적화를 위한 목적함수

- $argmin_X($$(\hat{Y}$ - $Y)^2$ ) , 제곱합이 가장 **작은** X 집합 찾기
- $MLE(X)$ : **가장 큰** likelihood(우도)를 갖는 X집합 찾기



중요한 점은 OBJECTIVE FUNCTION은 무조건 LOSS FUNCTION을 최소로 만드는 함수가 아니라는 것

목적에 따라 LOSS FUNCTION을 최대로 만들수도, 최소로 만들 수도 있다. 

학습에 따라선 학습이 진행됨에 따라 LOSS가 커지는게 오히려 잘 되는것일 수도 있다.



 