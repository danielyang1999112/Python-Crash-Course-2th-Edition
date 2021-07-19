class GameStats:
    """Collecting game stats"""

    def __init__(self, ai_game):
        """Initializing stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Inactive
        self.game_active = False

        # High score won't be reset
        self.high_score = 0

    def reset_stats(self):
        """Initializing changing stats during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1