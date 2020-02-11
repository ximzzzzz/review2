### python pillow 내부 메소드 알아보기



##### 패키지 설치 및 import

```python
!pip install pillow
import PIL
```



##### PIL.Image

> 이미지를 만들거나 불러오거나 회전시키거나 등등 가장 기본이 되는 함수

```python
im = PIL.Image.open(PATH)
im.rotate(45).show() # 45도 회전시킨뒤 보여주기
im.thumbnail(size) #입력 사이즈크기로 썸네일만들기
im.save('filename') 

```







##### PIL.ImageColor

>   이미지에 사용할 컬러를 가져오거나 변환할 수 있다

```python
print(PIL.ImageColor.colormap) #dict 형식으로 {'컬러이름' : '컬러코드'} 를 보여준다
colors = list(PIL.ImageColor.colormap.values()) 
# 컬러코드를 모두 가져와 랜덤하게 사용할  수 있다.
```







##### PIL.ImageDraw

> 2D 이미지를 그린 객체를 반환한다.  이미지위에 표시를 하거나 리터치를 할때 주로 사용

```python
pil_image = PIL.Image.fromarray(이미지행렬).convert('RGB') #이미지를 나타내는 객체반환
draw = PIL.ImageDraw.Draw(pil_image) # 이미지 위에 그릴준비완료
draw.line(좌표)
draw.rectangle(좌표) 
draw.text(좌표, 할말) #이미지위에 다채롭게 낙서할 수 있다.
```



https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

##### PIL.ImageFont

> PIL.ImageDraw.text() 에 사용할 폰트를 정할 수 있다
>
> PIL.ImageFont.getsize() 메소드를 통해  이미지위에 폰트를 구현하기 위해  
>
> 필요한 사이즈를 구할 수 있다.



```python
try :
    font = PIL.ImageFont.truetype(PATH , size=5)
    #트루타입이나 오픈타입의 폰트를 5사이즈의 오브젝트로 불러온다
except IOError:
    print('해당 경로에 폰트가 없으므로 기본값으로 갑니다')
	font = PIL.ImageFont.load_default()
  
draw.text((start_x_point, start_y_point), 'things to say', font = font) 
#내가 원하는 글자로 글을 그릴수 있다.
```



