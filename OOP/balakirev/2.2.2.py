class WindowDlg:

    def __init__(self, title, width, heigth):
        self.__title = title
        self.__width = width
        self.__heigth = heigth

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__heigth}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if 0 <= width <= 10_000:
            self.__width = width
            self.show()

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, heigth):
        if 0 <= heigth <= 10_000:
            self.__heigth = heigth
            self.show()
