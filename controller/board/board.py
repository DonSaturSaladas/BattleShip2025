
from cell import *
from views.view_constants import *
from factories.sprite import Sprite
from views.cellObserver import cellObserver


class Board:
    def __init__(self):
        self.cells = []
        self.createBoard()
    
    def createBoard(self):
        sprites = [Sprite(WATER_PATH)]
        
        for row in range(ROWS):
            self.cells.append([])
            for col in range(COLS):
                self.board[row].append(Cell(row, col, sprites))

            
    def getCell(self, x, y):
        return self.cells[x][y]
    
    