# Installing python in centos 7 

# without internet for Data science

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

```bash
pscp -P <port> <path to anaconda> <host@serverIPaddress:Targetpath>
```



​	(in my opinion, /home/<user>/ is convenient for Target path)

<img src='https://user-images.githubusercontent.com/44566113/50758973-0ab54100-12a7-11e9-896b-325310ce7071.png' width='850' >





​	3)	connect to server, then install received Anaconda.sh

​		- 	bash <downloaded Anacondafile>   

<img src="https://user-images.githubusercontent.com/44566113/50758974-0b4dd780-12a7-11e9-8ac5-48bf021fdc61.png" width='850'>

 



​		-	press enter     

​			<img src='https://user-images.githubusercontent.com/44566113/50758975-0b4dd780-12a7-11e9-94a9-f0a84af32afd.png' width='850'>





​		-	command 'yes' to agree with terms                                    

<img src='https://user-images.githubusercontent.com/44566113/50758976-0b4dd780-12a7-11e9-84dc-7091a244514e.png' width='850'>



 

​		-	confirm the install location        

<img src='https://user-images.githubusercontent.com/44566113/50758977-0b4dd780-12a7-11e9-967f-58d3b657bd01.png' width='850'>

 

##### 				-	make sure  command 'yes' to set PATH  automatically



<img src='https://user-images.githubusercontent.com/44566113/50758979-0be66e00-12a7-11e9-9de6-9baa0e3dabc7.png' width='850'>





​		-	don't have to install VScode	     

<img src='https://user-images.githubusercontent.com/44566113/50758980-0be66e00-12a7-11e9-9ff9-3302eedf6bc2.png' width='850'>

 				     

​	4) restart putty, and it would be successful if they understand when you command 'conda'

<img src='https://user-images.githubusercontent.com/44566113/50758981-0be66e00-12a7-11e9-87f1-85c78939bff1.png' width='850'>





### 3. Create virtual environment

​	1) create virtual environment by enter command below



```bash
conda create -n <virtual env> python==3.6.7
```



<img src="https://user-images.githubusercontent.com/44566113/50758982-0c7f0480-12a7-11e9-86db-1209a301a327.png" width='850'>					



​	2) activate virtual envirionment 

```bash
conda activate <virtual env>
```

​	you can see head point is changed to virtual env

<img src='https://user-images.githubusercontent.com/44566113/50758983-0c7f0480-12a7-11e9-8a49-725a6b61f8c4.png' width='800'>





### 4. Install python major package



​	1) in this case, assume we can use internet from other computer.

​	so download major packages for DataScience and then move to server

​	

 * ##### if don't want to follow this procedure manually, you can also download at once on


​	2) first of all, download package file including dependencies with command below 

​	from other computer(require installing anaconda)

```bash
conda install <package name> --download-only 
```

​	

​	3) you should check downloaded files in `anaconda3/pkgs/`, and copy to 

​	new folder `pkgs_down`

​	don't forget to copy dependencies as well

​	(don't recommend to copy `pkgs`at once, due to dependency problem)



​	4) after download major packages, move to server through `pscp` command

```bash
pscp -P <PORT> <./pkgs_down/*> <host@serverIPaddress>:<./anaconda3/pkgs/> 
```



​	5) check out moved files in server correctly, and install packages offline on server

```bash
conda install --offline <package>
```

<img src='https://user-images.githubusercontent.com/44566113/50758986-0d179b00-12a7-11e9-8526-36a6b522df04.png' >





### 5. jupyter notebook remote setting