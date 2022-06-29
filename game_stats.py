class GameStats:
    """track stats for alien invasion"""

    def __init__(self,ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize stats that can change duriing the game"""
        self.ships_left = self.settings.ship_limit
