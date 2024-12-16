from rlcard.games.manil.utils.manil_card import ManilCard
from rlcard.games.manil.utils.move import ManilMove


class ManilJudger:

    @staticmethod
    def judge(moves : [ManilMove], trump):
        if len(moves) <= 3:
            return None
        opening_card : ManilMove = moves[0]
        best : ManilMove = moves[0]
        if opening_card.card.suit_index == trump:
            for card in moves:
                if card.suit_index == best.card.suit_index and card.rank_index > best.card.rank_index:
                    best = card
        else:
            for card in moves:
                if ((card.suit_index == best.card.suit_index and card.rank_index > best.card.rank_index)
                        or (card.suit_index == trump and (best.card.suit_index != trump or best.card.rank_index < card.rank_index))):
                    best = card

        points = sum(c.get_point_value() for c in moves)
        ind = moves.index(best)
        winner = (best.player.player_id + ind) % 2
        return winner, points, ind

    @staticmethod
    def is_winning(moves, trump, current_player_index):
        winner, _, _ = ManilJudger.judge(moves, trump)
        return winner == current_player_index