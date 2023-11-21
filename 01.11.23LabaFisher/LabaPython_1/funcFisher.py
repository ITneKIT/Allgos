# import random
# import re
# import statistics

import numpy as np
import scipy
#from scipy.stats import stats
# import matplotlib.pyplot as plt
# import outliers.smirnov_grubbs as grubs

# ============================================================================== #
mo = 5.3 # мат ожидание
s1 = 0.12 # Дисперсия
n1 = 20
rng = np.random.default_rng()
z1 = (rng.standard_normal(n1))*s1 + mo # Выборка данных
z1 = np.sort(z1)

n2 = 17
s2 = 0.1 # Не ну вы представте это тоже дисперсия
z2 = (rng.standard_normal(n2))*s2 + mo
z2 = np.sort(z2)
# ============================================================================== #

# define Fisher's variable

disp1 = np.var(z1, ddof=1)
disp2 = np.var(z2, ddof=1)

if disp1 > disp2:
    F = disp1/disp2
    f1 = n1
    f2 = n2
else:
    F = disp2/disp1
    f1 = n2
    f2 = n1

file = open("OUT/out.out",'w')
file.write("Result of carried out:\n")
file.write("dispire F: ")
Fa = scipy.stats.f.ppf(q=1-.05, dfn = f1, dfd = f2)
file.write("Critical value F -> Fa = $Fa")

file.close()

# F = (max(disp1,disp2) ** 2) / (min(disp1, disp2) ** 2)
# Fa = scipy.stats.f.ppf(q=1-.05, dfn = n0, dfd = n0)
# print(Fa)
#d = scipy.stats.ttest_ind(z1,z2)
# print(F)



if F <= Fa:
    print("Критерий Фишера выполняется")
else:
    print("Критерий Фишера не выполняется")