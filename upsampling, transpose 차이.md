###  upsampling, transpose 차이



CNN 모델구조를 보면 

downsampling -> upsampling

encoder -> decoder

convolution -> deconvolution

와 같은 구조를 심심찮게 발견할 수 있는데



그때 사용하는 upsampling, transpose 함수가 헷갈리지 않도록 정리했다

#### layers.UpSampling2D

> 단순복제를 통해 데이터 사이즈를 키우는 방식

​	

​	예를들어 기존 2 x 2 사이즈의 행렬 [[1,2],[3,4]]가 있다 하자

```python
X = asarray([[1, 2],
			 [3, 4]])
```

​	여기서 4 x 4 사이즈의 행렬로 키우기 위해 layers.UpSampling2D 를 사용하자



```python
X = X.reshape((1, 2, 2, 1)) #학습용 이미지 shape(samples, height, width, channels)
model = Sequential()
model.add(UpSampling2D(input_shape=(2, 2, 1))) #upsampling2d 사용

yhat = model.predict(X) #직접 input을 넣은 뒤
yhat = yhat.reshape((4, 4)) #다시 우리가 원하는 4x4 행렬로 reshape하면
print(yhat)

#output
[[1. 1. 2. 2.]
 [1. 1. 2. 2.]
 [3. 3. 4. 4.]
 [3. 3. 4. 4.]]
```



위와 같은 결과가 나온다.

단순히 몸집을 뿔린 결과로 볼 수 있다.





#### layers.Conv2DTranspose

기존에 convolution 방식에 반대 방식으로 생각하면된다.

일반적으로 생각하는 convolution 연산(convolution forward)는 kernel size 와 filter 갯수를 정한 뒤

kernel이 stride수 만큼 sliding window를 하며 사이즈를 줄여나가는 방식이라고 하면,

**Transpose** 는 convolution 연산(convolution backward)을 똑같이 하지만 sliding window를 하며

shape 을 불려나가는 방식이라고 할 수 있다.



![img](https://cdn-images-1.medium.com/max/1200/1*BMngs93_rm2_BpJFH2mS0Q.gif)



```python
X = asarray([[1, 2],
			 [3, 4]])

X = X.reshape((1, 2, 2, 1))

#테스트를 위한 모델 생성
model = Sequential()
model.add(Conv2DTranspose(1, (1,1), strides=(2,2), input_shape=(2, 2, 1)))

# define weights that they do nothing
weights = [np.asarray([[[[1]]]]), np.asarray([0])]
# store the weights in the model
model.set_weights(weights)
# make a prediction with the model
yhat = model.predict(X)
# reshape output to remove channel to make printing easier
yhat = yhat.reshape((4, 4))
# summarize output
print(yhat)
```

