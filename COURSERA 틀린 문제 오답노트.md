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