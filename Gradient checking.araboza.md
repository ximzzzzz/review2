# Gradient checking



## 1. what is Gradient Checking?



#### - Back propagation 이 정상적으로 작동하고 있는지 확인하기 위한 검증방법

#### - derivates(미분값)을 구하는 과정에서 계산과정이 복잡해지기 때문에 

#### 	버그가 발생할 수 있다. 

#### - Gradient check을 통해 어느계산에서 잘못됬는지 문제를 파악하고 수정가능

#### 	 

#### 	`:한마디로 debugging`





## 2. principle



#### - back propagation 진행시에 계산된  θ(weight, bias) 값과 

#### 	직접 구한 근사값을 비교하여 이상유무를 검증한다

###  ![gradcheck](https://user-images.githubusercontent.com/44566113/51457140-947b0900-1d93-11e9-90ec-6a02815b6a93.PNG)



​		위의 예시를 봤을때, f(θ) 값은 θ의 세제곱이라고 가정하면,  

​		θ에 0.01의 작은 ε 을 더하고 뺀  θ+ε, θ-ε 사이의 기울기를 구한다.  

​		-> 직접구한 근사값(우측 상단의 기울기 공식 참조)

​		 

​		근사값 3.0001은 실제 미분값 3과 비교했을 때 0.0001 차이밖에 나지 않기 때문에 미분계산이 제대로

​		되었는지 확인할 수 있는 지표로 사용할 수 있다.

 		

​		이러한 원리를 응용하여 Back propagation 시에 구한 θ와 θ_approx(근사값)을 비교하여 

​		큰 차이가 나지않으면 제대로 Back propagation이 되고 있다고 볼 수있다.



### 3. gradient check



<img src='https://user-images.githubusercontent.com/44566113/51458141-7e6f4780-1d97-11e9-8672-328287ff652a.jpg' width='900'>

​	비용함수 J(θ) 를 2차원 그래프를 통해 위와 같이 나타낸다고 했을때,

​	(여기서 θ는 layer에 사용되는 weight, bias 값.   ex) w1,b1, w2,b2, w3,b3... )

​	back propagation 이 제대로 작동한다면 비용함수는 gradient descent를 통해

​	점점 아래(최적지점)로 내려갈 것이다. 이러한 내용을 Debug 하기 위해 근사값과 비교해 보려하는데,

​	파란색은 비용함수  J(θ)에 대한 기울기(derivative)로 볼 수 있다. 그리고 그 값을 근사하기 위해

​	우리는 아주 작은 값 ε의 간격사이의 θ의 기울기를 직접 구함으로서(빨간 기울기선) 그차이를 비교할 수 있다.

​	

​	그렇다면 hidden layer가 많아서 레이어 별로 grad check를 하고싶을때 어떻게 해야할까?	

<img src='https://user-images.githubusercontent.com/44566113/51460502-0278fd80-1d9f-11e9-9813-4b049eeb1141.jpg' width='900'>



​	

​	θ 는 θ1, θ2, θ3..을 모두 포함한 벡터로 볼 수 있다. 여기서 θ1은 hidden layer_1의 

​	parameter들(weight1, bias1) 을 의미한다. 그래서 우리가 구하는 비용함수 J(θ)는

​	hidden layer의 모든 parameter들을 적용하여 나온 output에 대한 비용함수로 볼 수 있다.

​	

​	다시 본론으로 돌아와, 특정 hidden layer의 grad check을 하고싶을땐 위 그림과 같이

​	체크하고자 하는 layer의 θ만 ε을 통해 기울기를 구하여 비교할 수 있는것이다.







### 4. notes



#### 	- don't use in training - only to debug

​		gradient check은 계산과정이 많기 때문에 초기에 구현이 잘되었는지 검증을 위한 용도 외에는 

​		사용하지 않는다. 특히 training에 사용할 경우 속도가 저하되기 때문에 반드시 제외한다.

 

#### 	- if algorithm fails grad check, look at components to try to identify bug

​		gradient check을 통해 차이가 큰걸 발견했을 경우 직접 확인하여 잘못된 지점을 찾고 수정한다.



#### 	- remember regularization

​		regularization을 했을경우, 비용함수를 계산할때 반드시 L2 norm/L1 norm이든  regular term을

​		포함시켜 계산해야 정확한 검증을 할 수 있다.



#### 	- doesn't work with dropout

​		dropout은 랜덤한 확률로 unit을 버리기 때문에 정확한 cost를 측정하는데 적합하지 않다.

​		때문에 dropout을 포함한 cost로 gradient check을 할경우에 잘 구현되었음에도 불구하고 

​		근사값과 derivate의 차이가 크게 날 수있다.

​		keep_prob=1 로 해두고 gradient check하길 권장한다.





참조.  coursera deeplearninig.ai (andrew ng)

​	http://goodtogreate.tistory.com/entry/Gradient-Checking (GOOD to GREAT)

​	http://1ambda.github.io/data-analysis/machine-learning-week-5/ (1ambda)

​	