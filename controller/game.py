from .player_entities import *
from .player_entities.player_entity import Player_Entity
from .player_entities.player import Player
from .factories.ship_factory import Ship_factory
from views.view_constants import ROWS, COLS
from views.cell_Observer import Cell_Observer



class Game:
    def __init__(self, main_screen):
        self.player = Player()
        # self.opponent_ai = Opponent_ai()
        self.main_screen = main_screen
        self.setBoardCellsObserver()
        self.ship_factory = Ship_factory()
        
    def setBoardCellsObserver(self):
        """'creates the observers of the cells and attaches them to their respective cells"""
        for row in range(ROWS):
            for col in range(COLS):
                cell = self.player.board.getCell(row, col)
                cell.registerObserver(Cell_Observer(self.main_screen ,cell))

    def create_ship(self, player_entity:Player_Entity, cells:[]):
        ship = self.ship_factory.create_ship(cells)
        player_entity.put_ship(ship)
        

