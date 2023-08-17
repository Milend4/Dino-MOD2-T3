import pygame
import os

# Global Constants
TITLE = "Sonic Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/Sonic_0.png"))



RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_00.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_01.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_02.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_03.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_04.png")),    
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_05.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_06.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_07.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_08.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_09.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_10.png")),    
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sprite_11.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Sonic_1.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/Sonic_2.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sonic_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sonic_5.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sonic_6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Sonic_7.png")),
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
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
