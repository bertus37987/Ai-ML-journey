'''Thats my first real Neural Network, i will try to impliment:
-multiple outputs
-So that the Components, all recieving the same input data deliver different outputs
-The exercise is inspired by grokking deep learning
- Here the goal is using elementwise multiplication'''

import numpy as np

weights = np.array([0.3, 0.2, 0.9])
outputs = ([])
inputs = np.array([10,11,12])

def NeuralNetwork(inputs, weights, outputs):
    if len(inputs) != len(weights):
        return 1
    else:

     for i in range(len(inputs)):
      output = 0
      output = np.dot(weights[i], inputs[i])
      outputs = np.append(outputs, output)
    
    return outputs

outputs = NeuralNetwork(inputs,weights, outputs)
print(outputs)