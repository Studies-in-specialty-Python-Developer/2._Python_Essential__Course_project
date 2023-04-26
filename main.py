""" Модуль является стартовым модулем (точкой входа) для карточной игры в BlackJack """

from game import Game


def main():
    """ Основная функция, в которой инициализируется и запускается новая игра """
    game = Game()
    game.start_game()
    game.player.print_money()


if __name__ == "__main__":
    main()
