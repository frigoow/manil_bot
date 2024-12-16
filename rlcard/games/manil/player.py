from rlcard.games.manil.utils.manil_card import ManilCard


class ManilPlayer:

    def __init__(self, player_id: int):
        self.player_id: int = player_id
        self.hand : [ManilCard] = []
        self.table_hand : [ManilCard] = []

    def get_available_cards(self) -> [ManilCard] :
        return self.hand + self.table_hand

    def remove_card_from_hand(self, card: ManilCard):
        self.hand.remove(card)

    def remove_card_from_table(self, card: ManilCard):
        self.table_hand.remove(card)

    def add_card_to_table_hand(self, card: ManilCard):
        self.table_hand.append(card)

    def __str__(self):
        return ['N', 'E', 'S', 'W'][self.player_id]