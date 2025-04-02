import pygame
import os



# Board #
BOARD_SEPARATION = 5

ROWS = 10
COLS = 10 
CELL_SIZE = 50

# Screen #
MARGIN = 150
BASE_SCREEN_WIDTH = ROWS * CELL_SIZE * 2 + BOARD_SEPARATION + MARGIN
BASE_SCREEN_HEIGHT = COLS * CELL_SIZE + MARGIN

# SHIP SETUP SCREEN CONSTANTS#
BOARD_SEPARATION_TO_SHIPS = 20
SHIP_POOL_WIDTH = 7
SHIP_POOL_HEIGHT = 7


# Assets Path #

# Cells and Ships
WATER_PATH = "src/assets/Water.png"

WATER_HITTED_PATH = "src/assets/Water-Hitted.png"

HITTED_SHIP_SPRITESHEET_PATH = "src/assets/Ships/Ship-hitted-fire-animation-spritesheet.png"

CROSS_PATH = "src/assets/cross.png"

SHIP_TEST_PATH = "src/assets/test-ship-img.jpg"


# Backgrounds And buttons
ACCEPT_BUTTON_SPRITESHEET_PATH = "src/assets/Buttons/Start-Metal-Button.png"

EXIT_BUTTON_SPRITESHEET_PATH = "src/assets/Buttons/Exit-Metal-Button.png"

MENU_BACKGROUND_LOGO_SPRITESHEET_PATH = "src/assets/Backgrounds/Menu-Background-Logo.png"

MENU_BACKGROUND_IMAGE_PATH = "src/assets/Backgrounds/Menu-Background.png"



# Font




