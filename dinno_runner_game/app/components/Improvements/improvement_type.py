from app.components.Improvements.improvement import Improvement
from app.utils.constants import HEART, HEART_TYPE,HAMMER,HAMMER_TYPE,SHIELD,SHIELD_TYPE


class Heart(Improvement):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)

class Hammer(Improvement):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)

class Shield(Improvement):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)



