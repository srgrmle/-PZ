#Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».

try:
    punctuation = '!",-.:;—?…_`'
    with open('text18-16.txt', 'r', encoding='utf-16') as file:
        text = file.read()
        print('cодержимое файла:')
        print(text)

        upp_count = 0
        for char in text:
            if char.isupper():
                upp_count += 1
        print('кол-во букв в верхнем регистре:', upp_count)

        fix_text = []
        for char in text:
            if char in punctuation:
                fix_text.append('!')
            else:
                fix_text.append(char)
        new_text = ''.join(fix_text)

        with open('new.txt', 'w', encoding='utf-8') as new_file:
            new_file.write(new_text)
            print('файл создан ')
except FileNotFoundError:
    print('файл не найден')