# python 에서 regular expression 활용하기



## 1. 리스트에서 re 활용하기

```python
list(filter(re.compile('정규표현식').search, 리스트))
```



### 2. pd.Series 형식에서 정규표현식 활용하기

```python
#df['columns'] 는 pd.Series 형태라 가정한다.
df['columns'].str.extract('exp', regex=True)


```



### 3. pd.Series 형식에서 정규표현식을 통해 빠르게 데이터 변경하기

```python
#df['columns'] 는 pd.Series 형태라 가정한다.
df['columns'].replace(regex = '정규표현식', value='바꾸고싶은값')
```

