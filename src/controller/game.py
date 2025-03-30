import random
import pygame
from .player_entities import *

from .factories.ship_factory import Ship_factory
from views.view_constants import ROWS, COLS
from views.cell_Observer import Cell_Observer
from controller.board_elements.cell import Cell

from .ships.carrier import Carrier



class Game:
    def __init__(self, main_screen):
        self.ship_factory = Ship_factory()
        self.player = Player()
        self.opponent_ai = Opponent_ai(self)
        self.main_screen = main_screen
        self.setBoardCellsObserver()
        
        self.randomize_float(self.opponent_ai)
        self.current_player = self.opponent_ai
        self.opponent_ai.board.print_board()
        
        self.turn  = 1
        
    def setBoardCellsObserver(self):
        """'creates the observers of the cells and attaches them to their respective cells"""
        for row in range(ROWS):
            for col in range(COLS):
                player_cell = self.player.board.getCell(row, col)
                player_cell.registerObserver(Cell_Observer(self.main_screen , player_cell))
                enemy_cell = self.opponent_ai.board.getCell(row, col)
                enemy_cell.registerObserver(Cell_Observer(self.main_screen , enemy_cell))

    def create_ship(self, player_entity:Player_Entity, cells:list[Cell]):
        if issubclass(Carrier,self.player.ships.__class__):
            ship = self.ship_factory.create_ship(cells, "Submarine")
            print("submarine printed")
        else:
            ship = self.ship_factory.create_ship(cells)
        player_entity.put_ship(ship)
        
    def randomize_float(self, player_entity):
        carrier5 = [None,None,None,None,None]
        battleship4 =[None,None,None,None]
        cruiser3 = [None,None,None]
        submarine3 = [None,None,None]
        destroyer2 = [None,None]
        
        ships = [carrier5, battleship4, cruiser3, submarine3, destroyer2]
        
        for ship in ships:
            self.opponent_ai.board.print_board()
            print()
            self.randomize_ship_pos(player_entity, ship)
            
    def randomize_ship_pos(self, player_entity, ship_array):
        valid_first_cell = False
        while not valid_first_cell:
            first_cell = self.generate_random_coords(player_entity)
            orientation = random.choice(["v", "h"])
            valid_first_cell = self.check_first_cell(first_cell, orientation, len(ship_array), player_entity)

        for i in range(len(ship_array)):
            if orientation == "v":
                ship_array[i] = player_entity.board.getCell(first_cell[0], first_cell[1] + i)
            elif orientation == "h":
                ship_array[i] = player_entity.board.getCell(first_cell[0] + i, first_cell[1])
        
        self.create_ship(player_entity, ship_array)
    
    def check_first_cell(self, first_cell_coords, orientation, ship_lenght, player_entity):
        is_valid = False
        if self.ship_size_on_board(first_cell_coords, orientation, ship_lenght):
            is_valid = True
            if orientation == "v":
                for i in range(ship_lenght):
                    cell = player_entity.board.getCell(first_cell_coords[0], first_cell_coords[1] + i)
                    if cell.hasShip:
                        is_valid = False
                        break
            elif orientation == "h":
                for i in range(ship_lenght):
                    cell = player_entity.board.getCell(first_cell_coords[0] + i, first_cell_coords[1])
                    if cell.hasShip:
                        is_valid = False
                        break
        return is_valid
    
    def ship_size_on_board(self, first_cell_coords, orientation, ship_lenght):
        is_on_board = True
        if orientation == "h":
            is_on_board = first_cell_coords[0] + ship_lenght < ROWS
        elif orientation == "v":
            is_on_board = first_cell_coords[1] + ship_lenght < COLS
        return is_on_board


    def generate_random_coords(self, player):
        
        random_coords = random.randint(0, ROWS - 1) , random.randint(0, COLS - 1)

        
        while player.board.getCell(random_coords[0],random_coords[1]).hasShip:
            random_coords = (random.randint(0, ROWS - 1) , random.randint(0, COLS - 1))
            
        return random_coords

    def run_game(self):
        self.current_player.play()
        if(self.player.remaining_ships <= 0 or self.opponent_ai.remaining_ships<=0):
            self.main_screen.change_screen("Menu") #TODO: Change for Game over screen and do this there
            self.restart_game()
            
    
    def change_current_player(self):
        if self.current_player == self.player:
            self.current_player = self.opponent_ai
        else:
            self.current_player = self.player

    def get_current_oposite_player(self):
        player = None
        if self.current_player == self.player:
            player = self.opponent_ai
        else:
            player = self.player
            
        return player
    
    def restart_game(self):
        self.main_screen.setup_screens()
        self.main_screen.set_game(Game(self.main_screen))
        