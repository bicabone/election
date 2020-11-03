from numpy.random import normal
import random


def sample_normal(mean, stdev):
    n = normal(mean, stdev) / 100
    if n < 0:
        return 0
    if n > 1:
        return 1
    return n


def coin_flip(probability) -> bool:
    uniform = random.uniform(0, 1)
    return uniform <= probability
