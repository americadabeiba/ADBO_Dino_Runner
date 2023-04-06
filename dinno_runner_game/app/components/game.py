import random
import pygame

from app.utils.constants import BG, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,ICON,COLOR_LAVANDA,FONT_STYLE_CONSOLE,DINO_START,GAME_SOUND,GAME_OVER,PHRASES, DINO_DEATH,RESET,SHIELD_TYPE,HAMMER_TYPE
from app.utils.message_util import print_message

from app.components.dinosaur import Dinosaur
from app.components.Background.background_generator import BackgroundGenerator
from app.components.Obstacles.obstacle_generator import ObstacleGenerator
from app.components.Improvements.improvements_manager import ImprovementManager
from app.components.score import Score


class Game:
    def __init__(self,player_name):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False 
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.max_score = 0
        self.player = None
        self.death_count = 0

        self.player = Dinosaur(player_name)
        self.background_generator = BackgroundGenerator()
        self.obstacle_generator = ObstacleGenerator()
        self.improvement_manager = ImprovementManager()
        self.score = Score()

        self.sonido = GAME_SOUND

    def run(self):
        self.executing = True  
        while self.executing:
            """for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.executing = False"""
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def start_game(self):
        # Game loop: events - update - draw
        #self.sonido.play(loops=-1)
        self.playing = True
        self.obstacle_generator.reset()
        self.improvement_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #self.sonido.stop()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.background_generator.update()
        self.obstacle_generator.update(self.game_speed, self.player,self.score,self.die)
        self.score.update(self)
        self.improvement_manager.update(self.game_speed, self.score.score, self.player)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((COLOR_LAVANDA))
        self.background_generator.draw(self.screen)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_generator.draw(self.screen,self.player)
        self.score.draw(self.screen)
        self.improvement_manager.draw(self.screen)
        self.player.check_improvement(self.screen)
        #pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def die(self):
        #is_invincible = self.player.type == SHIELD_TYPE or self.player.type == HAMMER_TYPE 
        #if not is_invincible:
            pygame.time.delay(500)
            self.death_count  += 1
            self.player.lives -=1
            self.playing=False
        
    def show_menu(self):
        self.screen.fill((206,233,218))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if not self.death_count:
            print_message(f"Welcome {self.player.player_name} press", self.screen, half_screen_width, half_screen_height+30, FONT_STYLE_CONSOLE, 25)
            print_message(f"any key to Start!", self.screen, half_screen_width, half_screen_height+80, FONT_STYLE_CONSOLE, 25)
            self.screen.blit(DINO_START, (half_screen_width - 40, half_screen_height - 140))
        elif self.player.lives == 0:
            self.screen.blit(GAME_OVER, (half_screen_width - 200, half_screen_height))
            self.screen.blit(DINO_DEATH, (half_screen_width - 40, half_screen_height - 140))
        else:
            motivational_phrases = PHRASES
            index = random.randint(0,19)
            self.screen.blit(RESET, (half_screen_width-50, half_screen_height-150))
            print_message(motivational_phrases[index], self.screen, half_screen_width, half_screen_height, font_color=(149,224,185))
            print_message(f"Deaths: {self.death_count}", self.screen, half_screen_width, half_screen_height + 50)
            print_message(f"Lives: {self.player.lives}", self.screen, half_screen_width, half_screen_height + 100)
            
        pygame.display.update()
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

            elif event.type == pygame.KEYDOWN:
                self.score.reset()
                if self.player.lives == 0:
                    self.player.lives = 3
                self.start_game()

    