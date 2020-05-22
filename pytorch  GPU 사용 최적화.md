## pytorch  GPU 사용 최적화

학습하다 놓치는 gpu 최적화!

1. Dataloader 최적화(workers 활용)

   gpu가 처리하는 시간과 Dataloader 가 배치데이터를 넘겨주는 타이밍이 맞아야한다

   Dataloader 에서 느리게 될 경우 gpu idle 타임이 길어져 고성능 gpu도 아무소용없게된다.

   

2. batch size 

   애초에 처리할 배치사이즈가 작을 경우,  Dataloader가 타이밍 맞게 넘겨줘도 gpu가 힘들이지 않고 처리하게 된다.

   이미지나 자연어 학습에선 과적합 우려보다는 학습이 느릴 우려가 더 크므로 OOM 뜨기 전까지 최대한 높게 

   batch size를 잡는걸 추천 한다

   

3. data parallel

   multi gpu 일 경우, 병렬처리를 잘 활용할 수록 속도가 증가한다. pytorch나 keras에서 `DataParallel` 과 같은

   병럴처리를 도와주는 메소드가 있지만 `distributed parallel`을 사용하는 것이 multi gpu를 최대한 활용하는 방법이다.

   