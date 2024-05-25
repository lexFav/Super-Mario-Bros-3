from pygame.locals import *
import numpy as np
import colorsys
import pygame
import coords
import random
import time
import math
import os
pygame.init()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
WIDTH, HEIGHT = 480, 360
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SMB 3")

# Constants
CENTER = (WIDTH / 2, HEIGHT / 2)
CENTER_X, CENTER_Y = CENTER
FPS = 30
FONT = pygame.font.Font('../../../Fonts/DotGothic16/DotGothic16-Regular.ttf', 24)
MOUSE = pygame.mouse
MOUSE_DOWN = lambda: MOUSE.get_pressed()[0]
TILE_SIZE = 32
GAME_LOOP_RUNNING = True
CLONE_COUNT_X = 16
CLONE_COUNT_Y = 13
CAMERA_X = 0
CAMERA_Y = 0
GRID_WIDTH = 0
GRID_HEIGHT = 0
KEY_WALK = 0
EDITOR = 0
LEVEL_NUM = 0
COINS = 0
BOUNCE_PLAYER = 0
BUMP_INDEX = None
LAYERS_BACKGROUND = 1
MARIO = 'Mini'
FIREBALLS = 0
STAR_POWER = 0
minus_TINY = 0
timer = 0
sin = lambda x: math.sin(math.radians(x))
cos = lambda x: math.cos(math.radians(x))
tan = lambda x: math.tan(math.radians(x))

# Lists
TILE_GRID = []
TILE_SHAPE = [
    '',
    '',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '',
    '',
    '',
    '',
    '',
    '',
    '=',
    '=',
    '=',
    '#',
    '#',
    '#',
    '#',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '=',
    '=',
    '=',
    '=',
    '',
    '',
    '',
    '',
    '',
    '',
    '#',
    '#',
    '#',
    '#',
    '',
    '',
    '',
    '',
    '#',
    '/10',
    r'\10',
    '/20',
    '/21',
    r'\20',
    r'\21',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '#',
    '',
    '',
    ''
]
TILE_GROUPS = [
    '',
    '',
    1,
    1,
    1,
    1,
    1,
    1,
    '',
    '',
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    4,
    4,
    4,
    4,
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    ''
]
OBJECT_IDX = []
OBJECT_TYPE = []
PARTICLES = []
LAYERS = [
    'background',
    'tile',
    'enemy',
    'particle',
    'mario'
]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 171, 25)
GRAY = (128, 128, 128)

