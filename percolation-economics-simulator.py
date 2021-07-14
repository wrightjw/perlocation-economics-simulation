class Percolation_Game:
    """
    Class to initialise and evolve the percolation game.
    """

    def __init__(self, initial_state, game_rules, game_dimensions):
        self.initial_state = initial_state
        self.game_rules = game_rules
        self.game_dimensions = game_dimensions
    
    def evolve_game(self, steps):
        state = self.initial_state
        previous_state = None
        round = []

        for t in range(steps):
            previous_state = state.copy()
            update.append(previous_state.grid)
            state = state
        
        update.append(state.grid)

        return update

