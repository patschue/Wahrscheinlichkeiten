# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:17:10 2021

@author: schue
"""

def MonteCarloNormal():
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal
    import numpy
    mean = 1000
    std = 150
    size = 100000
    my_generator = numpy.random.default_rng()
    result = my_generator.normal(mean, std, size)
    print(result)
    return result
    
# result = MonteCarloNormal()

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

import pandas as pd
import numpy as np

my_generator = np.random.default_rng()
Kosten = my_generator.normal(650000, 50000, 1000000)
Anzahl = np.random.binomial(30, 0.6, 1000000)
Verkaufspreis = my_generator.normal(600000, 30000, 1000000)
Prodpreis = my_generator.normal(450000, 40000, 1000000)
Result = pd.DataFrame(pd.np.column_stack([Kosten, Anzahl, Verkaufspreis, Prodpreis]))
Result["Kosten"] = Result[1] * Result[3]
Result["Erlös"] = Result[3] * Result[2]
Result["Gewinn"] = Result["Erlös"] - Result["Kosten"]
Result["Reingewinn"] = Result["Gewinn"] - Result[0]

dfverlust = Result[Result['Reingewinn'] < 0]
print(len(dfverlust))