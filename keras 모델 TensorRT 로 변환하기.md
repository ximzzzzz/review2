# keras 모델 TensorRT 로 변환하기



프로젝트를 진행하며 케라스를 통해 모델을 만들었는데, 연산속도가 0.5 초 정도로 생각보다 오래걸렸다.

평소엔 문제없지만, 서비스특성상 가끔씩 1초 간격으로 연속해서 들어올 때도 있는 점을 고려했을때 

문제가 될 것이라 판단했다. 



모델이 무거운 것도 아니었지만 그래도 다 시도해 보자는 생각에  TensorRT를 사용해보기로 했다.



### 1. TensorRT 도커 설치

갓커......환경설정하며 드는 시간과 비용을 아끼기 위해 도커를 선택했다. 또한 설치 후에 파이썬을 인식 못

한다는 경우를 본 적이 있어 안정적으로 도커로 갔다



여기서 방황이 시작되는데,



nvidia에서 만든 tensorRT 도커 컨테이너를 받아 RUN 했다.

TensorRT 도커 이미지 버전은 아래 링크에서 확인 가능하니 필요한 버전 사용하면 된다.

https://docs.nvidia.com/deeplearning/sdk/tensorrt-container-release-notes/rel_19-08.html#rel_19-08



```python
# 19.07 버전의 python3 컨테이너
nvidia-docker run -it --name TensorRT nvcr.io/nvidia/tensorrt:19.07-py3
```

그 후 TensorRT  컨테이너에 Tensorflow와 같은 딥러닝 프레임워크가 설치되어있지 않다는 내용에 따라

python 을 설치했다.



```python
/opt/tensorrt/python/python_setup.sh
```



그리고 예제 코드에 맞춰 모델 변환을 시도해보려는데, 이상한 점을 찾았다.



FP16 정밀도로 최적화 해보기로 했다.

![img](https://hiseon.me/wp-content/uploads/2018/03/tensorrt-1.png)



우선,  케라스를 통해 학습한 모델을 불러와 frozen graph로 바꾸는 작업을 해야한다.

보통 모델을 저장할때 meta graph와 weights 들을 다 나누어 저장하고 함께 부르는 방식을 취하는데,

frozen graph는 그래프 그대로 weights 와 함께 얼려버리는 것을 뜻한다.



```python
# load keras model
from keras.models import load_model
model = load_model('path/yourmodel.h5')
```

```python
def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):
    from tensorflow.python.framework.graph_util import convert_variables_to_constants
    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        input_graph_def = graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = convert_variables_to_constants(session, input_graph_def, output_names, freeze_var_names)
        return frozen_graph
```

위 함수는 케라스 모델을 frozen graph 로 변경해주는 함수다.



```python
from keras import backend as K
#frozen_graph 형태로 만든뒤,
frozen_graph = freeze_session(K.get_session(), output_names = [out.op.name for out in model.outputs]) 

#그래프를 그대로 저장한다
tf.train.write_graph(frozen_graph, "./save_path/","model_name.pb", as_text=False )
```



그래프로 저장한뒤엔, Tensor RT를 통해 본격적으로 변환할 수 있다.



```python
import tensorflow as tf
from tensorflow.python.compiler.tensorrt import trt_convert as trt
import numpy as np
import time
with tf.Session() as sess:
    # First deserialize your frozen graph, 얼려놨던 그래프를 불러와준다
    with tf.gfile.GFile('./save_path/model_name.pb', 'rb') as f:
        frozen_graph = tf.GraphDef()
        frozen_graph.ParseFromString(f.read())
        
    # Now you can create a TensorRT inference graph from your
    # frozen graph:
    converter = trt.TrtGraphConverter(
	    input_graph_def=frozen_graph,
	    nodes_blacklist=['dense_3/Sigmoid:0'], 
        ### 중요 :  반드시 마지막노드와 인덱스를 함께 입력해줘야 한다.
        precision_mode='FP16', #FP16으로 입력
        use_calibration=True) #output nodes
    trt_graph = converter.convert()

    output_node = tf.import_graph_def(
    trt_graph,
    return_elements=["dense_3/Sigmoid:0"]) #위의 nodes_blacklist에 적었던 노드 고대로 적기
    start = time.time()
    yhat = sess.run(output_node, 
                    feed_dict={'import/lstm_1_input:0' : np.zeros((100000,11,192))})
    print(time.time() - start)
    print(yhat)
```

한번 그래프를 구축했다면 계속 사용하면서 추론 시간을 재볼 수 있다.

```python
sess = tf.Session()
with tf.gfile.GFile('./models/test_tf.pb', 'rb') as f:
        frozen_graph = tf.GraphDef()
        frozen_graph.ParseFromString(f.read())
        
# Now you can create a TensorRT inference graph from your
# frozen graph:
converter = trt.TrtGraphConverter(input_graph_def=frozen_graph,
    nodes_blacklist=['batch_normalization_27_1/concat:0'], 
    ### 중요 :  반드시 마지막노드와 인덱스를 함께 입력해줘야 한다.
    precision_mode='FP16', #FP16으로 입력
    use_calibration=True) #output nodes
trt_graph = converter.convert()

output_node = tf.import_graph_def(trt_graph, return_elements=["batch_normalization_27_1/concat:0"])
#output node 만들기 완료
```



```python
# 이 셀만 돌리면서 순수 연산시간이 얼마나 줄었는지 확인할 수 있다.
start = time.time()
yhat = sess.run(output_node, 
                feed_dict={'import/lstm_1_input:0' : np.zeros((100000,11,192))})
print(time.time() - start)
print(yhat)

```





TensorRT에서 가장중요한건 변환할 모델의 연산과 노드를 정확히 알고 있어야한다는 점이다.

특히 `nodes_blacklist=[]`에선 반드시 마지막 연산과 인덱스를 함께 붙여줘야한다.

나의 경우엔 마지막 연산이 세번째 히든노드에 Sigmoid를 activation 하는 것이기 때문에

'dense_3/Sigmoid:0' 으로 입력했다. 뒤의 `:0`은 operation index 다(대부분 :0 임)



그리고 마지막 sess.run 부분에서 feed_dict에 입력할 노드 역시 주의깊게 봐야한다

케라스에서 frozen graph로 변경할때 노드별로 'import/' 라는 전치사가 붙는걸로 알고있는데

때문에 여기서 입력노드의 이름은 'lstm_1_input:0' 이 아닌 `import/lstm_1_input:0`이 되는것이다.



기존 케라스 모델과 시간 비교를 했을때 INT8이 아님에도 불구하고 약 1/4 정도 빨라진것을 확인했다.





 

https://hiseon.me/data-analytics/tensorflow/tensorflow-tensorrt/