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



FP32 정밀도로 최적화 해보기로 했다.

![img](https://hiseon.me/wp-content/uploads/2018/03/tensorrt-1.png)



우선, 그래프를 실행하는 함수를 정의하고, Frozen graph로 만드는 함수를 정의했다.



```python
def run_graph(gdef, dumm_inp):
  """Run given graphdef once."""
  gpu_options = cpb2.GPUOptions(per_process_gpu_memory_fraction=0.50)
  ops.reset_default_graph()
  g = ops.Graph()
  with g.as_default():
    inp, out = importer.import_graph_def(
        graph_def=gdef, 
        return_elements=["input_layer_name", "output_layer_name"]) 
    	#변환하려는 케라스 모델의 input layer과 output layer의 이름을 알고 있어야 한다. ex) 			'lstm_12_input', 'dense_51/sigmoid' 
    inp = inp.outputs[0]
    out = out.outputs[0]
  with csess.Session(
      config=cpb2.ConfigProto(gpu_options=gpu_options), graph=g) as sess:
    val = sess.run(out, {inp: dumm_inp})
  return val

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



케라스로 만든 모델을 불러온 뒤, Frozen graph로 만들었다.

```python
from keras.models import load_model
from keras import backend as K

model = load_model('./my_model.h5')
frozen_graph = freeze_session(K.get_session(), output_names = [out.op.name for out in model.outputs])
```



그리고  TensorRT 그래프로 변환작업을 시작하려는데..

```python

inp_dims = (10000, 11, 198)
dummy_input = np.random.random_sample(inp_dims) #input shape에 맞게 dummy data만들고

orig_graph = frozen_graph

int8_calib_gdef = trt.create_inference_graph(
  input_graph_def=orig_graph,
  outputs=["dense_51/Sigmoid"], #output layer name 을 입력해준다.
  max_batch_size=inp_dims[0],
  max_workspace_size_bytes=1 << 20,
  precision_mode="FP32",  # TRT Engine precision "FP32","FP16" or "INT8"
  minimum_segment_size=2  # minimum number of nodes in an engine
)

# int8_calib_gdef = trt.create_inference_graph(
#     input_saved_model_dir = './KTT_Data/models/tf_autoencoder/saved_model.pb',
#     output_saved_model_dir = './KTT_Data/models/tf_autoencoder_output')


o1 = run_graph(orig_graph, dummy_input)
_ = run_calibration(int8_calib_gdef, dummy_input)

int8_graph = trt.calib_graph_to_infer_graph(int8_calib_gdef)


start = time.time()
o1 = run_graph(orig_graph, dummy_input)
print('first : original : ',time.time() - start)
start = time.time()

o2 = run_graph(int8_calib_gdef, dummy_input)
# o2 = run_graph(int8_graph, dummy_input)
print('second : transformed : ',time.time()- start)
print( np.array_equal(o1, o2))
```





https://hiseon.me/data-analytics/tensorflow/tensorflow-tensorrt/