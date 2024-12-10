#Найти сумму чисел ряда 1,2,3,4 от числа n до числа m. Суммирование оформить функцией с параметрами.
#Значения n и m программа должна запрашивать.

def summa(a, b):  #функция, принимающая значения
    i = 1
    summa = a
    while i + a <= b: #пока условие выполняется,цикл работает
        summa = summa + (a + i)
        i += 1
    return summa #возвращает сумму

try:  #обработчик исключений
    n = int(input('Введите первое число: '))
    m = int(input('Введите второе число: '))

    if n > m: #выводит сообщение об ошибке
        print('Произошла ошибка, проверьте подходит ли число под условие')
    else: #если все правильно, то сумма числового ряда
        print('Сумма числового ряда: ', summa(n, m))

except:
    print('Проверьте еще раз, пожалуйста)')