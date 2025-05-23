# Lab 14 #1 (Side Alien Invasion Option) / Alien Invasion Game
# Nicholas Smith / 25 April 2025

"""
hud.py

This module defines the HUD class, which is responsible for displaying
game-related information such as the player's score, high score, remaining lives, and current level.

Classes:
    HUD: A class to manage and render the game's heads-up display.

Dependencies:
    - pygame: Used for rendering text and images on the screen.
    - typing.TYPE_CHECKING: Used for type hinting to avoid circular imports.
    - AlienInvasion: The main game class, passed to HUD for accessing game-related data.

Usage:
    The HUD class is initialized with an instance of the AlienInvasion game. It provides methods
    to update and render various HUD elements, such as scores, high scores, lives, and levels.

"""

import pygame as pg

class HUD:

    def __init__(self, game) -> None:
        """Initialize the HUD."""

        self.game = game
        self.settings = game.settings
        self.ship = game.ship
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.stats = game.game_stats
        self.font = pg.font.Font(str(self.settings.hud_font_file), self.settings.hud_font_size)
        self.padding = 20
        self.update_scores()
        self.setup_life_image()
        self.update_level()

    def update_scores(self) -> None:
        """Update the scores."""

        self._update_high_score()
        self._update_max_score()
        self._update_score()
        

    def _update_score(self) -> None:
        """Update the score."""

        score_str = (f"Score: {self.stats.score:,}")
        self.score_image = self.font.render(score_str, True, self.settings.hud_font_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self) -> None:
        """Update the max score."""

        max_score_str = (f"Max Score: {self.stats.max_score:,}")
        self.max_score_image = self.font.render(max_score_str, True, self.settings.hud_font_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_high_score(self):
        """UPdate the high score."""
        high_score_str = (f"High Score: {self.stats.high_score:,}")
        self.high_score_image = self.font.render(high_score_str, True, self.settings.hud_font_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.midtop = (self.boundaries.centerx, self.padding)
        
    def setup_life_image(self) -> None:
        """Set up the life image."""

        self.life_image = pg.transform.rotate(self.ship.image, -90).convert_alpha()
        #self.life_image = pg.transform.scale(self.life_image, (self.settings.ship_w, self.settings.ship_h))
        self.life_rect = self.life_image.get_rect()

    def update_level(self):
        """Update the level."""

        level_str = (f"Level: {self.stats.level:,}")
        self.level_image = self.font.render(level_str, True, self.settings.hud_font_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def draw(self) -> None:
        """Draw the HUD."""

        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()

    def _draw_lives(self) -> None:
        """Draw the lives to the screen."""
    
        current_x = self.padding
        current_y = self.padding

        for _ in range(self.stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width - 5

    