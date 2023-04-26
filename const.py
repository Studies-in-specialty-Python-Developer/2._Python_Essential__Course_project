""" Модуль содержит константы и настройки, необходимые для работы основного модуля main.py """

# Список мастей игральных карт
SUITS = ['spade', 'club', 'diamond', 'heart']

# Список рангов игральных карт
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

# Словарь символов, обозначающих масти карт
PRINTED = {'spade': '\u2660', 'club': '\u2663', 'diamond': '\u2666', 'heart': '\u2665'}

# Словарь, содержащий строковые сообщения для пользователя
MESSAGES = {
    'ask_card': 'Want new card? (y/n) ',
    'eq': '{player} player has {points} points so it eq with dealer points\n{player} bid will be back',
    'win': '{} player are win',
    'lose': '{} player are lose',
    'run_again': 'Wanna play again? (y/n)'
}

# Максимальное количество игроков, не считая дилера
MAX_PLAYER_COUNT = 4
