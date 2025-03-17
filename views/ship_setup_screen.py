import pygame
from views.view_constants import *
from pygame.locals import *


class ShipSetupScreen:
    def __init__(self, window, main_screen):
        self.window = window
        self.main_screen = main_screen
        self.scaled_cell_size = main_screen.scaled_cell_size
        self.ship_pool_coordinates = self.get_ship_pool_coordinates()
        self.board_coodinates = self.get_board_coordinates()
        self.ship_placeholders = self.get_ship_placeholders()
        self.buttons = []
        self.selected_ship = None
        self.ships_on_board = []
        self.selected_offset_x = 0
        self.selected_offset_y = 0
        
    
    def run(self):
        self.draw_setup_screen()

    def draw_setup_screen(self):
        self.main_screen.draw_board(self.board_coodinates[0], self.board_coodinates[1])
        self.draw_ship_pool(self.ship_pool_coordinates[0], self.ship_pool_coordinates[1])
        self.draw_ships()
        self.draw_acept_button()

    def draw_ship_pool(self, left, top):
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(left, top, SHIP_POOL_WIDTH * self.scaled_cell_size, SHIP_POOL_HEIGHT * self.scaled_cell_size), width=1)
    
    def draw_ships(self):
        pygame.draw.rect(self.window, (94, 100, 114), self.ship_placeholders[0][2])
        pygame.draw.rect(self.window, (255,166,158), self.ship_placeholders[1][2])
        pygame.draw.rect(self.window, (240,247,244), self.ship_placeholders[2][2])
        pygame.draw.rect(self.window, (13, 6, 48), self.ship_placeholders[3][2])
        pygame.draw.rect(self.window, (88,153,226), self.ship_placeholders[4][2])
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_clicked(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouse_released(event)
        elif event.type == pygame.MOUSEMOTION:
            if self.selected_ship:
                self.selected_ship.x = event.pos[0] + self.selected_offset_x
                self.selected_ship.y = event.pos[1] + self.selected_offset_y
        
    def mouse_clicked(self, event):
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        if event.button == 1:    #Left Click
            self.selected_ship = self.get_ship_clicked(mouse_x, mouse_y)
            if self.selected_ship:
                if self.selected_ship in self.ships_on_board:
                    self.ships_on_board.remove(self.selected_ship)
                self.selected_offset_x = -self.scaled_cell_size / 2
                self.selected_offset_y = -self.scaled_cell_size / 2
            
            if(len(self.ship_placeholders) ==  len(self.ships_on_board)):
                self.handle_acept_button_clicked(mouse_x, mouse_y)
                        
        elif self.selected_ship and event.button == 3: #Middle Click
            self.change_ship_orientation(self.selected_ship)
    
    
    def handle_acept_button_clicked(self, mouse_x, mouse_y):
       if self.buttons[0].collidepoint(mouse_x, mouse_y): #If click acept button
           
            for placeholder in self.ships_on_board:
                print((int)(placeholder.width /self.scaled_cell_size))
                ship_cells = []
                # Nos quedamos con el valor mas grande para saber la orientacion
                orientation = "H" if placeholder.width > placeholder.height else "V"
                lenght = (int) (placeholder.width / self.scaled_cell_size )if placeholder.width > placeholder.height else (int)(placeholder.height/self.scaled_cell_size)
                current_placeholder_x = placeholder.x
                current_placeholder_y = placeholder.y
                for i in range(lenght):
                    print(self.get_pressed_cell(current_placeholder_x,current_placeholder_y))
                    ship_cells.append(self.get_pressed_cell(current_placeholder_x,current_placeholder_y))
                    
                    if orientation == "H":
                        current_placeholder_x += self.scaled_cell_size
                    else:
                        current_placeholder_y += self.scaled_cell_size
                    
                self.main_screen.game.create_ship(self.main_screen.game.player ,ship_cells)

                # self.main_screen.change_screen("Game")

                        
        
    def change_ship_orientation(self, selected_ship):
        temp_width = selected_ship.width
        selected_ship.width = selected_ship.height
        selected_ship.height = temp_width
                
    def get_ship_clicked(self, coordinate_x, coordinate_y):
        ship_found = None
        ship_index = 0
        while not ship_found and ship_index < 5:
            ship = self.ship_placeholders[ship_index][2]
            if ship.collidepoint(coordinate_x, coordinate_y):
                ship_found = ship
            ship_index += 1
        return ship_found
                
    def mouse_released(self, event):
        if event.button == 1 and self.selected_ship is not None:
            if self.board_clicked(event.pos[0], event.pos[1]):
                board_coordinates = self.get_pressed_cell_coords(event.pos[0], event.pos[1])
                new_x = self.board_coodinates[0] + board_coordinates[0] * self.scaled_cell_size
                new_y = self.board_coodinates[1] + board_coordinates[1] * self.scaled_cell_size
            
                if not self.check_colission(self.selected_ship) and not self.ship_out_of_board(self.selected_ship):
                    self.selected_ship.x = new_x
                    self.selected_ship.y = new_y
                    self.ships_on_board.append(self.selected_ship)
                    self.selected_ship = None
                else:
                    self.return_ship_to_pool(self.selected_ship)
            else:
                self.return_ship_to_pool(self.selected_ship)
    
    
    def check_colission(self, rect):
        collision = False
        for ship in self.ships_on_board:
            if rect.colliderect(ship):
                    collision = True
                    break
        return collision

    def ship_out_of_board(self, ship):
        return ship.x + ship.width > self.board_coodinates[0] + (ROWS + 1/2) * self.scaled_cell_size or ship.y + ship.height > self.board_coodinates[1] + (COLS + 1/2) * self.scaled_cell_size
                
    def board_clicked(self, coordinate_x, coordinate_y):
        return coordinate_x >= self.board_coodinates[0] and coordinate_y <= self.board_coodinates[0] + ROWS * self.scaled_cell_size

    def get_pressed_cell_coords(self, coordinate_x, coordinate_y):
        board_x = int((coordinate_x - self.board_coodinates[0]) // self.scaled_cell_size)
        board_y = int(coordinate_y // self.scaled_cell_size)
        return (board_x, board_y)
    
    def get_pressed_cell(self, screen_x, screen_y):
        x, y = self.get_pressed_cell_coords(screen_x,screen_y)
        return self.main_screen.game.player.getBoard().getCell(x,y)

    def return_ship_to_pool(self, ship):
        coordinates = self.get_ship_base_coordinates(ship)
        self.return_ship_to_base_coordinates(coordinates)
        self.set_ship_horizontally(ship)
        self.selected_ship = None
    
    def return_ship_to_base_coordinates(self, coordinates):
        self.selected_ship.x = coordinates[0]
        self.selected_ship.y = coordinates[1]
        
    def set_ship_horizontally(self, ship):
        ship_width = self.selected_ship.width
        ship_height = self.selected_ship.height
        if ship_width < ship_height:
            self.selected_ship.width = ship_height
            self.selected_ship.height = ship_width

    
    def get_ship_base_coordinates(self, ship):
        found_ship = False
        ship_index = 0
        while not found_ship and ship_index < 4:
            if self.ship_placeholders[ship_index][2] == ship:
                found_ship = True
            else:
                ship_index += 1
        return (self.ship_placeholders[ship_index][0], self.ship_placeholders[ship_index][1])
    
    
    
    def ship_pool_clicked(self, coordinate_x, coordinate_y):
        x_on_ship_pool = coordinate_x >= self.ship_pool_coordinates[0] and coordinate_x <= self.ship_pool_coordinates[0] + SHIP_POOL_WIDTH * self.scaled_cell_size
        y_on_ship_pool = coordinate_y >= self.ship_pool_coordinates[1] and coordinate_y <= self.ship_pool_coordinates[1] + SHIP_POOL_HEIGHT * self.scaled_cell_size
        return x_on_ship_pool and y_on_ship_pool

    def screen_size_changed(self):
        self.scaled_cell_size = self.main_screen.scaled_cell_size
        self.ship_pool_coordinates = self.get_ship_pool_coordinates()
        self.board_coodinates = self.get_board_coordinates()

    def get_ship_setup_width(self):
        return ROWS * self.scaled_cell_size + BOARD_SEPARATION_TO_SHIPS + SHIP_POOL_WIDTH * self.scaled_cell_size
    
    def get_ship_pool_coordinates(self):
        used_width = self.get_ship_setup_width()
        return ((self.main_screen.screen_width - used_width) / 2, (self.main_screen.screen_height - SHIP_POOL_HEIGHT * self.scaled_cell_size) / 2)
    
    def get_board_coordinates(self):
        return (self.ship_pool_coordinates[0] + SHIP_POOL_WIDTH * self.scaled_cell_size + BOARD_SEPARATION_TO_SHIPS,
                (self.main_screen.screen_height - COLS * self.scaled_cell_size) / 2)
    
    def get_ship_placeholders(self):
        """[0] y [1] contienen la posicion original del placeholder"""
        pool_x = self.ship_pool_coordinates[0]
        pool_y = self.ship_pool_coordinates[1]
        cell_size = self.scaled_cell_size
        
        return [
            [pool_x + self.scaled_cell_size, pool_y, pygame.Rect(pool_x + self.scaled_cell_size, pool_y, 5 * self.scaled_cell_size, self.scaled_cell_size)],
            [pool_x + 3 * self.scaled_cell_size / 2, pool_y + 3 * self.scaled_cell_size / 2, pygame.Rect(pool_x + 3 * self.scaled_cell_size / 2, pool_y + 3 * self.scaled_cell_size / 2, 4 * self.scaled_cell_size, self.scaled_cell_size)],
            [pool_x + 2 * self.scaled_cell_size, pool_y + 3 * self.scaled_cell_size, pygame.Rect(pool_x + 2 * self.scaled_cell_size, pool_y + 3 * self.scaled_cell_size, 3 * self.scaled_cell_size, self.scaled_cell_size)],
            [pool_x + 2 * self.scaled_cell_size, pool_y + 9 * self.scaled_cell_size / 2, pygame.Rect(pool_x + 2 * self.scaled_cell_size, pool_y + 9 * self.scaled_cell_size / 2, 3 * self.scaled_cell_size, self.scaled_cell_size)],
            [pool_x + 5 * self.scaled_cell_size / 2, pool_y + 6 * self.scaled_cell_size, pygame.Rect(pool_x + 5 * self.scaled_cell_size / 2, pool_y + 6 * self.scaled_cell_size, 2 * self.scaled_cell_size, self.scaled_cell_size)]
        ]
        


    def draw_acept_button(self):
        poolX = self.get_board_coordinates()[0]
        poolY = self.get_board_coordinates()[1]
        button = pygame.Rect(poolX +self.scaled_cell_size*ROWS + 2, poolY, 70, 50)
        pygame.draw.rect(self.window, (255, 255, 255), button)
        
        text_surface_object = self.main_screen.PRIMARY_FONT.render("Start", True, (0,0,0))
        text_rect = text_surface_object.get_rect(center = button.center)
        self.window.blit(text_surface_object, text_rect)
        self.buttons.append(button)
        