import smirnov_grubbs as grubbs
import numpy as np
import re

fout = open('Out/Out.out', 'w')
fin = open('Inp/Inp.inp', 'r')
#x = [float(i) for i in fin.read().split(', ')]
x = [float(i) for i in re.findall(r"[-+]?\d*\.\d+|\d+", fin.read())] 
a = [x[i] for i in range(len(x))]

x[0] = 20
x[-1] = -40
alpha = 0.05
avg = np.mean(x)
x.sort()

s = 0
for i in range(len(x)):
    s += (x[i] - avg) ** 2
    
s = (s/(len(x) - 1))**0.5

uarr = [(avg - x[i])/s for i in range(len(x))]

un = uarr[-1]
u1 = uarr[0]

z = 'u1 =' + str(u1) + ' un=' + str(un)
z1 = grubbs.test(x,alpha) # двусторонняя проверка
z2 = grubbs.min_test(x,alpha) # проверка минимального
z3 = grubbs.max_test(x,alpha) # проверка максимального
z4 = grubbs.two_sided_test_indices(x,alpha) #индексы подходящие под критерий
z5 = grubbs.two_sided_test_outliers(x,alpha) #значения подходящие под критерий

print(a,x,z,z1,z2,z3,z4,z5,sep='\n\n', file=fout)
