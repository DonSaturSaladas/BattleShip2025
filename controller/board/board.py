
from cell import *
from views.view_constants import *


class Board:
    def __init__(self):
        self.cells = []
        self.createBoard()
    
    def createBoard(self):
        for row in range(ROWS):
            self.cells.append([])
            for col in range(COLS):
                self.board[row].append(Cell( row, col))
            
            
    def getCell(self, x, y):
        return self.cells[x][y]
    
    