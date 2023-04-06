import pygame

from app.utils.constants import DEFAULT_TYPE,DINO_DUCKING,DINO_JUMPING,DINO_RUNNING, DUCK_IMG,JUMP_IMG,RUN_IMG,JUMP_SOUND,HEART_TYPE,SCREEN_WIDTH
from app.utils.message_util import print_message


class Dinosaur(pygame.sprite.Sprite):
    POSITION_X = 80
    POSITION_y = 310
    JUMP_VELOCITY = 8.5
    DUCKING_VELOCITY = 340

    def __init__(self,player_name):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_y
        self.player_name = player_name
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0
        self.lives = 3
        self.improvement_duration = 0
        self.jump_sound = JUMP_SOUND
        

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
        print("VELOCITY:: ", self.jump_velocity)
        print("y       :: ", self.rect.y)
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
        print_message(f"Lives: {self.lives}", screen, 950, 55, font_size=24)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def pick_a_heart(self, improvement):
        self.type = improvement .type
        self.improvement_duration = improvement .start_time + \
            (improvement .duration * 1000)
        if self.type == HEART_TYPE:
            self.lives += 1

    def check_improvement(self,screen):
        time_to_show = round((self.improvement_duration - pygame.time.get_ticks()) / 1000, 2)
        if time_to_show >= 0:
            half_screen_width = SCREEN_WIDTH // 2
            if self.type == HEART_TYPE:
                print_message("You win an extra live.", screen, half_screen_width, 50, font_size=16)
            else:
                print_message("Unknown improving!", screen, half_screen_width, 50, font_size=16)
        else:
            self.type = DEFAULT_TYPE
            self.improvement_duration = 0
    
