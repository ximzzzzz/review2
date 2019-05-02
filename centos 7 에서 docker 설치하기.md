# centos 7 에서 Docker CE 설치하기



### 1.기존 설치되었던 docker 삭제

```bash
$ sudo yum remove docker docker-client\
> docker-client-latest docker-common docker-latest docker-latest-logrotate \
> docker-logrotate docker-engine
```



### 2. repository 설치

####  2-1 필수 패키지 설치

```bash
$ sudo yum install -y yum-utils \
>  device-mapper-persistent-data \
>  lvm2
```



#### 2-2 setup the repository

```bash
$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```



### 3. Docker CE 설치

```bash
$ sudo yum install docker-ce docker-ce-cli containerd.io
```



### 4. Docker CE 시작

```bash
$ sudo systemctl start docker
```



* 첫 실행시에 아래와 같은 에러가 나는 경우가 있다.

  Job for docker.service failed because the control process exited with error code. See "systemctl status docker.service" and "journalctl -xe" for details.



​	-첫 실행일 경우라면 /var/lib/docker 파일을 모두 제거한 뒤 재실행하면 작동한다

```bash
$ rm -rf /var/lib/docker
```



​	-그게 아니라면 기존의 이미지가 모두 지워지기 때문에 반드시 로그확인 후 문제를 해결해야한다(자세힌모름ㅎ)



### 5. docker 권한설정

```bash
$sudo groupadd docker
$sudo usermod -aG docker $USER
```





### 6. tensorflow 공식 이미지 가져오기

###### * Usage : docker run [OPTIONS] IMAGE [COMMAND]



```bash
docker run -it -p 8888:8888 tensorflow/tensorflowyu
```

​	-i: interactive, -t: tty

​	keep stdin open / allocate a terminal
​	(옵션을 주지 않으면 컨테이너 안에서의 터미널을 볼 수 없어요.) 



​	-p: port 8888:8888

​	도커 호스트의 포트 : 컨테이너의 포트 

​	

​	이미지 이름의 형식은 /: 입니다.

​	tag name이 주어지지 않을 경우 default는 ‘latest’ 



​	[COMMAND]가 주어지지 않을 경우 tensorflow 이미지의 디폴트 실행 프로그램은 Jupyter notebook!



### 7. deep learning 전용 이미지 가져오기(ufoym/deepo:all-jupyter)

##### -  텐서플로우부터 주피터노트북 뿐 만아니라 cntk, keras, caffe, darknet 등 다양한 딥러닝 프레임워크가 구축된 이미지

##### - 개인적으로 tensorflow 공식 이미지보다 사용하기 편해서 선호한다



```bash
docker run ufoym/deepo:all-jupyter
```



### 8.customization (optional)

##### - 위 이미지는 텐서플로우2 버전이 설치되어있기 때문에 1버전으로 변환하여 사용했다(1도 아직 미숙한데;;)

##### - gpu버전을 실험해본 결과 1.13.1이 에러 없이 호환되었다!!

#####  



### 9. alias 설정하여 쉽게 접근하기

##### - 매번 번거롭게 입력해야하는 파라미터는 귀찮으니까 `.bashrc` 안에 alias로 등록해두자

```bash
cd ~/.bashrc

alias docker-jupyter=docker run -it -p 8888:8888 -v \ /home/docker/Notebook/:/home/docker/Notebook --ipc=host ufoym/deepo:all-jupyter \
jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token= --notebook-dir='/home/docker/Notebook'
```

