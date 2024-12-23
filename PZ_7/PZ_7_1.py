#Дана строка. Преобразовать в ней все прописные латинские буквы в строчные

def stroka_lower(name): #преобразуем в строчные буквы
    try:
        name = str(name) #преобразуем в строку
        if not name.islower(): #проверка и возврат True
            result = name.lower() #преобразуем все заглавные буквы в строчные

            return result #возвращаем значение из функции
        else:
            raise ValueError("Строка должна содержать хотя бы одну заглавную букву.")

    except Exception as e:
        print(f"Ошибка! {e}")


user = input("Введите строку для преобразования: ")
converted_string = stroka_lower(user)

if converted_string:
     print(f"Преобразованная строка: {converted_string}")