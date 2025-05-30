# В двумерном списке найти сумму элементов второй половины матрицы.

import random
str = int(input("Введите количество строк: "))
col = int(input("Введите количество столбцов: "))

matr = [[random.randint(0,10) for el in range(col)] for el in range(str)] #матрица, создание столбцов и строк
print("Исходная матрица: ")
for s in matr:
    print(s)

polovina = len(matr) // 2
srez = matr[polovina:] #разделяем на две половины
print(srez)

sum = sum(sum(el) for el in srez) #суммирование
print("сумма элементов второй половины матрицы: ", sum)