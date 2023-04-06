import pygame

from app.utils.constants import BG, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,ICON,COLOR_LAVANDA,FONT_STYLE_CONSOLE,DINO_START
from app.components.background.background_generator import BackgroundGenerator
from app.components.dinosaur import Dinosaur
from app.utils.message_util import print_message
from app.components.Obstacles.obstacle_generator import ObstacleGenerator


class Game:
    def __init__(self):
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

        self.background_generator = BackgroundGenerator()
        self.player = None
        self.obstacle_manager = ObstacleGenerator()

    def run(self):
        self.player_name = input("Por favor, ingrese su nombre: ")
        self.player = Dinosaur(self.player_name)
        self.executing = True  #Añadido
        while self.executing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.executing = False
            if not self.playing:
                self.show_menu()

    def start_game(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.background_generator.update()
        self.obstacle_manager.update(self.game_speed, self.player)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.background_generator.draw(self.screen)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen,self.player)
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
    
    def show_menu(self):
        self.screen.fill(COLOR_LAVANDA)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        print_message(f"Welcome {self.player_name} press", self.screen, half_screen_width, half_screen_height+30, FONT_STYLE_CONSOLE, 25)
        print_message(f"any key to Start!", self.screen, half_screen_width, half_screen_height+80, FONT_STYLE_CONSOLE, 25)

        self.screen.blit(DINO_START, (half_screen_width - 40, half_screen_height - 140))
        pygame.display.update()
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
                return
            elif event.type == pygame.KEYDOWN:
                self.executing = False
                self.start_game()
                
        pygame.display.flip()

    