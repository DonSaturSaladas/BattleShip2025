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
        self.opponent_ai = Player()
        self.main_screen = main_screen
        self.setBoardCellsObserver()
        self.ship_factory = Ship_factory()
        
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
        

