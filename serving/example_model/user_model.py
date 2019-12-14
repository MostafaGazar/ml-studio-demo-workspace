# class UserModel(object):
#
#     def __init__(self):
#         # Load your model here
#         pass
#
#     def predict(self, data):
#         # Your predication code goes here
#         pass

import numpy as np
import math


def f(x):
    return 1 / (1 + math.exp(-x))


# Inspired by Seldon
class UserModel(object):

    def __init__(self, intValue=0):
        self.class_names = ["proba"]
        assert type(intValue) == int, "intValue parameters must be an integer"
        self.int_value = intValue

        print("Loading model here")
        X = np.load(open("model.npy", 'r'))
        self.threshold_ = X.mean() + self.int_value

    def _meaning(self, x):
        return f(x.mean() - self.threshold_)

    def predict(self, X):
        print(X)
        X = np.array(X)
        assert len(X.shape) == 2, "Incorrect shape"

        return [[self._meaning(x)] for x in X]
