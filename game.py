""" Модуль описывает свойства и метода класса, который реализует игровую логику и функционал
карточной игры BlackJack. Реализован только базовый функционал игры, без разновидностей правил """

import random
from deck import Deck
from player import Bot, Player, Dealer
from const import MESSAGES


class Game:
    max_player_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

    def _ask_starting(self, message):
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
        while True:
            bots_count = int(input('Hello, enter number of bots: '))
            if bots_count <= self.max_player_count - 1:
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
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def first_descr(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)

        card = self.deck.get_card()
        self.dealer.take_card(card)

    @staticmethod
    def check_stop(player):
        return player.full_points >= 21

    def remove_player(self, player):
        player.print_cards()
        if isinstance(player, Player):
            print('    You are fall!')
        elif isinstance(player, Bot):
            print(player.name, 'are fall!')
        self.players.remove(player)

    def ask_cards(self):
        for player in self.players:
            if player.full_points < 21:

                while player.ask_card():
                    card = self.deck.get_card()
                    player.take_card(card)

                    is_stop = self.check_stop(player)
                    if is_stop:
                        # if player.full_points > 21 or isinstance(player, Player):
                        #     self.remove_player(player)
                        break

                    if isinstance(player, Player):
                        player.print_cards()

    def check_winner(self):
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
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)

    def print_all_players_cards(self):
        for player in self.players:
            player.print_cards()
        self.dealer.print_cards()

    def print_all_players_money(self):
        for player in self.players:
            player.print_money()
        self.dealer.print_money()

    def start_game(self):

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
