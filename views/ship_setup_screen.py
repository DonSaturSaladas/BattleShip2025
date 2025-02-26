import pygame
from .view_constants import *

class ShipSetupScreen:
    def __init__(self, window, main_screen):
        self.window = window
        self.main_screen = main_screen
    
    def run(self):
        self.draw_setup_screen()
    
    def draw_setup_screen(self):
        total_width = BOARD_WIDTH * CELL_SIZE + BOARD_SEPARATION_TO_SHIPS + SHIP_POOL_WIDTH
        ship_pool_left = (SCREEN_WIDTH - total_width) / 2
        ship_pool_top = (SCREEN_HEIGHT - SHIP_POOL_HEIGHT) / 2
        
        board_left = ship_pool_left + SHIP_POOL_WIDTH + BOARD_SEPARATION_TO_SHIPS
        self.draw_ship_pool(ship_pool_left, ship_pool_top)
        self.main_screen.draw_board(board_left,0)
    
    def draw_ship_pool(self, left, top):
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(left, top, SHIP_POOL_WIDTH, SHIP_POOL_HEIGHT), width=1)