# Images
BIG = pygame.Surface([36 * (TILE_SIZE / 32), 36 * (TILE_SIZE / 32)])
mario_walk_1 = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioWalk1.png'), [14 * (TILE_SIZE / 16), 27 * (TILE_SIZE / 16)])
mario_walk_2 = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioWalk2.png'), [TILE_SIZE, 27 * (TILE_SIZE / 16)])
mario_walk_3 = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioWalk3.png'), [TILE_SIZE, 26 * (TILE_SIZE / 16)])
mario_walk_4 = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioWalk4.png'), [TILE_SIZE, 27 * (TILE_SIZE / 16)])
mario_turn = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioTurn.png'), [TILE_SIZE, 28 * (TILE_SIZE / 16)])
mario_jump = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioJump.png'), [TILE_SIZE, 26 * (TILE_SIZE / 16)])
mario_crouch = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioCrouch.png'), [14 * (TILE_SIZE / 16), 18 * (TILE_SIZE / 16)])
mario_slide = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioSlide.png'), [TILE_SIZE, 26 * (TILE_SIZE / 16)])
mario_death = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioDeath.png'), [24 * (TILE_SIZE / 16), 24 * (TILE_SIZE / 16)])
mini_walk_1 = pygame.transform.scale(pygame.image.load('assets/images/mario/MiniWalk1.png'), [12 * (TILE_SIZE / 16), 15 * (TILE_SIZE / 16)])
mini_walk_2 = pygame.transform.scale(pygame.image.load('assets/images/mario/MiniWalk2.png'), [15 * (TILE_SIZE / 16), TILE_SIZE])
mini_walk_1b = pygame.transform.scale(pygame.image.load('assets/images/mario/MiniWalk1b.png'), [12 * (TILE_SIZE / 16), 15 * (TILE_SIZE / 16)])
mini_walk_2b = pygame.transform.scale(pygame.image.load('assets/images/mario/MiniWalk2b.png'), [15 * (TILE_SIZE / 16), TILE_SIZE])
mini_turn = pygame.transform.scale(pygame.image.load('assets/images/mario/MiniTurn.png'), [14 * (TILE_SIZE / 16), TILE_SIZE])
mini_jump = pygame.transform.scale(pygame.image.load('assets/images/mario/MiniJump.png'), [TILE_SIZE, TILE_SIZE])
mini_walk_3 = pygame.transform.scale(pygame.image.load('assets/images/mario/MiniWalk3.png'), [TILE_SIZE, TILE_SIZE])
mini_death = pygame.transform.scale(pygame.image.load('assets/images/mario/MiniDeath.png'), [TILE_SIZE, TILE_SIZE])
mario_transform = pygame.transform.scale(pygame.image.load('assets/images/mario/MarioTransform.png'), [14 * (TILE_SIZE / 16), 22 * (TILE_SIZE / 16)])
fire_walk_1 = pygame.transform.scale(pygame.image.load('assets/images/mario/FireWalk1.png'), [14 * (TILE_SIZE / 16), 27 * (TILE_SIZE / 16)])
fire_walk_2 = pygame.transform.scale(pygame.image.load('assets/images/mario/FireWalk2.png'), [TILE_SIZE, 27 * (TILE_SIZE / 16)])
fire_walk_3 = pygame.transform.scale(pygame.image.load('assets/images/mario/FireWalk3.png'), [TILE_SIZE, 27 * (TILE_SIZE / 16)])
fire_walk_4 = pygame.transform.scale(pygame.image.load('assets/images/mario/FireWalk4.png'), [TILE_SIZE, 27 * (TILE_SIZE / 16)])
fire_turn = pygame.transform.scale(pygame.image.load('assets/images/mario/FireTurn.png'), [TILE_SIZE, 28 * (TILE_SIZE / 16)])
fire_jump = pygame.transform.scale(pygame.image.load('assets/images/mario/FireJump.png'), [TILE_SIZE, 26 * (TILE_SIZE / 16)])
fire_crouch = pygame.transform.scale(pygame.image.load('assets/images/mario/FireCrouch.png'), [14 * (TILE_SIZE / 16), 18 * (TILE_SIZE / 16)])
fire_slide = pygame.transform.scale(pygame.image.load('assets/images/mario/FireSlide.png'), [TILE_SIZE, 26 * (TILE_SIZE / 16)])
fire_death = pygame.transform.scale(pygame.image.load('assets/images/mario/FireDeath.png'), [24 * (TILE_SIZE / 16), 24 * (TILE_SIZE / 16)])
fire_throw_2 = pygame.transform.scale(pygame.image.load('assets/images/mario/FireThrow2.png'), [14 * (TILE_SIZE / 16), 27 * (TILE_SIZE / 16)])
fire_throw_1 = pygame.transform.scale(pygame.image.load('assets/images/mario/FireThrow1.png'), [14 * (TILE_SIZE / 16), 27 * (TILE_SIZE / 16)])
wood_0 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Wood-0.png'), [TILE_SIZE, TILE_SIZE])
wood_1 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Wood-1.png'), [TILE_SIZE, TILE_SIZE])
wood_2 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Wood-2.png'), [TILE_SIZE, TILE_SIZE])
wood_3 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Wood-3.png'), [TILE_SIZE, TILE_SIZE])
wood_4 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Wood-4.png'), [TILE_SIZE, TILE_SIZE])
wood_5 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Wood-5.png'), [TILE_SIZE, TILE_SIZE])
gold = pygame.transform.scale(pygame.image.load('assets/images/tiles/Block-Gold.png'), [TILE_SIZE, TILE_SIZE])
hard_block = pygame.transform.scale(pygame.image.load('assets/images/tiles/Block-Wood.png'), [TILE_SIZE, TILE_SIZE])
blue_1 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-1.png'), [TILE_SIZE, TILE_SIZE])
blue_2 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-2.png'), [TILE_SIZE, TILE_SIZE])
blue_3 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-3.png'), [TILE_SIZE, TILE_SIZE])
blue_4 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-4.png'), [TILE_SIZE, TILE_SIZE])
blue_5 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-5.png'), [TILE_SIZE, TILE_SIZE])
blue_6 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-6.png'), [TILE_SIZE, TILE_SIZE])
blue_7 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-7.png'), [TILE_SIZE, TILE_SIZE])
blue_8 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-8.png'), [TILE_SIZE, TILE_SIZE])
blue_9 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Blue-9.png'), [TILE_SIZE, TILE_SIZE])
question_1 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Question1.png'), [TILE_SIZE, TILE_SIZE])
question_2 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Question2.png'), [TILE_SIZE, TILE_SIZE])
question_3 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Question3.png'), [TILE_SIZE, TILE_SIZE])
question_4 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Question4.png'), [TILE_SIZE, TILE_SIZE])
coin_1 = pygame.transform.scale(pygame.image.load('assets/images/tiles/coin1.png'), [TILE_SIZE, TILE_SIZE])
coin_2 = pygame.transform.scale(pygame.image.load('assets/images/tiles/coin2.png'), [TILE_SIZE, TILE_SIZE])
coin_3 = pygame.transform.scale(pygame.image.load('assets/images/tiles/coin3.png'), [TILE_SIZE, TILE_SIZE])
coin_4 = pygame.transform.scale(pygame.image.load('assets/images/tiles/coin4.png'), [TILE_SIZE, TILE_SIZE])
bush = pygame.transform.scale(pygame.image.load('assets/images/tiles/Bush.png'), [TILE_SIZE, TILE_SIZE])
cloud = pygame.transform.scale(pygame.image.load('assets/images/tiles/cloud.png'), [TILE_SIZE, TILE_SIZE])
orange_1 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-1.png'), [TILE_SIZE, TILE_SIZE])
orange_2 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-2.png'), [TILE_SIZE, TILE_SIZE])
orange_3 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-3.png'), [TILE_SIZE, TILE_SIZE])
orange_4 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-4.png'), [TILE_SIZE, TILE_SIZE])
orange_5 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-5.png'), [TILE_SIZE, TILE_SIZE])
orange_6 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-6.png'), [TILE_SIZE, TILE_SIZE])
orange_7 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-7.png'), [TILE_SIZE, TILE_SIZE])
orange_8 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-8.png'), [TILE_SIZE, TILE_SIZE])
orange_9 = pygame.transform.scale(pygame.image.load('assets/images/tiles/Orange-9.png'), [TILE_SIZE, TILE_SIZE])
pipe_1 = pygame.transform.scale(pygame.image.load('assets/images/tiles/pipe1.png'), [TILE_SIZE, TILE_SIZE])
pipe_2 = pygame.transform.scale(pygame.image.load('assets/images/tiles/pipe2.png'), [TILE_SIZE, TILE_SIZE])
pipe_3 = pygame.transform.scale(pygame.image.load('assets/images/tiles/pipe3.png'), [TILE_SIZE, TILE_SIZE])
pipe_4 = pygame.transform.scale(pygame.image.load('assets/images/tiles/pipe4.png'), [TILE_SIZE, TILE_SIZE])
black_zag = pygame.transform.scale(pygame.image.load('assets/images/tiles/Black-Zag.png'), [TILE_SIZE, TILE_SIZE])
black = pygame.transform.scale(pygame.image.load('assets/images/tiles/Black.png'), [TILE_SIZE, TILE_SIZE])
grass_8 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass8.png'), [TILE_SIZE, TILE_SIZE])
grass_6 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass6.png'), [TILE_SIZE, TILE_SIZE])
grass_10 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass10.png'), [TILE_SIZE, TILE_SIZE])
grass_1 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass1.png'), [TILE_SIZE, TILE_SIZE])
grass_2 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass2.png'), [TILE_SIZE, TILE_SIZE])
grass_4 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass4.png'), [TILE_SIZE, TILE_SIZE])
grass_5 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass5.png'), [TILE_SIZE, TILE_SIZE])
grass_7 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass7.png'), [TILE_SIZE, TILE_SIZE])
grass_9 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass9.png'), [TILE_SIZE, TILE_SIZE])
grass_12 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass12.png'), [TILE_SIZE, TILE_SIZE])
grass_13 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass13.png'), [TILE_SIZE, TILE_SIZE])
grass_11 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass11.png'), [TILE_SIZE, TILE_SIZE])
grass_15 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass15.png'), [TILE_SIZE, TILE_SIZE])
grass_14 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass14.png'), [TILE_SIZE, TILE_SIZE])
grass_16 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass16.png'), [TILE_SIZE, TILE_SIZE])
grass_18 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass18.png'), [TILE_SIZE, TILE_SIZE])
grass_17 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass17.png'), [TILE_SIZE, TILE_SIZE])
grass_3 = pygame.transform.scale(pygame.image.load('assets/images/tiles/grass3.png'), [TILE_SIZE, TILE_SIZE])
goomba = pygame.transform.scale(pygame.image.load('assets/images/enemies/Goomba.png'), [TILE_SIZE, TILE_SIZE])
goomba_2 = pygame.transform.scale(pygame.image.load('assets/images/enemies/Goomba2.png'), [TILE_SIZE, TILE_SIZE])
goomba_squish = pygame.transform.scale(pygame.image.load('assets/images/enemies/Goomba_Squish.png'), [TILE_SIZE, 9 * (TILE_SIZE / 16)])
koopa_troopa_g2 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaTroopaG2.png'), [TILE_SIZE, 26 * (TILE_SIZE / 16)])
koopa_troopa_g1 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaTroopaG1.png'), [TILE_SIZE, 27 * (TILE_SIZE / 16)])
koopa_troopa_2 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaTroopa2.png'), [TILE_SIZE, 26 * (TILE_SIZE / 16)])
koopa_troopa_1 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaTroopa1.png'), [TILE_SIZE, 27 * (TILE_SIZE / 16)])
piranha_plant_1 = pygame.transform.scale(pygame.image.load('assets/images/enemies/PiranhaPlant1.png'), [TILE_SIZE, 2 * TILE_SIZE])
piranha_plant_2 = pygame.transform.scale(pygame.image.load('assets/images/enemies/PiranhaPlant2.png'), [TILE_SIZE, 2 * TILE_SIZE])
venus_fire_trap_g1 = pygame.transform.scale(pygame.image.load('assets/images/enemies/Venus-Fire-Trap-G1.png'), [TILE_SIZE, 2 * TILE_SIZE])
venus_fire_trap_g2 = pygame.transform.scale(pygame.image.load('assets/images/enemies/Venus-Fire-Trap-G2.png'), [TILE_SIZE, 2 * TILE_SIZE])
venus_fire_trap_g3 = pygame.transform.scale(pygame.image.load('assets/images/enemies/Venus-Fire-Trap-G3.png'), [TILE_SIZE, 2 * TILE_SIZE])
venus_fire_trap_g4 = pygame.transform.scale(pygame.image.load('assets/images/enemies/Venus-Fire-Trap-G4.png'), [TILE_SIZE, 2 * TILE_SIZE])
flame = pygame.transform.scale(pygame.image.load('assets/images/enemies/Flame.png'), [TILE_SIZE / 2, TILE_SIZE / 2])
koopa_paratroopa_1 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaParatroopa1.png'), [TILE_SIZE, 28 * (TILE_SIZE / 16)])
koopa_paratroopa_2 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaParatroopa2.png'), [TILE_SIZE, 28 * (TILE_SIZE / 16)])
koopa_paratroopa_3 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaParatroopa3.png'), [TILE_SIZE, 28 * (TILE_SIZE / 16)])
koopa_paratroopa_4 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaParatroopa4.png'), [TILE_SIZE, 28 * (TILE_SIZE / 16)])
score_100 = pygame.transform.scale(pygame.image.load('assets/images/enemies/Score100.png'), [11 * (TILE_SIZE / 16), (TILE_SIZE / 2)])
life = pygame.transform.scale(pygame.image.load('assets/images/enemies/Life.png'), [TILE_SIZE, TILE_SIZE])
end_box = pygame.transform.scale(pygame.image.load('assets/images/enemies/EndBox.png'), [26 * (TILE_SIZE / 16), 26 * (TILE_SIZE / 16)])
end_box_flower = pygame.transform.scale(pygame.image.load('assets/images/enemies/EndBox---Flower.png'), [26 * (TILE_SIZE / 16), 26 * (TILE_SIZE / 16)])
end_box_mushroom = pygame.transform.scale(pygame.image.load('assets/images/enemies/EndBox---Mushroom.png'), [26 * (TILE_SIZE / 16), 26 * (TILE_SIZE / 16)])
end_box_star = pygame.transform.scale(pygame.image.load('assets/images/enemies/EndBox---Star.png'), [26 * (TILE_SIZE / 16), 26 * (TILE_SIZE / 16)])
koopa_shell_g1 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaShellG1.png'), [18 * (TILE_SIZE / 16), TILE_SIZE])
koopa_shell_g2 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaShellG2.png'), [18 * (TILE_SIZE / 16), TILE_SIZE])
koopa_shell_g3 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaShellG3.png'), [18 * (TILE_SIZE / 16), TILE_SIZE])
koopa_shell_g4 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaShellG4.png'), [TILE_SIZE, TILE_SIZE])
koopa_shell_r1 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaShellR1.png'), [18 * (TILE_SIZE / 16), TILE_SIZE])
koopa_shell_r2 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaShellR2.png'), [18 * (TILE_SIZE / 16), TILE_SIZE])
koopa_shell_r3 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaShellR3.png'), [18 * (TILE_SIZE / 16), TILE_SIZE])
koopa_shell_r4 = pygame.transform.scale(pygame.image.load('assets/images/enemies/KoopaShellR4.png'), [TILE_SIZE, TILE_SIZE])
fire_flower = pygame.transform.scale(pygame.image.load('assets/images/enemies/FireFlower.png'), [TILE_SIZE, TILE_SIZE])
star = pygame.transform.scale(pygame.image.load('assets/images/enemies/Star.png'), [TILE_SIZE, TILE_SIZE])
smoke_1 = pygame.transform.scale(pygame.image.load('assets/images/particles/Smoke1.png'), [7 * (TILE_SIZE / 16), 8 * (TILE_SIZE / 16)])
smoke_2 = pygame.transform.scale(pygame.image.load('assets/images/particles/Smoke2.png'), [5 * (TILE_SIZE / 16), 5 * (TILE_SIZE / 16)])
background_1_1 = pygame.transform.scale(pygame.image.load('assets/images/backgrounds/Background-1-1.png'), [16 * TILE_SIZE, 2 * HEIGHT])
background_1_2 = pygame.transform.scale(pygame.image.load('assets/images/backgrounds/Background-1-2.png'), [16 * TILE_SIZE, 2 * HEIGHT])
mario_imgs = {
    1: mario_walk_1,
    2: mario_walk_2,
    3: mario_walk_3,
    4: mario_walk_4,
    11: mini_walk_1,
    12: mini_walk_2,
    13: mini_walk_1b,
    14: mini_walk_2b,
    20: fire_walk_1,
    21: fire_walk_2,
    22: fire_walk_3,
    23: fire_walk_4
}
mario_imgs_2 = {
    'MarioWalk1': mario_walk_1,
    'MarioWalk2': mario_walk_2,
    'MarioWalk3': mario_walk_3,
    'MarioWalk4': mario_walk_4,
    'MarioTurn': mario_turn,
    'MarioJump': mario_jump,
    'MarioCrouch': mario_crouch,
    'MarioSlide': mario_slide,
    'MarioDeath': mario_death,
    'BIG': BIG,
    'MiniWalk1': mini_walk_1,
    'MiniWalk2': mini_walk_2,
    'MiniWalk1b': mini_walk_1b,
    'MiniWalk2b': mini_walk_2b,
    'MiniTurn': mini_turn,
    'MiniJump': mini_jump,
    'MiniWalk3': mini_walk_3,
    'MiniDeath': mini_death,
    'MarioTransform': mario_transform,
    'FireWalk1': fire_walk_1,
    'FireWalk2': fire_walk_2,
    'FireWalk3': fire_walk_3,
    'FireWalk4': fire_walk_4,
    'FireTurn': fire_turn,
    'FireJump': fire_jump,
    'FireCrouch': fire_crouch,
    'FireSlide': fire_slide,
    'FireDeath': fire_death,
    'FireThrow2': fire_throw_2,
    'FireThrow1': fire_throw_1
}
tile_imgs = {
    1: BIG,
    2: pygame.Surface([1, 1]),
    3: wood_0,
    4: wood_1,
    5: wood_2,
    6: wood_3,
    7: wood_4,
    8: wood_5,
    9: gold,
    10: hard_block,
    11: blue_1,
    12: blue_2,
    13: blue_3,
    14: blue_4,
    15: blue_5,
    16: blue_6,
    17: blue_7,
    18: blue_8,
    19: blue_9,
    20: question_1,
    21: question_2,
    22: question_3,
    23: question_4,
    24: coin_1,
    25: coin_2,
    26: coin_3,
    27: coin_4,
    28: mario_walk_1,
    29: goomba,
    30: life,
    31: bush,
    32: cloud,
    33: orange_1,
    34: orange_2,
    35: orange_3,
    36: orange_4,
    37: orange_5,
    38: orange_6,
    39: orange_7,
    40: orange_8,
    41: orange_9,
    42: pipe_1,
    43: pipe_2,
    44: pipe_3,
    45: pipe_4,
    46: star,
    47: end_box,
    48: black_zag,
    49: black,
    50: grass_8,
    51: grass_6,
    52: grass_10,
    53: grass_1,
    54: grass_2,
    55: grass_4,
    56: grass_5,
    57: grass_7,
    58: grass_9,
    59: grass_12,
    60: grass_13,
    61: grass_11,
    62: grass_15,
    63: grass_14,
    64: grass_16,
    65: grass_18,
    66: grass_17,
    67: grass_3,
    68: piranha_plant_1,
    69: koopa_troopa_g2,
    70: fire_flower
}
enemy_imgs = {
    1: BIG,
    2: goomba,
    3: goomba_2,
    4: goomba_squish,
    5: koopa_troopa_g2,
    6: koopa_troopa_g1,
    7: koopa_troopa_2,
    8: koopa_troopa_1,
    9: piranha_plant_1,
    10: piranha_plant_2,
    11: venus_fire_trap_g1,
    12: venus_fire_trap_g2,
    13: venus_fire_trap_g3,
    14: venus_fire_trap_g4,
    15: flame,
    16: koopa_paratroopa_1,
    17: koopa_paratroopa_2,
    18: koopa_paratroopa_3,
    19: koopa_paratroopa_4,
    20: score_100,
    21: life,
    22: end_box,
    23: end_box_flower,
    24: end_box_mushroom,
    25: end_box_star,
    26: koopa_shell_g1,
    27: koopa_shell_g2,
    28: koopa_shell_g3,
    29: koopa_shell_g4,
    30: koopa_shell_r1,
    31: koopa_shell_r2,
    32: koopa_shell_r3,
    33: koopa_shell_r4,
}
enemy_imgs_2 = {
    'BIG': BIG,
    'Goomba Squish': goomba_squish,
    'Flame': flame,
    'Life': life,
    'Star': star,
    'EndBox': end_box,
    'FireFlower': fire_flower
}
particle_imgs = {
    1: smoke_1,
    2: smoke_2,
    3: coin_1,
    4: coin_2,
    5: coin_3,
    6: coin_4,
    7: BIG,
    8: score_100
}
background_imgs = {
    1: background_1_1,
    2: background_1_2
}

