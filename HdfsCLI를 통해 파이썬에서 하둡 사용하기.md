# HdfsCLI를 통해 파이썬에서 하둡 사용하기



## 1. HdfsCLI 설치

- #### pip를 통한 설치

  pip install  hdfs



- #### 직접설치

  다운로드

​	https://files.pythonhosted.org/packages/96/4e/f82bd349c7893e1595429ecc95233369bc33c9a26e4859991439bfa01c1f/hdfs-2.2.2.tar.gz

​	

​	압축풀기

```bash
tar xvf hdfs-2.2.2.tar.gz	
cd ./hdfs-2.2.2
```



​	빌드업 및 설치

```bash
python setup.py build
python setup.py install
```





## 2. HdfsCLI 사용



- #### 클라이언트 호출

  ```python
  from hdfs import InsecureClient
  
  hdfs_cli = InsecureClient('http://IP or HOSTNAME:PORT')
  # IP주소를 적어도되고, HOSTNAME을 적어도 가능하다
  ```


- #### 하둡서버내에 폴더만들기

  ```PYTHON
  hdfs_cli.makedirs('/temp/newfolder', permission=777)
  # 하둡서버내 폴더를 지정해준다, permission 미입력시 322(-rx/-r-/-r-) 디폴트로 생성 
  ```


- #### 하둡서버내에 업로드하기

  ```python
  hdfs_cli.upload('/temp/newfolder/', './iris.csv')
  # hdfs_cli.upload(hdfs_path, local_path)
  ```


- #### 하둡서버내에 파일생성하기

  ```python
  hello_list = ['hello1','hello2']
  world_list = ['world1','world2']
  df = pd.DataFrame({'hello':hello_list, 'world':world_list})
  
  
  with hdfs_cli.write('/tmp/example3.csv', encoding='utf-8') as writer:
      df.to_csv(writer)
     
  #안전한 세션종료를 위해 with구문과 함께 사용하길 권장
  ```



- #### 하둡서버내에서 로드하기

  ```python
  with hdfs_cli.read('tmp/df_test.csv', encoding='utf-8') as reader:
      df = pd.read(reader)
      print(df)
  ```



- #### 하둡서버에서 가져오기(download)

  ```python
  hdfs_cli.download('/tmp/df_test.csv', './download_folder/', overwrite=True)
  # download(hdfs_path, local_path)
  # overwrite=True 할경우 덮어씌운다
  ```



- #### 하둡서버폴더 삭제하기

  ```python
  hdfs_cli.delete('/tmp/df_test.csv', reculsive=False)
  #reculsive=True 일경우 하위폴더도 모두 삭제한다
  ```


## 3. Advanced usage

- #### document 참고

​	https://hdfscli.readthedocs.io/en/latest/index.html

​	