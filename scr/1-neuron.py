#!/usr/bin/env python3
""" 0x01. Classification """
import numpy as np


class Neuron:
    """Class that defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """
        Defines a single neuron performing binary classification
        :param nx: number of input features to the neuron

        __W: The weights vector for the neuron. Upon instantiation, it should be initialized using a random normal distribution.
        __b: The bias for the neuron. Upon instantiation, it should be initialized to 0.
        __A: The activated output of the neuron (prediction). Upon instantiation, it should be initialized to 0.
        Each private attribute should have a corresponding getter function (no setter function).
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """getter method"""
        return self.__W

    @property
    def b(self):
        """getter method"""
        return self.__b

    @property
    def A(self):
        """getter method"""
        return self.__A
