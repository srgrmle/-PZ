#Даны три целых числа, одно из которых отлично от двух других, равных между собой. Определить порядковый номер числа, отличного от остальных.

try:# обработчик исключений
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    if (a == b and a != c and b != c) or (a != b and a == c and b != c) or (a != b and a != c and b == c): #при проверке условия выполняется одна из веток
        if a == b:
            print("Отличное число: 3")
        elif a == c:
            print("Отличное число: 2")
        elif b == c:
            print("Отличное число: 1")
    else:
        print("Все числа различны!")
except:
    print("Ошибка.Введите число!")