import random
from app.components.Obstacles.obstacle import Obstacle
from app.utils.constants import SMALL_CACTUS,LARGE_CACTUS,LARGE_CACTUS_TYPE,SMALL_CACTUS_TYPE

class Cactus(Obstacle):
    CACTUS = {
        LARGE_CACTUS_TYPE: (LARGE_CACTUS,300),
        SMALL_CACTUS_TYPE: (SMALL_CACTUS,325)
    }

    def __init__(self,cactus_type):
        image, pos_y = self.CACTUS[cactus_type]
        type = random.randint(0,2)
        super().__init__(image[type])
        self.rect.y = pos_y

