import pygame
from .ship_setup_screen import ShipSetupScreen
from .view_constants import *

class MainScreen():
    def __init__(self, window):
        self.running = True
        self.window = window
        self.ship_setup_screen = ShipSetupScreen(window, self)
        self.selected_screen = self.ship_setup_screen

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.selected_screen.run()
        pygame.display.update()

    def is_running(self):
        return self.running
    
    def draw_board(self, left, top):
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(left, top, BOARD_WIDTH * CELL_SIZE, BOARD_HEIGHT * CELL_SIZE), width=1)


