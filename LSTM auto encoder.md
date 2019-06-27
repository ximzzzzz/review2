## 거꾸로 알아보는 LSTM Autoencoder 





### 1. 당장 사용하기



시계열 모델을 만들 때 단순히 시계열데이터를 입력값으로 넣어서 학습시키보다,

auto encoder를 통해 특징을 추출한 뒤, 학습을 진행할 경우 성능이 향상되었다는 논문결과가 있다.



 “[Time-series Extreme Event Forecasting with Neural Networks at Uber](http://roseyu.com/time-series-workshop/submissions/TSW2017_paper_3.pdf)” by [Nikolay Laptev](http://roseyu.com/time-series-workshop/), et al. 



![Details of LSTM Autoencoder for Feature Extraction](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2018/11/Details-of-LSTM-Autoencoder-for-Feature-Extraction.png)



해당 논문에선 일반 auto encoder가 아닌 LSTM encoder를 활용하여 시계열 데이터의 특징을 추출하엿는데,

해당 코드를 구현하며 공유해본다 ㅎㅎ

또한, LSTM 5개 층을 쌓아, 512 로 시작하여 32(64)까지 노드를 줄인것으로 볼 수 있다.



```python
from numpy import array
from keras.models import Model
from keras.layers import Input
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import RepeatVector
from keras.layers import TimeDistributed
from keras.utils import plot_model

n_in = train_x.shape[1] # time steps
features = train_x.shape[2] #variables

model = Sequential()
model.add(LSTM(512, input_shape=(n_in, features), return_sequences=True, activation='relu'))
model.add(LSTM(256, return_sequences =True, activation='relu'))
model.add(LSTM(128, activation='relu'))
model.add(RepeatVector(n_in))
model.add(LSTM(128, return_sequences = True, activation='relu'))
model.add(LSTM(256, return_sequences = True, activation='relu'))
model.add(LSTM(512, return_sequences = True, activation='relu'))
model.add(TimeDistributed(Dense(features)))

model.compile(optimizer='adam', loss='mse')

model.fit(train_x, train_x, epochs=300)
```



LSTM 층을 추가하는 과정에서 `activation`파라미터   디폴트 값과  'relu' 로 시도했을때, 

relu 가 초기 loss를 줄이는데 효과가 좋았다.



충분히 학습 시켰다면 decoder 부분을 떼어네고 encoder 부분만 stand alone으로 사용해야 한다.



```python
# standalone model
standalone = Model(inputs  = model.inputs, 
                   outputs = model.layers[2].output)
standalone.save('./standalone.h5')
```



output 의 인자값은 encoder 부분의 마지막부분이 되어야 하므로, `repeat vector` 레이어 바로 전 레이어의 인덱스를 입력해줘야 한다. 계산하기 헷갈린다면 

```python
model.summary() 
```

코드를 통해 모델 구조를 확인한뒤 해당 인덱스를 입력해주면 된다. 여기선 2를 사용했다.



### 2. 찬찬히 뜯어보기



급하게 돌려놨지만 원리와 사용법을 알아야 한다. 

살펴보아야 할 것은 `return_sequences`,  `RepeatVector`, `TimeDistributed` 세 가지다.

우선 아래 그림을 통해 LSTM Autoencoder에 대해 자세하게 들여다 볼 필요가 있다.



그림출처 : https://towardsdatascience.com/step-by-step-understanding-lstm-autoencoder-layers-ffab055b6352

![img](https://cdn-images-1.medium.com/max/1400/1*sWc8g2yiQrOzntbVeGzbEQ.png)



**첫번째,** 데이터셋 shape 은 LSTM 레이어에 들어가기 때문에 (n_samples, time_steps, features ) 모양으로 

되어있다고 가정할 때, input data는 (1, 3, 2) shape을 가진 하나의 데이터셋 샘플이다(그림에선 transpose 된 상태인데 시각적 표현을 위해 눕혀놓은것 같다 )

**두번째,** 각각의 LSTM layer는 time steps 만큼(여기선3) cell을 갖고 있는것을 볼 수 있다. 각 time step의 정보를 반영하기 위함인데, 이러한 LSTM layer를  계속 쌓아가기(stacked) 위해선 다음 LSTM layer 역시 동일한 time step의 cell을 가져야 한다.  이와 같이 LSTM layer를 쌓아 갈때 `return_sequences=True`를 사용한다.

 

![img](https://cdn-images-1.medium.com/max/2000/1*K5FAZ2au0WEh8y9x78Z8xQ.png)



`return_sequences=True`는 타임스탭별로 output을 모두 갖는 구조다. 때문에 3개의 t ime step일 경우 3개의 output이 생기게된다. 이러한 구조는 stacked 구조 뿐 만아니라, many to many 구조의 서비스를 개발할때 꼭 필요하다. 왼쪽 a는 True 인자값을 통해 3개의 output을 갖고, 다음 LSTM layer로 각각 연결되는것을 볼 수 있다.

반면, `return_sequences=False `인 오른쪽 b의 그림에선 마지막 cell의 output만 벡터의 형태로 갖는것을 볼 수 있다. 처음에 복잡했던 input 을 한가지 cell로 압축하였기 때문에 위 과정을 통틀어 `ENCODER`라고 한다.



**세번째, ** 오른쪽 그림 b 에서 output으로 나온 벡터를 다시 복사하는 `RepeatVector` 이 있다. encoding과정을 통해 요약된 핵심 정보는 `DECODER`과정을 통해 다시 input data로 복구 할 수 있어야한다.`RepeatVector`는 encoding 과 decoding 사이의 중간 가교 역할이며 time step을 맞추기 위해 단순복사를 시도한다.  

이 과정은 기존의 time step 의 갯수만큼 cell을 복사하는 과정으로 별거없다. 



**네번째**,  decoder 과정을 진행하기 위해 처음 encoder 과정처럼 LSTM cell 을 쌓아가는 과정이 필요하다.

encoder LSTM layer과 대칭모양을 이루게 하여 균형을 맞춘다. 물론 풍부한 표현을 위해 다시 `return_sequences`가 사용되어야 한다.



**다섯번째,**  input 데이터와 똑같은 구조를 만들기 위해 마지막 LSTM layer  다음에 `TimeDistributed` 레이어를 추가한다. 특별한 구조는 아니고 일반적인 hidden layer를 하나 만들어 행렬곱을 통해 기존 input data와 동일한 shape를 만들어 준다.  TimeDistributed` 의 인자값으론  input data feature의 갯수를 넣어주면 된다.

여기선 TimeDistributed(Dense(2))` 를 넣어주었다(처음에 2개였으므로)



이러한 과정을 통해 LSTM Autoencoder는 학습을 진행하게된다. 

여기까지만 보면 이렇게 무의미한 작업이 따로없다. 원본이 이미 있는데 원본과 똑같이 복제하는 모델을 만든다?

원본을 쓰면되지 왜 굳이? 





### 3. auto encoder 쓰는 이유





 

