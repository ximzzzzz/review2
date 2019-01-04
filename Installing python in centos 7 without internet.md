 Installing python in centos 7 

# without internet

##### python version : 2.6.7



### 	Index

1. ##### Install putty

2. ##### Install anaconda3

3. ##### Create virtual environment

4. ##### Install python major package

5. ##### jupyter notebook remote setting









### 1. install putty

​	1)  go to putty download page and download for 64bit

​		https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

​	  ![img](file:///C:\Users\ximzz\AppData\Local\Temp\Hnc\BinData\EMB000030b478e6.png)



  	2) install putty by just clicking 'next'



  <img src="file://C:/Users/ximzz/AppData/Local/Temp/Hnc/BinData/EMB000030b478f4.png" width="500">



 

​	3) run putty and enter SERVER IP ADDRESS, PORT



#### <img src="C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1546617791339.png" width="500">



​	4) write session name on Saved Sessions, and click Save to memorize personal setting



# <img src="C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1546617998671.png" width="500">



### 2. install Anaconda3



​	1) go to Anaconda homepage, click Linux in the middle, and download 3.7 version

  ![img](file:///C:\Users\ximzz\AppData\Local\Temp\Hnc\BinData\EMB000030b478f9.png)



​	2)   send server anaconda file by pscp

​		-	run command

###   <img src="file:///C:\Users\ximzz\AppData\Local\Temp\Hnc\BinData\EMB000030b478fe.png" width="400">



​		-	enter code 

​	 'pscp -P <port> <path to anaconda> <<host@serverIPaddress:Targetpath>>

​	(in my opinion, /home/<user>/ is convenient for Target path)

<img src='C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1546618734261.png' >



​	3)	connect to server, then install received Anaconda.sh

​		- 	bash <downloaded Anacondafile>   

​	![1546618920575](C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1546618920575.png)



​		-	press enter     

​			![1546619018390](C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1546619018390.png)



​		-	command 'yes' to agree with terms                                    

![1546619101088](C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1546619101088.png)

 

​		-	confirm the install location(skip image)       

##### 		-	make sure  command 'yes' to set PATH  automatically



![1546619496297](C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1546619496297.png)



​		-	don't have to install VScode (skip image)				     

​	4) restart putty, and it would be successful if they understand when you command 'conda'

![1546619730957](C:\Users\ximzz\AppData\Roaming\Typora\typora-user-images\1546619730957.png)



### 3. Create virtual environment