# Sounds
Music_L1 = pygame.mixer.Sound('assets/sounds/Music_L1.mp3')
jump_sound = pygame.mixer.Sound('assets/sounds/Jump.wav')
skid_sound = pygame.mixer.Sound('assets/sounds/Skid.wav')
block_hit_sound = pygame.mixer.Sound('assets/sounds/block_hit.mp3')
item_sprout_sound = pygame.mixer.Sound('assets/sounds/ItemSprout.wav')
item_sprout_sound = pygame.mixer.Sound('assets/sounds/ItemSprout.wav')
_1up_sound = pygame.mixer.Sound('assets/sounds/1up.wav')
bounce_off_enemy_sound = pygame.mixer.Sound('assets/sounds/Bounce_Off_Enemy.wav')
coin_sound = pygame.mixer.Sound('assets/sounds/Coin.wav')
stomped_sound = pygame.mixer.Sound('assets/sounds/Stomped.wav')
fireball_sound = pygame.mixer.Sound('assets/sounds/Fireball.wav')
flagpole_sound = pygame.mixer.Sound('assets/sounds/Flagpole.wav')
game_over_sound = pygame.mixer.Sound('assets/sounds/GameOver.wav')
goal_sound = pygame.mixer.Sound('assets/sounds/Goal.wav')
goal_card_1_sound = pygame.mixer.Sound('assets/sounds/GoalCard1.wav')
kick_1_sound = pygame.mixer.Sound('assets/sounds/Kick1.wav')
kick_shell_sound = pygame.mixer.Sound('assets/sounds/KickShell.wav')
level_select_sound = pygame.mixer.Sound('assets/sounds/Level_Select.wav')
lose_life_sound = pygame.mixer.Sound('assets/sounds/Lose_Life.wav')
power_up_sound = pygame.mixer.Sound('assets/sounds/Power_Up.wav')
power_down_sound = pygame.mixer.Sound('assets/sounds/Power_Down.wav')
slide_attack_sound = pygame.mixer.Sound('assets/sounds/Slide_Attack.wav')
swim_sound = pygame.mixer.Sound('assets/sounds/Swim.wav')
throw_sound = pygame.mixer.Sound('assets/sounds/Throw.wav')
warp_sound = pygame.mixer.Sound('assets/sounds/Warp.wav')
lets_go_sound = pygame.mixer.Sound("assets/sounds/Let's_Go.wav")
mammamia_sound = pygame.mixer.Sound('assets/sounds/Mammamia.wav')
just_what_I_needed_sound = pygame.mixer.Sound('assets/sounds/Just_What_I_Needed.wav')
oh_no_sound = pygame.mixer.Sound('assets/sounds/Oh_No.wav')
course_clear_sound = pygame.mixer.Sound('assets/sounds/Course_Clear.mp3')
star_power_sound = pygame.mixer.Sound('assets/sounds/Star_Power.wav')

def write_tile_grid():
    string = level_store.level_store[LEVEL_NUM - 1]
    for level in level_store.level_store:
        if level != level_store.level_store[LEVEL_NUM - 1]:
            string = f'{string}\n{level}'

    with open('tile_grid.txt', 'w') as f:
        f.write(string)

def read_tile_grid():
    with open('tile_grid.txt', 'r') as f:
        return f.readlines()

def colliding(object_1, object_2):
    pos_1 = coords.pygame([object_1.x, object_1.y], [WIDTH, HEIGHT])
    pos_2 = coords.pygame([object_2.x, object_2.y], [WIDTH, HEIGHT])
    width_1 = object_1.width
    width_2 = object_2.width
    height_1 = object_1.height
    height_2 = object_2.height
    rect_1 = pygame.Rect(pos_1[0] - width_1, pos_1[1] - height_1, width_1 * 2, height_1 * 2)
    rect_2 = pygame.Rect(pos_2[0] - width_2, pos_2[1] - height_2, width_2 * 2, height_2 * 2)
    return rect_1.colliderect(rect_2)                                                                                                                   

def distance(object_1, object_2):
    x_1 = object_1.x
    x_2 = object_2.x
    y_1 = object_1.y
    y_2 = object_2.y
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)

