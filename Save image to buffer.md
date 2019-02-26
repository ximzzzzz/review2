# Save image to buffer



이미지를 일일히 저장하고 로드해야할 상황이 왔을 때 사용하면 유용하다!

아래 예시를 통해 바로 확인 해보자



```python
import io

#scatterplot 이미지를 버퍼에 저장해보자!

plt.scatter(x = my['X'], y = my['Y'])

#버퍼 소환
buf = io.BytesIO()
#버퍼에 저장하기
plt.savefig(buf, format='jpg');
buf.seek(0)

#버퍼변수는 리스트에 담아 사용할 수도 있다.
buf_list =[]
buf_list.append(buf)

#이미지파일일 경우 getvalue() 함수를 통해 binary로 변환할 수 있다

buf_binary = buf.getvalue()
```



알고보면 진짜 별것 아니지만 모르는 사람에게는 가뭄에 단비가 될 거라 생각한다!