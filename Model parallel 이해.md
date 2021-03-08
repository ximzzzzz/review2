# Model parallel 이해



이 글은 [파이토치 튜토리얼](https://pytorch.org/tutorials/intermediate/model_parallel_tutorial.html)의 글을 바탕으로 학습한 내용임을 먼저 알립니다!

모델이 무거워 지며 Multi gpu 학습이 당연시 되는 요즘, DataParallel 위주의 병렬처리학습을 주로했지만

때떄로 발생하는 DataParallel 의 비효율성을 개선하기 위해 Model Parallel 필요성을 느꼈다. 

우선 DataParallel 단점을 간단히 알아보자



## 1.  DataParallel  이 비효율적일때

​	DataParallel을 효율적으로 사용하려면 각 gpu에 모델을 복제하고 input data를 나누어 학습 하는 방식이다. 

​	반대로 말하자면 모델이 개별 gpu 메모리 사이즈보다 클 경우 기대하는 속도만큼 빠르지 않다는 것이다.

​	(OOM이 되거나 학습이 안된다는 내용은 원문상에 없음)

​	이 경우, Model parallel을 통해 속도를 더욱 올릴 수 있다.



## 2. Model parallel 은 무엇이며 어떻게 해결하는가?

​	각 gpu에 모델을 복제하는 DataParallel 과 다르게, 하나의 모델을 multi gpu에 나누어 학습하는 방식이다.

​	예를들어 두개의 gpu와 10개의 레이어로 이루어져 있는 모델이 있다했을때, DataParallel은 각 gpu에 모델을 복제하고 

​	학습하는 방식이라면 Model Parallel은 5개의 레이어는 첫번째 gpu에 나머지 5개 레이어는 두번째 gpu에 분배한 뒤 

​	학습하는 방식이다.



## 3. 코드로 확인해보자



​	Resnet 아키텍쳐로 Model parallel을 확인해보자.

​	참고로 아래 코드에서 사용하는 resnet 라이브러리의 아키텍쳐는 크게

​	[ conv1, bn1, relu, maxpool, layer1, layer2, layer3, layer4, avgpool, fc] 순으로 구성되어있다.



```python
from torchvision.models.resnet import ResNet, Bottleneck
import torch
import torch.nn as nn
import torch.optim as optim

num_classes = 1000

class ModelParallelResNet50(ResNet):
    def __init__(self, *args, **kwargs):
        super(ModelParallelResNet50, self).__init__(Bottleneck, [3, 4, 6, 3], num_classes = num_classes, *args, **kwargs)
        # nn.Sequential로 기존 하나의 모델을 두개(seq1, seq2)로 나눈다.
        
        self.seq1 = nn.Sequential(
            self.conv1,
            self.bn1,
            self.relu,
            self.maxpool,
            
            self.layer1,
            self.layer2
        ).to('cuda:0')  # seq1은 0번째 gpu에 배정
        
        self.seq2 = nn.Sequential(
            self.layer3,
            self.layer4,
            self.avgpool
        ).to('cuda:1') # seq2는 1번째 gpu에 배정
        
        self.fc.to('cuda:1') # fc도 1번째 gpu에 배정
        
    def forward(self, x):
        # forward 과정 :  0번째 gpu에서 계산된 seq1의 output이 1번째 gpu로 가기위해 복사가 필요하다.
        x = self.seq2(self.seq1(x).to('cuda:1'))
        return self.fc(x.view(x.size(0), -1))

```



​	모델은 나눴지만 기존 DataParallel 에 비해 빨라질지는 의문스럽다. 한가지 gpu가 쓰이는 동안

​	나머지 하나의 gpu는 쉬고있기 때문이다. 보다 정확한 비교를 위해 학습을 위한 `train`함수를 만들고 테스트해보자

​	실제로 학습하는게 목표가 아니기때문에 input, gt 모두 랜덤하게 설정했다.

```python
import torchvision.models as models

num_batches = 3
batch_size = 120
image_w = 128
image_h = 128

def train(model):
    model.train()
    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001)
    # random labeling below
    one_hot_indices = torch.LongTensor(batch_size).random_(0, num_classes).view(batch_size, 1)
    
    for _ in range(num_batches):
        inputs = torch.randn(batch_size, 3, image_w, image_h)
        # onehot encoding
        labels = torch.zeros(batch_size, num_classes).scatter_(1, one_hot_indices, 1) 
        
        # forward pass
        optimizer.zero_grad()
        outputs = model(inputs.to('cuda:0'))
        # backward pass
        labels = labels.to(outputs.device)
        loss_fn(outputs, labels).backward()
        optimizer.step()
```



​	이제 timeit 을 통해 Model parallel과 Single GPU 성능을 비교해보자

```python
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
import numpy as np
import timeit

num_repeat = 10

stmt = 'train(model)'

# Model parallel test
setup = 'model = ModelParallelResNet50()' 
mp_run_times = timeit.repeat(stmt, setup, number=1, repeat=num_repeat, globals = globals())
mp_mean, mp_std = np.mean(mp_run_times), np.std(mp_run_times)

# Single gpu test
setup = 'import torchvision.models as models;'+\
        'model = models.resnet50(num_classes = num_classes).to("cuda:0")'
rn_run_times = timeit.repeat(stmt, setup, number=1, repeat = num_repeat, globals=globals())
rn_mean, rn_std = np.mean(rn_run_times), np.std(rn_run_times)

def plot(means, stds, labels, fig_name):
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(means)), means, yerr=stds,
           align='center', alpha=0.5, ecolor='red', capsize=10, width=0.6)
    ax.set_ylabel('ResNet50 Execution Time (Second)')
    ax.set_xticks(np.arange(len(means)))
    ax.set_xticklabels(labels)
    ax.yaxis.grid(True)
    plt.tight_layout()
    plt.savefig(fig_name)
    plt.close(fig)
    
plot([mp_mean, rn_mean],
    [mp_std, rn_std],
    ['Model Parallel','Single GPU'],
    'mp_vs_rn.png')
```

 	속도 테스트 결과는 아래와 같다



![mp_vs_rn](https://user-images.githubusercontent.com/44566113/110296248-76d19200-8035-11eb-8a25-ac659bf43bc2.png)



​	Single gpu 대비 4.02/3.75-1=7% 더 느린것을 확인할 수 있다. forward 과정에서 data를 다른 gpu로 복사하는 

​	과정에서 약 7%의 overhead가 있었다고 말할 수 있겠다.



## 4. Model parallel은 더 느린걸까?

​	하지만 앞선 내용처럼 forward 시에 일하지 않는 gpu idle time을 줄일 수 있다면 개선에 여지가 남아있다.

​	idle time을 줄이기 위한 한가지 방법은 학습에 사용되는 mini batch 를 나누어서(split) 파이프라인을 구성하는것이다.

​	즉 잘게 쪼개진(splitted) 첫번째 학습데이터가 seq1을 지나 seq2를 갈때, 두번째 학습데이터가 seq1에 들어가는

​	방식으로 촘촘하게 구성하는 방법이다. 이 경우 multi gpu는 동시에 일하게 된다.

```python
class PipelineParallelResNet50(ModelParallelResNet50):
    def __init__(self, split_size=20, *args, **kwargs):
        super(PipelineParallelResNet50, self).__init__(*args, **kwargs)
        self.split_size = split_size
        
    def forward(self, x):
        # 미니배치를 split_size 인자값으로 더 작게 나눈(쪼갠)다.
        splits = iter(x.split(self.split_size, dim=0))
        s_next = next(splits)
        s_prev = self.seq1(s_next).to('cuda:1') # 첫번째 input이 seq1을 지나 다른 gpu로 복사된다.
        ret = []
        
        for s_next in splits:
            
            s_prev = self.seq2(s_prev) # seq2, fc를 지나 rat에 담아둔다.
            ret.append(self.fc(s_prev.view(s_prev.size(0), -1)))
            
            s_prev = self.seq1(s_next).to('cuda:1') # 두번째 input은 바로 seq1으로 투입된다.
        
        s_prev = self.seq2(s_prev)
        ret.append(self.fc(s_prev.view(s_prev.size(0), -1)))
        
        return torch.cat(ret)
    
# timeit으로 시간을 비교해보자
setup = 'model = PipelineParallelResNet50()'
pp_run_times = timeit.repeat(stmt, setup, number =1, repeat=num_repeat, globals = globals())
pp_mean, pp_std = np.mean(pp_run_times), np.std(pp_run_times)

plot([mp_mean, rn_mean, pp_mean],
     [mp_std, rn_std, pp_std],
     ['Model Parallel', 'Single GPU', 'Pipelining Model Parallel'],
     'mp_vs_rn_vs_pp.png')
```

​	비교 결과는 아래와 같다.

​	![mp_vs_rn_vs_pp](https://user-images.githubusercontent.com/44566113/110296253-776a2880-8035-11eb-8091-47e90d5480c0.png)

​	

​	결과는 놀랍게도  Single GPU가 3.75/2.51-1=49% 더 오래 걸린다. 아직 100% 개선된건 아니지만 

​	 `split_size` 인자값을 통해 줄일 수 있는 여지가 있다. 위 결과를 직관적으로 해석해보자면 작은  `split_size`는 

​	작은 CUDA kernel을 실행시키며 idle time을 줄이는 반면, 큰  `split_size`는 상대적으로 긴 idle time을 

​	갖게되는것으로 볼 수  있다.

​	 `split_size`의 최적값은 여러 변수에 따라 달라 질 수 있으므로  그리드 서치와 같은 테스트를 통해 

​	직접 확인하는것이 좋다



```python
means = []
stds = []
split_sizes = [1, 3, 5, 8, 10, 12, 20, 40, 60]

for split_size in split_sizes:
    setup = "model = PipelineParallelResNet50(split_size=%d)" % split_size
    pp_run_times = timeit.repeat(
        stmt, setup, number=1, repeat=num_repeat, globals=globals())
    means.append(np.mean(pp_run_times))
    stds.append(np.std(pp_run_times))

fig, ax = plt.subplots()
ax.plot(split_sizes, means)
ax.errorbar(split_sizes, means, yerr=stds, ecolor='red', fmt='ro')
ax.set_ylabel('ResNet50 Execution Time (Second)')
ax.set_xlabel('Pipeline Split Size')
ax.set_xticks(split_sizes)
ax.yaxis.grid(True)
plt.tight_layout()
plt.savefig("split_size_tradeoff.png")
plt.close(fig)
```



![split_size_tradeoff](https://user-images.githubusercontent.com/44566113/110296255-7802bf00-8035-11eb-8bb0-5b8dbf41b609.png)

​	

​	위 경우 `split_size` 는 20이 최적이라고 판단된다.

