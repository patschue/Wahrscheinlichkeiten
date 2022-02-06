# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:29:42 2021

@author: schue
Voraussetzung Scipy Version grösser 1.70
"""

def BinomialHypotestOneSample():
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html#scipy.stats.binomtest
    from scipy.stats import binomtest
    # k = The number of successes
    k = 4
    # x = The number of trials
    x = 15
    # y = The hypothesized probability of success
    y = 0.1
    # ‘two-sided’ (default), ‘greater’, ‘less’
    result = binomtest(k, n=x, p=y, alternative='two-sided')
    print(result)
    # print(result)
    
# BinomialHypotestOneSample()

def zTestOneSample():
    # Wird angewendet bei Stichprobengrösse kleine ist < 30.
    # https://www.statology.org/z-test-python/
    from statsmodels.stats.weightstats import ztest as ztest
    Vergleichswert = 27
    data = [33, 31, 30, 29, 24, 27, 28, 31, 25, 23]
    result = ztest(data, value=Vergleichswert)
    print(result)
    print("Der zweite Wert ist der pvalue.")
    
# zTestOneSample()

def tTestOneSample():
    # Wird angewendet bei Stichprobengrösse kleine ist < 30.
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html
    from scipy import stats
    data = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 109, 110, 112, 112, 113, 114, 115]
    Vergleichswert = 100
    result = stats.ttest_1samp(data, Vergleichswert)
    print(result)
    
# tTestOneSample()

def tTestTwoSamples():
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
    from scipy import stats
    data1 = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 109, 100, 112, 100, 100, 105, 50]
    data2 = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 120, 110, 120, 112, 113, 130, 150]
    # alternative = ‘two-sided’, ‘less’, ‘greater’
    result = stats.ttest_ind(data1, data2)
    print(result)
    
# tTestTwoSamples()

def MannWhitneyUTest():
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    from scipy.stats import mannwhitneyu
    data1 = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 109, 100, 112, 100, 100, 105, 50]
    data2 = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99, 105, 109, 109, 120, 110, 120, 112, 113, 130, 150]
    U1, p = mannwhitneyu(data1, data2, method="exact")
    print(U1, p)
    
# MannWhitneyUTest()


def KolmogorovSmirnovTest():
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html
    # Überprüft Übereinstimmung zweier Wahrscheinlichkeitsverteilungen
    from scipy import stats
    import numpy as np
    rng = np.random.default_rng()
    x = stats.norm.rvs(loc=0.2, size=100, random_state=rng)
    result = stats.kstest(x, 'norm', alternative='less')
    print(result)
    
# KolmogorovSmirnovTest()


def NormalzuSollwert():
    from scipy import stats
    # m0 entspricht dem ursprünglichen Mittelwert
    m0 = 800
    # m1 entspricht dem neuen Mittelwert
    m1 = 840
    # v entspricht der neuen Standardabweichung
    v = 400
    # n entspricht der grösse der Stichprobe
    n = 26
    # tpg entspricht Prüfgrösse t
    tpg = (m1-m0)/(v/(n**0.5))
    print("Prüfgrösse t:", tpg)
    # a entspricht Irrtumswahrscheinlichkeit
    a = 0.01
    tonesided = stats.t.ppf(q=a,df= n-1)
    print("Kritische Grenze einseitig:", round(tonesided, 4))
    ttwosided = stats.t.ppf(q=a/2,df= n-1)
    print("Kritische Grenze einseitig:", round(ttwosided, 4))
    
    
NormalzuSollwert()
    
    
    