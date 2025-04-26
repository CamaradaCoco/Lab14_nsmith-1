# Lab 14 #1 (Side Alien Invasion Option) / Alien Invasion Game
# Nicholas Smith / 25 April 2025

"""
alien.py

This module defines the Alien class, which represents a single alien in the fleet for the Alien Invasion game.
The Alien class handles the alien's initialization, movement, and edge detection.

Classes:
    Alien: A class to represent a single alien in the fleet.

Dependencies:
    - pygame: Used for rendering the alien and managing its sprite behavior.
    - pygame.sprite.Sprite: The base class for all game objects in the game.
    - pathlib.Path: Used for handling file paths to load the alien image.

Usage:
    The Alien class is initialized with an instance of the game. It provides methods to update the alien's position
    and check if the alien has reached the edge of the screen.
"""

import pygame as pg
from pygame.sprite import Sprite
from pathlib import Path

class Alien(Sprite):
    """Represents a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        image_path = Path.cwd() / "Assets" / "images" / "small.png"
        self.image = pg.image.load(str(image_path)).convert_alpha()
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""

        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True
        return False

    def update(self):
        """Move the alien to the right."""
        
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x