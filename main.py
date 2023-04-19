from deck import Deck
from game import Game


def main():
    d = Deck()
    print(d.get_card(), '  ', len(d))


if __name__ == "__main__":
    game = Game()
    game.start_game()
    main()
