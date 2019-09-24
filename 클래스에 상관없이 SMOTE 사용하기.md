# SMOTE



SMOTE 방식은 데이터균형이 안맞는 경우에 사용하는 알고리즘이지만

CLASS에 상관없이 그냥 SMOTE 방식을 써보고 싶어 직접 구현해 보았다!



```python
def Smote_alone(orig_df, n_nearest_neighbor=5):
    synthetic_data=[]
    for i in range(len(orig_df)):
        origin = orig_df[i]
        nearest_idx= {}
        except_myself = list(range(len(orig_df)))
        except_myself.remove(i)
        for j in except_myself:
            nearest_idx[abs(origin - orig_df[j])] = j  
        sorted_values = list(nearest_idx)
        sorted_values.sort()
        nn = sorted_values[:n_nearest_neighbor]
        chosen_value = np.random.choice(nn, size=1)
        chosen_idx = nearest_idx[chosen_value[0]]
        synthetic_value = origin + chosen_value * np.random.rand()
        synthetic_data.append(synthetic_value)
    return np.asarray(synthetic_data).reshape((-1,))
```

