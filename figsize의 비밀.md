# plt figsize 의 비밀



파이썬에서 대표되는 시각화 패키지 matplotlib. aka plt

plt를 사용하며 좀 더 크거나 작게보고싶을때, 한 번쯤 plt.figure(figsize=()) 를 써봤을 것이다.

figsize 에는 보통 상수값을 넣기때문에 같은 상수값을 넣으면 어디에서나 

같은 크기의 시각화 이미지가 만들어 질것이라 생각했다.



### 하지만,

코린이(코딩 어린이)의 착각이었다.

figsize를 상수로 입력해도 모니터 dpi 기준으로 resize후 보여주기 때문에 실제로 이 시각화자료를 통해

학습을 하거나 편집을 할경우, 사용환경에 따라 다른 사이즈의 이미지가 나오는 즐거움을 맛 볼 수 있다.



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



