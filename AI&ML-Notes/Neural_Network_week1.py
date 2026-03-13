'''This Example is from 'Grokking deep learning' '''

# Weights
weight = 0.1
#Neural Network
def NeuralNetwork(input, weight):
  pred = input * weight
  return pred
#Dataset
toes = [8.5, 3.5, 9.2, 4.4]
input = toes[0]

pred = NeuralNetwork(input, weight)

print(pred)

