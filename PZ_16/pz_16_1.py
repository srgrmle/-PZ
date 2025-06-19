#Создайте класс «Книга», который имеет атрибуты название, автор и количество
#страниц. Добавьте методы для чтения и записи книги.

class Book:
    def __init__(self, title, author, pages):
        #сохранение данных
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Вы читаете книгу: '{self.title}' автора {self.author} ({self.pages} стр.).") #вывод о инфорции книги

    def write(self):
        print(f"Книга {self.title} была написана автором {self.author}.")

if __name__ == "__main__":
    book = Book("Анна Каренина", "Лев Толстой", 832)
    book.write()
    book.read()