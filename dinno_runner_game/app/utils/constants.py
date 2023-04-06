import pygame
import os

pygame.mixer.init()
# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/dinosaur.png"))
START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))

DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
DINO_DEATH = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))

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

SKY_PINK = pygame.image.load(os.path.join(IMG_DIR, 'Other/Sky_Pink.gif'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))

#Types
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HEART_TYPE = "life"
HAMMER_TYPE = "enhance"
DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"

LARGE_CACTUS_TYPE = "LARGE_CACTUS"
SMALL_CACTUS_TYPE = "SMALL_CACTUS"

BIRD_TYPE= "BIRD"

DUCK_IMG ={ DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, HEART_TYPE: DUCKING}
JUMP_IMG ={ DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, HEART_TYPE: JUMPING}
RUN_IMG ={ DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, HEART_TYPE: RUNNING}


#Colors
COLOR_NEGRO = (0,0,0)
COLOR_BLANCO = (255,255,255)
COLOR_ICY_BLUE = (145,216,242)
COLOR_LAVANDA = (37, 150, 190)

FONT_STYLE = "freesansbold.ttf"
FONT_STYLE_CONSOLE = os.path.join(IMG_DIR, 'Other/PressStart2P-Regular.ttf')

# Lista de frases motivacionales
PHRASES = [
    "You're stronger than you think.",
    "Believe in yourself.",
    "Keep pushing forward.",
    "Never give up.",
    "You can do it.",
    "Stay positive.",
    "Be brave.",
    "Keep going.",
    "Stay focused.",
    "Dream big.",
    "You're capable of amazing things.",
    "Embrace challenges.",
    "You're unstoppable.",
    "Success is within reach.",
    "Keep chasing your dreams.",
    "Believe in your abilities.",
    "Keep moving forward.",
    "You're making progress.",
    "You're on the right track.",
    "Rise above challenges.",
    "You're resilient and strong."
]


#Sounds
JUMP_SOUND = pygame.mixer.Sound("C:\\Users\\asus\\OneDrive\\Documentos\\GitHub\\ADBO_Dino_Runner\\dinno_runner_game\\app\\assets\\Music\\jump.wav")
DIE_SOUND = pygame.mixer.Sound("C:\\Users\\asus\\OneDrive\\Documentos\\GitHub\\ADBO_Dino_Runner\\dinno_runner_game\\app\\assets\\Music\\die.wav")
POINT_SOUND = pygame.mixer.Sound("C:\\Users\\asus\\OneDrive\\Documentos\\GitHub\\ADBO_Dino_Runner\\dinno_runner_game\\app\\assets\\Music\\point.wav")
GAME_SOUND = pygame.mixer.Sound("C:\\Users\\asus\\OneDrive\\Documentos\\GitHub\\ADBO_Dino_Runner\\dinno_runner_game\\app\\assets\\Music\\Cats_on_Mars.wav")
