import re
# Тесты чтения файла
# Ну всё как то таким макаром и будем читать данные

f = open("INP/inp.inp")

f.readline() # считываем слово alpha
alpha = f.readline()

# --

f.readline() # считываем букву m
# Считываем длины выборок
mArray = f.readline()
mArray = mArray[:len(mArray)-1] # Избавляемся от \n
mArray = mArray.split(" ")
# Теперь будем читать сами выборки
# for i in range(len(mArray)):
#     n = mArray[i] # Считываем
#     f.readline() # Скипаем названия выборок
#     m = f.readline() # Считываем выборку
#     m = m[:len(m)-1]
#     m = m.split()
#     m = [float(m[k]) for k in range(len(m))] # Афигеть, но смог используя генератор,
# # -------------
#
# # ------------
#     fw = open("OUT/out.out",'w')
#     fw.write("str(m)slkdmadslfmlsd")

fr = [float(i) for i in re.findall(r"[-+]?\d*\.\d+|\d+", f.read())] # В этом можно не разбираться, ваще хз что это
print(fr)


# Закрываем открытые файлы...
f.close()
# fw.close()


