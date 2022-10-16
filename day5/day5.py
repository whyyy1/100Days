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

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

def layerOutput(i,w,b):
    layerO = []
    for weight,bias in zip(w,b):
        #zip() iterates over list simultaneously 
        sum = 0 
        for k,l in zip(i,weight):
            sum += k*l
        sum += bias
        layerO.append(sum)
    print(layerO)


layerOutput(inputs,weights,biases)


# In numpy use the .dot(weights,inputs) then add the bias to the new value

