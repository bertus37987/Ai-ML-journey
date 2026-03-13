
#Added more weights
weights = [0.1, 0.2, 0]

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0

    for i in range(len(a)):
        output += (a[i] * b[i])
    return output


#Neural Network
def NeuralNetwork(inputs, weights):
    pred = w_sum(inputs, weights)
    return pred

toes = [8.5, 9.5, 9.9,] 
wlrec = [0.65, 0.8, 0.8] 
nfans = [1.2, 1.3, 0.5,]

inputs = [toes[0],wlrec[0],nfans[0]]

pred = NeuralNetwork(inputs, weights)
print(pred)