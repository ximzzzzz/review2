# datetime 활용하기!



## pd.datetime , datetime64 형태를 활용한 데이터 처리 방법



### 1. 시간별시각화



```python
plt.figure(figsize=(20,10))
plt.title('frequency by Hour')
danger_data.groupby(danger_data.dt.hour).count().plot(kind='bar',cmap='autumn')
plt.xlabel('Hour');
plt.grid(True,axis= 'y' );
```





### 2. 일별 시각화



```python
plt.figure(figsize=(20,10))
plt.title('frequency by Day',pad =10 )
plt.ylabel('count')
danger_data.groupby(danger_data.dt.day).count().plot(kind='bar')
plt.xlabel('Day')
plt.grid(True,axis= 'y' );
```





### 3. 요일별 시각화



```python
import calendar
danger_data_week = danger_data.apply(lambda x : x.weekday())
danger_data_week = danger_data_week.apply(lambda x : calendar.day_name[x])
danger_data_week.value_counts()

plt.figure(figsize=(20,10))
plt.title('frequency by week')
sns.barplot(x=danger_data_week.value_counts().index, y =danger_data_week.value_counts().values)
plt.xlabel('week days');
plt.grid(True,axis= 'y' );
```





### 4. 시간만 떼서 확인하고싶다면



```python
#data['신호수신시간']이 format = '%Y%m%d%H%M%S'형식의 데이터라고 할때 (ex'2019-05-15 12:22:29')

data['신호수신시간'].astype('datetime64').apply(lambda x : x.time()) #시간만 리턴한다.
#마찬가지로
data['신호수신시간'][4].month #월
data['신호수신시간'][4].minute #분
data['신호수신시간'][4].second #월 등 모두 가능하다
```





### 5. datetime 형태에서 int/str로 되돌리고 싶다면



```python
from datetime import datetime
datetime.strftime(데이트타임형태의 시간데이터, '%H%M%S')

data['datetime_column'].apply(lambda x : datetime.strftime(x, '%Y'))
```

```python

```



### 6. Timestamp 와 Timedelta를 활용한 연산

​	5일 전 날짜를 확인하고 싶을때!

```python
time = pd.Timestamp('2019-09-17')
time_5days_ago = time - pd.Timedelta('5D')
```

