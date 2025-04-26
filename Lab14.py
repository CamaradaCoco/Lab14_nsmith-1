# Lab 14 #1 (Side Alien Invasion Option) / Alien Invasion Game
# Nicholas Smith / 25 April 2025

"""
This module defines the AlienInvasion class, which serves as the main entry point
for the Alien Invasion game. It manages the game's initialization, main loop, and
core functionality, including event handling, updating game objects, and rendering
the game screen.

Classes:
    AlienInvasion: The main class to manage game assets and behavior.

Usage:
    To start the game, run this module directly. The game initializes all resources,
    enters the main loop, and handles user input, game updates, and rendering.
"""

import sys
from pathlib import Path
from time import sleep
import pygame as pg
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pg.init()
        self.clock = pg.time.Clock()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        # Set up screen, fullscreen.
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()

        # Set title bar of game window.
        pg.display.set_caption("Alien Invasion")

        # Load laser sound
        self.laser_sound = pg.mixer.Sound(str(Path.cwd() / "Assets" / "sound" / "laser.mp3"))
        self.laser_sound.set_volume(0.05)

        # Load impact sound
        self.impact_sound = pg.mixer.Sound(str(Path.cwd() / "Assets" / "sound" / "impactSound.mp3"))

        # Create an instance to store game statistics.
        self.game_stats = GameStats(self)

        # Create instance of Ship class.
        self.ship = Ship(self)
        # Create a group to store bullets in.
        self.bullets = pg.sprite.Group()
        # Create a group of aliens.
        self.aliens = pg.sprite.Group()

        self._create_fleet()

        # Create the Play button.
        self.play_button = Button(self, "Play", self.settings)

        # Start alien invasion in an active state.
        self.game_active = False

    # ------------------------------
    # Event Handling Functions
    # ------------------------------
    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN and self.game_active:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_keydown_events(self, event) -> None:
        """Respond to key presses."""
        if event.key == pg.K_UP:
            self.ship.moving_up = True
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pg.K_q:
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        """Respond to key releases."""
        if event.key == pg.K_UP:
            self.ship.moving_up = False
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = False

    def _check_button_clicked(self) -> None:
        """Check if the play button was clicked."""
        mouse_pos = pg.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    # ------------------------------
    # Game Update Functions
    # ------------------------------
    def _update_bullets(self) -> None:
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        self._check_bullet_alien_collisions()

        for bullet in self.bullets.copy():
            if bullet.rect.left <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self) -> None:
        """Respond to bullet-alien collisions."""
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # If bullet collides with alien, play impact sound.
        if collisions:
            self.impact_sound.play()
            self.impact_sound.set_volume(30)
            self.impact_sound.fadeout(500)
            self.game_stats.update_stats(collisions)

        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            # Update states stats model
            # Update HUD

    def _update_aliens(self) -> None:
        """Check if the fleet is at an edge, then update the positions."""
        self._check_fleet_edges()

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_direction * self.settings.alien_speed

        if alien.rect.bottom >= self.screen.get_rect().bottom:
            alien.rect.x += self.settings.fleet_drop_speed

        # Look for alien-ship collisions.
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self) -> None:
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x += self.settings.fleet_drop_speed

    def _check_aliens_bottom(self) -> None:
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom or alien.rect.top <= 0:
                for alien in self.aliens.sprites():
                    alien.rect.x += self.settings.fleet_drop_speed
                self.settings.fleet_direction *= -1
                break

    def _ship_hit(self) -> None:
        """Respond to the ship being hit by an alien."""

        self.impact_sound.play()
        self.impact_sound.set_volume(30)
        self.impact_sound.fadeout(500)

        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(1.5)
        else:
            self.game_active = False

    def _fire_bullet(self) -> None:
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # ------------------------------
    # Game Reset Functions
    # ------------------------------
    def _check_game_status(self) -> None:
        """Check if the game is over and reset if necessary."""
        if self.game_stats.ships_left >= 0:
            self.game_stats.ships_left -= 1
            self._reset_level
            sleep(0.5)
        else:
            self.game_active = False
    
    def restart_game(self) -> None:
        """Restart the game by resetting stats, level, and recentering the ship."""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self._reset_level()
        self.game_active = True
        pg.mouse.set_visible(False)

    def _reset_level(self) -> None:
        """Reset the level to its initial state."""
        self.game_stats.reset_stats()
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()

    # ------------------------------
    # Rendering Functions
    # ------------------------------
    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            pg.draw.rect(self.screen, self.settings.bullet_color, bullet.rect)

        self.screen.blit(self.ship.image, self.ship.rect)

        for alien in self.aliens.sprites():
            self.screen.blit(alien.image, alien.rect)

        if not self.game_active:
            self.play_button.draw()
            pg.mouse.set_visible(True)

        # Draw HUD

        pg.display.flip()

    # ------------------------------
    # Fleet Creation Functions
    # ------------------------------
    def _create_fleet(self) -> None:
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 1.5 * alien_height):
            while current_x < (self.settings.screen_width - 10 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 1 * alien_width
            current_x = alien_width
            current_y += 1 * alien_height

    def _create_alien(self, x_position, y_position) -> None:
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    # ------------------------------
    # Main Game Loop
    # ------------------------------
    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()