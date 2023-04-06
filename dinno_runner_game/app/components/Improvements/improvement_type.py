from app.components.Improvements.improvement import Improvement
from app.utils.constants import HEART, HEART_TYPE


class Heart(Improvement):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)


