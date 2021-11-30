# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 14:57:43 2021

@author: Patrick Schürmann
"""
# from scipy.stats import binom
# import scipy.stats

def Binominalverteilung():
    print("Binominalverteilung")
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
    from scipy.stats import binom
    # n entspricht Anzahl Versuche
    n = 3
    # p entspricht Erfolgswahrscheinlichkeit
    p = 1/6
    mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
    std = binom.std(n, p, loc=0)
    print("Mittelwert:", mean, "Varianz:", var, "Standardabw.:", round(std, 2), "Skewness:", skew, "Kurtosis:", kurt)
    # k entspricht Anzahl Treffer
    k = 1
    print("Wahrscheinlichkeit für k: PMF:", binom.pmf(k, n, p, loc=0))
    print("Wahrscheinlichkeit bis und mit k: CDF:", binom.cdf(k, n, p, loc=0))
    
# Binominalverteilung()

def Poissonverteilung():
    print("Poissonverteilung")
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html#scipy.stats.poisson
    from scipy.stats import poisson
    # Mu entspricht erwartete Anzahl Eintreten
    mu = 1/4  
    mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
    std = poisson.std(mu, loc=0)
    print("Mittelwert:", mean, "Varianz:", var, "Standardabw.:", round(std, 2), "Skewness:", skew, "Kurtosis:", kurt)
    # k entspricht Anzahl Treffer
    k = 0
    print("Wahrscheinlichkeit für k: PMF:", poisson.pmf(k, mu, loc=0))
    print("Wahrscheinlichkeit bis und mit k: CDF:", poisson.cdf(k, mu, loc=0))   

# Poissonverteilung()

def Exponentialverteilung():
    print("Exponentialverteilung")
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html#scipy.stats.expon
    from scipy.stats import expon
    # lamba entspricht der durchschnittlichen Wartezeit
    lamba = 10
    mean, var, skew, kurt = expon.stats(loc=0, scale=lamba, moments='mvsk')
    std = expon.std(loc=0, scale=lamba)
    print("Mittelwert:", mean, "Varianz:", var, "Standardabw.:", round(std, 2), "Skewness:", skew, "Kurtosis:", kurt)
    # x entspricht Beobachtungszeitraum
    x = 20
    print("Wahrscheinlichkeit bis und mit k: CDF:", expon.cdf(x, loc=0, scale=lamba))   

# Exponentialverteilung()

def Normalverteilung():
    print("Normalverteilung")
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm
    from scipy.stats import norm
    # m entspricht dem Mittelwert
    m = 96
    # v entspricht der Standardabweichung
    # Alternativ (n * p * (1-p)) ** 0.5
    v = 8
    mean, var, skew, kurt = norm.stats(loc=m, scale=v, moments='mvsk')
    std = norm.std(loc=m, scale=v)
    print("Mittelwert:", mean, "Varianz:", var, "Standardabw.:", round(std, 2), "Skewness:", skew, "Kurtosis:", kurt)
    # x entspricht der gewünschten Zahl
    x = 104
    # q entspricht definierter Wahrscheinlichkeit (1 = 100%)
    q = 0.95
    print("Wahrscheinlichkeit für k: PDF:", norm.pdf(x, loc=m, scale=v))
    print("Wahrscheinlichkeit bis und mit k: CDF:", norm.cdf(x, loc=m, scale=v))     
    print("Wert bei definierter Wahrscheinlichkeit:", norm.ppf(q, loc=m, scale=v))     
    
Normalverteilung() 
    
    