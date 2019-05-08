# python 에서 regular expression 활용하기



## 1. 리스트에서 re 활용하기

```python
list(filter(re.compile('정규표현식').search, 리스트))
```



### 2. pd.series 형식에서 정규표현식 활용하기

```python

df['columns'].str.extract
contains

```

