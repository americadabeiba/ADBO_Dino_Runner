import random
from pygame import Surface
from pygame.sprite import Sprite

from app.utils.constants import HEART_TYPE, SCREEN_WIDTH


class Improvement(Sprite):
    def __init__(self, image: Surface, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)
        self.type = type
        if type == HEART_TYPE:
            self.duration = 3
        else:
            self.duration = random.randint(5, 8) #Tiempo activo
        self.start_time = 0 #Momento de agarre del improvement

    def update(self, game_speed, improvements):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            improvements.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))