import random
from app.components.Obstacles.bird import Bird
from app.components.Obstacles.cactus import Cactus
from app.utils.message_util import print_message
from app.utils.constants import BIRD_TYPE, LARGE_CACTUS_TYPE, SMALL_CACTUS_TYPE,DIE_SOUND


class ObstacleGenerator:
    def __init__(self):
         self.cactus = []
         self.birds = [] 
         self.num_obstacles_evaded = 0
         self.num_birds_evaded = 0
         self.num_obstacles_hit = 0
         self.num_birds_hit = 0
         self.sound = DIE_SOUND
         self.minus = 0

    def update(self, game_speed, player,points, die):
        game_speed = game_speed * 1.4
        if not self.cactus:  #Verifica si la lista de obstáculos está vacía, en cuyo caso se procede a agregar nuevos obstáculos.
            if random.randint(0, 1): #Agregar nuevos cactos
                self.cactus.append(Cactus(SMALL_CACTUS_TYPE))
            else:
                self.cactus.append(Cactus(LARGE_CACTUS_TYPE))

        if len(self.birds) < 1 and random.randint(0, 100) == 1:
            self.birds.append(Bird())

        for obstacle in self.cactus:
            obstacle.update(game_speed, self.cactus)
            if obstacle.collide(player):
                self.sound.play()
                self.num_obstacles_hit += 1
                points.score -= 50
                #pygame.time.delay(500)
            if obstacle.rect.right < player.rect.left and not obstacle.passed and not obstacle.has_collided:
                obstacle.passed = True
                self.num_obstacles_evaded += 1
                points.score += 100

        for bird in self.birds:
            bird.update(game_speed, self.birds)
            if bird.collide(player):
                self.sound.play()
                self.num_birds_hit += 1
                points.score -= 25
            elif bird.rect.right < player.rect.left and not bird.passed and not bird.has_collided:
                bird.passed = True
                self.num_birds_evaded += 1
                points.score += 75

        if(points.score<= -100):
            die()
                
    def draw(self, screen,player):
        for obstacle in self.cactus:
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
        self.cactus = []
        self.birds = []
        self.num_birds_hit = 0
        self.num_obstacles_hit = 0
        self.num_birds_evaded = 0
        self.num_obstacles_evaded = 0






    """if not self.obstacles:
            obstacle_types = [Cactus(), Bird()]
            obstacle = random.choice(obstacle_types)
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.collide(player):
                if obstacle.type == SMALL_CACTUS_TYPE or obstacle.type == LARGE_CACTUS_TYPE:
                    self.num_obstacles_hit += 1
                    points.score -= 50 # Restar puntos al colisionar con cactus
                else:
                    self.num_birds_hit += 1
                    points.score -= 25 # Restar puntos al colisionar con pájaro
            elif obstacle.rect.right < player.rect.left and not obstacle.passed:
                obstacle.passed = True
                if obstacle.type == BIRD_TYPE:
                    self.num_birds_evaded += 1
                    points.score += 75 # Sumar puntos al evadir un pájaro
                else:
                    self.num_obstacles_evaded += 1
                    points.score += 100 # Sumar puntos al evadir un cactuS
                    
        if(points.score<= -100):
                die()
        if obstacle.check_collision(player.rect):
            self.sound.play()
            if obstacle.type == BIRD_TYPE:
                # Incrementar el contador de colisiones con pájaros
                self.num_birds_hit += 1
                points.score -= 25
            elif obstacle.type in [LARGE_CACTUS_TYPE, SMALL_CACTUS_TYPE]:
                # Incrementar el contador de colisiones con cactus
                self.num_obstacles_hit += 1
                points.score -= 50

            # Restricción para asegurarse de que no se incremente el contador de evasiones
            if not obstacle.check_evaded(player.rect):
                if obstacle.type == BIRD_TYPE:
                    # Incrementar el contador de evasiones de pájaros si el pájaro ha pasado al jugador
                    self.num_birds_evaded += 1
                    points.score += 75
                elif obstacle.type in [LARGE_CACTUS_TYPE, SMALL_CACTUS_TYPE]:
                    # Incrementar el contador de evasiones de cactus si el cactus ha pasado al jugador
                    self.num_obstacles_evaded += 1
                    points.score += 100
        else:
            if obstacle.check_evaded(player.rect):
                if obstacle.type == BIRD_TYPE:
                    # Incrementar el contador de evasiones de pájaros si el pájaro ha pasado al jugador
                    self.num_birds_evaded += 1
                    points.score += 75
                elif obstacle.type in [LARGE_CACTUS_TYPE, SMALL_CACTUS_TYPE]:
                    # Incrementar el contador de evasiones de cactus si el cactus ha pasado al jugador
                    self.num_obstacles_evaded += 1
                    points.score += 100"""
    
    









        