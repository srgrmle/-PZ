#Даны положительные числа A и B (A > Б). На отрезке длины A размещено
#максимально возможное количество отрезков длины B (без наложений). Не
#используя операции умножения и деления, найти количество отрезков Б,
#размещенных на отрезке A.

a = int(input('Введите число первое: '))
b = int(input('Введите число второе: '))
k = int(input('Введите число третье: '))
try: #обработка исключений
    while a > b : #выполнение цикла
        a = a - b
        k = k + 1
    print(k)
except:
    print("Неверный формат")