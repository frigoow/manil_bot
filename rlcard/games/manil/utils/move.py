from rlcard.games.manil.player import ManilPlayer
from rlcard.games.manil.utils.manil_card import ManilCard


class ManilMove:

    def __init__(self, round_num, player : ManilPlayer, round_card_num, card):
        self.player : ManilPlayer = player
        self.round_num : int = round_num
        self.round_card_num : int = round_card_num
        self.card : ManilCard = card

    def __repr__(self):
        s = "<%d %d %d>" % (self.player.player_id, self.round_num, self.round_card_num)
        s += "  " + self.card.__repr__()
        return s