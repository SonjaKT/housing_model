import random
import numpy as np

"""
Classes defining statistical distributions.
TODO: test these.
"""

class Dist(object):
    """A distribution object that you can sample from."""
    def sample(self):
        raise NotImplementedError


class UniformDist(Dist):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    
    def sample(self):
        val = random.random() # [0, 1) range
        val *= (self.max_value - self.min_value)
        val -= self.min_value
        return val


class NormalDist(Dist):
    def __init__(self, mean, std, min_value, max_value):
        self.mean = mean
        self.std = std
        self.min_value = min_value
        self.max_value = max_value
    
    def sample(self):
        val = random.normalvariate(self.mean, self.std)
        val = min(val, self.max_value)
        val = max(val, self.min_value)
        return val


class LogNormalDist(Dist):
    def __init__(self, mean, std, min_value, max_value):
        self.mean = mean
        self.std = std
        self.min_value = min_value
        self.max_value = max_value
    
    def sample(self):
        val = np.random.lognormal(mean=np.log(self.mean),
                                  sigma=self.std)
        val = min(val, self.max_value)
        val = max(val, self.min_value)
        return val