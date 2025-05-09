#Дан список A размера N и целое число K (1 < K < 4, K < N ). Осуществить
#циклический сдвиг элементов списка вправо на K позиций (при этом A1 перейдет в
#AK+1, A2 — в AK+2, ..., AN — в AK). Допускается использовать вспомогательный
#список из 4 элементов.

def cyclic_shift_right(A, K): #цикл сдвиг вправо
    N = len(A)

    if not (1 < K < 4 and K < N): #проверка условия К
        raise ValueError("Значение K должно удовлетворять условиям!")

    time = A[:K]  # временный список + срез от 0 до К-1

    for i in range(N - K):
        A[i] = A[i + K] # сдвиг остальных элементов вправо на K позиций

    for i in range(K):
        A[N - K + i] = time[i] # заполнение последних K позиций элементами из врем списка

A = [1, 2, 3, 4]
K = 3
cyclic_shift_right(A, K)
print(A)