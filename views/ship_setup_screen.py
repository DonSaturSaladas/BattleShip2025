import pygame
from .view_constants import *
from pygame.locals import *

class ShipSetupScreen:
    def __init__(self, window, main_screen):
        self.window = window
        self.main_screen = main_screen
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
        return coordinate_x >= self.board_coodinates[0] and coordinate_x <= self.board_coodinates[0] + BOARD_WIDTH * CELL_SIZE

    def get_pressed_cell(self, coordinate_x, coordinate_y):
        board_x = int((coordinate_x - self.board_coodinates[0]) // CELL_SIZE)
        board_y = int(coordinate_y // CELL_SIZE)
        return (board_x, board_y)
    
    def ship_pool_clicked(self, coordinate_x, coordinate_y):
        x_on_ship_pool = coordinate_x >= self.ship_pool_coordinates[0] and coordinate_x <= self.ship_pool_coordinates[0] + SHIP_POOL_WIDTH
        y_on_ship_pool = coordinate_y >= self.ship_pool_coordinates[1] and coordinate_y <= self.ship_pool_coordinates[1] + SHIP_POOL_HEIGHT
        return x_on_ship_pool and y_on_ship_pool


    def draw_setup_screen(self):

        self.draw_ship_pool(self.ship_pool_coordinates[0], self.ship_pool_coordinates[1])
        self.draw_ships()

        self.main_screen.draw_board(self.board_coodinates[0], self.board_coodinates[1])

    def get_ship_setup_width(self):
        return BOARD_WIDTH * CELL_SIZE + BOARD_SEPARATION_TO_SHIPS + SHIP_POOL_WIDTH
    
    def get_ship_pool_coordinates(self):
        used_width = self.get_ship_setup_width()
        return ((SCREEN_WIDTH - used_width) / 2, (SCREEN_HEIGHT - SHIP_POOL_HEIGHT) / 2)
    
    def get_board_coordinates(self):
        return (self.ship_pool_coordinates[0] + SHIP_POOL_WIDTH + BOARD_SEPARATION_TO_SHIPS, 0)

    def draw_ship_pool(self, left, top):
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(left, top, SHIP_POOL_WIDTH, SHIP_POOL_HEIGHT), width=1)
    
    def draw_ships(self):
        self.main_screen.draw_ship(5, self.ship_pool_coordinates[0] + CELL_SIZE, self.ship_pool_coordinates[1], (94, 100, 114))
        self.main_screen.draw_ship(4, self.ship_pool_coordinates[0] + 3 * CELL_SIZE / 2, self.ship_pool_coordinates[1] + 3 * CELL_SIZE / 2, (255,166,158))
        self.main_screen.draw_ship(3, self.ship_pool_coordinates[0] + 2 * CELL_SIZE, self.ship_pool_coordinates[1] + 3 * CELL_SIZE, (240,247,244))
        self.main_screen.draw_ship(3, self.ship_pool_coordinates[0] + 2 * CELL_SIZE, self.ship_pool_coordinates[1] + 9 * CELL_SIZE / 2, (13, 6, 48))
        self.main_screen.draw_ship(2, self.ship_pool_coordinates[0] + 5 * CELL_SIZE / 2, self.ship_pool_coordinates[1] + 6 * CELL_SIZE, (88,153,226))

