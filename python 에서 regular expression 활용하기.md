# python 에서 문자열 검색하기



## 1. 정규표현식  

####  리스트에서 re 활용하기

```python
list(filter(re.compile('정규표현식').search, 리스트))
```



#### pd.Series 형식에서 정규표현식 활용하기

```python
#df['columns'] 는 pd.Series 형태라 가정한다.
df['columns'].str.extract('exp', regex=True)
```



####  pd.Series 형식에서 정규표현식을 통해 빠르게 데이터 변경하기

```python
#df['columns'] 는 pd.Series 형태라 가정한다.
df['columns'].replace(regex = '정규표현식', value='바꾸고싶은값')
```





## 2. 정규표현식 안쓰고 확인하기(str.contains)

```python
#df['columns'] 는 pd.Series 형태라 가정한다.
df['감사메세지'] = ['축하합니다','감사합니다','행복하세요','축하ㅊㅋ']
df['감사메세지'].str.contains('축하') # [True, False, False, True] 반환

# 두 단어 이상으로 검색하고 싶을 경우
df['감사메세지'].str.contains('축하|감사') # [True, True, False, True] 반환
```

