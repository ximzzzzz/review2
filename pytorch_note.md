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

  

  