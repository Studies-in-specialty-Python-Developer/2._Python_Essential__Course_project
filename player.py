import abc


class AbstractPlayer(abc.ABC):

    def __init__(self, position):
        self.cards = []
        self.position = position

    def ask_card(self, deck):
        card = deck.get_card()
        self.cards.append(card)
        return True


class Player(AbstractPlayer):
    pass


# todo: is needed?
class Dealer(AbstractPlayer):
    pass


class Bot(AbstractPlayer):
    pass
