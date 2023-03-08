class Book:

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == 'title' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'author' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'pages' and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'year' and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            super.__setattr__(self, key, value)


book = Book('Python ООП', 'Сергей Балакbриев', 123, 2022)
