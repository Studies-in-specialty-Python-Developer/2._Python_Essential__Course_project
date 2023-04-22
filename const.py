""" Модуль содержит константы и настройки, необходимые для работы основного модуля main.py """

SUITS = ['spade', 'club', 'diamond', 'heart']

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

PRINTED = {'spade': '\u2660', 'club': '\u2663', 'diamond': '\u2666', 'heart': '\u2665'}

MESSAGES = {
    'ask_card': 'Want new card? (y/n) ',
    'eq': '{player} player has {points} points so it eq with dealer points\n {player} bid will be back',
    'win': '{} player are win',
    'lose': '{} player are lose',
    'run_again': 'Wanna play again? (y/n)'
}
