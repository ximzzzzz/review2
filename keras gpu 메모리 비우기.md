### keras gpu 메모리 비우기

학습하다보면 심심치 않게 발생하는 gpu 메모리에러

기존엔 커널을 리스타트하면서 사용했지만 세션만 정리하는 방법을 통해

리스타트없이 계속 사용할 수 있다는것을 알게 되었다!!



```python
import keras
from keras.backend.tensorflow_backend import set_session
from keras.backend.tensorflow_backend import clear_session
from keras.backend.tensorflow_backend import get_session
import tensorflow
import gc

# Reset Keras Session
def reset_keras():
    sess = get_session() #기존거 갖고와서
    clear_session() #비우고
    sess.close() #끈다
    sess = get_session() #그리고 새걸로 다시 갖고오기

    try:
        del classifier # this is from global space - change this as you need
    except:
        pass

    print(gc.collect()) # if it's done something you should see a number being outputted
    # garbage collect를 통해 안쓰는 메모리 확보!

    # use the same config as you used to create the session
    # 이부분은 입맛에 따라 커스터마이징 하면 됨
    config = tensorflow.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 1
    config.gpu_options.visible_device_list = "0"
    set_session(tensorflow.Session(config=config))
    
reset_keras()
```







