# Neural Networks from Scratch - P.3 The Dot Product
# https://www.youtube.com/watch?v=tMrbN67U9d4&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=3

import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87],
]
biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases
print(output)
