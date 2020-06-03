## pytorch



##### 기본 텐서에서 Transpose 를 한 뒤에도 순서는 변하지 않는다. id를 통해 확인해보면 그대로 인것을 알 수 있다.

즉, 텐서에 변화를 주어서 새로운 변수를 할당하더라도 새로운 메모리를 할당하는것이 아니라 storage로 부터

모양만 바꾼다



- contiguious 한 텐서는 storage 상에서 점핑? 없이 순서대로 참조하기때문에 메모리 접근 성능을 향상시킨다.

  ```python
  tensor_c = tensor.contiguous()
  tensor_c.is_contiguous() #True
  ```



- torch 연산중 `연산명_` 형식으로 되어있는 메소드는 inplace 역할을 한다.

  ```python
  # img 변수를 이미지 파일을 로드한 텐서라고 가정할 경우,
  img.sub_(0.5) #이미지 전체 텐서에 0.5를 뺀다
  img.div_(0.5) #전체 텐서에 0.5를 나눈다
  imb.sub_(0.5).div_(0.5) #0.5를 빼고 다시 0.5로 나눈다. Nonetype error 뜨지않음! 
  ```



- tensor.scatter_(dim, index, src) 함수는 tensor의 인덱스에 원하는 숫자를 꽂아준다. onehot 때 유용!

  ```python
  batch_size = 5
  onehot_dim = 10
  # make (5, 10) shaped tensor
  onehot_encoded = torch.FloatTensor(batch_size, onehot_dim).zero_().to('cpu') 
  #원핫인코딩 전 label 값이라 가정하자  (5,1) shaped tensor
  onehot_value = torch.LongTensor([[2],[4],[7],[1],[6]]).to('cpu') 
  onehot_encoded.scatter_(dim = 1, index = onehot_value, value = 1)
  # onehot_encoded 의 dimension (5) 와 onehot_value 의 dimension (5) 가 동일하기 때문에
  # onehot_encoded 의 첫번째 dimension(dim = 1 이므로)에 onehot_value의 값을 인덱스로 하여 
  # value 값 1을 추가시킨다.
  
  #-------output--------
  tensor([[0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
          [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.]])
  ```




- torch.no_grad() : 학습을 하지 않을때(추론시) autograd 기능을 끈채로 forward 연산을 진행하는걸 말한다

  > torch.no_grad() impacts the autograd engine and deactivate it. It will reduce memory usage and speed up computations but you won’t be able to backprop (which you don’t want in an eval script).
  >
  > with torch.no_grad() temporarily set all the requires_grad flag to false.

  