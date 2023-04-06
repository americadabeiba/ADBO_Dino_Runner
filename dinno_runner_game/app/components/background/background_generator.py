import random
import pygame

from app.utils.constants import SCREEN_WIDTH,CLOUDS
from app.components.Background.cloud import Cloud
from app.components.Background.sky import Sky

SCALE_FACTOR = 0.3

class BackgroundGenerator:
    def __init__(self):
        self.sky = Sky()
        self.sky_rect = self.sky.image.get_rect()
        self.cloud_images = CLOUDS
        self.clouds = pygame.sprite.Group()
        self.create_clouds()

    def create_clouds(self):
        for i in range(1,3):
            cloud_image = self.cloud_images[random.randint(0, 2)]
            scale_factor = SCALE_FACTOR 
            cloud = Cloud(
                cloud_image=cloud_image,
                x_pos=random.randint(0, SCREEN_WIDTH),
                y_pos=random.randint(0, 125),
                speed=random.randint(2, 3),
                scale_factor=scale_factor
            )
            self.clouds.add(cloud)

    def update(self):
        self.clouds.update()
        for cloud in self.clouds:
            if cloud.rect.right < 0:
                cloud_image = self.cloud_images[random.randint(0, 2)]
                self.clouds.remove(cloud)
                new_cloud = Cloud(
                    cloud_image = cloud_image,
                    x_pos=SCREEN_WIDTH,
                    y_pos=random.randint(0, 150),
                    speed=random.randint(2, 4),
                    scale_factor=SCALE_FACTOR
                )
                self.clouds.add(new_cloud)

    def draw(self, screen):
        self.sky.draw(screen)
        self.clouds.draw(screen)
