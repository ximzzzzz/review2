# TensorFlow 기본 강의



#### TENSORFLOW 사용하는 이유.EU

- 가장 많이 쓰고있다(contributors)



#### Tensorflow 기본개념

- node : opreation(연산)
- edge : arrays(tensor) -> 데이터셋이라고 생각할 수 있다



## Tensorflow mechanism

1. 그래프를 만든다
2. sess.run 을통해 그래프를 실행시킨다
3. 그래프안의 값들이 업데이트되거나 리턴한다



#### Tensorflow 기본실행

```python
import tensorflow as tf
hello = tf.constant('hello, ethan') #노드만들기
sess = tf.Session()
print(sess.run(hello)) #세션을 통해 노드를 실행시킨다
```



#### computational graph 만들기

- 더하기연산을 하는 텐서플로우 그래프를 만들어보자

  ```python
  node1 = tf.constant(3.0, tf.float32)
  node2 = tf.constant(4.0)
  node3 = tf.add(node1, node2) # == node3 = node1 + node2
  
  sess = tf.Session() #반드시 세션을 실행시켜야한다
  print(sess.run(node1,node2))
  print(sess.run(node3)) 
  ```


## placeholder

- 노드를 만들때 상수값이 아닌 변수로 지정해서 구조만 만들어놓을 수 있다

  ```python
  a = tf.placeholder(tf.float32)
  b = tf.placeholder(tf.float32)
  add_node = a + b
  
  sess.run(add_node, feed_dict={a:3 , b:4.5})
  sess.run(add_node, feed_dict={a:[1,3] , b:[2,4]})
  ```


### Tensor Ranks, Shapes



![1543302131471](C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1543302131471.png)

