# CTC Decoder 이해하기





## 시작

---------

​	Speech Recognition이나 OCR에서 많이 사용하는 CTC.

​	너무 어려워서 잘이해했는지 확인해 보기위해 직접 이해하는 과정을 정리해봤다



## CTC

-----------

겉핥기식 개념은 간단하다. 중복된 문자와 blank를 제거한다. 

예를들어 "`__BBB_OOYYY_ `" 의 경우 중복과 blank를 제거하면 `BOY`가 된다.

급하게 필요할땐 여기까지만 이해해도 갖다 쓸수 있다.

하지만  조금만 곰곰히 생각해보면 수많은 이해가지 않는 부분이 생기기 시작한다.

정리하자면, 음성샘플 `x`와 transcript(label) `z` 가 주어졌다고 헀을때 `P(z|x)` 를 최대화 할수있는 분류기를 만들 수 있도록 probability와  decoding에 새로운 접근이 필요하다.



## Probability

----------

`p(z|x)` 확률을 구하기 위해선 path ($$ {\pi }$$) 개념에 대해 이해해야 한다.

~~transcript 가 'HOT' 라고 가정하고 layer output이 (time steps , num_labels) shape 으로 이루어져 있다 가정해보자 여기선 time steps 를 5, num_labels 를~~ 

path($$\pi$$) 는 중복과 blank를 지웠을때 z가 될 수 있는 모든 경로들을 말한다.

CTC 기법에선 각 time step이 조건부 독립을 가정하기 때문에 각각의 path는 time step 별 확률의 곱으로 표현할 수 있다.
$$
p\left( \pi |\mathbf{x} \right) =\prod _{ t=1 }^{ T }{ { y }_{ { \pi  }_{ t } }^{ t } }
$$
그리고 `p(z|x)` 확률은 path의 확률을 더하면 된다.
$$
p( \mathbf{l} | \mathbf{x} )=\sum _{ \pi \in { \cal{B}  }^{ -1 } \left( \mathbf{l} \right) }^{  }{ p\left( \pi | \mathbf{x} \right)  }
$$


말이 쉽지 time step이 길어질수록 가능한 path는 폭증하기 때문에 일일히 적용하기는 불가능해보인다.

하지만 HMM(히든 마르코프 모델)에서 착안한 forward algorithm, backward algorithm을 사용하면

재귀적으로 이전 계산을 활용하기때문에 가능하게 된다.



## Decoding

--------------

위와 같은 CTC loss를 통해 학습한 모델의 output을 decoding 하기 위해선 크게 max decoding(greedy decoding), prefix decoding 두가지가 있다.

1. max decoding(greedy decoding)

   단순히 time step별로 argmax를 취한값을 사용하면 된다.

   그 후 중복과 blank를 제거하여 decoded output 을 최종적으로 만든다.

   너무 간편하고 빠르지만 정확도가 떨어지는 단점이있다.

   그 이유중 하나는 Language model 을 사용할수 없기때문이다.

   예를들어  `fairy tale` 에서 `tale`과 `tail` 은 동음어이기때문에 소리만으로 구분하긴 어렵다.

   이때 greedy decoding은 앞의 fairy를 고려하지 않고 소리만으로 판단하기때문에 tail로 분류할 가능성이 상대적으로 높다.

     

