#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Положительные числа:
#Количество положительных чисел:
#Отрицательные числа:
#Количество отрицательных чисел:


# создание последовательности из целых положительных и отрицательных чисел
nums = ['32 74 -95 7 4 -2 6 13 29']
f1 = open('data_1.txt', 'w')
f1.writelines(nums)
f1.close()

# Исходные данные:
f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(nums)
f2.close()

# Количество элементов:
f1 = open('data_1.txt')
m = f1.read()
m = m.split()
for i in range(len(m)):
    m[i] = int(m[i])
f1.close()

f2 = open('data_2.txt', 'a')
f2.write('\n')
print('Количество элементов: ', len(m), file=f2)
f2.close()

# Положительные числа:
positive = [num for num in m if num > 0]  # список в одну строку, больше нуля
f2 = open('data_2.txt', 'a')
f2.write('\n')
f2.write('Положительные числа: ')
f2.write('\n')
f2.write(' '.join(map(str, positive)))
f2.close()

# Количество положительных чисел:
f2 = open('data_2.txt', 'a')
f2.write('\n')
print('Количество положительных чисел: ', len(positive), file=f2)
f2.close()

# Отрицательные числа:
negative = [num for num in m if num < 0]  # список в одну строку,меньше нуля
f2 = open('data_2.txt', 'a')
f2.write('\n')
f2.write('Отрицательные числа: ')
f2.write('\n')
f2.write(' '.join(map(str, negative)))
f2.close()

# Количество отрицательных чисел:
f2 = open('data_2.txt', 'a')
f2.write('\n')
print('Количество отрицательных чисел: ', len(negative), file=f2)
f2.close()
