### KERAS FUNCTIONAL modeling example



케라스는 모델 아키텍쳐를 구성할 수 있도록 sequential과 functional 두가지 방식을 제공하고 있다.

기존에 직관적이고 편하다는 특징때문에 sequential을 사용했지만, 

인풋을 두군데로 하거나 아웃풋을 두군데로 하는등 모델을 커스텀하는데 있어 제약조건이 많기 때문에 

functional 방식을 사용해봤다.



특히 이번 데이터의 경우 시계열 어딘가에 있는 특정 패턴을 발견하는 것이 분류 정확도에 큰 역할을 하기때문에

CNN 과 GRU를 함께 섞어서 만들었다.



#### 모델구조 도식화



![캡처](https://user-images.githubusercontent.com/44566113/72869491-d03f0a80-3d28-11ea-8279-55de6af541a8.JPG)





```python
# architecture

filters = 32
kernel_size = 7
n_timesteps = train_x.shape[1]
n_features = train_x.shape[2]
n_outputs = train_y.shape[1]

input_layer = Input(shape=(n_timesteps, n_features))
cnn_layer = Conv1D(filters , kernel_size, padding='same', activation='relu')(input_layer)
cnn_layer = Conv1D(filters , kernel_size, padding='same', activation='relu')(cnn_layer)
cnn_layer = MaxPooling1D(pool_size=2)(cnn_layer)
cnn_layer = Flatten()(cnn_layer)
cnn_layer = Dense(32, activation='relu')(cnn_layer)
cnn_layer = BatchNormalization()(cnn_layer)
cnn_layer = Dropout(0.2)(cnn_layer)

gru_layer = GRU(32, input_shape=(train_x.shape[1], train_x.shape[2]), return_sequences=True)(input_layer)
gru_layer = GRU(32, return_sequences=False)(gru_layer)
gru_layer = Dense(32, activation='relu')(gru_layer)
gru_layer = BatchNormalization()(gru_layer)
gru_layer = Dropout(0.2)(gru_layer)

merge_layer = concatenate([gru_layer, cnn_layer])
output = Dense(n_outputs, activation='sigmoid')(merge_layer)

model = Model(inputs = input_layer, outputs = output )
```









