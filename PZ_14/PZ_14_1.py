# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество полученных элементов.
import re

with open('price.txt', 'r', encoding='utf-8') as file:
    text = file.read()  # Чтение содержимого файла

regular = re.compile(r'\d+\s*руб.\s*\d+\s*коп.') #ищем суммы
prices = regular.findall(text)

print('цены:')
for price in prices:
    print(price)
print('количество найденных цен:', len(prices))