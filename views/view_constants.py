import pygame
import os
BOARD_WIDTH         = 10
BOARD_HEIGHT        = 10
BOARD_SEPARATION    = 5

ROWS = 10
COLS = 10
CELL_SIZE = 50

SCREEN_WIDTH        = BOARD_WIDTH * CELL_SIZE * 2 + BOARD_SEPARATION
SCREEN_HEIGHT       = BOARD_HEIGHT * CELL_SIZE

#SHIP SETUP SCREEN CONSTANTS#
BOARD_SEPARATION_TO_SHIPS   = 20
SHIP_POOL_WIDTH             = 7 * CELL_SIZE
SHIP_POOL_HEIGHT            = 7 * CELL_SIZE

# Assets Path 

WATER_PATH = pygame.transform.scale((pygame.image.load(os.path.join ("assets","water.png"))),(CELL_SIZE, CELL_SIZE))