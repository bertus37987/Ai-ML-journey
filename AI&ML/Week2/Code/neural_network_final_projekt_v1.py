''' Inspired by the *sentdex* episode but i modyfied parts
for example i wanted to use relu not sigmoid'''

import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()
#New name for datasets i learnd(inputs for now)
X = np.array([[3.5, 2.3, 4.5, 6.7],
                   [2.0, 3.0, 5.0, 6.2],
                   [-1.5, 3.4, 6.6, 7.3]])

X, y = spiral_data(100, 3)



class NeuralNetwork:
    def __init__(self, n_inputs, n_neurons):
        #This eliminates the need for an transpose
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        #In this case the shape of bias will alyways be (1, numberofneurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        #Relu dierectly intigrated in forward
        self.output = np.maximum(0, np.dot(inputs, self.weights) + self.biases)

#Why the (4,3) for is the lenght of [0] of X an 3 is the number of neurons you want, not that exist
#Just to really make the point
#Now im using a real dataset

layer1 = NeuralNetwork(2, 5)

layer1.forward(X)
print(layer1.output)