""" Модуль является стартовым модулем (точкой входа) для карточной игры в BlackJack """

from game import Game


def main():
    game = Game()
    game.start_game()
    print(game.player.money)


if __name__ == "__main__":
    main()
