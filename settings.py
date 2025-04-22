"""
settings.py

This module defines the Settings class, which stores all the configurable settings
for the Alien Invasion game. These settings include screen dimensions, ship properties,
bullet properties, and alien fleet behavior.

Classes:
    Settings: A class to store all game settings.

Usage:
    The Settings class is instantiated at the start of the game and provides access
    to all static and dynamic settings throughout the game.

"""

from pathlib import Path

class Settings:
    "A class to store all settings for Alien Invasion."

    def __init__(self):
        """Initialize the game's static settings."""
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 100, 100)

        # Bullet settings
        self.bullet_color = (60, 60, 60)

        # Alien settings
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

        # Button settings
        self.button_color = (0, 0, 0)
        self.button_w = 200
        self.button_h = 50
        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 48
        self.font_file = Path.cwd () / "fonts" / "UnifrakturMaguntia-Regular.ttf"

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""

        # Ship settings
        self.ship_speed = 4
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 25
        self.bullet_height = 28
        self.bullet_speed = 20
        self.bullets_allowed = 3

        
        self.alien_speed = 5.0

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1