""" Модуль содержит классы, которые описывают свойства и методы объектов Карта и Колода для игры в BlackJack """

from itertools import product
from random import shuffle
from const import SUITS, RANKS, PRINTED


class Card:
    """ Класс реализует функциональность игральной карты
    Attributes:
        suit (str): масть
        rank (str): ранг (значение)
        picture (str): символьное обозначение для вывода в консоль
        points (int): количество очков
    Methods:
        __init__(self, suit: str, rank: str, picture: str, points: int):
            инициализирует атрибуты заданными значениями
    """

    def __init__(self, suit: str, rank: str, picture: str, points: int):
        self.suit = suit
        self.rank = rank
        self.picture = picture
        self.points = points

    def __str__(self):
        return f'{self.picture} ({self.points})'


class Deck:
    """ Класс реализует функциональность игральной карты
    Attributes:
        cards (list): список карт, которые есть в колоде в данный момент
    Methods:
        __init__(self):
            генерирует новую колоду из 52 карт и перемешивает её случайным образом
        _generate_deck() -> list:
            генерирует новую колоду из 52 карт
        get_card(self) -> Card:
            возвращает случайную карту и удаляет её из колоды
        __len__(self):
            возвращает количество карт, оставшихся в колоде
    """

    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    @staticmethod
    def _generate_deck() -> list:
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
            card = Card(suit=suit, rank=rank, points=points, picture=picture)
            cards.append(card)
        return cards

    def get_card(self) -> Card:
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
