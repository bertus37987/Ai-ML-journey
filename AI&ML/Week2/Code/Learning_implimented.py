#Weights and Inputs (made up)
weight = 0.5
inputs = 0.5
goal = 0.8
#Steps for the Correction -> to reach *goal*
step = 0.005
#Learning Attempts
learning_attempts = 1000 #Number of learning attempts

for i in range(learning_attempts):
    prediction = inputs * weight
    error = (prediction - goal) **2

    up_prediction = inputs * (weight + step)
    down_prediction = inputs * (weight - step)
    
    error_up = (up_prediction - goal)**2
    error_down = (down_prediction - goal) **2

    if error_up > error_down:
        weight = weight - step
    elif error_up < error_down:
        weight = weight + step #For visual else would be better, but im not 100% sure here
    

print(prediction) #Stimmt fast mit goal überein
''' I had an small error here i forgot the **2 that shows how important it is that the number stays positive and lager errors get larger'''