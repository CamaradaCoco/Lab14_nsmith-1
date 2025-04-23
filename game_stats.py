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
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Lab14 import AlienInvasion


class GameStats:
    """Track statistics for the game."""
    
    def __init__(self, AlienInvasion) -> None:
        """Initialize statistics."""
        self.game = AlienInvasion
        self.settings = AlienInvasion.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def update_stats(self) -> None:
        """Update the statistics."""
        self.ships_left = self.settings.ship_limit - self.game.stats.ships_left
        self.score = self.game.stats.score
        self.level = self.game.stats.level