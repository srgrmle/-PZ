# В последовательности на n целых чисел умножить все элементы на первый элемент
import random

n = int(input('Введите количество чисел: '))
listt = ([random.randint(0,50) for el in range(n)]) #список случайных чисел от 0 до 50

first = listt[0] #сохранение первого элемента
new = [i * first for i in listt] #новый список

print('Начальный список:', listt)
print('Новый список:', new)
