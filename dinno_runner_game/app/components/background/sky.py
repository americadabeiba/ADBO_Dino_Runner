import pygame
from app.utils.constants import SKY_PINK, SCREEN_HEIGHT, SCREEN_WIDTH

class Sky():
    def __init__(self):
        sky_width = SCREEN_WIDTH
        sky_height = SCREEN_HEIGHT
        self.image = pygame.transform.scale(SKY_PINK, (sky_width, sky_height))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image,(self.rect.x,self.rect.y))