## 순환형(stateful) LSTM 사용시 유의사항 in keras 



LSTM 사용하는 과정에서 stateful 파라미터를 사용할 때 유의사항을 적어봤다.



- `stateful = True` 는 이전 시퀀스(T-1)의 연산값이 현재 시퀀스(T)의 초기값으로 전달되는 것이다.

  초기값으로 전달된다는 말은  input data가 아니다.  그냥 이전 시퀀스의 연산값을 전달 받는다는 것이다.

- `stateful` 파라미터는 `unroll`과 아무런 상관없다.