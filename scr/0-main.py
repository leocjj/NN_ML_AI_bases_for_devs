#!/usr/bin/env python3

# 0. Neuron

import numpy as np

Neuron = __import__("0-neuron").Neuron

lib_train = np.load("data/Binary_Train.npz")
X_3D, Y = lib_train["X"], lib_train["Y"]
X = X_3D.reshape((X_3D.shape[0], -1)).T
np.random.seed(0)

# Should receive one image at a time of shape 1D vector (784, 1),
# equivalent to an image of (28, 28) pixels with one channel
neuron = Neuron(X.shape[0])
print(neuron.W)
print(neuron.W.shape)
print(neuron.b)
print(neuron.A)
neuron.A = 10
print(neuron.A)
