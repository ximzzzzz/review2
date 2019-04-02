# Oracle VM VirtualBox 하둡 설치하기



VirtualBox ver : 5.2.26

네트워크 : NAT 

os : CENTOS 7 (MINIMAL VERSION)



1. 인터넷이 안된다

   네트워크 연결이 되었다면 분명 로그를 출력하는데 아무런 반응도 없다....

   

   ```bash
   ping google.com
   ping 아는ip주소아무거나
   
   #안되는 경우라면 어느주소를 입력해도 조용할것이다
   
   ```

2. yum, bzip2 와 같은 필수 패키지?설치

   이정도로 미니멀한 버전일줄 몰랐지....

   ```bash
   yum install yum bzip2
   ```

   

3. 게스트확장설치가 안된다(마우스가 없다) 

   #### ***minimal 설치, gui환경이 아닐경우 마우스포인터가 없습니다.

   #### 강제로 만들어도 bash shell은 클립보드가 없기때문에 복붙이 불가합니다 

   wget 으로 자바랑 다 설치해야되는데 다운로드링크를 붙여넣기 할 수가 없다

   또한 커맨드환경에서 에러나 진행상황을 봐야되는데 마우스가 안되니 스크롤을 키보드로 올려야한다

   

   1) <http://download.virtualbox.org/virtualbox/> 접속

   2) 날짜보면서 대충 최근 버전 클릭 후, 

   ​	`Oracle_VM_VirtualBox_Extension_Pack-<버전>-.vbox-extpack`   파일 다운로드

   3) virtualBox 관리자에서 파일 - 환경설정-확장-파일추가 -> 업데이트

   4) 다시 위의 주소로 들어가 업데이트한 버전과 동일한 디렉토리 내에 있는 

   ​	` VBoxGuestAdditions_<버전>.iso` 파일 다운로드

   5) virtualBox 관리자에서 해당 버추얼머신 우클릭- 설정-저장소-컨트롤러:IDE -> iso파일추가

   

   6)가상머신 실행 후 터미널에서 입력

   ```bash
   $ mount -r /dev/cdrom /media
   $ cd /media
   $ ./VBoxLinuxAdditions.run #반드시 ./를 앞에 붙이자
   ```

   

   7)(가상머신 끈상태에서) virtualBox 관리자에서 설정-시스템-마더보드 중에서 '포인팅 장치'가 보인다

   ​	USB 태블릿 or USB 멀티터치 태블릿으로 설정 후 확인

   8)가상머신을 킨 뒤  상단 메뉴바에서 장치 - 클립보드 공유 - 양방향으로 설정

   

   여기까지 했는데도 안되면??(물론 나의 케이스 ㅎㅎ)

   

   9) 터미널에서 아래 파일 생성 및 내용 입력

   ```bash
   $ vi /etc/X11/xorg.conf.d/50-vmmouse.conf
   
   Section "InputDevice"
   Identifier "Mouse[0]"
   Driver "vmmouse"
   Option "Device" "/dev/input/mice"
   Option "Name" "VMware Pointing Device"
   EndSection
   
   ```

   

   여기까지하면 되야 한다 인간적으로

   

   그래도 만족스럽지 않다면?

   

   ## putty로 원격접속하자 속편하다 :)

   putty 원격접속방법 참고

   <http://blog.daum.net/blackrebit/6>



