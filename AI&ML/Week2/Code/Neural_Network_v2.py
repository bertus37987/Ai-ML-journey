'''I will try to implement a real Neural Network Now,
and yes i know that i'm using the same weights ands bias twice'''
import numpy as np

inputs = np.array([[2.7,3.3,2.7],
                  [4.3, -2.7, 3.3],
                  [4.3,2.2, 1.4]])
bias = np.array([3.4, -2.2, -3.3])

weights = np.array([[3.3, 4.5, 6.6],
                       [1.3, 4.9, 3.3],
                       [3.3, 3.6, 6.7]])


def NeuralNetwork(inputs, weights, bias):
    output = np.dot(inputs, weights) + bias
    layer2 = np.maximum(0, np.dot(output, weights) + bias)
    return output, layer2
outputs, layer2 = NeuralNetwork(inputs, weights, bias)


print(layer2)