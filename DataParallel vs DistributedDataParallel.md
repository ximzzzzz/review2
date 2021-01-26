# DataParallel vs DistributedDataParallel



쉽고 익숙한 DataParallel 과 낯설고 불편하지만 유용한 DistributedDataParallel 과의 간격을 줄여보자

파이토치 튜토리얼의 이해를 바탕으로 적은것이므로 틀린부분이 있을수 있다.  

-------

## Why?



1. DataParallel(앞으로 DP라 칭함 )이 보통 DistributedDataParallel(DDP라 칭함) 보다 빠르다

   DP는 단일 머신에서 단일 프로세스에 다중 스레드를 사용하는 방식이고, 

   DDP는 단일/다중 머신에 다중 프로세스를 사용하는 방식이다. DP는 다중 스레드를 사용하기 때문에 스레드 간 GIL contention이 불가피하고 iteration 마다 모델을 복제해야 하며, scattering 과 gathering 하는 Parallel 과정에서 오버헤드가 발생한다.

   

<img src="https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1585364509/gil_g47wzi.png" alt="Tutorial) Python Global Interpreter Lock - DataCamp" style="zoom: 80%;" />

​													<직관적인 GIL 설명 이미지>

2. 모델이 큰 경우 DDP는 model parallel을 사용하여 다중 gpu에 나눈다. 때문에 각각의 DDP 프로세스들은 model parallel 을 사용하며, data parallel 을 사용할 수 있다. 반면 DP는 model parallel을 사용하지 않는다.

   

## 출처 

https://pytorch.org/tutorials/intermediate/ddp_tutorial.html  

https://www.datacamp.com/community/tutorials/python-global-interpreter-lock 