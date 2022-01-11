# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:23:36 2021

@author: schue
"""

def Variationen_mit():
    # Geordnete Stichprobe
    # n = Anzahl Elemente in der Grundmenge
    n = 5
    # k = Anzahl der Ziehungen
    k = 5
    print(n ** k)
    
# Variationen_mit()

def Variationen_ohne():
    # Geordnete Stichprobe
    import math
    # n = Anzahl Elemente in der Grundmenge
    n = 4
    # k = Anzahl der Ziehungen
    k = 4
    result = (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * math.factorial(k)
    print(result)
    
# Variationen_ohne()

def Kombinationen_mit():
    # Ungeordnete Stichprobe
    import math
    # n = Anzahl Elemente in der Grundmenge
    n = 5
    # k = Anzahl der Ziehungen
    k = 3
    temp = n + k - 1
    result = math.factorial(temp) / (math.factorial(k) * math.factorial(temp - k))
    print(result)
    
# Kombinationen_mit()

def Kombinationen_ohne():
    # Ungeordnete Stichprobe
    import math
    # n = Anzahl Elemente in der Grundmenge
    n = 20
    # k = Anzahl der Ziehungen
    k = 5
    result = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    print(result)
          
Kombinationen_ohne()

def Permutation_ohne():
    import math
    # n = Anzahl Elemente in der Grundmenge
    n = 5
    result = math.factorial(n)
    print(result)

# Permutation_ohne()
