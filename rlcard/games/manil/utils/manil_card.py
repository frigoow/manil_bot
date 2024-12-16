

from rlcard.games.base import Card

SUITS = ['C', 'D', 'H', 'S']
RANKS = ['7', '8', '9', 'J', 'Q', 'K', 'A', 'T']
VALUES = [0, 0, 0, 1, 2, 3, 4, 5]

class ManilCard(Card):
    @staticmethod
    def card(card_id: int):
        return _deck[card_id]

    @staticmethod
    def get_deck() -> [Card]:
        return _deck.copy()

    def get_point_value(self):
        return VALUES[self.rank_index]

    def __init__(self, suit: str, rank: str):
        super().__init__(suit=suit, rank=rank)
        self.suit_index : int = SUITS.index(self.suit)
        self.rank_index : int = RANKS.index(self.rank)
        self.card_id = 8 * self.suit_index + self.rank_index
        self.is_table_card = False
        self.has_down_card = False

    def __str__(self):
        return f'{self.rank}{self.suit}'

    def __repr__(self):
        return f'{self.rank}{self.suit}'


_deck = [ManilCard(suit=suit, rank=rank) for suit in SUITS for rank in RANKS]  # want this to be read-only