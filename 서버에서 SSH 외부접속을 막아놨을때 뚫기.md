## 서버에서 SSH 외부접속을 막아놨을때 뚫기



하둡, 스파크 등등 분산처리환경에서 connection refused 에러가 뜰경우!





## 1.외부접근을 막아놨는지 확인!



- hosts.deny에서 접근을 모두 막아놔서 그럴지 모른다!



당장 들어가서 확인해 보자

```bash
$ vi /etc/hosts.deny 
```



`sshd:all ` , `ALL:ALL` 를 주석처리 해준다!!

```bash
#....
#sshd:ALL
#ALL:ALL
```



변경사항적용해주고~

```bash
$ source /etc/ssh/hosts.deny
```



- hosts.allow 도 확인해보자

```bash
#모두허용해준다
ssh:ALL:allow
sshd:ALL:allow
```





## 2.방화벽끄기

```bash
#재부팅시에도 방화벽끄기
$ systemctl stop firewalld

#or
$ systemctl mask firewalld

#or
$ systemctl disable firewalld
```







## 3.ssh_config 수정하기

/etc/ssh/ssh_config 파일에 들어가 Port를 추가한다

```bash
$ vi /etc/ssh/ssh_config

#주석처리된 Port를 풀어준다
#~~~~~
#~~~~
#
Port 22
Port 1234 #원하는 포트 추가 개방 가능
```



## 4.SELinux 끄기



```bash
sudo setenforce 0 
```





### 다시 시도해보자!!

### 단 보안에 취약해지니 주의하기바람