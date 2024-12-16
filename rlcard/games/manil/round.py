from rlcard.games.manil.judger import ManilJudger
from rlcard.games.manil.player import ManilPlayer
from rlcard.games.manil.utils.manil_card import ManilCard
from rlcard.games.manil.utils.move import ManilMove


class ManilRound:

    def __init__(self, round_num, players : [ManilPlayer], current_player, trump):
        self.players = players
        self.round_num = round_num
        self.num_players = len(players)
        self.current_player_index = current_player
        self.first_player_index = current_player
        self.trump = trump
        self.winner = None
        self.payoffs = []
        self.moves : [ManilMove] = []


    def is_over(self) -> bool:
        return len(self.moves) == 4

    def get_legal_actions(self):
        player : ManilPlayer = self.players[self.current_player_index]
        cards : [ManilCard] = player.get_available_cards()
        legal_actions : [ManilCard] = []
        if len(self.moves) == 0:
            legal_actions = cards
        else:
            winner, _, ind = ManilJudger.judge(self.moves, self.trump)
            first_move : ManilMove = self.moves[0]
            winning_move : ManilMove = self.moves[ind]
            is_winning = winner == self.current_player_index
            suit_cards = list(filter(lambda c: c.suit_index == first_move.card.suit_index, cards))
            if is_winning:
                if len(suit_cards) > 0:
                    legal_actions = suit_cards
                else:
                    legal_actions = cards
            else:
                if len(suit_cards) > 0 and winning_move.card.suit_index == self.trump:
                    legal_actions = suit_cards
                elif len(suit_cards) > 0 and winning_move.card.suit_index != self.trump:
                    higher_suit_cards = list(filter(lambda c: c.rank_index > winning_move.card.rank_index, suit_cards))
                    if len(higher_suit_cards) > 0:
                        legal_actions = higher_suit_cards
                    else:
                        legal_actions = suit_cards
                elif len(suit_cards) == 0 and winning_move.card.suit_index == self.trump:
                    higher_trump_cards = list(filter(lambda c: c.rank_index > winning_move.card.rank_index and c.suit_index == self.trump, cards))
                    if len(higher_trump_cards) > 0:
                        legal_actions = higher_trump_cards
                    else:
                        non_trump_cards = list(filter(lambda c: c.suit_index != self.trump, cards))
                        if len(non_trump_cards) > 0:
                            legal_actions = non_trump_cards
                        else:
                            legal_actions = cards
                # to buy the card
                else:
                    trump_cards = list(filter(lambda c: c.rank_index > c.suit_index == self.trump, cards))
                    if len(trump_cards) > 0:
                        legal_actions = trump_cards
                    else:
                        legal_actions = cards
        assert len(legal_actions) > 0
        return legal_actions
