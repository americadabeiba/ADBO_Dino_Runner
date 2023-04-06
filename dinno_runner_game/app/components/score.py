from app.utils.constants import POINT_SOUND
from app.utils.message_util import print_message


class Score:
    def __init__(self):
        self.score = 0
        self.sound = POINT_SOUND
        self.sound_played = False  # Bandera para indicar si el sonido se ha reproducido
        
    def update(self, game):
        #if game.player.type == HAMMER_TYPE:
       #     self.score += 10
        #else:
            #self.score += 1
            if self.score > 5000 and not self.sound_played:
                game.game_speed += 2
                self.sound.play()
                self.sound_played = True
            else:
                self.sound_played = False

    def draw(self, screen):
        print_message(f"Total points: {self.score}", screen, 950, 30, font_size=24)

    def reset(self):
         self.score = 0
    
    def __le__(self, other):
        if isinstance(other, int):
            return self.score <= other
        return NotImplemented
    