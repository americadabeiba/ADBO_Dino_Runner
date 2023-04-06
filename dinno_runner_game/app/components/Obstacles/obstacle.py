from pygame import Surface
from pygame.sprite import Sprite

from app.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image: Surface):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.passed = False
        self.has_collided = False

    def update(self, game_speed, obstacles, player_x_position = 0):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            if self in obstacles:
                obstacles.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, player):
        if self.rect.colliderect(player.rect) and not self.has_collided: # Verificar que no se haya chocado ya
            self.has_collided = True
            return True
        return False