import random
import pygame

from app.components.Improvements.improvement import Improvement
from app.components.Improvements.improvement_type import Heart


class ImprovementManager:
    def __init__(self):
        self.improvements: list[Improvement] = []
        self.when_appears = 0
    def update(self, game_speed, score, player):
        if not self.improvements and score == self.when_appears:
            self.when_appears += random.randint(200, 300)
            improvement_type = random.choice([Heart]) # Choose randomly between the 3 power-ups
            self.improvements.append(improvement_type())

        for improvement in self.improvements:
            improvement.update(game_speed, self.improvements)
            if improvement.rect.colliderect(player.rect):
                improvement.start_time = pygame.time.get_ticks()
                player.pick_a_heart(improvement)
                self.improvements.remove(improvement)

    def draw(self, screen):
        for improvement in self. improvements:
            improvement.draw(screen)

    def reset(self):
        self.improvements = []
        self.when_appears = random.randint(200, 300)
