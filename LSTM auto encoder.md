## LSTM auto encoder 



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







