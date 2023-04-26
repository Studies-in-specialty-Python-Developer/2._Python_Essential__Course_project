""" Модуль описывает свойства и метода класса, который реализует игровую логику и функционал
карточной игры BlackJack. Реализован только базовый функционал игры, без разновидностей правил
и некоторых особенностей хода игры """

import random

from deck import Deck
from player import Bot, Player, Dealer, AbstractPlayer
from const import MESSAGES, MAX_PLAYER_COUNT


class Game:
    """ Абстрактный класс реализует базовую функциональность каждого игрока в BlackJack.
    Класс служит предком для игроков Дилер (Dealer), Игрок (Player), игрок-бот (Bot)
    Attributes:
        players (list): список игроков, не считая дилера
        player (Player): игрок-человек
        player_pos (int): номер по порядку игрока-человека за столом
        dealer (Dealer): бот-дилер
        all_players_count (int): общее количество игроков, не считая дилера
        deck (Deck): колода карт
        max_bet (int): максимальная ставка
        min_bet (int): минимальная ставка
    Methods:
        __init__(self):
            инициализирует атрибуты значениями по умолчанию
        _ask_starting(self, message: str) -> bool:
            задает игроку вопрос о его (не)желании сыграть в BlackJack
        _launching(self):
            создает объекты игроков-ботов в заданном количестве, игрока-человека и генерирует его позицию
            по порядку за игровым столом
        ask_bet(self):
            игроки делают ставки в пределах минимальной и максимальной суммы
        first_descr(self):
            реализует первую раздачу карт, всем игрокам дилер сдает по две карты, а себе берет одну
        check_stop(player: AbstractPlayer) -> bool:
            статический метод, который делает проверку на превышение набранных игроком очков
            по сравнению с максимальным значением 21
        ask_cards(self):
            реализует процесс сдачи игроку дополнительных карт (после первой раздачи)
        check_winner(self):
            Делает проверку результата игры для каждого игрока и выдает соответствующее сообщение.
            Подсчитывает выигрыш или проигрыш каждого игрока и оставшуюся сумму денег
        play_with_dealer(self):
            реализует выдачу дополнительных карт (после первой раздачи) дилером самому себе
        print_all_players_cards(self):
            показывает в консоли карты, находящиеся на руках у всех игроков и у дилера
        print_all_players_money(self):
            показывает в консоли оставшуюся сумму денег у каждого игрока
        start_game(self):
            Реализует процесс игры """

    def __init__(self):
        """ Инициализирует атрибуты значениями по умолчанию """
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.min_bet, self.max_bet = 5, 20

    def _ask_starting(self, message: str) -> bool:
        """ Задает игроку вопрос о его (не)желании сыграть в BlackJack
        Arguments:
            message (str): вопрос в виде строки
        Returns:
            bool - выбор игрока """
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            if choice == 'y':
                for player in self.players:
                    player.cards.clear()
                self.dealer.cards.clear()
                return True

    def _launching(self):
        """ Создает объекты игроков-ботов в заданном количестве и игрока-человека, генерирует его позицию
         по порядку за игровым столом. Созданные объекты сохраняются в атрибутах класса """
        while True:
            bots_count = int(input('Hello, enter number of bots: '))
            if bots_count <= MAX_PLAYER_COUNT - 1:
                break
        self.all_players_count = bots_count + 1
        for i in range(bots_count):
            bot = Bot(f'Bot {i + 1}')
            self.players.append(bot)
        self.player = Player()
        self.player_pos = random.randint(0, self.all_players_count)
        print(f'Your position is: {self.player_pos}\n')
        self.players.insert(self.player_pos, self.player)

    def ask_bet(self):
        """ Игроки делают ставки в пределах минимальной и максимальной суммы """
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def first_descr(self):
        """ Реализует первую раздачу карт, всем игрокам дилер сдает по две карты, а себе берет одну """
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

        card = self.deck.get_card()
        self.dealer.take_card(card)

    @staticmethod
    def check_stop(player: AbstractPlayer) -> bool:
        """ Производится проверка на превышение набранных игроком очков по сравнению с максимальным значением 21
        Arguments:
            player (AbstractPlayer): проверяемый игрок
        Returns:
            bool - набрал ли игрок более 21 очка """
        return player.full_points >= 21

    def ask_cards(self):
        """ Реализует процесс сдачи игроку дополнительных карт (после первой раздачи) """
        for player in self.players:
            if player.full_points < 21:

                while player.ask_card():
                    card = self.deck.get_card()
                    player.take_card(card)

                    is_stop = self.check_stop(player)
                    if is_stop:
                        break

                    if isinstance(player, Player):
                        player.print_cards()

    def check_winner(self):
        """ Производит проверку результата игры для каждого игрока и выдает соответствующее сообщение.
        Подсчитывает выигрыш или проигрыш каждого игрока и оставшуюся сумму денег """
        if self.dealer.full_points > 21:
            # all win
            print('Dealer are fall! All players in game are win!')
            for winner in self.players:
                winner.money += winner.bet * 2

        else:
            for player in self.players:
                if player.full_points == self.dealer.full_points:
                    player.money += player.bet
                    print(MESSAGES.get('eq').format(player=player.name,
                                                    points=player.full_points))
                elif self.dealer.full_points < player.full_points <= 21:
                    player.money += player.bet * 2
                    if isinstance(player, Bot):
                        print(MESSAGES.get('win').format(player.name))
                    elif isinstance(player, Player):
                        print('You are win!')

                elif any([player.full_points < self.dealer.full_points, player.full_points > 21]):
                    if isinstance(player, Bot):
                        print(MESSAGES.get('lose').format(player.name))
                    elif isinstance(player, Player):
                        print('You lose!')

    def play_with_dealer(self):
        """ Реализует выдачу дополнительных карт (после первой раздачи) дилером самому себе """
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)

    def print_all_players_cards(self):
        """ Показывает в консоли карты, находящиеся на руках у всех игроков и у дилера """
        for player in self.players:
            player.print_cards()
        self.dealer.print_cards()

    def print_all_players_money(self):
        """ Показывает в консоли оставшуюся сумму денег у каждого игрока """
        for player in self.players:
            player.print_money()

    def start_game(self):
        """ Реализует процесс игры """

        # generating data for starting
        self._launching()

        while True:
            # ask about bet
            self.ask_bet()

            # give first cards to the players
            self.first_descr()

            # print all players and dealer cards after first deal
            print('\nSituation after first deal')
            self.print_all_players_cards()

            # ask players about cards
            self.ask_cards()

            # dealer takes cards
            self.play_with_dealer()

            # print all players and dealer cards after second deal
            print('\nSituation after second deal')
            self.print_all_players_cards()
            print()

            self.check_winner()

            print('\nPlayers money')
            self.print_all_players_money()

            print()
            if not self._ask_starting(MESSAGES.get('run_again')):
                break

            if len(self.deck) < (self.all_players_count + 1) * 3:
                print('\nThe deck of cards is over!')
                break
