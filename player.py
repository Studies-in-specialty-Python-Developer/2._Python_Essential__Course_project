""" Модуль содержит классы, которые описывают свойства и методы абстрактного игрока в BlackJack, а также
его потомков, реализующих игровой функционал Игрока, Дилера и других игроков (ботов) """

import abc
import random
from const import MESSAGES
from deck import Card


class AbstractPlayer(abc.ABC):
    """ Абстрактный класс реализует базовую функциональность каждого игрока в BlackJack.
    Класс служит предком для игроков Дилер (Dealer), Игрок (Player), игрок-бот (Bot)
    Attributes:
        cards (list): список карт
        bet (int): текущая ставка
        full_points (int): количество очков
        max_points (int): количество очков у игрока, при наборе которых он перестает брать дополнительные карты
        money (int): деньги игрока
        name (str): имя
    Methods:
        __init__(self):
            инициализирует атрибуты значениями по умолчанию
        change_points(self):
            рассчитывает количество набранных игроком очков
        take_card(self, card: Card):
            получает из колоды новую карту, добавляет её в список карт на руке игрока и рассчитывает
            количество набранных игроком очков
        change_bet(self, max_bet, min_bet):
            абстрактный метод, реализующий ставку игрока
        ask_card(self):
            метод, реализующий запрос игроком дополнительных карт
        print_cards(self):
            печатает в консоль карты на руке игрока и количество набранных очков
        print_money(self):
            печатает в консоль сумму денег, которой располагает игрок
    """

    def __init__(self):
        """ Инициализирует атрибуты значениями по умолчанию """
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.max_points = 0
        self.money = 100
        self.name = ''

    def change_points(self):
        """ Рассчитывает количество набранных игроком очков """
        self.full_points = sum(card.points for card in self.cards)

    def take_card(self, card: Card):
        """ Получает из колоды новую карту, добавляет её в список карт на руке игрока и рассчитывает
        количество набранных игроком очков
        Arguments:
            card (Card): новая карта """
        self.cards.append(card)
        self.change_points()

    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        """ Абстрактный метод, реализующий ставку игрока """

    def ask_card(self) -> bool:
        """ Реализует процесс выбора дилера - брать или нет еще одну дополнительную карту
        Returns:
            bool - выбор дилера """
        return self.full_points < self.max_points

    def print_cards(self):
        """ Показывает в консоли карты на руке игрока и количество набранных очков """
        print(f'{self.name} cards:'.ljust(len('Player cards:')), end='  ')
        for card in self.cards:
            print(f'{card}, ', end='')
        print('full points: ', self.full_points)

    def print_money(self):
        """ Показывает в консоли сумму денег, которой располагает игрок """
        print(f'{self.name} money: '.ljust(len('Player money: ')), self.money)


class Player(AbstractPlayer):
    """ Класс реализует базовую функциональность игрока-человека в BlackJack
    Attributes:
        name (str): имя
    Methods:
        __init__(self):
            назначает имя игроку
        change_bet(self, max_bet, min_bet):
            реализует процесс выбора ставки игроком
        ask_card(self):
            спрашивает у игрока, дать ли ему дополнительную карту """

    def __init__(self):
        """ Присваивает имя Player игроку """
        super().__init__()
        self.name = 'Player'

    def change_bet(self, max_bet, min_bet):
        """ Реализует процесс выбора ставки игроком
        Arguments:
            max_bet (int): максимальная ставка
            min_bet (int): минимальная ставка """
        while True:
            value = int(input('Make your bet: '))
            if max_bet > value > min_bet:
                self.bet = value
                self.money -= self.bet
                break
        print('Your bet is: ', self.bet)

    def ask_card(self) -> bool:
        """ Спрашивает у игрока, дать ли ему дополнительную карту
        Returns:
            bool - выбор игрока """
        choice = input(MESSAGES.get('ask_card'))
        return choice == 'y'


class Dealer(AbstractPlayer):
    """ Класс реализует базовую функциональность бота-дилера в BlackJack
    Attributes:
        name (str): имя
        max_points (int):  количество очков, при наборе которых дилер перестаёт брать дополнительные карты
    Methods:
        __init__(self):
            назначает имя игроку и количество очков, при наборе которых дилер перестаёт брать дополнительные карты
        change_bet(self, max_bet, min_bet):
            показывает, что по правилам игры дилер не делает ставки
        print_money(self):
            показывает, что по правилам игры у дилера нет денег """

    def __init__(self):
        """ Присваивает имя Dealer дилеру и максимальное количество очков, после набора которых
        дилер перестаёт брать дополнительные карты """
        super().__init__()
        self.name = 'Dealer'
        self.max_points = 17

    def change_bet(self, max_bet, min_bet):
        """ Показывает, что по правилам игры дилер не делает ставки
        Arguments:
            max_bet (int): максимальная ставка
            min_bet (int): минимальная ставка """
        print('This type is dealer so it has no bets')

    def print_money(self):
        """ Показывает, что по правилам игры у дилера нет денег """
        print('This type is dealer so it has no money')


class Bot(AbstractPlayer):
    """ Класс реализует базовую функциональность бота-игрока в BlackJack
    Attributes:
        name (str): автоматически назначаемое имя
        max_points (int):  количество очков, при наборе которых бот перестаёт брать дополнительные карты
    Methods:
        __init__(self):
            назначает имя боту и количество очков, при наборе которых бот перестаёт брать дополнительные карты
        change_bet(self, max_bet, min_bet):
            реализует процесс выбора ставки ботом """

    def __init__(self, name):
        """ Присваивает имя Bot с порядковым номером и максимальное количество очков, после набора которых
        бот перестаёт брать дополнительные карты """
        super().__init__()
        self.name = name
        self.max_points = random.randint(17, 20)

    def change_bet(self, max_bet, min_bet):
        """ Реализует процесс выбора ставки ботом
        Arguments:
            max_bet (int): максимальная ставка
            min_bet (int): минимальная ставка """
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(f'{self.name} give: {self.bet}')
