import random
from deck import Deck
from player import Bot, Player
from const import messages


class Game:

    def __init__(self):
        self.players = []
        self.player = None
        self.dealer = None
        self.all_players_count = 1
        self.deck = Deck()

    def _launching(self):
        bots_count = int(input('Hello, enter number of bots: '))
        self.all_players_count = bots_count + 1
        for i in range(bots_count):
            # Неправильное определение позиции бота в игре, возможны повторы
            # todo: should be randomly chosen
            bot = Bot(position=i)
            self.players.append(bot)

        # todo: should be randomly chosen
        player = Player(position=bots_count + 1)

    def start_game(self):
        # todo: max number of players?
        pass
