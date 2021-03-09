# Distributed Data Parallel 를 위한 기초용어 



### 1. world_size

> `group` : group of processes
>
> `world_size` : number of processes in this `group`. 
>
> ​					The total number of processes, so that the master knows how many workers to wait for.
>
> ​					usually the number of GPUs you are using for distributed training

### 2. rank

> `rank` : unique id for each process in the `group`

### 3. local_rank

> GPU id inside one process





출처 : https://stackoverflow.com/questions/58271635/in-distributed-computing-what-are-world-size-and-rank

​			https://pytorch.org/tutorials/intermediate/dist_tuto.html