class Mario:
    def __init__(self):
        self.real_x = 0
        self.real_y = 0
        self.costume = mini_walk_1
        self.direction = 90
        self.tile_grid_x = 0
        self.tile_grid_y = 0
        self.tile_index = 0
        self.tile = 1
        self.solid = None
        self.fix_dx = 0
        self.fix_dy = 0
        self.mod_x = 0
        self.mod_y = 0
        self.m = 0
        self.c = 0
        self.offset_y = 0
        self.orig_y = 0
        self.player_frame = 0
        self.temp = 0
        self.player_action = ''
        self.tile_shape = ''
        self.spawn_index = 0
        self.bop_y = None
        self.color = 0
        self.ghost = 0
        self.throw = 0
        LEVEL_start_game_loop_respawn()

    def reset_player(self):
        global minus_TINY, CAMERA_X, CAMERA_Y, MARIO, FIREBALLS, STAR_POWER

        minus_TINY = -0.000001
        if self.spawn_index > 0:
            self.x = math.floor((self.spawn_index - 1) / GRID_HEIGHT)
            self.y = ((self.spawn_index - 1) % GRID_HEIGHT)
        else:
            self.x = 3
            self.y = 3
        self.x = ((self.x * TILE_SIZE) + (TILE_SIZE / 2)) * (TILE_SIZE / 32)
        self.y = (self.y * TILE_SIZE) * (TILE_SIZE / 32)
        self.width = 8 * (TILE_SIZE / 32)
        self.height = 24 * (TILE_SIZE / 32)
        CAMERA_X = self.x
        CAMERA_Y = self.y
        self.jumping = 99
        self.falling = 99
        self.speed_x = 0
        self.speed_y = 0
        MARIO = 'Mini'
        self.invulnerable = 0
        FIREBALLS = 0
        STAR_POWER = 0
        self.direction = 90
        self.move_camera()

    def get_tile_at(self, x, y):
        self.tile_grid_x = math.floor(x / TILE_SIZE)
        self.tile_grid_y = math.floor(y / TILE_SIZE)
        self.tile_index = 1 + self.tile_grid_y + (self.tile_grid_x * GRID_HEIGHT)
        if self.tile_grid_y < 0:
            self.tile = -1
        else:
            self.tile = TILE_GRID[self.tile_index - 1]
        self.tile_shape = TILE_SHAPE[self.tile - 1]

    def fix_collision_in_direction(self, dx, dy):
        self.fix_dx = dx
        self.fix_dy = dy
        self.solid = -1

        for _ in range(2):
            self.fix_collision_at_point(self.x - self.width, self.y - self.height, 'feet')
            self.fix_collision_at_point(self.x + self.width + minus_TINY, self.y - self.height, 'feet')

            self.fix_collision_at_point(self.x - self.width, self.y)
            self.fix_collision_at_point(self.x + self.width + minus_TINY, self.y)

            if not (self.player_action == 'crouch' or MARIO == 'Mini'):
                self.fix_collision_at_point(self.x - self.width, self.y + self.height)
                self.fix_collision_at_point(self.x + self.width + minus_TINY, self.y + self.height)

            if self.solid < 1:
                return

    def fix_collision_at_point(self, x, y, part=''):
        self.get_tile_at(x, y)

        if self.tile_shape == '':
            return

        self.mod_x = x % TILE_SIZE
        self.mod_y = y % TILE_SIZE
        self.temp = TILE_SHAPE[self.tile - 1][0]

        if self.temp == '\\' or self.temp == '/':
            self.m = 1 / int(TILE_SHAPE[self.tile - 1][1])
            self.c = int(TILE_SHAPE[self.tile - 1][2]) * TILE_SIZE * self.m
            if self.temp == '\\':
                self.m = -self.m
                self.c = TILE_SIZE - self.c
            
            self.offset_y = self.mod_y - ((self.mod_x * self.m) + self.c)
            if not self.offset_y < 0:
                return
            
            if self.fix_dy < 0:
                self.y += -self.offset_y
                self.solid = 10
                return
            
            if self.fix_dy == 0 and ((self.fix_dx > 0) == (self.m > 0)):
                self.x += self.offset_y / self.m
                self.solid = 10
                return

        if self.tile_shape == '=':
            if (not part == 'feet') or (self.mod_y - self.fix_dy < TILE_SIZE):
                return
            
            if controls.down > 0:
                return

        self.solid = 10

        if self.fix_dy < 0:
            self.y += TILE_SIZE - self.mod_y

        if self.fix_dx < 0:
            self.x += TILE_SIZE - self.mod_x

        if self.fix_dy > 0:
            self.y += minus_TINY - self.mod_y

        if self.fix_dx > 0:
            self.x += minus_TINY - self.mod_x

    def make_skid_smoke(self):
        self.player_frame += 1
        if self.player_frame % 3 < 1:
            PARTICLES.append('smoke')
            PARTICLES.append(self.x)
            PARTICLES.append(self.y - (20 * (TILE_SIZE / 32)))
            skid_sound.play()

    def handle_keys_left_right(self):
        if self.player_action == 'crouch':
            if abs(self.speed_x) > 0.4:
                self.speed_x += -0.4 * (abs(self.speed_x) / self.speed_x)
                self.make_skid_smoke()
            else:
                self.speed_x = 0
                self.player_frame = -1
        else:
            global KEY_WALK

            self.player_action = 'walk'
            KEY_WALK = controls.x_axis

            if KEY_WALK == 0:
                if self.falling < 2:
                    if self.speed_x > 0.4:
                        self.speed_x -= 0.4
                    elif self.speed_x < -0.4:
                        self.speed_x += 0.4
                    else:
                        self.speed_x = 0
                        self.player_frame = 0
            else:
                self.direction = 90 * KEY_WALK
                if KEY_WALK * self.speed_x < 10 * (TILE_SIZE / 32):
                    if KEY_WALK * self.speed_x < 0:
                        self.speed_x += KEY_WALK * 0.8
                        if self.falling < 2:
                            self.player_action = 'turn'
                            self.make_skid_smoke()
                    else:
                        self.speed_x += KEY_WALK * 0.4

            self.temp = abs(self.speed_x) / 19
            if self.temp < 0.2:
                self.temp = 0.2
            self.player_frame += self.temp

    def handle_keys_jump_crouch(self):
        self.speed_y -= 2
        if self.speed_y < -22 * (TILE_SIZE / 32):
            self.speed_y = -22 * (TILE_SIZE / 32)

        if controls.down > 0 and not MARIO == 'Mini':
            if self.falling < 2:
                self.player_action = 'crouch'
            self.jumping = 0
        else:
            if self.player_action == 'crouch':
                self.handle_get_up()
            else:
                if controls.up > 0:
                    if self.falling < 2 or self.jumping > 0:
                        self.jumping += 1
                        if self.jumping < 11:
                            self.speed_y = 13 * (TILE_SIZE / 32)
                            if self.jumping == 1:
                                jump_sound.play()
                                if MARIO == 'Mini':
                                    self.jumping = 3
                else:
                    self.jumping = 0

    def handle_keys_fire(self):
        global FIREBALLS

        if controls.button_B == 1:
            if MARIO == 'Fire':
                if FIREBALLS < 2:
                    FIREBALLS += 1
                    self.throw = 2
                    fireball_sound.play()
                    mario_fireball()

    def handle_get_up(self):
        self.player_action = ''
        self.orig_y = self.y
        self.fix_collision_in_direction(0, 1)
        if self.solid > 0:
            self.player_action = 'crouch'
            self.y = self.orig_y
            self.speed_x += self.direction / -200

    def handle_god_mode(self):
        self.speed_x += 6 * controls.x_axis * (TILE_SIZE / 32)
        self.speed_y += 6 * controls.y_axis * (TILE_SIZE / 32)
        self.speed_x = 0.7 * self.speed_x
        self.speed_y = 0.7 * self.speed_y

        self.x += self.speed_x
        self.y += self.speed_y

    def move_sprite_x(self):
        self.orig_y = self.y
        self.x += self.speed_x
        self.fix_collision_in_direction(0, -1)
        if self.y > self.orig_y + abs(self.speed_x) + (TILE_SIZE / 8):
            self.y = self.orig_y
            self.fix_collision_in_direction(self.speed_x, 0)
            if self.solid > 0:
                self.speed_x = 0
        elif self.y > self.orig_y:
            self.speed_x = self.speed_x * 0.85

    def move_sprite_y(self):
        self.y += self.speed_y
        self.falling += 1
        self.fix_collision_in_direction(0, self.speed_y)
        if self.solid > 0:
            if self.speed_y < 0:
                self.falling = 0
            else:
                self.jumping = 99
                self.bump_head()
            self.speed_y = 0
        
    def bump_head(self):
        global BUMP_INDEX

        self.get_tile_at(self.x, self.y + self.height + (TILE_SIZE / 4))

        if self.tile == 20:
            BUMP_INDEX = self.tile_index
        
    def paint_sprite(self):
        self.costume = BIG

        if STAR_POWER > 0:
            self.color += 10
        else:
            self.color = 0

        self.real_x = self.x - CAMERA_X
        self.real_y = self.y - CAMERA_Y

        if self.throw > 0:
            self.costume = mario_imgs_2[MARIO + 'Throw' + str(math.ceil(self.throw))]
            self.throw += -0.25
            return
        
        if self.player_action == 'crouch':
            if MARIO == 'Mini':
                self.costume = mini_walk_1
                return
            self.costume = mario_imgs_2[MARIO + 'Crouch']
            return
        
        if self.player_action == 'lose life':
            self.costume = mario_imgs_2[MARIO + 'Death']
            return

        if self.falling > 1:
            if self.speed_y > 0:
                self.costume = mario_imgs_2[MARIO + 'Jump']
            else:
                self.costume = mario_imgs_2[MARIO + 'Walk3']
            return
        
        if self.player_action == 'turn':
            self.costume = mario_imgs_2[MARIO + 'Turn']
            return
        
        self.costume = mario_imgs_2[MARIO + 'Walk1']
        temp = list(mario_imgs_2.items()) 
        costume_number = [idx for idx, key in enumerate(temp) if key[0] == MARIO + 'Walk1'][0] + 1
        self.costume = mario_imgs[costume_number + (math.floor(self.player_frame) % 4)]

    def check_around_player_at_xy(self, x, y):
        global COINS

        self.get_tile_at(x, y)
        if self.tile == 24:
            TILE_GRID[self.tile_index - 1] = 2
            COINS += 1
            coin_sound.play()

    def check_around_player(self):
        if self.y < 0:
            mario_lose_life()
        self.check_around_player_at_xy(self.x, self.y - (TILE_SIZE / 4))
        self.check_around_player_at_xy(self.x, self.y + (TILE_SIZE / 4))
        
    def limit_camera(self, edge_x, edge_y):
        global CAMERA_X, CAMERA_Y

        if CAMERA_X < edge_x:
            CAMERA_X = edge_x

        if CAMERA_Y < edge_y:
            CAMERA_Y = edge_y

        if CAMERA_X > (TILE_SIZE * GRID_WIDTH) - edge_x:
            CAMERA_X = (TILE_SIZE * GRID_WIDTH) - edge_x

        if CAMERA_Y > (TILE_SIZE * GRID_HEIGHT) - edge_y:
            CAMERA_Y = (TILE_SIZE * GRID_HEIGHT) - edge_y

    def move_camera(self):
        global CAMERA_X, CAMERA_Y

        CAMERA_X = self.x
        CAMERA_Y += (self.y - CAMERA_Y) / 4

        if EDITOR > 0:
            self.limit_camera(CENTER_X, CENTER_Y)
        else:
            self.limit_camera(CENTER_X + TILE_SIZE, CENTER_Y)

    def LEVEL_start_game_loop(self):
        global GAME_LOOP_RUNNING, COINS
        COINS = 0
        GAME_LOOP_RUNNING = True

    def LEVEL_continue_game_loop(self):
        global GAME_LOOP_RUNNING
        GAME_LOOP_RUNNING = True

    def LEVEL_start_game_loop_respawn(self):
        global GAME_LOOP_RUNNING, COINS
        self.reset_player()
        COINS = 0
        GAME_LOOP_RUNNING = True

    def LEVEL_done_loading(self):
        try:
            self.spawn_index = TILE_GRID.index(28) + 1
            if EDITOR < 1:
                TILE_GRID[self.spawn_index - 1] = 2
        except:
            self.spawn_index = 0

    def LEVEL_stop(self):
        global GAME_LOOP_RUNNING
        GAME_LOOP_RUNNING = False

    def move_player(self):
        global BUMP_INDEX

        BUMP_INDEX = None

        if EDITOR > 0:
            self.handle_god_mode()
        else:
            if self.falling > 2 and self.speed_y < -1:
                self.bop_y = self.y
            else:
                self.bop_y = None

            self.handle_keys_left_right()
            self.handle_keys_jump_crouch()
            self.move_sprite_x()
            self.move_sprite_y()
            self.check_around_player()
            self.handle_keys_fire()
        self.paint_sprite()

    def move_player_after_enemy(self):
        global BOUNCE_PLAYER

        if BOUNCE_PLAYER > 0:
            BOUNCE_PLAYER += -1
            self.speed_y = 13
            self.falling = 2
            self.jumping = 1

        self.move_camera()
        self.paint_sprite()

    def position_tiles(self):
        if self.invulnerable > 0:
            self.invulnerable += -1

        if self.invulnerable % 2 < 1:
            self.ghost = 0
        else:
            self.ghost = 99

    def mario_lose_life(self):
        global GAME_LOOP_RUNNING
        
        lose_life_sound.play()
        self.player_action = 'lose life'
        GAME_LOOP_RUNNING = False

        self.paint_sprite()
        draw()
        pygame.display.flip()

        pygame.time.delay(833) # 25 frames

        self.speed_y = 17
        while not (self.y - CAMERA_Y < -(CENTER_Y + (20 * (TILE_SIZE / 32)))):
            clock.tick(30)
            self.speed_y += -1
            self.y += self.speed_y
            self.paint_sprite()
            draw()
            pygame.display.flip()

        pygame.time.delay(1000) # 30 frames

        GAME_LOOP_RUNNING = True
        level_store.LEVEL_load()
        LEVEL_start_game_loop_respawn()

    def mario_hurt(self):
        global GAME_LOOP_RUNNING, MARIO

        if self.invulnerable > 0:
            return

        if MARIO == 'Mini':
            mario_lose_life()
            return
        
        GAME_LOOP_RUNNING = False
        power_down_sound.play()
        draw()
        pygame.display.flip()
        self.invulnerable = 70
        self.throw = 0

        if MARIO == 'Fire':
            MARIO = 'Mario'
            self.paint_sprite()
            for _ in range(30):
                clock.tick(FPS)
                self.position_tiles()
                draw()
                pygame.display.flip()
        else:
            self.loop_transformation()
            MARIO = 'Mini'
            self.loop_transformation()

        LEVEL_continue_game_loop()

    def mario_level_complete(self):
        global GAME_LOOP_RUNNING, LEVEL_NUM
        GAME_LOOP_RUNNING = False

        self.speed_x = 0

        while not self.falling < 1:
            clock.tick(FPS)
            self.handle_keys_jump_crouch()
            self.move_sprite_x()
            self.move_sprite_y()
            self.paint_sprite()
            draw()
            pygame.display.flip()

        self.direction = 90
        while not self.real_x > WIDTH + (20 * (TILE_SIZE / 32)):
            self.x += 2.5 * (TILE_SIZE / 32)
            self.player_frame += 0.6
            self.paint_sprite()
            position_tiles()
            draw()
            pygame.display.flip()
        
        pygame.time.delay(1000) # 30 frames

        GAME_LOOP_RUNNING = True
        LEVEL_NUM += 1
        level_store.LEVEL_load()
        LEVEL_start_game_loop_respawn()

    def collect_1up(self):
        global MARIO, GAME_LOOP_RUNNING

        if not MARIO == 'Mini':
            return
        
        GAME_LOOP_RUNNING = False
        power_up_sound.play()
        draw()
        pygame.display.flip()

        self.loop_transformation()
        MARIO = 'Mario'
        self.loop_transformation()

        LEVEL_continue_game_loop()

    def loop_transformation(self):
        for _ in range(3):
            clock.tick(FPS)
            
            self.costume = mario_transform
            draw()
            pygame.display.flip()
            pygame.time.delay(67) # 2 frames

            self.costume = mario_imgs_2[MARIO + 'Walk1']
            pygame.time.delay(100) # 3 frames
            draw()
            pygame.display.flip()

    def draw(self):
        image = self.costume

        # Ghost Effect
        image.set_alpha(255 - round(2.55 * self.ghost))

        # Color Effect
        if self.color > 0:
            self.color %= 200
            modified_surface = pygame.Surface(image.get_size())
            modified_surface.set_colorkey((0, 0, 0))  # Set black color as transparent
            for x in range(image.get_width()):
                for y in range(image.get_height()):
                    # Get the color of the pixel
                    color = image.get_at((x, y))

                    # Convert color to RGB tuple
                    r, g, b, a = color

                    # Convert RGB to HSV
                    hsv = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

                    # Update the hue value
                    hsv_modified = (self.color, hsv[1], hsv[2])

                    # Convert HSV to RGB
                    rgb = colorsys.hsv_to_rgb(hsv_modified[0] / 360, hsv_modified[1], hsv_modified[2])

                    # Scale the RGB values to 0-255 range
                    r = int(rgb[0] * 255)
                    g = int(rgb[1] * 255)
                    b = int(rgb[2] * 255)

                    # Create a new color with the modified RGB values
                    modified_color = (r, g, b, a)

                    # Set the modified color on the modified surface
                    modified_surface.set_at((x, y), modified_color)

            image = modified_surface

        offset_x = 0
        offset_y = TILE_SIZE / 16

        if self.player_action == 'crouch':
            offset_y += (-TILE_SIZE / 2) - (TILE_SIZE / 16)
        if image == mario_transform:
            offset_y += (-TILE_SIZE * (3 / 8)) - (TILE_SIZE / 16)
        elif MARIO == 'Mini':
            offset_y += (-TILE_SIZE * (3 / 4))

        pos = coords.pygame([self.real_x + offset_x, self.real_y + offset_y], [WIDTH, HEIGHT])

        if self.direction == 90:
            screen.blit(image, [pos[0] - (14 * (TILE_SIZE / 32)), pos[1] - (27 * (TILE_SIZE / 32))])
        else:
            screen.blit(pygame.transform.flip(image, True, False), [pos[0] - (14 * (TILE_SIZE / 32)), pos[1] - (27 * (TILE_SIZE / 32))])

