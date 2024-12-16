from rlcard.envs import Env
from rlcard.games.manil import Game

class ManilEnv(Env):

    def __init__(self, config):
        self.name = 'manil'
        self.game = Game()
        super().__init__(config=config)
        state_shape_size = self.manilStateExtractor.get_state_shape_size()
        #self.state_shape = [[1, state_shape_size] for _ in range(self.num_players)]
        #self.action_shape = [None for _ in range(self.num_players)]