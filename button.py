"""
button.py

This module defines the Button class, which is responsible for creating and managing
interactive buttons in the game. Buttons are used for actions such as starting the game
or interacting with the user interface.

Classes:
    Button: A class to create and render buttons, handle button clicks, and manage button properties.

Dependencies:
    - pygame: Used for rendering the button and handling user input.
    - settings: Provides configuration for button dimensions, colors, and fonts.

Usage:
    The Button class is initialized with an instance of the game, a message to display on the button,
    and a settings object. It provides methods to render the button and check for mouse clicks.

Example:
    from button import Button
    play_button = Button(game, "Play", settings)
    play_button.draw()
    if play_button.check_clicked(mouse_pos):
        print("Button clicked!")
"""

import pygame as pg
from settings import Settings

class Button:
    """A class to create a button."""

    def __init__(self, ai_game, msg, settings) -> None:
        """Initialize button attributes."""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = settings.button_w, settings.button_h
        self.button_color = settings.button_color
        self.text_color = settings.text_color
        self.font = pg.font.Font(str(settings.font_file), settings.button_font_size)

        # Build the button's rect object and center it.
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self._prep_msg(msg)

    def _prep_msg(self, msg) -> None:
        """Turn msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        """Draw the button on the screen."""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """Check if the button was clicked."""

        return self.rect.collidepoint(mouse_pos)