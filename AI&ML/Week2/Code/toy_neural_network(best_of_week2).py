''' This is the best Neural Network of week 2'''
import numpy as np

inputs = np.array([3.3, 5.6, 4.44])
weights = np.array([1.2, 3.0, 1.9])

alpha = 0.01

training_duration = 10
goal_predicition = 10


for i in range(training_duration):
    prediciton = np.dot(inputs, weights)
    derivative = prediciton - goal_predicition
    error = prediciton - goal_predicition
#Fehler von mir: der Gradient entscheidet ob es hoch oder runter geh
#Kein **2 erlaubt
    gradient = error * inputs

    weights = weights - alpha * gradient
    print(f"Prediction {i}: {prediciton}")
         
#final prediction
print(f"{prediciton}")