class Tile:
    def __init__(self, x, y, tile_idx):
        self.tile_x = x
        self.tile_y = y
        self.tile = tile_imgs[3]
        self.tile_index = tile_idx
        self.real_x = x
        self.real_y = y
        self.bumped = 0

    def loop_tile_x(self, tile_skip):
        self.tile_x += tile_skip * TILE_SIZE
        self.tile_index += tile_skip * GRID_HEIGHT

    def loop_tile_y(self, tile_skip):
        self.tile_y += tile_skip * TILE_SIZE
        self.tile_index += tile_skip

    def editor_brush(self):
        if EDITOR < 1 or MOUSE_DOWN():
            return

        ghost = 128
        self.tile_x = (TILE_SIZE * editor.tile_grid_x) + (TILE_SIZE / 2)
        self.tile_y = (TILE_SIZE * editor.tile_grid_y) + (TILE_SIZE / 2)
        self.tile = editor.chosen_brush
        image = tile_imgs[self.tile]
        image.set_alpha(ghost)
        self.real_x = self.tile_x - CAMERA_X
        self.real_y = self.tile_y - CAMERA_Y
        self.draw(image)
        image.set_alpha(255)

    def LEVEL_done_loading(self):
        if self.tile_index != None:
            self.tile_index = 1 + math.floor(self.tile_y / TILE_SIZE)
            self.tile_index += GRID_HEIGHT  * math.floor(self.tile_x / 32)

    def position_tiles(self):
        global COINS

        if self.tile_index == None:
            self.editor_brush()
            return
        else:
            if abs(self.tile_x - CAMERA_X) > CLONE_COUNT_X * (TILE_SIZE / 2):
                if self.tile_x < CAMERA_X:
                    self.loop_tile_x(CLONE_COUNT_X)
                else:
                    self.loop_tile_x(-CLONE_COUNT_X)
            if abs(self.tile_y - CAMERA_Y) > CLONE_COUNT_Y * (TILE_SIZE / 2):
                if self.tile_y < CAMERA_Y:
                    self.loop_tile_y(CLONE_COUNT_Y)
                else:
                    self.loop_tile_y(-CLONE_COUNT_Y)
            try:
                self.tile = TILE_GRID[self.tile_index - 1]
            except:
                self.tile = 2
        
        last_tile = self.tile
        self.tile = tile_imgs[1]
        self.real_x = self.tile_x - CAMERA_X
        self.real_y = self.tile_y - CAMERA_Y
        self.tile = last_tile
        if self.tile < 2:
            self.tile = 2
        elif self.tile == 20 or self.tile == 24:
            self.tile += math.floor(timer * 8) % 4

            if EDITOR < 1:
                if BUMP_INDEX == self.tile_index:
                    TILE_GRID[self.tile_index - 1] = 9
                    self.bumped = 180
                    if self.tile_index not in OBJECT_IDX:
                        PARTICLES.append('coin')
                        PARTICLES.append(self.tile_x)
                        PARTICLES.append(self.tile_y + TILE_SIZE)
                        COINS += 1

        if self.bumped > 0:
            self.bumped += -30
            self.real_y += (24 * (TILE_SIZE / 32)) * sin(self.bumped)

    def draw(self, image=0):
        if self.tile == 2:
            return

        if self.tile == 28:
            pos = coords.pygame([self.real_x, self.real_y - (10 * (TILE_SIZE / 32))], [WIDTH, HEIGHT])
        elif self.tile == 68:
            pos = coords.pygame([self.real_x + (TILE_SIZE / 2), self.real_y + TILE_SIZE], [WIDTH, HEIGHT])
        elif self.tile == 69:
            pos = coords.pygame([self.real_x, self.real_y + (TILE_SIZE / 8)], [WIDTH, HEIGHT])
        else:
            pos = coords.pygame([self.real_x, self.real_y], [WIDTH, HEIGHT])

        if image == 0:
            screen.blit(tile_imgs[self.tile], [pos[0] - (TILE_SIZE / 2), pos[1] - (TILE_SIZE / 2)])
        else:
            if self.tile == 69:
                width, height = image.get_size()
                screen.blit(image, [pos[0] - (width / 2), pos[1] - (height / 2)])
            else:
                screen.blit(image, [pos[0] - (TILE_SIZE / 2), pos[1] - (TILE_SIZE / 2)])

