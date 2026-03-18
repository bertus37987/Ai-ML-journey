''' Inspired by the *sentdex* episode'''

import numpy as np
#New name for datasets i learnd(inputs for now)
X = np.array([[3.5, 2.3, 4.5, 6.7],
                   [2.0, 3.0, 5.0, 6.2],
                   [-1.5, 3.4, 6.6, 7.3]])



class NeuralNetwork:
    def __init__(self, n_inputs, n_neurons):
        #This eliminates the need for an transpose
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        #In this case the shape of bias will alyways be (1, numberofneurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

#Why the (4,3) for is the lenght of [0] of X an 3 is the number of neurons you want, not that exist
#Just to really make the point
layer1 = NeuralNetwork(4,3)
layer2 = NeuralNetwork(3,2)
layer3 = NeuralNetwork(2,5)
layer4 = NeuralNetwork(5,7)

layer1.forward(X)
layer2.forward(layer1.output)
layer3.forward(layer2.output)
layer4.forward(layer3.output)
print(layer4.output)