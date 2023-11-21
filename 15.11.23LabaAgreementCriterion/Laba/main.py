import numpy as np
import scipy.stats as stat

s1 = 0.3
mo = 5
rng = np.random.default_rng()
x = (rng.standard_normal(50))*s1 + mo # Выборка данных
# x = np.random.poisson(5,100)
x = sorted(x)
alpha = 0.05

# Shapiro
def Shapiro(sample):
    print(stat.shapiro(sample))
Shapiro(x)

#Smirnov
def Smirnov(sample):
    res = ""
    statictic,p_value = stat.kstest(sample, 'norm')
    if p_value >= 0.05:
        res = "Соответствует нормальному распределению"
    else:
        res = "Не соответствует нормальному распределению"
    print("Smirnov-test:",res,"[][][]","statictic:",statictic,"; p_value:", p_value)
Smirnov(x)

def Anderson(sample):
    print(stat.anderson(sample))
Anderson(x)

def xSquare(sample):
    print(stat.chisquare(sample))
xSquare(x)
