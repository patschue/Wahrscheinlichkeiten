# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:23:36 2021

@author: schue
"""

def Variationen_mit():
    # n = Anzahl Elemente in der Grundmenge
    n = 10
    # k = Anzahl der Ziehungen
    k = 4
    print(n ** k)
    
# Variationen_mit()

def Variationen_ohne():
    import math
    # n = Anzahl Elemente in der Grundmenge
    n = 5
    # k = Anzahl der Ziehungen
    k = 3
    result = (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * math.factorial(k)
    print(result)
    
# Variationen_ohne()

def Kombinationen_mit():
    import math
    # n = Anzahl Elemente in der Grundmenge
    n = 6
    # k = Anzahl der Ziehungen
    k = 4
    temp = n + k - 1
    result = math.factorial(temp) / (math.factorial(k) * math.factorial(temp - k))
    print(result)
    
Kombinationen_mit()

def Kombinationen_ohne():
    import math
    # n = Anzahl Elemente in der Grundmenge
    n = 5
    # k = Anzahl der Ziehungen
    k = 4
    result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    print(result)
          
# Kombinationen_ohne()

def Permutation_ohne():
    import math
    # n = Anzahl Elemente in der Grundmenge
    n = 4
    result = math.factorial(n)
    print(result)

# Permutation_ohne()
