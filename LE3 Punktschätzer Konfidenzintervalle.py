# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 12:30:30 2021

@author: Patrick Schürmann
"""

def Punktschätzer_Mittelwert():
    print("Punktschätzer Mittelwert")
    # https://spaces.technik.fhnw.ch/multimediathek/file/parameterschatzung-skript
    import numpy as np
    data = [1.9, 3.4, 4.9, 4.4, 5.5]
    print(round(np.mean(data), 3))
    
# Punktschätzer_Mittelwert()

def Punktschätzer_Standardabweichung():
    print("Punktschätzer Standardabweichung")
    # https://spaces.technik.fhnw.ch/multimediathek/file/parameterschatzung-skript
    import numpy as np
    data = [1.9, 3.4, 4.9, 4.4, 5.5]
    print("Varianz:", round(np.var(data, ddof=1), 3))
    print("Standardabweichung:", round(np.std(data, ddof=1), 3))
    
# Punktschätzer_Standardabweichung()

def Punktschätzer_relHäufigkeit():
    print("Punktschätzer relative Häufigkeit")
    # https://welt-der-bwl.de/Punktschätzung
    import numpy as np
    data = [10, 20, 18, 15, 17]
    print(round(np.mean(data), 3))

# Punktschätzer_relHäufigkeit()

def Mittelwert_Intervall_kleine_Stichprobe():
    # t-Verteilt
    import numpy as np
    from scipy.stats import t
    data = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]
    # ki = Konfidenzintervall
    ki = 0.95
    # n = Umfang Stichprobe oder len(data)
    n = 12
    # m = Mittelwert oder np.mean(data)
    m = 6.1
    print(t.interval(alpha = ki, df = n - 1, loc = m, scale=0.8))
    
# Mittelwert_Intervall_kleine_Stichprobe()

# def Mittelwert_Intervall_grosse_Stichprobe():
#     import numpy as np
#     from scipy.stats import norm
#     data = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]
#     # ki = Konfidenzintervall
#     ki = 0.95
#     # m = Mittelwert oder np.mean(data)
#     m = 0.6
#     print(norm.interval(alpha = ki, loc = m, scale=0.8))
    
# Mittelwert_Intervall_grosse_Stichprobe()
     
def Mittelwert_Intervall_grosse_Stichprobe():
    import scipy.stats as st
    # p = Wahrscheinlichkeit
    p = 86/123
    # n = Anzahl
    n = 123
    # ki = Konfidenzintervall
    ki = 0.975
    zscore = st.norm.ppf(ki)
    print(zscore)
    intervall = zscore * (((p * (1-p))/n) ** 0.5)
    print(p - intervall, p + intervall)
    
Mittelwert_Intervall_grosse_Stichprobe()