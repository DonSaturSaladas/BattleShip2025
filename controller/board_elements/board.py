
from .cell import *
from views.view_constants import *
from controller.factories.sprite import Sprite


class Board:
    '''Is the logic representation of the board'''
    def __init__(self):
        self.cells = []
        self.createBoard()
    
    def createBoard(self):
        sprites = [Sprite(WATER_PATH), Sprite(CROSS_PATH)]
        
        for row in range(ROWS):
            self.cells.append([])
            for col in range(COLS):
                self.cells[row].append(Cell(col, row, sprites))

    def getCell(self, x, y):
        return self.cells[y][x]

    def shoot_cell(self, cell):
        cell.selected()
    
    #debug method
    def print_board(self):
        for row in self.cells:
            row_str = ""
            for col in row:
                row_str += "S " if col.hasShip else "W "
                
            print(row_str)
    
