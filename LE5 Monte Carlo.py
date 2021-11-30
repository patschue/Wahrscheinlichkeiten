# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:17:10 2021

@author: schue
"""

def MonteCarloNormal():
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal
    import numpy
    mean = 10
    std = 5
    size = 10
    my_generator = numpy.random.default_rng()
    result = my_generator.normal(mean, std, size)
    print(result)
    return result
    
result = MonteCarloNormal()

def MonteCarloExponential():
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.exponential.html#numpy.random.Generator.exponential
    import numpy
    scale = 5
    size = 100
    my_generator = numpy.random.default_rng()
    result = my_generator.exponential(scale, size)
    print(result)
    return result
    
# MonteCarloExponential()