class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        if isinstance(other, ChessPlayer):
            return self.rating == other
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        if isinstance(other, ChessPlayer):
            return self.rating > other
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        if isinstance(other, ChessPlayer):
            return self.rating < other
        else:
            return'Невозможно выполнить сравнение'


magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
assert magnus.name == 'Carlsen'
assert magnus.surname == 'Magnus'
assert magnus.rating == 2847
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
assert not magnus == 4000
assert ian == 2789
assert not magnus == ian
assert magnus > ian
assert not magnus < ian
assert (magnus < [1, 2]) == 'Невозможно выполнить сравнение'

v1 = ChessPlayer('Гарри ', 'Каспаров', 10)
v2 = ChessPlayer('Бобби', 'Фишер', 20)
v3 = ChessPlayer('Bot', 'Bot', 20)

assert isinstance(v1, ChessPlayer)
assert isinstance(v2, ChessPlayer)
assert v2.__dict__ == {'name': 'Бобби', 'surname': 'Фишер', 'rating': 20}
assert v1.__dict__ == {'name': 'Гарри ', 'surname': 'Каспаров', 'rating': 10}
assert v1 > 5
assert not v1 > 10
assert not v1 > 11
assert not v1 < 5
assert not v1 < 10
assert v1 < 11
assert not v1 == 5
assert v1 == 10
assert not v1 == 11
assert not v1 > v2
assert not v1 == v2
assert v3 == v2
assert not v3 != v2
assert v1 < v2
assert (v1 > 'fdsfd') == 'Невозможно выполнить сравнение'
assert (v1 < 'fdsfd') == 'Невозможно выполнить сравнение'
assert (v1 == 'fdsfd') == 'Невозможно выполнить сравнение'
assert (v1 == [1, 2]) == 'Невозможно выполнить сравнение'
assert (v1 < [1, 2]) == 'Невозможно выполнить сравнение'
print('Good')