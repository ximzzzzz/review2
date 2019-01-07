Installing python in centos 7 

# without internet

##### python version : 3.6.7



### 	Index

1. ##### Install putty

2. ##### Install anaconda3

3. ##### Create virtual environment

4. ##### Install python major package

5. ##### jupyter notebook remote setting









### 1. install putty

​	1)  go to putty download page and download for 64bit

​		https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

​	  ![img](https://user-images.githubusercontent.com/44566113/50758967-09841400-12a7-11e9-9357-5fd84a44a7ea.png)





  	2) install putty by just clicking 'next'



​			     <img src="https://user-images.githubusercontent.com/44566113/50758968-0a1caa80-12a7-11e9-94c8-9ae552353349.png" width="500">		





 

​	3) run putty and enter SERVER IP ADDRESS, PORT



<img src="https://user-images.githubusercontent.com/44566113/50758969-0a1caa80-12a7-11e9-9862-da52e0298a55.png" width="500">





​	4) write session name on Saved Sessions, and click Save to memorize personal setting



<img src="https://user-images.githubusercontent.com/44566113/50758970-0a1caa80-12a7-11e9-9365-bae5e1fcb79e.png" width="500">





### 2. install Anaconda3



​	1) go to Anaconda homepage, click Linux in the middle, and download 3.7 version

![img](https://user-images.githubusercontent.com/44566113/50758972-0ab54100-12a7-11e9-82a8-1d158808e1b4.png)







​	2)   send server anaconda file by pscp

​		-	run command

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