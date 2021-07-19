import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Managing ship class"""

    def __init__(self, ai_game):
        """Initializing ship and location"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # image for ship
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()

        # reload for each new ship
        self.rect.midbottom = self.screen_rect.midbottom

        # floats for Ship feature x
        self.x = float(self.rect.x)

        # moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Move ship according to the KEY"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed

        if self.moving_left and self.rect.left >0:
            self.rect.x -= self.settings.ship_speed

        # update self.x according to rect
        # self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """A fixed position for ship"""
        self.screen.blit(self.image, self.rect)
