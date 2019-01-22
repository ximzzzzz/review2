



- *Zeros initialization* -- setting `initialization = "zeros"` in the input argument.
- *Random initialization* -- setting `initialization = "random"` in the input argument. This initializes the weights to large random values.
- *He initialization* -- setting `initialization = "he"` in the input argument. This initializes the weights to random values scaled according to a paper by He et al., 2015.



zeros initialization

The weights W[l]W[l] should be initialized randomly to break symmetry.It is however okay to initialize the biases b[l]b[l] to zeros. Symmetry is still broken so long as W[l]W[l] is initialized randomly





random initialization (with large value)

Initializing weights to very large random values does not work well.Hopefully intializing with small random values does better. The important question is: how small should be these random values be? Lets find out in the next part!



he initialization

 "He Initialization"; this is named for the first author of He et al., 2015. (If you have heard of "Xavier initialization", this is similar except Xavier initialization uses a scaling factor for the weights W[l]W[l] of `sqrt(1./layers_dims[l-1])` where He initialization would use `sqrt(2./layers_dims[l-1])`.)



This function is similar to the previous `initialize_parameters_random(...)`. The only difference is that instead of multiplying `np.random.randn(..,..)`by 10, you will multiply it by 2dimension of the previous layer⎯⎯√2dimension of the previous layer, which is what He initialization recommends for layers with a ReLU activation.





Different initializations lead to different resultsRandom initialization is used to break symmetry and make sure different hidden units can learn different thingsDon't intialize to values that are too largeHe initialization works well for networks with ReLU activations.

