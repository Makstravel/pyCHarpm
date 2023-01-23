class Zebra:
    def __init__(self, white="Полоска белая", black="Полоска черная"):
        self.white = white
        self.black = black

    def which_stripe(self):
        print(self.white)
        self.white, self.black = self.black, self.white

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe()

