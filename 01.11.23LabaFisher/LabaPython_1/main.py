import random
import re
import statistics

import numpy as np
from scipy.stats import stats, norm
import matplotlib.pyplot as plt
import outliers.smirnov_grubbs as grubs

# Создаем массив нормального распределения
# ================================================================== #
# fout = open('Out/Out.out', 'w')
# fin = open('Inp/Inp.inp', 'r')
# x = [float(i) for i in fin.read().split(', ')]
# x = [float(i) for i in re.findall(r"[-+]?\d*\.\d+|\d+", fin.read())]
# a = [x[i] for i in range(len(x))]
# ================================================================== #
x = np.arange(-3,3, 0.001)
y = norm.pdf(x,0,1)

y[0] = random.randint(0,10)
y[-1] = random.randint(0,10)
y = np.sort(y)


print(grubs.max_test_outliers(y, alpha = 0.05)) # Выводит эдементы ненормально отклоняющиеся от нормального распределения
print(grubs.max_test_indices(y, alpha=0.05)) # Выводит индексы чисел, выделяющихся из нормального распределения

# =============================================================== #
# Ср. знач
averageValue = sum(y)/len(y)

# Дисперсия
s = np.sqrt(statistics.variance(y)) # среднее квадратичное отклонение

print(s)
# =============================================================== #
alpha = 0.05
# Поиск значений U-?

u1 = (averageValue - y[1])/s
un = (y[-1] - averageValue)/s
ua =

z = 'u1 =' + str(u1) + ' un=' + str(un)
z1 = grubs.test(x,alpha) # двусторонняя проверка
z2 = grubs.min_test(x,alpha) # проверка минимального
z3 = grubs.max_test(x,alpha) # проверка максимального
z4 = grubs.two_sided_test_indices(x,alpha) #индексы подходящие под критерий
z5 = grubs.two_sided_test_outliers(x,alpha) #значения подходящие под критерий
print(a,x,z,z1,z2,z3,z4,z5,sep='\n\n', file=fout)

