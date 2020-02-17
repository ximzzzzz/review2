## Yolo v3



### 들어가기 전 알아야할 개념



##### AP(Average Precison) 

> precision, recall 을 y축, x축으로 그린 뒤 ,  threshold를 조정함에 따라 
>
> precision, recall이 어떻게 변화하는지를 나타낸 그래프(curve)에서
>
> 그래프 아래 면적(area under curve)을 말한다



​	ROC 커브의 AUC와 비슷한 개념이지만 특이도(specificity)와 민감도(sensitivity) 대신,

​	precision 과 recall 을 사용한다는 점이 다르다





#####  mAP(mean Average Precision)

> 각 클래스 별로 AP 를 구한 뒤 평균 낸 수치





loss 는 sum of Sqared error 사용

ground truth가 가장많이 오버랩되는 bounding box는 confidence score가 1이 되어야한다

다른 Faster R-CNN 등 과 다르게 ground truth 하나당 내가 예측한 bounding box 하나만 갖게하기



Multiclass classification : 최종분류할때 softmax 함수를 사용하는 것과 다르게, 각 클래스값에 

​	sigmoid를 사용함으로써, multiclass classification 을 가능하게 했다

​	person > women 과 같이 hierarchical 한 multi class를 분류할 수 있게 했다



anchor box는 3가지 스케일에 대해서 3가지 바운딩박스를 사용한다

​	N * N * (3 *( 4 + 1+ 80 ))



anchor box를 뽑아내는 과정이 특이하다

​	faster rcnn 128, 256, 512 scale 3개, 1:1 , 1:2, 2:2 aspect ratio 3개 (ssd 도 비슷)

​	but, yolo는 현재 데이터셋에서 k means clusting 한다(내가 찾고자하는 특징을 잘 반영한 anchor box)

​	총 9 개를 clustering 한뒤에 3개씩나눠서 3개 디텍터에 배분한다



backbone은 darknet 53을 사용한다



negative mining  : 수천개에 bounding box를 뽑게되는데 background class 를 두면 imbalanced data가 되고 이걸 해결하기 위해 쓰는 방법



multi scaling training : 다양한 이미지를 집어넣어서 물체의 크기가 크고 작은걸 커버해줌

data augumentation, batch normalization 



