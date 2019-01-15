# MICE.araboza



### 1. what is MICE?

​	Multivariate Imputation by Chained Equations

![MICE ALGORITHM](https://cdn-images-1.medium.com/max/1600/1*Cw4F1pzPug0BT5XNdF_P3Q.png)



MAR(Missing At Random) : 

​	결측값이 해당 속해있는 자신의 변수와 관련있지 않고, 

​	다른 관측변수와 영향이 있다는 가정이다.

​	ex) 일주일 흡연양을 체크하는 문항(변수)에 결측값이 있길래 봤더니,

​		앞선 질문에 흡연여부 yes/no가 있었고 흡연자만 다음문항에 답변하라고 적혀있음



​			결측여부를 R ( 관측1, 결측 0)

​			결측변수 Y, 관측변수를 X라 가정시,



![MAR](https://ssl.pstatic.net/images.se2/smedit/2015/6/20/ib5a2wnze6ksr8.jpg)



​		- 해석 :  R(결측여부)에 상관없이 Y의 확률은 동일하다  



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

​		비모수적 모형으로는 propensity 등 자료별로 다른 

​		

​		non-monotone 자료일때는 일반적으로 MCMC(Markov Chain Monte Carlo) 사용

​		m이 많을 수록 좋지만 분석에 시간이 많이 소요되기때문에 일반적으로 3,5가 충분

​		

​	분석단계(Analysis step)

​		: 대치값을 분석하여 각 m개의 데이터셋에서의 세타를 추출한다. 모수의 추정



​	결합단계(Combination step)

​		: 세타의 평균값을 구하여 최종 대체값을 넣는다.

​	