class Enemy:
    def __init__(self, dummy=False, info=False):
        if dummy:
            self.type = None
            self.speed_x = 0
            self.speed_y = 0
            self.visible = 0
            self.frame = None
            self.hide = True
        else:
            self.start_as_clone(info)

        self.real_x = 0
        self.real_y = 0
        self.tile_grid_x = 0
        self.tile_grid_y = 0
        self.tile_index = 0
        self.tile = 1
        self.solid = None
        self.falling = 0
        self.fix_dx = 0
        self.fix_dy = 0
        self.mod_x = 0
        self.mod_y = 0
        self.tile_shape = ''
        self.object_item_num = 0

        LAYERS.remove('enemy')
        LAYERS.insert(LAYERS_BACKGROUND + 2, 'enemy')

    def delete_clone(self):
        global FIREBALLS

        if self.type == 'Fireball':
            FIREBALLS += -1

        enemies.remove(self)

    def start_as_clone(self, info):
        self.type = info[0]
        self.costume = info[1]
        self.root_costume = info[1]
        self.width = info[2]
        self.height = info[3]
        self.x = info[4]
        self.y = info[5]
        self.frame = info[6]
        self.spawn_index = info[7]
        self.direction = mario.direction
        self.hide = True
        self.speed_x = 0
        self.speed_y = 0
        if EDITOR > 0 or self.frame == None:
            self.visible = 1
        else:
            self.visible = 0
        self.paint_sprite()

        if self.type == 'Piranha':
            self.x += TILE_SIZE / 2
            if EDITOR < 1:
                self.y += -2 * TILE_SIZE
                LAYERS.remove('enemy')
                LAYERS.insert(LAYERS_BACKGROUND, 'enemy')

        if self.type == 'Fireball':
            self.root_costume = 'Flame'
            self.costume = self.root_costume
            self.width = 8
            self.height = 8
            self.x = mario.x
            self.y = mario.y + (10 * (TILE_SIZE / 32))
            if mario.direction > 0:
                self.speed_x = 10
            else:
                self.speed_x = -10
            self.speed_y = -6
            self.paint_sprite()
            self.visible = 2
            self.frame = 0

    def set_type(self, type_, costume, width, height, frame=None):
        x = math.floor((self.spawn_index - 1) / GRID_HEIGHT)
        y = (self.spawn_index - 1) % GRID_HEIGHT
        x = (x * TILE_SIZE) + (TILE_SIZE / 2)
        y = (y * TILE_SIZE) + height

        enemies.append(Enemy(info=[type_, costume, width * (TILE_SIZE / 32), height * (TILE_SIZE / 32), x, y, frame, self.spawn_index]))

    def spawn_type(self, tile_type):
        if not self.type == None:
            return

        if tile_type == 29:
            self.set_type('Goomba', 2, 14, 14)

        if tile_type == 30:
            self.set_type('Life', 'Life', 16, 16, -1)

        if tile_type == 46:
            self.set_type('Life', 'Star', 16, 16, -1)

        if tile_type == 70:
            self.set_type('Life', 'FireFlower', 16, 16, -1)

        if tile_type == 47:
            self.set_type('EndBox', 'EndBox', 16, 16)

        if tile_type == 68:
            self.set_type('Piranha', 9, 16, 32)

        if tile_type == 69:
            self.set_type('Koopa', 5, 16, 24)

    def spawn_loop(self):
        self.object_item_num = 1

        for _ in range(len(OBJECT_IDX)):
            self.spawn_index = OBJECT_IDX[self.object_item_num - 1]
            self.spawn_type(OBJECT_TYPE[self.object_item_num - 1])
            self.object_item_num += 1

        self.object_item_num = None

    def switch_costume(self, costume):
        if isinstance(costume, int):
            if costume == 0:
                return
            self.real_costume = enemy_imgs[costume]
        else:
            self.real_costume = enemy_imgs_2[costume]

    def get_tile_at(self, x, y):
        self.tile_grid_x = math.floor(x / TILE_SIZE)
        self.tile_grid_y = math.floor(y / TILE_SIZE)
        self.tile_index = 1 + self.tile_grid_y + (self.tile_grid_x * GRID_HEIGHT)
        if self.tile_grid_y < 0:
            self.tile = -1
        else:
            self.tile = TILE_GRID[self.tile_index - 1]
        self.tile_shape = TILE_SHAPE[self.tile - 1]

    def fix_collision_in_direction(self, dx, dy):
        self.fix_dx = dx
        self.fix_dy = dy
        self.solid = -1

        for _ in range(2):
            self.fix_collision_at_point(self.x - self.width, self.y - self.height, 'feet')
            self.fix_collision_at_point(self.x - self.width, self.y)
            self.fix_collision_at_point(self.x - self.width, self.y + self.height)

            self.fix_collision_at_point(self.x + self.width + minus_TINY, self.y - self.height, 'feet')
            self.fix_collision_at_point(self.x + self.width + minus_TINY, self.y)
            self.fix_collision_at_point(self.x + self.width + minus_TINY, self.y + self.height)

            if self.solid < 1:
                return       

    def fix_collision_at_point(self, x, y, part=''):
        self.get_tile_at(x, y)

        if self.tile_shape == '':
            return

        self.mod_x = x % TILE_SIZE
        self.mod_y = y % TILE_SIZE
        self.temp = TILE_SHAPE[self.tile - 1][0]

        if self.temp == '\\' or self.temp == '/':
            self.m = 1 / int(TILE_SHAPE[self.tile - 1][1])
            self.c = int(TILE_SHAPE[self.tile - 1][2]) * TILE_SIZE * self.m
            if self.temp == '\\':
                self.m = -self.m
                self.c = TILE_SIZE - self.c
            
            self.offset_y = self.mod_y - ((self.mod_x * self.m) + self.c)
            if not self.offset_y < 0:
                return
            
            if self.fix_dy < 0:
                self.y += -self.offset_y
                self.solid = 10
                return
            
            if self.fix_dy == 0 and ((self.fix_dx > 0) == (self.m > 0)):
                self.x += self.offset_y / self.m
                self.solid = 10
                return

        if self.tile_shape == '=':
            if (not part == 'feet') or (self.mod_y - self.fix_dy < TILE_SIZE):
                return

        self.solid = 10

        if self.fix_dy < 0:
            self.y += TILE_SIZE - self.mod_y

        if self.fix_dx < 0:
            self.x += TILE_SIZE - self.mod_x

        if self.fix_dy > 0:
            self.y += minus_TINY - self.mod_y

        if self.fix_dx > 0:
            self.x += minus_TINY - self.mod_x

    def move_sprite_x(self):
        self.orig_y = self.y
        self.x += self.speed_x
        self.fix_collision_in_direction(0, -1)
        if self.y > self.orig_y + abs(self.speed_x) + (TILE_SIZE / 8):
            self.y = self.orig_y
            self.fix_collision_in_direction(self.speed_x, 0)
            if self.solid > 0:
                self.speed_x = 0
                self.direction = -self.direction
        elif self.y > self.orig_y:
            self.speed_x = self.speed_x * 0.85

    def move_sprite_y(self):
        self.y += self.speed_y
        self.falling += 1
        self.fix_collision_in_direction(0, self.speed_y)
        if self.solid > 0:
            if self.speed_y < 0:
                self.falling = 0
            else:
                self.jumping = 99
            self.speed_y = 0

    def check_around_player_at_xy(self, x, y):
        global COINS

        self.get_tile_at(x, y)
        if self.tile == 24:
            TILE_GRID[self.tile_index - 1] = 2
            COINS += 1
            coin_sound.play()

    def paint_sprite(self):
        self.switch_costume('BIG')

        self.real_x = self.x - CAMERA_X
        self.real_y = self.y - CAMERA_Y

        self.switch_costume(self.costume)

    def flip(self):
        kick_shell_sound.play()
        self.speed_y = 14
        self.speed_x = mario.direction / 45
        self.type = 'flip'
        self.direction = 180

    def check_flip(self):
        if BUMP_INDEX == None:
            return
        
        self.get_tile_at(self.x - self.width, self.y - self.height - (TILE_SIZE / 4))
        if not self.tile_index == BUMP_INDEX:
            self.get_tile_at(self.x + self.width, self.y - self.height - (TILE_SIZE / 4))
            if not self.tile_index == BUMP_INDEX:
                return
            
        self.flip()
            
    def _move_enemy_(self):
        if self.type == 'flip':
            self.x += self.speed_x
            self.speed_y += -1
            self.y += self.speed_y
            if self.y < CAMERA_Y - (CENTER_Y + 20):
                self.delete_clone()
            return

        if self.y < -TILE_SIZE:
            self.delete_clone()
        
        if self.type == 'squish':
            self.frame += 1
            if self.frame > 10:
                self.delete_clone()

        if self.frame in [None, -1]:
            if self.frame == -1:
                if BUMP_INDEX == self.spawn_index:
                    self.frame = 0
                    self.direction = -mario.direction
                    LAYERS.remove('enemy')
                    LAYERS.insert(LAYERS_BACKGROUND, 'enemy')
                return
            if abs(self.x - CAMERA_X) > CENTER_X + (20 * (TILE_SIZE / 32)):
                return
            if abs(self.y - CAMERA_Y) > CENTER_Y + (20 * (TILE_SIZE / 32)):
                return
            
            if self.x > mario.x:
                self.direction = -90
            else:
                self.direction = 90

        if self.type == 'Goomba':
            self.tick_goomba()
            return

        if self.type == 'Life':
            self.tick_life()
            return

        if self.type == 'Piranha':
            if abs(self.x - CAMERA_X) > CENTER_X + (20 * (TILE_SIZE / 32)):
                LAYERS.remove('enemy')
                LAYERS.insert(LAYERS_BACKGROUND + 2, 'enemy')
                return
            if abs(self.y - CAMERA_Y) > CENTER_Y + (20 * (TILE_SIZE / 32)):
                LAYERS.remove('enemy')
                LAYERS.insert(LAYERS_BACKGROUND + 2, 'enemy')
                return
            LAYERS.remove('enemy')
            LAYERS.insert(LAYERS_BACKGROUND, 'enemy')
            self.tick_piranha()
            return

        if self.type == 'EndBox':
            try:
                self.frame += 0.15
            except:
                self.frame = 0.15
            self.costume = 23 + math.floor(self.frame) % 3

            if colliding(self, mario):
                if distance(self, mario) < 28 * (TILE_SIZE / 32):
                    self.type = 'costume'
                    self.costume = 'EndBox'
                    mario_level_complete()

            return

        if self.type == 'Koopa':
            self.tick_goomba()
            return
        
        if self.type == 'Koopa Shell':
            self.tick_shell()
            return
        
        if self.type == 'Fireball':
            self.tick_fireball()
            return

    def general_move(self, acc_x, max_):
        self.speed_y += -1
        self.move_sprite_y()

        if self.direction > 0:
            if self.speed_x < max_ * (TILE_SIZE / 32):
                self.speed_x += acc_x
        else:
            if self.speed_x > -max_ * (TILE_SIZE / 32):
                self.speed_x += -acc_x
            
        self.move_sprite_x()

    def tick_goomba(self):
        global BOUNCE_PLAYER

        self.general_move(0.1, 1)

        try:
            self.frame += 0.25
            self.costume = self.root_costume + math.floor(self.frame % 2)
        except:
            self.frame = 0.25
            self.costume = self.root_costume + math.floor(self.frame % 2)

        self.paint_sprite()

        if colliding(self, mario):
            if STAR_POWER > 0:
                self.flip()
                return
            
            if mario.bop_y != None:
                stomped_sound.play()
                self.direction = 90
                self.frame = 0
                BOUNCE_PLAYER = 5

                if self.type == 'Goomba':
                    self.type = 'squish'
                    self.costume = 'Goomba Squish'
                else:
                    if self.type == 'Koopa':
                        self.type = 'Koopa Shell'
                        self.root_costume = 26
                        self.height = 15 * (TILE_SIZE / 32)
                    else:
                        pass

                PARTICLES.append('score 100')
                PARTICLES.append(self.x)
                PARTICLES.append(self.y)
            else:
                mario_hurt()

        self.check_flip()

    def tick_life(self):
        global MARIO

        self.frame += TILE_SIZE / 32
        if self.frame < TILE_SIZE / 2:
            return

        if self.frame < (3 / 2) * TILE_SIZE:
            if self.frame == TILE_SIZE / 2:
                item_sprout_sound.play()

            self.visible = 1
            self.y += TILE_SIZE / 32

            if self.frame == ((3 / 2) * TILE_SIZE) - 1:
                LAYERS.remove('enemy')
                LAYERS.insert(LAYERS_BACKGROUND + 2, 'enemy')

        else:
            if self.root_costume == 'Life':
                self.general_move(3, 1)

            if colliding(self, mario):
                just_what_I_needed_sound.play()
                if self.root_costume == 'FireFlower' and MARIO == 'Mario':
                    MARIO = 'Fire'
                elif self.root_costume == 'Star':
                    collect_star_power()
                else:
                    collect_1up()
                enemies.remove(self)

    def tick_piranha(self):
        LAYERS.remove('enemy')
        LAYERS.insert(LAYERS_BACKGROUND, 'enemy')
        try:
            self.frame += 1
        except:
            self.frame = 1
        
        self.costume = 9 + (math.floor(self.frame / 4) % 2)

        self.temp = (self.frame / 16) % 8
        if math.floor(self.temp) < 4:
            if abs(self.x - mario.x) < 45:
                self.frame = 1
        if math.floor(self.temp) == 4:
            self.y += TILE_SIZE / 8
        if math.floor(self.temp) == 7:
            self.y += -TILE_SIZE / 8

        if self.temp > 4.2:
            if colliding(self, mario):
                if STAR_POWER > 0:
                    self.flip()
                    return

                mario_hurt()

    def tick_shell(self):
        global BOUNCE_PLAYER

        self.costume = self.root_costume
        self.speed_y += -1
        self.move_sprite_y()
        if self.frame == None:
            self.frame = 0

        if self.frame < 3:
            self.frame += 1
            return
        
        if self.frame == 3:
            if not colliding(self, mario):
                return
            
            if mario.x < self.x:
                self.direction = 90
            else:
                self.direction = -90
            self.visible = 2
            
        self.frame += 0.5
        self.speed_x = self.direction / 9
        self.move_sprite_x()
        self.costume += math.floor(self.frame % 4)

        self.paint_sprite()

        if self.frame > 10 and colliding(self, mario):
            if not mario.bop_y == None:
                stomped_sound.play()
                self.direction = 90
                self.frame = 0
                BOUNCE_PLAYER = 5
                self.visible = 1
            else:
                mario_hurt()

        self.check_flip()
        self.check_around_player_at_xy(self.x, self.y)

    def tick_fireball(self):
        self.frame += 1
        if self.frame > 2:
            self.direction += 90
            self.frame = 0

        self.move_sprite_x()
        if self.speed_x == 0:
            self.delete_clone()

        if abs(self.x - CAMERA_X) > CENTER_X:
            self.delete_clone()

        if self.speed_y > -12:
            self.speed_y += -1.5
        
        self.move_sprite_y()

        if self.falling == 0:
            self.speed_y = 11
            
        self.direction %= 360
        if self.direction == 270:
            self.direction = -90

    def move_enemy(self):
        global BUMP_INDEX

        if EDITOR > 0 or self.type == None:
            return

        self._move_enemy_()

        if self.visible == 1:
            self.hide = True

    def move_player_after_enemy(self):
        if self.type == None:
            return
        
        if self.type in 'flip Life EndBox':
            return

        if EDITOR < 1 and self.visible == 1:
            self.hide = False
            
            for enemy in enemies:
                if not enemy == self and not enemy.type == None:
                    if colliding(self, enemy) and enemy.visible == 2:
                        self.flip()
                        break
            
            self.hide = True

    def hide_fireballs(self):
        if self.type == 'Fireball':
            self.hide = True
            return
        
        if self.visible > 0:
            self.hide = False

    def check_fireballs(self):
        if self.type == 'Fireball':
            self.hide = False
            
            for enemy in enemies:
                if not enemy == self and not enemy.type == None:
                    if colliding(self, enemy) and enemy.visible == 1:
                        self.delete_clone()
                        break
            
            self.hide = True

    def position_tiles(self):
        if self.visible > 0:
            self.hide = False

        if self.type == None:
            return
        self.paint_sprite()

    def LEVEL_done_loading(self):
        ENTITY_clear()
        ENTITY_setup()

    def ENTITY_clear(self):
        if self.type == None:
            return

        enemies.remove(self)

    def ENTITY_setup(self):
        if not self.type == None:
            return

        self.spawn_loop()

    def mario_fireball(self):
        if self.type == None:
            enemies.append(Enemy(info=['Fireball', 0, 0, 0, 0, 0, 0, 0]))

    def draw(self):
        if self.type == None or self.hide:
            return
        
        if self.costume == 'Goomba Squish':
            pos = coords.pygame([self.real_x, self.real_y - (TILE_SIZE / 4)], [WIDTH, HEIGHT])
        else:
            pos = coords.pygame([self.real_x, self.real_y], [WIDTH, HEIGHT])
        
        width = self.real_costume.get_width() / 2
        height = self.real_costume.get_height() / 2

        if self.direction == 90:
            screen.blit(self.real_costume, [pos[0] - width, pos[1] - height])
        elif self.direction == -90:
            image = pygame.transform.flip(self.real_costume, True, False)
            screen.blit(image, [pos[0] - width, pos[1] - height])
        elif self.direction == 180:
            image = pygame.transform.flip(self.real_costume, False, True)
            screen.blit(image, [pos[0] - width, pos[1] - height])
        elif self.direction == 0:
            image = pygame.transform.flip(self.real_costume, True, True)
            screen.blit(image, [pos[0] - width, pos[1] - height])
        else:
            screen.blit(self.real_costume, [pos[0] - width, pos[1] - height])

