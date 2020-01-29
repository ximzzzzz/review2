#### likelihood(가능도, 우도) , likelihood function(우도함수), MLE



**표기** : $f(x|\theta) = L(\theta|x) = L(\theta) = Pr[x|\theta]$  

**의미** : 관측치가 이미 주어졌을 때,  현재 알려지지않은 모수에서 해당 관측치가 나올 확률(likelihood)

​			likelihood를 연속형 함수로 표현한 것(likelihood function)

​			likelihood 중에 가장 큰 확률을 가진 모수를 추정하는것(MLE)



확률을 처음 공부할때 보통 고정된 확률($p$) 를 통해 결과확률($x$)을 계산했다.

예를들어, 동전을 5번 던졌을때, 앞면이 5번 나올 확률을 구할때,  우리는 이미 동전의 확률($p$)를 알고있다.

그리고 $p$를 통해 결과($x$)가 $\frac1{32}$ 라는걸 알 수 있었다.

likelihood 는 이와 반대로 관측치 $\frac1{32}$ , 즉 결과($x$)가 주어졌을때  $p$를 구하는것이다.

정리하자면 아래와 같다.



> 이미 알고있는 모수 $\theta$ (위 설명에선 $p$)	***--확률함수 $f(x)$-->***  결과구하기
>
> 이미 알고있는 결과 $x$							***--우도함수 $L(\theta)$-->***	주어진 결과를 가장 잘 표현하는 모수 $\theta$ 구하기





참고 : https://blog.naver.com/mykepzzang/221568285099





