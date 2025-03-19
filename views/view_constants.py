import pygame
import os




BOARD_SEPARATION = 5

ROWS = 10
COLS = 10 
CELL_SIZE = 50

BASE_SCREEN_WIDTH = ROWS * CELL_SIZE * 2 + BOARD_SEPARATION
BASE_SCREEN_HEIGHT = COLS * CELL_SIZE

# SHIP SETUP SCREEN CONSTANTS#
BOARD_SEPARATION_TO_SHIPS = 20
SHIP_POOL_WIDTH = 7
SHIP_POOL_HEIGHT = 7

# Assets Path

WATER_PATH = pygame.transform.scale(
    (pygame.image.load(os.path.join("assets", "water.png"))),
    (CELL_SIZE - 3, CELL_SIZE -1),
)

SHIP_TEST_PATH = pygame.transform.scale(
    (pygame.image.load(os.path.join("assets", "test-ship-img.jpg"))),
    (CELL_SIZE - 3, CELL_SIZE -1),
)

ACCEPT_BUTTON_SPRITESHEET_PATH = "assets/Buttons/Start-Metal-Button.png"

# Font




