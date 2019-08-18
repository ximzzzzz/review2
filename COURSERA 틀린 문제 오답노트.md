# COURSERA 틀린 문제 오답노트





### 4. CNN 



##### Q: The following equation captures the computation in a ResNet block. What goes into the two blanks above?


$$
a^{[l+2]} = g(W^{[l+2]}g(W^{[l+1]}a^{[l]} + b^{[l+1]})+b^{l+2} + \text{_______ }) + \text{_______}
$$

###### 





###### A :  *a*[*l*] and 0, respectively



##### Q: In order to be able to build very deep networks, we usually only use pooling layers to downsize the height/width of the activation volumes while convolutions are used with “valid” padding. Otherwise, we would downsize the input of the model too quickly.







###### A: False





##### Q: Which ones of the following statements on Residual Networks are true? (Check all that apply.)



- Using a skip-connection helps the gradient to backpropagate and thus helps you to train deeper networks

- The skip-connections compute a complex non-linear function of the input to pass to a deeper layer in the network.

- A ResNet with L layers would have on the order of L^2*L*2 skip connections in total.

- The skip-connection makes it easy for the network to learn an identity mapping between the input and the   output within the ResNet block.





###### A: 1,4





##### Q: Which ones of the following statements on Inception Networks are true? (Check all that apply.)



- Inception blocks usually use 1x1 convolutions to reduce the input data volume’s size before applying 3x3 and 5x5 convolutions.
- A single inception block allows the network to use a combination of 1x1, 3x3, 5x5 convolutions and pooling.
- Making an inception network deeper (by stacking more inception blocks together) should not hurt training set performance.

- Inception networks incorporates a variety of network architectures (similar to dropout, which randomly chooses a network architecture on each step) and thus has a similar regularizing effect as dropout.





###### A:  1,2









##### Q: Suppose you are using YOLO on a 19x19 grid, on a detection problem with 20 classes, and with 5 anchor boxes. During training, for each image you will need to construct an output volume y*y* as the target value for the neural network; this corresponds to the last layer of the neural network. (y*y* may include some “?”, or “don’t cares”). What is the dimension of this output volume?





###### A: 19 * 19 * ?







##### Why do we learn a function d(img1, img2)*d*(*i**m**g*1,*i**m**g*2) for face verification? (Select all that apply.)



##### Neural style transfer is trained as a supervised learning task in which the goal is to input two images (x*x*), and train a network to output a new, synthesized image (y*y*).





##### In neural style transfer, what is updated in each iteration of the optimization algorithm?







### 5. Sequence models



##### Q: Let E*E* be an embedding matrix, and let o_{1234}*o*1234 be a one-hot vector corresponding to word 1234. Then to get the embedding of word 1234, why don’t we call E * o_{1234} in Python?



- It is computationally wasteful.

- The correct formula is E^T* o_{1234}*E**T*∗*o*1234.

- This doesn’t handle unknown words (<UNK>).

- None of the above: calling the Python snippet as described above is fine.











###### A:  It is computationally wasteful.





Q: Suppose you have a 10000 word vocabulary, and are learning 500-dimensional word embeddings. The word2vec model uses the following softmax function:


$$
P(t∣c) = {e_t^{θ^Te^c} \over ∑^{10000}_{t'=1}e^{θ_{t'}^Te_c}}
$$


Which of these statements are correct? Check all that apply.



- *θ_t* and *e_c* are both 500 dimensional vectors.

- *θ_t* and *e_c* are both 10000 dimensional vectors.

- *θ_t* and *e_c* are both trained with an optimization algorithm such as Adam or gradient descent.

- After training, we should expect *θ_t* to be very close to *e_c*  when *t* and *c* are the same word.



  







###### A : 

###### 	θ_t* and *e_c* are both 500 dimensional vectors,

###### 	θ_t* and *e_c* are both trained with an optimization algorithm such as Adam or gradient descent.