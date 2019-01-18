# MICE.araboza



### 1. what is MICE?

##### 	 Multivariate Imputation by Chained Equations

![MICE ALGORITHM](https://cdn-images-1.medium.com/max/1600/1*Cw4F1pzPug0BT5XNdF_P3Q.png)

### 2. Single imputation

##### 	단순대치법(Single Imputation)

​		hot-deck : 최빈치로 대체

​		mean : 평균값으로 대체

​		regression : 회귀식을 통한 대체



#### 	`: 표준오차가 과소추정되는 문제가 생김`



### 3. before MICE(assume)

##### ​	MAR(Missing At Random) : 

​		결측값이 해당 속해있는 자신의 변수와 관련있지 않고, 

​		다른 관측변수와 영향이 있다는 가정이다.

​		ex) 일주일 흡연양을 체크하는 문항(변수)에 결측값이 있길래 봤더니,

​		앞선 질문에 흡연여부 yes/no가 있었고 흡연자만 다음문항에 답변하라고 적혀있음



​			결측여부를 R ( 관측1, 결측 0)

​			결측변수 Y, 관측변수를 X라 가정시,



![MAR](https://ssl.pstatic.net/images.se2/smedit/2015/6/20/ib5a2wnze6ksr8.jpg)



​		- 해석 :  R(결측여부)에 상관없이 Y의 확률은 동일하다  



### 4. MICE

##### 	다중대치법(Multiple Imputation)



​	단순대치법에서 표준오차가 과소추정되는 점, 계산의 난해함의 문제를 보완하고자 개발

​	단순대치법을 한 번 하지 않고 m번 반복하여 m개의 가상의 자료를 만들어 분석하는 방법



​	i) 대치단계(imputation step)

​		-  MAR 가정

​		- 가능한 대체 값의 분포에서 추출된 서로 다른값으로 결측치를 처리한 복수의 데이터 셋을 생성

​		- 채워넣기 단계 : 모든 변수의 결측치를 변수의 순서대로 채운다. 앞서 채워진 변수가 다음 채워지는

​			변수의 독립변수로 활용되는 방식

​		- 대체단계 : 앞서 채워진 값들을 변수의 순서대로 대체하는 과정. 

​			대체된 데이터셋에서 결측치가 독립적인 추출이 될 때까지 시행한다.

​	<img src='https://user-images.githubusercontent.com/44566113/51376507-d9acfa00-1b4b-11e9-9de9-638e85b4b7c5.PNG'>

​		

​		- 대치 방법   

​			- 연속형 데이터 : PMM (Predictive Mean Matching)

​			- 이변량 데이터 : Logistic Regression

​			- 다변량 데이터 : Bayesian polytomous Regression     

​			- 순서형 데이터 : Proportional odds model 

​			- non-monotone 데이터 :  MCMC(Markov Chain Monte Carlo) , 대체모형에 대한 분포가정을 한다

​			

​		-  m이 많을 수록 좋지만 분석에 시간이 많이 소요되기때문에 일반적으로 3,5가 충분

​	

​	ii) 분석단계(Analysis step)

​		- 대치값을 분석하여 각 m개의 데이터셋에서의 세타를 추출한다. 

​		- 모수의 추정을 통해 세타를 구한다.	   

​	



<img src='https://user-images.githubusercontent.com/44566113/51255129-f3ccc800-19e5-11e9-9d8c-98090da0c2d0.png' >

​							<모수추정 예시>





​		iii) 결합단계(Combination step)

​		- 추정치의 평균값을 구하여 최종 대체값을 넣는다.

​	





참고. 설문자료의 결측치 처리방법에 대한 연구 : 다중대체법과재조사법을 중심으로 (고길곤, 탁현우)