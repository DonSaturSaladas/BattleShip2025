import pygame
from .view_constants import *
from pygame.locals import *

class ShipSetupScreen:
    def __init__(self, window, main_screen):
        self.window = window
        self.main_screen = main_screen
        self.ship_pool_coordinates = self.get_ship_pool_coordinates()
        self.board_coodinates = self.get_board_coordinates()
    
    def run(self):
        self.draw_setup_screen()
    
    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.mouse_clicked(event)
        
    def mouse_clicked(self, event):
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        if event.button == 1:    #Left Click
            if self.board_clicked(mouse_x, mouse_y):
                pressed_cell_coordinates = self.get_pressed_cell(mouse_x, mouse_y)
                print(pressed_cell_coordinates)
        
    def board_clicked(self, coordinate_x, coordinate_y):
        return coordinate_x >= self.board_coodinates[0] and coordinate_x <= self.board_coodinates[0] + BOARD_WIDTH * CELL_SIZE

    def get_pressed_cell(self, coordinate_x, coordinate_y):
        board_x = int((coordinate_x - self.board_coodinates[0]) // CELL_SIZE)
        board_y = int(coordinate_y // CELL_SIZE)
        return (board_x, board_y)

    def draw_setup_screen(self):

        self.draw_ship_pool(self.ship_pool_coordinates[0], self.ship_pool_coordinates[1])

        self.main_screen.draw_board(self.board_coodinates[0], self.board_coodinates[1])

    def get_ship_setup_width(self):
        return BOARD_WIDTH * CELL_SIZE + BOARD_SEPARATION_TO_SHIPS + SHIP_POOL_WIDTH
    
    def get_ship_pool_coordinates(self):
        used_width = self.get_ship_setup_width()
        return ((SCREEN_WIDTH - used_width) / 2, (SCREEN_HEIGHT - SHIP_POOL_HEIGHT) / 2)

    def draw_ships(self, pool_left, pool_top):
        pass
    
    def get_board_coordinates(self):
        return (self.ship_pool_coordinates[0] + SHIP_POOL_WIDTH + BOARD_SEPARATION_TO_SHIPS, 0)

    def draw_ship_pool(self, left, top):
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(left, top, SHIP_POOL_WIDTH, SHIP_POOL_HEIGHT), width=1)

