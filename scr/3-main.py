#!/usr/bin/env python3

# 3. Neuron Cost
# Cost: the function that calculates the loss, which the network is minimising during training.
# In most cases of supervised learning, that would be the distance between the predicted value,
# and ground truth labeled value

import numpy as np

Neuron = __import__("3-neuron").Neuron

lib_train = np.load("data/Binary_Train.npz")
X_3D, Y = lib_train["X"], lib_train["Y"]
X = X_3D.reshape((X_3D.shape[0], -1)).T

np.random.seed(0)
neuron = Neuron(X.shape[0])
A = neuron.forward_prop(X)
cost = neuron.cost(Y, A)
print(cost)
