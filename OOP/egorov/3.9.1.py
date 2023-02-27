class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return iter(self._cards)


deck = Deck()
for card in deck.cards:
    print(card.rank, card.suit)