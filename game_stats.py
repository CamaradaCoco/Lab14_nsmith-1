# Lab 14 #1 (Side Alien Invasion Option) / Alien Invasion Game
# Nicholas Smith / 25 April 2025

"""
game_stats.py

This module defines the GameStats class, which is responsible for tracking and managing
statistics for the Alien Invasion game. These statistics include the number of ships
remaining and other game-related metrics.

Classes:
    GameStats: A class to track and manage game statistics.

Usage:
    The GameStats class is instantiated at the start of the game and is used to track
    statistics that can change during gameplay, such as the number of ships left.
"""

from pathlib import Path
import json

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Lab14 import AlienInvasion


class GameStats:
    """Track statistics for the game."""
    
    def __init__(self, AlienInvasion) -> None:
        """Initialize statistics."""

        self.game = AlienInvasion
        self.settings = AlienInvasion.settings
        self.high_score = 0
        self.max_score = 0
        self.level = 1
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self) -> None:
        """Initialize saved scores."""

        self.path = self.settings.score_file
        if self.path.exists():
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get("high_score", 0)
        else:
            self.high_score = 0
            self.save_scores()

    def save_scores(self) -> None:
        """Save scores to a file."""

        scores = {"high_score": self.high_score}
        
        contents = json.dumps(scores, indent=4)

        try:
            self.path.write_text(contents)
        except:
            FileNotFoundError(f"File {self.path} not found.")

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""

        self.ships_left = self.settings.ship_limit
        self.score = 0

    def update_stats(self, collisions) -> None:
        """Update the statistics."""

        # Update score
        self._update_score(collisions)

        self._update_max_score()

        # Update high score
        self._update_high_score()

    def _update_max_score(self):
        """Update max score if the current score is higher."""

        if self.score > self.max_score:
            self.max_score = self.score

    def _update_high_score(self):
        """Update high score if the current score is higher."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_scores()

    def _update_score(self, collisions):
        """Update the score based on collisions."""

        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self) -> None:
        """Update the level."""

        self.level += 1
        self.settings.increase_difficulty()