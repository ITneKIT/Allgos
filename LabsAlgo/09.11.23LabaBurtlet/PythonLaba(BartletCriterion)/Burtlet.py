# Напишем критерий Бартлета и однофакторный дисперсионный анализ
import numpy as np
import scipy.stats as stat

n=10 # Количество элементов в первой выборке
m=12 # Количество элементов во второй выборке
# Создание выборок
# ============================================================================== #
mo = 5.3 # мат ожидание
s1 = 0.12 # Дисперсия
n1 = 10
rng = np.random.default_rng()
z1 = (rng.standard_normal(n1))*s1 + mo # Выборка данных
z1 = np.sort(z1) # Первая выборка данных

n2 = 12
s2 = 0.1 # Не ну вы представте это тоже дисперсия
z2 = (rng.standard_normal(n2))*s2 + mo
z2 = np.sort(z2) # Вторая выборка данных

n3 = 19
s3 = 0.05
z3 = (rng.standard_normal(n3))*s3 + mo
z3 = np.sort(z3)
# ============================================================================== #
# Попробуем сделать чтене из файла
file = open("INP/inp.inp",'r')
file.readline() # читается alpha
alpha = file.readline("\n")
file.readline() # читается m
m = list(file.readline())
arraySamples = list() # создаем лист для выборок


for i in range(len(m)):
    arraySamples[i] = file.readline()


resultBurtlet = stat.bartlett(*arraySamples)
resultOneWay = stat.f_oneway(z1,z2) # Однофакторный

print(resultBurtlet)
print(resultOneWay)

# stat.chisquare()
