
from .cell import *
from views.view_constants import *
from controller.factories.sprite import Sprite


class Board:
    '''Is the logic representation of the board'''
    def __init__(self):
        self.cells = []
        self.createBoard()
    
    def createBoard(self):
        sprites = [Sprite(WATER_PATH), Sprite()]
        
        for row in range(ROWS):
            self.cells.append([])
            for col in range(COLS):
                self.cells[row].append(Cell(row, col, sprites))

            
    def getCell(self, x, y):
        return self.cells[x][y]
    
    