2. prefix decoding

   위와같은 이유로  prefix decoding이 대안이 되는데, 마찬가지로 기본적인 아이디어는 단순하다

   <img src="https://i.imgur.com/bjbfVAV.png" alt="image-50px" style="zoom:25%;" />

   
   
   하지만 실제 알고리즘은 다소 사악한데...
   
   이해를 위해서 참고란에 있는 [Lasse Borgholt](https://medium.com/corti-ai/ctc-networks-and-language-models-prefix-beam-search-explained-c11d1ee23306) 님의 깃허브에있는 코드를 인용했다(포스팅상에 있는 코드는 indentation이 맞지않는 부분이 있어서 수정이 필요함)
   
   
   
   본격적인 설명에 들어가기전에  설명에서 사용할 기본개념에 대한 이해가 필요하다
   
   <img src="https://miro.medium.com/max/1688/1*JizQp-avRd0s6m-lwQEg7A.png" alt="Image for post" style="zoom: 67%;" />
   
   <그림1>
   
   
   
   The emission probability : output의 결과물로 해당시점의 해당 index의 확률을 말한다.
   
   위 matrix를 output의 결과물로 생각할경우 30 time steps 동안 [A-Z] 에  ['_', ' >' , '-']  3가지를 추가한(총 29 레이블) 전체레이블의 확률값이다. (30, 29) 사이즈
   
   위와같은 output 을  코드에서 `ctc` 로 표현하며, 이를바탕으로  4시점의 B로 판단할 확률은  `ctc[4][2]` 로 표현할 수 있다.
   
   
   
   The blank probability : 변수 $$P_b$$ 로 표현하며 해당시점에 해당 prefix(label이라 생각해도 좋다)를 가질수 있는 모든 path중에 마지막이 `blank` 로 끝나는 path들의 확률의 합이다.  말이 복잡한데 예를들어  $$P_b$$`[3]['b']` 는 3시점에 'b' 라는 label을 가질 path 중에 마지막이 `blank` 로 끝나는 path 들의 확률의 합이다.
   
   해당 path에는 `b--`, `-b-`, `bb-` 3가지가 있으므로 각 확률의 합을 통해 구할수 있다.
   
   
   
   The non-blank probability: blank probability와 반대의 개념이다. 변수 $$P_nb$$로 표현하며 해당시점에 해당 prefix를 가질수있는 모든 path중에 마지막이 `blank`로 끝나지 않는 path들의 확률합이다. 예를들어 $$P_nb$$`[3]['b']` 의 path는 `--b`, `-bb`, `bbb`  3가지가 있으므로 확률의 합을 통해 구할 수 있다.
   
   
   
   hyperparameters : alpha 는 language model 에 대한 비중, beta는 compensation weight, k는 beam width다. 
   
   
   
   ```python
   # step 1 initialization
   from collections import Counter, defaultdict
   
   O = ''
   Pb, Pnb = defaultdict(Counter), defaultdict(Counter)
   Pb[0][O] = 1
   Pnb[0][O] = 0
   A_prev = [O]
   ```
   
   
   
   0번째 스텝을 초기화한다. 처음엔 `''`(빈상태) 로 시작하며 Pb는 1, Pnb는 0의 확률을 부여했다.  '' 상태에서 다른 글자가 추가되는순간 중복과 blank를 제거하면 ''가 아니게되므로 Pnb는 0이 되어야한다.
   
   ​    
   
   ```python
   # STEP 2: Iterations and pruning
   	for t in range(1, T): #1
   		pruned_alphabet = [alphabet[i] for i in np.where(ctc[t] > prune)[0]] #2
   		for l in A_prev:
   			
   			if len(l) > 0 and l[-1] == '>':  # 3
   				Pb[t][l] = Pb[t - 1][l]
   				Pnb[t][l] = Pnb[t - 1][l]
   				continue  
   
   			for c in pruned_alphabet:
   				c_ix = alphabet.index(c)
                     # END: STEP 2
   ```
   
   
   
   #1 step별로 iteration을 하며 A_prev를 업데이트한다. 
   
   #2 <그림1> 의 matrix에서 보듯이 label은 많고 대부분은 확률이 아주 낮기 때문에 효율을 위해서 pruning을 해준다.
   
   #3 그 다음 prefix 의 요소들에 대해 pruned alphabet 들을 추가해보며 확률을 계산한다
   
   여기서 ' > '는 eos 같은개념으로 마지막 글자의 예측까지 마쳤다고 생각될경우 그다음 step에 예측하는 label 이다.
   
   만약 prefix 요소 중 하나의 마지막이 ' > '로 끝났다면 이번 step엔 추가된 정보가 없기때문에 이전 t-1 시점의 확률을 그대로 쓰고 추가 없이 마무리한다.
   
     
   
   
   
   ```python
               for c in pruned_alphabet:   
                   c_ix = alphabet.index(c)
                   # END: STEP 2
   
                   # STEP 3: “Extending” with a blank
                   if c == '%':     #1
                       Pb[t][l] += ctc[t][-1] * (Pb[t - 1][l] + Pnb[t - 1][l])
                       # END: STEP 3
   ```
   
   
   
   #1 여기서 '%'는 `blank` label을 지칭한다.  기존 prefix에서  '%' 를 추가할경우 forward algorithm으로 구할수 있는데,
   
   새롭게 추가되는 label이 `blank` 이므로 여기서 Pnb의 확률은 업데이트할수 없고 Pb의 확률만 업데이트한다.
   
   
   
   ```python
   				# STEP 4: Extending with the end character
   				else:
   					l_plus = l + c  #1
   					if len(l) > 0 and c == l[-1]:  #2
   						Pnb[t][l_plus] += ctc[t][c_ix] * Pb[t - 1][l]
   						Pnb[t][l] += ctc[t][c_ix] * Pnb[t - 1][l]
   				# END: STEP 4
   ```
   
   #1  pruned_alphabet이`blank`가 아닐경우 기존 prefix에 c를 덧붙여 확률을 구해본다.
   
    #2 c가 l[-1]과 같다는것은 결국 중복된 레이블을 예측했다는건데 (e.g. 기존 prefix  '-h' 에  'h' 를 추가하려할 경우 ) 
   
   이땐  중복된 레이블을 지우지 않고 포함시킨 확률과 중복된 레이블을 제거한 확률 두가지 경우의 수로 계산한다. 예를들어 `happy` 의 경우 중복된 레이블을 지우면 항상 hapy가 되기때문에 두가지 경우의 수를 고려한다.
   
   
   
   내가 이거마무리하고만다 
   
   
   
   
   
   
   
   

## 참고

-----------

[CTC Networks and Language Models: Prefix Beam Search Explained | by Lasse Borgholt | Corti | Medium](https://medium.com/corti-ai/ctc-networks-and-language-models-prefix-beam-search-explained-c11d1ee23306)

[Connectionist Temporal Classification - ratsgo's speechbook](https://ratsgo.github.io/speechbook/docs/neuralam/ctc#decoding)

