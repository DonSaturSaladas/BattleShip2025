import pygame
from .view_constants import *
from pygame.locals import *

class ShipSetupScreen:
    def __init__(self, window, main_screen):
        self.window = window
        self.main_screen = main_screen
        self.scaled_cell_size = main_screen.scaled_cell_size
        self.ship_pool_coordinates = self.get_ship_pool_coordinates()
        self.board_coodinates = self.get_board_coordinates()
        self.selected_ship = None
    
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
            elif self.ship_pool_clicked(mouse_x, mouse_y):
                print("Clicked ship pool")
        
    def board_clicked(self, coordinate_x, coordinate_y):
        return coordinate_x >= self.board_coodinates[0] and coordinate_x <= self.board_coodinates[0] + ROWS * self.scaled_cell_size

    def get_pressed_cell(self, coordinate_x, coordinate_y):
        board_x = int((coordinate_x - self.board_coodinates[0]) // self.scaled_cell_size)
        board_y = int(coordinate_y // self.scaled_cell_size)
        return (board_x, board_y)
    
    def ship_pool_clicked(self, coordinate_x, coordinate_y):
        x_on_ship_pool = coordinate_x >= self.ship_pool_coordinates[0] and coordinate_x <= self.ship_pool_coordinates[0] + SHIP_POOL_WIDTH * self.scaled_cell_size
        y_on_ship_pool = coordinate_y >= self.ship_pool_coordinates[1] and coordinate_y <= self.ship_pool_coordinates[1] + SHIP_POOL_HEIGHT * self.scaled_cell_size
        return x_on_ship_pool and y_on_ship_pool


    def draw_setup_screen(self):

        self.draw_ship_pool(self.ship_pool_coordinates[0], self.ship_pool_coordinates[1])
        self.draw_ships()

        self.main_screen.draw_board(self.board_coodinates[0], self.board_coodinates[1])

    def get_ship_setup_width(self):
        return ROWS * self.scaled_cell_size + BOARD_SEPARATION_TO_SHIPS + SHIP_POOL_WIDTH * self.scaled_cell_size
    
    def get_ship_pool_coordinates(self):
        used_width = self.get_ship_setup_width()
        return ((self.main_screen.screen_width - used_width) / 2, (self.main_screen.screen_height - SHIP_POOL_HEIGHT * self.scaled_cell_size) / 2)
    
    def get_board_coordinates(self):
        return (self.ship_pool_coordinates[0] + SHIP_POOL_WIDTH * self.scaled_cell_size + BOARD_SEPARATION_TO_SHIPS,
                (self.main_screen.screen_height - COLS * self.scaled_cell_size) / 2)

    def draw_ship_pool(self, left, top):
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(left, top, SHIP_POOL_WIDTH * self.scaled_cell_size, SHIP_POOL_HEIGHT * self.scaled_cell_size), width=1)
    
    def draw_ships(self):
        self.main_screen.draw_ship(5, self.ship_pool_coordinates[0] + self.scaled_cell_size, self.ship_pool_coordinates[1], (94, 100, 114))
        self.main_screen.draw_ship(4, self.ship_pool_coordinates[0] + 3 * self.scaled_cell_size / 2, self.ship_pool_coordinates[1] + 3 * self.scaled_cell_size / 2, (255,166,158))
        self.main_screen.draw_ship(3, self.ship_pool_coordinates[0] + 2 * self.scaled_cell_size, self.ship_pool_coordinates[1] + 3 * self.scaled_cell_size, (240,247,244))
        self.main_screen.draw_ship(3, self.ship_pool_coordinates[0] + 2 * self.scaled_cell_size, self.ship_pool_coordinates[1] + 9 * self.scaled_cell_size / 2, (13, 6, 48))
        self.main_screen.draw_ship(2, self.ship_pool_coordinates[0] + 5 * self.scaled_cell_size / 2, self.ship_pool_coordinates[1] + 6 * self.scaled_cell_size, (88,153,226))
    
    def screen_size_changed(self):
        self.scaled_cell_size = self.main_screen.scaled_cell_size
        self.ship_pool_coordinates = self.get_ship_pool_coordinates()
        self.board_coodinates = self.get_board_coordinates()

    
