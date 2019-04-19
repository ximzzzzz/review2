# 파이썬 시각화 - 기본 꾸미기 



### 정말 간단하지만 훨씬 깔끔해지는 시각화 기본 꾸미기 

### 

### 1. Grid

도표의 배경에 반투명회색의 수직/수평선을 추가해준다. 간단한 코드한줄이지만 분위기가 달라진다.

`axis` 인자값을  `x,y, both` 등으로 선택하여 수직,수평,모두 줄 수 있다. 개인적으론 수평만 주는것을 환영

```python
plt.grid(True, axis=y);

```



### 	1-2. 그리드 배경색 바꾸기

​		그리드에 사용될 배경 색상을 바꿈으로써 좀 더 깔끔하거나 전문적인 느낌을 낼 수 있다.

​	 	{darkgrid, whitegrid, dark, white, ticks}

```py
sns.set_style('darkgrid')
```

​													`darkgrid`선택시 배경화면이 회색으로 바뀐다.

![plt.gridì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://seaborn.pydata.org/_images/aesthetics_9_0.png)





### 2. CMAP(Colormap) 활용하기



##### color map 의 종류는 아래 링크에서 확인 가능하다 

##### 원하는 컬러를 활용하면 데이터값에 따라 다른 컬러(명암)을 지정할 수 있다.

<https://matplotlib.org/tutorials/colors/colormaps.html>



![../../_images/sphx_glr_colormaps_002.png](https://matplotlib.org/_images/sphx_glr_colormaps_002.png)

##### 																							<컬러맵 예시>



문제는 0~1 사이의 데이터일 경우엔 cmap 인자값에 원하는 컬러맵 이름만 적어주면 되지만,

데이터 수치가 클 경우엔 컬러맵의 밝거나 어두운 한가지 색으로만 나타나 컬러의 연속성을 못살린다.

그래서 colormap의 표현범위안에 들 수 있도록 data normalize 작업이 필요하다

(실제 차트값이 normalize 되는건 아니다)



```python
import matplotlib as mpl

YlGn = get_cmap('YlGn') 
cNorm = mpl.colors.Normalize(vmin=0, vmax=max(데이터) #시각화데이터의 최대 값(value)를 넣는다.
scalarMap = mpl.cm.ScalarMappable(norm=cNorm, cmap=YlGn)
colorVal = scalarMap.to_rgba(시각화 데이터)
```

이렇게 normalize 한 데이터를 rgba에 매핑한 후(`colorVal`),  `color`인자에 넣어주면된다.



```python
my_dataframe['var'].plot(kind='bar', color = colorVal) 
#colormap 이 아닌 color인자에 입력해야한다!                                  
```



`matplotlib` 뿐 만 아니라 `seaborn` 에도 활용가능하다



```python
plt.figure(figsize=(20,10))
plt.grid(True)
sns.set_palette(colorVal) #요녀석이다, 아까 설정한 colorVal를 넣어주면된다.
sns.barplot(x= data['var'].index , y = data['var'].values);
```

