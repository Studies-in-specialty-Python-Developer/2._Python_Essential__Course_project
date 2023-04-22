""" Модуль содержит классы, которые описывают свойства и методы абстрактного игрока в BlackJack, а также
его потомков, реализующих игровой функционал Игрока, Дилера и других игроков (ботов) """

import abc
import random
from const import MESSAGES


class AbstractPlayer(abc.ABC):

    def __init__(self):
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.money = 100
        self.name = ''

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])

    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    @abc.abstractmethod
    def ask_card(self):
        pass

    def print_cards(self):
        print(f'{self.name} cards:'.ljust(len('Player cards:')), end='  ')
        for card in self.cards:
            print(f'{card}, ', end='')
        print('full points: ', self.full_points)

    def print_money(self):
        print(f'{self.name} money: '.ljust(len('Player money: ')), self.money)


class Player(AbstractPlayer):

    def __init__(self):
        super().__init__()
        self.name = 'Player'

    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Make your bet: '))
            if max_bet > value > min_bet:
                self.bet = value
                self.money -= self.bet
                break
        print('Your bet is: ', self.bet)

    def ask_card(self):
        choice = input(MESSAGES.get('ask_card'))
        return choice == 'y'


class Dealer(AbstractPlayer):

    def __init__(self):
        super().__init__()
        self.name = 'Dealer'
        self.max_points = 17

    def change_bet(self, max_bet, min_bet):
        print('This type is dealer so it has no bets')

    def ask_card(self):
        return self.full_points < self.max_points

    def print_money(self):
        pass


class Bot(AbstractPlayer):
    def __init__(self, name):
        super().__init__()
        self.max_points = random.randint(17, 20)
        self.name = name

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(f'{self.name} give: {self.bet}')

    def ask_card(self):
        return self.full_points < self.max_points
