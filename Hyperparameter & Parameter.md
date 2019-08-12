# Hyperparameter & Parameter



## 1. Parameter



> 쉽게 말해, 알고리즘의 학습의 결과로 얻을 수 있는 값이다. 
>
> 딥러닝에서 가중치(weight, bias),  트리기반 모델에서 분류의 기준,  SVM에서 서포트 벡터를 들 수 있다. 



parameter 특

- parameter 는 학습되어 진다
- 모델의 학습(최적화) 과정에서 결정된다
- 사용자에 의해 결정되지 않는다







## 2. Hyperparameter



> 알고리즘을 구현시에 결정해야 하는 옵션 값이다.
>
> 딥러닝에서 learning rate, drop out rate, 트리기반 모델에서 max_depth, SVM에서 코스트값 c, 
>
> KNN 에서 K 를 들 수 있다. 



hyperparameter 특

- 모델 구현과정에서 사용자가 직접 결정해야하는 값이다
- 휴리스틱하게 결정되는 경우도 있다
- hyperparameter 를 어떻게 지정하느냐에 따라 모델 정확도가 달라질 수 있다
- 흔히 말하는 '모델 최적화', '모델 튜닝' 단계에서 바꿔가며 시도해보는 옵션이다 





참고.

http://blog.naver.com/PostView.nhn?blogId=tjdudwo93&logNo=221067763334&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView