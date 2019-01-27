

베이지안 통계(베이즈 확률론)



1. probability :  평균이 정해져있을때 y를 추측하는것

2. likelihood : y가 정해져있을때 평균을 추측하는것, 모수가 표집값과 일관되는 정도를 나타내는 값

   MLE : 주어진 데이터에서 가장 가능성이 높은 mu값을 찾을 때 사용, 어떤확률변수에서 표집한 값들을 토대로 

   ​	그 확률변수의 모수를 구하는 방법.

    

   MLE 구하는 식 : 여러개의 독립적으로 관측된 y 의 각각의 likelihood의 곱으로 표현한다.


   $$
   {\mathcal {L}}(\theta |x)=P_{\theta }(X=x)=P_{1,\theta }(X_{1}=x_{1})P_{2,\theta }(X_{2}=x_{2})\cdots P_{n,\theta }(X_{n}=x_{n})
   $$

   

3. 사전확률  / 사후 확률

   

4. 베이즈정리 : 사전확률을 알고 있을때, 사건 발생후에 그 확률이 수정되거나 변할 수 있다

   



참고 

https://medium.com/@deepvalidation/%EB%B2%A0%EC%9D%B4%EC%8B%9C%EC%95%88-%ED%86%B5%EA%B3%84-%EB%91%98%EC%A7%B8-%EA%B1%B8%EC%9D%8C-b486aa23d68b



https://mlduck.tistory.com/3 (MCMC)