import pygame
from .ship_setup_screen import ShipSetupScreen
from .view_constants import *

class MainScreen():
    def __init__(self, window):
        self.running = True
        self.window = window
        self.ship_setup_screen = ShipSetupScreen(window, self)
        self.selected_screen = self.ship_setup_screen
        self.scale_factor = 1

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                if event.type == pygame.RESIZABLE:
                    nWidth, nHeight = event.w, event.h
                    self.scale_factor = nWidth /SCREEN_WIDTH
                self.selected_screen.handle_event(event)
                
        self.selected_screen.run()
        pygame.display.update()

    def is_running(self):
        return self.running
    
    def draw_board(self, left, top):
        scaled_cell_size = int(CELL_SIZE * self.scale_factor)

        board_width = BOARD_WIDTH * scaled_cell_size
        board_height = BOARD_HEIGHT * scaled_cell_size
        
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(left, top, board_width, board_width), width=1)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(self.window, (255,255,255), pygame.Rect(row*scaled_cell_size+left, col*CELL_SIZE+top,scaled_cell_size, scaled_cell_size), width=1)
        pygame.display.update()
    


