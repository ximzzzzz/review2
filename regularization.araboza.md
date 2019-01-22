## REGULARIZATION



### 1. Why Regularization?

- 학습은 항상 과적합(over fitting)의 문제를 안고 있다. 우리는 트레이닝셋 뿐만 아니라,

  모든 데이터셋에 안정적인 정확도를 나타낼 수 있도록 모델을 일반화 시켜야한다.

  

- 직관적으로 생각했을때 over fitting은 트레이닝셋에만 딱 맞게 최적화되어 복잡한 모델을 의미한다.

  

  <img src='https://cdn-images-1.medium.com/max/1600/1*JZbxrdzabrT33Yl-LrmShw.png'>

  때문에 모델을 일반화시키는 방법은 모델을 좀 더 단순하게 만드는 과정이라고 생각하면 된다. 

  (상단 그림 오른쪽 모델 ->왼쪽모델)

  

##### `그렇다면 모델의 복잡도는 어떤 기준으로 측정하고 어떻게 단순화 시킬 수 있을까?`



### 2. L2 Regularization(Normalization)



- L2 regularization 은 모델의 복잡도를 측정하기위해 L2_norm 을 사용한다.

  L2 norm이란 유클리디안 놈(Euclidean norm) ,  Frobenius norm 이라 불리기도 하는데,

  쉽게 설명하면 원점으로 부터 거리를 의미한다. 자세한 설명은 아래 링크 참고

  http://taewan.kim/post/norm/  

  

-  다시 직관적으로 생각해보면, 모델이 복잡해진다는것은 weight가 크기때문에 들쭉날쭉한 기울기의 모델이 된다는 말인데, 이러한 weight를 모두 제곱한 뒤 더함으로써 복잡도를 측정할 수 있고, 큰 값을 가지고 있는

  weight를 0에 가깝게 감소시킴으로써 모델을 단순화(일반화) 시킬 수 있는것이다. 

  `weight decay`라고도 한다.

  

- L2 regularization에선 L2 norm을 살짝 변형하여 사용하는데(계산상의 이유 같다),

  기존 L2 norm의 값을 데이터셋 관측치의 수(sample 갯수)로 나눈뒤 람다(lambda)/2 를 곱한다. 

  
  $$
  \underbrace{\frac{1}{m} \frac{\lambda}{2} \sum\limits_l\sum\limits_k\sum\limits_j W_{k,j}^{[l]2} }_\text{L2 regularization cost} 
  $$
  

  어렵게 보이지만 그냥 DEDEDDDD||ADQD

#### - Compute cost with Regularization                                                                                                                       



```python
L2_regularization_cost = lambd/(2*m) * np.sum(np.square(Wl))
```





#### - Backward propagation with Regularization

- regularization cost를 반영해야 될 곳은 weight이기 때문에 weight의 업데이트를 위한 미분값을 구할 때 

  regularization의 미분값 역시 추가해준다. bias엔 추가해줄 필요 없다(굳이)

- regularization cost의 미분 공식은 아래와 같이 간단하게 정리할 수 있다.

  
  $$
  \frac{d}{dW} ( \frac{1}{2}\frac{\lambda}{m}  W^2) = \frac{\lambda}{m} W
  $$
  

```python
# 3 Hidden layer 가정시,

dW3 = 1./m * np.dot(dZ3, A2.T) + (lambd/m) * W3 
dW2 = 1./m * np.dot(dZ2, A1.T) + (lambd/m) * W2
dW1 = 1./m * np.dot(dZ1, X.T) + (lambd/m) * W1
```





### 3. Drop out





###  