import random

from .player_entities import *
from .player_entities.player_entity import Player_Entity
from .player_entities.player import Player
from .factories.ship_factory import Ship_factory
from views.view_constants import ROWS, COLS
from views.cell_Observer import Cell_Observer
from controller.board_elements.cell import Cell

from .ships.carrier import Carrier



class Game:
    def __init__(self, main_screen):
        self.player = Player()
        self.opponent_ai = Player(self)
        self.main_screen = main_screen
        self.setBoardCellsObserver()
        self.ship_factory = Ship_factory()
        self.current_player = self.player
        
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
        
    def init_ai_float():
        carrier5 = [None,None,None,None,None]
        battleship4 =[None,None,None,None]
        cruiser3 = [None,None,None]
        submarine3 = [None,None,None]
        destroyer2 = [None,None]
        
        ships = [carrier5, battleship4, cruiser3, submarine3, destroyer2]
        
        for ship in ships:
            self.randomize_ship_pos(ship)
            
    def randomize_ship_pos(ship_array):
        
        for 
        
            
    def generate_random_coords(self, player):
        
        random_coords = random.randint(0, ROWS) , random.randint(0, COLS)

        
        while not player.board.getCell(random_coords[0],random_coords[1]).has_ship:
            random_coords = random.randint(0, ROWS) , random.randint(0, COLS)
            
        return random_coords

    def run_game(self):
        self.current_player.play()
            
    
    def change_current_player(self):
        if self.current_player == self.player:
            self.current_player = self.opponent_ai
        else:
            self.current_player = self.player

    def get_current_player(self):
        return self.current_player
    