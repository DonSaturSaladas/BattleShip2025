from abc import ABC, abstractmethod
from controller.board_elements.cell import Cell

class Ship():
    
    def __init__(self): 
        self.parts: list[Cell]  = []
        
        
    def init_ship(self):
        for cell in self.parts:
            cell.update()
        
        