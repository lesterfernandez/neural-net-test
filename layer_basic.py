# Neural Networks from Scratch - P.2 Coding a Layer
# https://www.youtube.com/watch?v=lGLto9Xd7bU&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=2

inputs = [1, 2, 3, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87],
]
biases = [2, 3, 0.5]

output = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for edge_input, edge_weight in zip(inputs, neuron_weights):
        neuron_output += edge_input * edge_weight
    output.append(neuron_output + neuron_bias)

print(output)
