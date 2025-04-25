import pygame as pg
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Lab14 import AlienInvasion

class HUD:

    def _init__(self, game: 'AlienInvasion') -> None:
        """Initialize the HUD."""

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.stats = game.game_stats
        self.font = pg.font.Font(str(self.settings.hud_font_file), self.settings.hud_font_size)
        self.padding = 20
        self.update_scores()
        self._update_high_score()
        self.setup_life_image()
        self.update_level()

    def update_scores(self) -> None:
        """Update the scores."""

    def _update_score(self) -> None:
        """Update the score."""

        score_str = (f"Score: {self.stats.score}", True, self.settings.hud_font_color, self.settings.hud_color)
        self.score_image = self.font.render(score_str, True, self.settings.hud_font_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.padding

    def _update_high_score(self):
        high_score_str = (f"Score: {self.stats.score}", True, self.settings.hud_font_color, self.settings.hud_color)
        self.high_score_image = self.font.render(high_score_str, True, self.settings.hud_font_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.boundaries.right - self.padding
        self.high_score_rect.top = self.padding

    def setup_life_image(self) -> None:
        """Set up the life image."""

        self.setup_life_image()

    def update_level(self):
        """Update the level."""

        self.update_level()


    