"""Module doctring"""


class Game:
    """Class representing a Bownling Game"""

    def __init__(
        self,
    ):
        print("Game created")
        self.total_score = 0;

    def score(self):
        """
        Score
        """
        return self.total_score

    def roll(self, pins_down: int):
        """Roll"""
        self.total_score += pins_down

