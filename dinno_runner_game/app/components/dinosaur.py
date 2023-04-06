import pygame

from app.utils.constants import DEFAULT_TYPE,DINO_DUCKING,DINO_JUMPING,DINO_RUNNING, \
    DUCK_IMG,JUMP_IMG,RUN_IMG,JUMP_SOUND


class Dinosaur(pygame.sprite.Sprite):
    POSITION_X = 80
    POSITION_y = 310
    JUMP_VELOCITY = 8.5
    DUCKING_VELOCITY = 340

    def __init__(self,player_name):
        self.type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_y

        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0

        self.jump_sound = JUMP_SOUND

        self.player_name = player_name

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        print("VELOCITY ::", self.jump_velocity)
        print("y ::", self.rect.y)
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.jump_sound.play()
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = DINO_RUNNING
            self.rect.y = self.POSITION_y 
            

    def duck(self):
        print("Ducking")
        self.image = DUCK_IMG[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.DUCKING_VELOCITY
        self.step += 1

    def run(self):
        self.image = RUN_IMG[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_y
        self.step += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
