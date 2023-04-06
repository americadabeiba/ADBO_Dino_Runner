import random
from app.components.Obstacles.Bird import Bird
from app.components.Obstacles.cactus import Cactus
from app.utils.message_util import print_message
from app.utils.constants import SMALL_CACTUS_TYPE,LARGE_CACTUS_TYPE


class ObstacleGenerator:
    def __init__(self):
         self.obstacles = []
         self.birds = [] 
         self.num_obstacles_evaded = 0
         self.num_birds_evaded = 0
         self.num_obstacles_hit = 0
         self.num_birds_hit = 0
        
    def update(self, game_speed, player):
        if not self.obstacles:  #Verifica si la lista de obstáculos está vacía, en cuyo caso se procede a agregar nuevos obstáculos.
            if random.randint(0, 1):    # Agregar nuevos cactos
                self.obstacles.append(Cactus(SMALL_CACTUS_TYPE))
            else:
                self.obstacles.append(Cactus(LARGE_CACTUS_TYPE))

        if len(self.obstacles) < 2 and random.randint(0, 300) == 1:
            self.obstacles.append(Bird())
           
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.collide(player):
                self.num_obstacles_hit += 1
                #pygame.time.delay(500)
            if obstacle.rect.right < player.rect.left and not obstacle.passed and not obstacle.has_collided:
                obstacle.passed = True
                self.num_obstacles_evaded += 1


        for bird in self.birds:
            bird.update(game_speed, self.obstacles)
            if bird.collide(player):
                self.num_birds_hit += 1
                #pygame.time.delay(500)
            elif bird.rect.right < player.rect.left and not bird.passed and not bird.has_collided:
                bird.passed = True
                self.num_birds_evaded += 1

        for bird in self.birds:
            bird.update(game_speed, self.obstacles)
            if bird.rect.right < 0:
                if bird in self.birds:
                    self.birds.remove(bird)

        for bird in self.birds:
            bird.update(game_speed, self.obstacles)
            if bird.rect.right < 0:
                if bird in self.birds:
                    self.birds.remove(bird)

        # Agregar nuevos pájaros
        if len(self.birds) < 1 and random.randint(0, 100) == 1:
            self.birds.append(Bird())

                
    def draw(self, screen,player):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        for bird in self.birds:
            bird.draw(screen)
        
        messages = [f"Dinosaur name : {player.player_name}",
                    f"Dodge Birds   : {self.num_birds_evaded}", 
                    f"Dodge Cactus  : {self.num_obstacles_evaded}", 
                    f"Bird Strike   : {self.num_birds_hit}", 
                    f"Cactus Strike : {self.num_obstacles_hit}"]
        y_pos = 20
        for message in messages:
            print_message(message,screen,90,y_pos,font_size=15)
            y_pos += 15

    def reset(self):
        self.obstacles = []
        self.score = 0
        self.num_obstacles_evaded = 0
        self.num_birds_evaded = 0
        self.num_obstacles_hit = 0
        self.num_birds_hit = 0
    
    