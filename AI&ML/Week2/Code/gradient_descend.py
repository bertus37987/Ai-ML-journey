#grdient descend in python

weight = 0.5
goal = 0.8
#Number of 'learning attempts'
attempts = 10
inputs = 0.5

for i in range(attempts):
    prediciton = weight * inputs

    error = (prediciton - goal) **2
    dierection_and_amount = (prediciton - goal) * inputs
    weight = weight - dierection_and_amount

print(prediciton)