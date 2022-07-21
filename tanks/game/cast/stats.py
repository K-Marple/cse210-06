from constants import *
from game.cast.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug=False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._hits = 0
        self._lives = DEFAULT_LIVES
        self._score = 0

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: a number representing the points to add.
        """
        self._score += points

    def add_hits(self, hits):
        """Adds a hit for every barricade destroyed.
        
        Returns:
            a number representing the number of barricades hit.
        """
        self._hits += hits

    def get_lives(self):
        """Gets the lives.
        
        Returns:
            a number representing the lives.
        """
        return self._lives

    def get_score(self):
        """Gets the score.
        
        Returns:
            a number representing the score.
        """
        return self._score

    def get_hits(self):
        """Gets the hits.
        
        Returns:
            a number representing the number of hits.
        """
        return self._hits

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1

    # def next_level(self):
    #     """Adds one level."""
    #     self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._hits = 0
        self._lives = DEFAULT_LIVES
        self._score = 0