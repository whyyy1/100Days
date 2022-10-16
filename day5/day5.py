import numpy as np 

# single neuron 
n1Input = [1,2,3,2.5]
n1Weights = [0.2,0.8,-0.5,1]
bias = 2.0

def neuronOutput(l,w,b):
    total = 0
    for i in range(len(l)):
        total += (l[i]*w[i])
    total += b
    print(total)


neuronOutput(n1Input,n1Weights,bias)

inputs = [[1, 2, 3, 2.5], [2., 5., -1., 2], [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

#Adding another layer 
weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]
biases2 = [-1, 2, -0.5]

def layerOutput(i,w,b):
    layerO = []
    for weight,bias in zip(w,b):
        #zip() iterates over list simultaneously 
        sum = 0.00
        for k,l in zip(i,weight):
            sum += k*l
        sum += bias
        layerO.append(sum)
    return layerO


def neuralN(i,w,b):
    return np.dot(i,np.array(w).T) + b

layer1 = neuralN(inputs,weights,biases)
#Created a second layer aka hidden layer
layer2 = neuralN(layer1,weights2,biases2)
print(layer1)
print(layer2)
# In numpy use the .dot(weights,inputs) then add the bias to the new value



