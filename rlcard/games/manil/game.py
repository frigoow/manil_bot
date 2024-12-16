import numpy as np

from rlcard.games.manil.player import ManilPlayer
from rlcard.games.manil.round import ManilRound


class ManilGame:

    def __init__(self):
        return

    def init_game(self):
        ''' Initialize players and state.

        Returns:
            dict: first state in one game
            int: current player's id
        '''
        self.num_games = 128
        self.current_game_index = 0
        # initialize public variables
        self.num_actions = 32
        self.num_players = 2
        self.players : [ManilPlayer] = [ManilPlayer(i) for i in range(2)]
        self.round = ManilRound(0, self.players, 0, 0)

        return self.state, 0

    def step(self, action):
        ''' Perform one draw of the game

        Args:
            action (str): specific action of doudizhu. Eg: '33344'

        Returns:
            dict: next player's state
            int: next player's id
        '''


        return

    def step_back(self):
        ''' Return to the previous state of the game

        Returns:
            (bool): True if the game steps back successfully
        '''
        if not self.round.trace:
            return False

        #winner_id will be always None no matter step_back from any case
        self.winner_id = None

        #reverse round
        player_id, cards = self.round.step_back(self.players)

        #reverse player
        if (cards != 'pass'):
            self.players[player_id].played_cards = self.round.find_last_played_cards_in_trace(player_id)
        self.players[player_id].play_back()

        #reverse judger.played_cards if needed
        if (cards != 'pass'):
            self.judger.restore_playable_cards(player_id)

        self.state = self.get_state(self.round.current_player)
        return True

    def get_state(self, player_id):
        ''' Return player's state

        Args:
            player_id (int): player id

        Returns:
            (dict): The state of the player
        '''
        player = self.players[player_id]
        others_hands = self._get_others_current_hand(player)
        num_cards_left = [len(self.players[i].current_hand) for i in range(self.num_players)]
        if self.is_over():
            actions = []
        else:
            actions = list(player.available_actions(self.round.greater_player, self.judger))
        state = player.get_state(self.round.public, others_hands, num_cards_left, actions)

        return state

    @staticmethod
    def get_num_actions():
        ''' Return the total number of abstract acitons

        Returns:
            int: the total number of abstract actions of doudizhu
        '''
        return 32

    def get_player_id(self):
        ''' Return current player's id

        Returns:
            int: current player's id
        '''
        return self.round.current_player

    def get_num_players(self):
        ''' Return the number of players in doudizhu

        Returns:
            int: the number of players in doudizhu
        '''
        return self.num_players

    def is_over(self):
        ''' Judge whether a game is over

        Returns:
            Bool: True(over) / False(not over)
        '''
        return self.round.round_num == 8