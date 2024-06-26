import pygame
import numpy as np

pygame.init()
# Constants
x, y = 10, 10
DIMS = (x*63.2, y*90)
space = 4
BLUE, WHITE, RED, ORANGE, GREEN, YELLOW, BLACK  = (0, 141, 218), (255, 255, 255), (237,25,9), (242,133,0), (50,205,50), (255,255,0), (0, 0, 0)
COLORS = (RED, ORANGE, GREEN, YELLOW, BLUE, WHITE)
player_start = pygame.Rect(0, y*80, x*62.2, y*1.5) # Used for menu only
player = pygame.Rect(x*2, y*80, x*4, y*1.5)
# Game borders 
wall_left = pygame.Rect(0, 0, x*1, y*90)
wall_right = pygame.Rect(x*62.2, 0, x*1, y*90)
border_top = pygame.Rect(0, y*8, x*63.2, y*3.5)

# Loop generating tiles
red_tiles, orange_tiles, green_tiles, yellow_tiles = [], [], [], []
tile_array = [red_tiles, orange_tiles, green_tiles, yellow_tiles]
side_tiles = []
side_tiles_colors = [RED, RED, ORANGE, ORANGE, GREEN, GREEN, YELLOW, YELLOW]
# red tile has no spacing
for j in range(4):     
    for k in range(1,3):
        for i in range(14):
            tile = pygame.Rect(
                x*1 + (i*x*4) + i*space,
                y*20 + k*x*1.5 + k*space +2*j*x*1.5 + 2*j*space,
                x*4, 
                y*1.5)
            tile_array[j].append(tile)
            

# Colors on side walls:
for i in range(4):
    for k in range(2):
        side_tile = pygame.Rect(
            0 + 622*k, # Left
            20-2 + 200+ 38*i, # Top
            10, # Width
            38, # Height
        )
        side_tiles.append(side_tile)

# Ball settings (An inscribed square is used to wrap around the ball)
ball_radius = 5
ball_rect = int(ball_radius * 2 **0.5)
ball =  pygame.Rect(400, 400, ball_rect, ball_rect)
ball_speed = 3
dx, dy = 1, -1 
ball_color = pygame.Color(255,255,255)

# Text rendering
font_big = pygame.font.Font("../misc/pixel-loot.ttf", 50)
font_small = pygame.font.Font("../misc/pixel-loot.ttf", 30)

score_coord = (100, 190)
lives_coord = (400, 140)
high_score_coord = (500, 190)

def flash_text(screen, score, coord):
    score_text = ('000' + str(score))[-3:]
    text = font_big.render(score_text, True, WHITE, None)
    textRect = text.get_rect()
    textRect.center = coord
    screen.blit(text, textRect)

def update_text(screen, score, coord):
    score_text = ('000' + str(score))[-3:]
    text = font_big.render(score_text, True, WHITE, None)
    textRect = text.get_rect()
    textRect.center = coord
    screen.blit(text, textRect)

def update_lives(screen, lives, coord):
    text = font_big.render(str(lives), True, WHITE, None)
    textRect = text.get_rect()
    textRect.center = coord
    screen.blit(text, textRect)


def banner(screen, message, ball_speed):
    # Initialize Banner font:
    text = font_small.render(message, True, WHITE, None)
    textRect = text.get_rect()
    textRect.center = (300, 60)
    if textRect.x > 900:
        textRect.x = -400
    textRect.x += ball_speed
    screen.blit(text, textRect)


def render_game(screen, player):
            # Render start screen
            pygame.draw.rect(screen, BLUE, player)
            # Game borders 
            pygame.draw.rect(screen, WHITE, wall_left)
            pygame.draw.rect(screen, WHITE, wall_right)
            pygame.draw.rect(screen, WHITE, border_top)
            # Game border blue
            pygame.draw.rect(screen, BLUE, pygame.Rect(0, y*79, x*1, y*3.5))
            pygame.draw.rect(screen, BLUE, pygame.Rect(x*62.2, y*79, x*1, y*3.5))
            # Loop generating colored side tiles
            for i in range(8):
                pygame.draw.rect(screen, side_tiles_colors[i], side_tiles[i])
            
            # Loop generating tiles
            for i in range(4):
                for tile in tile_array[i]:
                    pygame.draw.rect(screen, COLORS[i], tile)
        