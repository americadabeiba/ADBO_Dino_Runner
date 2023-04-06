import pygame

class Cloud(pygame.sprite.Sprite):
    def __init__(self, cloud_image: pygame.Surface, x_pos, y_pos, speed, scale_factor):
        super().__init__()
        self.original_image = cloud_image
        self.image = pygame.transform.scale(cloud_image, (int(cloud_image.get_width() * scale_factor), int(cloud_image.get_height() * scale_factor)))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = speed
        self.scale_factor = scale_factor

    def update(self):
        self.rect.x -= self.speed
