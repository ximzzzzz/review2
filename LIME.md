$$
f : \mathbb{R}^d \to \mathbb{R}
$$

$$
f(x)
$$


$$
g \in G
$$

$$
\{0,1\}^d
$$

$$
\Pi_x(z)
$$

$$
\mathcal{L}(f,g,\Pi_x(z))
$$



  (measure of how unfaithful  $g$  is approximating  $f$  in the locality defined by  $\Pi_x$ )


$$
\xi(x) = argmin_{g \in G}\mathcal{L}(f,g,\Pi) + \Omega(g)
$$





Sampling for Local Exploration

 interpretable representation  $x^{‘} \in \{0,1\}^d$ 의 non-zero element를 랜덤하게 뽑아서 샘플을 만든다

 original representation $z \in R^d$ 의 예측값 $f(z)$ 를 구한다.

 샘플들과 모형에서 구한 레이블을 가지고 위의 Equation을 최적화하여 Explanation을 구한다.



## SP-LIME

 $W$ : $n\times d^{‘}$  Explanation Matrix.

- 각 인스턴스의 interpretable component의 local importance

- 예를 들어 linear model을 explanation으로 사용한 경우 $W_{ij} = \vert w_{g_{ij}}\vert$ 

  

$I_j$  : $W$의 $j$ 번째 컬럼의 global importance

- 많은 인스턴스를 설명할수록 global importance가 높다고 함

- linear model의 예에서는 $I_j = \sqrt{\sum_{i=1}^{n} w_{ij}}$ 로 정의 가능

  

coverage $c(V, W, I)$ 

- $W, I$ 가 주어졌을때 set $V$ 에 속한 인스턴스에 한번이라도 나타난 feature의 total importance

  

$$
Pick(W, I) = argmax_{V, \vert V \vert \le B} c(V, W, I)
$$


