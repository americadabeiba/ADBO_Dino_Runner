import pygame
from app.utils.constants import SCREEN_WIDTH


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH  #Posición inicial del rectángulo en la coordenada x fuera de la pantalla en el borde derecho.
        self.passed = False
        self.has_collided = False # Agregar variable has_collided

    def update(self, game_speed, obstacles, player_x_position = 0):
        """self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            if self in obstacles:
                obstacles.remove(self)"""
        limit = -self.rect.width
        if player_x_position != 0:
            limit = player_x_position
        self.rect.x -= game_speed
        if self.rect.x < limit:
            if self in obstacles:
                obstacles.remove(self)

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def collide(self, player):
        if self.rect.colliderect(player.rect) and not self.has_collided: # Verificar que no se haya chocado ya
            self.has_collided = True
            return True
        return False