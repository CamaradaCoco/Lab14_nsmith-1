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
        self.font_file = Path.cwd () / "Assets" / "fonts" / "UnifrakturMaguntia-Regular.ttf"

        # HUD settings
        self.score_file = Path.cwd () / "Assets" / "file" / "scores.json"
        self.hud_color = (0, 0, 0)
        self.hud_w = 200
        self.hud_h = 50
        self.hud_font_size = 48
        self.hud_font_color = (255, 255, 255)
        self.hud_font_file = Path.cwd () / "Assets" / "fonts" / "UnifrakturMaguntia-Regular.ttf"

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""

        # Ship settings
        self.ship_speed = 4
        self.ship_limit = 1

        # Bullet settings
        self.bullet_width = 25
        self.bullet_height = 28
        self.bullet_speed = 20
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 15
        self.alien_points = 50

    def increase_difficulty(self) -> None:
        """Increase speed settings."""
        self.ship_speed *= 1.1
        self.bullet_speed *= 1.1
        self.alien_speed *= 1.1

        # Increase the fleet's drop speed.
        self.fleet_drop_speed *= 1.1

        # Increase the number of bullets allowed.
        if self.bullets_allowed < 10:
            self.bullets_allowed += 1