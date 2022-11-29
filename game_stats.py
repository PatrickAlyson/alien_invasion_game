import json


class GameStats:
    """ Tracks statistics for alien invasion game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion at an active state
        self.game_active = False

        # Chow the difficult selection buttons
        self.difficulty_flag = False

        # High score should never be reset.
        # self.high_score = 0
        self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """Reads the high score saved in a file."""
        try:
            file_name = 'saveconfig.json'
            with open(file_name, 'r') as fo:
                self.read_high_score = fo.read()
                self.read_high_score = self.read_high_score.strip()
                self.read_high_score = int(self.read_high_score)
        except FileNotFoundError:
            self.read_high_score = 0
        self.high_score = self.read_high_score

    def save_high_score(self):
        """Save the high score in a file."""
        file_name = 'saveconfig.json'
        if self.high_score > self.read_high_score:
            with open(file_name, 'w') as fo:
                json.dump(self.high_score, fo)
        elif self.high_score == self.read_high_score:
            with open(file_name, 'w') as fo:
                json.dump(self.high_score, fo)
        else:
            with open(file_name, 'w') as fo:
                json.dump(self.read_high_score, fo)
