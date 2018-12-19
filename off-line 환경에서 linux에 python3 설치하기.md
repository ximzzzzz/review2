# off-line 환경에서 linux에 python3 설치하기



1. ##### (윈도우)python-버전.tar 파일을 다운로드 받는다.

2. ##### (윈도우)putty를 설치한후 `pscp` 를 통해 서버로 설치파일을 전송한다

   ```cmd
   pscp c:\python-3.6.7.tar root@110.244.24.100: /root/python/
   ```

3. #####  (리눅스)압축을 푼 뒤, configure를 실행해 컴파일한다.

   ```bash
   ./configure
   ```

4. #####  (리눅스)만약 c 컴파일러가 없다면 $PATH$에 c compiler가 없다는 에러메세지를 받게된다.

5. ##### (리눅스)오프라인 상태에서 설치할 예정이기 때문에, yum이나 wget이 아닌, rpm을 다운받고

   ##### 이동식저장장치를 통해 추후 설치서버에 공급한다.

   ```bash
   yum install yumdownloader
   yumdownloader gcc 
   ```


6. python3와 python2를 동시에 가지고 있는경우, pip3를 통해 python3 라이브러리가 다운가능하다


7. 파이썬 3.6이상의 버전의 경우, venv가 기본으로 설치되어 있기 때문에 

   따로 virtualenv를 pip로설치하지 않아도 된다