class Editor:
    def __init__(self):
        global EDITOR, LEVEL_NUM, TILE_GRID, GRID_WIDTH, GRID_HEIGHT

        self.tile = 0
        self.tile_index = 1
        self.tile_grid_x = 0
        self.tile_grid_y = 0
        self.found_index = 0
        self.auto = 1
        self.tile_keymap = [
            '',
            '',
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            2,
            '',
            '',
            '',
            4,
            '',
            '',
            '',
            4,
            9,
            9,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            1,
            1,
            1,
            1,
            9,
            9,
            2,
            2,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            9,
            9,
            9
        ]
        self.tile_recipes = [
            '',
            '',
            '1110 1100',
            '1111 1101 1000',
            '1011 1001',
            '0110 0100',
            '0111 0101 0000 0010',
            '0011 0001',
            '',
            '',
            '1100',
            '1101 1000',
            '1001',
            '1110',
            '1111 1010',
            '1011',
            '0110 0100',
            '0111 0010 0000 0101',
            '0011 0011 0001',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '0110 0100',
            '0111 0010 0000 0101',
            '0011 0001',
            '1110',
            '1111',
            '1011',
            '1100',
            '1101 1000',
            '1001',
            '0110 0100',
            '0011 0001',
            '1110 1100',
            '1011 1001',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ]
        self.edited_indexes = []

        EDITOR = 0
        LEVEL_NUM = 1
        TILE_GRID = []
        level_store.LEVEL_load()
        self.brush = 0
        self.chosen_brush = 10

        if len(TILE_GRID) == 0:
            GRID_WIDTH = 100
            GRID_HEIGHT = 40
            self.generate_level()

    def generate_level(self):
        global TILE_GRID, OBJECT_IDX, OBJECT_TYPE
        TILE_GRID = []
        OBJECT_IDX = []
        OBJECT_TYPE = []
        self.add_wall_column()
        for _ in range(GRID_WIDTH - 2):
            self.add_boxed_column()
        self.add_wall_column()

    def add_wall_column(self):
        for _ in range(GRID_HEIGHT):
            TILE_GRID.append(10)

    def add_boxed_column(self):
        TILE_GRID.append(7)
        for _ in range(GRID_HEIGHT - 2):
            TILE_GRID.append(2)
        TILE_GRID.append(10)

    def get_tile_at(self, x, y):
        self.tile_grid_x = math.floor(x / TILE_SIZE)
        self.tile_grid_y = math.floor(y / TILE_SIZE)
        self.tile_index = 1 + self.tile_grid_y + (self.tile_grid_x * GRID_HEIGHT)
        self.tile = TILE_GRID[self.tile_index - 1]

    def fix_costume_at(self, idx):
        if pygame.key.get_pressed()[K_SPACE]:
            if not idx in self.edited_indexes:
                return            

        self.tile = TILE_GRID[idx - 1]
        self.tile_group = 0
        self.edge_tile = 0
        if self.tile_recipes[self.tile - 1] == '':
            return
        
        self.tile_group = TILE_GROUPS[self.tile - 1]
        if self.tile_group == '':
            return
        
        self.recipe = ''
        self.build_recipe(idx + 1)
        self.build_recipe(idx + GRID_HEIGHT)
        self.build_recipe(idx - 1)
        self.build_recipe(idx - GRID_HEIGHT)

        self.tile = 1
        for _ in range(len(TILE_GROUPS)):
            if TILE_GROUPS[self.tile - 1] == self.tile_group:
                if self.recipe in self.tile_recipes[self.tile - 1]:
                    TILE_GRID[idx - 1] = self.tile
                    return
            self.tile += 1

    def build_recipe(self, edge_index):
        if pygame.key.get_pressed()[K_SPACE]:
            if not edge_index in self.edited_indexes:
                self.recipe = f'{self.recipe}0'
                return

        self.edge_tile = TILE_GRID[edge_index - 1]
        if self.tile_group == TILE_GROUPS[self.edge_tile - 1]:
            self.recipe = f'{self.recipe}1'
        else:
            self.recipe = f'{self.recipe}0'

    def paint_tile(self):
        if self.brush == 0:
            if self.tile == self.chosen_brush:
                self.brush = 2
            else:
                self.brush = self.chosen_brush

                if self.auto > 0:
                    self.tile_group = TILE_GROUPS[self.chosen_brush - 1]
                    if not self.tile_group == '':
                        if self.tile_group == TILE_GROUPS[self.tile - 1]:
                            self.brush = 2

        if self.brush == 28:
            try:
                self.found_index = TILE_GRID.index(self.brush)
                TILE_GRID[self.found_index] = 2
            except:
                pass

        TILE_GRID[self.tile_index - 1] = self.brush

        if self.auto > 0:
            if not self.tile_index in self.edited_indexes:
                self.edited_indexes.append(self.tile_index)

            self.fix_costume_at(self.tile_index)
            self.fix_costume_at(self.tile_index + 1)
            self.fix_costume_at(self.tile_index + GRID_HEIGHT)
            self.fix_costume_at(self.tile_index - 1)
            self.fix_costume_at(self.tile_index - GRID_HEIGHT)

    def paint_entity(self):
        if self.brush > 0:
            return
        
        self.brush = self.chosen_brush

        try:
            self.found_index = OBJECT_IDX.index(self.tile_index) + 1
        except:
            self.found_index = 0

        if self.found_index > 0:
            OBJECT_IDX.pop(self.found_index - 1)
            OBJECT_TYPE.pop(self.found_index - 1)
        else:
            OBJECT_IDX.append(self.tile_index)
            OBJECT_TYPE.append(self.brush)

        ENTITY_clear()
        ENTITY_setup()

    def next_brush(self, key):
        for _ in range(len(self.tile_keymap)):
            if self.chosen_brush < len(self.tile_keymap):
                self.chosen_brush += 1
            else:
                self.chosen_brush = 1

            if self.tile_keymap[self.chosen_brush - 1] == key:
                self.tile_group = TILE_GROUPS[self.chosen_brush - 1]

                if self.auto < 1 or self.tile_group == '':
                    return
                
                if TILE_GROUPS.index(self.tile_group) + 1 == self.chosen_brush:
                    return

    def move_player(self):
        if EDITOR < 1:
            return
        
        mouse_x, mouse_y = coords.reg(MOUSE.get_pos(), [WIDTH, HEIGHT])
        self.get_tile_at(mouse_x + CAMERA_X, mouse_y + CAMERA_Y)

        if not MOUSE_DOWN():
            self.brush = 0
            self.edited_indexes = []
            return
        
        if self.tile_keymap[self.chosen_brush - 1] == 9:
            self.paint_entity()
            return
        
        self.paint_tile()

class Particle:
    def __init__(self, dummy=False, info=False):
        global PARTICLES

        if dummy:
            self.frame = None
            PARTICLES = []
        else:
            self.start_as_clone(info)
        self.real_x = 0
        self.real_y = 0
        self.costume = smoke_1

    def start_as_clone(self, info):
        self.frame = 1
        self.type = info[0]
        self.x = info[1]
        self.y = info[2]

        if self.type == 'coin':
            self.speed_y = 12
            coin_sound.play()

    def spawn_particles(self):
        while not (len(PARTICLES) == 0):
            type = PARTICLES[0]
            x = PARTICLES[1]
            y = PARTICLES[2]
            particles.append(Particle(info=[type, x, y]))

            for _ in range(3):
                PARTICLES.pop(0)

    def position_with_costume(self, costume):
        self.costume = particle_imgs[7]
        self.real_x = self.x - CAMERA_X
        self.real_y = self.y - CAMERA_Y
        self.costume = particle_imgs[costume]

    def tick_smoke(self):
        if not self.frame < 3:
            particles.remove(self)
            return

        self.position_with_costume(math.floor(self.frame))
        self.frame += 0.4

    def tick_coin(self):
        self.speed_y += -1
        if self.speed_y < -12:
            particles.remove(self)
        self.y += self.speed_y

        self.position_with_costume(3 + (math.floor(self.frame) % 4))
        self.frame += 0.5

    def tick_score(self):
        self.y += 1
        self.position_with_costume(8)
        self.frame += 1
        if self.frame > 60: # 2 seconds
            particles.remove(self)

    def position_tiles(self):
        if self.frame == None:
            self.spawn_particles()
            return
        
        if self.type == 'coin':
            self.tick_coin()
            return
        
        if 'score' in self.type:
            self.tick_score()
            return
        
        self.tick_smoke()

    def draw(self):
        if self.frame == None:
            return

        width, height = self.costume.get_size()
        pos = coords.pygame([self.real_x, self.real_y], [WIDTH, HEIGHT])
        screen.blit(self.costume, [pos[0] - (width / 2), pos[1] - (height / 2)])

class Controls:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.down = 0
        self.up = 0
        self.x_axis = 0
        self.y_axis = 0
        self.button_B = None

    def check_controls(self):
        keys = pygame.key.get_pressed()

        self.left = keys[K_LEFT] or keys[K_a]
        self.right = keys[K_RIGHT] or keys[K_d]
        self.down = keys[K_DOWN] or keys[K_s]
        self.up = keys[K_UP] or keys[K_w]

        self.x_axis = self.right - self.left
        self.y_axis = self.up - self.down

        if keys[K_x]:
            if self.button_B == None:
                self.button_B = 0
            self.button_B += 1
        else:
            self.button_B = None

