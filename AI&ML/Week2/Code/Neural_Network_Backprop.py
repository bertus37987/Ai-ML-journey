'''Here i will try to implement a simple error fixing, a learing algorithim in pure python and/or numpy im not sure yet !, Here i only will format the error,
Backpropagation i will be doing later.'''
import numpy as np

inputs = np.array([1.2])
weights = np.array([2.3])

#In the real world that would be real data from things that already happen, some kind of validation
true__outputs = ([2.3])

def NeuralNetwork(inputs, weights):
    outputs = inputs * weights
    return outputs

output = NeuralNetwork(inputs, weights)

#Here the mistake is calculated, the pow(2) is used to make the error alway positve and make larger errors be larger
error = (output - true__outputs) **2
print(error) # in this case 0.2116
'''The key understanding from this task is, that searching an error is the key problem to solve to make an neural network predict anything accuratly'''