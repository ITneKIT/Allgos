import numpy as np
import scipy.stats as stats

s1 = 0.3
mo = 5
rng = np.random.default_rng()

x1 = (rng.standard_normal(50))*s1 + mo # Выборка данных
x1 = sorted(x1)

s2 = 0.4
x2 = (rng.standard_normal(50))*s2 + mo # Выборка данных
x2 = sorted(x2)


# Критерий Уилкоксона
def Uilkonson(sample1, sample2):
    print(stats.wilcoxon(sample1, sample2))
Uilkonson(x1, x2)

# Критерий знкаов для медианы
# def SignOfMedian(sample1,sample2):
#     print(stats.binomtest(sample1, sample2))
# SignOfMedian(x1, x2)

# Критерий Двух выборочный критерий Уилкоксона
def DoubleSampleUilkokson(samole):
    print(stats.)

# Критерий Краскела - Уоллиса
def KrskolUolis(sample):
    print()