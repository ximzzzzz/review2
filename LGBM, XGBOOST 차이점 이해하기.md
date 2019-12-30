# LGBM, XGBOOST 차이점 이해하기!





## 1.  Level-wise , Leaf-wise



우선 Gradient Boosting Decision Tree 를 만들어 나가는 과정에서 level-wise, leaf-wise 방식을 알아야 한다.



![img](https://i0.wp.com/mlexplained.com/wp-content/uploads/2018/01/DecisionTrees_3_thumb.png?resize=704%2C122)

- level-wise

  트리의 노드를 아래로 늘려 나가는 과정, 즉 depth를 깊게 만드는 과정에서 depth의 노드를 균형있게 맞추며
  
  늘리는 방식이다. 위 그림에서 왼쪽과 같이 depth를 깊게 만들 때 마다 level의 노드가 균형을 이룬 모습이다.
  
  균형을 맞추며 노드를 늘려나가기 때문에 leaf-wise 방식에 비해 상대적으로 정규화된 모델이라 할 수 있다.
  
- leaf-wise

  depth를 깊게 만드는 과정에서 균형을 유지하는 것을 고려하지 않고 오직 loss를 줄이는 것만 목적으로

  노드를 늘려나가는 방식이다.  균형에 상관없이 노드를 늘리기 때문에 level-wise에 비해 상대적으로 유연하지만 반대로 과적합될 수 있는 위험이 있다. 



트리가 커질 수록 두 방식에 따른 트리의 차이가 커지기 때문에 하이퍼파라미터 튜닝시 유의해야한다.

특히  `num_leaves` , `max_depth` 와 같은 경우, 두 가지 트리를 같은 숫자로 세팅하더라도 결과가 크게 다를 수

있기 때문에 잘 살펴봐야 한다.



## 2. 최적의 쪼개기  

최고의 GBDT 를 만들기 위해선 결국 어떤 기준으로 leaf를 펼처나갈지가 관건이다. 일반적으로 이 과정에선

최적의 기준을 찾기 위해 모든 데이터 포인트와 feature를 검토해야한다. 엄청난 연산을 요구하는 이 작업은 

당연하게도 데이터셋이 클 수록 더 많은 시간을 필요로 한다.



때문에 xgboost 와 LGBM은 이 연산시간을 단축하며 최적의 기준을 제시하기 위해 몇 가지 방법을 사용한다.



### 2-1. Histogram-based methods(xgboost and lightGBM)

변수를 평가하는데 걸리는 시간은 데이터가 얼마나 많이 쪼개져 있는지에 달려있다. 분포가 나눠져있다는 말은 

그만큼 최적의 기준을 찾기위해 계산해야하는 경우의 수가 많아진다는것과 같다. 하지만 대게 미미한 숫자들의 

분포(변화)는 성능에 큰 차이를 주지 못한다. 



Histogram-based methods는 이러한 사실을 바탕으로 feature 끼리 묶어 새로운 bin(묶은 개념)을 만든다.

이후, feature 별로 연산을 하는것이 아닌 bin 별로 연산을 진행한다. 모든 피쳐를 연산하는 것이 아닌 몇 개만

하위추출(subsampling) 해서  best split을 연산하는 방식이라고 생각하면 된다. 이 방법은  트리를 만들기 전에

feature 들을 묶기 때문에 학습속도를 향상시키고 연산의 복잡성을 줄일 수 있다.



![img](https://i2.wp.com/mlexplained.com/wp-content/uploads/2018/01/binned_split_gbdt.png?resize=300%2C260)

###### 								binning(묶는 방식)이 어떻게 연산을 줄일 수 있는지 보여주는 예시이다.

​				





참고자료 : https://mlexplained.com/2018/01/05/lightgbm-and-xgboost-explained/

