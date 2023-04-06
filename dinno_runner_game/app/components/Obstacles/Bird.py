import random

from app.components.Obstacles.obstacle import Obstacle
from app.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD[0])
        self.rect.y = random.randint(100, 200)
        self.index = 0
        self.counter = 0    #frecuencia del cambio de la imagen del pájaro.

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        self.counter += 1
        if self.counter == 8:
            self.counter = 0
            self.index += 1
            if self.index >= len(BIRD):
                self.index = 0
            self.image = BIRD[self.index]