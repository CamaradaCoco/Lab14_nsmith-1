
import pygame as pg
import pygame.font
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