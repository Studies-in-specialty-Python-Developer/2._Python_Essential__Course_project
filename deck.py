from const import SUITS, RANKS, PRINTED
from itertools import product
from random import shuffle


class Card:

    def __init__(self, suit, rank, picture, points):
        self.suit = suit
        self.rank = rank
        self.points = points
        self.picture = picture

    def __str__(self):
        return self.picture + '  Points: ' + str(self.points)


class Deck:
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    @staticmethod
    def _generate_deck():
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank.isdigit():
                points = int(rank)
            elif rank == 'ace':
                points = 11
            else:
                points = 10
            if rank.isdigit():
                picture = rank
            else:
                picture = rank.capitalize()[0]
            picture = f'{picture}{PRINTED.get(suit)}'
            card = Card(suit, rank, picture, points)
            cards.append(card)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
