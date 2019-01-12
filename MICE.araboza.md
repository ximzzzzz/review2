# MICE.araboza



### 1. what is MICE?

​	Multivariate Imputation by Chained Equations

![MICE ALGORITHM](https://cdn-images-1.medium.com/max/1600/1*Cw4F1pzPug0BT5XNdF_P3Q.png)



MAR(Missing At Random) : 

​	결측값이 해당 속해있는 자신의 변수와 관련있지 않고, 

​	다른 관측변수와 영향이 있다는 가정이다.

​	ex)



![MAR](https://ssl.pstatic.net/images.se2/smedit/2015/6/20/ib5a2wnze6ksr8.jpg)





MNAR

![MNAR](https://ssl.pstatic.net/images.se2/smedit/2015/6/20/ib5d5wj6rgjy40.jpg)

![MNAR2](https://ssl.pstatic.net/images.se2/smedit/2015/6/20/ib5da0y9k2ydzt.jpg)



단순대치법(Single Imputation)

다중대치법(Multiple Imputation)

​	단순대치법에서 표준오차가 과소추정되는 점, 계산의 난해함의 문제를 보완하고자 개발

​	단순대치법을 한 번 하지 않고 m번의 대치를 통한 m개의 가상의 자료를 만들어 분석하는 방법



​	대치단계(imputation step)

​		: mar가정

​		자료의 형태가 monotone일땐 모수적 모형으로 regression method, 

​		비모수적 모형으로는 propensity 등..

​		

​		non-monotone 자료일때는 일반적으로 MCMC(Markov Chain Monte Carlo) 사용

​		m이 많을 수록 좋지만 분석에 시간이 많이 소요되기때문에 일반적으로 3,5가 충분

​		

​	분석단계(Analysis step)

​		: 대치값을 분석하여 각 m개의 데이터셋에서의 세타를 추출한다.



​	결합단계(Combination step)

​		: 세타의 평균값을 구하여 최종 대체값을 넣는다.

​	