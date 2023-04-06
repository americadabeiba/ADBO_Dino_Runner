import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))
START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUDS = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud3.png'))
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))

SKY_COLD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Sky_Cold.jpg'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

#Types
DEFAULT_TYPE = "default"
DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"
LARGE_CACTUS_TYPE = "LARGE_CACTUS"
SMALL_CACTUS_TYPE = "SMALL_CACTUS"

#Colors
COLOR_NEGRO = (0,0,0)
COLOR_BLANCO = (255,255,255)
COLOR_ICY_BLUE = (145,216,242)

FONT_STYLE = "freesansbold.ttf"

#Penguin
ICON_PINGU =    pygame.image.load(os.path.join(IMG_DIR, "Penguin/Penguin_icon.png"))

PINE_TREES = [
    pygame.image.load(os.path.join(IMG_DIR, "Pine_tree/LargePineTree.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Pine_tree/LargePineTree2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Pine_tree/LargePineTree3.png")),
]

IGLUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Iglu/SmallIglu1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Iglu/SmallIglu2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Iglu/SmallIglu3.png")),
]

PENGUIN_START = pygame.image.load(os.path.join(IMG_DIR, "Penguin/Penguin_start.gif"))
penguin_width, penguin_height = PENGUIN_START.get_size()
PENGUIN_START = pygame.transform.scale(PENGUIN_START, (int(penguin_width * 0.30), int(penguin_height * 0.3)))


