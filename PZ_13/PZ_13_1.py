#В двумерном списке найти суммы элементов каждой строки и поместить их в новый
#массив. Выполнить замену элементов третьей строчки исходной матрицы на
#полученные суммы.

import random

try:

   str = int(input("Введите количество строк: "))
   col = int(input("Введите количество столбцов: "))

   matr = [[random.randint(0,10) for el in range(col)] for el in range(str)] #матрица, создание столбцов и строк

   print("Исходная матрица: ")
   for s in matr:
       print(s)


   sum_str = [sum(el) for el in matr] #суммирование
   print("Сумма элементов 3 строчки:", sum_str)

   matr[2] = sum_str #3-я строка
   print("Итоговая матрица: ")
   for i in matr:
       print(i)
except IndexError:
    print("Ошибка: в матрице меньше 3 строк, невозможно заменить 3-ю строку")