class Level_Store:
    def __init__(self):
        self.level_store = read_tile_grid()

        self.a_to_z = [
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z'
        ]

    def Int(self, string):
        try:
            integer = int(string)
        except:
            integer = 9999
        return integer

    def write_value(self, value, delimeter):
        self.encoded = f'{self.encoded}{value}{delimeter}'

    def read_letter(self):
        try:
            self.letter = self.encoded[self.read_index - 1]
        except:
            self.letter = ''
        self.read_index += 1

    def read_value(self):
        self.value = ''
        self.read_letter()
        while not (self.Int(self.letter) > 9 or self.letter == ''):
            self.value = self.value + self.letter
            self.read_letter()

    def save_tile_grid(self):
        self.write_value(GRID_WIDTH, '_')
        self.write_value(GRID_HEIGHT, '_')
        self.tile_index = 1
        self.tile = TILE_GRID[0]
        self.length = 0

        for _ in range(GRID_HEIGHT):
            for __ in range(GRID_WIDTH):
                if self.length < 26 and self.tile == TILE_GRID[self.tile_index - 1]:
                    self.length += 1
                else:
                    if self.tile == 2:
                        self.tile = ''
                    self.write_value(self.tile, self.a_to_z[self.length - 1])
                    self.tile = TILE_GRID[self.tile_index - 1]
                    self.length = 1
                self.tile_index += GRID_HEIGHT
            self.tile_index += 1 - (GRID_WIDTH * GRID_HEIGHT)

        self.write_value(self.tile, self.a_to_z[self.length - 1])

    def save_objects(self):
        self.row = 1
        self.write_value(len(OBJECT_IDX), '_')

        for _ in range(len(OBJECT_IDX)):
            self.write_value(OBJECT_IDX[self.row - 1], '_')
            self.write_value(OBJECT_TYPE[self.row - 1], '_')
            self.row += 1

    def load_tile_grid(self):
        global TILE_GRID, GRID_WIDTH, GRID_HEIGHT

        TILE_GRID = []
        self.read_value()
        GRID_WIDTH = self.Int(self.value)
        self.read_value()
        GRID_HEIGHT = self.Int(self.value)

        for _ in range(GRID_WIDTH * GRID_HEIGHT):
            TILE_GRID.append('')
        
        self.tile_index = 1
        while not (self.read_index > len(self.encoded)):
            self.read_value()
            if self.value == '':
                self.value = 2
            for _ in range(self.a_to_z.index(self.letter) + 1):
                TILE_GRID[self.tile_index - 1] = self.Int(self.value)
                self.tile_index += GRID_HEIGHT

                if self.tile_index > GRID_WIDTH * GRID_HEIGHT:
                    self.tile_index += 1 - (GRID_WIDTH * GRID_HEIGHT)
                    
                    if self.tile_index > GRID_HEIGHT:
                        return

    def load_objects(self):
        global OBJECT_IDX, OBJECT_TYPE

        OBJECT_IDX = []
        OBJECT_TYPE = []
        self.read_value()

        for _ in range(self.Int(self.value)):
            self.read_value()
            OBJECT_IDX.append(self.Int(self.value))
            self.read_value()
            OBJECT_TYPE.append(self.Int(self.value))

    def save_level(self, level_num):
        self.encoded = ''
        self.write_value(1, '_')
        
        self.save_tile_grid()
        self.save_objects()
        
        for _ in range(level_num - len(self.level_store)):
            self.level_store.append('')

        self.level_store[level_num - 1] = self.encoded

    def load_level(self, level_num):
        try:
            self.encoded = read_tile_grid()[level_num - 1].replace('\n', '')
        except:
            self.encoded = read_tile_grid()[0].replace('\n', '')
        
        self.read_index = 1
        self.read_value()
        if not self.Int(self.value) == 1:
            return
        
        self.load_tile_grid()
        self.load_objects()

    def LEVEL_save(self):
        self.save_level(LEVEL_NUM)
        write_tile_grid()

    def LEVEL_load(self):
        self.load_level(LEVEL_NUM)
        LEVEL_done_loading()

class Background:
    def __init__(self, costume):
        self.real_x = 0
        self.real_y = 0
        self.costume = costume

        self.sprite_width = 256 * (TILE_SIZE / 16)
        self.x = (costume - 1) * self.sprite_width
        self.screen_x = 0

    def position_tiles(self):
        self.screen_x = self.x - (CAMERA_X / 2)
        self.real_x = (self.screen_x % (self.sprite_width * 2)) - self.sprite_width
        self.real_y = (CENTER_Y + (2 * TILE_SIZE)) - (CAMERA_Y / 2)

    def draw(self):
        image = background_imgs[self.costume]
        height = image.get_height()
        pos = coords.pygame([self.real_x, self.real_y], [WIDTH, HEIGHT])
        screen.blit(image, [pos[0] - (self.sprite_width / 2), pos[1] - (height / 2)])

class Sounds:
    def __init__(self):
        pass

    def music(self):
        Music_L1.stop()
        if EDITOR < 1:
            Music_L1.play(-1)

    def LEVEL_start_game_loop(self):
        self.music()

    def LEVEL_start_game_loop_respawn(self):
        self.music()

    def LEVEL_stop(self):
        Music_L1.stop()

    def mario_lose_life(self):
        Music_L1.stop()

    def mario_level_complete(self):
        Music_L1.stop()
        star_power_sound.stop()
        course_clear_sound.play()

    def collect_star_power(self):
        global STAR_POWER

        Music_L1.stop()
        STAR_POWER = 1000

        star_power_sound.play()

    def move_player(self):
        global STAR_POWER

        if STAR_POWER > 0:
            if pygame.mixer.get_busy():
                return
            level_select_sound.play()
            STAR_POWER = 0
            self.music()


def check_controls():
    controls.check_controls()

def move_player():
    mario.move_player()
    editor.move_player()
    sounds.move_player()

def move_enemy():
    for enemy in enemies:
        enemy.move_enemy()

def move_player_after_enemy():
    mario.move_player_after_enemy()

    for enemy in enemies:
        enemy.move_player_after_enemy()

def hide_fireballs():
    for enemy in enemies:
        enemy.hide_fireballs()

def check_fireballs():
    for enemy in enemies:
        enemy.check_fireballs()

def position_tiles():
    mario.position_tiles()

    for tile in tiles:
        tile.position_tiles()

    for enemy in enemies:
        enemy.position_tiles()

    for particle in particles:
        particle.position_tiles()

    for background in backgrounds:
        background.position_tiles()

def LEVEL_start_game_loop():
    global FIREBALLS

    FIREBALLS = 0
    mario.LEVEL_start_game_loop()
    sounds.LEVEL_start_game_loop()

def LEVEL_start_game_loop_respawn():
    try:
        mario.LEVEL_start_game_loop_respawn()
        sounds.LEVEL_start_game_loop_respawn()
    except:
        pass

def LEVEL_stop():
    mario.LEVEL_stop()
    sounds.LEVEL_stop()

def LEVEL_done_loading():
    mario.LEVEL_done_loading()
    for tile in tiles:
        tile.LEVEL_done_loading()
    try:
        for enemy in enemies:
            enemy.LEVEL_done_loading()
    except:
        pass

def LEVEL_continue_game_loop():
    mario.LEVEL_continue_game_loop()

def ENTITY_clear():
    for enemy in enemies:
        enemy.ENTITY_clear()

def ENTITY_setup():
    for enemy in enemies:
        enemy.ENTITY_setup()

def mario_lose_life():
    sounds.mario_lose_life()
    mario.mario_lose_life()

def mario_level_complete():
    sounds.mario_level_complete()
    mario.mario_level_complete()

def collect_1up():
    mario.collect_1up()

def mario_hurt():
    mario.mario_hurt()

def mario_fireball():
    for enemy in enemies:
        enemy.mario_fireball()

def collect_star_power():
    sounds.collect_star_power()

def setup():
    tile_index = 1
    tile_x = TILE_SIZE / 2
    for _ in range(CLONE_COUNT_X):
        tile_y = TILE_SIZE / 2
        for __ in range(CLONE_COUNT_Y):
            tiles.append(Tile(tile_x, tile_y, tile_index))
            tile_y += TILE_SIZE
            tile_index += 1
        tile_x += TILE_SIZE
        tile_index += GRID_HEIGHT - CLONE_COUNT_Y

def draw():
    screen.fill((128, 168, 248))

    if GAME_LOOP_RUNNING:
        check_controls()
        move_player()
        move_enemy()
        move_player_after_enemy()
        hide_fireballs()
        check_fireballs()
        position_tiles()

    for sprite in LAYERS:
        if sprite == 'mario':
            mario.draw()

        elif sprite == 'tile':
            for tile in tiles:
                if not tile == tiles[0]:
                    tile.draw()

        elif sprite == 'enemy':
            for enemy in enemies:
                enemy.draw()
        
        elif sprite == 'particle':
            for particle in particles:
                particle.draw()

        elif sprite == 'background':
            for background in backgrounds:
                background.draw()

    label = FONT.render(f'COINS: {COINS}', 1, BLACK)
    screen.blit(label, [CENTER_X - (label.get_width() / 2), 0])

    if EDITOR > 0:
        tiles[0].editor_brush()
        screen.blit(FONT.render(f'LEVEL#: {LEVEL_NUM}', 1, BLACK), [0, 0])

tiles = []
clock = pygame.time.Clock()
level_store = Level_Store()
mario = Mario()
editor = Editor()
tiles = [Tile(0, 0, None)]
enemies = []
enemies.append(Enemy(dummy=True))
particles = []
particles.append(Particle(dummy=True))
controls = Controls()
backgrounds = [Background(1), Background(2)]
sounds = Sounds()

LEVEL_start_game_loop()
mario.reset_player()
level_store.LEVEL_load()

setup()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_0:
                if EDITOR > 0:
                    LEVEL_stop()
                    level_store.LEVEL_save()
                    EDITOR = 0
                    LEVEL_done_loading()
                    LEVEL_start_game_loop()
                else:
                    LEVEL_stop()
                    EDITOR = 1
                    level_store.LEVEL_load()
                    LEVEL_start_game_loop()
                
            if EDITOR > 0:
                if event.key == K_1:
                    editor.next_brush(1)
                if event.key == K_2:
                    editor.next_brush(2)
                if event.key == K_3:
                    editor.next_brush(3)
                if event.key == K_4:
                    editor.next_brush(4)
                if event.key == K_5:
                    editor.next_brush(5)
                if event.key == K_9:
                    editor.next_brush(9)

                if event.key == K_e:
                    if editor.tile_index in OBJECT_IDX:
                        obj_num = OBJECT_IDX.index(editor.tile_index)
                        editor.chosen_brush = OBJECT_TYPE[obj_num]
                    else:
                        editor.chosen_brush = editor.tile

                if event.key == K_q:
                    editor.auto = 1 - editor.auto

                if event.key == K_l:
                    answer = float(input(f'Enter Level Number (Current {LEVEL_NUM}) '))
                    if round(answer) >= 1:
                        LEVEL_stop()
                        level_store.LEVEL_save()
                        LEVEL_NUM = round(answer)
                        level_store.LEVEL_load()
                        LEVEL_start_game_loop_respawn()

                if event.key == K_r:
                    answer = input(f'Reset Level - Are you sure? [Y|N] ')
                    if answer.capitalize() == 'Y':
                        LEVEL_stop()
                        answer = input(f'Enter Level Width (Current {GRID_WIDTH}) ')

                        if not answer == '':
                            GRID_WIDTH = int(answer)

                        answer = input(f'Enter Level Height (Current {GRID_HEIGHT}) ')

                        if not answer == '':
                            GRID_HEIGHT = int(answer)

                        editor.generate_level()
                        LEVEL_done_loading()
                        LEVEL_start_game_loop_respawn()

    timer += 1 / FPS

    draw()

    pygame.display.flip()
