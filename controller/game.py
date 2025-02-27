from .player_entities.player import Player
from views.view_constants import ROWS, COLS
from views.cell_Observer import Cell_Observer


class Game:
    def __init__(self, main_screen):
        self.player = Player()
        self.main_screen = main_screen
        self.setBoardCellsObserver()

    def setBoardCellsObserver(self):
        """'creates the observers of the cells and attaches them to their respective cells"""
        for row in range(ROWS):
            for col in range(COLS):
                cell = self.player.board.getCell(row, col)
                cell.registerObserver(Cell_Observer(self.main_screen ,cell))

