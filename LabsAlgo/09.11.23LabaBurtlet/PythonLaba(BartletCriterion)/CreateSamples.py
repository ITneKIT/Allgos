import numpy as np
import random
import re

# ===========================
# Тут будут все функции печати в файл
def WriteInFile(x):
    for i in x:
        file.write(str(i)+" ")

# def



# ================================================
# Работа с файлом
file = open("INP/inp.inp",'w')
# Сразу запишем значение с которым будет вестись сравнение результатов
file.write("alpha")
print("Введите параметр alpha:")
file.write(input()) # Записываем в файл некоторое введённое значение


file.write("m")
print("Введите длины желаемых выборок в пределе от 10 до 20 значений, используя пробел")
strNCounts = input()
nLens = strNCounts.split(" ")
nLens = [int(k) for k in nLens if int(k) >= 10 and int(k) <= 20] # Пересобираем массив с длинами выборок



mo = 5.3 # мат ожидание
for i in range (len(nLens)):
    s1 = random.uniform(0.05,0.1) # Дисперсия
    rng = np.random.default_rng()
    n1 = nLens[i] # Берем значение, соответствующее номеру выборки
    z1 = (rng.standard_normal(n1))*s1 + mo # Выборка данных
    z1 = np.sort(z1) # Первая выборка данных
    WriteInFile(z1)
    file.write("\n")
    print(n1)

# s2 = 0.1 # Не ну вы представте это тоже дисперсия
# z2 = (rng.standard_normal(n2))*s2 + mo
# z2 = np.sort(z2) # Вторая выборка данных
# WriteInFile(z2)
# file.write("\n")

# s3 = 0.05
# z3 = (rng.standard_normal(n3))*s3 + mo
# z3 = np.sort(z3)
# WriteInFile(z3)
# file.write("\n")

file.close()