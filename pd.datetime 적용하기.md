# pd.datetime 으로 시각화 하기!



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
data['신호수신시간'].astype('datetime64').apply(lambda x : x.time())
```





### 5. datetime 형태에서 int/str로 되돌리고 싶다면



```python
from datetime import datetime
datetime.strftime(데이트타임형태의 시간데이터, '%H%M%S')

data['datetime_column'].apply(lambda x : datetime.strftime(x, '%Y'))
```

```python

```

