# plt figsize 의 비밀



파이썬에서 대표되는 시각화 패키지 matplotlib. aka plt

plt를 사용하며 좀 더 크거나 작게보고싶을때, 한 번쯤 plt.figure(figsize=()) 를 써봤을 것이다.

figsize 에는 보통 상수값을 넣기때문에 같은 상수값을 넣으면 어디에서나 

같은 크기의 시각화 이미지가 만들어 질것이라 생각했다.



### 하지만,

코린이(코딩 어린이)의 착각이었다.

figsize를 상수로 입력해도 모니터 dpi 기준으로 resize후 보여주기 때문에 실제로 이 시각화도표를 데이터로

학습을 하거나 편집을 할경우, 사용환경에 따라 다른 사이즈의 이미지가 나오는 즐거움?을 맛 볼 수 있다.

심지어 같은 환경에서도 듀얼모니터를 사용하는 경우 어느쪽에서 표를만들고 저장했느냐에 따라 

해상도가 다르게 저장되는 것을 발견하게 된다.



예를들어, `plt.figure(figsize(3,2))` 를 통해 사이즈를 가로3, 세로2로 지정해줬다 하더라도

실제 모니터에 출력될 때는 (3/dpi), (2/dpi)로 resize 하여 출력된다.  

때문에 일관된 사이즈로 이미지를 출력하려면 원하는 size 뿐 만아니라 dpi도 고정값으로 지정해야한다.

또한, 기존에 사용하는 plt.figure() 가아닌 set_size_inches() 를 사용해야 한다.

참고로 사용모니터의 dpi는 검색하면 바로 체크할 수 있다.



```python
# w 가로길이 
# h 세로길이
# dpi = 사용자 모니터환경 dpi


fig = plt.figure(frameon=False);
fig.set_size_inches((float(w)/dpi) ,(float(h)/dpi)) 
plt.원하는 plot
```


이미지를 저장할때도 dpi를 관리해줘야 한다



```python
plt.savefig('img_dir', format = 'png', dpi = dpi )
```



마지막으로, dpi와 사이즈를 지정해줄 경우 어떤환경에서도 일관된 해상도로 만들 수 있지만

폰트크기나 선굵기 등의 차이로인해 미묘하게 차이가 생긴다. 이유는 정확하게 모르지만

아마 고정 사이즈로 resize되면서 폰트나 선도 함께 resize 되기때문에 변형이 생기는 것 같다.



##### -> 오늘 해결방법을 알게됨. 미묘한 변화도 거슬릴 경우 `fig.tight_layout()`을 써줘면 된다.

```python
fig = plt.figure(frameon=False, dpi=dpi, figsize =((float(w)/dpi) ,(float(h)/dpi)));
fig.tight_layout()
```



원래 tight_layout()은 도표간에 폰트가 겹치거나 title과 subtitle이 겹치는 등 여러개의 도표가 겹치지않도록

간격을 맞춰주는 메소드인데, 어떤 이유로 위와같은 기능을 하는지는 모르겠다. **하지만 시도한 것 중 유일하게**

**다른 환경(다른 모니터 뿐 만아니라 다른 PC)에서도 동일한 사이즈와 도표를 만들었다.**

