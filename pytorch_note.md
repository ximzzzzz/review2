## pytorch



##### 기본 텐서에서 Transpose 를 한 뒤에도 순서는 변하지 않는다. id를 통해 확인해보면 그대로 인것을 알 수 있다.

즉, 텐서에 변화를 주어서 새로운 변수를 할당하더라도 새로운 메모리를 할당하는것이 아니라 storage로 부터

모양만 바꾼다



##### contiguious 한 텐서는 storage 상에서 점핑? 없이 순서대로 참조하기때문에 메모리 접근 성능을 향상시킨다.

```python
tensor_c = tensor.contiguous()
tensor_c.is_contiguous() #True
```



