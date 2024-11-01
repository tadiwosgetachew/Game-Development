import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        '''Initialize the alien and set its starting position'''
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        #load the alien image and set it rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each alien near the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)
    def check_edges(self):
        """Checks to see if the aliens are at either edges and return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """Move the aliens to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        '''draw the alien at its current location'''
        self.screen.blit(self.image, self.rect)
